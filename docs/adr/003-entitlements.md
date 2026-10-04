# ADR-003: Entitlement-Oriented Monetization

**Status:** Accepted

## Context
Business model may move from free usage to quotas, subscriptions, tiers, or hybrid charging. Feature code must not encode plan names.

## Decision
Separate Plan, Subscription, Entitlement, and Usage concepts. Features ask capability/quota questions such as `search.execute` or `search.daily_limit`.

Initial entitlement types are only:
- boolean capability
- numeric quota

A general rules engine is explicitly out of scope.

## Consequences
Commercial packaging can change without rewriting feature logic. A policy/evaluator boundary exists without speculative complexity.
