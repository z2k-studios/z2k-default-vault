from __future__ import annotations

"""
CTLv3 Sustaining — Shared Test Utilities

Provides:
  - Command Queue packet submission and polling
  - Output file reading and diff comparison
  - Rendered note cleanup
  - Error log position recording and new-entry detection
"""

import re
import shutil
import sys
import time
import uuid
from pathlib import Path

from config import (
    COMMAND_QUEUE_DIR,
    COMMAND_QUEUE_TIMEOUT_SECONDS,
    ERROR_LOG_FAIL_LEVELS,
    ERROR_LOG_PATH,
    POLL_INTERVAL_SECONDS,
)


# ---------------------------------------------------------------------------
# Command Queue
# ---------------------------------------------------------------------------

def submit_packet(packet_path: Path) -> Path:
    """
    Copy a JSON packet into the Command Queue watched directory.

    Returns the path of the queued file (used to detect when it moves to done/).
    A unique suffix is added to the filename to avoid collisions between test runs.
    """
    if not COMMAND_QUEUE_DIR.exists():
        raise RuntimeError(
            f"Command Queue directory does not exist: {COMMAND_QUEUE_DIR}\n"
            "Ensure the Z2K Templates plugin is installed and Command Queues are enabled."
        )

    unique_name = f"{packet_path.stem}_{uuid.uuid4().hex[:8]}{packet_path.suffix}"
    dest = COMMAND_QUEUE_DIR / unique_name
    shutil.copy2(packet_path, dest)
    return dest


def wait_for_output(output_path: Path, timeout: int = COMMAND_QUEUE_TIMEOUT_SECONDS) -> bool:
    """
    Poll for an output file to appear at output_path.

    Returns True if found within timeout, False otherwise.
    """
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if output_path.exists():
            return True
        time.sleep(POLL_INTERVAL_SECONDS)
    return False


def wait_for_queue_done(queued_file: Path, timeout: int = COMMAND_QUEUE_TIMEOUT_SECONDS) -> bool:
    """
    Poll for a queued packet to appear in the done/ subfolder.

    The plugin renames the file with a timestamp before moving it, so we
    search for any done/ entry whose stem starts with the original stem prefix.
    Returns True if found, False on timeout.
    """
    done_dir = COMMAND_QUEUE_DIR / "done"
    stem_prefix = queued_file.stem
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if done_dir.exists():
            matches = list(done_dir.glob(f"{stem_prefix}*"))
            if matches:
                return True
        time.sleep(POLL_INTERVAL_SECONDS)
    return False


def read_output(output_path: Path) -> str:
    """Read and return the content of a rendered output file."""
    return output_path.read_text(encoding="utf-8")


def diff_output(actual: str, expected_path: Path) -> list[str]:
    """
    Compare actual rendered output to the expected golden file.

    Returns a list of diff lines (empty if identical). Does not normalize
    dynamic fields — callers are responsible for normalization before passing
    actual content if needed.
    """
    import difflib
    expected = expected_path.read_text(encoding="utf-8")
    actual_lines = actual.splitlines(keepends=True)
    expected_lines = expected.splitlines(keepends=True)
    diff = list(difflib.unified_diff(
        expected_lines,
        actual_lines,
        fromfile=f"expected/{expected_path.name}",
        tofile="actual",
    ))
    return diff


def normalize_dynamic_fields(content: str) -> str:
    """
    Replace known dynamic field values with stable placeholders for diff comparison.

    Covers:
      - z2k_creation_date YAML field (wikilink date)
      - z2k_creation_timestamp YAML field (compact YYYYMMDDHHMMSS format)
      - z2k_creation_creator YAML field (wikilink to creator name)
      - Remaining inline [[YYYY-MM-DD]] wikilinks
      - ISO 8601 timestamps
    """
    # YAML field: z2k_creation_date: "[[YYYY-MM-DD]]"
    content = re.sub(
        r'(z2k_creation_date:\s+)"[^"]*"',
        r'\1"[[DATE_PLACEHOLDER]]"',
        content,
    )
    # YAML field: z2k_creation_timestamp: "YYYYMMDDHHMMSS" (compact, 14 digits)
    content = re.sub(
        r'(z2k_creation_timestamp:\s+)"[^"]*"',
        r'\1"TIMESTAMP_PLACEHOLDER"',
        content,
    )
    # YAML field: z2k_creation_creator: "[[Name]]"
    content = re.sub(
        r'(z2k_creation_creator:\s+)"[^"]*"',
        r'\1"[[CREATOR_PLACEHOLDER]]"',
        content,
    )
    # Remaining inline [[YYYY-MM-DD]] wikilinks
    content = re.sub(r'\[\[\d{4}-\d{2}-\d{2}\]\]', '[[DATE_PLACEHOLDER]]', content)
    # ISO 8601 timestamps: 2026-03-02T10:30:00 etc.
    content = re.sub(
        r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})?',
        'TIMESTAMP_PLACEHOLDER',
        content,
    )
    return content


def cleanup_output(output_path: Path) -> None:
    """Delete a rendered output file. Silently ignores missing files."""
    try:
        output_path.unlink()
    except FileNotFoundError:
        pass


# ---------------------------------------------------------------------------
# Error log monitoring
# ---------------------------------------------------------------------------

def get_error_log_position() -> int:
    """
    Return the current byte offset (size) of the error log file.
    Returns 0 if the file does not exist yet.
    """
    if not ERROR_LOG_PATH.exists():
        return 0
    return ERROR_LOG_PATH.stat().st_size


def get_new_error_log_entries(position: int) -> list[str]:
    """
    Read new content from the error log since `position` bytes.

    Returns a list of entry strings (each entry is the block of text between
    `## [LEVEL] timestamp` and the next `---` separator). Only entries at
    levels listed in ERROR_LOG_FAIL_LEVELS are returned.

    Returns an empty list if no relevant new entries exist.
    """
    if not ERROR_LOG_PATH.exists():
        return []

    current_size = ERROR_LOG_PATH.stat().st_size
    if current_size <= position:
        return []

    with ERROR_LOG_PATH.open(encoding="utf-8") as f:
        f.seek(position)
        new_content = f.read()

    # The error log format: entries separated by '---' lines.
    # Each entry starts with '## [LEVEL] timestamp'.
    entries = []
    # Split on separator lines (--- on its own line)
    blocks = re.split(r'\n---\n', new_content)
    for block in blocks:
        block = block.strip()
        if not block:
            continue
        # Check if this block starts with a known header
        match = re.match(r'^##\s+\[(\w+)\]', block)
        if match:
            level = match.group(1)
            if level in ERROR_LOG_FAIL_LEVELS:
                entries.append(block)
        # If no header match, the block might be a continuation fragment
        # from a partial read — include it conservatively if non-trivial
        elif len(block) > 20:
            entries.append(block)

    return entries


def format_error_log_entries(entries: list[str]) -> str:
    """Format error log entries for inclusion in test failure output."""
    if not entries:
        return "(none)"
    return "\n---\n".join(entries)
