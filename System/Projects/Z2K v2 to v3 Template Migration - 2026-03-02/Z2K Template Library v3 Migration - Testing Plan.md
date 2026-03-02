---
document_type: Testing Plan
status: Locked
---
# Testing Plan — Z2K Template Library v3 Migration

> [!WARNING] TESTING PLAN AUDIT REQUIRED ON UPSTREAM DOCUMENT CHANGES
> Whenever the **Statement of Work**, **Project Requirements Document**, or **Implementation Plan** is changed — including changes made during a phase rollback — this Testing Plan must undergo a **full-scale audit** before the next phase begins.
>
> The audit must verify:
> 1. Every requirement in the PRD has at least one test assertion mapped to it in this document
> 2. Every task in the IP has at least one test assertion mapped to it in this document
> 3. Any requirements or tasks added or modified by the upstream change have new validation steps explicitly assigned
>
> **This audit is not optional.** The Testing Plan may not be re-locked until the audit is complete and all gaps are resolved. No execution phase may begin with a known coverage gap.


## Overview

This plan defines how CTL v3 implementation tasks will be validated. All testing prioritizes automation. User-assisted testing is explicitly deferred to a future revision of this document.

**Guiding principles:**
- Tests must be scripted, repeatable, and runnable as regression tests
- Tests assert deterministic outputs — no AI judgment about whether something "looks right"
- Automated tests first; user-assisted tests last
- Scripts are grouped by phase/chunk, not one per task
- Phase 0 (Testing Infrastructure Validation) must complete before this plan is considered final — primary testing method (Command Queue vs URI) is subject to TP-0 findings

---

## Testing Infrastructure

### Testing Vault

A dedicated vault is created for CTL v3 testing:

**Path:** `Data/Vaults/z2k-testing-vaults/Z2K System Vault Testing/`

This vault is separate from `Templates Test Vault - Primary/` (maintained by another developer — do not modify). It has the Z2K Templates Plugin installed with Command Queue enabled.

**Queue folder:** `.obsidian/plugins/z2k-plugin-templates/command-queue/`
**Scan frequency:** 10s (fast turnaround during testing)

### Primary Testing Method: Command Queue

Command Queue is the preferred testing method. Tests are executed by:

1. Writing one or more `.json` or `.jsonl` command files to the vault's queue folder
2. Triggering "Process Command Queue Now" from the Obsidian Command Palette (user-assisted trigger; one action per test run)
3. Polling for output files using the test script
4. Asserting output content against expected files

**JSON package pattern for document template tests:**
```json
{
  "cmd": "new",
  "templatePath": "<vault-relative path to template>",
  "destDir": "Testing/Output/<test-name>/",
  "fileTitle": "output",
  "prompt": "none",
  "finalize": true,
  "<FieldName>": "<value>",
  ...
}
```

**JSON package pattern for block template tests:**
```json
{
  "cmd": "insertblock",
  "blockPath": "<vault-relative path to block>",
  "existingFilePath": "Testing/Output/<test-name>/target.md",
  "location": "file-bottom",
  "prompt": "none",
  "finalize": true,
  "<FieldName>": "<value>",
  ...
}
```

**URI fallback:** If Command Queue has blocking bugs (determined in TP-0.2/TP-0.3), tests fall back to URI-based triggering via `subprocess.run(["open", uri])`. The test script structure is identical; only the trigger mechanism differs.

### Script Storage

All CTL v3 test scripts live in the project's `Testing/` subfolder:

```
Testing/
  scripts/
    test-structure.py          # Structure/existence tests (Phases 0–3)
    test-blocks.py             # Block template tests (Phases 4–5)
    test-templates.py          # Document template tests (Phase 6)
    lib/
      runner.py                # Shared: Command Queue dispatch, file polling, assertion helpers
      yaml_utils.py            # YAML parsing and assertion helpers
  commands/
    <phase>/                   # JSON command files, one per template test
  expected/
    <test-name>/
      expected.md              # Golden output file (saved on first passing run)
```

