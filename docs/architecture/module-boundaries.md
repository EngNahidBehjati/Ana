# Module Boundaries v1

## Core modules

| Module | Owns | May depend on |
|---|---|---|
| Identity | user identity/authentication | Shared |
| Agency | agency + membership lifecycle | Identity, Shared |
| Authorization | permission decisions | Identity, Agency |
| Property | sensitive property facts | Agency |
| Listing | supply publication lifecycle | Property, Agency, Entitlement |
| Requirement | demand publication lifecycle | Agency, Entitlement |
| Discovery | query/read models | Listing, Requirement, Entitlement |
| Collaboration | collaboration state machine | Listing/Requirement contracts, Agency |
| Agreement | versioned mutual terms | Collaboration |
| Deal | transaction outcome | Agreement |
| Commission | commission terms/status | Agreement, Deal |
| Entitlement | capability/quota decisions | Agency |
| Trust | trust evidence/events | Agency + domain references |
| Notification | delivery orchestration | domain events |
| Audit | security/business audit records | domain events |
| Administration | operational workflows | public module contracts |

## Extraction rule

A module becomes a service only after evidence of at least one of: independent scaling, independent release cadence, fault isolation need, regulatory boundary, materially different runtime, or independent team ownership.
