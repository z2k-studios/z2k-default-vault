---
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_author: "Z2K Studios, LLC"
z2k_template_suggested_title: "{{today}} - Log"
z2k_card_type: ".:Z2K/CardType/Daily/Log"
---
{{! Flame fields are populated by external automation (z2k-sheet-importer). Do NOT rename, prompt, or add fieldInfo for any Flame-* field. }}
{{fieldInfo Weather "What's the weather like?" type="text"}}
{{fieldInfo NewsHeadlines "Any notable headlines?" type="text"}}
{{fieldInfo DailyQuotes "Quotations for the day?" type="text"}}
{{fieldInfo WordOfTheDay "Word of the day?" type="text"}}
{{fieldInfo DailyPondering "What are you pondering?" type="text"}}
{{fieldInfo HumilityCode "Humility check?" type="text"}}
{{fieldInfo DailySurprisal "What surprised you today?" type="text"}}
{{fieldInfo VirtueOfTheDay "Virtue of the day?" type="text"}}
{{fieldInfo DailyJournalPrompt "Journal prompt?" type="text"}}
{{fieldInfo DailyLifeGuidance "Life guidance for today?" type="text"}}
{{fieldInfo DailyLookbacks "Any lookbacks?" type="text"}}
{{fieldInfo Calendar "Calendar events?" type="text"}}
{{fieldInfo DailyTasks "Tasks snapshot?" type="text"}}
{{fieldInfo CompletedTasks "Completed tasks?" type="text"}}
{{fieldInfo DailyCardModifications "Card modifications?" type="text"}}
{{fieldInfo LocationBlocks "Location blocks?" type="text"}}
{{fieldInfo HealthStatus "Health status?" type="text"}}
{{fieldInfo SleepStatus "Sleep status?" type="text"}}
{{fieldInfo FitnessStatus "Fitness status?" type="text"}}
{{fieldInfo FitnessCharts "Fitness charts?" type="text"}}

**Daily Log Report - {{Flame-OneWordTheme}}**
*{{dayOfWeek}}, {{wikilink today}}, week of {{wikilink yearWeek}} - [[{{today}}|Journal]], [[{{today}} - Log|Log]]*
- **← Previous Day**:: {{wikilink (formatString '{0} - Log' yesterday) '← Previous Day'}}
- **→ Next Day**:: {{wikilink (formatString '{0} - Log' tomorrow) '→ Next Day'}}

---
# Overview
{{Flame-LogDate-Link}}- **Day of Week**:: {{dayOfWeek}}
{{Flame-DayType}}
---
# Wake up
---
## Weather
{{Flame-WeatherRanking}}{{Weather}}

## News
- The Economist's [World In Brief](https://www.economist.com/the-world-in-brief) {{NewsHeadlines}}

## Quotations for the Day
{{DailyQuotes}}
## Vocabulary for the Day
{{WordOfTheDay}}

## Daily Instigations
{{DailyPondering}}{{HumilityCode}}{{DailySurprisal}}{{VirtueOfTheDay}}{{DailyJournalPrompt}}{{DailyLifeGuidance}}

## Daily Lookbacks
{{DailyLookbacks}}

---
# Agenda
---

## Calendar
{{Calendar}}

## Tasks (Snapshot)
{{DailyTasks}}

### Other Completed Tasks
{{CompletedTasks}}

---
# Activities of the Day
---
## Tagged Events
-

## Image of the Day


## Z2K Activity of Note
{{Flame-TimestampSubmit}}{{Flame-TimestampExport}}{{Flame-ExportErrors}}
{{DailyCardModifications}}

---
# Touch The Flame
---

## Rankings
{{Flame-ImportanceToPosterity}}{{Flame-OverallFulfillment}}{{Flame-Serenity}}{{Flame-SelfDoubt}}{{Flame-LoveOfLife}}{{Flame-Intellectual}}

## Relationship
{{Flame-RelationshipState}}{{Flame-RelationshipCollocated}}

---
# Location Log
---
## Summary
{{Flame-Location}}- [Google Timeline](https://timeline.google.com/maps/timeline)

## Location Blocks
{{LocationBlocks}}

---
# Health Log
---
{{Flame-BodyHealthRanking}}{{Flame-Sleepiness}}{{Flame-ExerciseRanking}}
## Food Consumption
{{Flame-FoodConsumption}}
{{HealthStatus}}
{{SleepStatus}}
{{FitnessStatus}}
{{FitnessCharts}}

{{!-- To include Card Fabric: {{> "Card Fabric"}} --}}

---
# Automated Logs
---
Anything below this line was logged automatically through automation routines.

| Date | Time | Device | Action |
| ---- | ---- | ------ | ------ |
