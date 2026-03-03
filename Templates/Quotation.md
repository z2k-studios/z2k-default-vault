---
z2k_template_type: block-template
ContentAuthor: "{{ContentAuthor}}"
ContentTitle: "{{ContentTitle}}"
---
{{fieldInfo ContentAuthor "Who is the author?"}}
{{fieldInfo ContentTitle "What is the title of the source?"}}
{{fieldInfo ContentText "What is the quote?" type="text"}}

> {{ContentText}}
> — {{ContentAuthor}}, *{{ContentTitle}}*
