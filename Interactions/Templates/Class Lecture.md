---
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_suggested_title: "Class - {{ClassNum}} - {{ClassSubject}} - Week {{Weeknum}} - {{LectureSubject}}"
z2k_card_source_type: ".:Z2K/SourceType/ClassLecture"
z2k_card_privacy: ".:Z2K/Privacy/Quasi-Public/Setting"
---
{{fieldInfo ConciseSummary "Briefly, what was this lecture about?" type="text" directives="required"}}
{{fieldInfo ClassNum "What is the class number?" type="text"}}
{{fieldInfo ClassSubject "What is the class subject?" type="text"}}
{{fieldInfo LectureDate "What date was this lecture?" type="date"}}
{{fieldInfo Weeknum "What week number is this - and postfix with A or B if multiple lectures per week" type="text"}}
{{fieldInfo LectureSubject "What is the lecture subject?" type="text"}}
{{fieldInfo ClassName "What is the class name?" type="text"}}
{{fieldInfo LectureInstructor "Who is the instructor?" type="text"}}
{{fieldInfo OverviewDetails "Describe this lecture" type="text"}}

{{ConciseSummary}}

---

# Overview
{{OverviewDetails}}

# Class Details
- **Lecture Date**:: {{LectureDate}}
- **Lecture Week Number**:: {{Weeknum}}
- **Lecture Subject**:: {{LectureSubject}}
- **Class Name**:: [[{{ClassName}}]]
- **Class Instructor**:: {{LectureInstructor}}
- **Materials Location**::
- **Links to Class Readings**::
- **Previous Class**::
- **Next Class**::

{{> "Logistics"}}

---

# My Key Takeaways and Learnings
-

## Key Moments in the Lecture


---

# Class Notes
*Reminder: Use ^ blocknotes that can be referenced elsewhere*

---

# Excerpts from Class Materials
-

---

# Class Discussions
-

# Class Writings
-

---

# Class Lecture Transcription
```
```

{{!-- To include Card Fabric: {{> "Card Fabric"}} --}}
