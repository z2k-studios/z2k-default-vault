---
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_suggested_title: "{{ShowName}} - {{Interviewee}}"
z2k_card_source_type: ".:Z2K/SourceType/Podcast"
---
{{fieldInfo ConciseSummary "Provide a concise summary of this podcast interview:" type="text" directives="required"}}
{{fieldInfo ShowName "Name of the podcast show:" type="text"}}
{{ConciseSummary}}

---

{{> "Podcast Interview Content"}}

{{!-- To include Card Fabric: {{> "Card Fabric"}} --}}
