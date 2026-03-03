---
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_suggested_title: "{{ConciseSummary}}"
z2k_card_source_type: ".:Z2K/SourceType/OtherCards"
z2k_card_type: ".:Z2K/CardType/Structure/Ontology"
---
{{fieldInfo ConciseSummary "What is this ontology about?" type="text" directives="required"}}
{{fieldInfo OverviewDetails "Overview of the ontology" type="text"}}

{{ConciseSummary}}

---

# Overview
{{OverviewDetails}}

{{> "When Where Who"}}

# TOC 1

# TOC 2


{{!-- To include Card Fabric: {{> "Card Fabric"}} --}}
