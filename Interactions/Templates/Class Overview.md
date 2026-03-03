---
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_suggested_title: "Class - {{ClassNum}} - {{ClassSubject}}"
z2k_card_source_type: ".:Z2K/SourceType/ClassLecture"
z2k_card_privacy: ".:Z2K/Privacy/Quasi-Public/Setting"
---
{{fieldInfo ConciseSummary "Briefly, what is this class about?" type="text" directives="required"}}
{{fieldInfo SchoolName "What school is this at?" type="text"}}
{{fieldInfo ClassNum "What is the class number?" type="text"}}
{{fieldInfo ClassSubject "What is the class subject?" type="text"}}
{{fieldInfo InstructorName "Who is the instructor?" type="text"}}
{{fieldInfo Semester "What semester?" type="text"}}
{{fieldInfo OverviewDetails "Describe this class" type="text"}}

{{ConciseSummary}}

---

# Overview
{{OverviewDetails}}

# Class Details
- **School**:: {{SchoolName}}
- **Class Number**:: {{ClassNum}}
- **Class Subject**:: {{ClassSubject}}
- **Class Name**:: [[{{cardTitle}}]]
- **Instructor**:: {{InstructorName}}
- **Semester**:: {{Semester}}

{{> "Logistics"}}

# Lectures
Links to the different lectures from the class:
-

{{!-- To include Card Fabric: {{> "Card Fabric"}} --}}
