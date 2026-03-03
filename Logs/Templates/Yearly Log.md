---
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_suggested_title: "{{year}} - Yearly Log"
z2k_card_type: ".:Z2K/CardType/Log/Yearly"
---
{{fieldInfo YearlyTheme "Enter a word or short phrase capturing the year" type="text" directives="required"}}
{{fieldInfo YearOverview "What happened this year? Just what was most important." type="text"}}
{{fieldInfo YearlyThemeReason "Why did you choose this theme?" type="text"}}

#YearlyTheme: **{{YearlyTheme}}**
- **← Previous Year**:: {{wikilink (formatString '{0} - Yearly Log' (formatDate 'YYYY' (dateAdd today -1 'years'))) '← Previous Year'}}
- **→ Next Year**:: {{wikilink (formatString '{0} - Yearly Log' (formatDate 'YYYY' (dateAdd today 1 'years'))) '→ Next Year'}}

---

# Year In Review
{{YearOverview}}

## Theme
**{{YearlyTheme}}** : {{YearlyThemeReason}}

## Quarterly Focus
-

## Travel
| Start | End | Who | Location |
| ----- | --- | --- | -------- |

## Resolutions

## Top Cards
-

## Location Map
