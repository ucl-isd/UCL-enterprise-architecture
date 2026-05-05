# Business Architecture

## Digital Strategic Plan Metamodel

The Digital Strategic Plan metamodel describes how UCL's strategic planning elements are structured and related. These elements are documented in Essential (EAS), our enterprise architecture tool, using its standard object types mapped to UCL-specific terminology.

### EAS to UCL Mapping

| EAS Element | UCL Term |
|---|---|
| {term}`Business Driver` | 4 areas in 22–27 strategic plan |
| {term}`Business Goal` | UCL Objective (4 big things) |
| {term}`Business Objective` | UCL Capability |
| {term}`Strategic Plan` | UCL Strategic Initiative |
| {term}`Performance Indicator` | {term}`KPI` |
| {term}`Roadmap` | Roadmap |

### Metamodel Relationships

```{mermaid}
graph TD
    BD[Business Driver]
    BG[Business Goal]
    BO[Business Objective]
    SP[Strategic Plan]
    PI[Performance Indicator]
    RM[Roadmap]

    BD --> BG
    BG --> BO
    BG --> PI
    BO --> PI
    BO --> SP
    SP --> RM
    PI -.-> RM
```

:::{tip}
All terms link to the {doc}`../reference/glossary` where full definitions and UCL context are provided.
:::
