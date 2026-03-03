---
Description: Testing Plan for the CTLv3 Sustaining project — defines the two-tier testing model (quantitative + qualitative), Command Queue testing mechanism, AI quality scorecard, test output contract, regression modes, and the Test Suite Refresh procedure.
document_type: Testing Plan
status: Draft
---

# Testing Plan - CTLv3 Sustaining


## 1. Testing Philosophy

**All tests must be automated.** This is a hard requirement. The goal is a project where a single command (`run_all_tests.py`) validates the entire CTLv3 template library without human intervention (beyond ensuring Obsidian is running).

Tests are divided into two tiers:

- **Quantitative** — script-automated, deterministic, fast. These test concrete, objectively verifiable behaviors.
- **Qualitative** — AI agent-assessed, scored against a checklist. These evaluate subjective quality criteria that cannot be reduced to a script.

Both tiers are integrated into the regression framework. Manual testing is permitted only when automation is genuinely infeasible, and each exception must be explicitly documented with written justification.

---

## 2. Prerequisites

Before any tests can run:

- **Obsidian must be running** with the Z2K Templates plugin active
- **Command Queues must be enabled** in Z2K Templates settings (Settings → Z2K Templates → Command Queue Settings)
- **Python 3.x** must be available
- **Claude API access** must be configured (for qualitative tests only; not needed for `--no-quality` mode)

Feature 001 (Infrastructure Test) validates all prerequisites before other tests execute.

---

## 3. Two-Tier Testing Model


### 3.1 Tier 1 — Quantitative Testing

Quantitative tests are script-automated and deterministic. They verify concrete, objectively measurable behaviors.

#### 3.1.1 Command Queue Rendering Tests

The primary quantitative mechanism uses Command Queues to render templates and compare output:

1. **Create JSON Package**: The test script generates a `.json` file specifying:
   ```json
   {
     "cmd": "new",
     "templatePath": "<path to template>",
     "prompt": "none",
     "finalize": true,
     "<field1>": "<value1>",
     "<field2>": "<value2>"
   }
   ```
2. **Record error log position**: Before submitting, record the current byte offset of the error log file (`.obsidian/plugins/z2k-plugin-templates/error-log.md`). If the file does not yet exist, record offset 0.
3. **Drop into Queue Folder**: The script writes the JSON file to the Command Queue watched directory.
4. **Wait for Processing**: The script polls for the command file to move to the `done/` subfolder, or for the output note to appear. Timeout after a configurable period (recommend 30s, accounting for the scan interval).
5. **Read Output**: The script reads the rendered note file created by the plugin.
6. **Check error log**: Read any new content in the error log since the recorded position. If new Warning-or-above entries are present, fail the test immediately and include the log content in the failure output. This surfaces plugin errors that are not visible in the rendered file.
7. **Compare**: Diff the rendered output against the expected output file in `expected/`.
8. **Clean Up**: Remove the rendered note file (and optionally the archived JSON from `done/`).

**Timing considerations**: The Command Queue scans at a configurable interval (default 60s). For faster testing, either:
- Configure a shorter scan interval in the test vault's settings
- Use the "Process Command Queue Now" command palette action (if scriptable)
- Account for the delay in the test script's timeout logic

#### 3.1.2 Non-Rendering Quantitative Tests

Not all quantitative tests require rendering. Examples:

- **Structure validation**: Verify expected folders, files, and configuration exist
- **Syntax validation**: Parse templates for valid Handlebars syntax
- **Naming convention checks**: Scan field names and verify custom fields use PascalCase (not camelCase), built-in fields are recognized as exceptions
- **System block presence**: Verify templates contain required system blocks
- **YAML frontmatter checks**: Verify templates have required metadata fields
- **Comment formatting**: Check that comments don't leave trailing spaces or break line clearing


### 3.2 Tier 2 — Qualitative Testing

Qualitative tests use an AI agent to evaluate templates against the Template Quality Scorecard (`CTLv3 Sustaining - Template Quality Scorecard.md`).

