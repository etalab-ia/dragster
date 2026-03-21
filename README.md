# Dragster

Skills for local document ingestion and semantic search. Built for AI coding agents (Letta Code, Claude Code, OpenCode, etc.).

## Quick Start

```bash
# Install tools
bun install -g @tobilu/qmd
npm install -g @llamaindex/liteparse

# Install all skills
npx skills add etalab-ia/dragster

# Or install individual skills
npx skills add etalab-ia/dragster --skill liteparse
npx skills add etalab-ia/dragster --skill setup-knowledge-base
npx skills add etalab-ia/dragster --skill search-knowledge-base
```

## Skills

| Skill | Purpose | Tool |
|-------|---------|------|
| `liteparse` | PDF/DOCX/PPTX/XLSX/Images → Markdown/JSON | [liteparse](https://github.com/run-llama/liteparse) |
| `setup-knowledge-base` | Index documents for semantic search | [qmd](https://github.com/tobi/qmd) |
| `search-knowledge-base` | Search indexed documents | [qmd](https://github.com/tobi/qmd) |

## Workflow

```
Documents ──[liteparse]──> Markdown ──[setup-knowledge-base]──> Index ──[search-knowledge-base]──> Results
```

1. **Parse**: Convert documents to markdown or JSON (PDF, DOCX, PPTX, XLSX, images)
2. **Index**: Create searchable embeddings with qmd
3. **Search**: Query your knowledge base

## Integration

Works with:
- Letta Code
- Claude Code
- OpenCode
- Pi
- Cursor
- Any agent that supports skills

See [docs/integration-guide.md](docs/integration-guide.md) for detailed setup instructions.

## Documentation

- [Integration Guide](docs/integration-guide.md) — How to use with various AI agents
- [qmd Setup](docs/qmd-setup.md) — Detailed qmd installation and configuration

## Requirements

- Node.js 18+ or Bun
- liteparse: `npm install -g @llamaindex/liteparse`
- qmd: `bun install -g @tobilu/qmd`

## License

MIT
