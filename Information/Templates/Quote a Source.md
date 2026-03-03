---
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_suggested_title: "{{ConciseSummary}}"
z2k_card_source_type: ".:Z2K/SourceType/Person"
---
{{fieldInfo ConciseSummary "Provide a concise summary:" type="text" directives="required"}}
{{fieldInfo Quote "The quote or paraphrase:" type="text" directives="required"}}
{{fieldInfo Context "Context and details:" type="text"}}
{{fieldInfo Source "Source of the quote:" type="text"}}
{{ConciseSummary}}

---

# Quote
{{Quote}}

# Details
{{Context}}

# Source
{{Source}}

{{!-- To include Card Fabric: {{> "Card Fabric"}} --}}
