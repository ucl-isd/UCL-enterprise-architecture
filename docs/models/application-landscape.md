# Application Landscape

The application landscape maps UCL's software systems to the business capabilities they support. This view helps identify duplication, gaps, and integration opportunities.

## Application Portfolio Overview

```{mermaid}
graph LR
    subgraph Education
        SITS[SITS - Student Records]
        Moodle[Moodle - VLE]
        Turnitin[Turnitin - Plagiarism]
        Portico[Portico - Student Portal]
    end

    subgraph Research
        Worktribe[Worktribe - Grants]
        RPS[RPS - Publications]
        RDM[Research Data Store]
    end

    subgraph Professional Services
        SAP[SAP - Finance/HR]
        ServiceNow[ServiceNow - ITSM]
        Planon[Planon - Estates]
    end

    subgraph Engagement
        CRM[CRM - Alumni/Donors]
        CMS[CMS - Web Content]
    end
```

## Application Catalogue

### Tier 1 — Enterprise Systems

These are mission-critical systems with broad organisational impact.

| Application | Domain | Capability | Status |
|---|---|---|---|
| SITS | Education | Student Lifecycle | Live |
| Moodle | Education | Teaching Delivery | Live |
| SAP | Professional Services | Finance, HR | Live |
| ServiceNow | Professional Services | IT Services | Live |

### Tier 2 — Domain Systems

| Application | Domain | Capability | Status |
|---|---|---|---|
| Worktribe | Research | Grant Management | Live |
| Portico | Education | Student Lifecycle | Live |
| Planon | Professional Services | Estates & Facilities | Live |

### Tier 3 — Departmental / Specialist

:::{admonition} Work in Progress
:class: warning

The departmental application inventory is being compiled. Contributions welcome via pull request.
:::

## Integration Patterns

Key integration flows between enterprise systems:

```{mermaid}
flowchart LR
    SITS -->|Student data| Moodle
    SITS -->|Enrolment| SAP
    SAP -->|Finance| Worktribe
    ServiceNow -->|Incidents| SAP
```
