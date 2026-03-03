---
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_suggested_title: "Email with {{EmailTo}} - {{EmailSubject}}"
z2k_card_source_type: ".:Z2K/SourceType/Email"
z2k_card_privacy: ".:Z2K/Privacy/Private/Implied"
---
{{fieldInfo ConciseSummary "Briefly, what is this email about?" type="text" directives="required"}}
{{fieldInfo EmailSubject "What is the subject line?" type="text"}}
{{fieldInfo EmailCorrespondence "Link to the correspondence thread (if applicable)" type="text"}}
{{fieldInfo EmailFrom "Who is the email from?" type="text"}}
{{fieldInfo EmailTo "Who is the email to?" type="text"}}
{{fieldInfo EmailDate "What date was the email sent?" type="date"}}
{{fieldInfo Quote "Key quote from the email?" type="text"}}
{{fieldInfo Context "Any additional context or details?" type="text"}}
{{fieldInfo Source "Full email contents?" type="text"}}

{{ConciseSummary}}

---

# Key Takeaways
-

# Email Information
- **Subject Line**:: {{EmailSubject}}
- **Correspondence Reference**:: {{EmailCorrespondence}}
- **From**:: {{EmailFrom}}
- **To**:: {{EmailTo}}
- **Date**:: {{EmailDate}}

{{> "Logistics"}}

# Quote
{{Quote}}

# Details
{{Context}}

# Full Email Contents
```
{{Source}}
```

{{!-- To include Card Fabric: {{> "Card Fabric"}} --}}
