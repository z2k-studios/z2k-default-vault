---
Description: Statement of Work for the CTLv3 Sustaining project — validates that the CTL v3 template library and template engine work as advertised through feature-based automated and AI-assisted testing.
document_type: Statement of Work
status: Draft
---

# Statement of Work (SoW) - CTLv3 Sustaining

## 1. Project Overview

**Project Name:** CTLv3 Sustaining
**Owner:** GP
**Primary Project Folder:** `Data/Vaults/z2k-default-vault/System/Projects/CTLv3 Sustaining/`
**GitHub Repository (if applicable):** None
**Date Created:** 2026-03-02
**Status:** Draft


### 1.1 Objective

This is a sustaining project for the Z2K Core Template Library v3 (CTLv3). Its purpose is to develop and maintain a comprehensive validation system that ensures every template in the library works as intended — templates render correctly, fields resolve properly, formatting is consistent, and the overall system behaves as advertised.

The project uses a two-tier testing model:

- **Quantitative testing** — script-automated tests that use Command Queues to render templates with JSON data packets and diff the results against expected outputs.
- **Qualitative testing** — AI agent-based assessment that evaluates templates against a quality scorecard for subjective criteria (readability, best practices, complexity showcase, documentation quality).

The project organizes its validation around features — each representing a template, a domain of templates, or a cross-cutting quality concern — with enumerated requirements and corresponding automated test suites.


### 1.2 Non-Goals

- This project does not build the template library or engine from scratch.
- This project does not follow an iterative development lifecycle — implementation is handled externally via coding workflows.
- Feature implementation is out of scope for this project's workflow; only feature description, requirements definition, test creation, and acceptance validation are managed here.
- This project does not maintain or reference the old v2 template library or migration procedures.


### 1.3 Terms and Acronyms

| Term | Full Form | Definition |
|---|---|---|
| **SoW** | Statement of Work | This document. Defines the project boundaries, goals, and process framework. |
| **PF** | Project Framework | The overall structure — files, folders, and staged processes — described in §4 of this SoW. |
| **PRD** | Project Requirements Document | Describes the structural conventions for features and requirements. Does not index individual features. |
| **IP** | Implementation Plan | Describes how new features enter the system via the drop folder and the handoff to external implementation. |
| **TP** | Testing Plan | Defines testing infrastructure, conventions, output contract, and the regression testing process. |
| **CTLv3** (also **CTL**) | Z2K Core Template Library v3 | The template library under test — the collection of Handlebars templates, block templates, and supporting files that make up the Z2K template system. |
| **Feature** | — | A discrete capability area, represented by a numbered file in the `features/` folder. In this project, a feature is typically a template file, a domain of templates, or a cross-cutting quality concern. |
| **Requirement** | — | A specific expected behavior tagged as either `quantitative` (script-testable) or `qualitative` (AI-assessed), identifiable by a compound `NNN-RRR` ID. |
| **Command Queue** | — | A file-based automation system in Z2K Templates. JSON files dropped into a watched directory are automatically processed to create notes from templates. Used as the rendering mechanism for quantitative tests. |
| **JSON Package** | — | A JSON file containing a `cmd`, `templatePath`, field data, and control flags (`"prompt": "none"`, `"finalize": true`). Consumed by the Command Queue to create a note. |
| **Scorecard** | Template Quality Scorecard | A maintained project document defining qualitative assessment criteria. Used by the AI quality agent. |
| **Test Suite Refresh** | — | A named process for updating a feature's test folder when its requirements change. See §4. |

<Add project-specific terms below as the project progresses.>


### 1.4 Document Highlighting Conventions

The following highlighting conventions are used across all project documents:

- `==highlighted text==` — **Open question** — an unresolved decision or ambiguity that must be addressed before the section can be finalized, typically with the user.
- `===triple-highlighted text===` — **AI directive** — an instruction specifically addressed to an AI agent executing tasks in this project.

These follow the Z2K documentation library highlighting nomenclature.


### 1.5 Long Form Usage Feedback

When the user provides you at any point a long-form response to a document revision or creation, always save these into a "User Feedback" folder created under the Primary Project Folder. This ensures that all user feedback is preserved and can be referenced later if needed, and also allows you to track the evolution of user feedback over time. Create a subfolder for Archived conversations.

---

---

## 2. Success Criteria

