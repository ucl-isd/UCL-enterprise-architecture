# Application Landscape Metamodel

The relationships between capabilities, services, applications, and managed
services in {term}`Essential (EAS)`.

:::{note}
Stub — relationships confirmed against the live model; narrative to follow.
:::

```{mermaid}
classDiagram
    class Application_Capability
    class Application_Service
    class Application_Provider_Role
    class Application_Provider
    class Managed_Service
    class Managed_Service_Criticality
    class Supplier
    class Application_Delivery_Model

    Application_Service --> Application_Capability : realises_application_capabilities
    Application_Service --> Application_Provider_Role : provided_by_application_provider_roles
    Application_Provider_Role --> Application_Provider : role_for_application_provider
    Application_Provider --> Application_Provider : contained_application_providers (modules)
    Application_Provider --> Supplier : ap_supplier
    Application_Provider --> Application_Delivery_Model : ap_delivery_model
    Managed_Service --> Application_Service : ms_managed_app_elements
    Managed_Service --> Managed_Service_Criticality : ms_criticality
```

## Application-to-application data flows

Directed connections between applications, carrying the information that flows
across them (the static architecture).

```{mermaid}
classDiagram
    class Application_Provider
    class Static_Application_Provider_Usage
    class APU_TO_APU_STATIC_RELATION
    class APP_PRO_TO_INFOREP_RELATION
    class Information_Representation

    Application_Provider --> Static_Application_Provider_Usage : ap_static_architecture / static_usage_of_app_provider
    APU_TO_APU_STATIC_RELATION --> Static_Application_Provider_Usage : FROM / TO
    APU_TO_APU_STATIC_RELATION --> APP_PRO_TO_INFOREP_RELATION : apu_to_apu_relation_inforeps
    APP_PRO_TO_INFOREP_RELATION --> Information_Representation : app_pro_to_inforep_to_inforep
```

**Resolving "sends to / receives from" for an app:**

1. Find the app's `Static_Application_Provider_Usage` instances (usage where
   `static_usage_of_app_provider` = the app; an app may have several, one per architecture).
2. **Sends to** = `APU-TO-APU-STATIC-RELATION` where `FROM` is one of those usages →
   resolve `TO` usage → its app.
3. **Receives from** = edges where `TO` is one of those usages → resolve `FROM` usage → its app.
4. **Data** crossing each edge = `apu_to_apu_relation_inforeps` → `APP_PRO_TO_INFOREP_RELATION`
   → `Information_Representation`.
