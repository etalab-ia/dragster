# Dragster

[![Release](https://img.shields.io/github/v/release/etalab-ia/dragster?sort=date&style=flat-square)](https://github.com/etalab-ia/dragster/releases)
[![License](https://img.shields.io/github/license/etalab-ia/dragster?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/status-beta-orange?style=flat-square)](https://github.com/etalab-ia/dragster)

```
 ██████╗ ██████╗  █████╗  ██████╗ ███████╗████████╗███████╗██████╗
 ██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔════╝╚══██╔══╝██╔════╝██╔══██╗
 ██║  ██║██████╔╝███████║██║  ███╗███████╗   ██║   █████╗  ██████╔╝
 ██║  ██║██╔══██╗██╔══██║██║   ██║╚════██║   ██║   ██╔══╝  ██╔══██╗
 ██████╔╝██║  ██║██║  ██║╚██████╔╝███████║   ██║   ███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
```

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
npx skills add etalab-ia/dragster --skill qmd/setup
npx skills add etalab-ia/dragster --skill qmd/search
```

## Skills

| Skill | Purpose | Provider |
|-------|---------|----------|
| `parse` | PDF/DOCX/PPTX/XLSX/Images → Markdown/JSON | [liteparse](https://github.com/run-llama/liteparse) |
| `setup` | Index documents for semantic search | [qmd](https://github.com/tobi/qmd) |
| `search` | Search indexed documents | [qmd](https://github.com/tobi/qmd) |

## Workflow

```
Documents ──[/parse]──> Markdown ──[/setup]──> Index ──[/search]──> Results
```

1. **Parse**: Convert documents to markdown or JSON (PDF, DOCX, PPTX, XLSX, images)
2. **Index**: Create searchable embeddings with qmd
3. **Search**: Query your knowledge base

## Provider System

Skills support multiple providers via metadata in each SKILL.md:

```yaml
---
name: search
provider: qmd
available-providers:
  - qmd
  - pinecone
  - weaviate
---
```

- **provider**: Current active provider (editable by agents)
- **available-providers**: Providers this skill can support

To switch providers, ask your agent to update the `provider` field in the skill file.

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
