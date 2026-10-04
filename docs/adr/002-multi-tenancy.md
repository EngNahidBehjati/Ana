# ADR-002: Multi-Tenancy Baseline

**Status:** Accepted

## Context
Ana is B2B and Agency data must be isolated. ID manipulation must never expose another Agency's private resource.

## Decision
Agency is the initial tenant boundary. Shared PostgreSQL is used. Tenant ownership and object-level authorization are explicit in application rules and tests.

## Alternatives
- Database per tenant: rejected for MVP operational cost.
- Schema per tenant: rejected for migration/operations complexity.
- PostgreSQL RLS immediately: deferred; useful defense-in-depth later, but not a substitute for application authorization.

## Consequences
Every tenant-owned feature must define tenant ownership and isolation tests.
