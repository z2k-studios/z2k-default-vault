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
| Task 01 | Testing Infrastructure | TP-0.1–0.4 | Pending | With Task 02 | — | Phase 6 execution gate |

---

## Phase 1 — Vault Structure

| Task | Name | IP Tasks | Status | Parallelizable | Depends On | Blocks |
|---|---|---|---|---|---|---|
| Task 02 | Vault Structure | 1.1–1.6 | Pending | No (must be first) | — | Tasks 03–24 |

---

## Phase 2 — Root System Block

| Task | Name | IP Tasks | Status | Parallelizable | Depends On | Blocks |
|---|---|---|---|---|---|---|
| Task 03 | Root System Block | 2.1 | Pending | With Tasks 04–09 | Task 02 | All Phase 6 tasks |

---

## Phase 3 — Domain System Blocks

| Task | Name | IP Tasks | Status | Parallelizable | Depends On | Blocks |
|---|---|---|---|---|---|---|
| Task 04 | Domain System Blocks: Core Domains | 3.1–3.10, 3.12 | Pending | With Tasks 03, 05–09 | Task 02 | Tasks 10–22 |
| Task 05 | Domain System Block: AI Domain | 3.11 | Pending | With Tasks 03, 04, 06–09 | Task 02 | None (no Phase 6 AI templates) |
| Task 06 | Domain System Block: Projects | 3.13 | Pending | With Tasks 03, 04, 05, 07–09 | Task 02 | Task 18 |

> **Task 05** has open issue AI-PERSP (design AI authorship field). May require design decision before executing.
> **Task 06** has open issue DSB-005. Read REF-E (System Block Stops) before executing.

---

## Phase 4 — Root Block Templates

| Task | Name | IP Tasks | Status | Parallelizable | Depends On | Blocks |
|---|---|---|---|---|---|---|
| Task 07 | Root Block Templates | 4.1–4.5 | Pending | With Tasks 03–06, 08–09 | Task 02 | Tasks 10–22 |

> **Dot-notation test gate (BLK-001/004/005):** Task 07 includes a test of `Content.Author` dot-notation. Result affects field naming across all Phase 5 and 6 tasks. Complete Task 07 before committing to field names in Tasks 08–22.

---

## Phase 5 — Domain Block Templates

| Task | Name | IP Tasks | Status | Parallelizable | Depends On | Blocks |
|---|---|---|---|---|---|---|
| Task 08 | Information Domain Blocks | 5.1–5.5 | Pending | With Tasks 03–07, 09 | Task 02 | Task 12 |
| Task 09 | Other Domain Blocks | 5.6–5.8 | Pending | With Tasks 03–08 | Task 02 | Tasks 13, 14, 19 |

---

## Phase 6 — Document Templates

> All Phase 6 tasks depend on Tasks 02, 03, 04, 07 (minimum). Additional dependencies noted per task.

| Task | Name | IP Tasks | Status | Parallelizable | Additional Deps | Templates |
|---|---|---|---|---|---|---|
| Task 10 | Thoughts Templates | 6.1 | Pending | With Tasks 11, 15–17, 20–22 | — | 7 |
| Task 11 | Beliefs Templates | 6.2 | Pending | With Tasks 10, 15–17, 20–22 | — | 1 |
| Task 12 | Information Templates | 6.3 | Pending | With Tasks 13–14, 18–22 after Task 08 | Task 08 | 21 |
| Task 13 | Interactions Templates | 6.4 | Pending | With Tasks 12, 14, 18–22 after Task 09 | Task 09 | 12 |
| Task 14 | Memories Templates | 6.5 | Pending | With Tasks 12–13, 18–22 after Task 09 | Task 09 | 5 |
| Task 15 | Locations Templates | 6.6 | Pending | With Tasks 10–11, 16–17, 20–22 | — | 1–2 |
| Task 16 | Journals Templates | 6.7 | Pending | With Tasks 10–11, 15, 17, 20–22 | — | 2 |
| Task 17 | Logs Templates | 6.8 | Pending | With Tasks 10–11, 15–16, 20–22 | — | 6 |
| Task 18 | Projects Templates | 6.9 | Pending | With Tasks 12–17, 19–22 after Task 06 | Task 06 | 7 |
| Task 19 | Body Templates | 6.10 | Pending | With Tasks 12–18, 20–22 after Task 09 | Task 09 | 1 |
| Task 20 | System Templates | 6.11 | Pending | With Tasks 10–11, 15–17, 21–22 | — | 1 |
| Task 21 | Entities Templates | 6.12 | Pending | With Tasks 10–11, 15–17, 20, 22 | — | 1 |
| Task 22 | Root Cross-Domain Templates | 6.14 | Pending | With Tasks 10–11, 15–17, 20–21 | — | 2+ |

> Task 6.13 (AI domain templates): **No action** — AI domain receives system-block only. No task file created.

---

## Phase 7 — Supporting Documentation

| Task | Name | IP Tasks | Status | Parallelizable | Depends On |
|---|---|---|---|---|---|
| Task 23 | Supporting Documentation | 7.1–7.3 | Pending | No (7.1 based on migration observations) | All Phase 6 tasks |

---

## Phase 8 — Cleanup and Archival

| Task | Name | IP Tasks | Status | Parallelizable | Depends On |
|---|---|---|---|---|---|
| Task 24 | Cleanup and Archival | 8.1–8.8 | Pending | No | Task 23 |

---

## Summary

| Metric | Value |
|---|---|
| Total tasks | 24 |
| Tasks with open issues (blocking) | Task 05 (AI-PERSP), Task 06 (DSB-005) |
| Critical path bottleneck | Task 02 (Vault Structure) → Tasks 03–09 → Phase 6 |
| Largest single task | Task 12 (Information Templates — 21 templates) |
| Dot-notation test gate | Task 07 (must complete before finalizing field names in Tasks 08–22) |
| User-assist required | Task 01 (opening testing vault in Obsidian), all Phase 6 Category B tests |
