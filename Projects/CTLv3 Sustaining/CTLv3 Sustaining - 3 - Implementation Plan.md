---
Description: Implementation Plan for the CTLv3 Sustaining project — describes the drop folder mechanism, how new features enter the system, and the handoff to external implementation.
document_type: Implementation Plan
status: Draft
---

# Implementation Plan - CTLv3 Sustaining


## Overview

In a sustaining project, **feature implementation is external to the project workflow**. This project's scope covers feature description, requirements definition, test creation, and acceptance validation — not the implementation of the template engine or plugin features themselves.

Implementation is handled through other workflows (e.g., `/wf code/plan`, `/wf code/implement`) or manual development as appropriate for the template system.

This document describes how new features enter the sustaining project system and the handoff points between this project and external implementation.

---

## The Drop Folder

The `drop/` folder is the single entry point for new features. To initiate the per-feature implementation cycle:

1. Place a file in `drop/` containing a description of the feature to be validated. The file can be as simple as a few sentences or as detailed as a full specification — the per-feature cycle will flesh it out during Stage 1.
2. Issue `/wf project/implement` to begin processing the dropped feature.
3. The implement workflow will consult this project's Statement of Work for the per-feature implementation cycle and execute it.


### What Goes in a Drop File

- A description of the template feature or capability to be validated
- Any known requirements or expected behaviors
- Context about how the feature is used in templates
- Known error states or edge cases (if available)

The file format is free-form Markdown. No specific structure is required — the Describe & Flesh Out stage will impose structure.

---

## Handoff to External Implementation

During Stage 4 (Implement) of the per-feature cycle, the project hands off to external implementation. At this point, the sustaining project has produced:

- **Feature file** (`features/NNN - <Feature Name>.md`) — the specification
- **Test plan** (`tests/NNN - <Feature Name>/test_plan.md`) — the acceptance criteria
- **Test scripts** (`tests/NNN - <Feature Name>/run_tests.py`) — the automated validation

The implementer should:

1. Read the feature file for the specification
2. Read the test plan for acceptance criteria
3. Implement the feature using appropriate tools and workflows
4. Return to this project for acceptance testing (Stage 5)


### When Implementation Is Already Done

Many CTLv3 features are already implemented. When the sustaining project is retroactively adding test coverage for an existing feature, Stage 4 may be skipped entirely. Proceed directly to Stage 5 (Acceptance Testing).

---

## Implementation Open Issues

| ID | Description | Status | Resolution |
|---|---|---|---|
| — | — | — | — |
