# Contributing to awesome-free-llm-api

Thank you for your interest in contributing! This guide will help you get started.

## Quick Start

### Fork and Clone

```bash
# Fork via GitHub UI, then clone your fork
git clone https://github.com/YOUR_USERNAME/awesome-free-llm-api.git
cd awesome-free-llm-api
```

### Install Dependencies

No external dependencies required! This project uses only Python standard library.

### Make Changes

1. Edit `data/providers.json` to add/modify providers
2. Update documentation as needed

## Workflow

### 1. Adding a Provider

Add your provider to the providers array in `data/providers.json`:

```json
{
  "name": "Provider Name",
  "description": "Brief description of the provider.",
  "category": "free-tier",
  "website": "https://provider-website.com",
  "free_tier": "Description of free offering",
  "openai_compatible": true,
  "notes": "Developer notes about this provider.",
  "tags": ["free-tier", "developer-friendly"]
}
```

### 2. Validating Changes

Run the validation script before committing:

```bash
python scripts/validate.py
```

This checks:
- Required fields present
- Data types correct
- Category values valid
- Tag values valid
- String length constraints

### 3. Regenerating README

After modifying providers.json, regenerate the README:

```bash
python scripts/generate_readme.py
```

This updates:
- Quick comparison table
- Categorized provider sections
- Last updated date

### 4. Commit and Push

```bash
git add .
git commit -m "Add: Provider Name free-tier API"
git push origin main
```

### 5. Create Pull Request

Open a pull request on GitHub with:
- Clear title describing the change
- Reference any related issues
- Brief explanation of the addition

## Pull Request Checklist

Before submitting, verify:

- [ ] Provider meets [inclusion criteria](docs/criteria.md)
- [ ] All required fields in providers.json are complete
- [ ] Validation script passes: `python scripts/validate.py`
- [ ] README regenerated: `python scripts/generate_readme.py`
- [ ] No duplicate entries
- [ ] Information is accurate and up-to-date
- [ ] No sensitive information included

## Categories

When adding a provider, use the correct category:

| Category | Description |
|----------|-------------|
| free-tier | Official free tiers from legitimate providers |
| openai-compatible | OpenAI-compatible API gateways |
| self-hosted | Self-hostable open-source alternatives |
| experimental | Daily free access or experimental offerings |

## Tags

Add relevant tags from this list:

- free-tier
- openai-compatible
- self-hosted
- open-source
- daily-free-access
- developer-friendly
- prototyping
- testing
- multi-model
- privacy-focused
- scalable
- embeddings
- high-speed
- research

## Code Style

### Python Scripts

- Use Python 3.6+ syntax
- Follow PEP 8 style guidelines
- Add docstrings to functions
- Use meaningful variable names

### JSON Files

- Use 2-space indentation
- No trailing commas
- UTF-8 encoding

### Markdown

- Use ATX-style headers
- Keep lines under 120 characters when possible
- Use code blocks for examples

## Reporting Issues

For incorrect information or concerns:

1. Search existing issues first
2. Open a new issue with:
   - Provider name
   - Specific concern
   - Evidence/documentation
   - Suggested correction

## Questions?

Open an issue for questions about contributing.
