# Manual Skill Testing Plan (Letta Code)

Use this checklist to verify Dragster skills are loaded and working in a fresh test agent.

## 0) Confirm skills are visible

Run in Letta Code:

```text
/skills
```

Expected skills:
- `liteparse`
- `setup-knowledge-base`
- `search-knowledge-base`

---

## 1) Test `liteparse` selection

Prompt:

```text
I need to parse a PDF at ./tests/fixtures/sample.pdf into markdown. Please use the appropriate skill and show me the exact command you would run.
```

Pass criteria:
- Mentions/uses `liteparse`
- Suggests `lit parse ...`
- Gives a concrete command and output path

---

## 2) Test `setup-knowledge-base`

Prompt:

```text
I have markdown files in ./docs and want a searchable knowledge base. Use the right skill and provide the qmd commands step by step.
```

Pass criteria:
- Uses `setup-knowledge-base`
- Gives `qmd` setup/indexing flow
- Explicitly states **collection name** and **source path**
- Explicitly states where the index/collection is stored and includes `qmd status` for verification

Fail criteria:
- Omits storage location details
- Omits collection name/path context

---

## 3) Test `search-knowledge-base`

Prompt:

```text
Now search that knowledge base for “authentication flow” and show the exact query command and how to interpret results.
```

Pass criteria:
- Uses `search-knowledge-base`
- Gives a concrete `qmd` query/search command
- Briefly explains result interpretation (e.g., score/snippet/source)

---

## 4) End-to-end workflow test

Prompt:

```text
Give me an end-to-end workflow from raw PDF -> parsed markdown -> indexed knowledge base -> semantic search, using the available skills only.
```

Pass criteria:
- Correct sequence: parse → setup/index → search
- No invented tools
- Commands are runnable in this repository

---

## 5) Negative/control test

Prompt:

```text
I want to convert DOCX to markdown and then semantically search it. Which skills will you use and why?
```

Pass criteria:
- Selects `liteparse` for conversion
- Selects `setup-knowledge-base` + `search-knowledge-base` for indexing/search
- Explains tool choice clearly

---

## Optional quick scoring template

| Test | Pass/Fail | Notes |
|------|-----------|-------|
| 0. Skills listed |  |  |
| 1. liteparse |  |  |
| 2. setup-knowledge-base |  |  |
| 3. search-knowledge-base |  |  |
| 4. End-to-end |  |  |
| 5. Negative/control |  |  |

