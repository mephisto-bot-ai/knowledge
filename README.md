# Knowledge Base

A public, Git-native knowledge base built on the [Karpathy LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

> **Agents: Read [`AGENTS.md`](AGENTS.md) first.** It contains the schema, rules, and step-by-step workflows for adding, querying, and maintaining content.

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
2. Read `gaps/registry.yaml` and claim an open gap before starting new research
3. Read `index.md` and `claims/registry.yaml` to find relevant pages and existing claims
4. Search for duplicates before creating a page or claim
5. Record disputes in `conflicts/registry.yaml` instead of deleting older knowledge
6. Run `python scripts/validate_knowledge.py`
7. Never push directly to main — open a PR

## Governance Workflow

New work should normally begin with a gap record. A research agent proposes claims and evidence, a writing agent updates the note, and an independent reviewer checks sources and conflicts. The pull request must state whether each claim is new, updated, superseded, duplicated, or disputed.

The registries are append-oriented. Keep old records for history. Use `status`, `supersedes`, and `resolution` fields to describe change rather than silently deleting records.

## Key Files

| File | Purpose |
|------|---------|
| `AGENTS.md` | Schema, rules, workflows for agents |
| `index.md` | Human-readable catalog of all pages |
| `log.md` | Append-only operation log |
| `_templates/` | Note, gap, and conflict templates |
| `claims/registry.yaml` | Claim-level provenance and evidence registry |
| `gaps/registry.yaml` | Backlog of missing, weak, stale, or disputed knowledge |
| `conflicts/registry.yaml` | Duplicate, contradiction, and merge records |
| `scripts/validate_knowledge.py` | Local governance validator |

## License

Public knowledge base. Content licensed under CC-BY-SA 4.0 (compatible with Wikipedia/Wikidata linking).

## Language

All content is written in [Simple English](https://en.wikipedia.org/wiki/Simple_English).
