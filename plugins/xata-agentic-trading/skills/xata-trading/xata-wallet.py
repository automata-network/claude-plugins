#!/usr/bin/env python3
"""
xata-wallet.py — EVM wallet generation and registration helper.

Security note: private keys are written only to the wallet file (mode 0600)
and NEVER emitted to stdout. All stdout output is JSON. Errors go to stderr
as JSON with exit code 1.
"""

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request


def err(message: str) -> None:
    """Print a JSON error to stderr and exit with code 1."""
    print(json.dumps({"error": message}), file=sys.stderr)
    sys.exit(1)


def cmd_generate(args: argparse.Namespace) -> None:
    wallet_path = args.wallet_file

    # Refuse to overwrite unless --force is given
    if os.path.exists(wallet_path) and not args.force:
        err("Wallet file already exists. Use --force to overwrite.")

    try:
        from eth_account import Account  # type: ignore
    except ImportError:
        err("eth_account is not installed. Run: pip install eth_account")

    account = Account.create()
    address: str = account.address
    private_key: str = account.key.hex()
    if not private_key.startswith("0x"):
        private_key = "0x" + private_key

    wallet_data = {"address": address, "private_key": private_key}

    # Create parent directories if they don't exist
    parent = os.path.dirname(os.path.abspath(wallet_path))
    os.makedirs(parent, exist_ok=True)

    # Write wallet file
    try:
        with open(wallet_path, "w") as fh:
            json.dump(wallet_data, fh)
    except OSError as exc:
        err(f"Failed to write wallet file: {exc}")

    # Restrict permissions to owner read/write only
    try:
        os.chmod(wallet_path, 0o600)
    except OSError as exc:
        err(f"Failed to set wallet file permissions: {exc}")

    # Only the address goes to stdout — never the private key
    print(json.dumps({"address": address}))


def cmd_register(args: argparse.Namespace) -> None:
    wallet_path = args.wallet_file

    # Read wallet JSON
    try:
        with open(wallet_path, "r") as fh:
            wallet_data = json.load(fh)
    except OSError as exc:
        err(f"Failed to read wallet file: {exc}")
    except json.JSONDecodeError as exc:
        err(f"Invalid JSON in wallet file: {exc}")

    private_key: str = wallet_data.get("private_key", "")
    address: str = wallet_data.get("address", "")

    if not private_key or not address:
        err("Wallet file must contain 'private_key' and 'address' fields.")

    try:
        from eth_account import Account  # type: ignore
        from eth_account.messages import encode_defunct  # type: ignore
    except ImportError:
        err("eth_account is not installed. Run: pip install eth_account")

    # Generate nonce (milliseconds since epoch)
    nonce = int(time.time() * 1000)

    # Construct and sign message using EIP-191
    message = f"Register XATA: {nonce}"
    msg = encode_defunct(text=message)
    signed = Account.sign_message(msg, private_key=private_key)
    signature: str = signed.signature.hex()
    if not signature.startswith("0x"):
        signature = "0x" + signature

    # POST to XATA registration endpoint
    payload = json.dumps(
        {"wallet_address": address, "signature": signature, "nonce": nonce}
    ).encode("utf-8")

    req = urllib.request.Request(
        "https://api.x.ata.network/v2/account/register",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(req) as resp:
            body = resp.read().decode("utf-8")
            print(body)
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8")
        print(
            json.dumps({"error": f"Registration failed: {exc.code} {body}"}),
            file=sys.stderr,
        )
        sys.exit(1)
    except urllib.error.URLError as exc:
        print(
            json.dumps({"error": f"Network error: {exc.reason}"}),
            file=sys.stderr,
        )
        sys.exit(1)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="xata-wallet",
        description="EVM wallet operations for the xata-agentic-trading skill.",
    )
    subparsers = parser.add_subparsers(dest="subcommand", required=True)

    # --- generate ---
    gen = subparsers.add_parser("generate", help="Generate a new EVM wallet.")
    gen.add_argument(
        "--wallet-file",
        required=True,
        metavar="PATH",
        help="Path where the wallet JSON file will be written.",
    )
    gen.add_argument(
        "--force",
        action="store_true",
        default=False,
        help="Overwrite the wallet file if it already exists.",
    )
    gen.set_defaults(func=cmd_generate)

    # --- register ---
    reg = subparsers.add_parser("register", help="Register wallet and obtain API key.")
    reg.add_argument(
        "--wallet-file",
        required=True,
        metavar="PATH",
        help="Path to the wallet JSON file.",
    )
    reg.set_defaults(func=cmd_register)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
