---
name: xata-trading
description: Trade on decentralized exchanges via XATA API — setup wallets, bind venues, and execute trades
allowed-tools: Bash, Read, Write, WebFetch, AskUserQuestion
---

# XATA Trading Skill

## Overview

This skill enables AI-powered trading on decentralized exchanges through the XATA API. It handles wallet setup, venue binding, and trade execution across supported platforms.

Supported platforms (v0.1.0): Hyperliquid, Lighter, Aster, and HIP-3 perp dexes (on Hyperliquid).

Full API reference: https://docs.ata.network/xata/api

This skill handles single interactive requests only. Do not implement automated, scheduled, or looping trading strategies. Each invocation processes one user request and completes.

---

## Venue Discovery

When the user asks what venues or exchanges they can trade on, list:
- **Hyperliquid** — the main Hyperliquid L1 perp DEX
- **Lighter** — Lighter DEX
- **Aster** — Aster DEX
- **HIP-3 perp dexes** — third-party perpetual DEXes deployed on Hyperliquid via the HIP-3 standard

If the user asks what HIP-3 dexes are available or supported, fetch the list from the XATA API. Run via Bash:

```bash
curl -s "<API_BASE>/v2/hyperliquid/getHip3Dexes" \
  -H "x-api-key: <API_KEY>"
```

The response contains a `dexes` array listing the short names of supported HIP-3 dexes. Present the list to the user.

### Trading on HIP-3 Dexes

HIP-3 dexes settle on Hyperliquid. The user must have Hyperliquid bound as a venue before trading on any HIP-3 dex. If Hyperliquid is not yet bound, guide them through the Hyperliquid venue binding flow first. **HIP-3 dexes do not require their own separate venue binding** — once Hyperliquid is bound, all HIP-3 dexes are accessible. Do not offer to "bind" a HIP-3 dex.

HIP-3 dexes support the same API methods as Hyperliquid (except `getHip3Dexes`, which is Hyperliquid-only). When constructing requests for a HIP-3 dex, follow the same Trading Flow as Hyperliquid — including fetching endpoint documentation from `https://docs.ata.network/xata/api` — with two differences:
1. **API path**: Use `<API_BASE>/v2/hip3/<dexname>/<endpoint>` instead of `<API_BASE>/v2/hyperliquid/<endpoint>`. For example, to trade on XYZ use `<API_BASE>/v2/hip3/xyz/<endpoint>`, for dreamcash use `<API_BASE>/v2/hip3/cash/<endpoint>`, etc.
2. **Symbol names**: Use the coin name without any prefix (e.g., `GOLD`, `TSLA`, `MAG7`) — not the prefixed form.

---

## Script Path Discovery

Before any operation, locate the helper script `xata-wallet.py`. Run via Bash:

```bash
SCRIPT_PATH="$(find ~/.claude/plugins -name 'xata-wallet.py' -path '*/xata-trading/*' 2>/dev/null | head -1)"
```

If `SCRIPT_PATH` is empty, try the fallback:

```bash
SCRIPT_PATH="$(find . -name 'xata-wallet.py' -path '*/xata-trading/*' 2>/dev/null | head -1)"
```

If still empty, inform the user that the xata-trading plugin may not be installed correctly and stop.

Store the resolved `SCRIPT_PATH` and reuse it for all subsequent script invocations in this session.

---

## Entry Point — State Detection

When this skill is triggered:

1. Locate `xata-wallet.py` using the discovery procedure above.
2. Use the Read tool to read `~/.xata-claude/config.json`.
3. Follow this decision tree:
   - If the file is missing or does not contain an `api_key` field, enter the **Setup Flow**.
   - If `api_key` exists but the user's target venue is not listed in `venues` (or its status is not `"active"`), enter the **Venue Binding Flow** for that venue.
   - If `api_key` exists and the target venue is active in `venues`, enter the **Trading Flow**.

Config file schema (`~/.xata-claude/config.json`):

```json
{
  "api_key": "api_...",
  "api_base": "https://api.x.ata.network",
  "venues": {
    "hyperliquid": {"status": "active", "bound_at": "2026-03-25T..."}
  },
  "settings": {
    "confirm_before_trade": true
  }
}
```

---

