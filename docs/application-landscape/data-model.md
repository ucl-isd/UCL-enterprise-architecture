# Application Landscape Data Model

The concrete {term}`Essential (EAS)` classes and `slot_reference` values for the
application portfolio.

:::{note}
Stub — slot names are authoritative; descriptions and worked examples to follow.
:::

## Application portfolio

| Class | Key slots | Notes |
| :--- | :--- | :--- |
| `Application_Capability` | `name`, `description`, `contained_app_capabilities`, `element_classified_by` | Top of the tree |
| `Application_Service` / `Composite_Application_Service` | `name`, `description`, `realises_application_capabilities`, `provided_by_application_provider_roles`, `supports_business_process_appsvc` | Realises capabilities |
| `Application_Provider_Role` | `role_for_application_provider`, `implementing_application_service` | Join between service and app |
| `Application_Provider` / `Composite_Application_Provider` | `name`, `description`, `ap_supplier`, `ap_delivery_model`, `ap_disposition_lifecycle_status` (TIME), `contained_application_providers`, `ap_static_architecture` | The app; modules via `contained_application_providers` |
| `Managed_Service` | `name`, `description`, `ms_criticality`, `ms_managed_app_elements`, `stakeholders` | "al managed by services" |
| `Managed_Service_Criticality` | `name` | e.g. "Tier 1b" |
| `Supplier` | `name`, `supplier_owned_application_providers` | Via `ap_supplier` |
| `Application_Delivery_Model` | `name` | e.g. "Private Cloud Service" |

- **TIME status**: `Application_Provider.ap_disposition_lifecycle_status` → disposition enum
  (Invest / Tolerate / Migrate / Eliminate).
- **Managed service stakeholders**: `Managed_Service.stakeholders` →
  `ACTOR_TO_ROLE_RELATION` → `act_to_role_from_actor` (actor) + `act_to_role_to_role` (role).

## Data flows

| Class | Key slots | Notes |
| :--- | :--- | :--- |
| `Static_Application_Provider_Usage` | `static_usage_of_app_provider`, `used_in_static_app_provider_architecture` | An app's presence in a static architecture |
| `APU-TO-APU-STATIC-RELATION` | `FROM`, `TO` (usages), `relation_label`, `relation_name`, `apu_to_apu_relation_inforeps` | The directed A→B connection |
| `APP_PRO_TO_INFOREP_RELATION` | `app_pro_to_inforep_to_inforep` | The data crossing the link |
| `Information_Representation` | `name` | The information (→ Views → Data Objects) |
| `Application_Provider_Interface` | `name` | Interfaces modelled as nodes alongside apps |
