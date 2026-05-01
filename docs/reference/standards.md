# Standards

This page lists the technical and governance standards that apply to UCL's enterprise architecture.

## Technology Standards

### Identity & Access

| Standard | Requirement |
|---|---|
| Authentication | Microsoft Entra ID (SSO via SAML 2.0 or OIDC) |
| Authorisation | Role-based access control (RBAC) |
| MFA | Required for all staff and privileged access |

### Integration

| Standard | Requirement |
|---|---|
| API Style | RESTful APIs preferred; GraphQL where appropriate |
| API Documentation | OpenAPI 3.x specification required |
| Messaging | Event-driven via Azure Service Bus or equivalent |
| Data Format | JSON for APIs; CSV/Parquet for bulk data exchange |

### Data

| Standard | Requirement |
|---|---|
| Classification | UCL Data Classification Scheme (Public, Internal, Confidential, Highly Confidential) |
| Retention | Per UCL Records Retention Schedule |
| Encryption at Rest | AES-256 minimum |
| Encryption in Transit | TLS 1.2+ required |

### Hosting

| Standard | Requirement |
|---|---|
| Cloud Provider | Azure preferred; AWS and GCP permitted with justification |
| Containerisation | Docker / Kubernetes for cloud-native workloads |
| Infrastructure as Code | Terraform or Bicep for cloud resource provisioning |

## Governance Standards

### Architecture Review

All projects above £50k or introducing new technology must undergo architecture review.

### Data Protection

- Data Protection Impact Assessment (DPIA) required for personal data processing
- UK GDPR compliance mandatory
- Data Processing Agreements required for third-party processors

### Accessibility

- WCAG 2.2 Level AA compliance required
- Accessibility statement required for public-facing services
