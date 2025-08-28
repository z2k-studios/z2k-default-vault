---
z2k_template_type: partial
---
{{~prompt-info Prerequisites prompt="Enter a list of cards that should be known in order to understand this card"~}}
{{~prompt-info ReferenceTags prompt="Enter a list of known Tags associated with this card"~}}
{{~prompt-info ReferenceCards prompt="Enter a list of relevant cards"~}}
# Overview
{{OverviewDetails}}

# Prerequisites
{{format-string-bulletize Prerequisites}}

# References
- Ref: 
    - Tags: {{ReferenceTags}}
    - Cards:{{format-string-bulletize ReferenceCards 2}}
