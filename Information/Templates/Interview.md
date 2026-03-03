---
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_suggested_title: "{{InterviewerNameOnly}} Interview - {{IntervieweeNameOnly}}"
z2k_card_source_type: ".:Z2K/SourceType/Interview"
---
{{fieldInfo ConciseSummary "Provide a concise summary of this interview:" type="text" directives="required"}}
{{fieldInfo InterviewerNameOnly "Interviewer name (for card title):" type="text" directives="required"}}
{{fieldInfo IntervieweeNameOnly "Interviewee name (for card title):" type="text" directives="required"}}
{{fieldInfo InterviewTitle "Title of the interview:" type="text"}}
{{fieldInfo Interviewee "Interviewee (with wikilink formatting if desired):" type="text"}}
{{fieldInfo Interviewer "Interviewer (with wikilink formatting if desired):" type="text"}}
{{fieldInfo InterviewDate "Date of the interview:" type="date"}}
{{fieldInfo KeyTakeaways "List out the core takeaway concepts here:" type="text"}}
{{fieldInfo FurtherDetails "Further details:" type="text"}}
{{fieldInfo TranscriptURL "URL of the transcript:" type="text"}}
{{fieldInfo TranscriptText "Full transcript text:" type="text"}}
{{ConciseSummary}}

---

# Overview
- **Interview Title**:: *{{InterviewTitle}}*
- **Interviewee**:: {{Interviewee}}
- **Interviewer**:: {{Interviewer}}
- **References**::
- **Date of Interview**:: {{InterviewDate}}

# Context:
- **Location(s)**:
	- {{! Where did I listen to this? }}
- **Listened to Date(s)**:
    - {{wikilink today}}


---
# Background and Context
{{! Who is the author? What is their background? Any links to other cards? }}


---
# Synthesized Key Points
{{KeyTakeaways}}


---
# Questions To Ask the Author
{{! Insert any questions you would want to ask the author and flag them with #Questions/ToAsk/Author. Reminder - this helps you operate in Synthesis mode. }}


---

# Details
{{FurtherDetails}}


---

# Transcript
- URL: {{TranscriptURL}}

Full text:
{{TranscriptText}}

{{!-- To include Card Fabric: {{> "Card Fabric"}} --}}
