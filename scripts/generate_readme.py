#!/usr/bin/env python3
"""
README Generator for awesome-free-llm-api

Reads providers.json and generates:
1. Quick Comparison Table (between AUTO-GENERATED-COMPARISON markers)
2. Categorized Provider Sections (between AUTO-GENERATED-SECTIONS markers)

Usage:
    python scripts/generate_readme.py

The script updates README.md in place, preserving all content outside the markers.
"""

import json
import sys
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# Paths relative to project root
PROJECT_ROOT = Path(__file__).parent.parent
PROVIDERS_PATH = PROJECT_ROOT / "data" / "providers.json"
CATEGORIES_PATH = PROJECT_ROOT / "data" / "categories.json"
README_PATH = PROJECT_ROOT / "README.md"

# Category display names
CATEGORY_NAMES = {
    "free-tier": "Free Tier APIs",
    "openai-compatible": "OpenAI-Compatible APIs",
    "self-hosted": "Self-Hosted / Open Source Alternatives",
    "experimental": "Experimental / Daily Free Access"
}


def load_json(file_path: Path) -> dict | list:
    """Load and parse JSON file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"ERROR: File not found: {file_path}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON in {file_path}: {e}")
        sys.exit(1)


def group_providers_by_category(providers: list) -> dict:
    """Group providers by their category."""
    grouped = defaultdict(list)
    for provider in providers:
        category = provider.get("category", "unknown")
        grouped[category].append(provider)
    return dict(grouped)


def generate_comparison_table(providers: list) -> str:
    """Generate the quick comparison table."""
    lines = []
    lines.append("")
    lines.append("| Provider | Category | Free Tier | OpenAI-Compatible | Notes | Website |")
    lines.append("|----------|----------|-----------|-------------------|-------|---------|")

    for p in providers:
        name = p.get("name", "Unknown")
        category = p.get("category", "")
        category_display = CATEGORY_NAMES.get(category, category)
        free_tier = p.get("free_tier", "N/A")
        openai = "Yes" if p.get("openai_compatible", False) else "No"
        notes = p.get("notes", "")[:50] + ("..." if len(p.get("notes", "")) > 50 else "")
        website = p.get("website", "")

        # Escape pipes in content
        notes = notes.replace("|", "\\|")

        lines.append(f"| {name} | {category_display} | {free_tier} | {openai} | {notes} | {website} |")

    lines.append("")
    return "\n".join(lines)


def generate_categorized_sections(grouped: dict) -> str:
    """Generate categorized provider sections."""
    lines = []

    # Determine section order
    section_order = ["free-tier", "openai-compatible", "self-hosted", "experimental"]
    categories_to_generate = [cat for cat in section_order if cat in grouped]

    for category in categories_to_generate:
        providers = grouped[category]
        category_name = CATEGORY_NAMES.get(category, category)

        lines.append("")
        lines.append(f"### {category_name}")
        lines.append("")

        for p in providers:
            name = p.get("name", "Unknown")
            description = p.get("description", "")
            website = p.get("website", "")
            free_tier = p.get("free_tier", "N/A")
            openai = p.get("openai_compatible", False)
            notes = p.get("notes", "")
            tags = p.get("tags", [])

            lines.append(f"### {name}")
            lines.append("")
            lines.append(f"- **Website**: [{website}]({website})")
            lines.append(f"- **Free Tier**: {free_tier}")
            lines.append(f"- **Models**: See provider documentation")
            lines.append(f"- **OpenAI-Compatible**: {'Yes' if openai else 'No'}")
            lines.append(f"- **Notes**: {notes}")
            lines.append("")

    return "\n".join(lines)


def update_readme(comparison_table: str, sections: str):
    """Update README.md with generated content."""
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace comparison table section
    comparison_start = "<!-- AUTO-GENERATED-COMPARISON-START -->"
    comparison_end = "<!-- AUTO-GENERATED-COMPARISON-END -->"

    if comparison_start in content and comparison_end in content:
        content = content.replace(
            f"{comparison_start}\n<!-- AUTO-GENERATED-COMPARISON-END -->",
            f"{comparison_start}\n{comparison_table}\n<!-- AUTO-GENERATED-COMPARISON-END -->"
        )
        # Handle case where there's nothing between markers
        content = content.replace(
            f"{comparison_start}<!-- AUTO-GENERATED-COMPARISON-END -->",
            f"{comparison_start}\n{comparison_table}\n<!-- AUTO-GENERATED-COMPARISON-END -->"
        )
    else:
        print("WARNING: Comparison markers not found in README.md")
        print(f"  Expected: {comparison_start} ... {comparison_end}")

    # Replace sections section
    sections_start = "<!-- AUTO-GENERATED-SECTIONS-START -->"
    sections_end = "<!-- AUTO-GENERATED-SECTIONS-END -->"

    if sections_start in content and sections_end in content:
        content = content.replace(
            f"{sections_start}\n<!-- AUTO-GENERATED-SECTIONS-END -->",
            f"{sections_start}\n{sections}\n<!-- AUTO-GENERATED-SECTIONS-END -->"
        )
        content = content.replace(
            f"{sections_start}<!-- AUTO-GENERATED-SECTIONS-END -->",
            f"{sections_start}\n{sections}\n<!-- AUTO-GENERATED-SECTIONS-END -->"
        )
    else:
        print("WARNING: Sections markers not found in README.md")
        print(f"  Expected: {sections_start} ... {sections_end}")

    # Update last updated date
    date_str = datetime.now().strftime("%Y-%m-%d")
    content = content.replace(
        "*Maintained by the community. Last updated: ",
        f"*Maintained by the community. Last updated: {date_str}"
    )
    if date_str not in content:
        # Find and replace the date line
        import re
        content = re.sub(
            r"\*Maintained by the community\. Last updated: \d{4}-\d{2}-\d{2}\*",
            f"*Maintained by the community. Last updated: {date_str}*",
            content
        )

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"README.md updated successfully")


def main():
    """Main generation function."""
    print("=" * 60)
    print("awesome-free-llm-api README Generator")
    print("=" * 60)
    print()

    # Load providers
    print(f"Loading providers from: {PROVIDERS_PATH}")
    providers = load_json(PROVIDERS_PATH)

    if not isinstance(providers, list):
        print("ERROR: providers.json must contain an array")
        sys.exit(1)

    print(f"Loaded {len(providers)} provider(s)")
    print()

    # Group by category
    grouped = group_providers_by_category(providers)
    print("Providers by category:")
    for category, cats in grouped.items():
        cat_name = CATEGORY_NAMES.get(category, category)
        print(f"  - {cat_name}: {len(cats)} provider(s)")
    print()

    # Generate content
    print("Generating comparison table...")
    comparison_table = generate_comparison_table(providers)

    print("Generating categorized sections...")
    sections = generate_categorized_sections(grouped)

    # Update README
    print("Updating README.md...")
    update_readme(comparison_table, sections)

    print()
    print("Generation complete!")
    print()
    print("Next steps:")
    print("  1. Review the updated README.md")
    print("  2. Commit changes: git add . && git commit -m 'Update provider list'")
    print("  3. Push: git push")


if __name__ == "__main__":
    main()
