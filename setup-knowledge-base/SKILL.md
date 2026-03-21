---
name: setup-knowledge-base
description: Index a document corpus with qmd for semantic search. Use when the user wants to set up a knowledge base, create a searchable index from markdown documents, or enable semantic search. Triggers on keywords like "index documents", "create knowledge base", "setup search", "semantic search".
license: MIT
allowed-tools: Bash
---

# Setup Knowledge Base

Index a document corpus with qmd for semantic search.

## Prerequisites

Install qmd:

```bash
bun install -g @tobilu/qmd
```

Verify installation:

```bash
qmd --version
```

Documents must be in markdown format. Use `/ingest-documents` first to convert PDFs/DOCX.

## Workflow

### 1. Verify qmd

```bash
qmd --version
```

If not installed, see Prerequisites above.

### 2. Create Collection

```bash
qmd collection add <path> --name <name>
```

Arguments:

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `path` | string | required | Path to document directory |
| `name` | string | derived | Collection name (defaults to directory name) |

Examples:

```bash
qmd collection add ./docs --name my-project
qmd collection add ~/Documents/api-docs --name api-docs
```

### 3. Add Context (Optional)

Add semantic context to help with retrieval:

```bash
qmd context add qmd://<name> "<description>"
```

Examples:

```bash
qmd context add qmd://api-docs "API documentation for the project"
qmd context add qmd://contracts "Legal contracts and agreements"
```

### 4. Generate Embeddings

```bash
qmd embed
```

This creates vector embeddings for all documents in the collection.

### 5. Verify Setup

```bash
qmd status
```

Should show your collection with document count.

## Full Example

```bash
# Create collection
qmd collection add ./docs --name my-project

# Add context
qmd context add qmd://my-project "Project documentation and guides"

# Generate embeddings
qmd embed

# Verify
qmd status
```

## Arguments

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `path` | string | required | Path to document directory |
| `name` | string | derived | Collection name |
| `context` | string | asked | Context description for retrieval |

## Troubleshooting

### "sqlite-vec is not available"

qmd requires SQLite with extension loading support. Solutions:

- **macOS**: `brew install sqlite`
- **Linux**: Build sqlite-vec from source
- **Docker**: Use official qmd Docker image

See docs/qmd-setup.md for detailed instructions.

### Other Issues

If embeddings fail:
1. Check qmd status: `qmd status`
2. Verify documents exist: `ls -la <path>`
3. Check for empty files: `find <path> -empty`

## Next Steps

After setting up the knowledge base, use `/search-knowledge-base` to search your documents.
