---
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_author: "Z2K Studios, LLC"
z2k_template_suggested_title: "{{yearMonth}} - Monthly Log"
z2k_card_type: ".:Z2K/CardType/Log/Monthly"
---
{{fieldInfo MonthTheme "Enter a word or short phrase capturing the month" type="text" directives="required"}}
{{fieldInfo MonthOverview "What happened this month? Just what was most important." type="text"}}
{{fieldInfo MonthThemeReason "Why did you choose this theme?" type="text"}}
{{fieldInfo Fulfillment "Fulfillment (0-10)?" type="number"}}
{{fieldInfo Positivity "Positivity (0-10)?" type="number"}}
{{fieldInfo PhysicalHealth "Physical health (0-10)?" type="number"}}
{{fieldInfo MentalHealth "Mental health (0-10)?" type="number"}}
{{fieldInfo Meaning "Meaning (0-10)?" type="number"}}
{{fieldInfo Purpose "Purpose (0-10)?" type="number"}}
{{fieldInfo Goodness "Goodness (0-10)?" type="number"}}
{{fieldInfo Deferment "Deferment (0-10)?" type="number"}}
{{fieldInfo Friendships "Friendships (0-10)?" type="number"}}
{{fieldInfo Relationships "Relationships (0-10)?" type="number"}}

#MonthlyTheme: **{{MonthTheme}}**
*Month of {{formatDate 'MMMM' now}}, {{year}}*

---

# Month In Review
{{MonthOverview}}

# Theme
**{{MonthTheme}}** : {{MonthThemeReason}}

# Image of the Month

# Metrics

## Flourishing
Take the following [flourishing quiz](https://www.nytimes.com/interactive/2021/05/04/well/mind/languishing-definition-flourishing-quiz.html). Reference: [[How to Flourish In Life]]

In this past month:
1. How fulfilled are you with life as a whole these days?
	- Fulfillment:: {{Fulfillment}}
2. How positive in your outlook do you usually feel?
	- Positivity:: {{Positivity}}
3. In general, how would you rate your physical health?
	- PhysicalHealth:: {{PhysicalHealth}}
4. How would you rate your overall mental health?
	- MentalHealth:: {{MentalHealth}}
5. Overall, to what extent do you feel the things you do in your life are worthwhile?
	- Meaning:: {{Meaning}}
6. I understand my purpose in life.
	- Purpose:: {{Purpose}}
7. I always act to promote good in all circumstances, even in difficult and challenging situations.
	- Goodness:: {{Goodness}}
8. I am always able to give up some happiness now for greater happiness later.
	- Deferment:: {{Deferment}}
9. I am content with my friendships and relationships.
	- Friendships:: {{Friendships}}
10. My relationships are as fulfilling as I would like them to be.
	- Relationships:: {{Relationships}}

**Results**:
This Month's total Flourishing gauge:
	FlourishingGauge::

# Location Map

---

# Links

## Weeks
| Week | Weekly Log |
| ---- | ---------- |
| Week 1 |          |
| Week 2 |          |
| Week 3 |          |
| Week 4 |          |
| Week 5 |          |

## Month Links
- **← Previous Month**:: {{wikilink (formatString '{0} - Monthly Log' (formatDate 'YYYY-MM' (dateAdd today -1 'months'))) '← Previous Month'}}
- **→ Next Month**:: {{wikilink (formatString '{0} - Monthly Log' (formatDate 'YYYY-MM' (dateAdd today 1 'months'))) '→ Next Month'}}