#### 3.2.1 Assessment Mechanism

1. The test script invokes Claude (via CLI call to `claude` or via the Anthropic API) with:
   - The full template source content
   - The Template Quality Scorecard criteria
   - The feature's requirements (for context)
   - Instructions to evaluate each scorecard item and produce a structured result
2. The AI agent evaluates the template and returns:
   - Per-item score (pass/fail/partial with notes)
   - Overall numeric score (percentage of scorecard items passed)
   - List of improvement suggestions
3. The test script compares the overall score against the passing threshold.

#### 3.2.2 Two Modes

- **Analysis mode** (default): Read-only. Outputs scorecard results, score, and suggestions to the test output. Does not modify any files. This is what runs during regression.
- **Fix mode** (explicit invocation only): The AI agent iteratively applies suggestions to improve the template, re-assesses, and repeats until the score exceeds the threshold or a maximum iteration count is reached.

**Fix mode safeguards:**
- Requires an explicit command-line flag (e.g., `--fix`)
- Requires interactive user confirmation before proceeding ("Fix mode will modify template files. Continue? [y/N]")
- All changes are reviewable via `git diff`
- Fix mode is NEVER invoked during standard regression

#### 3.2.3 Passing Threshold

The global passing threshold is defined here: **Threshold: 70%**

Per-feature override: A feature's `test_plan.md` may include a `quality_override: pass` directive to force the qualitative test to pass regardless of score. Use this for intentionally simple templates that would score low due to their nature (e.g., a bare-bones starter template), not due to actual quality problems. The override must include a written justification.

---

## 4. Test Folder Structure

### 4.1 Per-Feature Layout

Each feature has a corresponding test folder in `tests/`, named identically to the feature file minus `.md`:

```
tests/NNN - <Feature Name>/
├── test_plan.md                    ← Testing plan for this feature
├── run_tests.py                    ← Root test script (runs all tests for this feature)
├── json_packets/                   ← JSON Package files for Command Queue tests
│   ├── basic.json                  ← Standard data packet
│   ├── edge_cases.json             ← Edge case data (special chars, empty fields, etc.)
│   └── ...
├── expected/                       ← Expected output files for diff comparison
│   ├── basic_expected.md           ← Expected output from basic.json
│   ├── edge_cases_expected.md      ← Expected output from edge_cases.json
│   └── ...
└── (additional helper scripts, test data)
```

### 4.2 Shared Resources

Reusable test utilities live in `tests/shared/`:

```
tests/shared/
├── test_utils.py                   ← Common Python utilities (queue submission, output reading, diff, cleanup, error log monitoring)
├── quality_agent.py                ← Qualitative AI assessment invocation logic
├── output_formatter.py             ← Standardized test output formatting
├── json_templates/                 ← Reusable JSON packet fragments/templates
│   ├── edge_case_fields.json       ← Universal edge case field values (special chars, Unicode, etc.)
│   └── empty_fields.json           ← All-empty field values for boundary testing
└── config.py                       ← Paths, timeouts, thresholds, and other configuration
```

### 4.3 Naming Conventions

- **Test folders**: `NNN - <Feature Name>/` (matches feature file name minus `.md`)
- **Root test script** (per feature): Always `run_tests.py`
- **Master regression script**: Always `run_all_tests.py` (in `tests/` root)
- **JSON packets**: Descriptive names in `json_packets/` subfolder
- **Expected outputs**: Corresponding names in `expected/` subfolder
- **Shared utilities**: In `tests/shared/`

---

## 5. Test Output Contract

All test scripts (`run_tests.py` and `run_all_tests.py`) must conform to the following output contract.


### 5.1 Exit Codes

| Code | Meaning |
|---|---|
| `0` | All tests passed |
| `1` | One or more tests failed |
| `2` | Test execution error (infrastructure failure, not a test failure) |


### 5.2 Standard Output Format (Per Feature)

