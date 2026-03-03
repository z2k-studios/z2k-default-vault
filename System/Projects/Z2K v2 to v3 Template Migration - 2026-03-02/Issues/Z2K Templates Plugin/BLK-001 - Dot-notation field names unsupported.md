# BLK-001 — Dot-notation field names unsupported

**Discovered by:** Task 07 (dot-notation test gate)
**Open issues:** BLK-001, BLK-004, BLK-005

## Symptom
Field names containing dots (e.g., `Content.Author`, `Fabric.MentalModel`) are not recognized by the template engine. Both `{{fieldInfo Content.Author "prompt"}}` and `{{Content.Author}}` render verbatim in the output.

## Reproduction
```json
{
  "cmd": "new",
  "templateContents": "{{fieldInfo Content.Author \"Author?\"}}\nAuthor: {{Content.Author}}",
  "fileTitle": "dot-notation-test-output",
  "prompt": "none",
  "finalize": true,
  "Content.Author": "Test Author"
}
```

**Expected:** `Author: Test Author`
**Actual:** `Author: {{Content.Author}}` (verbatim)

## Root Cause
Handlebars interprets `Content.Author` as property access (`Content` object, `Author` property), not as a field named `Content.Author`. This is standard Handlebars behavior, not a bug per se — but it means dotted field names cannot be used as template field identifiers.

## Impact
All block and document templates must use flat field names instead of the originally planned dot-notation namespacing:
- `Content.Author` → `ContentAuthor`
- `Content.Title` → `ContentTitle`
- `Fabric.MentalModel` → `FabricMentalModel`
- etc.

## Resolution
Use flat names for all affected fields across Tasks 07–22.
