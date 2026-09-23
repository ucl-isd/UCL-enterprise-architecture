# Institutional Risk Metamodel

The relationships between risks, assessments, controls, and stakeholders in
{term}`Essential (EAS)`.

:::{note}
Stub — relationships confirmed against the live model; narrative to follow.
:::

```{mermaid}
classDiagram
    class Risk
    class Risk_Category
    class Risk_Assessment
    class Risk_Impact
    class Control
    class Performance_Measure
    class Service_Quality_Value
    class Individual_Business_Role
    class ACTOR_TO_ROLE_RELATION
    class Actor
    class Roadmap
    class Enterprise_Strategic_Plan

    Risk --> Risk_Category : risk_category
    Risk --> Risk : risk_leading_to (causes)
    Risk --> Control : risk_related_control
    Risk --> Roadmap : risk_related_support
    Risk --> Enterprise_Strategic_Plan : risk_related_support
    Risk --> Individual_Business_Role : stakeholders
    Individual_Business_Role --> ACTOR_TO_ROLE_RELATION : stakeholders
    ACTOR_TO_ROLE_RELATION --> Actor : act_to_role_from_actor
    Risk_Assessment --> Risk : ra_assessed_risk
    Risk_Assessment --> Risk_Impact : ra_risk_impact
    Control --> Performance_Measure : performance_measures
    Performance_Measure --> Service_Quality_Value : pm_performance_value
```

**Control RAG chain:** `Control` → `performance_measures` → `Performance_Measure`
→ `pm_performance_value` → `Service_Quality_Value.name` (e.g. "Control RAG - Amber").
