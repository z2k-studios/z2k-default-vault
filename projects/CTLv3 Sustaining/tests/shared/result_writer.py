from __future__ import annotations

"""
CTLv3 Sustaining — Test Result Writer

Writes last-run-results.md into each feature's test folder after a test run.
The file has YAML frontmatter (machine-readable) and a Markdown body (human-readable).

Usage:
    from shared.result_writer import RunResult, write_results

    run_result = RunResult("003", "Directory Structure")
    run_result.add_req("003-001", "Vault root folder exists", "PASS")
    run_result.add_req("003-002", "Templates folder exists", "FAIL", notes="Missing folder: ...")
    write_results(FEATURE_DIR, run_result)
"""

import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class ReqResult:
    id: str
    description: str
    result: str                    # "PASS" | "FAIL" | "SKIP"
    tier: str = "quantitative"    # "quantitative" | "qualitative"
    score: Optional[float] = None  # 0–100, qualitative only
    notes: str = ""               # failure detail or skip reason


@dataclass
class TemplateAssessment:
    """Per-template qualitative assessment detail."""
    path: str                      # relative path from vault root
    weighted_score: float          # 0–100 final weighted score
    item_results: list             # list of dicts: {id, score, notes}
    suggestions: list              # list of str


@dataclass
class RunResult:
    feature_number: str
    feature_name: str
    date_run: datetime = field(default_factory=datetime.now)
    quality_score: Optional[float] = None
    quality_threshold: float = 70.0
    quality_override: bool = False
    requirements: list = field(default_factory=list)       # list[ReqResult]
    template_assessments: list = field(default_factory=list)  # list[TemplateAssessment]

    def add_req(
        self,
        id: str,
        description: str,
        result: str,
        tier: str = "quantitative",
        score: Optional[float] = None,
        notes: str = "",
    ) -> None:
        self.requirements.append(ReqResult(id, description, result, tier, score, notes))

    def add_template(
        self,
        path: str,
        weighted_score: float,
        item_results: list,
        suggestions: list,
    ) -> None:
        self.template_assessments.append(
            TemplateAssessment(path, weighted_score, item_results, suggestions)
        )

    @property
    def passed(self) -> int:
        return sum(1 for r in self.requirements if r.result == "PASS")

    @property
    def failed(self) -> int:
        return sum(1 for r in self.requirements if r.result == "FAIL")

    @property
    def skipped(self) -> int:
        return sum(1 for r in self.requirements if r.result == "SKIP")

    @property
    def overall_result(self) -> str:
        if self.failed > 0:
            return "FAIL"
        if self.skipped > 0 and self.passed == 0:
            return "SKIP"
        return "PASS"


# ---------------------------------------------------------------------------
# Writer
# ---------------------------------------------------------------------------

def write_results(
    test_dir: Path,
    run_result: RunResult,
    weights: Optional[dict] = None,
) -> Path:
    """
    Write last-run-results.md to test_dir.

    Args:
        test_dir:   Path to the feature's test folder (e.g., tests/003 - Directory Structure/)
        run_result: Populated RunResult for this run
        weights:    Optional {req_id: int} weight map (qualitative features only).
                    Included in YAML frontmatter if provided.

    Returns:
        Path to the written file.
    """
    out_path = test_dir / "last-run-results.md"
    content = _build_content(run_result, weights)
    out_path.write_text(content, encoding="utf-8")
    return out_path


def _build_content(run: RunResult, weights: Optional[dict]) -> str:
    parts = []
    parts.append(_build_yaml(run, weights))
    parts.append(_build_markdown(run, weights))
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# YAML frontmatter
# ---------------------------------------------------------------------------

def _build_yaml(run: RunResult, weights: Optional[dict]) -> str:
    lines = ["---"]
    lines.append(f'feature_number: "{run.feature_number}"')
    lines.append(f'feature_name: "{_escape_yaml(run.feature_name)}"')
    lines.append(f'date_run: "{run.date_run.strftime("%Y-%m-%d %H:%M:%S")}"')
    lines.append(f"result: {run.overall_result}")
    lines.append(f"passed: {run.passed}")
    lines.append(f"failed: {run.failed}")
    lines.append(f"skipped: {run.skipped}")

    if run.quality_score is not None:
        lines.append(f"quality_score: {run.quality_score:.1f}")
        lines.append(f"quality_threshold: {run.quality_threshold:.1f}")
    elif run.quality_override:
        lines.append("quality_score: OVERRIDE")

    lines.append("requirements:")
    for req in run.requirements:
        lines.append(f"  - id: {req.id}")
        lines.append(f"    description: \"{_escape_yaml(req.description)}\"")
        lines.append(f"    result: {req.result}")
        lines.append(f"    tier: {req.tier}")
        if req.score is not None:
            lines.append(f"    score: {req.score:.1f}")
        if req.notes:
            lines.append(f"    notes: \"{_escape_yaml(req.notes)}\"")

    lines.append("---")
    return "\n".join(lines)