## Authentication

All API calls require the header `x-api-key: <api_key>` where `<api_key>` is read from `~/.xata-claude/config.json`.

The only exception is the initial `/v2/account/register` call during setup, which requires no API key.

---

## Setup Flow

Execute these steps in order:

1. **Check and install Python dependencies.** Run via Bash:
   ```bash
   python3 -c "import eth_account; import requests"
   ```
   If this fails, automatically install the dependencies via Bash:
   ```bash
   pip install eth_account requests
   ```
   After installation, re-run the import check to confirm. If it still fails (e.g., pip not available), inform the user and stop.

2. **Generate wallet.** Run via Bash:
   ```bash
   python3 $SCRIPT_PATH generate --wallet-file ~/.xata-claude/wallet.json
   ```
   Parse the JSON stdout. Confirm the `address` field is present.

3. **Inform the user.** Tell them: "Management wallet created. This wallet is only for API key management — it holds no funds."

4. **Register with XATA API.** Run via Bash:
   ```bash
   python3 $SCRIPT_PATH register --wallet-file ~/.xata-claude/wallet.json
   ```
   Parse the JSON stdout. Extract the `api_key` and `wallet_address` fields.

5. **Write config file.** Use the Write tool to create `~/.xata-claude/config.json` with:
   ```json
   {
     "api_key": "<api_key from register output>",
     "api_base": "https://api.x.ata.network",
     "venues": {},
     "settings": {
       "confirm_before_trade": true
     }
   }
   ```

6. **Set file permissions.** Run via Bash:
   ```bash
   chmod 600 ~/.xata-claude/config.json
   ```

7. Tell the user setup is complete and ask which venue they want to bind, or what they would like to do next.

---

## Venue Binding Flow

This flow is triggered when the user explicitly asks to bind a venue (e.g., "bind Hyperliquid") or implicitly when the user wants to trade on a venue that is not yet in `venues` with status `"active"`.

Read the `api_key` from `~/.xata-claude/config.json` before proceeding. Store it as `API_KEY`.

### Important: Main Wallet Addresses

Each venue requires a `main_wallet_address` during the confirm step. This is the user's primary trading wallet on that specific venue. **Do not assume the same wallet is used across all venues** — always ask the user for the main wallet address for each venue separately. If the user is binding multiple venues at once, collect the main wallet address for each venue individually before confirming.

### Hyperliquid — Agent Wallet

The Hyperliquid binding API is being redesigned. Before constructing the request, fetch the latest parameters.

1. Use WebFetch to retrieve `https://docs.ata.network/xata/api/agent-access/venue-setup` and extract the current required parameters for the Hyperliquid venue setup call. If WebFetch fails, tell the user: "Could not fetch the latest docs. Check https://docs.ata.network/xata/api/agent-access/venue-setup manually for current parameters."

2. **Prepare.** Submit the venue prepare request via Bash:
   ```bash
   curl -s -X POST "<API_BASE>/v2/account/venues/hyperliquid/prepare" \
     -H "X-API-KEY: <API_KEY>" \
     -H "Content-Type: application/json" \
     -d '{}'
   ```

3. Parse the response. Show the returned agent wallet address, agent name, and instructions to the user. Tell them to:
   - Go to https://app.hyperliquid.xyz/API
   - Approve the agent wallet address shown in the response
   - Set the agent name as shown in the response
   - Set expiry to their preference

4. Use AskUserQuestion to wait for the user to confirm they have approved the agent wallet on Hyperliquid. **In the same question or a follow-up**, ask for their **Hyperliquid main wallet address** (the wallet they used to approve the agent on Hyperliquid).

5. **Confirm.** Run via Bash:
   ```bash
   curl -s -X POST "<API_BASE>/v2/account/venues/hyperliquid/confirm" \
     -H "X-API-KEY: <API_KEY>" \
     -H "Content-Type: application/json" \
     -d '{"main_wallet_address": "0x..."}'
   ```
   Replace `0x...` with the user's Hyperliquid main wallet address.

6. Check the response for status `"active"`. If not active, show the error to the user.

7. Use Read to load `~/.xata-claude/config.json`, add or update the `hyperliquid` entry in `venues` with `{"status": "active", "bound_at": "<current ISO timestamp>"}`, and use Write to save the updated config.

