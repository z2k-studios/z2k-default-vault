---
task_id: "Task-01"
ip_tasks: ["TP-0.1", "TP-0.2", "TP-0.3", "TP-0.4"]
execution_phase: "Phase 0"
status: "Done"
domain: "Global"
parallelizable: true
parallel_group: "Phase 0/1 setup — can run alongside Task 02"
---
# Task 01 — Testing Infrastructure

> Before executing this task, read `tasks/Agent Brief.md` — project-wide paths, constraints, naming conventions, and conversion rules.

## Goal
Create the CTL v3 testing vault, validate Command Queue (or URI fallback), and produce a confirmed, working path for automated template testing.

## Dependencies
None — independent of vault structure.

## References to Read First
- REF-L: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/URI, JSON, Command Queues/Command Queues/Command Queues Overview.md`
- REF-M: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/URI, JSON, Command Queues/JSON Packages/JSON Packages Overview.md`
- REF-N: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/URI, JSON, Command Queues/URI Actions/URI Actions.md`

## Output Files
- New vault: `Data/Vaults/z2k-testing-vaults/Z2K System Vault Testing/`
- Test script: `Testing/scripts/tp-0-hello-world.py` (in this project folder)
- `Testing/scripts/test-structure.py` — Category A skeleton (runnable, no assertions yet)
- `Testing/scripts/test-blocks.py` — Category B blocks skeleton
- `Testing/scripts/test-templates.py` — Category B templates skeleton
- `Testing/scripts/lib/runner.py` — shared Command Queue dispatch, file polling, assertion helpers
- `Testing/scripts/lib/yaml_utils.py` — YAML parsing and assertion helpers
- `Testing/commands/` — directory for JSON command files (one subfolder per phase)
- `Testing/expected/` — directory for golden output files (one subfolder per test)
- Feature Prioritization table update (in IP §Z2K Templates Feature Prioritization)

> **Do not modify** `Data/Vaults/z2k-testing-vaults/Templates Test Vault - Primary/` — maintained by another developer.

## Steps

### TP-0.1 — Create CTL v3 Testing Vault
1. Create vault root: `Data/Vaults/z2k-testing-vaults/Z2K System Vault Testing/`
2. Create `.obsidian/` config directory inside the vault
3. Install Z2K Templates Plugin (copy from an existing vault's `.obsidian/plugins/z2k-plugin-templates/`)
4. Configure plugin: set creator name, templates folder name
5. Enable Command Queue: Settings → Z2K Templates → Command Queue Settings
6. Set queue folder: `.obsidian/plugins/z2k-plugin-templates/command-queue/`
7. Set scan frequency to 10s

> ⚠️ **User assist required:** Opening the new vault in Obsidian and confirming the plugin is active requires user interaction. This is the gate for all subsequent testing steps.

### TP-0.2 — Validate Command Queue with Hello World Test
1. Write `Testing/scripts/tp-0-hello-world.py` in the project folder
2. JSON package: `{"cmd": "new", "templateContents": "Hello {{Name}}!", "fileTitle": "hello-world-output", "prompt": "none", "finalize": true, "Name": "World"}`
3. Write to queue folder; trigger "Process Command Queue Now" from Obsidian Command Palette
4. Verify: `hello-world-output.md` created in vault root; command moved to `done/`
5. Investigate whether "Process Command Queue Now" can be triggered via URI/AppleScript (document findings)

### TP-0.3 — Evaluate URI Fallback (If Needed)
- **Skip if TP-0.2 fully succeeds**
- If TP-0.2 has blocking issues: build a minimal URI-based fallback script using `subprocess.run(["open", uri])`
- Use same hello-world template via `templateContents` + URI `fromJson` command

### TP-0.4 — Select Primary Testing Method and Document Findings
1. Select: Command Queue (preferred) or URI (fallback)
2. Log any plugin bugs discovered to `Issues/Z2K Templates Plugin/`
3. Update IP §Z2K Templates Feature Prioritization table: mark Command Queue row as Validated (✅) or note failure
4. Note: findings feed into Testing Plan TP-INF-001

### TP-0.5 — Scaffold Test Script Infrastructure
Create all base test script files so subsequent tasks can add assertions without creating new files.

1. Create directory structure:
   - `Testing/scripts/lib/`
   - `Testing/commands/`
   - `Testing/expected/`

2. Create `Testing/scripts/lib/yaml_utils.py` — YAML parsing helpers:
   - `load_yaml_frontmatter(path)` → dict of frontmatter fields
   - `assert_field_present(frontmatter, field)` → pass/fail
   - `assert_field_value(frontmatter, field, expected)` → pass/fail

3. Create `Testing/scripts/lib/runner.py` — shared test runner infrastructure:
   - `assert_path_exists(path)` → pass/fail with message
   - `write_command_file(queue_dir, filename, payload)` → writes JSON to queue folder
   - `poll_for_output(output_path, timeout_s=30)` → waits for file to appear, returns content
   - `normalize_dynamic_fields(content)` → replaces `{{wikilink today}}` → `<TODAY_WIKILINK>` etc.
   - `compare_to_golden(actual_normalized, golden_path)` → diff and report; save golden if absent
   - `run_suite(tests)` → runs list of test functions, prints pass/fail summary, exits non-zero on any failure

4. Create `Testing/scripts/test-structure.py` — runnable skeleton:
   ```python
   #!/usr/bin/env python3
   """Category A — Structure and existence tests. Add assertions below as tasks complete."""
   import sys
   from pathlib import Path
   sys.path.insert(0, str(Path(__file__).parent))
   from lib.runner import assert_path_exists, run_suite
   from lib.yaml_utils import load_yaml_frontmatter, assert_field_present, assert_field_value

   VAULT = Path("Data/Vaults/z2k-default-vault")

   def test_placeholder():
       """Remove this once real assertions are added."""
       return True, "placeholder — no assertions yet"

   run_suite([test_placeholder])
   ```

5. Create `Testing/scripts/test-blocks.py` — same skeleton pattern; replace `test_placeholder` docstring with `"""Category B — Block template instantiation tests."""`

6. Create `Testing/scripts/test-templates.py` — same skeleton pattern; docstring `"""Category B — Document template instantiation tests."""`

7. Run `python3 Testing/scripts/test-structure.py` — confirm it exits 0 with "1 passed".

> **Note:** All paths in test scripts are relative to the workspace root (the directory containing `Data/`), not the vault. Agents run from the workspace root.

## Open Issues
None blocking this task (DSB-005, BLK-001, etc. are downstream).

## Acceptance Criteria
- New testing vault exists at `Data/Vaults/z2k-testing-vaults/Z2K System Vault Testing/`
- Z2K Templates Plugin active; Command Queue enabled
- At least one template instantiation test passes end-to-end (hello-world)
- Primary testing method confirmed and documented
- Testing Plan TP-INF-001 can be resolved
- All three skeleton scripts (`test-structure.py`, `test-blocks.py`, `test-templates.py`) exist and exit 0
- `lib/runner.py` and `lib/yaml_utils.py` exist with the helpers listed in TP-0.5

## Validation (from Testing Plan)
| Test | Pass Condition |
|---|---|
| Testing vault exists | `Z2K System Vault Testing/` folder exists |
| Plugin installed | Plugin folder + `manifest.json` exist |
| Command Queue hello-world | Output file created; command in `done/` |
