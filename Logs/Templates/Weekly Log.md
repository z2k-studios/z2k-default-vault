---
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_author: "Z2K Studios, LLC"
z2k_template_suggested_title: "{{yearWeek}} - Weekly Log"
z2k_card_type: ".:Z2K/CardType/Log/Weekly"
---
{{fieldInfo WeekTheme "Enter a word or short phrase capturing the week" type="text" directives="required"}}
{{fieldInfo OverviewAndDetails "Enter any longer description of what happened this week" type="text"}}
{{fieldInfo WeeklyThemeReason "Why did you choose this theme?" type="text"}}
{{fieldInfo KeyEvents "Key events of the week" type="text"}}
{{fieldInfo PersonalNotabilityDescription "What made this week personally notable?" type="text"}}
{{fieldInfo PersonalNotabilityScale "Scale 1-10: how notable personally?" type="number"}}
{{fieldInfo FamilyNotabilityDescription "What made this week notable for the family?" type="text"}}
{{fieldInfo FamilyNotabilityScale "Scale 1-10: how notable for family?" type="number"}}
{{fieldInfo WorldEventsDescription "Notable world events this week?" type="text"}}
{{fieldInfo WorldEventsScale "Scale 1-10: how notable were world events?" type="number"}}
{{fieldInfo HealthBiggestIssue "Biggest health issue this week?" type="text"}}
{{fieldInfo HealthIssueScale "Scale 1-10: how big was the health issue?" type="number"}}
{{fieldInfo PrimaryWeekLocation "Primary location this week (City, State/Country)?" type="text"}}

#WeeklyTheme: **{{WeekTheme}}**
*Week of {{weekNum}}*

---

# Week In Review
{{OverviewAndDetails}}

# Theme
**{{WeekTheme}}** : {{WeeklyThemeReason}}

# Image of the Week

# Key Events
{{KeyEvents}}

# Notability
- **Personal Notability - Description**: {{PersonalNotabilityDescription}}
- **Personal Notability - Scale**: {{PersonalNotabilityScale}}

- **Family Notability - Description**: {{FamilyNotabilityDescription}}
- **Family Notability - Scale**: {{FamilyNotabilityScale}}

- **World Events Notability - Description**: {{WorldEventsDescription}}
- **World Events - Scale**: {{WorldEventsScale}}

- **Personal Health - Biggest Issue**: {{HealthBiggestIssue}}
- **Personal Health - Scale**: {{HealthIssueScale}}

# Metrics
- **Primary Location**: {{PrimaryWeekLocation}}

# Location Map

---

# Links

## Daily Links
| Day of the Week | Daily Log |
| --------------- | --------- |
| Sunday          |           |
| Monday          |           |
| Tuesday         |           |
| Wednesday       |           |
| Thursday        |           |
| Friday          |           |
| Saturday        |           |

## Week Links
- **← Previous Week**:: {{wikilink (formatString '{0} - Weekly Log' (formatDate 'YYYY-[w]WW' (dateAdd today -7 'days'))) '← Previous Week'}}
- **→ Next Week**:: {{wikilink (formatString '{0} - Weekly Log' (formatDate 'YYYY-[w]WW' (dateAdd today 7 'days'))) '→ Next Week'}}
