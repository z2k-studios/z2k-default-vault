---
document_type: Post-Project Requirements Index
status: Active
---
# CTLv3 Project — Requirements Index

Items collected during the CTLv3 migration project to be included in the **CTLv3 Project** — the successor ongoing project for iteratively building out the Z2K Core Template Library v3.

> **About the CTLv3 Project:** A new ongoing project (with its own SoW, PRD, IP, TP) for adding new templates and capabilities to CTLv3. Its first run validates that the existing CTLv3 library passes all tests. Input comes from new template requests and discussion, not CTLv2. Only begins after the current migration project is fully validated.

> **Archived Q&A Reference:** For background and decision context on any item sourced from the migration project, consult the archived Q&A documents in `User Feedback Documentation/Archived/` within the CTLv3 migration project folder.

---

## Requirements / Items

| # | Item | Source | Notes |
|---|---|---|---|
| CTLP-001 | Full Entities CRM template set (Person, Organization, Named Entity) | OOS-001 | Start with ~Generic Contact built in this project; expand to full CRM |
| CTLP-002 | AI domain content templates | OOS-002 | AI domain gets system-block only in v3 migration; templates deferred here |
| CTLP-003 | `{{me}}` built-in field integration (once Core Plugin supports it) | OOS-004 | Currently hard-coded literal `[!me]`; update templates when feature ships |
| CTLP-004 | "Default Template" feature integration (once plugin supports GH #182) | OOS-005 | Rename `My Writings (Default).md` to `Template - ~Generic.md` when feature ships |
| CTLP-005 | Health Log sub-block decomposition | OOS-006 | Decompose `Block - Health Log` into individual composable sub-blocks |
| CTLP-006 | Generic (non-Flame) Daily Log template | OOS-007 | Create a public-friendly Daily Log not dependent on Google Forms/Flame automation |
| CTLP-007 | Option 4 podcast template (conditional multi-select per host) | OOS-010 | Interesting future enhancement over Option 3 chosen for v3 |
| CTLP-008 | `[!me]` vs `[!Geoff]` callout-type design resolution | PRD §17 (Mig Q5) | v3 uses `[!me]` as portable standard; long-term open question whether identity-expressive `[!Geoff]` is preferred; resolve before CTLv3 is published |
