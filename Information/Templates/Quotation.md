---
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_suggested_title: "{{Author}} - {{ConciseSummary}}"
z2k_card_source_type: ".:Z2K/SourceType/Quotation"
---
{{fieldInfo ConciseSummary "Provide a concise summary of this quotation:" type="text" directives="required"}}
{{fieldInfo Quote "The quote text:" type="text" directives="required"}}
{{fieldInfo Author "Who said or wrote this quote:" type="text" directives="required"}}
{{fieldInfo Value "Why this quote is so important to me:" type="text"}}
{{fieldInfo Context "Contextual connections:" type="text"}}
{{ConciseSummary}}

---

# Quote
> {{Quote}}
>
> -- {{Author}}

# Value
{{Value}}

# Contextual Fibers
{{Context}}

{{!-- To include Card Fabric: {{> "Card Fabric"}} --}}
