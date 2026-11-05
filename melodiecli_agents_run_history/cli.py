"""Command surface for melodiecli-agents-run-history (scaffold; status: PLANNED).

This stub is intentionally minimal and fails closed: only status, verify, and
help are implemented. It performs no financial, wallet, token, provider, or
network operations.
"""

from __future__ import annotations

import argparse
import json
import sys

NAME = "melodiecli-agents-run-history"
VERSION = "0.1.0"
STATUS = "PLANNED"
CATEGORY = "agents"
SCOPE = "agent coordination tooling: run history"
DATA_POLICY = "ZERO TOLERANCE FOR FABRICATED DATA"


def cmd_status(_args: argparse.Namespace) -> int:
    payload = {
        "name": NAME,
        "version": VERSION,
        "status": STATUS,
        "category": CATEGORY,
        "scope": SCOPE,
        "implementation": "SCAFFOLD_ONLY",
        "data_policy": DATA_POLICY,
        "operations_performed": [],
        "note": "No business operation is implemented in this scaffold.",
    }
    print(json.dumps(payload, indent=2))
    return 0


def cmd_verify(_args: argparse.Namespace) -> int:
    print(f"{NAME}: product-level verification is not configured (status: {STATUS}).")
    print("Scaffold tests validate the status CLI only; see tests/ for details.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog=NAME,
        description=f"{NAME} - {SCOPE} (status: {STATUS})",
    )
    parser.add_argument("--version", action="version", version=f"{NAME} {VERSION}")
    sub = parser.add_subparsers(dest="command", metavar="COMMAND")
    sub.add_parser("status", help="Print scaffold status metadata as JSON")
    sub.add_parser("verify", help="Report product-level verification availability")
    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command == "status":
        return cmd_status(args)
    if args.command == "verify":
        return cmd_verify(args)
    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
