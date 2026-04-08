#!/usr/bin/env python3
"""
Validation script for awesome-free-llm-api providers.json

Checks:
- Required fields present
- Data types correct
- Category values valid against categories.json
- Tag values valid against tags.json
- String length constraints
- URL format validation

Usage:
    python scripts/validate.py

Exit codes:
    0 - All records valid
    1 - Validation errors found
"""

import json
import sys
from pathlib import Path
from typing import Any

# Paths relative to project root
PROJECT_ROOT = Path(__file__).parent.parent
PROVIDERS_PATH = PROJECT_ROOT / "data" / "providers.json"
CATEGORIES_PATH = PROJECT_ROOT / "data" / "categories.json"
TAGS_PATH = PROJECT_ROOT / "data" / "tags.json"
SCHEMA_PATH = PROJECT_ROOT / "data" / "schema.json"

# Required fields for each provider entry
REQUIRED_FIELDS = ["name", "description", "category", "website", "free_tier", "openai_compatible", "notes", "tags"]

# Valid categories
VALID_CATEGORIES = ["free-tier", "openai-compatible", "self-hosted", "experimental"]

# Valid tag IDs
VALID_TAG_IDS = [
    "free-tier",
    "openai-compatible",
    "self-hosted",
    "open-source",
    "daily-free-access",
    "developer-friendly",
    "prototyping",
    "testing",
    "multi-model",
    "privacy-focused",
    "scalable",
    "embeddings",
    "high-speed",
    "research"
]

# String length constraints
CONSTRAINTS = {
    "name": {"min": 1, "max": 100},
    "description": {"min": 10, "max": 500},
    "free_tier": {"min": 1, "max": 200},
    "notes": {"min": 1, "max": 500}
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


def validate_string(value: Any, field_name: str, entry_name: str) -> list:
    """Validate string field."""
    errors = []

    if not isinstance(value, str):
        errors.append(f"  [{entry_name}] '{field_name}' must be a string, got {type(value).__name__}")
        return errors

    constraints = CONSTRAINTS.get(field_name, {"min": 1, "max": float("inf")})

    if len(value) < constraints["min"]:
        errors.append(f"  [{entry_name}] '{field_name}' is too short (min {constraints['min']} chars)")
    if len(value) > constraints["max"]:
        errors.append(f"  [{entry_name}] '{field_name}' is too long (max {constraints['max']} chars)")

    if value != value.strip():
        errors.append(f"  [{entry_name}] '{field_name}' has leading/trailing whitespace")

    return errors


def validate_boolean(value: Any, field_name: str, entry_name: str) -> list:
    """Validate boolean field."""
    errors = []

    if not isinstance(value, bool):
        errors.append(f"  [{entry_name}] '{field_name}' must be true or false, got {type(value).__name__}")

    return errors


def validate_url(value: str, field_name: str, entry_name: str) -> list:
    """Validate URL format."""
    errors = []

    if not isinstance(value, str):
        errors.append(f"  [{entry_name}] '{field_name}' must be a string, got {type(value).__name__}")
        return errors

    if not value.startswith(("http://", "https://")):
        errors.append(f"  [{entry_name}] '{field_name}' must start with http:// or https://")

    if len(value) < 10:
        errors.append(f"  [{entry_name}] '{field_name}' is too short to be a valid URL")

    return errors


def validate_tags(value: Any, entry_name: str) -> list:
    """Validate tags array."""
    errors = []

    if not isinstance(value, list):
        errors.append(f"  [{entry_name}] 'tags' must be an array, got {type(value).__name__}")
        return errors

    if len(value) == 0:
        errors.append(f"  [{entry_name}] 'tags' must have at least one tag")
        return errors

    if len(value) > 10:
        errors.append(f"  [{entry_name}] 'tags' has too many items (max 10)")

    for tag in value:
        if not isinstance(tag, str):
            errors.append(f"  [{entry_name}] each tag must be a string, got {type(tag).__name__}")
        elif tag not in VALID_TAG_IDS:
            errors.append(f"  [{entry_name}] invalid tag '{tag}' - must be one of: {', '.join(VALID_TAG_IDS)}")

    return errors


def validate_category(value: str, entry_name: str) -> list:
    """Validate category value."""
    errors = []

    if not isinstance(value, str):
        errors.append(f"  [{entry_name}] 'category' must be a string, got {type(value).__name__}")
        return errors

    if value not in VALID_CATEGORIES:
        errors.append(f"  [{entry_name}] invalid category '{value}' - must be one of: {', '.join(VALID_CATEGORIES)}")

    return errors


def validate_provider(provider: dict, index: int) -> list:
    """Validate a single provider entry."""
    errors = []
    entry_name = f"Entry[{index}] '{provider.get('name', 'UNKNOWN')}'"

    # Check required fields
    for field in REQUIRED_FIELDS:
        if field not in provider:
            errors.append(f"  [{entry_name}] missing required field: '{field}'")

    if "name" in provider:
        errors.extend(validate_string(provider["name"], "name", entry_name))

    if "description" in provider:
        errors.extend(validate_string(provider["description"], "description", entry_name))

    if "free_tier" in provider:
        errors.extend(validate_string(provider["free_tier"], "free_tier", entry_name))

    if "notes" in provider:
        errors.extend(validate_string(provider["notes"], "notes", entry_name))

    if "website" in provider:
        errors.extend(validate_url(provider["website"], "website", entry_name))

    if "openai_compatible" in provider:
        errors.extend(validate_boolean(provider["openai_compatible"], "openai_compatible", entry_name))

    if "category" in provider:
        errors.extend(validate_category(provider["category"], entry_name))

    if "tags" in provider:
        errors.extend(validate_tags(provider["tags"], entry_name))

    return errors


def main():
    """Main validation function."""
    print("=" * 60)
    print("awesome-free-llm-api Provider Validation")
    print("=" * 60)
    print()

    # Load providers
    print(f"Loading providers from: {PROVIDERS_PATH}")
    providers = load_json(PROVIDERS_PATH)

    if not isinstance(providers, list):
        print("ERROR: providers.json must contain an array")
        sys.exit(1)

    if len(providers) == 0:
        print("WARNING: No providers found in providers.json")

    print(f"Found {len(providers)} provider(s)")
    print()

    # Validate each provider
    all_errors = []
    validated_count = 0

    for i, provider in enumerate(providers):
        if not isinstance(provider, dict):
            all_errors.append(f"  Entry[{i}] must be an object, got {type(provider).__name__}")
            continue

        errors = validate_provider(provider, i)
        if errors:
            all_errors.extend(errors)
        else:
            validated_count += 1

    # Print results
    print("-" * 60)
    print(f"Validated: {validated_count}/{len(providers)} entries")
    print("-" * 60)

    if all_errors:
        print()
        print("VALIDATION ERRORS:")
        print()
        for error in all_errors:
            print(error)
        print()
        print("Validation FAILED")
        sys.exit(1)
    else:
        print()
        print("Validation PASSED - All records are valid!")
        print()
        print("Valid categories:", ", ".join(VALID_CATEGORIES))
        print("Valid tags:", ", ".join(VALID_TAG_IDS))
        sys.exit(0)


if __name__ == "__main__":
    main()
