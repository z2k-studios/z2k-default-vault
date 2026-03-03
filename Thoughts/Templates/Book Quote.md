---
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_suggested_title: "{{BookTitle}} Quote - {{AuthorNameOnly}}"
z2k_card_source_type: ".:Z2K/SourceType/Quotation"
---
{{fieldInfo ConciseSummary "Brief description of this quote?" type="text" directives="required"}}
{{fieldInfo BlockQuoteHere "The quote itself" type="text" directives="required"}}
{{fieldInfo BookTitle "Title of the book?" type="text" directives="required"}}
{{fieldInfo Author "Author (with wikilink)?" type="text"}}
{{fieldInfo AuthorNameOnly "Author name only (no brackets)?" type="text" directives="required"}}
{{fieldInfo Citation "Citation details?" type="text"}}
{{fieldInfo Synthesis "Your commentary on this quote?" type="text"}}

{{ConciseSummary}}

---

# Quote
{{BlockQuoteHere}}

# Author and Citation
- **Title**:: {{BookTitle}}
- **Author**:: {{Author}}
- **Source**:: [[{{BookTitle}} - {{AuthorNameOnly}}]]
- **Citation**:: {{Citation}}

# Personal Commentary
> [!me]
> Me: {{Synthesis}}

{{!-- To include Card Fabric: {{> "Card Fabric"}} --}}