### Expected Output Model

For template instantiation tests, the expected output is saved as a "golden file" on the first successful run and used for regression comparison on all subsequent runs.

Workflow:
1. Write the template (Phase 4/5/6 execution task)
2. Run the test script — if no `expected.md` exists yet, the script instantiates the template, displays the output, and prompts: "Is this output correct? [y/n]"
3. On confirmation, `expected.md` is saved to `Testing/expected/<test-name>/`
4. All future runs diff actual output against `expected.md` automatically — no user judgment required

---

## Test Categories

### Category A — Structure Tests

**What is tested:** File and folder existence; YAML field presence in system-block files.

**How it works:** Pure Python — uses `os.path.exists()` and YAML parsing. No Obsidian or plugin involvement.

**Script:** `Testing/scripts/test-structure.py`

**Target vault:** `Data/Vaults/z2k-default-vault/` (the production vault being built)

**What counts as pass:** Every asserted path exists; every YAML field check matches expected value/pattern.

### Category B — Template Instantiation Tests

**What is tested:** Template rendering end-to-end — system-block injection, `{{fieldInfo}}` resolution, block partial inclusion, YAML output, markdown body output.

**How it works:** Command Queue dispatch → output file polling → diff against expected.

**Scripts:** `Testing/scripts/test-blocks.py`, `Testing/scripts/test-templates.py`

**Target vault:** `Data/Vaults/z2k-testing-vaults/Z2K System Vault Testing/` (the testing vault)

