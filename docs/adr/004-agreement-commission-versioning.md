# ADR-004: Versioned Agreements and Commission Terms

**Status:** Accepted

## Context
Commission and collaboration terms need flexibility, mutual consent, dispute traceability, and future extensibility.

## Decision
Agreement changes create versions. Acceptance is explicit per party. An accepted version is immutable. Commission uses stable structured fields plus schema-versioned extension data for uncommon future terms.

## Rejected
- Hard-coded A/B percentages: too rigid.
- Generic contract/rules engine: premature complexity.
- Entire commission payload as opaque JSON: harms validation/reporting.

## Consequences
Historical deals remain interpretable even after future business-model changes.
