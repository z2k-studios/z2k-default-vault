---
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_suggested_title: "Conversation with {{PrimaryParticipant}} - {{today}}"
z2k_card_source_type: ".:Z2K/SourceType/Conversation"
z2k_card_privacy: ".:Z2K/Privacy/Private/Implied"
---
{{fieldInfo ConciseSummary "Briefly, what was this conversation about?" type="text" directives="required"}}
{{fieldInfo PrimaryParticipant "Who is the primary participant?" type="text"}}
{{fieldInfo PrimaryParticipantWithNameTag "Primary participant with name tag link?" type="text"}}
{{fieldInfo OtherParticipants "Who else was present?" type="text"}}
{{fieldInfo FactualNotes "What are the factual notes?" type="text"}}
{{fieldInfo ImmaterialNotes "Reflect on the immaterial aspects" type="text"}}
{{fieldInfo ActionItems "What are the action items?" type="text"}}

{{ConciseSummary}}

---

# Participants
- {{PrimaryParticipantWithNameTag}}
- {{OtherParticipants}}

# Context
- **Previous Conversation**::
- **Next Conversation**::
- **Ontology**::

{{> "Logistics"}}

---

# Key Notes and Takeaways

## The Facts
{{FactualNotes}}

## The Immaterial
{{! It is important to reflect if you can on the immaterial, e.g.: What emotion did you walk away having? How are you different than before the meeting? What were the power dynamics? Where did you not represent yourself accurately? What was the real motivation for the meeting? What fed into making this meeting happen? }}
{{ImmaterialNotes}}

---

# Action Items
{{ActionItems}}

{{!-- To include Card Fabric: {{> "Card Fabric"}} --}}
