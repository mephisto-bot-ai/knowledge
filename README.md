# Knowledge Base

A public, Git-native knowledge base built on the [Karpathy LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

## What This Is

This repository contains original, public knowledge — concepts, entities, comparisons, and syntheses — as structured Markdown files. All content is independently authored from public sources.

| Repo | Visibility | Content |
|------|-----------|---------|
| `mephisto-bot-ai/knowledge` | **Public** (this repo) | Original knowledge pages, concepts, entities, comparisons |
| `mephisto-bot-ai/research` | Private | Independent — separate research, not shared |

## Structure

```
Layer 1: wiki/     Knowledge pages (concepts, entities, comparisons, syntheses)
Layer 2: AGENTS.md Schema — structure, rules, workflows
```

## How to Use

### For Humans
1. Open this repo as an Obsidian vault
2. Use `[[wikilinks]]` for bidirectional links
3. Use Git plugin or CLI for sync

### For Agents
1. Read `AGENTS.md` for schema, rules, and workflows
2. Read `index.md` to find relevant pages
3. Follow the Query operation to retrieve knowledge
4. Never push directly to main — open a PR

## Key Files

| File | Purpose |
|------|---------|
| `AGENTS.md` | Schema, rules, workflows for agents |
| `index.md` | Human-readable catalog of all pages |
| `log.md` | Append-only operation log |
| `_templates/` | Note templates |

## License

Public knowledge base. Content licensed under CC-BY-SA 4.0 (compatible with Wikipedia/Wikidata linking).

## Language

All content is written in [Simple English](https://en.wikipedia.org/wiki/Simple_English).
