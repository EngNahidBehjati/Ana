# Configuration and Secrets Baseline

- Configuration is environment-driven.
- `.env` is local-only and ignored by Git.
- `.env.example` contains names/default-safe values only.
- Production secrets must be stored in the selected deployment platform's secret manager; no secrets in repository or CI YAML.
- Environment names: local, test, staging, production.
- Deployment-provider-specific secret strategy is intentionally deferred until the provider is selected.
