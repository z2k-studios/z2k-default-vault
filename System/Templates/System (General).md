---
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_suggested_title: "{{ConciseSummary}}"
---
{{fieldInfo ConciseSummary "Briefly, what is this system card about?" type="text" directives="required"}}
{{fieldInfo OverviewDetails "Describe in more detail" type="text"}}
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
