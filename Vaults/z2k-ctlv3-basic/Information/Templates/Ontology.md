---
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_author: "Z2K Studios, LLC"
z2k_template_suggested_title: "{{ConciseSummary}} - Ontology"
z2k_card_source_type: ".:Z2K/SourceType/OtherCards"
z2k_card_type: ".:Z2K/CardType/Structure/Ontology"
---
{{fieldInfo ConciseSummary "Provide a concise summary for this ontology:" type="text" directives="required"}}
{{fieldInfo OverviewDetails "Overview details:" type="text"}}
{{fieldInfo TOC1 "Table of Contents section 1:" type="text"}}
{{fieldInfo TOC2 "Table of Contents section 2:" type="text"}}
{{ConciseSummary}}

---

# Overview
{{OverviewDetails}}

# TOC 1
{{TOC1}}

# TOC 2
{{TOC2}}

{{!-- To include Card Fabric: {{> "Card Fabric"}} --}}
