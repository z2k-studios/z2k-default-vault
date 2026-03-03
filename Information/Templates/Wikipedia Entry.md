---
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_suggested_title: "{{WikipediaTitle}}"
z2k_card_source_type: ".:Z2K/SourceType/WebArticle"
---
{{fieldInfo ConciseSummary "Provide a concise summary:" type="text" directives="required"}}
{{fieldInfo WikipediaTitle "Title of the Wikipedia entry:" type="text" directives="required"}}
{{fieldInfo WikipediaLink "Link to the Wikipedia page:" type="text"}}
{{fieldInfo OverviewDetails "Overview details:" type="text"}}
{{fieldInfo FurtherDetails "Further details:" type="text"}}
{{ConciseSummary}}

---

# Wikipedia Entry
{{WikipediaLink}}

# Overview
*Reminder - don't use this card if a link to wikipedia is sufficient. Only create a card if you want to capture additional content or aggregate repeated linkages across the vault. Delete this reminder after you have confirmed it.*
{{OverviewDetails}}

# Details
{{FurtherDetails}}

{{!-- To include Card Fabric: {{> "Card Fabric"}} --}}
