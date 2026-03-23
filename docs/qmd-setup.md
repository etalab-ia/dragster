# qmd Setup Guide

Detailed guide for installing and configuring qmd for semantic search.

## What is qmd?

qmd is a CLI tool for semantic document search. It creates vector embeddings from markdown files and enables natural language queries.

## Installation

### Option 1: Bun (Recommended)

```bash
bun install -g @tobilu/qmd
```

### Option 2: npm

```bash
npm install -g @tobilu/qmd
```

### Verify Installation

```bash
qmd --version
```

## First-Time Setup

### 1. Create a Collection

```bash
qmd collection add <path> --name <name>
```

Example:

```bash
qmd collection add ./docs --name my-project
```

### 2. Add Context (Optional)

Context helps qmd understand your corpus:

```bash
qmd context add qmd://<name> "<description>"
```

Example:

```bash
qmd context add qmd://my-project "Project documentation including API guides, tutorials, and reference material"
```

### 3. Generate Embeddings

```bash
qmd embed
```

This creates vector embeddings for all documents. Depending on corpus size, this may take a few minutes.

### 4. Verify Setup

```bash
qmd status
```

Expected output:

```
Collections:
  my-project
    Documents: 42
    Status: ready
```

## Basic Operations

### List Collections

```bash
qmd collection list
```

### Remove Collection

```bash
qmd collection remove <name>
```

### Update Documents

After adding/modifying documents:

```bash
qmd collection update <path> --name <name>
qmd embed
```

## Search

### Query (Semantic Search)

```bash
qmd query "<query>" --json
```

### Vector Search (with Scores)

```bash
qmd vsearch "<query>" --json
```

### Hybrid Search

```bash
qmd search "<query>" --json
```

### Limit Results

```bash
qmd query "<query>" --limit 10 --json
```

### Search Specific Collection

```bash
qmd query "<query>" --collection <name> --json
```

## Configuration

qmd stores data in:

```
~/.qmd/
├── collections/
├── embeddings/
└── config.json
```

### Environment Variables

| Variable | Description |
|----------|-------------|
| `QMD_DATA_DIR` | Custom data directory |
| `QMD_EMBEDDING_MODEL` | Embedding model (default: OpenAI) |

## Embedding Models

By default, qmd uses OpenAI embeddings. Set `OPENAI_API_KEY`:

```bash
export OPENAI_API_KEY="sk-..."
```

For local embeddings, see qmd documentation for supported models.

## MCP Server

qmd can run as an MCP server:

```bash
qmd mcp
```

This exposes qmd functionality via the Model Context Protocol.

### MCP Configuration

Add to your MCP settings:

```json
{
  "mcpServers": {
    "qmd": {
      "command": "qmd",
      "args": ["mcp"]
    }
  }
}
```

## Requirements

### sqlite-vec Extension

qmd requires SQLite with the `sqlite-vec` extension for vector operations. This is included in some SQLite builds but not all.

**Check if sqlite-vec is available:**

```bash
qmd embed
```

If you see: `sqlite-vec is not available`, you need to install a SQLite build with extension loading support.

**Solutions:**

1. **macOS (Homebrew):**
   ```bash
   brew install sqlite
   ```

2. **Linux:**
   ```bash
   # Ubuntu/Debian
   sudo apt-get install sqlite3 libsqlite3-dev

   # Build sqlite-vec from source
   git clone https://github.com/asg017/sqlite-vec
   cd sqlite-vec
   make loadable
   ```

3. **Use Docker:**
   ```bash
   docker run -v $(pwd):/data tobil/qmd embed
   ```

## Troubleshooting

### "No collections found"

Run `qmd collection add <path> --name <name>` first.

### "sqlite-vec is not available"

This error means SQLite doesn't have extension loading support. See Requirements section above.

### "Embeddings failed"

1. Check `OPENAI_API_KEY` is set (if using OpenAI embeddings)
2. Verify documents are readable: `ls -la <path>`
3. Check for empty files: `find <path> -empty`
4. Verify sqlite-vec is available (see Requirements)

### "Search returns no results"

1. Verify embeddings: `qmd embed`
2. Try broader query terms
3. Check collection status: `qmd status`

### Slow embeddings

Large corpora may take time. For faster processing:
- Use smaller chunk sizes
- Split into multiple collections
- Use local embedding models

## Resources

- [qmd GitHub](https://github.com/tobi/qmd)
- [qmd Documentation](https://github.com/tobi/qmd#readme)
