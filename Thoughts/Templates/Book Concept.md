---
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_suggested_title: "{{ConciseSummary}}"
z2k_card_source_type: ".:Z2K/SourceType/InternalThought"
---
{{fieldInfo ConciseSummary "Briefly, what is this concept?" type="text" directives="required"}}
{{fieldInfo BookConcept "Describe the concept" type="text"}}
{{fieldInfo BookTitle "Title of the book?" type="text" directives="required"}}
{{fieldInfo Author "Author (with wikilink)?" type="text"}}
{{fieldInfo AuthorNameOnly "Author name only (no brackets)?" type="text" directives="required"}}
{{fieldInfo Citation "Citation details?" type="text"}}
{{fieldInfo Synthesis "Your synthesis or commentary?" type="text"}}

{{ConciseSummary}}

---

# Concept
{{BookConcept}}

# Author and Citation
- **Title**:: {{BookTitle}}
- **Author**:: {{Author}}
- **Source**:: [[{{BookTitle}} - {{AuthorNameOnly}}]]
- **Citation**:: {{Citation}}

# Synthesis
> [!me]
> Me: {{Synthesis}}

{{!-- To include Card Fabric: {{> "Card Fabric"}} --}}
