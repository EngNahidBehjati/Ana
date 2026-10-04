# Sprint 0 - Foundation

## Sprint goal
Create the minimum professional foundation needed to start product development immediately without foundational architectural debt.

## Backlog status

- [x] S0-01 Architecture Baseline
- [x] S0-02 Domain Vocabulary v1
- [x] S0-03 Module Boundaries v1
- [x] S0-04 ADR-001 Modular Monolith
- [x] S0-05 ADR-002 Multi-tenancy model
- [x] S0-06 ADR-003 Entitlement architecture
- [x] S0-07 ADR-004 Agreement/Commission versioning
- [x] S0-08 ADR-005 Domain Events strategy
- [x] S0-09 Technology Stack decision (ADR-006)
- [x] S0-10 Repository scaffold
- [x] S0-11 Testing foundation
- [x] S0-12 CI baseline
- [x] S0-13 Configuration/secrets baseline
- [x] S0-14 Observability baseline
- [x] S0-15 First migration: Identity/Agency/Membership foundation

## CI/CD decision

CI is required now. Every PR/main push runs backend lint/type/tests/migration checks and frontend lint/tests/build.

Full Continuous Deployment is intentionally NOT part of Sprint 0 because no staging/production provider, domain, secret store, migration rollout, health-check/rollback policy has been selected. Creating CD now would be fake completeness. CD becomes a deliverable when the first staging target is selected.

## Definition of Done for Sprint 0

- Decisions are stored in repository, not only chat.
- Backend and frontend bootstraps exist.
- Health endpoint exists.
- Initial DB migration exists.
- Local config template exists; secrets are excluded from Git.
- CI workflow exists.
- Backend smoke test and offline migration compilation pass locally; full lint/type/frontend/build gates are configured in CI and execute after the remote repository is pushed.
- Git repository is initialized with `main` branch and an initial commit.
- Sprint 1 backlog is ready.

## Sprint 1 goal

Deliver the first real vertical slice: a user can establish an Agency tenant and only access authorized Agency data.

## External repository handoff

The source tree is a real local Git repository with an initial commit. A GitHub remote cannot be created by the currently available connector, so the only external handoff step is creating an empty `ana` repository and pushing `main`; see `docs/engineering/github-setup.md`. This does not change the Sprint 0 architecture/code deliverables.

## Validation note

The execution environment used to prepare this sprint has no outbound package-registry/Docker access. Backend smoke tests and Alembic offline SQL generation were executed successfully using the available runtime. CI contains the authoritative full gates (dependency install, lint, type check, PostgreSQL migration cycle, tests, frontend lint/test/build) and will execute after the first GitHub push.
