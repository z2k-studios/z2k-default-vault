---
feature_number: "142"
description: "Family Vacation Trip document template for capturing family vacation memories"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/142 - Family Vacation Trip/"
---

# Feature 142 — Family Vacation Trip

## Description
The Family Vacation Trip template is a document template in the Memories domain for capturing memories from family vacation trips. It provides structured fields for recording the destination, dates, participants, highlights, and memorable moments from family travel experiences.

## Requirements
### 142-001 — Template file exists `[quantitative]`
Template file exists at `Memories/Templates/Family Vacation Trip.md`.

### 142-002 — All fields have fieldInfo declarations `[quantitative]`
Every user-prompted field in the template has a corresponding `{{fieldInfo}}` declaration.

### 142-003 — Renders correctly via Command Queue `[quantitative]`
Template renders without error when invoked via Command Queue JSON packet with standard test data. Output matches expected golden file after dynamic field normalization.

### 142-004 — Quality meets scorecard threshold `[qualitative]`
AI quality scorecard assessment meets or exceeds the 70% passing threshold.
