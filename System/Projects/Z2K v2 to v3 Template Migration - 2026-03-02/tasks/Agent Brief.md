---
document_type: Agent Context Brief
status: Active
---
# Agent Context Brief — Z2K Template Library v3 Migration

Read this document before executing any task file in this project. It provides the project-wide constants, constraints, naming conventions, and conversion rules that task files assume but do not repeat.

---

## Project Summary

Migrate the Z2K template library from v2 (Obsidian Templater) to v3 (Z2K Templates Plugin) inside `Data/Vaults/z2k-default-vault`. Deliverables: vault folder structure, root + domain system-blocks, root + domain block templates, ~60 document templates, and supporting documentation.

---

## Key Paths

| Item | Path |
|---|---|
| **Target vault** | `Data/Vaults/z2k-default-vault/` |
| **v2 source templates (READ-ONLY)** | `/Users/gp/Vaults/Z2K (Sync) - Snapshot 2026-02-28/~Templates/` |
| **Testing vault** | `Data/Vaults/z2k-testing-vaults/Z2K System Vault Testing/` |
| **Project folder** | `Data/Vaults/z2k-default-vault/System/Projects/Z2K v2 to v3 Template Migration - 2026-03-02/` |
| **Task files** | `<Project folder>/tasks/` |
| **Template version string** | `v3.0.0 2026-03-02` |

---

## Critical Constraints

- **v2 source is READ-ONLY.** Never modify `/Users/gp/Vaults/Z2K (Sync) - Snapshot 2026-02-28/~Templates/`. Read only.
- **All output goes to `Data/Vaults/z2k-default-vault/` only.**
- **Locked documents (SoW, PRD, IP, TP) are READ-ONLY.** Do not modify them even if something appears inconsistent. Stop and report conflicts to the user.
- **Read REF-A before any template work.** The AI reference manual is always the first reference for plugin usage.
- **Preserve unconvertible Templater code verbatim.** Wrap with `{{! FLAGGED: <explanation of what the code does and why it was not converted> }}`. Do not guess at Templater behavior.

---

## Naming Conventions

| Artifact | Convention | Example |
|---|---|---|
| Document templates | `<Name>.md` — no `Template -` prefix | `Beliefs (General).md` |
| Block templates | `<Name>.md` — no `Block -` prefix | `Card Fabric.md` |
| System blocks | `.system-block.md` (dot-prefixed) | `.system-block.md` |
| Domain defaults | `<DomainName> (General).md` | `Memories (General).md` |

All templates live in the `Templates/` subfolder of their domain (or `Templates/` at vault root for cross-domain artifacts). System blocks go directly in their domain root.

---

## v3 Metadata Required on All Templates

### Document templates (every field below is required)
```yaml
z2k_template_type: document-template
z2k_template_version: "v3.0.0 2026-03-02"
z2k_template_suggested_title: <expression>
```
Personal templates additionally include:
```yaml
z2k_template_author: "Geoff (z2k-gwp)"
```

### Block templates
```yaml
z2k_template_type: block-template
```

### System blocks
No template metadata — system-blocks contain domain identity fields and domain-specific card metadata only.

---

## Template Conversion Approach (Phase 6 tasks)

Apply this sequence to each v2 template:

1. Read source from `/Users/gp/Vaults/Z2K (Sync) - Snapshot 2026-02-28/~Templates/<filename>`
2. Apply API Translation table (see Requirements §3)
3. Add v3 YAML metadata (see above)
4. Add `{{fieldInfo}}` declarations for all user-prompted fields
5. Convert `%% ... %%` comments → `{{! ... }}`
6. Convert `G:` / `Geoff:` prefixes → `[!me]` callout with `Me:` label
7. Replace Card Fabric section with opt-in comment: `{{! To include Card Fabric: {{> "Card Fabric"}} }}`
8. Templater code (`<% ... %>`): replace only when a clear v3 equivalent exists. If not, preserve verbatim and wrap with `{{! FLAGGED: <explanation> }}`
9. Write to target path in `Data/Vaults/z2k-default-vault/`

---

## Reference Docs Index

Read these on demand as directed by the task file. Do not read all of them upfront.

