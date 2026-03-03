---
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_author: "Z2K Studios, LLC"
z2k_template_suggested_title: "{{today}}"
z2k_card_type: ".:Z2K/CardType/Daily/Journal"
---
{{! Flame fields are populated by external automation — do NOT add fieldInfo declarations for them. }}
{{fieldInfo GratitudeChangeUp "What are you grateful for today?" type="text"}}
{{fieldInfo MostEssentialTask "What is your most essential task today?" type="text"}}
{{fieldInfo LeastEssentialTask "What is the least essential task you can drop?" type="text"}}
{{fieldInfo ToFeelToday "How do you want to feel today?" type="text"}}
{{fieldInfo MoodEntry "Current mood?" type="text"}}

**Daily Journal - {{Flame-OneWordTheme}}**
*{{dayOfWeek}}, {{wikilink today}}, week of {{wikilink yearWeek}} - [[{{today}}|Journal]], [[{{today}} - Log|Log]]*
- **← Previous Day**:: {{wikilink (formatString '{0} - Journal' yesterday) '← Previous Day'}}
- **→ Next Day**:: {{wikilink (formatString '{0} - Journal' tomorrow) '→ Next Day'}}

---
# Overview and Review
{{Flame-LogDate}}- **Day of Week**:: {{dayOfWeek}}
{{Flame-DayType}}{{Flame-OneWordThemeAndContext}}{{Flame-DailyRemembrance}}{{Flame-DailySummary}}{{Flame-AmazingEvent}}{{Flame-MoodPrimary}}{{Flame-MoodSecondary}}{{MoodEntry}}- **Log Report**:: [[{{today}} - Log]]

---
# Morning
---

## Awareness and Assessment

### Gratefulness
{{GratitudeChangeUp}}
### Challenges
{{Flame-StrugglingIssue}}
### Goals
{{MostEssentialTask}}{{LeastEssentialTask}}{{ToFeelToday}}

---
# Daily Notes
---

## Diary (Private)
-

## Journaling
{{Flame-Journal}}-

## Passing Memories
-

## Passing Thoughts
-

## Passing Interactions
{{Flame-SocialInteractions}}-

## Passing Information
-

## Passing Quotations
>

## Beautiful Language
-

## Passing Poetry


## Scratch Area
-

{{!-- To include Card Fabric: {{> "Card Fabric"}} --}}
