---
feature_ref: "features/020 - Global Template Quality.md"
feature_number: "020"
---

# Test Plan — Feature 020: Global Template Quality

## Feature Reference

- **Feature file:** `features/020 - Global Template Quality.md`
- **Requirements:** 020-001 through 020-012

## Scope

Tests run against **all templates** — all `.md` files under `*/Templates/` directories in the vault.
No exclusions. Personal templates are prohibited in the CTL system vault (020-013); if present, they fail both 020-005 (wrong author) and 020-013 (existence violation).

## Test Assertions

| Req ID | Assertion | Tier | Type | Automated | Expected Result |
|---|---|---|---|---|---|
| 020-001 | Every CTL template has valid Handlebars syntax (balanced `{{`/`}}`, matched block tags) | Quantitative | Content check | Yes | No syntax errors across all templates |
| 020-002 | No CTL template contains `<% ... %>` Templater syntax outside a FLAGGED comment | Quantitative | Content check | Yes | No v2 syntax found |
| 020-003 | Every document template has `z2k_template_type`, `z2k_template_version`, and `z2k_template_suggested_title` | Quantitative | Content check | Yes | All 3 fields present in all document templates |
| 020-004 | Every block template has `z2k_template_type: block-template` | Quantitative | Content check | Yes | Field present in all block templates |
| 020-005 | Every template in the vault has `z2k_template_author: "Z2K Studios, LLC"` (no exclusions) | Quantitative | Content check | Yes | Author field correct on all templates |
| 020-006 | All `{{fieldInfo}}` custom field names use PascalCase (built-ins excluded) | Quantitative | Content check | Yes | No lowercase-leading field names |
| 020-007 | Comments containing `{{` or `}}` use `{{!-- --}}` double-dash form | Quantitative | Content check | Yes | No single-form `{{! }}` comments with mustache content |
| 020-008 | Comment-only lines have no trailing whitespace | Quantitative | Content check | Yes | No trailing spaces after comment closing `}}` |
| 020-009 | Every `{{fieldInfo}}` declaration has at minimum a field name | Quantitative | Content check | Yes | No malformed fieldInfo tags |
| 020-010 | Every `{{> "BlockName"}}` partial reference points to an existing template file | Quantitative | Content check | Yes | All referenced blocks exist |
| 020-011 | Every `z2k_card_source_type` value in a template is from the canonical registry | Quantitative | Content check | Yes | No non-canonical source type values |
| 020-012 | No two templates within the same `Templates/` folder share the same filename | Quantitative | Structure check | Yes | No duplicate filenames per folder |
| 020-013 | No template in the CTL vault has a personal author value (`"Geoff (z2k-gwp)"` or similar) | Quantitative | Content check | Yes | No personal-authored templates found |

## JSON Packets

None — Feature 020 is a pure filesystem/content check (Category A).

## Expected Outputs

None — all tests check file content directly.

## Coverage Checklist

- [x] Every requirement ID from the feature file appears in the test assertion table
- [x] No test rows reference requirement IDs that do not exist
- [x] All quantitative tests have clearly defined expected results
- [x] No qualitative tests (Feature 020 has no qualitative requirements)
- [x] No manual tests required
- [x] 020-013 added: personal templates prohibited in CTL vault (no exclusion circular risk)
