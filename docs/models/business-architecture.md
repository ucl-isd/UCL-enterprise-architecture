# Business Architecture

## Digital Strategic Plan Metamodel

The {term}`Digital Strategic Plan` metamodel describes how UCL's strategic planning elements are structured and related. These elements are documented in Essential (EAS), our enterprise architecture tool, using its standard object types mapped to UCL-specific terminology.

### EAS to UCL Mapping

| EAS Element | UCL Term |
|---|---|
| {term}`Business Driver` | 4 areas in 22–27 strategic plan |
| {term}`Business Goal` | UCL Objectives (the 3 or 4 priorities for that business area) |
| {term}`Business Objective` | long running objectives over the next 7 years |
| {term}`Strategic Plan` | UCL Strategic Initiative - a long running programme of change consisting may be linked to many lean business cases and Epics in delivery |
| {term}`Performance Indicator` | {term}`KPI` |
| {term}`Roadmap` | Roadmap |

### Metamodel Relationships

```{mermaid}
erDiagram
    BUSINESS-DRIVER ||--|| BUSINESS-GOAL : drives
    BUSINESS-GOAL ||--o{ BUSINESS-OBJECTIVE : "decomposes to"
    BUSINESS-OBJECTIVE }o--o{ STRATEGIC-PLAN : "realised by"
    BUSINESS-OBJECTIVE }o--o{ PERFORMANCE-INDICATOR : "measured by"
    BUSINESS-OBJECTIVE }o--|| BUSINESS-MODEL : "part of"
    BUSINESS-MODEL ||--o{ PERFORMANCE-INDICATOR : "tracked by"
    BUSINESS-MODEL ||--|| ROADMAP : "planned on"
    STRATEGIC-PLAN }o--|| ROADMAP : "scheduled on"
```




:::{tip}
All terms link to the {doc}`../reference/glossary` where full definitions and UCL context are provided.
:::
