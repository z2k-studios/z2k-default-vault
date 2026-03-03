---
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_author: "Z2K Studios, LLC"
z2k_template_suggested_title: "{{ConciseSummary}}"
z2k_card_source_type: ".:Z2K/SourceType/InternalThought"
---
{{fieldInfo ConciseSummary "Briefly, what is this thought?" type="text" directives="required"}}
{{fieldInfo OverviewDetails "Describe this thought in more detail" type="text"}}
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
