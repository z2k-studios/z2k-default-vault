---
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_author: "Z2K Studios, LLC"
z2k_template_suggested_title: "{{EmailSubject}} - {{EmailFrom}}"
z2k_card_source_type: ".:Z2K/SourceType/Email"
---
{{fieldInfo ConciseSummary "Provide a concise summary:" type="text" directives="required"}}
{{fieldInfo Quote "The relevant email quote or excerpt:" type="text" directives="required"}}
{{fieldInfo Context "Context and details:" type="text"}}
{{fieldInfo EmailSubject "Email subject line:" type="text"}}
{{fieldInfo EmailCorrespondence "Correspondence reference:" type="text"}}
{{fieldInfo EmailFrom "From:" type="text"}}
{{fieldInfo EmailTo "To:" type="text"}}
{{fieldInfo EmailDate "Date of the email:" type="date"}}
{{fieldInfo Source "Full email source text:" type="text"}}
{{ConciseSummary}}

---

# Quote
{{Quote}}

# Details
{{Context}}

# Email Information
- Subject:: {{EmailSubject}}
- Correspondence Reference:: {{EmailCorrespondence}}
- From:: {{EmailFrom}}
- To:: {{EmailTo}}
- Date:: {{EmailDate}}

# Source
```
{{Source}}
```

{{!-- To include Card Fabric: {{> "Card Fabric"}} --}}
