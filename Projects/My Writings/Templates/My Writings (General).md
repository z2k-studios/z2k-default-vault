---
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_author: "Z2K Studios, LLC"
z2k_template_suggested_title: "{{ConciseSummary}}"
z2k_card_source_type: ".:Z2K/SourceType/InternalThought"
---
{{fieldInfo ConciseSummary "Brief summary of this writing?" type="text" directives="required"}}
{{fieldInfo FullTitle "Full title of the writing?" type="text"}}
{{fieldInfo PublishingMethod "Publishing method? (Blog, Class, Email)" type="text"}}
{{fieldInfo FirstPublishDate "First publish date?" type="text"}}
{{fieldInfo Audience "Who is the audience?" type="text"}}
{{fieldInfo BackgroundContext "Core contributory concepts?" type="text"}}
{{fieldInfo Overview "Overview and key tenets?" type="text"}}
{{fieldInfo DiscussionPoints "Draft discussion points?" type="text"}}
{{fieldInfo FeedbackReceived "Feedback received?" type="text"}}

{{ConciseSummary}}

---

# Writing Details
- **Full Title**:: {{FullTitle}}
- **Publishing Method**:: {{PublishingMethod}}
- **First Publish Date**:: {{FirstPublishDate}}
- **Audience**:: {{Audience}}

# Core Contributory Concepts
{{BackgroundContext}}

# Overview and Key Tenets
{{Overview}}

# Draft Discussion Points
{{DiscussionPoints}}

# Feedback Received
{{FeedbackReceived}}

---

# Full Contents
{{! Insert the full contents here. If it is heavily formatted then just leave it unformatted just for searching - but make a note here to refer to the full formatted file. }}

{{!-- To include Card Fabric: {{> "Card Fabric"}} --}}
