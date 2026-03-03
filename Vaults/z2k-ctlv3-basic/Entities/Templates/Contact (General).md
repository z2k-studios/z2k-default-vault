---
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_author: "Z2K Studios, LLC"
z2k_template_suggested_title: "{{ContactName}}"
---
{{fieldInfo ContactName "Name of the contact?" type="text" directives="required"}}
{{fieldInfo ContactRole "Role or title?" type="text"}}
{{fieldInfo ContactOrganization "Organization?" type="text"}}
{{fieldInfo ContactRelationship "Relationship to you?" type="text"}}
{{fieldInfo ContactFirstMet "When did you first meet?" type="date"}}
{{fieldInfo ContactTags "Tags (comma-separated)?" type="text"}}
{{fieldInfo ContactNotes "Notes?" type="text"}}

# {{ContactName}}

## Summary
- **Name**:: {{ContactName}}
- **Role / Title**:: {{ContactRole}}
- **Organization**:: {{ContactOrganization}}
- **Relationship**:: {{ContactRelationship}}
- **First Met**:: {{ContactFirstMet}}
- **Tags**:: {{ContactTags}}

## Notes
{{ContactNotes}}

{{!-- To include Card Fabric: {{> "Card Fabric"}} --}}
