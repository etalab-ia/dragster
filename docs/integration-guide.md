# Integration Guide

How to use Dragster skills with various AI coding agents.

## Letta Code

```bash
# Install all skills
npx skills add etalab-ia/dragster --all

# Or install specific skills
npx skills add etalab-ia/dragster --skill ingest-documents
npx skills add etalab-ia/dragster --skill setup-knowledge-base
npx skills add etalab-ia/dragster --skill search-knowledge-base
```

### Usage

In Letta Code, invoke skills with `/`:

```
/ingest-documents ./pdfs --output ./docs
/setup-knowledge-base ./docs --name my-project
/search-knowledge-base "authentication flow"
```

## Claude Code

Claude Code uses the same skills format:

```bash
# Install to Claude Code
npx skills add etalab-ia/dragster --agent claude-code
```

Skills are installed to `.claude/skills/`.

### Usage

Claude Code auto-loads skills from `.claude/skills/`. Use natural language:

```
Parse the PDFs in ./documents and create a knowledge base
```

## OpenCode

```bash
# Install to OpenCode
npx skills add etalab-ia/dragster --agent opencode
```

Skills are installed to `.opencode/skills/`.

## Cursor

```bash
# Install to Cursor
npx skills add etalab-ia/dragster --agent cursor
```

Skills are installed to `.cursor/skills/`.

## GitHub Copilot

```bash
# Install to Copilot
npx skills add etalab-ia/dragster --agent github-copilot
```

Skills are installed to `.github/copilot/skills/`.

## Manual Installation

If your agent isn't supported by the skills CLI, manually copy the SKILL.md files:

```bash
# Clone the repo
git clone https://github.com/etalab-ia/dragster.git

# Copy skills to your agent's skills directory
cp -r dragster/ingest-documents ~/.your-agent/skills/
cp -r dragster/setup-knowledge-base ~/.your-agent/skills/
cp -r dragster/search-knowledge-base ~/.your-agent/skills/
```

## MCP Integration (Future)

Iteration 1 will add MCP server support for:
- Confluence integration
- Real-time document sync
- Enterprise authentication

## Troubleshooting

### Skills not loading

1. Check the skill directory exists: `ls ~/.your-agent/skills/`
2. Verify SKILL.md format: `head -20 ~/.your-agent/skills/ingest-documents/SKILL.md`
3. Restart your agent

### Tools not found

1. Verify liteparse: `lit --version`
2. Verify qmd: `qmd --version`
3. Install if missing (see README.md)

### Search returns no results

1. Check collection exists: `qmd status`
2. Verify embeddings: `qmd embed`
3. Try broader query terms
