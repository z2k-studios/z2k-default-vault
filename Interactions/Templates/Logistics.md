---
z2k_template_type: block-template
z2k_template_author: "Z2K Studios, LLC"
---
{{fieldInfo LogisticsDate "Date of the interaction?" type="date"}}
{{fieldInfo LogisticsLocation "Where did this take place?" type="text"}}
{{fieldInfo LogisticsParticipants "Who was involved?" type="text"}}
{{fieldInfo LogisticsRecorded "Was this recorded?" type="singleSelect" opts="Yes, No" fallback="No"}}

## Logistics
- **Date**:: {{LogisticsDate}}
- **Location**:: {{LogisticsLocation}}
- **Participants**:: {{LogisticsParticipants}}
- **Recorded**:: {{LogisticsRecorded}}
