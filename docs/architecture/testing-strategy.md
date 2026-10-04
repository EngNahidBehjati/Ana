# Testing Strategy Baseline

- Unit tests: domain rules and deterministic policies.
- Integration tests: PostgreSQL persistence, migrations, repository/query behavior.
- API tests: HTTP contracts and validation.
- Authorization tests: object-level and tenant-level access.
- Tenant isolation tests: mandatory for all tenant-owned resources.
- Frontend component tests: important forms/states, not blanket coverage.
- E2E tests: only critical journeys; introduced with Sprint 1 vertical slice.
- CI uses PostgreSQL, never SQLite as a production substitute.

Coverage percentage is not a goal. Risk coverage is the goal.
