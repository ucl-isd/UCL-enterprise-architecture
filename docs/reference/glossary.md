# Glossary

Common terms used in the UCL Digital Architecture Library.

```{glossary}
Business Driver
  A top-level strategic force that shapes organisational direction. At UCL, Business Drivers correspond to the four areas defined in the 2022–27 strategic plan. Modelled as **Business Driver** in Essential (EAS).

Business Goal
  A high-level objective that the organisation aims to achieve. At UCL, Business Goals are the "4 big things" — the UCL Objectives. Each is driven by one or more Business Drivers. Modelled as **Business Goal** in Essential (EAS).

Business Objective
  A specific outcome required to deliver on a Business Goal. At UCL, Business Objectives represent UCL Capabilities. They are measured by KPIs and realised through Strategic Initiatives. Modelled as **Business Objective** in Essential (EAS).

Cost
  An Essential (EAS) class linking a cost to an element (a strategic plan or application) via `cost_for_elements`, broken down into per-year `cost_components`.

Enterprise_Strategic_Plan
  The Essential (EAS) class representing a Digital Strategic Plan (DSP) initiative. Key slots include `valid_start_date`, `valid_end_date`, `plan_status`, and `performance_measures`. Grouped by Roadmaps and the concrete implementation of the conceptual {term}`Strategic Plan`.

Performance Measure
  An Essential (EAS) supertype (`Performance_Measure`) that carries a measured value against an element — for example a plan's priority or a control's RAG status — via `pm_category` and `pm_performance_value`.

Digital Strategic Plan
  The UCL Digital Strategic Plan 2026–32 sets out the university's strategic ambitions and objectives over seven years, and outlines the high-level digital activity needed to support these goals. It is jointly developed by the Office of the Chief Information Officer, the Office for the President & Provost and Strategic Change, and co-created with the broader UCL community. The plan provides oversight of future investment needs, helps prioritise and sequence competing activity, and promotes a set of guiding Digital Principles for consistent decision-making. See [UCL Digital Strategic Plan 2026-32](https://www.ucl.ac.uk/isd/about-ucl-isd/digital-strategy-under-development).

Essential (EAS)
  Essential (Essential Architecture Suite / Essential Cloud), UCL's enterprise architecture tool. Strategy elements are documented using Essential's standard object types mapped to UCL-specific terminology. See [Essential](https://ucl.essentialintelligence.com/).

KPI
  [UCL institutional KPI](https://liveuclac.sharepoint.com/sites/UCLstrategicplan/SitePages/UCL's-Key-Performance-Indicators.aspx)

Performance Indicator
  See {term}`KPI`.

Roadmap
  A time-based delivery view showing when Strategic Initiatives will be executed. Roadmaps are generated from Strategic Plans. Modelled as **Roadmap** in Essential (EAS).

Strategic Plan
  A concrete initiative that implements the strategy by building or improving capabilities. At UCL, Strategic Plans correspond to UCL Strategic Initiatives. Each feeds into a Roadmap for delivery planning. Modelled as **Strategic Plan** in Essential (EAS).
```
