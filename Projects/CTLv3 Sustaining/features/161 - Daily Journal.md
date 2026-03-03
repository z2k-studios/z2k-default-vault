---
feature_number: "161"
description: "Daily Journal document template with absorbed Ideas domain sections"
status: "Describing"
date_added: "2026-03-02"
test_folder: "tests/161 - Daily Journal/"
---

# Feature 161 — Daily Journal

## Description
The Daily Journal template is the primary daily writing template in the Journals domain. It absorbs the retired Ideas domain by including dedicated sections for passing thoughts, memories, and information capture.

## Requirements
### 161-001 — Template file exists `[quantitative]`
The file `Journals/Templates/Daily Journal.md` must exist in the vault.

### 161-002 — All fields have fieldInfo declarations `[quantitative]`
Every field referenced in the template body must have a corresponding `fieldInfo` declaration in the frontmatter.

### 161-003 — Renders correctly via Command Queue `[quantitative]`
The template must render without errors when processed through the Command Queue.

### 161-004 — Quality meets scorecard threshold `[qualitative]`
The rendered output must meet the established quality scorecard threshold for document templates.

### 161-005 — Absorbed Ideas domain sections exist `[quantitative]`
The rendered output must contain `## Passing Thoughts`, `## Passing Memories`, and `## Passing Information` sections, representing the absorbed retired Ideas domain.
