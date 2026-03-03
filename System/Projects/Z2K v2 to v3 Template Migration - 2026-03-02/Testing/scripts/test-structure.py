#!/usr/bin/env python3
"""Category A — Structure and existence tests. Add assertions below as tasks complete."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from lib.runner import assert_path_exists, run_suite
from lib.yaml_utils import load_yaml_frontmatter, load_raw_yaml, load_file_text, assert_field_present, assert_field_value

VAULT = Path("Data/Vaults/z2k-default-vault")
TESTING_VAULT = Path("Data/Vaults/z2k-testing-vaults/Z2K System Vault Testing")

# ── Task 01: Testing Infrastructure ──────────────────────────

def test_testing_vault_exists():
    return assert_path_exists(TESTING_VAULT)

def test_plugin_installed():
    return assert_path_exists(TESTING_VAULT / ".obsidian/plugins/z2k-plugin-templates/manifest.json")

def test_plugin_config():
    return assert_path_exists(TESTING_VAULT / ".obsidian/plugins/z2k-plugin-templates/data.json")

def test_command_queue_dir():
    return assert_path_exists(TESTING_VAULT / ".obsidian/plugins/z2k-plugin-templates/command-queue")

def test_skeleton_test_structure():
    return assert_path_exists(Path("Data/Vaults/z2k-default-vault/System/Projects/Z2K v2 to v3 Template Migration - 2026-03-02/Testing/scripts/test-structure.py"))

def test_skeleton_test_blocks():
    return assert_path_exists(Path("Data/Vaults/z2k-default-vault/System/Projects/Z2K v2 to v3 Template Migration - 2026-03-02/Testing/scripts/test-blocks.py"))

def test_skeleton_test_templates():
    return assert_path_exists(Path("Data/Vaults/z2k-default-vault/System/Projects/Z2K v2 to v3 Template Migration - 2026-03-02/Testing/scripts/test-templates.py"))

def test_lib_runner():
    return assert_path_exists(Path("Data/Vaults/z2k-default-vault/System/Projects/Z2K v2 to v3 Template Migration - 2026-03-02/Testing/scripts/lib/runner.py"))

def test_lib_yaml_utils():
    return assert_path_exists(Path("Data/Vaults/z2k-default-vault/System/Projects/Z2K v2 to v3 Template Migration - 2026-03-02/Testing/scripts/lib/yaml_utils.py"))

# ── Task 02: Vault Structure ─────────────────────────────────

DOMAINS = [
    "AI", "Beliefs", "Body", "Entities", "Information",
    "Interactions", "Journals", "Locations", "Logs",
    "Memories", "Projects", "System", "Thoughts",
]

def test_domain_folders_exist():
    missing = [d for d in DOMAINS if not (VAULT / d).is_dir()]
    if missing:
        return False, f"Missing domain folders: {', '.join(missing)}"
    return True, f"All {len(DOMAINS)} domain folders exist"

def test_domain_templates_subfolders():
    missing = [d for d in DOMAINS if not (VAULT / d / "Templates").is_dir()]
    if missing:
        return False, f"Missing Templates/ in: {', '.join(missing)}"
    return True, f"All {len(DOMAINS)} domains have Templates/ subfolder"

def test_root_templates_folder():
    return assert_path_exists(VAULT / "Templates")

def test_my_writings_templates():
    return assert_path_exists(VAULT / "Projects" / "My Writings" / "Templates")

# ── Task 03: Root System Block ───────────────────────────────

ROOT_SB = VAULT / ".system-block.md"

def test_root_sb_exists():
    return assert_path_exists(ROOT_SB)

def test_root_sb_required_fields():
    fields = load_raw_yaml(ROOT_SB)
    required = [
        "z2k_metadata_version", "z2k_creation_creator", "z2k_creation_date",
        "z2k_creation_timestamp", "z2k_creation_template", "z2k_creation_language",
        "z2k_creation_library_version", "z2k_card_source_type",
    ]
    missing = [f for f in required if f not in fields]
    if missing:
        return False, f"Missing fields: {', '.join(missing)}"
    return True, f"All {len(required)} required fields present"

def test_root_sb_removed_fields():
    fields = load_raw_yaml(ROOT_SB)
    removed = ["z2k_creation_domain", "z2k_card_build_state", "z2k_card_status"]
    present = [f for f in removed if f in fields]
    if present:
        return False, f"Removed fields still present: {', '.join(present)}"
    return True, "All 3 removed fields confirmed absent"

def test_root_sb_fieldinfo_me():
    text = load_file_text(ROOT_SB)
    if "{{fieldInfo me" in text:
        return True, "{{fieldInfo me}} found in body"
    return False, "{{fieldInfo me}} NOT found in body"

# ── Task 04: Domain System Blocks (Core Domains) ─────────────

RATINGS_DOMAINS = ["Information", "Thoughts", "Beliefs", "Memories"]
PRIVACY_DOMAINS = {
    "Journals": ".:Z2K/Privacy/Private/Journal",
    "Logs": ".:Z2K/Privacy/Private/Log",
}
IDENTITY_ONLY_DOMAINS = ["Interactions", "Locations", "Entities", "Body", "System"]

def test_core_domain_sbs_exist():
    all_core = RATINGS_DOMAINS + list(PRIVACY_DOMAINS.keys()) + IDENTITY_ONLY_DOMAINS
    missing = [d for d in all_core if not (VAULT / d / ".system-block.md").exists()]
    if missing:
        return False, f"Missing .system-block.md in: {', '.join(missing)}"
    return True, f"All {len(all_core)} core domain system blocks exist"

def test_core_domain_sbs_creation_domain():
    all_core = RATINGS_DOMAINS + list(PRIVACY_DOMAINS.keys()) + IDENTITY_ONLY_DOMAINS
    bad = []
    for d in all_core:
        fields = load_raw_yaml(VAULT / d / ".system-block.md")
        expected = f".:Z2K/Domain/{d}"
        if fields.get("z2k_creation_domain") != expected:
            bad.append(f"{d} (got {fields.get('z2k_creation_domain')!r})")
    if bad:
        return False, f"Wrong z2k_creation_domain: {', '.join(bad)}"
    return True, f"All {len(all_core)} have correct z2k_creation_domain"

def test_ratings_domains_have_ratings():
    bad = []
    for d in RATINGS_DOMAINS:
        fields = load_raw_yaml(VAULT / d / ".system-block.md")
        required = ["z2k_rating_depth", "z2k_rating_surprisal", "z2k_rating_passion"]
        missing = [f for f in required if f not in fields]
        if missing:
            bad.append(f"{d} missing {', '.join(missing)}")
    if bad:
        return False, f"Ratings issues: {'; '.join(bad)}"
    return True, f"All {len(RATINGS_DOMAINS)} ratings domains have 3 rating fields"

def test_journals_privacy():
    fields = load_raw_yaml(VAULT / "Journals" / ".system-block.md")
    return assert_field_value(fields, "z2k_card_privacy", ".:Z2K/Privacy/Private/Journal")

def test_logs_privacy():
    fields = load_raw_yaml(VAULT / "Logs" / ".system-block.md")
    return assert_field_value(fields, "z2k_card_privacy", ".:Z2K/Privacy/Private/Log")

def test_identity_only_no_extra_fields():
    bad = []
    for d in IDENTITY_ONLY_DOMAINS:
        fields = load_raw_yaml(VAULT / d / ".system-block.md")
        extra = [k for k in fields if k != "z2k_creation_domain"]
        if extra:
            bad.append(f"{d} has extra: {', '.join(extra)}")
    if bad:
        return False, f"Extra fields: {'; '.join(bad)}"
    return True, f"All {len(IDENTITY_ONLY_DOMAINS)} identity-only domains have no extra fields"

# ── Task 05: AI Domain System Block ──────────────────────────

def test_ai_sb_exists():
    return assert_path_exists(VAULT / "AI" / ".system-block.md")

def test_ai_sb_domain():
    fields = load_raw_yaml(VAULT / "AI" / ".system-block.md")
    return assert_field_value(fields, "z2k_creation_domain", ".:Z2K/Domain/AI")

def test_ai_sb_perspective():
    fields = load_raw_yaml(VAULT / "AI" / ".system-block.md")
    return assert_field_value(fields, "z2k_creation_perspective", "AI")

# ── Task 06: Projects Domain System Block ────────────────────

def test_projects_sb_exists():
    return assert_path_exists(VAULT / "Projects" / ".system-block.md")

def test_projects_sb_domain():
    fields = load_raw_yaml(VAULT / "Projects" / ".system-block.md")
    return assert_field_value(fields, "z2k_creation_domain", ".:Z2K/Domain/Projects")

def test_my_writings_stop_file():
    return assert_path_exists(VAULT / "Projects" / "My Writings" / ".system-block-stop")

# ── Task 07: Root Block Templates ────────────────────────────

BLOCK_TEMPLATES = [
    "Perspective - Me.md",
    "Quotation.md",
    "Citation.md",
    "Card Fabric.md",
    "Extended YAML.md",
]

def test_block_templates_exist():
    missing = [b for b in BLOCK_TEMPLATES if not (VAULT / "Templates" / b).exists()]
    if missing:
        return False, f"Missing block templates: {', '.join(missing)}"
    return True, f"All {len(BLOCK_TEMPLATES)} block templates exist"

def test_block_templates_have_type():
    bad = []
    for b in BLOCK_TEMPLATES:
        fm = load_yaml_frontmatter(VAULT / "Templates" / b)
        if fm.get("z2k_template_type") != "block-template":
            bad.append(b)
    if bad:
        return False, f"Missing z2k_template_type: block-template in: {', '.join(bad)}"
    return True, f"All {len(BLOCK_TEMPLATES)} have z2k_template_type: block-template"

# ── Task 08: Information Domain Blocks ────────────────────────

INFO_BLOCKS = [
    "Podcast Interview Content.md",
    "Information - Summary.md",
    "Information - Overview.md",
    "Information - Synthesis.md",
    "Information - Details.md",
]

def test_info_blocks_exist():
    missing = [b for b in INFO_BLOCKS if not (VAULT / "Information" / "Templates" / b).exists()]
    if missing:
        return False, f"Missing Info blocks: {', '.join(missing)}"
    return True, f"All {len(INFO_BLOCKS)} Information domain blocks exist"

def test_info_blocks_have_type():
    bad = []
    for b in INFO_BLOCKS:
        fm = load_yaml_frontmatter(VAULT / "Information" / "Templates" / b)
        if fm.get("z2k_template_type") != "block-template":
            bad.append(b)
    if bad:
        return False, f"Missing block-template type in: {', '.join(bad)}"
    return True, f"All {len(INFO_BLOCKS)} have z2k_template_type: block-template"

# ── Task 09: Other Domain Blocks ─────────────────────────────

OTHER_BLOCKS = [
    ("Interactions", "Logistics.md"),
    ("Memories", "When Where Who.md"),
    ("Body", "Health Log.md"),
]

def test_other_blocks_exist():
    missing = [f"{d}/{n}" for d, n in OTHER_BLOCKS if not (VAULT / d / "Templates" / n).exists()]
    if missing:
        return False, f"Missing blocks: {', '.join(missing)}"
    return True, f"All {len(OTHER_BLOCKS)} other domain blocks exist"

def test_other_blocks_have_type():
    bad = []
    for d, n in OTHER_BLOCKS:
        fm = load_yaml_frontmatter(VAULT / d / "Templates" / n)
        if fm.get("z2k_template_type") != "block-template":
            bad.append(f"{d}/{n}")
    if bad:
        return False, f"Missing block-template type in: {', '.join(bad)}"
    return True, f"All {len(OTHER_BLOCKS)} have z2k_template_type: block-template"

# ── Task 10: Thoughts Document Templates ─────────────────────

THOUGHTS_TEMPLATES = [
    "Thoughts (General).md",
    "Book Quote.md",
    "Book Concept.md",
    "General Quote.md",
    "Ontology.md",
    "Quote a Source.md",
    "Resolutions.md",
]

def test_thoughts_templates_exist():
    missing = [t for t in THOUGHTS_TEMPLATES if not (VAULT / "Thoughts" / "Templates" / t).exists()]
    if missing:
        return False, f"Missing Thoughts templates: {', '.join(missing)}"
    return True, f"All {len(THOUGHTS_TEMPLATES)} Thoughts templates exist"

def test_thoughts_templates_have_type():
    bad = []
    for t in THOUGHTS_TEMPLATES:
        fm = load_yaml_frontmatter(VAULT / "Thoughts" / "Templates" / t)
        if fm.get("z2k_template_type") != "document-template":
            bad.append(t)
    if bad:
        return False, f"Missing document-template type: {', '.join(bad)}"
    return True, f"All {len(THOUGHTS_TEMPLATES)} have z2k_template_type: document-template"

def test_thoughts_templates_have_version():
    bad = []
    for t in THOUGHTS_TEMPLATES:
        fm = load_yaml_frontmatter(VAULT / "Thoughts" / "Templates" / t)
        if not fm.get("z2k_template_version"):
            bad.append(t)
    if bad:
        return False, f"Missing z2k_template_version: {', '.join(bad)}"
    return True, f"All {len(THOUGHTS_TEMPLATES)} have z2k_template_version"

def test_thoughts_templates_have_suggested_title():
    bad = []
    for t in THOUGHTS_TEMPLATES:
        fm = load_yaml_frontmatter(VAULT / "Thoughts" / "Templates" / t)
        if not fm.get("z2k_template_suggested_title"):
            bad.append(t)
    if bad:
        return False, f"Missing z2k_template_suggested_title: {', '.join(bad)}"
    return True, f"All {len(THOUGHTS_TEMPLATES)} have z2k_template_suggested_title"

# ── Task 11: Beliefs Document Templates ──────────────────────

def test_beliefs_template_exists():
    return assert_path_exists(VAULT / "Beliefs" / "Templates" / "Beliefs (General).md")

def test_beliefs_template_type():
    fm = load_yaml_frontmatter(VAULT / "Beliefs" / "Templates" / "Beliefs (General).md")
    if fm.get("z2k_template_type") != "document-template":
        return False, "Missing z2k_template_type: document-template"
    return True, "Beliefs (General) has z2k_template_type: document-template"

# ── Task 15: Locations Document Templates ─────────────────────

def test_locations_template_exists():
    return assert_path_exists(VAULT / "Locations" / "Templates" / "Locations (General).md")

def test_locations_template_type():
    fm = load_yaml_frontmatter(VAULT / "Locations" / "Templates" / "Locations (General).md")
    if fm.get("z2k_template_type") != "document-template":
        return False, "Missing document-template type"
    return True, "Locations (General) has z2k_template_type: document-template"

# ── Task 16: Journals Document Templates ──────────────────────

JOURNALS_TEMPLATES = ["Daily Journal.md", "Yearly Summary.md"]

def test_journals_templates_exist():
    missing = [t for t in JOURNALS_TEMPLATES if not (VAULT / "Journals" / "Templates" / t).exists()]
    if missing:
        return False, f"Missing: {', '.join(missing)}"
    return True, f"All {len(JOURNALS_TEMPLATES)} Journals templates exist"

def test_daily_journal_passing_sections():
    text = load_file_text(VAULT / "Journals" / "Templates" / "Daily Journal.md")
    required = ["## Passing Thoughts", "## Passing Memories", "## Passing Information"]
    missing = [s for s in required if s not in text]
    if missing:
        return False, f"Missing sections: {', '.join(missing)}"
    return True, "Daily Journal has all 3 passing capture sections"

# ── Task 17: Logs Document Templates ─────────────────────────

LOGS_TEMPLATES = [
    "Daily Log.md", "Weekly Log.md", "Monthly Log.md",
    "Yearly Log.md", "Quarterly Focus List.md", "Yearly Strategic Plan.md",
]

def test_logs_templates_exist():
    missing = [t for t in LOGS_TEMPLATES if not (VAULT / "Logs" / "Templates" / t).exists()]
    if missing:
        return False, f"Missing: {', '.join(missing)}"
    return True, f"All {len(LOGS_TEMPLATES)} Logs templates exist"

def test_logs_templates_have_type():
    bad = []
    for t in LOGS_TEMPLATES:
        fm = load_yaml_frontmatter(VAULT / "Logs" / "Templates" / t)
        if fm.get("z2k_template_type") != "document-template":
            bad.append(t)
    if bad:
        return False, f"Missing document-template type: {', '.join(bad)}"
    return True, f"All {len(LOGS_TEMPLATES)} have z2k_template_type: document-template"

def test_daily_log_flame_fields():
    text = load_file_text(VAULT / "Logs" / "Templates" / "Daily Log.md")
    flame_fields = ["Flame-OneWordTheme", "Flame-LogDate-Link", "Flame-DayType",
                    "Flame-WeatherRanking", "Flame-ImportanceToPosterity",
                    "Flame-Location", "Flame-BodyHealthRanking"]
    missing = [f for f in flame_fields if f"{{{{" + f + "}}}}" not in text and f"{{{{{f}}}}}" not in text]
    # Simpler check: just look for the field name string
    missing = [f for f in flame_fields if f not in text]
    if missing:
        return False, f"Missing Flame fields: {', '.join(missing)}"
    return True, f"All {len(flame_fields)} sampled Flame fields present"

# ── Task 19: Body Document Templates ─────────────────────────

def test_body_template_exists():
    return assert_path_exists(VAULT / "Body" / "Templates" / "Body (General).md")

# ── Task 20: System Document Templates ───────────────────────

def test_system_template_exists():
    return assert_path_exists(VAULT / "System" / "Templates" / "System (General).md")

# ── Task 21: Entities Document Templates ─────────────────────

def test_entities_template_exists():
    return assert_path_exists(VAULT / "Entities" / "Templates" / "Contact (General).md")

# ── Task 13: Interactions Document Templates ─────────────────

INTERACTIONS_TEMPLATES = [
    "Interactions (General).md", "Business Meeting.md", "Email.md",
    "Class Lecture.md", "Class Overview.md", "Conversation.md",
    "Amateur Hour.md", "Conversation with Doug.md",
    "Conversation with John Kashiwabara.md",
    "PoND Conversation with Bryn.md", "YPO Event.md", "YPO Forum.md",
]

INTERACTIONS_PERSONAL = [
    "Amateur Hour.md", "Conversation with Doug.md",
    "Conversation with John Kashiwabara.md",
    "PoND Conversation with Bryn.md", "YPO Event.md", "YPO Forum.md",
]

def test_interactions_templates_exist():
    missing = [t for t in INTERACTIONS_TEMPLATES if not (VAULT / "Interactions" / "Templates" / t).exists()]
    if missing:
        return False, f"Missing: {', '.join(missing)}"
    return True, f"All {len(INTERACTIONS_TEMPLATES)} Interactions templates exist"

def test_interactions_templates_have_type():
    bad = []
    for t in INTERACTIONS_TEMPLATES:
        fm = load_yaml_frontmatter(VAULT / "Interactions" / "Templates" / t)
        if fm.get("z2k_template_type") != "document-template":
            bad.append(t)
    if bad:
        return False, f"Missing document-template type: {', '.join(bad)}"
    return True, f"All {len(INTERACTIONS_TEMPLATES)} have z2k_template_type: document-template"

def test_interactions_include_logistics():
    bad = []
    for t in INTERACTIONS_TEMPLATES:
        text = load_file_text(VAULT / "Interactions" / "Templates" / t)
        if '{{> "Logistics"}}' not in text:
            bad.append(t)
    if bad:
        return False, f"Missing Logistics partial: {', '.join(bad)}"
    return True, f"All {len(INTERACTIONS_TEMPLATES)} include Logistics partial"

def test_interactions_personal_author():
    bad = []
    for t in INTERACTIONS_PERSONAL:
        fm = load_yaml_frontmatter(VAULT / "Interactions" / "Templates" / t)
        if fm.get("z2k_template_author") != "Geoff (z2k-gwp)":
            bad.append(t)
    if bad:
        return False, f"Missing z2k_template_author: {', '.join(bad)}"
    return True, f"All {len(INTERACTIONS_PERSONAL)} personal templates have correct author"

# ── Task 14: Memories Document Templates ─────────────────────

MEMORIES_TEMPLATES = [
    "Memories (General).md", "Family Vacation Trip.md",
    "Ontology.md", "PCT Trail Day.md", "Solo Trip Summary.md",
]

def test_memories_templates_exist():
    missing = [t for t in MEMORIES_TEMPLATES if not (VAULT / "Memories" / "Templates" / t).exists()]
    if missing:
        return False, f"Missing: {', '.join(missing)}"
    return True, f"All {len(MEMORIES_TEMPLATES)} Memories templates exist"

def test_memories_templates_have_type():
    bad = []
    for t in MEMORIES_TEMPLATES:
        fm = load_yaml_frontmatter(VAULT / "Memories" / "Templates" / t)
        if fm.get("z2k_template_type") != "document-template":
            bad.append(t)
    if bad:
        return False, f"Missing document-template type: {', '.join(bad)}"
    return True, f"All {len(MEMORIES_TEMPLATES)} have z2k_template_type: document-template"

def test_memories_include_when_where_who():
    bad = []
    for t in MEMORIES_TEMPLATES:
        text = load_file_text(VAULT / "Memories" / "Templates" / t)
        if '{{> "When Where Who"}}' not in text:
            bad.append(t)
    if bad:
        return False, f"Missing When Where Who partial: {', '.join(bad)}"
    return True, f"All {len(MEMORIES_TEMPLATES)} include When Where Who partial"

def test_pct_trail_day_author():
    fm = load_yaml_frontmatter(VAULT / "Memories" / "Templates" / "PCT Trail Day.md")
    return assert_field_value(fm, "z2k_template_author", "Geoff (z2k-gwp)")

# ── Task 18: Projects Document Templates ─────────────────────

PROJECTS_ROOT_TEMPLATES = [
    "Project (General).md", "Active Project.md", "Completed Project.md",
]

MY_WRITINGS_TEMPLATES = [
    "My Writings (General).md", "Personal Writing.md", "Treatise.md", "Code Poem.md",
]

def test_projects_root_templates_exist():
    missing = [t for t in PROJECTS_ROOT_TEMPLATES if not (VAULT / "Projects" / "Templates" / t).exists()]
    if missing:
        return False, f"Missing: {', '.join(missing)}"
    return True, f"All {len(PROJECTS_ROOT_TEMPLATES)} Projects root templates exist"

def test_projects_root_templates_have_type():
    bad = []
    for t in PROJECTS_ROOT_TEMPLATES:
        fm = load_yaml_frontmatter(VAULT / "Projects" / "Templates" / t)
        if fm.get("z2k_template_type") != "document-template":
            bad.append(t)
    if bad:
        return False, f"Missing document-template type: {', '.join(bad)}"
    return True, f"All {len(PROJECTS_ROOT_TEMPLATES)} have z2k_template_type: document-template"

def test_projects_root_templates_have_project_status():
    bad = []
    for t in PROJECTS_ROOT_TEMPLATES:
        fm = load_yaml_frontmatter(VAULT / "Projects" / "Templates" / t)
        if "project_status" not in fm:
            bad.append(t)
    if bad:
        return False, f"Missing project_status: {', '.join(bad)}"
    return True, f"All {len(PROJECTS_ROOT_TEMPLATES)} have project_status field"

def test_my_writings_templates_exist():
    missing = [t for t in MY_WRITINGS_TEMPLATES if not (VAULT / "Projects" / "My Writings" / "Templates" / t).exists()]
    if missing:
        return False, f"Missing: {', '.join(missing)}"
    return True, f"All {len(MY_WRITINGS_TEMPLATES)} My Writings templates exist"

def test_my_writings_templates_have_type():
    bad = []
    for t in MY_WRITINGS_TEMPLATES:
        fm = load_yaml_frontmatter(VAULT / "Projects" / "My Writings" / "Templates" / t)
        if fm.get("z2k_template_type") != "document-template":
            bad.append(t)
    if bad:
        return False, f"Missing document-template type: {', '.join(bad)}"
    return True, f"All {len(MY_WRITINGS_TEMPLATES)} have z2k_template_type: document-template"

def test_code_poem_author():
    fm = load_yaml_frontmatter(VAULT / "Projects" / "My Writings" / "Templates" / "Code Poem.md")
    return assert_field_value(fm, "z2k_template_author", "Geoff (z2k-gwp)")

# ── Task 12: Information Document Templates ──────────────────

INFO_DOCUMENT_TEMPLATES = [
    "Information (General).md", "Academic Paper.md", "Blinkist.md",
    "Book.md", "Kindle Notes.md", "Conference.md", "Lecture.md",
    "Interview.md", "Web Article.md", "Wikipedia Entry.md",
    "Quotation.md", "Quote a Source.md", "Quote an Email.md",
    "Ontology.md", "Podcast Interview.md",
    "Podcast Interview - Adam Grant.md", "Podcast Interview - Dwarkesh Patel.md",
    "Podcast Interview - Huberman Lab.md", "Podcast Interview - Knowledge Project.md",
    "Podcast Interview - Lex Fridman.md", "Podcast Interview - Tim Ferriss.md",
]

INFO_PODCAST_HOST_TEMPLATES = [
    "Podcast Interview - Adam Grant.md", "Podcast Interview - Dwarkesh Patel.md",
    "Podcast Interview - Huberman Lab.md", "Podcast Interview - Knowledge Project.md",
    "Podcast Interview - Lex Fridman.md", "Podcast Interview - Tim Ferriss.md",
]

def test_info_document_templates_exist():
    missing = [t for t in INFO_DOCUMENT_TEMPLATES if not (VAULT / "Information" / "Templates" / t).exists()]
    if missing:
        return False, f"Missing: {', '.join(missing)}"
    return True, f"All {len(INFO_DOCUMENT_TEMPLATES)} Information document templates exist"

def test_info_document_templates_have_type():
    bad = []
    for t in INFO_DOCUMENT_TEMPLATES:
        fm = load_yaml_frontmatter(VAULT / "Information" / "Templates" / t)
        if fm.get("z2k_template_type") != "document-template":
            bad.append(t)
    if bad:
        return False, f"Missing document-template type: {', '.join(bad)}"
    return True, f"All {len(INFO_DOCUMENT_TEMPLATES)} have z2k_template_type: document-template"

def test_podcast_templates_include_content_block():
    all_podcast = ["Podcast Interview.md"] + INFO_PODCAST_HOST_TEMPLATES
    bad = []
    for t in all_podcast:
        text = load_file_text(VAULT / "Information" / "Templates" / t)
        if '{{> "Podcast Interview Content"}}' not in text:
            bad.append(t)
    if bad:
        return False, f"Missing Podcast Interview Content partial: {', '.join(bad)}"
    return True, f"All {len(all_podcast)} podcast templates include content block"

def test_podcast_host_templates_have_fixed_fields():
    bad = []
    for t in INFO_PODCAST_HOST_TEMPLATES:
        text = load_file_text(VAULT / "Information" / "Templates" / t)
        if 'directives="no-prompt"' not in text:
            bad.append(t)
    if bad:
        return False, f"Missing no-prompt directives: {', '.join(bad)}"
    return True, f"All {len(INFO_PODCAST_HOST_TEMPLATES)} host templates have fixed fields"

# ── Task 23: Supporting Documentation ────────────────────────

def test_ai_recommendations_exists():
    return assert_path_exists(VAULT / "AI" / "Z2K Template Library - AI Recommendations.md")

def test_tags_taxonomy_exists():
    return assert_path_exists(VAULT / "System" / "Z2K Tags Taxonomy.md")

def test_library_version_card_exists():
    return assert_path_exists(VAULT / "System" / "Z2K Template Library - v3.md")

# ── Task 22: Root Cross-Domain Templates ─────────────────────

CROSS_DOMAIN_TEMPLATES = ["Card (General).md", "Ontology.md"]

def test_cross_domain_templates_exist():
    missing = [t for t in CROSS_DOMAIN_TEMPLATES if not (VAULT / "Templates" / t).exists()]
    if missing:
        return False, f"Missing: {', '.join(missing)}"
    return True, f"All {len(CROSS_DOMAIN_TEMPLATES)} cross-domain templates exist"

def test_cross_domain_templates_have_type():
    bad = []
    for t in CROSS_DOMAIN_TEMPLATES:
        fm = load_yaml_frontmatter(VAULT / "Templates" / t)
        if fm.get("z2k_template_type") != "document-template":
            bad.append(t)
    if bad:
        return False, f"Missing document-template type: {', '.join(bad)}"
    return True, f"All {len(CROSS_DOMAIN_TEMPLATES)} have z2k_template_type: document-template"

# ── Run ──────────────────────────────────────────────────────

run_suite([
    # Task 01
    test_testing_vault_exists,
    test_plugin_installed,
    test_plugin_config,
    test_command_queue_dir,
    test_skeleton_test_structure,
    test_skeleton_test_blocks,
    test_skeleton_test_templates,
    test_lib_runner,
    test_lib_yaml_utils,
    # Task 02
    test_domain_folders_exist,
    test_domain_templates_subfolders,
    test_root_templates_folder,
    test_my_writings_templates,
    # Task 03
    test_root_sb_exists,
    test_root_sb_required_fields,
    test_root_sb_removed_fields,
    test_root_sb_fieldinfo_me,
    # Task 04
    test_core_domain_sbs_exist,
    test_core_domain_sbs_creation_domain,
    test_ratings_domains_have_ratings,
    test_journals_privacy,
    test_logs_privacy,
    test_identity_only_no_extra_fields,
    # Task 05
    test_ai_sb_exists,
    test_ai_sb_domain,
    test_ai_sb_perspective,
    # Task 06
    test_projects_sb_exists,
    test_projects_sb_domain,
    test_my_writings_stop_file,
    # Task 07
    test_block_templates_exist,
    test_block_templates_have_type,
    # Task 08
    test_info_blocks_exist,
    test_info_blocks_have_type,
    # Task 09
    test_other_blocks_exist,
    test_other_blocks_have_type,
    # Task 10
    test_thoughts_templates_exist,
    test_thoughts_templates_have_type,
    test_thoughts_templates_have_version,
    test_thoughts_templates_have_suggested_title,
    # Task 11
    test_beliefs_template_exists,
    test_beliefs_template_type,
    # Task 15
    test_locations_template_exists,
    test_locations_template_type,
    # Task 16
    test_journals_templates_exist,
    test_daily_journal_passing_sections,
    # Task 17
    test_logs_templates_exist,
    test_logs_templates_have_type,
    test_daily_log_flame_fields,
    # Task 19
    test_body_template_exists,
    # Task 20
    test_system_template_exists,
    # Task 21
    test_entities_template_exists,
    # Task 13
    test_interactions_templates_exist,
    test_interactions_templates_have_type,
    test_interactions_include_logistics,
    test_interactions_personal_author,
    # Task 14
    test_memories_templates_exist,
    test_memories_templates_have_type,
    test_memories_include_when_where_who,
    test_pct_trail_day_author,
    # Task 18
    test_projects_root_templates_exist,
    test_projects_root_templates_have_type,
    test_projects_root_templates_have_project_status,
    test_my_writings_templates_exist,
    test_my_writings_templates_have_type,
    test_code_poem_author,
    # Task 22
    test_cross_domain_templates_exist,
    test_cross_domain_templates_have_type,
    # Task 12
    test_info_document_templates_exist,
    test_info_document_templates_have_type,
    test_podcast_templates_include_content_block,
    test_podcast_host_templates_have_fixed_fields,
    # Task 23
    test_ai_recommendations_exists,
    test_tags_taxonomy_exists,
    test_library_version_card_exists,
])
