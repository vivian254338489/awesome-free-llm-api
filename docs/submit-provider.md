# How to Submit a Provider

Thank you for your interest in contributing to awesome-free-llm-api! This guide explains how to submit a new provider for consideration.

## Submission Process

### Step 1: Check Eligibility

Before submitting, ensure the provider meets our [inclusion criteria](criteria.md).

The provider should:
- Have a legitimate free tier or trial offering
- Be actively maintained
- Have clear documentation
- Not violate our exclusion criteria

### Step 2: Prepare Information

Gather the following information for the submission:

| Field | Required | Description |
|-------|----------|-------------|
| name | Yes | Provider display name |
| description | Yes | Brief description (10-500 chars) |
| category | Yes | One of: free-tier, openai-compatible, self-hosted, experimental |
| website | Yes | Official website URL |
| free_tier | Yes | Description of free offering |
| openai_compatible | Yes | true or false |
| notes | Yes | Developer notes, pros/cons (1-500 chars) |
| tags | Yes | Array of tag IDs from tags.json |

### Step 3: Format as JSON

Example provider entry:

```json
{
  "name": "Example Provider",
  "description": "A sample provider demonstrating the submission format for new entries in the list.",
  "category": "free-tier",
  "website": "https://example-provider.com",
  "free_tier": "100 requests per day",
  "openai_compatible": true,
  "notes": "Good for prototyping. Simple API design. Requires API key registration.",
  "tags": ["free-tier", "developer-friendly", "prototyping"]
}
```

### Step 4: Submit a Pull Request

1. Fork this repository
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/awesome-free-llm-api.git
   cd awesome-free-llm-api
   ```
3. Add your provider to `data/providers.json` (add to the array, don't replace)
4. Run validation:
   ```bash
   python scripts/validate.py
   ```
5. Commit your changes:
   ```bash
   git add data/providers.json
   git commit -m "Add: Example Provider free-tier API"
   ```
6. Push and create a pull request

## Quality Expectations

Submissions should meet these standards:

- **Accurate information**: Provide truthful, verifiable details
- **Professional tone**: Use professional, objective language
- **Complete entries**: All required fields must be filled
- **Appropriate categorization**: Select the correct category
- **Relevant tags**: Use appropriate tags from tags.json

## What Happens After Submission

1. **Automated checks**: Your PR will run validation scripts
2. **Community review**: Contributors may comment or ask questions
3. **Maintainer review**: A maintainer will evaluate the submission
4. **Merge or feedback**: Acceptable submissions are merged; others receive feedback

## Common Reasons for Rejection

- Provider violates exclusion criteria
- Information is inaccurate or misleading
- Entry is incomplete
- Provider is not genuinely free or accessible
- Duplicate of existing entry

## Questions?

Open an issue for clarification before submitting if needed.
