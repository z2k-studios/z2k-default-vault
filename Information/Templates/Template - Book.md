---
# Z2K Card Properties from Template File -----------------------
z2k_creation_template_version:     "v3.0 2025-06-29"
z2k_card_type:                     ".:Z2K/CardType/Atom"
z2k_card_source_type:              ".:Z2K/SourceType/Book"
z2k_template_default_title:        "{{format-string-file-friendly BookBriefTitle}} - {{format-string-file-friendly AuthorName}}"

# Z2K Card Properties from Template File -----------------------
# The following YAML properties store away template fields so they can be access through database tools and subsequent partials
Author:          "{{Author}}" 
Title:           "{{Title}}" 
FullTitle:       "{{FullTitle}}" 

---
{{! Z2K Templates - Field Definitions --------------------------------------------------------------- }}
{{! The following field definitions specify more complex prompting information for fields}}
{{~no-output Author            "text" "Enter the name of the author (without wikilinks):" "Walt Whitman"}}
{{~no-output Title             "text" "Enter a brief version of the book title (to be used in the card title):"}}
{{~no-output FullTitle         "text" "Enter the full title of the book:" "{{Title}}" "{{Title}}"}}
{{~no-output PersonalLocation  "multiSelect:Audible, Kindle, Physical, Public Library" "Where or how is this book stored?"}}
{{~no-output WhereWhenWhy      "text" "When, Where and Why I acquired this book?"}}
{{~no-output BookMedium        "multiSelect:#Media/Book/PhysicalBook,#Media/Book/Kindle,#Media/Book/PDF,#Media/Book/Online,None" "|"What medium is the book stored in within your Library?" "#Media/Book/PhysicalBook"}}
{{~}}
{{> Partial - Information - 1 - Summary Section}}

---
{{> Partial - Information - 2 - Overview Section}}

---
# Personal Relevance
- **Personal Library Location**:: {{PersonalLocation}}
- **Recommended By**:: {{wikilink RecommendedBy}}
- **Read With**:: {{wikilink ReadWith}}
- **When, Where and Why I Acquired This Book**:: {{WhereWhenWhy}}


# Citation
- **Book Title**:: {{Title}}
- **Book Full Title**:: {{FullTitle}}
- **Author**:: {{wikilink Author}}
- **Citation**:: {{Citation}}
- **Publish Date**:: {{wikilink ArticleDate}}
- **ASIN**:: [{{asin}}]({{appBookLink}})
- **Full Source Material URL**:: {{BookURL}}
- **Medium**:: {{BookMedium}}

---
{{> Partial - Information - 3 - Synthesis Section}}

---
# Questions To Ask the Author
%% Insert any questions you would want to ask the author and flag them with \#Questions/ToAsk/Author . Reminder - this helps you operate in Synthesis mode. %%

---
# Details
{{! Delve into the details here. Use WriterTags hashtags:  
   - #WriterTags/BeautifulLanguage - word choices that really strike a cord
   - #WriterTags/ExternalQuotes - quotes of *other* authors made by the author (could be useful in figuring out what else to read or explore)
   - #WriterTags/Abstractions - when an author makes a broader statement
}}
{{FurtherDetails}}
{{sourceData}}

---
# Key Excerpts
{{! Insert a series of excerpts from the paper here. Be sure to either group with named headers (as below) or add a ^ at the end of each quote to enable block quoting from other cards.}}
{{! Use the Partial "Partial - Quotation" to insert additional quotations from the book.}}

## {{QuotationName}}
> {{Quotation}}

- {{QuotationTakeaways}}

