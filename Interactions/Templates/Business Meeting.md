---
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_suggested_title: "Meeting with {{PrimaryParticipant}} - {{today}}"
z2k_card_source_type: ".:Z2K/SourceType/Meeting"
z2k_card_privacy: ".:Z2K/Privacy/Private/Professional"
---
{{fieldInfo ConciseSummary "Briefly, what was this meeting about?" type="text" directives="required"}}
{{fieldInfo PrimaryParticipant "Who is the primary participant?" type="text"}}
{{fieldInfo OtherParticipants "Who else was present?" type="text"}}
{{fieldInfo KeyNotes "What are the key notes and takeaways?" type="text"}}
{{fieldInfo FactualNotes "What are the factual notes?" type="text"}}
{{fieldInfo ColorNotes "Any color or qualitative impressions?" type="text"}}
{{fieldInfo ActionItems "What are the action items?" type="text"}}

{{ConciseSummary}}

---

{{> "Logistics"}}

- **Primary Participant**:: {{PrimaryParticipant}}
- **Other Participants**:: {{OtherParticipants}}

---

# Key Notes and Takeaways
{{KeyNotes}}

---

# Details

## The Facts
{{FactualNotes}}

## Color
{{ColorNotes}}

---

# Action Items
{{ActionItems}}

{{!-- To include Card Fabric: {{> "Card Fabric"}} --}}
