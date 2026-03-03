---
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_suggested_title: "{{BookTitle}} - {{AuthorNameOnly}}"
z2k_card_source_type: ".:Z2K/SourceType/Book"
---
{{fieldInfo ConciseSummary "Provide a concise summary of this book:" type="text" directives="required"}}
{{fieldInfo BookTitle "Title of the book:" type="text" directives="required"}}
{{fieldInfo AuthorNameOnly "Author name (without wikilinks):" type="text" directives="required"}}
{{fieldInfo Author "Author (with wikilink formatting if desired):" type="text"}}
{{fieldInfo Citation "Citation reference:" type="text"}}
{{fieldInfo OverviewDetails "Overview details:" type="text"}}
{{fieldInfo PersonalLocation "Where is it stored?" type="singleSelect" opts="Audible, Kindle, Physical, Public Library"}}
{{fieldInfo RecommendedBy "Recommended by:" type="text"}}
{{fieldInfo WhenWhereWhy "When, where and why you acquired this book:" type="text"}}
{{fieldInfo Synthesis "Synthesis of key points:" type="text"}}
{{fieldInfo FurtherDetails "Further details:" type="text"}}
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
- Medium:: #Media/Book
- Title:: {{BookTitle}}
- Author:: {{Author}}
- Source:: [[{{cardTitle}}]]
- Citation:: {{Citation}}
- Full Source Materials - File Location::
- Personal Library Location:: {{PersonalLocation}}
- Recommended By:: {{RecommendedBy}}
- Read With::
- When, Where and Why I Acquired This Book:: {{WhenWhereWhy}}

# Synthesis of Key Points
{{Synthesis}}
{{! What thought/awareness/belief did you have after reading it that made you the most different than what you were before you read? }}
{{! Note: build up an index here of key themes as you are reading, per Tim Ferriss. }}

---
# Questions To Ask the Author
{{! Insert any questions you would want to ask the author and flag them with #Questions/ToAsk/Author. Reminder - this helps you operate in Synthesis mode. }}


---

# Details
{{! Delve into the details here. Use WriterTags hashtags: }}
{{! - #WriterTags/BeautifulLanguage - word choices that really strike a chord }}
{{! - #WriterTags/ExternalQuotes - quotes of other authors made by the author }}
{{! - #WriterTags/Abstractions - when an author makes a broader statement }}
{{FurtherDetails}}


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
