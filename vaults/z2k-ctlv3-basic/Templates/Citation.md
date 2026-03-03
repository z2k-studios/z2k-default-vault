---
z2k_template_type: block-template
z2k_template_author: "Z2K Studios, LLC"
ContentAuthor: "{{ContentAuthor}}"
ContentTitle: "{{ContentTitle}}"
ContentSource: "{{ContentSource}}"
ContentURL: "{{ContentURL}}"
ContentDate: "{{ContentDate}}"
---
{{fieldInfo ContentAuthor "Who is the author?"}}
{{fieldInfo ContentTitle "What is the title?"}}
{{fieldInfo ContentSource "What is the source publication?"}}
{{fieldInfo ContentURL "URL of the source?"}}
{{fieldInfo ContentDate "Date of publication?"}}

**Source:** {{ContentAuthor}}, "{{ContentTitle}}" — *{{ContentSource}}*
{{#if ContentURL}}**URL:** {{ContentURL}}{{/if}}
{{#if ContentDate}}**Date:** {{ContentDate}}{{/if}}
