# Architecture Principles

These principles guide architecture decisions across UCL. They are aligned with UCL's strategic objectives and provide a framework for evaluating technology choices.

## Core Principles

### 1. Cloud-First

Adopt cloud-hosted solutions by default. On-premises hosting requires explicit justification.

Rationale
: Cloud services offer scalability, resilience, and reduced operational burden.

Implications
: New projects must evaluate cloud options before considering on-premises. Existing systems should have a cloud migration path.

### 2. Buy Before Build

Prefer commercial off-the-shelf (COTS) or SaaS solutions over custom development.

Rationale
: Custom software carries long-term maintenance costs and key-person risk.

Implications
: Custom development is appropriate only when no suitable product exists or when the capability is a genuine differentiator.

### 3. Data as a Shared Asset

Data is owned by the organisation, not by individual systems or teams.

Rationale
: Siloed data leads to duplication, inconsistency, and poor decision-making.

Implications
: Systems must expose data via APIs. Master data sources must be clearly identified.

### 4. Design for Integration

Systems must be designed to integrate with the wider enterprise, not operate in isolation.

Rationale
: Isolated systems create manual workarounds and data quality issues.

Implications
: All new systems must support standard integration patterns (APIs, event-driven messaging).

### 5. Security by Design

Security and data protection must be considered from the outset, not bolted on.

Rationale
: Retrofitting security is expensive and often incomplete.

Implications
: Architecture reviews must include threat modelling. Systems handling personal data must complete a DPIA.

### 6. Reuse Before Reinvent

Leverage existing platforms, services, and patterns before introducing new ones.

Rationale
: Reducing technology sprawl lowers cost and complexity.

Implications
: Architecture review is required before procuring new platforms that overlap with existing capabilities.

### 7. Accessibility and Inclusion

All digital services must be accessible to the widest possible audience.

Rationale
: UCL has legal obligations under the Equality Act 2010 and a commitment to inclusion.

Implications
: Services must meet WCAG 2.2 AA as a minimum. Accessibility testing must be part of delivery.
