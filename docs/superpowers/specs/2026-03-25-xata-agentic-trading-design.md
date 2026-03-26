# XATA Agentic Trading — Design Spec

**Date:** 2026-03-25
**Status:** Draft
**Version:** 0.1.0

## Overview

A Claude Code skill plugin that enables users to trade on decentralized exchanges via XATA's Trading API using natural language. Claude handles wallet setup, venue binding, and trade execution on behalf of the user.

**Supported platforms (v0.1.0):** Hyperliquid, Lighter, Aster

## File Structure

```
plugins/xata-agentic-trading/
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   └── xata-trading/
│       ├── SKILL.md
│       ├── xata-wallet.py
│       └── requirements.txt
└── README.md
```

The Python helper script lives inside the skill directory (not a separate `scripts/` directory) to ensure it is distributed with the plugin when installed from the marketplace.

### plugin.json

Standard plugin manifest. Name: `xata-agentic-trading`, version `0.1.0`. Declares one skill only — no commands, agents, or hooks.

### xata-wallet.py

Python helper script for EVM wallet operations. Dependencies listed in `requirements.txt`: `eth_account`, `requests`.

Two subcommands, all output JSON to stdout:

| Subcommand | Purpose | Output |
|------------|---------|--------|
| `generate --wallet-file ~/.xata-claude/wallet.json` | Create new EVM wallet, save to file (mode 0600). Only outputs address, never private key. | `{"address": "0x..."}` |
| `register --wallet-file ~/.xata-claude/wallet.json` | Full registration: generate nonce (`int(time.time() * 1000)`) → construct message `"Register XATA: {nonce}"` → sign with EIP-191 → POST `/v2/account/register` | `{"api_key": "api_...", "wallet_address": "0x..."}` |

**Security:**
- Private keys are never passed as CLI arguments — the script reads them from the wallet file to avoid exposure in process lists and shell history.
- The `generate` command only outputs the address to stdout, never the private key — prevents key leakage into the LLM context window or conversation logs.

### SKILL.md

Core skill file. Frontmatter:

```yaml
---
name: xata-trading
description: Trade on decentralized exchanges via XATA API — setup wallets, bind venues, and execute trades
allowed-tools: Bash, Read, Write, WebFetch, AskUserQuestion
---
```

The skill is invoked as `xata-trading` (not `xata-agentic-trading` — the plugin name and skill name differ intentionally; the plugin is the package, the skill is the interface).

## Authentication

All API calls to XATA require the header:

```
x-api-key: <api_key>
```

Where `<api_key>` is the value stored in `~/.xata-claude/config.json`. This header is required for every request to `https://api.x.ata.network` except the initial `/v2/account/register` call.

## Local Data Storage

Path: `~/.xata-claude/`

All files in this directory are created with mode `0600` (owner read/write only) to protect sensitive data.

**wallet.json** — Management wallet (used only for API key lifecycle, not for holding funds):
```json
{
  "address": "0x...",
  "private_key": "0x..."
}
```

**config.json** — Runtime configuration:
```json
{
  "api_key": "api_1a2b3c...",
  "api_base": "https://api.x.ata.network",
  "venues": {
    "hyperliquid": {"status": "active", "bound_at": "2026-03-25T..."}
  },
  "settings": {
    "confirm_before_trade": true
  }
}
```

## Skill Logic

### Entry Point — State Detection

When the skill is triggered, Claude checks `~/.xata-claude/config.json`:

| State | Action |
|-------|--------|
| File missing or no `api_key` | → Setup Flow |
| `api_key` exists but target venue not in `venues` | → Venue Binding Flow |
| `api_key` exists and target venue active | → Trading Flow |

### Setup Flow

1. **Check Python environment** — verify `eth_account` and `requests` are installed. If not, prompt user to install: `pip install -r skills/xata-trading/requirements.txt`.
2. **Generate management wallet** — run `python skills/xata-trading/xata-wallet.py generate`. The script creates `~/.xata-claude/wallet.json` with mode 0600. Inform user this wallet is for API key management only.
3. **Register API Key** — run `python skills/xata-trading/xata-wallet.py register --wallet-file ~/.xata-claude/wallet.json`. The script internally: generates nonce from current timestamp (ms), constructs message `"Register XATA: {nonce}"`, signs with EIP-191, POSTs to `/v2/account/register`. Write returned `api_key` to `~/.xata-claude/config.json` (mode 0600).

