# melodiecli-agents-run-history

**State:** PLANNED — scaffold with a runnable status CLI; no business functionality is implemented.

## Intended responsibility

Agent coordination tooling: run history

## What the scaffold actually does

- `melodiecli-agents-run-history status` prints machine-readable scaffold metadata (JSON) and exits 0.
- `melodiecli-agents-run-history verify` reports that product-level verification is not configured (PLANNED).
- Any future command beyond `status`/`verify`/`--help` is not implemented and must fail closed.

The scaffold does not process payments, sign transactions, transfer funds, mint tokens,
contact providers, or generate business data.

## Scope and dependencies

- Owner: TBD; confirm the GitHub account or organization before publication.
- Dependencies: none declared.
- No production credentials, customer information, payment records, wallet data,
  AI-provider connections, or token balances are included.
- This repository does not copy files from `MelodieLiteLLM` or `OmniRev-Engine`.

## Readiness labels

| Label | Meaning |
|---|---|
| PLANNED | Intended scope only; scaffold CLI present; not a product. |
| IMPLEMENTED | Code exists and has been reviewed; not a production claim. |
| TESTED | Named tests passed in a recorded environment; scope and evidence stated. |
| PRODUCTION-READY | Operational, security, legal, ownership, and release criteria verified. |

Current product state: **PLANNED**. Scaffold tests validate the status CLI only.

## Development

```powershell
python -m melodiecli_agents_run_history status
python -m unittest discover -s tests -v
```

Configuration keys are documented in `.env.example`; values are intentionally blank.
See `CONFIGURATION.md`, `SECURITY.md`, and `EVIDENCE.md` before adding integrations.