**What counts as pass:** Output file created; content matches `expected.md` exactly (or within a normalized comparison that strips dynamic values like timestamps and wikilinks with today's date).

> **Note on dynamic fields:** Fields like `{{wikilink today}}` and `{{timestamp}}` produce values that change per run. The test runner must normalize these (replace with `<TODAY>`, `<TIMESTAMP>` etc.) before comparison. `expected.md` stores the normalized form.

---

## Test Coverage by Implementation Phase

### Phase 0 — Testing Infrastructure

| Test | Category | Script | Pass Condition | IP Task |
|---|---|---|---|---|
| Testing vault exists | A | test-structure.py | `Z2K System Vault Testing/` folder exists | TP-0.1 |
| Plugin installed | A | test-structure.py | Plugin folder + `manifest.json` exist | TP-0.1 |
| Command Queue hello-world | B | TP-0 ad hoc | Output file created; command in `done/` | TP-0.2 |

### Phase 1 — Vault Structure

| Test | Category | Script | Pass Condition | IP Task |
|---|---|---|---|---|
| All 13 domain folders exist | A | test-structure.py | All domain roots exist | 1.1, 1.2, 1.6 |
| All domain `Templates/` subfolders exist | A | test-structure.py | 13 × `Templates/` exist | 1.1, 1.2, 1.3, 1.6 |
| `Templates/` root folder exists | A | test-structure.py | `Templates/` at vault root | 1.5 |
| `Projects/My Writings/Templates/` exists | A | test-structure.py | Path exists | 1.4 |
| `Body/`, `AI/`, `System/Templates/` exist | A | test-structure.py | All 3 paths exist | 1.1, 1.2, 1.3 |

### Phase 2 — Root System Block

| Test | Category | Script | Pass Condition | IP Task |
|---|---|---|---|---|
| `.system-block.md` exists | A | test-structure.py | File exists | 2.1 |
| YAML: required fields present | A | test-structure.py | `z2k_metadata_version`, `z2k_creation_creator`, `z2k_creation_date`, `z2k_creation_timestamp`, `z2k_creation_template`, `z2k_creation_language`, `z2k_creation_library_version`, `z2k_card_source_type` all present | 2.1 |
| YAML: removed fields absent | A | test-structure.py | `z2k_creation_domain`, `z2k_card_build_state`, `z2k_card_status` not present | 2.1 |
| Body: `{{fieldInfo me}}` present | A | test-structure.py | File body contains `{{fieldInfo me` | 2.1 |

### Phase 3 — Domain System Blocks

| Test | Category | Script | Pass Condition | IP Task |
|---|---|---|---|---|
| All 13 domain `.system-block.md` files exist | A | test-structure.py | All 13 paths exist | 3.1–3.13 |
| Each has correct `z2k_creation_domain` value | A | test-structure.py | YAML field matches expected string per domain | 3.1–3.13 |
| Ratings domains have ratings fields | A | test-structure.py | `z2k_rating_depth`, `z2k_rating_surprisal`, `z2k_rating_passion` in Thoughts, Beliefs, Information, Memories system-blocks | 3.1, 3.2, 3.3, 3.4 |
| Journals has `z2k_card_privacy` | A | test-structure.py | `.:Z2K/Privacy/Private/Journal` | 3.6 |
| Logs has `z2k_card_privacy` | A | test-structure.py | `.:Z2K/Privacy/Private/Log` | 3.7 |

### Phase 4 — Root Block Templates

| Test | Category | Script | Pass Condition | IP Task |
|---|---|---|---|---|
| All 5 block files exist | A | test-structure.py | All 5 paths in `Templates/` exist | 4.1–4.5 |
| Each has `z2k_template_type: block-template` | A | test-structure.py | YAML field present | 4.1–4.5 |
| Quotation instantiation | B | test-blocks.py | Output matches expected (Content.* fields rendered) | 4.2 |
| Citation instantiation | B | test-blocks.py | Output matches expected; field names consistent with Quotation | 4.3 |
| Card Fabric instantiation | B | test-blocks.py | Output matches expected; `{{formatStringBulletize}}` renders correctly | 4.4 |
| Perspective - Me instantiation | B | test-blocks.py | Output matches expected; `[!me]` callout present | 4.1 |
| Extended YAML instantiation | B | test-blocks.py | Output matches expected; YAML fields rendered | 4.5 |

> **Dot-notation test (BLK-001/004/005):** Quotation block test inherently validates whether `Content.Author` dot-notation works. If the output file shows `{{Content.Author}}` verbatim (unfilled), dot-notation is unsupported — log a plugin bug and switch to flat field names.

### Phase 5 — Domain Block Templates

| Test | Category | Script | Pass Condition | IP Task |
|---|---|---|---|---|
| All 8 domain block files exist | A | test-structure.py | All 8 paths in domain `Templates/` exist | 5.1–5.8 |
| Each has `z2k_template_type: block-template` | A | test-structure.py | YAML field present | 5.1–5.8 |
| Each block instantiates without error | B | test-blocks.py | Output created; no error log generated | 5.1–5.8 |
| Health Log: Flame fields preserved verbatim | B | test-blocks.py | All `{{Flame-*}}` field names appear unfilled in output (no-prompt) | 5.8 |

### Phase 6 — Document Templates

| Test | Category | Script | Pass Condition | IP Task |
|---|---|---|---|---|
| All templates exist in correct locations | A | test-structure.py | All ~68 target paths exist | 6.1–6.14 |
| Each has `z2k_template_type: document-template` | A | test-structure.py | YAML field present | 6.1–6.14 |
| Each has `z2k_template_version` | A | test-structure.py | YAML field present | 6.1–6.14 |
| Each has `z2k_template_suggested_title` | A | test-structure.py | YAML field present | 6.1–6.14 |
| Each template instantiates without error | B | test-templates.py | Output created; no error log generated | 6.1–6.14 |
| System-block YAML injection works | B | test-templates.py | Output YAML contains `z2k_creation_domain` from domain system-block | 6.1–6.14 |
| Personal templates have correct `z2k_template_author` | A | test-structure.py | `Geoff (z2k-gwp)` in personal template YAML | 6.4, 6.5, 6.9 |
| Privacy templates have correct `z2k_card_privacy` | A | test-structure.py | Correct value per domain (Journals, Logs, personal templates) | 6.4, 6.7, 6.8 |

### Phase 7 — Supporting Documentation

| Test | Category | Script | Pass Condition | IP Task |
|---|---|---|---|---|
| AI Recommendations doc exists | A | test-structure.py | `AI/Z2K Template Library - AI Recommendations.md` exists | 7.1 |
| Tags Taxonomy placeholder exists | A | test-structure.py | `System/Z2K Tags Taxonomy.md` exists | 7.2 |
| Library Version card exists | A | test-structure.py | `System/Z2K Template Library - v3.md` exists | 7.3 |

---

## Coverage Completeness Check

Every IP task must appear in at least one test row or have an explicit exclusion rationale. This section is the traceability gate — no execution phase may begin with an unresolved coverage gap in prior phases.

**Fully covered tasks** (each has at least one test row in the phase tables above):

- Phase 0: TP-0.1, TP-0.2
- Phase 1: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6
- Phase 2: 2.1
- Phase 3: 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 3.10, 3.12
- Phase 4: 4.1, 4.2, 4.3, 4.4, 4.5
- Phase 5: 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8
- Phase 6: 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9, 6.10, 6.11, 6.12, 6.14
- Phase 7: 7.1, 7.2, 7.3

**Excluded tasks** (no test coverage required):

| IP Task | Reason |
|---|---|
| TP-0.3 | Conditional fallback path; skip condition if TP-0.2 passes; no structural artifact to test |
| TP-0.4 | Documentation/decision task; no structural artifact |
| 6.13 | No templates created — AI domain receives system-block only; template content deferred |
| 8.1–8.8 | Cleanup and archival tasks only; no independently testable artifacts |

**Known coverage gaps** (automated tests insufficient; manual validation required):

| IP Task | Gap | Resolution |
|---|---|---|
| 3.11 | AI authorship/perspective field not yet designed (open issue AI-PERSP); no test row for this field | Add test row when AI-PERSP design is finalized |
| 3.13 | System Block Stop functional behavior (suppression of z2k_* fields in project subfolders) cannot be verified by file-system check alone | Manual Obsidian validation required during Phase 3 execution; document result in IP §Task 3.13 |

---

## Assertion Normalization

The following dynamic values must be normalized before comparing actual vs expected output:

| Dynamic value | Normalization |
|---|---|
| `{{wikilink today}}` rendered output | `<TODAY_WIKILINK>` |
| `{{timestamp}}` rendered output | `<TIMESTAMP>` |
| `{{wikilink creator}}` rendered output | `<CREATOR_WIKILINK>` |
| `{{wikilink templateName}}` rendered output | `<TEMPLATE_WIKILINK>` |

Any field left unfilled (placeholder preserved) is compared literally — if the expected output has `{{FieldName}}`, the actual must too.

---

## Deferred: User-Assisted Testing

The following testing activities require user involvement and are explicitly deferred to a future revision of this Testing Plan:

- **Prompting interface validation:** Verifying that `{{fieldInfo}}` prompts appear correctly in Obsidian's UI with correct field types, labels, and defaults
- **End-to-end vault workflow:** Manually creating a card from each template in the live vault and verifying the result in Obsidian (visual formatting, wikilinks, rendering)
- **Dot-notation UX test:** If dot-notation works syntactically (Category B passes), a manual check that the prompt groups fields under namespaced headings in the UI
- **Block insertion UX test:** Manually triggering `{{> BlockName}}` from within a document and confirming the picker and insertion work correctly

These tests are not blocked — they can begin as soon as templates are written. They are deferred from this document because they cannot be scripted with current tooling.

---

## Open Items

| ID | Issue | Blocking |
|---|---|---|
| TP-INF-001 | Command Queue confirmed as primary method? (TP-0 result) | Testing Plan finalization |
| TP-INF-002 | Can "Process Queue Now" be triggered non-interactively (URI/AppleScript)? | Not blocking; nice-to-have |
| TP-INF-003 | Exact normalization rules for dynamic fields — confirm all dynamic built-ins | test-templates.py authoring |
