---
name: ingest-documents
description: Parse PDFs, DOCX, and images into markdown using LiteParse. Use when the user has documents they want to convert to markdown, prepare for indexing, or set up a knowledge base. Triggers on keywords like "parse PDF", "convert document", "ingest documents", "PDF to markdown".
license: MIT
allowed-tools: Bash
---

# Ingest Documents

Parse PDFs, DOCX, and images into markdown for indexing or knowledge base setup.

## Prerequisites

Install liteparse:

```bash
npm install -g @llamaindex/liteparse
# or
brew tap run-llama/liteparse
brew install llamaindex-liteparse
```

Verify installation:

```bash
lit --version
```

## Workflow

### 1. Verify liteparse

```bash
lit --version
```

If not installed, see Prerequisites above.

### 2. Parse Single Document

```bash
lit parse <input> --format text -o <output.md>
```

Examples:

```bash
lit parse report.pdf --format text -o report.md
lit parse document.docx --format text -o document.md
```

### 3. Batch Parse Directory

```bash
lit batch-parse <input-dir> <output-dir>
```

Examples:

```bash
lit batch-parse ./pdfs ./docs
lit batch-parse ~/Documents/contracts ./markdown
```

### 4. Verify Output

Check the generated markdown:

```bash
ls -la <output-dir>
head -50 <output.md>
```

## Arguments

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `input` | string | required | Path to document or directory |
| `output` | string | ./output | Output path (file or directory) |
| `format` | string | text | Output format: `text` or `json` |

## Supported Formats

- **PDF**: `.pdf`
- **DOCX**: `.docx`, `.doc`
- **Images**: `.png`, `.jpg`, `.jpeg` (requires OCR)

## Error Handling

If parsing fails:
1. Check file exists: `ls -la <input>`
2. Check file type: `file <input>`
3. Try with verbose output: `lit parse <input> --format text -o <output> -v`

## Next Steps

After ingesting documents, use `/setup-knowledge-base` to index them for semantic search.