def _escape_yaml(s: str) -> str:
    """Minimal YAML string escaping for double-quoted scalars."""
    return s.replace("\\", "\\\\").replace('"', '\\"')


# ---------------------------------------------------------------------------
# Markdown body
# ---------------------------------------------------------------------------

def _build_markdown(run: RunResult, weights: Optional[dict]) -> str:
    sections = []

    # Header
    sections.append(f"# Feature {run.feature_number} — {run.feature_name} — Last Run Results")
    sections.append(f"**Date:** {run.date_run.strftime('%Y-%m-%d %H:%M:%S')}")
    sections.append(f"**Overall Result:** {run.overall_result}")
    sections.append("")

    # Score line (qualitative features)
    if run.quality_score is not None:
        threshold = run.quality_threshold
        pass_fail = "PASS" if run.quality_score >= threshold else "FAIL"
        sections.append(
            f"**Quality Score:** {run.quality_score:.1f}% "
            f"(threshold: {threshold:.0f}%) — {pass_fail}"
        )
        sections.append("")
    elif run.quality_override:
        sections.append("**Quality Score:** OVERRIDE (forced pass)")
        sections.append("")

    # Requirements summary table
    sections.append("## Requirements")
    sections.append("")
    header = "| Req ID | Description | Result | Tier |"
    divider = "|--------|-------------|--------|------|"
    if weights:
        header = "| Req ID | Description | Result | Tier | Weight | Score |"
        divider = "|--------|-------------|--------|------|--------|-------|"

    sections.append(header)
    sections.append(divider)
    for req in run.requirements:
        result_badge = req.result
        desc = req.description
        tier = req.tier
        if weights:
            w = weights.get(req.id, 0)
            w_str = f"{w}%" if w > 0 else "—"
            sc_str = f"{req.score:.0f}%" if req.score is not None else "—"
            sections.append(f"| {req.id} | {desc} | {result_badge} | {tier} | {w_str} | {sc_str} |")
        else:
            sections.append(f"| {req.id} | {desc} | {result_badge} | {tier} |")

    sections.append("")

    # Failures detail
    failures = [r for r in run.requirements if r.result == "FAIL"]
    if failures:
        sections.append("## Failures")
        sections.append("")
        for req in failures:
            sections.append(f"### {req.id} — {req.description}")
            if req.notes:
                sections.append(req.notes)
            sections.append("")

    # Per-template qualitative breakdown
    if run.template_assessments:
        sections.append("## Per-Template Qualitative Assessment")
        sections.append("")
        sections.append(f"{len(run.template_assessments)} templates assessed.")
        sections.append("")

        # Sort: lowest scores first for easier review of problem areas
        sorted_assessments = sorted(run.template_assessments, key=lambda a: a.weighted_score)

        for assessment in sorted_assessments:
            template_name = Path(assessment.path).name
            score_str = f"{assessment.weighted_score:.1f}%"
            pass_fail = "PASS" if assessment.weighted_score >= run.quality_threshold else "FAIL"
            sections.append(f"### {template_name} — {score_str} {pass_fail}")
            sections.append(f"*Path: {assessment.path}*")
            sections.append("")

            if assessment.item_results:
                sections.append("| Item | Score | Notes |")
                sections.append("|------|-------|-------|")
                for item in assessment.item_results:
                    item_id = item.get("id", "")
                    item_score = item.get("score", "")
                    item_notes = item.get("notes", "").replace("\n", " ").replace("|", "\\|")
                    score_display = f"{item_score}%" if isinstance(item_score, (int, float)) else str(item_score)
                    sections.append(f"| {item_id} | {score_display} | {item_notes} |")
                sections.append("")

            if assessment.suggestions:
                sections.append("**Suggestions:**")
                for suggestion in assessment.suggestions:
                    sections.append(f"- {suggestion}")
                sections.append("")

    return "\n".join(sections)