### Aster — Prepare + Confirm

1. **Prepare.** Run via Bash:
   ```bash
   curl -s -X POST "<API_BASE>/v2/account/venues/aster/prepare" \
     -H "X-API-KEY: <API_KEY>" \
     -H "Content-Type: application/json" \
     -d '{}'
   ```

2. Parse the response. Show the returned API wallet address and instructions to the user. Tell them to:
   - Go to https://www.asterdex.com/en/api-wallet
   - Add the returned address as an API wallet

3. Use AskUserQuestion to wait for the user to confirm they have registered the address in Aster. **In the same question or a follow-up**, ask for their **Aster main wallet address** (the wallet they used to register the API wallet on Aster).

4. **Confirm.** Run via Bash:
   ```bash
   curl -s -X POST "<API_BASE>/v2/account/venues/aster/confirm" \
     -H "X-API-KEY: <API_KEY>" \
     -H "Content-Type: application/json" \
     -d '{"main_wallet_address": "0x..."}'
   ```
   Replace `0x...` with the user's Aster main wallet address.

5. Check the response for status `"active"`. If not active, show the error to the user.

6. Use Read to load `~/.xata-claude/config.json`, add or update the `aster` entry in `venues` with `{"status": "active", "bound_at": "<current ISO timestamp>"}`, and use Write to save the updated config.

### Lighter — User Credentials

1. Inform the user they need to provide credentials from Lighter. The required fields are:
   - `api_key_private_key` — the private key for the Lighter API key
   - `api_key_index` — the API key index
   - `account_index` — the account index
   - `l1_address` — the L1 wallet address

2. Use AskUserQuestion to collect each credential from the user.

3. Submit credentials via Bash:
   ```bash
   curl -s -X POST "<API_BASE>/v2/account/venues/lighter/credentials" \
     -H "X-API-KEY: <API_KEY>" \
     -H "Content-Type: application/json" \
     -d '{"credentials": {"api_key_private_key": "...", "api_key_index": ..., "account_index": ..., "l1_address": "0x..."}}'
   ```
   Replace placeholder values with the actual credentials provided by the user.

4. Check the response for status `"active"`. If not active, show the error to the user.

5. Use Read to load `~/.xata-claude/config.json`, add or update the `lighter` entry in `venues` with `{"status": "active", "bound_at": "<current ISO timestamp>"}`, and use Write to save the updated config.

---

## Trading Flow

1. **Parse user intent.** Determine the following from the user's message:
   - Platform (hyperliquid, lighter, aster, or a HIP-3 dex name such as xyz, flx, vntl, hyna, km, cash, etc.)
   - Operation: order, cancel, query orders, balance, position, market data, leverage, or strategy
   - Symbol / trading pair
   - Side (buy / sell) if applicable
   - Quantity
   - Price (if limit order)
   - Order type (limit / market)

2. **Default quote currency.** If the user specifies only the base asset (e.g., "buy ETH"), default the quote currency to USDC. If USDC is not available for the pair, fall back to USDT.

3. **Validate trading pair.** Run via Bash:
   ```bash
   curl -s "https://api.x.ata.network/v2/<platform>/getSymbolInfo" \
     -H "x-api-key: <API_KEY>"
   ```
   Check that the requested symbol exists in the response. If not, show the user the list of available pairs and ask them to pick one.

4. **Fetch endpoint documentation.** Use WebFetch to retrieve the relevant page from `https://docs.ata.network/xata/api` for the specific endpoint being used. This ensures the correct parameters and request format.

5. **Construct the request.** Build the curl command using this template:
   ```bash
   curl -s -X <METHOD> "https://api.x.ata.network/v2/<platform>/<endpoint>" \
     -H "x-api-key: <API_KEY>" \
     -H "Content-Type: application/json" \
     -d '<JSON_BODY>'
   ```
   Replace `<METHOD>`, `<platform>`, `<endpoint>`, `<API_KEY>`, and `<JSON_BODY>` with actual values.

6. **Confirm with user if enabled.** Use Read to check `~/.xata-claude/config.json`. If `settings.confirm_before_trade` is `true` and the operation modifies state (placing orders, cancelling, adjusting leverage), show the full request parameters to the user and use AskUserQuestion to get confirmation before executing. Do not confirm for read-only queries (balances, positions, market data).

