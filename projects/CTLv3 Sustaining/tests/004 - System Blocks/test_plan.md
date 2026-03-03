---
feature_ref: "features/004 - System Blocks.md"
feature_number: "004"
---

# Test Plan — Feature 004: System Blocks

## Feature Reference

- **Feature file:** `features/004 - System Blocks.md`
- **Requirements:** 004-001 through 004-013

## Test Assertions

| Req ID | Assertion | Tier | Type | Automated | Expected Result |
|---|---|---|---|---|---|
| 004-001 | `VAULT_ROOT/.system-block.md` exists | Quantitative | Structure check | Yes | File exists |
| 004-002 | Root system block starts with `---` and has a closing `---` | Quantitative | Content check | Yes | Valid YAML frontmatter delimiters |
| 004-003 | All 11 required fields are present in root system block YAML | Quantitative | Content check | Yes | All field names found in content |
| 004-004 | Deprecated fields absent from root system block | Quantitative | Content check | Yes | `z2k_creation_domain`, `z2k_card_build_state`, `z2k_card_status` not present |
| 004-005 | Root system block body contains `{{fieldInfo me value="me"}}` | Quantitative | Content check | Yes | String found in content |
| 004-006 | `.system-block.md` exists in each of the 13 domain folders | Quantitative | Structure check | Yes | All 13 files exist |
| 004-007 | Each domain system block has the correct `z2k_creation_domain` value | Quantitative | Content check | Yes | Canonical value present for each domain |
| 004-008 | Ratings domains (Information, Thoughts, Beliefs, Memories) contain all 3 ratings fields | Quantitative | Content check | Yes | `z2k_rating_depth`, `z2k_rating_surprisal`, `z2k_rating_passion` present |
| 004-009 | Non-ratings domains do NOT contain ratings fields | Quantitative | Content check | Yes | None of the 3 ratings field names present |
| 004-010 | Journals has `z2k_card_privacy: ".:Z2K/Privacy/Private/Journal"`; Logs has `z2k_card_privacy: ".:Z2K/Privacy/Private/Log"` | Quantitative | Content check | Yes | Correct privacy values present |
| 004-011 | AI system block contains `z2k_creation_perspective: "AI"` | Quantitative | Content check | Yes | Field and value present |
| 004-012 | `Projects/My Writings/.system-block-stop` exists | Quantitative | Structure check | Yes | File exists |
| 004-013 | All 13 domain system blocks use `---` YAML frontmatter delimiters | Quantitative | Content check | Yes | Each file has valid delimiters |

## JSON Packets

None — Feature 004 is a pure filesystem/content check (Category A). No Command Queue or Obsidian interaction required.

## Expected Outputs

None — all tests check file existence and string content directly.

## Coverage Checklist

- [x] Every requirement ID from the feature file appears in the test assertion table
- [x] No test rows reference requirement IDs that do not exist
- [x] All quantitative tests have clearly defined expected results
- [x] No qualitative tests (Feature 004 has no qualitative requirements)
- [x] No manual tests required
