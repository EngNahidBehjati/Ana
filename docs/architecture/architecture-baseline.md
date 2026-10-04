# Architecture Baseline v1

## Style

Modular Monolith. One deployable backend initially, with explicit domain ownership and contract-based cross-module access.

## Non-negotiable rules

1. Business rules live with the owning module.
2. Commercial access/limits are evaluated through Entitlements, not hard-coded plan names inside features.
3. Accepted agreements and business-significant events are versioned/auditable.
4. Cross-module communication goes through public application contracts; modules do not mutate each other's internals.
5. PostgreSQL is the transactional source of truth.
6. Redis is optional infrastructure for cache/ephemeral coordination, never authoritative business state.
7. Extraction to a service is driven by demonstrated operational/organizational need, not anticipated scale.

## Runtime

- FastAPI application
- SQLAlchemy 2.x
- PostgreSQL
- React/TypeScript web application
- Redis only when a concrete use case appears

## API

- Versioned HTTP prefix: `/api/v1`
- FastAPI/Pydantic produce OpenAPI.
- Frontend client/types will be generated from OpenAPI from Sprint 1.

## Data ownership

Each module owns writes to its tables. Foreign keys across logical modules are allowed while the system is a monolith when they protect integrity, but cross-module business logic must not depend on ORM graph traversal.
