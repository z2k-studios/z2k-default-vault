---
# Z2K Card Properties from Template File -----------------------
z2k_creation_template_version:     "v3.101 2025-07-08"
z2k_card_type:                     ".:Z2K/CardType/Atom"
z2k_card_source_type:              ".:Z2K/SourceType/WebArticle"
z2k_template_default_title:        "{{format-string-file-friendly ArticleBriefTitle}} - {{format-string-file-friendly AuthorName}}"

# Z2K Card Properties from Template File -----------------------
# The following YAML properties store away template fields so they can be access through database tools and subsequent partials
Author:             "{{Author}}" 
Title:              "{{Title}}" 
FullTitle:          "{{FullTitle}}" 
PublicationName:    "{{PublicationName}}" 

---
{{! Z2K Templates - Field Definitions --------------------------------------------------------------- }}
{{! The following field definitions specify more complex prompting information for fields}}
{{~no-output Title             "text" "Enter a brief version of the article title (to be used in the card title):" "Self-Reliance" "Unnamed Article"}}
{{~no-output FullTitle  "text" "Enter the full title from the source material:" "{{ArticleBriefTitle}}" "{{ArticleBriefTitle}}"}}
{{~no-output Author        "text" "Enter the name of the Author:" "Ralph Waldo Emerson" "Unknown Author"}}
{{~no-output PublicationName   "text" "What publication published this article?" "The Atlantic" ""}}
{{~no-output ArticleMedium     "multiSelect:#Media/Magazine,#Media/Web,#Media/News,#Media/Journal" "What medium is the article published in?" "#Media/Magazine" ""}}
{{~}}
{{> Partial - Information - 1 - Summary Section}}

---
{{> Partial - Information - 2 - Overview Section}}

---
# Citation
- Article Title:: {{Title}}
- Article Full Title :: {{FullTitle}}
- Author:: {{wikilink Author}}
- Citation:: {{Citation}}
- Article Date:: {{wikilink ArticleDate}}
- Article Publication:: {{wikilink (format-string-file-friendly PublicationName)}}
- Article Medium:: {{ArticleMedium}}
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
{{! Use the Partial "Partial - Quotation" to insert additional quotations from the article.}}

## {{QuotationName}}
> {{Quotation}}

- {{QuotationTakeaways}}

