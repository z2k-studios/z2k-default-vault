---
feature_number: "020"
feature_name: "Global Template Quality"
date_run: "2026-03-03 12:43:48"
result: PASS
passed: 13
failed: 0
skipped: 0
requirements:
  - id: 020-001
    description: "Valid Handlebars syntax"
    result: PASS
    tier: quantitative
  - id: 020-002
    description: "No v2 Templater syntax"
    result: PASS
    tier: quantitative
  - id: 020-003
    description: "Document templates have required YAML metadata"
    result: PASS
    tier: quantitative
  - id: 020-004
    description: "Block templates have required YAML metadata"
    result: PASS
    tier: quantitative
  - id: 020-005
    description: "Template author field correct"
    result: PASS
    tier: quantitative
  - id: 020-006
    description: "Field naming conventions followed (PascalCase)"
    result: PASS
    tier: quantitative
  - id: 020-007
    description: "Comment syntax correct (double-dash for mustache content)"
    result: PASS
    tier: quantitative
  - id: 020-008
    description: "No trailing spaces on comment-only lines"
    result: PASS
    tier: quantitative
  - id: 020-009
    description: "All fieldInfo declarations are well-formed"
    result: PASS
    tier: quantitative
  - id: 020-010
    description: "Block partial references point to existing files"
    result: PASS
    tier: quantitative
  - id: 020-011
    description: "Source type values are canonical"
    result: PASS
    tier: quantitative
  - id: 020-012
    description: "No duplicate template filenames within same Templates/ folder"
    result: PASS
    tier: quantitative
  - id: 020-013
    description: "No personal templates in the CTL vault"
    result: PASS
    tier: quantitative
---
# Feature 020 — Global Template Quality — Last Run Results
**Date:** 2026-03-03 12:43:48
**Overall Result:** PASS

## Requirements

| Req ID | Description | Result | Tier |
|--------|-------------|--------|------|
| 020-001 | Valid Handlebars syntax | PASS | quantitative |
| 020-002 | No v2 Templater syntax | PASS | quantitative |
| 020-003 | Document templates have required YAML metadata | PASS | quantitative |
| 020-004 | Block templates have required YAML metadata | PASS | quantitative |
| 020-005 | Template author field correct | PASS | quantitative |
| 020-006 | Field naming conventions followed (PascalCase) | PASS | quantitative |
| 020-007 | Comment syntax correct (double-dash for mustache content) | PASS | quantitative |
| 020-008 | No trailing spaces on comment-only lines | PASS | quantitative |
| 020-009 | All fieldInfo declarations are well-formed | PASS | quantitative |
| 020-010 | Block partial references point to existing files | PASS | quantitative |
| 020-011 | Source type values are canonical | PASS | quantitative |
| 020-012 | No duplicate template filenames within same Templates/ folder | PASS | quantitative |
| 020-013 | No personal templates in the CTL vault | PASS | quantitative |