- [ ] All identified templates in the CTLv3 library have corresponding feature files with enumerated requirements
- [ ] All features have automated test suites (quantitative tests via Command Queue rendering)
- [ ] All features with qualitative requirements pass the AI quality scorecard at or above threshold
- [ ] The master regression test passes in both script-only and full (with AI) modes
- [ ] Feature 001 (Infrastructure Test) passes, confirming project structure and Command Queue functionality
- [ ] Testing infrastructure is self-documenting and can be run without human intervention (except Obsidian being running)
- [ ] Template Quality Scorecard exists and covers all qualitative global requirements
- [ ] Test Suite Refresh Process is documented and executable by an AI agent standalone

---

## 3. Project Documentation

Note: all project documents reside in the Primary Project Folder listed above unless otherwise noted.


### 3.1 Core Project Documents (Authority Order)

1. **Statement of Work**
    – Defines the project, its structure, and the Project Framework.
    - `CTLv3 Sustaining - 1 - Statement of Work.md`

2. **Project Requirements Document**
    – Describes the structural conventions for features, requirements, and their organization. Also contains domain knowledge (what the CTL domains are and what they're for).
    - `CTLv3 Sustaining - 2 - Project Requirements.md`

3. **Implementation Plan**
    – Describes the drop folder mechanism and the handoff to external implementation.
    - `CTLv3 Sustaining - 3 - Implementation Plan.md`

4. **Testing Plan**
    – Defines testing infrastructure, conventions, output contract, two-tier testing model, and the regression testing process.
    - `CTLv3 Sustaining - 4 - Testing Plan.md`

5. **Template Quality Scorecard**
    – Defines qualitative assessment criteria for the AI quality agent. Derived from global qualitative requirements. Maintained as a living document.
    - `CTLv3 Sustaining - Template Quality Scorecard.md`

If documents conflict, higher authority overrides lower. Notify the user of any significant conflicts or ambiguities between documents.


### 3.2 Project Folder Structure

```
CTLv3 Sustaining/
├── CTLv3 Sustaining - 1 - Statement of Work.md
├── CTLv3 Sustaining - 2 - Project Requirements.md
├── CTLv3 Sustaining - 3 - Implementation Plan.md
├── CTLv3 Sustaining - 4 - Testing Plan.md
├── CTLv3 Sustaining - Template Quality Scorecard.md
├── CTLv3 Sustaining - Project Phase Tracker.md
├── drop/
│   └── (incoming feature descriptions — processed and moved to features/)
├── features/
│   ├── 001 - Infrastructure Test.md
│   ├── 0XX - <Infrastructure/Domain Feature>.md
│   ├── 0XX - <Template Feature>.md
│   └── ...
├── tests/
│   ├── run_all_tests.py
│   ├── shared/
│   │   ├── (reusable Python utilities)
│   │   ├── (shared JSON packet templates)
│   │   └── (common expected output fragments)
│   ├── 001 - Infrastructure Test/
│   │   ├── test_plan.md
│   │   ├── run_tests.py
│   │   └── ...
│   ├── 0XX - <Feature Name>/
│   │   ├── test_plan.md
│   │   ├── run_tests.py
│   │   ├── json_packets/
│   │   ├── expected/
│   │   └── ...
│   └── ...
└── User Feedback/
    └── Archived/
```


### 3.3 AI-Maintained Project Files

1. **Project Metadata File**
    - Basic project information (name, owner, folder, repo).
    - `ai-context/shared/library/project/known-projects/CTLv3 Sustaining.md`

2. **Project Phase Tracker**
    - Tracks the current state of the project and any in-progress activity, for session continuity.
    - `CTLv3 Sustaining - Project Phase Tracker.md`


### 3.4 Reference Doc Index

Key reference documents that agents working on this project should be familiar with:

| Document | Path | Purpose |
|---|---|---|
| Reference Manual for AI | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Appendix/Reference Manual for AI.md` | **Always load first** — comprehensive AI-friendly reference for all plugin features |
| Command Queues Overview | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/URI, JSON, Command Queues/Command Queues/Command Queues Overview.md` | How Command Queues work — the rendering mechanism for quantitative tests |
| JSON Packages Overview | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/URI, JSON, Command Queues/JSON Packages/JSON Packages Overview.md` | JSON Package format specification |
| Template Quality Scorecard | `CTLv3 Sustaining - Template Quality Scorecard.md` | Qualitative assessment criteria |
| Z2K Card Metadata - YAML | `Docs/z2k-system-docs/4 - Z2K Reference Docs/4b - Data Formats/Z2K Card Metadata - YAML.md` | YAML field structure for Z2K cards |
| Intro to System Blocks | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/System Blocks/Intro to System Blocks.md` | How system blocks work |
| Using System Blocks and fieldInfo | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/System Blocks/Using System Blocks and fieldInfo.md` | fieldInfo in system blocks |
| System Block Stops | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/System Blocks/System Block Stops.md` | Suppressing system block inheritance (Projects) |
| formatStringBulletize | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Built-In Helper Functions/Formatting Functions/formatStringBulletize.md` | Conditional section rendering |
| Storing Field Values in YAML | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Z2K Templates and YAML/Storing Field Values in YAML.md` | YAML mirroring for blocks and templates |
| z2k_template_suggested_title | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Z2K Templates and YAML/YAML Configuration Properties/z2k_template_suggested_title.md` | Title expression syntax |
| Z2K Metadata Specification v3.0 | `Docs/z2k-design-notes/Z2K System - Design Notes/Z2K Data Architecture/Z2K Metadata/Z2K Metadata Specification - Version 3.0.md` | Source type taxonomy |
| formatString | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Built-In Helper Functions/Formatting Functions/formatString.md` | String formatting helpers |
| Template Organization | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Template Folders/Template Organization.md` | Folder structure conventions |
| Naming Fields | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Naming Conventions/Naming Fields` | Field naming conventions |
| URI Actions | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/URI, JSON, Command Queues/URI Actions/URI Actions.md` | URI-based triggering (fallback) |
| Migration Mining Results | `User Feedback/Migration Project Mining Results.md` | Complete template inventory, global requirements, testing patterns, resolved issues |

---

## 4. Project Framework

The CTLv3 Sustaining Project Framework defines the structure and processes for maintaining and validating the template library through feature-based testing. This framework is event-driven: the project remains static until a new feature arrives via the drop folder or a regression test is requested.


### 4.1 Critical Imperatives

- **Project Phase Tracker**: Keep the Project Phase Tracker document updated with the current activity — what feature is being processed, what stage of the per-feature cycle it is in, and any open items. Update it at least when starting and completing each stage of the per-feature cycle.
- **Session Continuity**: Before ending a session, fully update the Project Phase Tracker and any in-progress feature or test documents with sufficient detail to resume in a new session without loss of information. Use `/wf project/save` to perform this save.
- **User Agreement**: Always get clear agreement from the user before transitioning between stages of the per-feature cycle.
- **Request Feedback**: Engage with the user to solicit feedback during feature description and requirements stages. Do not assume your work is sufficient.
- **Phase Rollback Not Applicable**: Phase rollback (as defined in the iterative project framework) does not apply to this sustaining project. Features are small, self-contained units — if a feature's requirements or tests need to change, use the Test Suite Refresh Process (§4.4). If the `/wf project/phase-rollback` workflow consults this project, respond that phase rollback is not applicable for sustaining projects and direct the user to the Test Suite Refresh Process instead.
- **Requirement Tagging**: Every requirement in every feature file must be tagged as either `quantitative` (can be tested by a script) or `qualitative` (requires AI assessment). This drives which tier of testing applies.


### 4.2 Project Structure


#### Feature Numbering Scheme

Features are numbered with three-digit IDs. The `0XX` range (001–099) is reserved for infrastructure, cross-cutting, and domain-level features. Individual template features use numbers 100+.

| Range | Purpose | Examples |
|---|---|---|
| 001 | Infrastructure Test | Project structure validation, Command Queue smoke test |
| 002–019 | System infrastructure | Working System (hello world), Directory Structure, System Blocks |
| 020–039 | Cross-cutting quality | Global Template Quality (quantitative), Template Quality Standards (qualitative) |
| 040–099 | Domain-level features | One per top-level CTL domain (Media, Daily, etc.) |
| 100+ | Individual template features | One per template file in the CTL |

Exact numbers are assigned during feature creation. The ranges above are guidelines, not hard boundaries.


#### `drop/`

The intake point for new features. A file placed here contains a description of a feature to be validated. When the per-feature cycle begins (via `/wf project/implement`), the file is processed, fleshed out with the user, and moved into `features/`. The drop folder should be empty when no feature is being processed.

Future use: An audit agent may generate feature requests for missing templates and place them in the drop folder for processing.


#### `features/`

Contains one Markdown file per feature, numbered with a three-digit prefix. Each feature file contains YAML frontmatter (feature number, description, status, date added, test folder path), a prose description, and enumerated requirements. Each requirement carries a compound `NNN-RRR` ID and a tag of `quantitative` or `qualitative`.

The `features/` folder is self-documenting: YAML frontmatter is machine-greppable for quick discovery.


#### `tests/`

Contains one folder per feature (named identically to the feature file minus `.md`), plus:

- `run_all_tests.py` — master regression script
- `shared/` — reusable Python utilities, shared JSON packet templates, common expected output fragments

Each feature test folder contains `test_plan.md`, `run_tests.py`, and supporting files (JSON packets in `json_packets/`, expected outputs in `expected/`).


#### Feature 001 — Infrastructure Test

Validates the project structure itself and confirms the Command Queue system is operational. This is the hello world: create a JSON packet that instantiates a trivial template and verify the output file is created correctly. A failure here means the testing infrastructure is broken and no other tests should run.


### 4.3 Per-Feature Implementation Cycle

When a new feature arrives in the `drop/` folder (or is otherwise initiated via `/wf project/implement`), the following staged process is executed. Each stage requires user agreement before proceeding to the next.


#### Stage 1 — Describe & Flesh Out

Read the dropped feature description and engage in a back-and-forth discussion with the user to fully flesh out:

- What the feature (template/domain/concern) does
- How to know if it is working correctly
- Context and usage scenarios
- Potential error states and edge cases

Store the refined description back into the feature file. Move the file from `drop/` to `features/` with the next available number (respecting the numbering scheme in §4.2). Update the YAML frontmatter.


#### Stage 2 — Define Requirements

Develop the numbered requirements for this feature. Each requirement must:

- Describe a specific expected behavior, outcome, or aspect of the feature
- Be tagged as `quantitative` or `qualitative`
- Carry a three-digit requirement ID (forming the compound `NNN-RRR` identifier)
- Be independently testable (quantitative) or assessable (qualitative)

Iterate with the user until requirements are complete and unambiguous.


#### Stage 3 — Build Test Suite

Create the corresponding test folder in `tests/` and develop:

- `test_plan.md` — maps each requirement to test assertions, noting which are quantitative (scripted) and which are qualitative (AI-assessed)
- `run_tests.py` — automated test script following the output contract in the Testing Plan
- JSON packets in `json_packets/` for Command Queue-based rendering tests
- Expected output files in `expected/` for diff-based validation
- Any supporting files

Quantitative tests must be fully automated. Qualitative tests are handled by the AI scorecard agent invoked by `run_tests.py` (or the master regression script, depending on configuration). See the Testing Plan for the full specification.


#### Stage 4 — Implement

Implementation is **external to this project**. The user handles implementation using other workflows (e.g., `/wf code/plan`, `/wf code/implement`). This stage is a handoff — the feature description and requirements serve as the specification.

This stage may be skipped if the feature is already implemented (common for this project, since most CTLv3 templates already exist).


#### Stage 5 — Acceptance Testing

Before running any tests, execute the **Test Session Initiation** process (§4.4) to establish mode and scope for the session.

Run the feature's test suite and evaluate results:

- If all quantitative tests pass and qualitative score meets threshold: proceed to Stage 6.
- If tests fail: execute the **Failure Handling and Fix Process** (§4.4).

The iteration loop (adjust → re-test) continues until the feature passes acceptance.


#### Stage 6 — Regression

After a feature passes acceptance, run the master regression test (`tests/run_all_tests.py`) to confirm no existing features were broken.

- If regression passes: mark the feature as `Complete`.
- If regression fails: investigate and resolve before marking complete.


### 4.4 Named Processes


#### Test Suite Refresh Process

When a feature's requirements change (requirements added, modified, or removed), the test suite must be updated to match. This process is the sustaining project's equivalent of phase rollback — but scoped to a single feature and without the formality of document locking.

**Steps:**

1. **Read the updated feature file** — identify which requirements changed, were added, or were removed.
2. **Update `test_plan.md`** — add/modify/remove test assertions to match the new requirements. Ensure every requirement has at least one corresponding test.
3. **Update `run_tests.py`** — modify the test script to implement the new/changed assertions.
4. **Update expected outputs** — regenerate any expected output files in `expected/` that are affected by the changes. Create new JSON packets in `json_packets/` if needed.
5. **Run the feature's tests** — execute `run_tests.py` and verify all tests pass.
6. **Run regression** — execute `run_all_tests.py` to confirm no other features are affected.

This process must be documented thoroughly enough that an AI agent can execute it standalone without user input. The Testing Plan (§ "Test Suite Refresh Procedure") contains the detailed procedural specification.

**Trigger:** This process is triggered whenever a feature file's requirements section is modified. It can be invoked by the user or by an AI agent.


#### Test Session Initiation

Before running any feature test or regression (whether via `/wf project/implement`, `/wf project/regress`, or directly), ask the user these three questions. The answers govern the entire session — do not re-ask mid-session unless the user explicitly changes direction.

**Question 1 — Scope**: Run tests for a specific feature, or full regression against all features?
- *Specific feature*: prompt for the feature number (e.g., 020)
- *Full regression*: run `run_all_tests.py`

**Question 2 — Test mode**: Script-only (quantitative only, `--no-quality`), or Full (quantitative + AI qualitative)?
- Script-only is faster and free; use when doing rapid iteration
- Full includes AI scorecard assessment; use for definitive acceptance or scheduled regression

**Question 3 — Fix mode**: Test-only, or Test + Fix?
- *Test-only*: report failures and stop; do not modify any files
- *Test + Fix*: on failure, proceed to the Failure Handling and Fix Process (below)

**Defaults when auto-triggered** (e.g., a new template is dropped into `drop/`): Full (AI + script), test-only, specific feature.

Record the session mode in the Phase Tracker at the start of each session so it is explicit and reviewable.


#### Failure Handling and Fix Process

When a test fails, follow these steps in order. Do not skip steps.

**Step 1 — Categorize the failure**

Determine which category the failure falls into before taking any action:

- **Test bug**: The test assertion is wrong (e.g., checking the wrong field name, wrong expected value). The requirement is fine; the test script needs to change. → Use the Test Suite Refresh Process, not this one.
- **Implementation gap**: The requirement is correct and the template simply does not comply (e.g., a required field is missing). No PRD change needed. → Proceed to Step 2.
- **Requirements gap**: The failure reveals that a requirement is missing, incorrect, or outdated. The PRD itself needs to change. → STOP. Document the finding and put it into human review state. Do not proceed to fix until the user has reviewed and resolved the requirements gap.
- **Infrastructure issue**: The failure is in the test infrastructure (Command Queue, Obsidian not running, etc.). → Resolve infrastructure first; re-run tests.

**Step 2 — Check PRD impact**

Even for implementation gaps, confirm the fix does not implicitly require a PRD change. Ask: does making this fix require adding, removing, or modifying any requirement? If yes → treat as a Requirements gap (above) and STOP. If no → proceed to Step 3.

**Step 3 — Propose the fix** *(interactive mode)*

Before modifying any file, state clearly:
- What is wrong
- What the proposed fix is (specific change to which file(s))
- How many files are affected

If more than 10 files are affected, explicitly flag this and obtain user approval before proceeding.

In automation mode, skip this step and proceed directly to Step 4. The user will review changes at git commit time.

**Step 4 — Execute the fix**

Make the minimum change necessary to bring the template(s) into compliance. Re-run the specific test to verify it now passes.

**Do not commit.** Leave all changes in git status for human review before any commit is made.

**Step 5 — Post-fix regression**

After the specific test passes, run the full regression (`run_all_tests.py --no-quality` at minimum) to confirm no other features were broken by the fix.

**Step 6 — Document**

Update the Phase Tracker with a note on what was fixed. If the failure revealed a process gap (e.g., a step was missed during migration), note it so future processes can be improved.

**Trigger:** This process is triggered whenever a test fails during Stage 5 or regression, and fix mode is active.


### 4.5 Testing Architecture

The project uses a two-tier testing model. Both tiers are integrated into the regression framework.


#### Tier 1 — Quantitative Testing

Quantitative tests are script-automated and deterministic. The primary mechanism is:

1. A Python test script creates a JSON Package file (specifying the template, `"prompt": "none"`, `"finalize": true`, and field data).
2. The script drops the JSON file into the Command Queue folder.
3. The script waits for the Z2K Templates plugin to process the command (monitoring for the file to appear in `done/` or the output note to be created).
4. The script reads the rendered output file and compares it against the expected output (diff).
5. Pass/fail is determined by whether the rendered output matches expectations.

**Prerequisites:** A running Obsidian instance with the Z2K Templates plugin active and Command Queues enabled.

Quantitative tests also include non-rendering checks: verifying folder structure, checking field naming conventions (e.g., no lowercase-initial custom fields unless they're built-ins), validating Handlebars syntax, and confirming system block presence.


#### Tier 2 — Qualitative Testing

Qualitative tests use an AI agent to assess templates against the Template Quality Scorecard. The mechanism:

1. A Python script invokes Claude (via CLI or API) with the template content and the scorecard criteria.
2. The AI agent evaluates the template against each scorecard item and produces a score and list of suggestions.
3. The score is compared against the passing threshold defined in the Testing Plan.
4. Pass/fail is determined by whether the score meets or exceeds the threshold.

**Two modes:**

- **Analysis mode** (default): Read-only. Outputs the scorecard results, score, and suggestions. Does not modify any files. This mode runs during standard regression.
- **Fix mode** (explicit invocation only): The AI agent iteratively improves the template based on scorecard suggestions. **Safeguards:** Fix mode requires an explicit command flag AND user confirmation before execution. Changes are reviewable via Git diff.

**Per-feature override:** A feature's `test_plan.md` may include a `quality_override: pass` flag to force the qualitative test to pass regardless of score. This is intended for intentionally simple templates that would score low due to their simplicity, not due to quality issues.


#### Regression Testing

A full regression test can be triggered at any time via `tests/run_all_tests.py` or `/wf project/regress`.

**Two regression modes:**

- **Full regression** (default): Runs both quantitative and qualitative tests. Includes AI agent calls. Slower, costs API tokens.
- **Script-only regression** (`--no-quality` flag): Runs only quantitative tests. No AI calls. Fast and free. Suitable for quick validation after minor changes.

The regression script iterates through every feature test folder, runs each `run_tests.py`, aggregates results per the output contract in the Testing Plan, and reports overall pass/fail.

---

## 5. Risks

- **Command Queue timing**: Tests depend on the Command Queue scan interval (default 60s). Tests must account for processing delay. Mitigation: Use the "Process Command Queue Now" command palette action where possible, or configure a shorter scan interval for the test vault.
- **Obsidian dependency**: All rendering tests require a running Obsidian instance. Mitigation: Feature 001 (Infrastructure Test) validates Obsidian + Command Queue functionality before other tests run.
- **AI quality assessment cost**: Full regression with qualitative tests incurs Claude API costs. Mitigation: Script-only mode available; run full regression only when needed.
- **AI quality assessment consistency**: AI scoring may vary between runs. Mitigation: Scorecard criteria should be specific enough to minimize variance; threshold should have margin.
- **Template library evolution**: Templates may change outside this project's awareness. Mitigation: Regular regression testing; expected outputs updated via Test Suite Refresh Process.

---

## 6. Constraints

- **Running Obsidian required**: Quantitative tests cannot execute without a running Obsidian instance with Z2K Templates plugin and Command Queues enabled.
- **Python**: Test scripts are written in Python.
- **Command Queue must be enabled**: The Command Queue feature is disabled by default in Z2K Templates. The test vault must have it explicitly enabled in settings.
- **Single-machine queue processing**: Command Queues are processed by one Obsidian instance. Tests must run on the same machine.

---

## 7. Dependencies

- Z2K Template Engine (`Code/Obsidian Plugins/z2k-template-engine/`)
- Z2K Template Plugin (`Code/Obsidian Plugins/z2k-plugin-templates/`)
- Z2K Testing Vaults (`Data/Vaults/z2k-testing-vaults/`)
- Python 3.x (for test scripts)
- Claude API access (for qualitative testing)
- Obsidian (running instance for Command Queue processing)
- Z2K Templates Reference Manual (`Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/`)

---

## 8. Acceptance & Closure

The sustaining project is considered healthy when:

- All success criteria are met.
- All feature test suites pass (both tiers).
- The master regression test passes in full mode.
- No open critical issues remain.

The sustaining project may be closed when the CTLv3 template system is retired or the sustaining effort is no longer needed. Status must be updated to "Completed".
