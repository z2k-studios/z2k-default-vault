---
feature_ref: "features/002 - Working System.md"
feature_number: "002"
---

# Test Plan — Feature 002: Working System

## Feature Reference

- **Feature file:** `features/002 - Working System.md`
- **Requirements:** 002-001 through 002-006

## Test Assertions

| Req ID | Assertion | Tier | Type | Automated | Expected Result |
|---|---|---|---|---|---|
| 002-001 | JSON packet with `templatePath` pointing to `Beliefs/Templates/Beliefs (General).md` produces output | Quantitative | Command Queue | Yes | Output file created at `System/Test Output/ctlv3-working-system-test.md` |
| 002-002 | Output contains `z2k_metadata_version: 3.00` and `z2k_creation_library_version: "3.0.0"` from root `.system-block.md` | Quantitative | Content check | Yes | Both fields present in rendered YAML |
| 002-003 | Output contains `z2k_creation_domain: ".:Z2K/Domain/Beliefs"` from domain `.system-block.md` | Quantitative | Content check | Yes | Field present in rendered YAML |
| 002-004 | Output contains field value supplied in JSON packet (e.g., `ConciseSummary` text) | Quantitative | Content check | Yes | Supplied text present in output body |
| 002-005 | Dynamic fields (`z2k_creation_creator`, `z2k_creation_date`, `z2k_creation_timestamp`) are resolved — not raw Handlebars expressions | Quantitative | Content check | Yes | No `{{` or `}}` in the output |
| 002-006 | After normalizing dynamic fields, output matches the golden expected file | Quantitative | Diff | Yes (requires golden file) | Diff is empty |

## JSON Packets

| File | Purpose |
|---|---|
| `json_packets/basic.json` | Renders `Beliefs (General).md` via `templatePath` with known field values |

## Expected Outputs

The golden expected file must be generated before 002-006 can run. To generate it:

1. Ensure Obsidian is running with Z2K Templates plugin active and Command Queues enabled.
2. Run the test once (it will render the template and save the output).
3. Copy the rendered output from `System/Test Output/ctlv3-working-system-test.md` to `expected/basic_expected.md`.
4. Apply normalization (replace dynamic fields with placeholders per `test_utils.normalize_dynamic_fields()`).
5. Save the normalized version as `expected/basic_expected.md`.

Until the expected file is created, requirement 002-006 runs as SKIP with instructions.

**Note on output location:** The packet uses `destDir: "System/Test Output"`. The output file will appear at:
`<vault_root>/System/Test Output/ctlv3-working-system-test.md`

The `System/Test Output/` folder is created automatically by the plugin if it doesn't exist.

## Coverage Checklist

- [x] Every requirement ID from the feature file appears in the test assertion table
- [x] No test rows reference requirement IDs that do not exist
- [x] All quantitative tests have clearly defined expected results (002-006 pending golden file)
- [x] No qualitative tests (Feature 002 has no qualitative requirements)
- [x] No manual tests required
