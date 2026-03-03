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
{{fieldInfo Synthesis "Synthesis of key points:" type="text"}}
{{fieldInfo FurtherDetails "Further details:" type="text"}}
{{ConciseSummary}}
{{! Reminder: you will need to manually copy the Z2K YAML Properties to the Kindle Notes }}
FYI - plugin at [Obsidian Kindle Plugin](https://github.com/hadynz/obsidian-kindle-plugin "https://github.com/hadynz/obsidian-kindle-plugin")

---

# Overview
{{OverviewDetails}}

# Author and Citation
- Title:: {{BookTitle}}
- Author:: {{Author}}
- Source:: [[{{cardTitle}}]]
- Citation:: {{Citation}}
- Full Source Materials - File Location::
- Personal Library Location:: {{PersonalLocation}}
- Recommended By:: {{RecommendedBy}}


# Synthesis of Key Points
{{Synthesis}}


---

# Details
{{FurtherDetails}}


---

# Kindle Notes:
{{! FLAGGED: The v2 template contained Jinja2-style template code for iterating over Kindle highlights ({% for highlight in highlights %}...{% endfor %}). This syntax is from the Obsidian Kindle Plugin, not Templater or Z2K Templates, and cannot be converted to v3 Handlebars syntax. The user should paste Kindle highlights manually or use the Kindle Plugin's own import feature. }}

{{!-- To include Card Fabric: {{> "Card Fabric"}} --}}