Each feature's `run_tests.py` must emit structured output to stdout:

```
[PASS] NNN-RRR: <requirement description> [quantitative]
[FAIL] NNN-RRR: <requirement description> [quantitative]
  → Expected: <expected value or behavior>
  → Actual: <actual value or behavior>
[SKIP] NNN-RRR: <requirement description> [qualitative]
  → Reason: <why this test was skipped (e.g., --no-quality mode)>
[PASS] NNN-RRR: <requirement description> [qualitative] (score: 85%)
[FAIL] NNN-RRR: <requirement description> [qualitative] (score: 55%, threshold: 70%)
  → Suggestions: <summary of AI suggestions>

========================================
Feature NNN - <Feature Name>
  Passed:  X
  Failed:  Y
  Skipped: Z
  Total:   T
  Quality Score: XX% (threshold: YY%) | OVERRIDE | N/A
========================================
```


### 5.3 Master Regression Output

`run_all_tests.py` aggregates per-feature results:

```
<per-feature output from each run_tests.py>

========================================
REGRESSION TEST SUMMARY
  Mode: full | script-only
  Features tested:  N
  Features passed:  X (all requirements met)
  Features failed:  Y
  Features skipped: Z

  Total requirements: T
  Passed:  P
  Failed:  F
  Skipped: S

  Quality assessments: Q (of N features)
  Quality overrides:   O
========================================
RESULT: PASS | FAIL
```


### 5.4 Stderr

Diagnostic information, stack traces, and debugging output should go to stderr. Only the structured test output described above should go to stdout.

---

## 6. Per-Feature Test Plan Document

Each feature's `test_plan.md` must contain:

### 6.1 Required Sections

- **Feature Reference**: Link to the feature file and its requirement IDs
- **Test Assertions**: A table mapping each requirement ID to one or more test assertions, with tier indicated
- **Automation Status**: For each test, whether it is quantitative (scripted), qualitative (AI), or manual (with justification)
- **JSON Packets**: Description of JSON packets used for rendering tests (if applicable)
- **Expected Outputs**: Description of expected outputs or references to files in `expected/`
- **Quality Override** (optional): If present, `quality_override: pass` with written justification

### 6.2 Test Assertion Table Format

| Req ID | Assertion | Tier | Type | Automated | Expected Result |
|---|---|---|---|---|---|
| NNN-001 | <What is being tested> | Quantitative | Diff | Yes | <Expected outcome> |
| NNN-002 | <What is being tested> | Quantitative | Syntax check | Yes | <Expected outcome> |
| NNN-003 | <What is being tested> | Qualitative | AI scorecard | Yes (AI) | Score ≥ threshold |

### 6.3 Coverage Requirement

Every requirement listed in the feature file must have at least one corresponding test assertion in the test plan. The test plan must not reference requirement IDs that do not exist in the feature file.

Before finalizing a feature's test plan, confirm:

- [ ] Every requirement ID from the feature file appears in the test assertion table
- [ ] No test rows reference requirement IDs that do not exist
- [ ] All quantitative tests have clearly defined expected results
- [ ] All qualitative tests reference specific scorecard criteria
- [ ] Any manual tests have written justification for why automation is infeasible

---

## 7. Feature 001 — Infrastructure Test

Feature 001 validates the project structure and testing infrastructure. Its requirements must cover:

- Expected folder structure exists (`features/`, `tests/`, `drop/`, `tests/shared/`)
- Python 3.x is available and can execute test scripts
- Obsidian is running and accessible
- Command Queue is enabled and functional (hello world test: create a JSON packet for a trivial template, verify the output file is created)
- Z2K Templates Error Log is monitored during test execution: the test framework records the log's byte offset before each Command Queue test and checks for new Warning-or-above entries afterward. Any new entries cause the test to fail with the log content included in the failure output.
- Test output formatting utilities work correctly
- `run_all_tests.py` can discover and invoke feature test folders

Feature 001 should always pass. A failure means the testing infrastructure is broken.

---

