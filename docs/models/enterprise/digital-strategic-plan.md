# Digital Strategic Plan Metamodel

The {term}`Digital Strategic Plan` sets out UCL's digital ambitions and objectives over a seven-year horizon (2026–32). It provides oversight of future investment needs, helps prioritise competing activity, and promotes guiding Digital Principles for consistent decision-making across the university.

The metamodel below describes how the strategic planning elements are structured and related. These elements are documented in Essential (EAS), our enterprise architecture tool, using its standard object types mapped to UCL-specific terminology.

The full strategic plan data can be explored in the [Strategic Roadmap Dashboard](https://ucl.essentialintelligence.com/viewer/8b3b72ca41670a212b09_1/report?XML=reportXML.xml&XSL=user/strategic_roadmap.xsl&LABEL=Strategic%20Roadmap%20Dashboard&cl=en-gb) in Essential.

## EAS to UCL Mapping

| EAS Element | UCL Term |
|---|---|
| {term}`Business Driver` | 4 areas in 22–27 strategic plan |
| {term}`Business Goal` | UCL Objectives (the 3 or 4 priorities for that business area) |
| {term}`Business Objective` | long running objectives over the next 7 years |
| {term}`Strategic Plan` | UCL Strategic Initiative - a long running programme of change consisting may be linked to many lean business cases and Epics in delivery |
| {term}`Performance Indicator` | {term}`KPI` |
| {term}`Roadmap` | Roadmap |

## Metamodel Relationships

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
All terms link to the {doc}`../../reference/glossary` where full definitions and UCL context are provided.
:::

## Example — Academic Excellence and Impact

An instance of the metamodel using the Academic Excellence and Impact strategic area:

```{mermaid}
graph TD
    BD["Academic Excellence\nand Impact"]
    BG["Enhancing the creation of\nresearch & excellent outputs"]
    BO["Elevate data- and compute-intensive\nresearch through powerful technology\nplatforms and expertise"]
    SP["Evolve UCL's flexible and scalable\nresearch computing platform"]
    BM["Research"]
    RM["Research Roadmap"]
    PI["REF Overall"]

    BD --> BG
    BG --> BO
    BO --> SP
    BO --> BM
    BM --> RM
    BM --> PI
    SP --> RM

    click BO "https://ucl.essentialintelligence.com/viewer/8b3b72ca41670a212b09_1/report?XML=reportXML.xml&PMA=store_39_Class140029&cl=en-gb&XSL=business/core_bl_bus_obj_summary.xsl&PAGEXSL=&LABEL=store_39_Class140029Link" "View in Essential"
    click SP "https://ucl.essentialintelligence.com/viewer/8b3b72ca41670a212b09_1/report?XML=reportXML.xml&PMA=store_39_Class160017&cl=en-gb&XSL=enterprise%2Fcore_el_strategic_plan_summary.xsl&PAGEXSL=&LABEL=Strategic+Plan+Summary+-store_39_Class160017Link%26xsl%3D&essscope=W10%253D" "View in Essential"
```
