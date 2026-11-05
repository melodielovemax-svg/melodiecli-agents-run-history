# Configuration

No runtime configuration is implemented.

`.env.example` contains variable names only. Do not put credentials, account
identifiers, customer data, or production values in this file. Keep local `.env`
files untracked and use an approved secret manager for real deployments.

Any future configuration must document its owner, purpose, sensitivity, validation,
and safe default. Empty or missing credentials must fail closed.