### Venue Binding Flow

**Trigger:** Active (user says "bind Hyperliquid") or passive (user wants to trade on unbound venue).

Three venue types for v0.1.0:

#### Hyperliquid — Backend-Generated Agent Wallet

> **Note:** The Hyperliquid venue setup API is being redesigned. The current API requires Privy wallet parameters (`privy_wallet_id`, `wallet_address`), but this flow will be simplified. The spec describes the target flow; exact endpoint parameters should be fetched via WebFetch at implementation time to get the latest version.

1. Claude calls the venue setup endpoint with `x-api-key` header.
2. Backend returns agent wallet address + user-facing instructions.
3. Claude shows instructions to user (how to approve the agent wallet on Hyperliquid).
4. User confirms completion → Claude calls `GET /v2/venues` to verify the venue appears with status "active" → updates `config.json`.

#### Aster — Prepare + Confirm

1. Claude calls `POST /v2/venue/prepare` with `{"venue": "aster"}` and `x-api-key` header → receives generated keypair + instructions.
2. Claude shows instructions: user must register the generated address in Aster's API wallet page.
3. User confirms completion → Claude calls `POST /v2/venue/confirm` with `{"venue": "aster", "main_wallet_address": "0x..."}`.
4. Claude calls `GET /v2/venues` to verify status → updates `config.json`.

#### Lighter — User-Provided Credentials

1. Claude shows instructions: how to obtain credentials from Lighter (api_key_private_key, api_key_index, account_index, l1_address).
2. User provides credentials.
3. Claude calls `POST /v2/venue/credentials` with the credentials payload + `x-api-key` header.
4. Claude calls `GET /v2/venues` to verify status → updates `config.json`.

**What is hardcoded vs. dynamic:** The endpoint path patterns (e.g., `/v2/venue/prepare`, `/v2/{platform}/order`) are stable API contracts and are hardcoded in the skill. Venue-specific request body parameters (which fields each venue requires) are fetched via WebFetch from `https://docs.ata.network/xata/api/agent-access/venue-setup` at runtime to stay current.

### Trading Flow

**Step 1 — Parse user intent.** Extract from natural language: platform, operation type (order/cancel/query/balance/position), symbol, side, quantity, price, order type. Use `AskUserQuestion` for missing required parameters. When user specifies an asset without a quote currency (e.g., "buy 1 ETH"), default to USDC as quote currency; if unavailable, fall back to USDT. Use `GET /v2/{platform}/symbol-info` to validate the trading pair exists.

**Step 2 — Fetch API spec.** WebFetch the relevant documentation page from `https://docs.ata.network/xata/api` to get current endpoint parameters for the specific operation.

**Step 3 — Construct request.** Build the API request based on spec. If `confirm_before_trade` is true in config, show the full request parameters to user via `AskUserQuestion` for confirmation before sending.

**Step 4 — Execute.** Send request via `curl` with `x-api-key` header. Parse response, show result to user (fill price, quantity, order ID, etc.). On failure, show error and suggest corrections.

**Strategy engine operations** (cross-exchange arbitrage submit/query/cancel) follow the same flow: parse intent → fetch spec → construct → confirm → execute.

### API Capabilities Summary (embedded in SKILL.md)

```
Available operations:
- Query balances (single platform / aggregated), positions, funding rates
- Place orders (single / batch up to 10), cancel orders, query open orders
- Query fill history
- Market data (best bid/ask, orderbook depth, symbol info)
- Adjust leverage
- Strategy engine (cross-exchange arbitrage: submit/query/cancel)

Supported platforms (v0.1.0): Hyperliquid, Lighter, Aster

Full API reference: https://docs.ata.network/xata/api
```

### Error Handling

| Error | Action |
|-------|--------|
| API Key invalid/expired (401/403) | Prompt user to re-register via Setup Flow |
| Venue not bound | Auto-enter Venue Binding Flow |
| Trade failure (4xx/5xx) | Show HTTP status, error body, and suggest fix |
| Network error / timeout | Suggest retry |
| Missing Python deps | Prompt `pip install eth_account requests` |
| Invalid trading pair | Show available pairs from symbol-info endpoint |

