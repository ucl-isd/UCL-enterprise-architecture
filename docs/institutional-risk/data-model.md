# Institutional Risk Data Model

The concrete {term}`Essential (EAS)` classes and `slot_reference` values for
institutional risk.

:::{note}
Stub — slot names are authoritative; descriptions and worked examples to follow.
:::

| Class | Key slots | Notes |
| :--- | :--- | :--- |
| `Risk` | `name`, `description`, `short_description`, `risk_category`, `risk_leading_to`, `risk_related_control`, `risk_related_support`, `stakeholders` | `risk_leading_to` = causes (other Risks); `risk_related_support` mixes Roadmaps + Plans |
| `Risk_Category` | `name` | e.g. "UCL Strategic Risk Area" |
| `Risk_Assessment` | `ra_assessed_risk`, `ra_assessment_date_ISO8601`, `ra_risk_probability` (0-100), `ra_risk_impact`, `description` ("Inherent"/"Residual") | Two per risk (inherent + residual) |
| `Risk_Impact` | `name`, `enumeration_value`, `enumeration_score` (1-4) | Impact severity enum |
| `Control` | `name`, `description`, `performance_measures` | Effectiveness stored as a perf measure (RAG) |
| `Individual_Business_Role` | `name` ("Risk Owner"/"Risk Manager"), `stakeholders` | Stakeholder role on the risk |
| `ACTOR_TO_ROLE_RELATION` | `act_to_role_from_actor`, `act_to_role_to_role`, `relation_name` | Links role to the actual actor |
| `Actor` (Individual/Group) | `name` | The person/team |

:::{note}
`ACTOR_TO_ROLE_RELATION` class name varies in places (`Actor_To_Role_Relationship`);
match on presence of the `act_to_role_from_actor` slot rather than the exact type name.
:::
