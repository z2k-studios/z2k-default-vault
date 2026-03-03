---
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_suggested_title: "{{BookTitle}} - {{AuthorNameOnly}}"
z2k_card_source_type: ".:Z2K/SourceType/Book"
---
{{fieldInfo ConciseSummaryOfConcept "Provide a concise summary of the concept:" type="text" directives="required"}}
{{fieldInfo BookTitle "Title of the book:" type="text" directives="required"}}
{{fieldInfo AuthorNameOnly "Author name (without wikilinks):" type="text" directives="required"}}
{{fieldInfo Author "Author (with wikilink formatting if desired):" type="text"}}
{{fieldInfo BlinkistLinkText "Blinkist link:" type="text"}}
{{fieldInfo QuoteDescription "Brief description of the quote:" type="text"}}
{{fieldInfo Quote "The quote text:" type="text"}}
{{ConciseSummaryOfConcept}}

---

# Source Book Details
Note: this concept was originally instigated by a Blinkist book summary.
- Book Title:: {{BookTitle}}
- Book Author:: {{Author}}
- Blink Links:
    - {{BlinkistLinkText}}


# Key Observations
-
-

# Blinkist Quotes

## Blinkist Quote : {{QuoteDescription}}
> {{Quote}}

{{!-- To include Card Fabric: {{> "Card Fabric"}} --}}
