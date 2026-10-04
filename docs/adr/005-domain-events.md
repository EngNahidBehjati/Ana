# ADR-005: Domain Events Without a Broker

**Status:** Accepted

## Context
Important business actions need decoupled reactions and may later require async processing.

## Decision
Define domain events in code when needed. Initially dispatch in-process. Do not introduce Kafka/RabbitMQ merely for future scale.

When reliable async integration becomes necessary, introduce a transactional outbox and broker behind the existing event contracts.

## Consequences
Event semantics can mature now while transport complexity is deferred.