## 8. Master Regression Script

The `run_all_tests.py` script in the `tests/` folder:

1. Discovers all feature test folders (matching the `NNN - *` naming pattern)
2. Executes `run_tests.py` in each folder, in numerical order
3. Captures and aggregates results per the output contract (§5.3)
4. Reports overall pass/fail status
5. Returns exit code `0` only if all features pass

**Command-line flags:**

| Flag | Behavior |
|---|---|
| (none) | Full regression — runs both quantitative and qualitative tests |
| `--no-quality` | Script-only regression — skips all qualitative (AI) tests. Qualitative requirements reported as `[SKIP]`. |
| `--feature NNN` | Run tests for a single feature only |
| `--fix` | Enable fix mode for qualitative tests (requires user confirmation) |

This script must be runnable with no arguments (beyond `--no-quality` if desired) and no prior setup beyond the stated prerequisites.

---

## 9. Test Suite Refresh Procedure

When a feature's requirements change, the corresponding test suite must be updated. This procedure is designed to be executable by an AI agent standalone, without user input.

### 9.1 Trigger

This procedure is triggered when:
- A feature file's `## Requirements` section is modified (requirements added, changed, or removed)
- The Template Quality Scorecard is updated (affects qualitative tests for all features)
- A new shared JSON packet template is added to `tests/shared/`

### 9.2 Steps

1. **Read the updated feature file** — identify which requirements changed, were added, or were removed. Compare against the existing `test_plan.md`.
2. **Update `test_plan.md`** — add new test assertions for added requirements, modify assertions for changed requirements, remove assertions for deleted requirements. Ensure coverage requirement (§6.3) is still met.
3. **Update `run_tests.py`** — implement the new/changed test assertions in the script. Remove tests for deleted requirements.
4. **Update JSON packets** — create new packets in `json_packets/` if new rendering tests are needed. Modify existing packets if field expectations changed.
5. **Regenerate expected outputs** — update files in `expected/` to reflect the new expected behavior. For rendering tests, this may require running the template through the Command Queue with correct data and capturing the output.
6. **Run the feature's tests** — execute `run_tests.py` to verify all tests pass with the updated suite.
7. **Run regression** — execute `run_all_tests.py` to confirm no other features are affected.

### 9.3 Documentation Requirements

Each step must produce a clear audit trail. When an AI agent performs the refresh:
- Log which requirements changed and why
- Log which test assertions were added/modified/removed
- Verify coverage requirement before completing

---

## 10. When Tests Fail

The full failure handling procedure — including session kick-off mode questions, failure categorization, PRD impact check, fix proposal, fix execution rules, and post-fix regression — is defined in the Statement of Work §4.4 (**Test Session Initiation** and **Failure Handling and Fix Process**). Follow that procedure.

Quick reference for common cases:

- **Test bug** (assertion is wrong, not the template): Use the Test Suite Refresh Process (SoW §4.4), not the Failure Handling process.
- **Implementation gap** (template doesn't comply with a correct requirement): Follow the Failure Handling and Fix Process. Propose the fix before executing in interactive mode.
- **Requirements gap** (failure reveals a missing or incorrect requirement): STOP. Flag for human review. Do not fix until requirements are resolved.
- **Qualitative score below threshold**: Review the AI's suggestions. If the template is intentionally simple, consider adding `quality_override: pass` to its `test_plan.md` (with justification). Otherwise, use fix mode or manual improvement.
- **Flaky tests** (intermittent failures): Investigate root cause. Do not mark as "known flaky" — either fix the test or fix the system.

---

## 11. Template Quality Scorecard Reference

The Template Quality Scorecard is maintained as a separate project document: `CTLv3 Sustaining - Template Quality Scorecard.md`.

The scorecard contains the qualitative assessment criteria derived from the project's global quality requirements. Each item is evaluated by the AI agent during qualitative testing.

When the scorecard is updated, all features with qualitative requirements should be re-assessed via regression testing with quality enabled.
