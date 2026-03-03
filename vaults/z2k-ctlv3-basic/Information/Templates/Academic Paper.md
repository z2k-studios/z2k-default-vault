---
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_author: "Z2K Studios, LLC"
z2k_template_suggested_title: "{{ArticleTitle}} - {{AuthorNameOnly}}"
z2k_card_source_type: ".:Z2K/SourceType/WebArticle"
---
{{fieldInfo ConciseSummary "Provide a concise summary of this academic paper:" type="text" directives="required"}}
{{fieldInfo ArticleTitle "Title of the academic paper:" type="text" directives="required"}}
{{fieldInfo AuthorNameOnly "Author name (without wikilinks):" type="text" directives="required"}}
{{fieldInfo Author "Author (with wikilink formatting if desired):" type="text"}}
{{fieldInfo Citation "Citation reference:" type="text"}}
{{fieldInfo PaperYear "Year of publication:" type="text"}}
{{fieldInfo URL "Full source material URL:" type="text"}}
{{fieldInfo OverviewDetails "Overview details:" type="text"}}
{{fieldInfo SynthesizedTakeaways "Synthesized takeaways:" type="text"}}
{{fieldInfo Quote1 "Key excerpt #1:" type="text"}}
{{fieldInfo Quote1Takeaways "Takeaways from excerpt #1:" type="text"}}
{{fieldInfo Quote2 "Key excerpt #2:" type="text"}}
{{fieldInfo Quote2Takeaways "Takeaways from excerpt #2:" type="text"}}
{{fieldInfo QuoteN "Additional key excerpt:" type="text"}}
{{fieldInfo QuoteNTakeaways "Takeaways from additional excerpt:" type="text"}}
{{ConciseSummary}}

---

# Overview
{{OverviewDetails}}

# Author and Citation
* Author:: {{Author}}
* Source:: [[{{ArticleTitle}}]]
* Citation:: {{Citation}}
* Year:: {{PaperYear}}
* Full Source Material URL:: {{URL}}

---

# Synthesized Takeaways
{{SynthesizedTakeaways}}

---

# General Notes
-

---

# Key Excerpts
{{! Insert a series of excerpts from the paper here. Be sure to either group with headers or add a ^ at the end of each quote to enable block quoting from other cards. }}

## Quote1Summary
> {{Quote1}}

- {{Quote1Takeaways}}


## Quote2Summary
> {{Quote2}}

- {{Quote2Takeaways}}


## QuoteNSummary
> {{QuoteN}}

- {{QuoteNTakeaways}}

{{!-- To include Card Fabric: {{> "Card Fabric"}} --}}
