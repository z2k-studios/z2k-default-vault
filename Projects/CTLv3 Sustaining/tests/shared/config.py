"""
CTLv3 Sustaining — Shared Test Configuration

All paths are derived from this file's location. Do not use hardcoded absolute paths
in test scripts; always import from here.

Vault-specific settings (e.g., NOTE_OUTPUT_DIR for Feature 002 templatePath tests)
may need adjustment based on vault configuration.
"""

from pathlib import Path

# ---------------------------------------------------------------------------
# Derived paths
# ---------------------------------------------------------------------------

SHARED_DIR = Path(__file__).resolve().parent          # tests/shared/
TESTS_DIR = SHARED_DIR.parent                         # tests/
PROJECT_DIR = TESTS_DIR.parent                        # CTLv3 Sustaining/
VAULT_ROOT = PROJECT_DIR.parent.parent.parent         # z2k-default-vault/

PLUGIN_DIR = VAULT_ROOT / ".obsidian" / "plugins" / "z2k-plugin-templates"
COMMAND_QUEUE_DIR = PLUGIN_DIR / "command-queue"
ERROR_LOG_PATH = PLUGIN_DIR / "error-log.md"

# ---------------------------------------------------------------------------
# Output locations
#
# templateContents packets (no template file) output to VAULT_ROOT by default.
# templatePath packets output to the template's configured card type folder.
# Set TEMPLATE_PATH_OUTPUT_DIR to that folder if it differs from VAULT_ROOT.
# ---------------------------------------------------------------------------

# Default output dir for templateContents tests (inline template, no templatePath)
INLINE_TEMPLATE_OUTPUT_DIR = VAULT_ROOT

# ---------------------------------------------------------------------------
# Timing
# ---------------------------------------------------------------------------

# How long to wait for the Command Queue to process a packet (seconds).
# Default queue scan interval is 60s; allow generous headroom.
COMMAND_QUEUE_TIMEOUT_SECONDS = 90

# How often to poll for the output file or done/ entry (seconds).
POLL_INTERVAL_SECONDS = 2

# ---------------------------------------------------------------------------
# Quality thresholds
# ---------------------------------------------------------------------------

# Global qualitative passing threshold (percentage, 0–100).
# Must match Testing Plan §3.2.3.
QUALITY_THRESHOLD_PERCENT = 70

# ---------------------------------------------------------------------------
# Error log monitoring
# ---------------------------------------------------------------------------

# Log levels considered failures during test execution.
# At Warning level, the plugin logs: errors, missing fields, fallback values,
# deprecated usage. Debug is excluded — too verbose for regression runs.
ERROR_LOG_FAIL_LEVELS = {"None", "Error", "Warning"}
