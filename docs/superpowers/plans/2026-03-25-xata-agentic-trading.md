# XATA Agentic Trading Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a Claude Code skill plugin that lets users trade on DEXes (Hyperliquid, Lighter, Aster) via XATA's Trading API using natural language.

**Architecture:** Single skill plugin with a Python helper script for EVM wallet operations. The skill (SKILL.md) contains all flow logic; the script (xata-wallet.py) handles cryptographic operations. Local storage at `~/.xata-claude/` for wallet and config.

**Tech Stack:** Python (eth_account, requests), Claude Code skill system, XATA REST API

**Spec:** `docs/superpowers/specs/2026-03-25-xata-agentic-trading-design.md`

---

## Task Dependencies

Tasks MUST be executed sequentially: 1 → 2 → 3 → 4 → 5 → 6. Each task depends on the files created by previous tasks.

## File Map

| File | Action | Responsibility |
|------|--------|----------------|
| `plugins/xata-agentic-trading/.claude-plugin/plugin.json` | Create | Plugin manifest |
| `plugins/xata-agentic-trading/skills/xata-trading/SKILL.md` | Create | Core skill — all flow logic |
| `plugins/xata-agentic-trading/skills/xata-trading/xata-wallet.py` | Create | EVM wallet generate + register (2 subcommands) |
| `plugins/xata-agentic-trading/skills/xata-trading/requirements.txt` | Create | Python dependencies |
| `plugins/xata-agentic-trading/README.md` | Create | Plugin documentation |
| `.claude-plugin/marketplace.json` | Modify | Add plugin entry |

---

### Task 1: Plugin Scaffold — plugin.json + requirements.txt + README

**Files:**
- Create: `plugins/xata-agentic-trading/.claude-plugin/plugin.json`
- Create: `plugins/xata-agentic-trading/skills/xata-trading/requirements.txt`
- Create: `plugins/xata-agentic-trading/README.md`

- [ ] **Step 1: Create directory structure**

```bash
mkdir -p plugins/xata-agentic-trading/.claude-plugin
mkdir -p plugins/xata-agentic-trading/skills/xata-trading
```

- [ ] **Step 2: Create plugin.json**

```json
{
  "name": "xata-agentic-trading",
  "version": "0.1.0",
  "description": "Trade on decentralized exchanges via XATA API with AI-powered natural language trading",
  "author": {
    "name": "Automata Network",
    "email": "devops@ata.network"
  },
  "keywords": ["trading", "defi", "xata", "hyperliquid", "aster", "lighter"]
}
```

- [ ] **Step 3: Create requirements.txt**

```
eth_account>=0.13.0,<0.15.0
requests>=2.31.0
```

- [ ] **Step 4: Create README.md**

Brief plugin overview covering: what it does, supported platforms (Hyperliquid, Lighter, Aster), prerequisites (Python 3.8+), quick start (install plugin → invoke skill → follow setup), and link to XATA API docs at `https://docs.ata.network/xata/api`.

- [ ] **Step 5: Commit**

```bash
git add plugins/xata-agentic-trading/
git commit -m "Add xata-agentic-trading plugin scaffold"
```

---

### Task 2: xata-wallet.py — Wallet Generation

**Files:**
- Create: `plugins/xata-agentic-trading/skills/xata-trading/xata-wallet.py`

**Acceptance criteria:** `generate` subcommand creates a valid wallet file with 0600 permissions, outputs only the address to stdout (never the private key), and refuses to overwrite an existing file without `--force`.

- [ ] **Step 1: Implement generate subcommand**

Write `xata-wallet.py` with:
- `#!/usr/bin/env python3` shebang
- `argparse` CLI with `generate` and `register` subcommands (register implemented as stub that prints error)
- `generate --wallet-file <path> [--force]`:
  - If wallet file already exists and `--force` not set, exit with error: `{"error": "Wallet file already exists. Use --force to overwrite."}`
  - Use `eth_account.Account.create()` to generate a new wallet
  - Create parent directory if needed (`os.makedirs(exist_ok=True)`)
  - Write `{"address": "0x...", "private_key": "0x..."}` to the wallet file
  - Set file permissions to 0600 (`os.chmod(path, 0o600)`)
  - Print only `{"address": "0x..."}` to stdout (never the private key)
- All output as JSON to stdout
- Errors as JSON `{"error": "message"}` to stderr with exit code 1

- [ ] **Step 2: Manual verification**

