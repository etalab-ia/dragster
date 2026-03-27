---
name: memory
description: Maintain persistent memory for document ingestion and issues. Use when ingesting documents, tracking parsing problems, or recalling collection state. Works with ctx for cross-session persistence.
license: MIT
allowed-tools: Bash, Read, Write
---

# Memory Skill

Persistent memory for dragster document processing. Track collections, ingestion history, and issues across sessions.

## Memory Files

### ctx Default Files (created by `ctx init`)

| File | Purpose | When to Use |
|------|---------|-------------|
| `TASKS.md` | Active work | Track what we're doing now |
| `DECISIONS.md` | Architecture decisions | Record why we chose X |
| `LEARNINGS.md` | Patterns learned | Store discovered patterns |
| `CONVENTIONS.md` | Coding conventions | Define how we work |

### Dragster-Specific Files (our templates)

| File | Purpose | When to Use |
|------|---------|-------------|
| `COLLECTIONS.md` | Collection state + ingestion history | Before/after ingesting documents |
| `ISSUES.md` | Parsing problems + workarounds | When encountering errors |

## Location

These files live in `.context/` (ctx's directory) for cross-session persistence:

```
.context/
├── COLLECTIONS.md     # What we've indexed
├── ISSUES.md          # What's broken
├── TASKS.md           # (ctx default) Active work
├── DECISIONS.md       # (ctx default) Architecture decisions
├── LEARNINGS.md       # (ctx default) Patterns learned
└── CONVENTIONS.md     # (ctx default) Conventions
```

## Templates vs Runtime Files

The files in this skill directory (`skills/memory/`) are **templates** for reference.

**Runtime files** live in `.context/` (managed by ctx):

```
.context/
├── COLLECTIONS.md     # Created by ctx init or copied from template
├── ISSUES.md          # Created when first issue is recorded
└── ...
```

### Initial Setup

1. Install ctx: `brew install worktrunk` (or see ctx.ist)
2. Initialize ctx in your project: `ctx init`
   - This creates `.context/` with TASKS.md, DECISIONS.md, LEARNINGS.md, CONVENTIONS.md
3. Copy dragster templates to `.context/`:
   ```bash
   cp skills/memory/COLLECTIONS.md .context/
   cp skills/memory/ISSUES.md .context/
   ```
4. Add dragster-specific patterns to LEARNINGS.md:
   ```bash
   ctx add learning "French government PDFs require --ocr-language fra"
   ctx add learning "Scanned documents benefit from --dpi 300"
   ```

---

## Commands

### Record Ingestion

After successfully ingesting documents, add an entry to COLLECTIONS.md and update the Collections table.

### Record Issue

When encountering a parsing problem, add an entry to ISSUES.md with the error and any workaround found.

### Promote to Learning

When a pattern is discovered, promote to LEARNINGS.md via:
```bash
ctx add learning "<pattern-description>"
```

---

## Workflow

### Starting a Session

1. Read `.context/COLLECTIONS.md` to understand current state
2. Check `.context/ISSUES.md` for any open problems
3. Proceed with document processing

### After Ingestion

1. Update `COLLECTIONS.md` with ingestion details
2. If issues occurred, add entries to `ISSUES.md`
3. If patterns discovered, promote to `LEARNINGS.md`

### Session Wrap-up

1. Review open issues in `ISSUES.md`
2. Mark resolved issues
3. Ensure collections table is accurate

---

## Integration with ctx

This skill integrates with ctx's memory system:

- `ctx agent` includes COLLECTIONS.md and ISSUES.md in context packets
- `ctx add learning` promotes patterns to persistent memory
- `ctx status` shows memory file health
