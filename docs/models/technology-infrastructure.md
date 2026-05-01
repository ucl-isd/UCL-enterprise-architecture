# Technology Infrastructure

This model describes UCL's technology infrastructure layers, hosting environments, and network architecture.

## Infrastructure Layers

```{mermaid}
graph TB
    subgraph Cloud["Cloud Services"]
        Azure[Microsoft Azure]
        AWS[AWS]
        GCP[Google Cloud]
    end

    subgraph OnPrem["On-Premises"]
        DC[UCL Data Centres]
        HPC[HPC Clusters]
    end

    subgraph Network["Network"]
        JANET[JANET]
        Campus[Campus Network]
        VPN[VPN Services]
    end

    Cloud --> Network
    OnPrem --> Network
```

## Hosting Strategy

UCL operates a hybrid hosting model:

Cloud-first
: New workloads default to cloud hosting unless there is a specific reason for on-premises.

On-premises
: Legacy systems and high-performance computing remain on-premises where appropriate.

Hybrid
: Some workloads span both environments, using cloud for burst capacity.

## Platform Services

| Service | Platform | Purpose |
|---|---|---|
| Identity & Access | Microsoft Entra ID | Authentication, SSO |
| Email & Collaboration | Microsoft 365 | Email, Teams, SharePoint |
| Web Hosting | Azure / AWS | Public-facing web services |
| HPC | On-premises clusters | Research computing |
| Storage | Azure Blob / On-prem SAN | Data storage |
| Monitoring | Datadog / Azure Monitor | Observability |

## Network Architecture

UCL connects to the internet and research networks via JANET (Joint Academic Network). The campus network provides wired and wireless connectivity across all UCL sites.

### Key Network Zones

- **Public DMZ** — Internet-facing services
- **Internal** — Staff and student services
- **Restricted** — Sensitive data and systems
- **Research** — Dedicated research network segments

## Disaster Recovery

:::{admonition} DR Classification
:class: tip

Systems are classified into DR tiers based on their Recovery Time Objective (RTO) and Recovery Point Objective (RPO):

| Tier | RTO | RPO | Examples |
|---|---|---|---|
| Platinum | < 1 hour | < 15 min | Identity, Email |
| Gold | < 4 hours | < 1 hour | Student Records, Finance |
| Silver | < 24 hours | < 4 hours | Departmental systems |
| Bronze | < 72 hours | < 24 hours | Non-critical services |
:::
