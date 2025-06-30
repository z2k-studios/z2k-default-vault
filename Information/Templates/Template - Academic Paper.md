---
# Z2K Card Properties from Template File -----------------------
z2k_creation_template_version:     "v3.1 2025-06-29"
z2k_card_type:                     ".:Z2K/CardType/Atom"
z2k_card_source_type:              ".:Z2K/SourceType/WebArticle"
z2k_template_default_title:        "{{format-string-file-friendly ArticleTitle}} - {{format-string-file-friendly AuthorName}}"

---
{{> Partial - Information - 1 - Summary Section}}

---
{{> Partial - Information - 2 - Overview Section}}

---
# Citation
- Article Title:: {{ArticleBriefTitle|text|Enter a brief version of the article title (to be used in the card title)}}
- Article Full Title :: {{ArticleFullTitle|text|Enter the full title from the source material|{{ArticleBriefTitle}}|{{ArticleBriefTitle}}}}
- Author:: {{wikilink AuthorName}}
- Citation:: {{Citation}}
- Article Date:: {{wikilink ArticleDate}}
- Article Publication:: {{wikilink PublicationName|text|What publication published this article?}}
- Article Medium:: {{ArticleMedium|multiSelect:#Media/Magazine,#Media/Web,#Media/News,#Media/Journal|What medium is the article published in?|#Media/Magazine}}

- Full Source Material URL:: {{URL}}

---
{{> Partial - Information - 3 - Synthesis Section}}

---
# General Notes
{{! Insert general notes here.}}
{{sourceData}}

---
# Key Excerpts
{{! Insert a series of excerpts from the paper here. Be sure to either group with headers (as below) or add a ^ at the end of each quote to enable block quoting from other cards.}}

## Quote1Summary
> {{Quote1}}

- {{Quote1Takeaways}}


## Quote2Summary
> {{Quote2}}

- {{Quote2Takeaways}}


## QuoteNSummary
> {{QuoteN}}

- {{QuoteNTakeaways}}

