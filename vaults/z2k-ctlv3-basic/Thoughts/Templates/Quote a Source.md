---
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_author: "Z2K Studios, LLC"
z2k_template_suggested_title: "{{ConciseSummary}}"
z2k_card_source_type: ".:Z2K/SourceType/Quotation"
---
{{fieldInfo ConciseSummary "Briefly, what is this quote about?" type="text" directives="required"}}
{{fieldInfo Quote "The quote itself" type="text" directives="required"}}
{{fieldInfo Context "Context or details about the quote?" type="text"}}
{{fieldInfo Source "Who or what is the source?" type="text"}}

{{ConciseSummary}}

---

# Quote
{{Quote}}

# Details
{{Context}}

# Source
{{Source}}

{{!-- To include Card Fabric: {{> "Card Fabric"}} --}}
