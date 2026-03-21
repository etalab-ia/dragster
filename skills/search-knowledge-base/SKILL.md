---
name: search-knowledge-base
description: Search the qmd index for relevant documents. Use when the user wants to find documents in their indexed corpus, has questions that could be answered by their documents, or needs context from their knowledge base. Triggers on keywords like "search documents", "find in knowledge base", "query index".
license: MIT
allowed-tools: Bash
---

# Search Knowledge Base

Search the qmd index for relevant documents.

## Prerequisites

- qmd installed: `bun install -g @tobilu/qmd`
- Collection set up: Use `/setup-knowledge-base` first

Verify setup:

```bash
qmd status
```

## Workflow

### 1. Verify Knowledge Base

```bash
qmd status
```

Should show your collection(s) with document counts.

### 2. Run Search

```bash
qmd query "<query>" --json
```

Examples:

```bash
qmd query "authentication flow" --json
qmd query "API design patterns" --json
qmd query "deployment process" --json
```

### 3. Present Results

Parse the JSON output and present:

- Document path
- Relevance score
- Relevant excerpt

## Arguments

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `query` | string | required | Search query |
| `mode` | string | query | Search mode: `query`, `vsearch`, `search` |
| `limit` | int | 5 | Number of results |
| `collection` | string | all | Restrict to specific collection |

## Search Modes

| Mode | Description |
|------|-------------|
| `query` | Semantic search (default) |
| `vsearch` | Vector search with scores |
| `search` | Hybrid search |

## Examples

```bash
# Basic search
qmd query "authentication" --json

# Limit results
qmd query "API design" --limit 10 --json

# Search specific collection
qmd query "deployment" --collection api-docs --json

# Vector search with scores
qmd vsearch "configuration" --json
```

## Output Format

JSON output structure:

```json
{
  "results": [
    {
      "path": "docs/guide.md",
      "score": 0.89,
      "content": "..."
    }
  ]
}
```

## Integration with Agents

When using this skill:

1. Run the search query
2. Parse JSON results
3. Present top results with scores
4. Optionally read full documents for deeper context

## Troubleshooting

If no results:
1. Check collection exists: `qmd status`
2. Verify embeddings generated: `qmd embed`
3. Try broader query terms