```bash
# Install deps
pip install "eth_account>=0.13.0,<0.15.0" requests

# Run generate
python plugins/xata-agentic-trading/skills/xata-trading/xata-wallet.py generate --wallet-file /tmp/test-xata-wallet.json
# Expected stdout: {"address": "0x..."}

# Verify file contents
python -c "import json; d=json.load(open('/tmp/test-xata-wallet.json')); assert 'private_key' in d; assert 'address' in d; print('OK')"

# Verify permissions (macOS)
stat -f "%Lp" /tmp/test-xata-wallet.json  # Should be 600

# Verify --force protection
python plugins/xata-agentic-trading/skills/xata-trading/xata-wallet.py generate --wallet-file /tmp/test-xata-wallet.json
# Expected stderr: {"error": "Wallet file already exists..."}

# Cleanup
rm /tmp/test-xata-wallet.json
```

- [ ] **Step 3: Commit**

```bash
git add plugins/xata-agentic-trading/skills/xata-trading/xata-wallet.py
git commit -m "Add xata-wallet.py with generate subcommand"
```

---

### Task 3: xata-wallet.py — Register Subcommand

**Files:**
- Modify: `plugins/xata-agentic-trading/skills/xata-trading/xata-wallet.py`

**Acceptance criteria:** `register` subcommand reads wallet from file, signs with EIP-191, calls XATA register API, and returns the API key.

- [ ] **Step 1: Implement register subcommand**

Replace the register stub with full implementation:
- `register --wallet-file <path>`:
  - Read wallet JSON from file, extract `private_key` and `address`
  - Generate nonce: `int(time.time() * 1000)`
  - Construct message: `f"Register XATA: {nonce}"`
  - Sign with EIP-191:
    ```python
    from eth_account.messages import encode_defunct
    msg = encode_defunct(text=message)
    signed = Account.sign_message(msg, private_key=private_key)
    signature = signed.signature.hex()
    ```
  - POST to `https://api.x.ata.network/v2/account/register` with JSON body:
    ```json
    {"wallet_address": "0x...", "signature": "0x...", "nonce": 1710000000000}
    ```
  - On success (2xx): print `{"api_key": "...", "wallet_address": "..."}` to stdout
  - On HTTP error: print `{"error": "Registration failed: <status> <body>"}` to stderr, exit 1

- [ ] **Step 2: Manual verification**

```bash
# Generate wallet
python plugins/xata-agentic-trading/skills/xata-trading/xata-wallet.py generate --wallet-file /tmp/test-xata-wallet.json

# Register (calls real XATA API)
python plugins/xata-agentic-trading/skills/xata-trading/xata-wallet.py register --wallet-file /tmp/test-xata-wallet.json
# Expected stdout: {"api_key": "api_...", "wallet_address": "0x..."}

# Cleanup
rm /tmp/test-xata-wallet.json
```

- [ ] **Step 3: Commit**

```bash
git add plugins/xata-agentic-trading/skills/xata-trading/xata-wallet.py
git commit -m "Add register subcommand to xata-wallet.py"
```

---

### Task 4: SKILL.md — Core Skill File

**Files:**
- Create: `plugins/xata-agentic-trading/skills/xata-trading/SKILL.md`

This is the main deliverable. The SKILL.md must contain all the logic Claude follows when the skill is invoked.

**Script path discovery:** In SKILL.md, instruct Claude to locate `xata-wallet.py` by running:
```bash
SCRIPT_PATH="$(find ~/.claude/plugins -name 'xata-wallet.py' -path '*/xata-trading/*' 2>/dev/null | head -1)"
```
If not found, fall back to searching from the current working directory:
```bash
SCRIPT_PATH="$(find . -name 'xata-wallet.py' -path '*/xata-trading/*' 2>/dev/null | head -1)"
```

- [ ] **Step 1: Write SKILL.md frontmatter and overview**

```yaml
---
name: xata-trading
description: Trade on decentralized exchanges via XATA API — setup wallets, bind venues, and execute trades
allowed-tools: Bash, Read, Write, WebFetch, AskUserQuestion
---
```

Followed by:
- Brief overview: what this skill does
- Supported platforms: Hyperliquid, Lighter, Aster
- Link to full API docs: `https://docs.ata.network/xata/api`
- Note: this skill handles single interactive requests only — automated/scheduled trading is not supported

- [ ] **Step 2: Write Entry Point — State Detection section**

Instructions for Claude to:
1. Locate `xata-wallet.py` using the discovery commands above, store path for later use
2. Read `~/.xata-claude/config.json` using the Read tool
3. If file missing or no `api_key` → go to Setup Flow
4. If `api_key` exists but target venue not in `venues` → go to Venue Binding Flow
5. If `api_key` exists and target venue active → go to Trading Flow

Include the exact JSON structure Claude should expect for `config.json`.

- [ ] **Step 3: Write Setup Flow section**