7. **Execute.** Run the curl command via Bash.

8. **Parse and display results.** Format the response clearly for the user. For orders, show order ID, fill status, and price. For balances, show each asset and amount. For positions, show size, entry price, and PnL if available.

9. **Handle errors.** See the Error Handling section below.

### Strategy Engine Operations

Strategy engine operations (cross-exchange arbitrage) follow the same flow as above. The endpoints are under `/v2/all/strategy/...`. Use the same authentication, confirmation, and error handling patterns.

---

## API Capabilities Summary

```
Available operations:
- Query balances (single platform / aggregated), positions, funding rates
- Place orders (single / batch up to 10), cancel orders, query open orders
- Query fill history
- Market data (best bid/ask, orderbook depth, symbol info)
- Adjust leverage
- Strategy engine (cross-exchange arbitrage: submit/query/cancel)

Supported platforms (v0.1.0): Hyperliquid, Lighter, Aster, HIP-3 perp dexes
API base URL: https://api.x.ata.network
Full API reference: https://docs.ata.network/xata/api
```

---

## Error Handling

When an error occurs, detect and respond according to this table:

| Error | Detection | Action |
|-------|-----------|--------|
| API key invalid or expired | HTTP 401 or 403 response | Tell the user the API key is invalid. Delete `~/.xata-claude/config.json` and re-run the Setup Flow from the beginning. |
| Venue not bound | Target venue missing from `venues` in config.json or not `"active"` | Automatically enter the Venue Binding Flow for that venue. |
| Trade failure | HTTP 4xx or 5xx response | Show the HTTP status code and full error body to the user. Suggest a fix based on the error message. |
| Network error | curl command fails (non-zero exit, no HTTP response) | Tell the user there was a network error and suggest retrying. |
| Missing Python dependencies | `python3 -c "import ..."` fails | Tell the user to run `pip install eth_account requests` and retry. |
| Invalid trading pair | Symbol not found in symbol-info response | Show the list of available trading pairs and ask the user to select one. |
| Rate limited | HTTP 429 response | Show the error to the user and suggest waiting before retrying. |

---

## User Settings

Handle these user requests by modifying `~/.xata-claude/config.json`:

- **"Don't confirm trades" / "Skip confirmations"**: Use Read to load config.json, set `settings.confirm_before_trade` to `false`, use Write to save. Confirm the change to the user.

- **"Restore confirmations" / "Confirm trades again"**: Use Read to load config.json, set `settings.confirm_before_trade` to `true`, use Write to save. Confirm the change to the user.

---

## Teardown

### Delete API Key

1. Retrieve the list of API keys via Bash:
   ```bash
   curl -s "https://api.x.ata.network/v2/api-keys" -H "x-api-key: <API_KEY>"
   ```
2. Parse the response to find the `keyId` for the current key.
3. Delete the key via Bash:
   ```bash
   curl -s -X DELETE "https://api.x.ata.network/v2/api-keys/<keyId>" -H "x-api-key: <API_KEY>"
   ```
4. Remove the config file via Bash:
   ```bash
   rm ~/.xata-claude/config.json
   ```
5. Tell the user the API key has been deleted.

### Unbind a Venue

1. Retrieve venues via Bash:
   ```bash
   curl -s "https://api.x.ata.network/v2/venues" -H "x-api-key: <API_KEY>"
   ```
2. Parse the response to find the `venueId` for the target venue.
3. Delete the venue binding via Bash:
   ```bash
   curl -s -X DELETE "https://api.x.ata.network/v2/venues/<venueId>" -H "x-api-key: <API_KEY>"
   ```
4. Use Read to load `~/.xata-claude/config.json`, remove the venue from `venues`, and use Write to save.
5. Tell the user the venue has been unbound.

### Reset Everything

1. Retrieve and delete all API keys (as in Delete API Key above).
2. Retrieve and delete all venue bindings (as in Unbind a Venue above).
3. Remove the entire config directory via Bash:
   ```bash
   rm -rf ~/.xata-claude/
   ```
4. Tell the user everything has been reset.
