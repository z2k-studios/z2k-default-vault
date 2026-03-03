---
document_type: Task List and Progress Tracker
status: Active
---
# Task List and Progress Tracker — Z2K Template Library v3 Migration

> All task files are in `tasks/` subfolder. Statuses: `Pending` / `In Progress` / `Blocked` / `Done`.
>
> **Parallelizable** = can be executed concurrently with other tasks in the same group, provided their shared dependencies are met.

---

## Phase 0 — Testing Infrastructure

| Task | Name | IP Tasks | Status | Parallelizable | Depends On | Blocks |
|---|---|---|---|---|---|---|
| Task 01 | Testing Infrastructure | TP-0.1–0.4 | Done | With Task 02 | — | Phase 6 execution gate |

---

## Phase 1 — Vault Structure

| Task | Name | IP Tasks | Status | Parallelizable | Depends On | Blocks |
|---|---|---|---|---|---|---|
| Task 02 | Vault Structure | 1.1–1.6 | Done | No (must be first) | — | Tasks 03–24 |

---

## Phase 2 — Root System Block

| Task | Name | IP Tasks | Status | Parallelizable | Depends On | Blocks |
|---|---|---|---|---|---|---|
| Task 03 | Root System Block | 2.1 | Done | With Tasks 04–09 | Task 02 | All Phase 6 tasks |

---

## Phase 3 — Domain System Blocks

| Task | Name | IP Tasks | Status | Parallelizable | Depends On | Blocks |
|---|---|---|---|---|---|---|
| Task 04 | Domain System Blocks: Core Domains | 3.1–3.10, 3.12 | Done | With Tasks 03, 05–09 | Task 02 | Tasks 10–22 |
| Task 05 | Domain System Block: AI Domain | 3.11 | Done | With Tasks 03, 04, 06–09 | Task 02 | None (no Phase 6 AI templates) |
| Task 06 | Domain System Block: Projects | 3.13 | Done | With Tasks 03, 04, 05, 07–09 | Task 02 | Task 18 |

> **Task 05** AI-PERSP resolved: `z2k_creation_perspective: "AI"` chosen.
> **Task 06** DSB-005 resolved: per-project-subfolder `.system-block-stop` strategy. `My Writings/.system-block-stop` created.

---

## Phase 4 — Root Block Templates

| Task | Name | IP Tasks | Status | Parallelizable | Depends On | Blocks |
|---|---|---|---|---|---|---|
| Task 07 | Root Block Templates | 4.1–4.5 | Done | With Tasks 03–06, 08–09 | Task 02 | Tasks 10–22 |

> **Dot-notation test gate (BLK-001/004/005):** Task 07 includes a test of `Content.Author` dot-notation. Result affects field naming across all Phase 5 and 6 tasks. Complete Task 07 before committing to field names in Tasks 08–22.

---

## Phase 5 — Domain Block Templates

| Task | Name | IP Tasks | Status | Parallelizable | Depends On | Blocks |
|---|---|---|---|---|---|---|
| Task 08 | Information Domain Blocks | 5.1–5.5 | Done | With Tasks 03–07, 09 | Task 02 | Task 12 |
| Task 09 | Other Domain Blocks | 5.6–5.8 | Done | With Tasks 03–08 | Task 02 | Tasks 13, 14, 19 |

---

## Phase 6 — Document Templates

> All Phase 6 tasks depend on Tasks 02, 03, 04, 07 (minimum). Additional dependencies noted per task.

| Task | Name | IP Tasks | Status | Parallelizable | Additional Deps | Templates |
|---|---|---|---|---|---|---|
| Task 10 | Thoughts Templates | 6.1 | Done | With Tasks 11, 15–17, 20–22 | — | 7 |
| Task 11 | Beliefs Templates | 6.2 | Done | With Tasks 10, 15–17, 20–22 | — | 1 |
| Task 12 | Information Templates | 6.3 | Done | With Tasks 13–14, 18–22 after Task 08 | Task 08 | 21 |
| Task 13 | Interactions Templates | 6.4 | Done | With Tasks 12, 14, 18–22 after Task 09 | Task 09 | 12 |
| Task 14 | Memories Templates | 6.5 | Done | With Tasks 12–13, 18–22 after Task 09 | Task 09 | 5 |
| Task 15 | Locations Templates | 6.6 | Done | With Tasks 10–11, 16–17, 20–22 | — | 1 |
| Task 16 | Journals Templates | 6.7 | Done | With Tasks 10–11, 15, 17, 20–22 | — | 2 |
| Task 17 | Logs Templates | 6.8 | Done | With Tasks 10–11, 15–16, 20–22 | — | 6 |
| Task 18 | Projects Templates | 6.9 | Done | With Tasks 12–17, 19–22 after Task 06 | Task 06 | 7 |
| Task 19 | Body Templates | 6.10 | Done | With Tasks 12–18, 20–22 after Task 09 | Task 09 | 1 |
| Task 20 | System Templates | 6.11 | Done | With Tasks 10–11, 15–17, 21–22 | — | 1 |
| Task 21 | Entities Templates | 6.12 | Done | With Tasks 10–11, 15–17, 20, 22 | — | 1 |
| Task 22 | Root Cross-Domain Templates | 6.14 | Done | With Tasks 10–11, 15–17, 20–21 | — | 2 |

> Task 6.13 (AI domain templates): **No action** — AI domain receives system-block only. No task file created.

---

## Phase 7 — Supporting Documentation

| Task | Name | IP Tasks | Status | Parallelizable | Depends On |
|---|---|---|---|---|---|
| Task 23 | Supporting Documentation | 7.1–7.3 | Done | No (7.1 based on migration observations) | All Phase 6 tasks |

---

## Phase 8 — Cleanup and Archival

| Task | Name | IP Tasks | Status | Parallelizable | Depends On |
|---|---|---|---|---|---|
| Task 24 | Cleanup and Archival | 8.1–8.8 | Done | No | Task 23 |

---

## Summary

| Metric | Value |
|---|---|
| Total tasks | 24 |
| Tasks Done | 24 (Tasks 01–24) |
| Tasks Pending | 0 |
| Open issues resolved | AI-PERSP (Task 05), DSB-005 (Task 06), LOC-001 (Task 15), PROJ-YAML (Task 18), ST-001 (Task 12) |
| Test suite | 74 passed, 0 failed (Category A — structure and existence) |
| Plugin issues | 1 (BLK-001 — dot-notation unsupported; workaround in place) |
| Project status | **Complete** — 2026-03-02 |
