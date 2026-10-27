# ADR-0001: Backend-Architecture (Architecture Decision Record)

## Status
Proposed

## Context
Ana is a real estate collaboration platform.
The backend is being developed by a small team, and our current priority is delivering the MVP.
The system includes multiple business domains such as agencies, properties, listings, collaborations, and deals.
We need an architecture that is simple to develop and deploy while maintaining clear boundaries between business modules.

## Decision
We will use a Modular Monolith architecture for the Ana backend.
The system will be organized into independent business modules with explicit boundaries.
We may consider extracting some modules into microservices in the future if there is a clear technical or business need.

## Alternatives
* Unstructured Monolith
A single application with few enforced module boundaries.
Advantage: Simple initial setup.
Disadvantage: Higher risk of tightly coupled business logic as the project grows.

* Microservices
Multiple independently deployable services communicating through network interfaces or messaging.
Advantages: Independent deployment and scaling of individual services.
Disadvantages: Increased infrastructure, distributed communication, observability, testing, and data-consistency complexity.

* Modular Monolith — Selected
A single deployable backend with explicit internal business module boundaries.
This provides a balance between development simplicity and maintainable separation of responsibilities.


## Reasons
- The team is small, and development capacity should focus on delivering the MVP.
- A single backend deployment reduces initial operational complexity.
- In-process communication between modules avoids unnecessary distributed-system complexity.
- Transactions involving multiple modules can be coordinated within one database when appropriate.
- Explicit business boundaries support maintainability and testing.
- Independent service extraction remains an option if future requirements justify it.

## Architectural Principles

Modules should be organized around business capabilities, not individual database tables.
Each module owns its domain rules and business operations.
Cross-module interactions should use explicit contracts or public application interfaces.
Modules should not directly modify another module's persistent data.
Business logic should remain separate from HTTP-specific and database-specific concerns.
Dependencies on infrastructure should be isolated where practical.
Transaction boundaries must be explicitly defined for business operations.
Architectural complexity should be introduced when justified by real requirements.

## Consequences
* Positive

Simpler local development and deployment.
Lower initial infrastructure and operational costs.
Easier integration testing than in a distributed architecture.
Opportunities for transactional consistency within PostgreSQL.
Clearer ownership of business responsibilities.

* Negative / Trade-offs

Modules cannot be deployed independently by default.
Module boundaries require discipline, code review, and automated checks.
Shared application resources can create performance dependencies between modules.
Cross-module operations may still introduce unwanted coupling if poorly designed.
Future migration to microservices may require changes to data ownership, transactions, and communication patterns.

## Future Reconsideration

We will reconsider this architecture when there is evidence of requirements such as:

- Independent deployment needs for particular business capabilities.
- Different scaling requirements between modules.
- Increased team autonomy and ownership. 
- Operational or reliability limitations that cannot be reasonably addressed within the modular monolith.
- Migration to microservices will be an evidence-based decision, not a predefined milestone.

## Related Decisions

Future ADRs may document:

- Domain module boundaries.
- Database and transaction management.
- Authentication and agency-context authorization.
- Cross-module communication conventions.

