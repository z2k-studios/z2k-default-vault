---
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_suggested_title: "{{ConciseSummary}}"
z2k_card_source_type: ".:Z2K/SourceType/Quotation"
---
{{fieldInfo ConciseSummary "Briefly, what is this quote about?" type="text" directives="required"}}
{{fieldInfo BlockQuoteHere "The quote itself" type="text" directives="required"}}
{{fieldInfo Author "Who said or wrote this?" type="text"}}
{{fieldInfo Source "Where did you find the quote?" type="text"}}
{{fieldInfo RecommendedBy "Who recommended this to you?" type="text"}}
{{fieldInfo Synthesis "Your commentary on this quote?" type="text"}}

{{ConciseSummary}}

---

# Quote
{{BlockQuoteHere}}

# Author and Citation
- **Author**:: {{Author}}
- **Source**:: {{Source}}
- **Recommended By**:: {{RecommendedBy}}

# Synthesis
> [!me]
> Me: {{Synthesis}}

{{!-- To include Card Fabric: {{> "Card Fabric"}} --}}
