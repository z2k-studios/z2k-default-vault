---
feature_number: "051"
description: "AI domain — system block only with z2k_creation_perspective AI; no content templates (deferred CTLP-002)"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/051 - AI Domain/"
---

# Feature 051 — AI Domain

## Description
The AI domain captures AI-generated and AI-related content. It has NO content templates — the domain currently consists of a system block and an empty `Templates/` folder only, located at `AI/Templates/`. The system block includes domain identity plus `z2k_creation_perspective: "AI"`. Content templates are deferred to a future effort (CTLP-002). This feature validates the system block configuration and the existence of the empty Templates/ folder.

## Requirements
### 051-001 — Domain folder structure exists `[quantitative]`
The `AI/` domain folder exists with a `Templates/` subfolder.

### 051-002 — System block exists with domain identity and creation perspective `[quantitative]`
The AI domain system block exists and includes domain identity fields plus `z2k_creation_perspective: "AI"`.

### 051-003 — Templates/ folder exists and is empty of content templates `[quantitative]`
The `AI/Templates/` folder exists but contains no document or block content templates. The system block file may be present but no user-facing templates should exist.

### 051-004 — Creation perspective field is set to AI `[quantitative]`
The system block includes `z2k_creation_perspective` set to the value `"AI"`, distinguishing this domain from all others.

### 051-005 — Domain structure conforms to AI domain conventions `[qualitative]`
The domain folder structure and system block follow consistent patterns appropriate for the AI domain, even in the absence of content templates.
