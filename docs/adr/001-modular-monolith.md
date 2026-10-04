# ADR-001: Modular Monolith

**Status:** Accepted

## Context
Ana needs rapid delivery by a very small team while retaining domain boundaries and a credible extraction path.

## Decision
Start as one backend deployable using a Modular Monolith. Modules own business rules/data writes and expose application contracts.

## Alternatives
- Microservices now: rejected; distributed complexity has no current justification.
- Unstructured monolith: rejected; makes future maintenance/extraction expensive.

## Consequences
Lower operational cost now; discipline is required to prevent cross-module coupling.

## Exit strategy
Extract a module when evidence shows independent scaling, release, fault, regulatory, runtime, or team-ownership needs.