### User Settings

Users adjust settings via natural language, persisted in `config.json`:

- "Don't ask me to confirm trades" → `confirm_before_trade: false`
- "Restore trade confirmation" → `confirm_before_trade: true`

### Teardown

Users can request cleanup. To discover resource IDs, Claude first calls list endpoints:

- **List API keys:** `GET /v2/api-keys` → returns array with `keyId` for each key
- **List venues:** `GET /v2/venues` → returns array with `venueId` for each bound venue

Actions:
- "Delete my API key" → `GET /v2/api-keys` to find `keyId` → `DELETE /v2/api-keys/{keyId}` → remove `config.json`
- "Unbind Hyperliquid" → `GET /v2/venues` to find `venueId` → `DELETE /v2/venues/{venueId}` → remove venue from `config.json`
- "Reset everything" → Delete API key + all venues → remove `~/.xata-claude/` directory

## marketplace.json Entry

```json
{
  "name": "xata-agentic-trading",
  "source": "./plugins/xata-agentic-trading",
  "description": "Trade on decentralized exchanges via XATA API with AI-powered natural language trading",
  "version": "0.1.0",
  "author": {"name": "Automata Network", "email": "devops@ata.network"}
}
```

## Example User Flows

### First-Time Setup + Trade

```
User: Help me buy 1 ETH on Hyperliquid
Claude: XATA not set up yet. Starting setup...
       → Checking Python dependencies... ✓
       → Generated management wallet ✓
       → Registered API Key ✓
       → Hyperliquid not bound. Starting binding...
       → Backend returned agent wallet: 0xABC...
       → Please approve this agent wallet on Hyperliquid: [instructions]
User: Done, approved.
Claude: Binding confirmed ✓ (verified via GET /v2/venues)
       → Preparing order: Market buy 1 ETH/USDC on Hyperliquid
       → Confirm execution?
User: Yes
Claude: Filled at $3,850, quantity 1 ETH
```

### Daily Usage (Already Set Up)

```
User: Check my Hyperliquid positions
Claude: [calls GET /v2/hyperliquid/position] → shows position list

User: Place a limit buy for 0.5 ETH at $3,800
Claude: Limit buy 0.5 ETH/USDC @ $3,800 on Hyperliquid. Confirm?
User: Yes
Claude: Order submitted, orderId: xxx
```

### Passive Venue Binding

```
User: Sell 100 USDC worth of ETH on Lighter
Claude: Lighter is not bound to your API key yet. Let me guide you through setup.
       → To get your Lighter credentials: [step-by-step instructions]
User: Here are my credentials: [provides them]
Claude: Credentials submitted ✓ Lighter bound. (verified via GET /v2/venues)
       → Preparing order: Market sell ~0.026 ETH on Lighter. Confirm?
```

## Decisions & Constraints

- **Python chosen** for wallet script because XATA docs use `eth_account` in examples.
- **Private keys read from file, never passed as CLI args** — prevents exposure in process lists and shell history.
- **File permissions 0600** on all files in `~/.xata-claude/` — owner-only access.
- **Script lives in skill directory** (`skills/xata-trading/xata-wallet.py`) — ensures distribution with plugin installation.
- **Endpoint paths hardcoded, body parameters dynamic** — paths are stable API contracts; venue-specific parameters fetched via WebFetch for currency.
- **Management wallet holds no funds** — only used for EIP-191 signatures to manage API keys.
- **v0.1.0 scope limited to 3 platforms** — Hyperliquid (agent wallet), Aster (prepare+confirm), Lighter (credentials). Covers all three venue setup patterns.
- **No scheduled/automated trading** — skill handles single interactive requests only.
- **Default quote currency USDC** — falls back to USDT if USDC pair unavailable.

## Future Considerations (out of scope for v0.1.0)

- **Additional platforms:** Kuru, Hyena, GRVT, Nado, Paradex
- **WebSocket support:** Real-time order updates, price feeds, position monitoring
- **Automated/scheduled trading:** Integration with Claude Code's cron capabilities
- **Rate limiting:** Respect XATA API rate limits for batch operations
