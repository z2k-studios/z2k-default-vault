---
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_author: "Z2K Studios, LLC"
z2k_template_suggested_title: "{{ConciseSummary}}"
z2k_card_source_type: ".:Z2K/SourceType/Unknown"
---
{{fieldInfo ConciseSummary "Provide a concise summary for this information card:" type="text" directives="required"}}
{{fieldInfo OverviewDetails "Overview details:" type="text"}}
{{fieldInfo FurtherDetails "Further details:" type="text"}}
{{ConciseSummary}}

---

# Overview
{{OverviewDetails}}

# Details
{{FurtherDetails}}

{{!-- To include Card Fabric: {{> "Card Fabric"}} --}}
