---
date_generated: "2026-03-03 13:04:42"
document_type: Test Result Summary
---

# Test Result Summary — 2026-03-03 01:04 PM

**Features:** 6 total — 3 passed, 2 failed, 0 no results

| Feature | Name                    | Date Run         | Result     | Score         |
|---------|-------------------------|------------------|------------|---------------|
| 001     | [Infrastructure Test](<../001 - Infrastructure Test/last-run-results.md>)     | 2026-03-03 12:43 | PASS       | 7P / 0F / 0S  |
| 002     | [Working System](<../002 - Working System/last-run-results.md>)          | 2026-03-03 12:43 | ==FAILED== | 4P / 2F / 0S  |
| 003     | [Directory Structure](<../003 - Directory Structure/last-run-results.md>)     | 2026-03-03 12:43 | PASS       | 6P / 0F / 0S  |
| 004     | [System Blocks](<../004 - System Blocks/last-run-results.md>)           | 2026-03-03 12:43 | ==FAILED== | 8P / 5F / 0S  |
| 020     | [Global Template Quality](<../020 - Global Template Quality/last-run-results.md>) | 2026-03-03 12:43 | PASS       | 13P / 0F / 0S |
| 900     | [Template Quality Gate](<../900 - Template Quality Gate/last-run-results.md>)   | 2026-03-03 12:43 | SKIP       | 0P / 0F / 3S  |

## Failed Features

- **[002 — Working System](<../002 - Working System/last-run-results.md>)**: 2 requirement(s) failed
  - 002-002 — Root system block YAML injected
  - 002-006 — Output matches expected golden file
- **[004 — System Blocks](<../004 - System Blocks/last-run-results.md>)**: 5 requirement(s) failed
  - 004-001 — Root system block exists
  - 004-002 — Root system block has YAML delimiters
  - 004-003 — Root system block required fields present
  - 004-004 — Root system block deprecated fields absent
  - 004-005 — Root system block has me fieldInfo
