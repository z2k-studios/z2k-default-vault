---
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_author: "Z2K Studios, LLC"
z2k_template_suggested_title: "{{ConciseSummary}}"
---
{{fieldInfo ConciseSummary "What is this card about?" type="text" directives="required"}}
{{fieldInfo OverviewDetails "Overview?" type="text"}}
{{fieldInfo PrerequisitesForUnderstanding "Prerequisites for understanding?" type="text"}}
{{fieldInfo FurtherDetails "Further details?" type="text"}}

{{ConciseSummary}}

---
# Overview
{{OverviewDetails}}

# Prerequisites
{{PrerequisitesForUnderstanding}}

# Details
{{FurtherDetails}}

{{!-- To include Card Fabric: {{> "Card Fabric"}} --}}