Step-by-step instructions for Claude:
1. Check Python deps: `python3 -c "import eth_account; import requests"` via Bash — if fails, ask user to install: `pip install eth_account requests`
2. Run `python3 <SCRIPT_PATH> generate --wallet-file ~/.xata-claude/wallet.json` via Bash
3. Parse JSON stdout to confirm address was created
4. Inform user: "Management wallet created at ~/.xata-claude/wallet.json. This wallet is only used for API key management — it holds no funds."
5. Run `python3 <SCRIPT_PATH> register --wallet-file ~/.xata-claude/wallet.json` via Bash
6. Parse JSON stdout to get `api_key`
7. Write `~/.xata-claude/config.json` using the Write tool with content:
   ```json
   {
     "api_key": "<api_key from register>",
     "api_base": "https://api.x.ata.network",
     "venues": {},
     "settings": {
       "confirm_before_trade": true
     }
   }
   ```
8. Set file permissions: `chmod 600 ~/.xata-claude/config.json` via Bash

- [ ] **Step 4: Write Venue Binding Flow section**

Three subsections with complete curl templates:

**Hyperliquid (agent wallet):**
- Note: API is being redesigned. Before calling, fetch latest parameters via WebFetch from `https://docs.ata.network/xata/api/agent-access/venue-setup`. If WebFetch fails, instruct user to check the docs manually and provide the required parameters.
- Call venue setup endpoint:
  ```bash
  curl -s -X POST "https://api.x.ata.network/v2/venue/setup" \
    -H "x-api-key: <API_KEY>" \
    -H "Content-Type: application/json" \
    -d '{"venue": "hyperliquid", ...params from docs...}'
  ```
- Show returned agent wallet address and instructions to user
- Wait for user to confirm they've approved the agent wallet
- Verify: `curl -s "https://api.x.ata.network/v2/venues" -H "x-api-key: <API_KEY>"`
- Check response for hyperliquid with status "active"
- Update `config.json` venues via Read + Edit tools

**Aster (prepare + confirm):**
- Prepare: `curl -s -X POST "https://api.x.ata.network/v2/venue/prepare" -H "x-api-key: <API_KEY>" -H "Content-Type: application/json" -d '{"venue": "aster"}'`
- Show returned keypair and instructions: register the address in Aster's API wallet page
- Wait for user confirmation
- Confirm: `curl -s -X POST "https://api.x.ata.network/v2/venue/confirm" -H "x-api-key: <API_KEY>" -H "Content-Type: application/json" -d '{"venue": "aster", "main_wallet_address": "0x..."}'`
- Verify via `GET /v2/venues`, update `config.json`

**Lighter (credentials):**
- Show instructions: how to get credentials from Lighter (api_key_private_key, api_key_index, account_index, l1_address)
- Use AskUserQuestion to collect each credential
- Submit: `curl -s -X POST "https://api.x.ata.network/v2/venue/credentials" -H "x-api-key: <API_KEY>" -H "Content-Type: application/json" -d '{"venue": "lighter", "credentials": {...}}'`
- Verify via `GET /v2/venues`, update `config.json`

- [ ] **Step 5: Write Trading Flow section**

Instructions for Claude:
1. Parse user intent: platform, operation type (order/cancel/query/balance/position), symbol, side, quantity, price, order type
2. Default quote currency: USDC, fallback USDT
3. Validate trading pair: `curl -s "https://api.x.ata.network/v2/{platform}/symbol-info" -H "x-api-key: <API_KEY>"`
4. WebFetch the relevant API doc page for the specific operation from `https://docs.ata.network/xata/api`
5. Construct curl request with all required parameters
6. If `confirm_before_trade` is true in config, show the full request to user and ask confirmation via AskUserQuestion
7. Execute via Bash + curl
8. Parse JSON response and display results clearly (fill price, quantity, order ID, etc.)
9. On error: show HTTP status + error body, suggest corrections

Include the full API capabilities list:
```
Available operations:
- Query balances (single platform / aggregated), positions, funding rates
- Place orders (single / batch up to 10), cancel orders, query open orders
- Query fill history
- Market data (best bid/ask, orderbook depth, symbol info)
- Adjust leverage
- Strategy engine (cross-exchange arbitrage: submit/query/cancel)

Supported platforms (v0.1.0): Hyperliquid, Lighter, Aster
API base URL: https://api.x.ata.network
Full API reference: https://docs.ata.network/xata/api
```

Include a generic curl template:
```bash
curl -s -X <METHOD> "https://api.x.ata.network/v2/{platform}/{endpoint}" \
  -H "x-api-key: <API_KEY>" \
  -H "Content-Type: application/json" \
  -d '<JSON_BODY>'
```

Strategy engine operations follow the same flow pattern. Endpoints are under `/v2/all/strategy/...`.

- [ ] **Step 6: Write Error Handling section**