| Ref ID | Path | Relevant For |
|---|---|---|
| REF-A | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Appendix/Reference Manual for AI.md` | **All tasks involving templates** |
| REF-B | `Docs/z2k-system-docs/4 - Z2K Reference Docs/4b - Data Formats/Z2K Card Metadata - YAML.md` | Task 03 |
| REF-C | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/System Blocks/Intro to System Blocks.md` | Tasks 03–06 |
| REF-D | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/System Blocks/Using System Blocks and fieldInfo.md` | Tasks 03–06 |
| REF-E | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/System Blocks/System Block Stops.md` | Tasks 06, 18 |
| REF-F | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Built-In Helper Functions/Formatting Functions/formatStringBulletize.md` | Task 07 (Card Fabric) |
| REF-G | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Z2K Templates and YAML/Storing Field Values in YAML.md` | Tasks 07–22 |
| REF-H | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Z2K Templates and YAML/YAML Configuration Properties/z2k_template_suggested_title.md` | Tasks 10–22 |
| REF-I | `Docs/z2k-design-notes/Z2K System - Design Notes/Z2K Data Architecture/Z2K Metadata/Z2K Metadata Specification - Version 3.0.md` | Task 12 (source types) |
| REF-J | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Built-In Helper Functions/Formatting Functions/formatString.md` | Task 12 (as needed) |
| REF-K | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/Template Folders/Template Organization.md` | Task 02 |
| REF-L | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/URI, JSON, Command Queues/Command Queues/Command Queues Overview.md` | Task 01 |
| REF-M | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/URI, JSON, Command Queues/JSON Packages/JSON Packages Overview.md` | Task 01 |
| REF-N | `Code/Obsidian Plugins/z2k-plugin-templates/docs/reference-manual/URI, JSON, Command Queues/URI Actions/URI Actions.md` | Task 01 |

---

## Testing Discipline (Required on Every Task)

Apply this sequence after writing each artifact, before marking the task Done.

### Step 1 — Add assertions to the appropriate script

| Artifact type | Script |
|---|---|
| Folder/file existence, YAML field presence | `Testing/scripts/test-structure.py` |
| Block template instantiation | `Testing/scripts/test-blocks.py` |
| Document template instantiation | `Testing/scripts/test-templates.py` |

All scripts live in the project's `Testing/scripts/` subfolder. Task 01 creates them as runnable skeletons. Every subsequent task adds assertions to the relevant script — never creates a new one.

Assertions are **additive and permanent.** Do not remove assertions from a prior task. The script always represents the full history of what must be true.

### Step 2 — Run the full script

Run the **entire** script, not just new assertions. All prior assertions must still pass. A regression in a prior task's assertions means something was broken — stop and resolve before proceeding.

```bash
python3 Testing/scripts/test-structure.py
```

### Step 3 — Category B tests (template instantiation)

1. Write the JSON command file to `Testing/commands/<phase>/<test-name>.json`
2. Flag to user: "Please trigger 'Process Command Queue Now' in Obsidian"
3. After user confirms output: run the test script to poll and assert
4. First passing run: confirm golden file saved to `Testing/expected/<test-name>/expected.md`
5. Subsequent runs: script auto-diffs — no user judgment required

### Script ownership

Task 01 is responsible for creating all skeleton scripts and the `lib/` infrastructure. Tasks 02–24 only add assertions. If a script does not exist when you go to add assertions, stop — Task 01 is incomplete.

---

## Logging Plugin Issues

If you discover a bug or limitation in the Z2K Templates Plugin:
- Create a file in `Issues/Z2K Templates Plugin/` in the project folder
- One file per issue; short descriptive name
- Include: task ID that uncovered it, symptom, reproduction steps, impact on this task

---

## Updating Task Status

When you begin a task: set `status: "In Progress"` in the task file frontmatter.
When you complete a task: set `status: "Done"` in the task file frontmatter.
If blocked: set `status: "Blocked"` and document the blocker in the task file under a `## Blockers` section.

Also update the master tracker: `Z2K Template Library v3 Migration - Task List and Progress Tracker.md` in the project folder.
