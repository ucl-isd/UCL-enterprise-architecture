# Data Architecture

The data architecture model describes UCL's key data entities, their ownership, and how data flows between systems.

## Conceptual Data Model

```{mermaid}
erDiagram
    STUDENT ||--o{ ENROLMENT : has
    PROGRAMME ||--o{ ENROLMENT : offers
    STUDENT ||--o{ ASSESSMENT : takes
    STAFF ||--o{ MODULE : teaches
    PROGRAMME ||--o{ MODULE : contains
    STAFF ||--o{ RESEARCH_PROJECT : leads
    RESEARCH_PROJECT ||--o{ GRANT : funded_by
    DEPARTMENT ||--o{ STAFF : employs
    FACULTY ||--o{ DEPARTMENT : contains
```

## Data Domains

### Student Data

Owner
: Student Records & Systems

Systems of Record
: SITS, Portico

Key Entities
: Student, Enrolment, Programme, Module, Assessment

### Research Data

Owner
: Research Services

Systems of Record
: Worktribe, RPS

Key Entities
: Research Project, Grant, Publication, Research Output

### Financial Data

Owner
: Finance Division

Systems of Record
: SAP

Key Entities
: Cost Centre, General Ledger, Purchase Order, Invoice

### People Data

Owner
: Human Resources

Systems of Record
: SAP HR

Key Entities
: Employee, Contract, Department, Role

## Data Governance

:::{important}
All data handling must comply with UCL's Data Protection Policy and UK GDPR requirements. See {doc}`../reference/standards` for applicable standards.
:::

## Data Flow Summary

| Source | Target | Data | Frequency |
|---|---|---|---|
| SITS | Moodle | Student enrolments | Daily |
| SITS | SAP | Student fee data | Termly |
| SAP | Worktribe | Cost centre data | Weekly |
| HR (SAP) | ServiceNow | Staff records | Daily |