| Error | Detection | Action |
|-------|-----------|--------|
| API Key invalid/expired | HTTP 401/403 | Prompt user to re-register: delete `config.json`, re-run Setup Flow |
| Venue not bound | Venue missing from `config.json` | Auto-enter Venue Binding Flow for that venue |
| Trade failure | HTTP 4xx/5xx | Show status code + error body, suggest parameter corrections |
| Network error / timeout | curl returns non-zero | Suggest retry |
| Missing Python deps | `import` fails | Prompt `pip install eth_account requests` |
| Invalid trading pair | symbol-info returns no match | Show available pairs from symbol-info |
| Rate limited | HTTP 429 | Show error, suggest waiting before retry |

- [ ] **Step 7: Write User Settings and Teardown sections**

**Settings:**
- User says "don't confirm trades" → Read `config.json`, set `settings.confirm_before_trade` to `false`, write back
- User says "restore confirmation" → set to `true`

**Teardown:**
- "Delete my API key": `curl -s "https://api.x.ata.network/v2/api-keys" -H "x-api-key: <API_KEY>"` → find `keyId` → `curl -s -X DELETE "https://api.x.ata.network/v2/api-keys/{keyId}" -H "x-api-key: <API_KEY>"` → `rm ~/.xata-claude/config.json`
- "Unbind Hyperliquid": `curl -s "https://api.x.ata.network/v2/venues" -H "x-api-key: <API_KEY>"` → find `venueId` for hyperliquid → `curl -s -X DELETE "https://api.x.ata.network/v2/venues/{venueId}" -H "x-api-key: <API_KEY>"` → remove venue from `config.json`
- "Reset everything": delete all API keys, delete all venues, `rm -rf ~/.xata-claude/`

- [ ] **Step 8: Commit**

```bash
git add plugins/xata-agentic-trading/skills/xata-trading/SKILL.md
git commit -m "Add SKILL.md for xata-trading skill"
```

---

### Task 5: Update marketplace.json

**Files:**
- Modify: `.claude-plugin/marketplace.json`

- [ ] **Step 1: Add plugin entry to marketplace.json**

Add to the `plugins` array:

```json
{
  "name": "xata-agentic-trading",
  "source": "./plugins/xata-agentic-trading",
  "description": "Trade on decentralized exchanges via XATA API with AI-powered natural language trading",
  "version": "0.1.0",
  "author": {
    "name": "Automata Network",
    "email": "devops@ata.network"
  },
  "keywords": ["trading", "defi", "xata", "hyperliquid", "aster", "lighter"],
  "category": "trading"
}
```

- [ ] **Step 2: Validate JSON**

```bash
cat .claude-plugin/marketplace.json | python -m json.tool > /dev/null && echo "Valid JSON" || echo "INVALID"
```

- [ ] **Step 3: Commit**

```bash
git add .claude-plugin/marketplace.json
git commit -m "Add xata-agentic-trading to marketplace"
```

---

### Task 6: End-to-End Smoke Test

- [ ] **Step 1: Verify plugin structure**

```bash
# Check all required files exist
ls plugins/xata-agentic-trading/.claude-plugin/plugin.json
ls plugins/xata-agentic-trading/skills/xata-trading/SKILL.md
ls plugins/xata-agentic-trading/skills/xata-trading/xata-wallet.py
ls plugins/xata-agentic-trading/skills/xata-trading/requirements.txt
ls plugins/xata-agentic-trading/README.md

# Validate JSON files
python -m json.tool plugins/xata-agentic-trading/.claude-plugin/plugin.json > /dev/null && echo "plugin.json: Valid"
python -m json.tool .claude-plugin/marketplace.json > /dev/null && echo "marketplace.json: Valid"
```

- [ ] **Step 2: Test wallet generation + registration flow**

```bash
# Generate wallet
python plugins/xata-agentic-trading/skills/xata-trading/xata-wallet.py generate --wallet-file /tmp/smoke-test-wallet.json
# Expected stdout: {"address": "0x..."}

# Register (calls real XATA API)
python plugins/xata-agentic-trading/skills/xata-trading/xata-wallet.py register --wallet-file /tmp/smoke-test-wallet.json
# Expected stdout: {"api_key": "api_...", "wallet_address": "0x..."}

# Cleanup
rm /tmp/smoke-test-wallet.json
```

- [ ] **Step 3: Verify SKILL.md frontmatter**

```bash
head -10 plugins/xata-agentic-trading/skills/xata-trading/SKILL.md
# Must show --- delimited YAML with: name, description, allowed-tools
```

- [ ] **Step 4: Final commit if any fixes needed**

```bash
git add plugins/xata-agentic-trading/ .claude-plugin/marketplace.json
git commit -m "Fix issues found in smoke test"
```
