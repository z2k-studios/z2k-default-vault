---
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_author: "Z2K Studios, LLC"
z2k_template_suggested_title: "{{ConciseSummary}}"
z2k_card_source_type: ".:Z2K/SourceType/Conversation"
z2k_card_privacy: ".:Z2K/Privacy/Private/Implied"
---
{{fieldInfo ConciseSummary "Briefly, what was this interaction about?" type="text" directives="required"}}
{{fieldInfo Who "Who was involved?" type="text"}}
{{fieldInfo KeyItems "What were the key items discussed?" type="text"}}
{{fieldInfo ContextDetails "Any additional context?" type="text"}}

{{ConciseSummary}}

---

{{> "Logistics"}}

# Key Items
{{KeyItems}}

# Context
{{ContextDetails}}

{{!-- To include Card Fabric: {{> "Card Fabric"}} --}}
