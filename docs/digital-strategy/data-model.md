# Digital Strategy Data Model

Where the {doc}`metamodel` describes the strategy in conceptual UCL terms
(Driver → Goal → Objective), this page documents the **concrete implementation**
in {term}`Essential (EAS)` — the actual classes and their `slot_reference` values
as held in the live model.

:::{note}
Slot names below are the authoritative `slot_reference` values, confirmed against
the live model. Instances are `simple_instance` nodes; every relationship is an ID
reference resolved by matching `name`.
:::

## Strategic planning classes

| Class | Key slots | Notes |
| :--- | :--- | :--- |
| `Enterprise_Strategic_Plan` | `name`, `description`, `short_description`, `performance_measures`, `valid_start_date`, `valid_end_date`, `plan_status` | A Digital Strategic Plan (DSP) initiative |
| `Roadmap` | `name`, `description`, `roadmap_strategic_plans` | Groups plans (e.g. "Technical Capability — Initiatives") |
| `Performance_Measure` (supertype) | `pm_category`, `pm_performance_value` | Carries plan priority, control RAG, etc. |
| `Performance_Measure_Category` | `name` | e.g. "Priority" |
| `Service_Quality_Value` (supertype) | `name`, `service_quality_value_score` | The measured value (e.g. "P1") |

```{mermaid}
classDiagram
    class Enterprise_Strategic_Plan
    class Roadmap
    class Performance_Measure
    class Performance_Measure_Category
    class Service_Quality_Value

    Roadmap --> Enterprise_Strategic_Plan : roadmap_strategic_plans
    Enterprise_Strategic_Plan --> Performance_Measure : performance_measures
    Performance_Measure --> Performance_Measure_Category : pm_category
    Performance_Measure --> Service_Quality_Value : pm_performance_value
```

**Plan priority chain:** `Enterprise_Strategic_Plan` → `performance_measures` →
`Performance_Measure` → `pm_performance_value` → `Service_Quality_Value.name`
(e.g. "P1").

## Cost cross-links

Strategic plans carry cost through the `Cost` class, which links a cost to an
element (a plan or an application) and breaks it down into per-year components.

| Class | Key slots | Notes |
| :--- | :--- | :--- |
| `Cost` | `cost_for_elements`, `cost_components` | Links a cost to an element (plan/app) |
| `Adhoc_Cost_Component` / `Annual_Cost_Component` | `cc_cost_amount`, `cc_cost_start_date_iso_8601`, `cc_cost_end_date_iso_8601`, `cc_cost_component_of_cost`, `description` | Per-year cost lines |

```{mermaid}
classDiagram
    class Enterprise_Strategic_Plan
    class Cost
    class Cost_Component

    Cost --> Enterprise_Strategic_Plan : cost_for_elements
    Cost --> Cost_Component : cost_components
```

## Risk cross-links

Risks reference strategic plans and roadmaps through the `Risk.risk_related_support`
slot, which mixes both. The full risk model is documented in
{doc}`../institutional-risk/index`.

```{mermaid}
classDiagram
    class Risk
    class Roadmap
    class Enterprise_Strategic_Plan

    Risk --> Enterprise_Strategic_Plan : risk_related_support
    Risk --> Roadmap : risk_related_support
```

:::{note}
`risk_related_support` mixes Roadmaps and Plans in a single slot — resolve each
reference by matching `name` against both class types.
:::
