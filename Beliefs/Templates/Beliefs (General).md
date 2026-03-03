---
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_author: "Geoff (z2k-gwp)"
z2k_template_suggested_title: "{{ConciseSummary}}"
z2k_card_source_type: ".:Z2K/SourceType/LifeLessons"
---
{{fieldInfo ConciseSummary "Briefly, what is this belief?" type="text" directives="required"}}
{{fieldInfo OverviewDetails "Describe this belief in detail" type="text"}}
{{fieldInfo PrerequisitesForUnderstanding "What do you need to know to understand this?" type="text"}}
{{fieldInfo FurtherDetails "Any additional details?" type="text"}}

{{ConciseSummary}}

---

# Overview
{{OverviewDetails}}

# Prerequisites
{{PrerequisitesForUnderstanding}}

# Details
{{FurtherDetails}}

{{!-- To include Card Fabric: {{> "Card Fabric"}} --}}
