# Project Phase Tracker - CTLv3 Sustaining


## Project State

**Status:** Active


## Current Activity

**Activity:** Active — Feature testing, regression, and acceptance validation
**Stage:** Per-feature cycle (see Statement of Work §4 for cycle stages)


## Current Activity Details

Per-feature cycle in progress. Features 001–004 and 020 have test suites. Features 001–004 are Complete. Feature 020 (Global Template Quality) test suite was built this session — the regression currently has outstanding failures in Feature 020 that need to be resolved.

**Next recommended action:** Run the regression to assess the current state, then follow the SoW §4.4 processes (Test Session Initiation, Failure Handling and Fix Process) to resolve any failures.
```
cd "Data/Vaults/z2k-default-vault/System/Projects/CTLv3 Sustaining/tests"
python3 run_all_tests.py --feature 001
```


## Work Chunks

The remaining setup work is broken into chunks designed to fit within a single session each. Each chunk should be completable independently given the context below.

### Chunk 1: Rewrite SoW + Testing Plan ← DONE
**Status:** Complete (2026-03-02)
**What to do:**
1. Read Command Queues documentation: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/URI, JSON, Command Queues/Command Queues/Command Queues Overview.md`
2. Rewrite `CTLv3 Sustaining - 1 - Statement of Work.md` to incorporate:
   - Two-tier testing model: quantitative (script-automated) + qualitative (AI scorecard agent)
   - Command Queue testing mechanism (JSON packets → Obsidian → rendered file → diff)
   - Qualitative AI agent: analysis mode (score + suggestions) and fix mode (explicit user confirmation required, safeguards)
   - Test Suite Refresh Process — named process for updating test folders when feature requirements change (executable by AI agent standalone). Steps: update test_plan.md → update run_tests.py → update expected outputs → run and verify.
   - Feature numbering scheme: 0XX range for infrastructure/domain features, higher numbers for individual template features
   - Reference doc index (key pages agents need — to be populated from migration project in Chunk 2)
   - Drop folder audit agent concept (future use: AI identifies missing templates, generates feature requests)
   - Phase rollback not applicable (already present)
   - Requirement tagging: each requirement tagged `quantitative` or `qualitative`
   - Running Obsidian instance as a prerequisite for testing
   - Hello world smoke test as first validation
3. Rewrite `CTLv3 Sustaining - 4 - Testing Plan.md` to incorporate:
   - Command Queue mechanism details (how JSON packets work, timing, cleanup)
   - Two-tier model: quantitative script tests + qualitative AI agent tests
   - Shared test resources: `tests/shared/` for reusable scripts and JSON packets
   - `run_all_tests.py` modes: full regression (with AI quality) vs script-only (`--no-quality` or similar)
   - Qualitative scorecard: maintained as `Template Quality Scorecard.md` project document, derived from global requirements
   - Passing threshold defined in Testing Plan, with per-feature override flag in feature's test_plan.md
   - Fix mode safeguards: explicit command, user confirmation, Git comparison
   - Test Suite Refresh Process — detailed procedural steps (same as initial creation)
   - Hello world smoke test specification
4. Present both documents to user for review.

**Key context:**
- User feedback document: `User Feedback/Initial Setup.md` (read this first — contains all design decisions)
- Command Queues docs: `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/URI, JSON, Command Queues/Command Queues/Command Queues Overview.md`
- Current SoW: `CTLv3 Sustaining - 1 - Statement of Work.md`
- Current Testing Plan: `CTLv3 Sustaining - 4 - Testing Plan.md`

### Chunk 2: Mine Migration Project ← DONE
**Status:** Complete (2026-03-02)
**What to do:**
1. Read the migration project at `Data/Vaults/z2k-default-vault/System/Projects/Z2K v2 to v3 Template Migration - 2026-03-02/`
2. Focus on: PRD (per-template and per-domain requirements, global requirements), Agent Brief (reference docs, agent context), Testing approach (JSON/command queue patterns)
3. IGNORE: iterative framework process in SoW, old template migration procedures, anything about converting v2→v3
4. Compile findings into a working document: `User Feedback/Migration Project Mining Results.md`
5. Extract: list of all templates and their requirements, list of all domains, global system requirements, reference manual pages, testing patterns

**Key context:**
- Sister project folder: `Data/Vaults/z2k-default-vault/System/Projects/Z2K v2 to v3 Template Migration - 2026-03-02/`
- User feedback: `User Feedback/Initial Setup.md` (Q1 answer specifies what to extract)

### Chunk 3: Create Feature Files ← DONE
**Status:** Complete (2026-03-02)
**What to do:**
1. Using the mining results from Chunk 2, create feature files in `features/`:
   - `001 - Infrastructure Test.md` — project structure validation
   - `0XX - Working System.md` — hello world command queue test
   - `0XX - Directory Structure.md` — CTL folder structure validation
   - `0XX - System Blocks.md` — system block functionality
   - `0XX - Global Template Quality.md` — cross-cutting quantitative requirements (valid syntax, naming, formatting, etc.)
   - `0XX - Template Quality Standards.md` — cross-cutting qualitative requirements (AI scorecard)
   - `0XX - <Domain Name>.md` — one per top-level domain
   - `0XX+ - <Template Name>.md` — one per individual template
2. Each feature file uses the Feature template with YAML frontmatter, description, and numbered requirements
3. Requirements tagged `quantitative` or `qualitative`
4. Update PRD (`CTLv3 Sustaining - 2 - Project Requirements.md`) with domain knowledge section

**Key context:**
- Mining results: `User Feedback/Migration Project Mining Results.md` (from Chunk 2)
- Feature template: `ai-context/shared/library/project/templates/sustaining/Template - sustaining - Feature.md`

### Chunk 4: Create Test Infrastructure + Scorecard ← DONE
**Status:** Complete (2026-03-02)
**What to do:**
1. Create `tests/shared/` with reusable Python utilities and JSON packet templates
2. Create `tests/run_all_tests.py` — master regression script with `--no-quality` flag
3. Create `tests/001 - Infrastructure Test/` folder with test_plan.md and run_tests.py
4. Create hello world smoke test (in Working System feature's test folder)
5. Create `Template Quality Scorecard.md` — derived from qualitative global requirements
6. Update Implementation Plan if needed
7. Run Feature 001 test to verify infrastructure works
8. Transition project state to Active

**Key context:**
- Testing Plan: `CTLv3 Sustaining - 4 - Testing Plan.md` (defines all conventions)
- Command Queues docs: see Chunk 1 reference
- Feature files: created in Chunk 3


## Completed Actions (Current Activity)

- Project folder structure created (drop/, features/, tests/, User Feedback/)
- Project Metadata file created in known-projects
- Template documents copied into project folder (SoW, PRD, IP, TP, Phase Tracker)
- Initial SoW draft created and reviewed by user
- User provided extensive feedback in `User Feedback/Initial Setup.md`
- 14 clarifying questions asked and answered (all in Initial Setup.md)
- All design decisions recorded and confirmed
- **Chunk 1 complete:** SoW and Testing Plan fully rewritten with two-tier testing model, Command Queue mechanism, qualitative AI agent, Test Suite Refresh Process, feature numbering scheme, and all user feedback incorporated.
- **Chunk 2 complete:** Migration project mined. Results in `User Feedback/Migration Project Mining Results.md` — 80 templates inventoried, 13 domains cataloged, global requirements extracted (naming, metadata, structure, qualitative standards), reference doc index populated (16 entries in SoW §3.4), testing patterns documented (Command Queue, golden file model, normalization), 6 resolved open issues recorded, 8 successor project items carried forward. Qualitative threshold set to 70% in Testing Plan §3.2.3.
- **Chunk 3 complete:** 90 feature files created in `features/`. Numbering scheme: 001-004 (infrastructure), 020-021 (cross-cutting), 040-052 (domains), 100-179 (individual templates). PRD updated with §3 Feature Numbering Scheme, §4 Cross-Cutting Requirements, §5 Domain Knowledge table. All 71 non-personal templates covered (58 document + 13 block), plus 4 infrastructure features, 2 cross-cutting, and 13 domain features. Personal templates (9) excluded from project scope. Cross-cutting requirements (type, version, title, author) centralized in Feature 020 — not duplicated in individual features.
- **Chunk 4 complete:** Test infrastructure created. `tests/shared/` (config.py, test_utils.py, output_formatter.py, quality_agent.py, JSON templates). `tests/run_all_tests.py` with `--no-quality`, `--feature`, `--fix` flags. `tests/001 - Infrastructure Test/` (test_plan.md, run_tests.py, json_packets/hello_world.json). `tests/002 - Working System/` (test_plan.md, run_tests.py, json_packets/basic.json — expected output pending golden file generation). `CTLv3 Sustaining - Template Quality Scorecard.md` created from Feature 021 (10 items, 70% threshold). Error log integration complete: Feature 001 requirement 001-007 added, Testing Plan §3.1.1 updated with error log steps, §4.2 updated, §7 cleaned up. Project transitioned to Active.


## Remaining Actions (Current Activity)

- [x] **Chunk 1:** Rewrite SoW + Testing Plan (incorporate all feedback)
- [x] **Chunk 2:** Mine migration project for requirements, templates, reference docs
- [x] **Chunk 3:** Create all feature files (infrastructure, domains, templates, global)
- [x] **Chunk 4:** Create test infrastructure, scorecard, PRD update, go Active


## Open Items

- The sustaining project template files (in `ai-context/shared/library/project/templates/sustaining/`) are generic versions. The CTLv3-specific project documents in the project folder will diverge significantly from the templates after rewrites — this is expected and correct.


## Active Session — 2026-03-03 (CTLv3 #5)

**Session mode:** Full regression | Full (quantitative + AI qualitative) | Test + Fix
**Status:** Feature 020 resolved and marked Complete. Regression PASS. Per-feature cycle ongoing.

**Fix applied:** Added `z2k_template_author: "Z2K Studios, LLC"` to 72 CTL templates total:
- 71 templates missing the field entirely
- 1 CTL template (`Beliefs/Templates/Beliefs (General).md`) that had the wrong personal author (`"Geoff (z2k-gwp)"`) — smoke test left by previous session; previously invisible due to false-positive exclusion logic
- Feature 002 golden file updated to reflect the corrected Beliefs author

**PRD update:** Added requirement 020-013 ("No personal templates in the CTL vault") and removed the personal-template exclusion from all 020 checks. Verified via smoke test that the new checks correctly fail on a personal-authored template before fixing it.


## Last Regression Test — 2026-03-03

**Date:** 2026-03-03
**Result:** PASS
**Notes:** Features 001–004 + 020 all passing. 45/45 quantitative requirements (script-only mode). Feature 020 marked Complete with 13 requirements.
