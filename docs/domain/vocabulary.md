# Domain Vocabulary v1

This vocabulary is intentionally small. Terms are refined as discovery and implementation produce evidence.

- **User**: A person authenticated in Ana.
- **Agency**: A real-estate business participating in the network. Primary tenant boundary.
- **Membership**: Relationship between a User and an Agency, including role/status.
- **Property**: The underlying real-world property. Sensitive source data may be more private than a published Listing.
- **Listing**: Supply-side offer published by an Agency for sale/rent/transfer or another supported transaction type.
- **Requirement**: Demand-side need published by an Agency on behalf of a buyer/renter/participant.
- **Discovery**: Search/browse/match behavior over Listings and Requirements.
- **Collaboration**: Structured relationship between agencies around a Listing or Requirement.
- **Agreement**: Versioned mutually accepted terms governing a Collaboration.
- **Commission Terms**: Commercial terms within an Agreement. Flexible but not a generic rules engine.
- **Deal**: Transaction outcome that follows an accepted Agreement.
- **Entitlement**: A capability or quota an Agency is allowed to use, independent of plan names.
- **Plan**: Commercial packaging of Entitlements; mutable over product lifetime.
- **Subscription**: Assignment of a Plan/version to an Agency for a time period.
- **Usage**: Measured consumption used for limits, analytics, or future billing.
- **Trust Evidence**: Contextual fact/event related to behavior, listing accuracy, agreements, disputes, or deals. Not a single score.
- **Audit Event**: Immutable record of a security/business-significant action.
- **Tenant**: An Agency for data-isolation purposes in the initial model.
