# AGENTS.md — Knowledge Base Schema & Rules

> This file is the schema layer of the Karpathy LLM Wiki pattern.
> It tells agents how the knowledge base is structured, what conventions to follow,
> and what workflows to run when ingesting, querying, or maintaining the wiki.
> Co-evolve this file over time as you figure out what works.

## Purpose

This is a **public knowledge base** — original, self-contained knowledge pages accessible to anyone.

This repo is **independent**. It does not contain, derive from, or reference any private research data. All content is originally authored for this repo based on public sources.

## Bilingual Structure

This repo is bilingual: **English (primary) + Traditional Chinese (auto-translated)**.

```
wiki/
  concepts/
    karpathy-llm-wiki.md        ← English (primary, authoritative)
    karpathy-llm-wiki.zh.md     ← Traditional Chinese (auto-translated from .en)
  entities/
    ...
    ...
    entity-name.zh.md
```

### Language Rules

1. **English is primary.** Create/edit the `.md` file (no suffix) first.
2. **Traditional Chinese is derivative.** Auto-generate `.zh.md` from the English version.
3. **Never edit `.zh.md` directly.** It will be overwritten on next sync. Fix the English source instead.
4. **Frontmatter `lang` field**: `lang: en` for primary, `lang: zh` for translation.
5. **Wikilinks**: `[[note-name]]` links to English, `[[note-name.zh]]` links to Chinese.
6. **Translation preserves structure.** Same sections, same evidence table, same frontmatter (except `lang`).
7. **Technical terms stay in English** within Chinese text (e.g. "frontmatter", "Wikidata QID").

## Directory Structure

```
wiki/
  concepts/      Core concept pages (.md = EN, .zh.md = ZH)
  entities/      People, organizations, tools, projects
  comparisons/   A vs B comparisons
  syntheses/     Cross-source thematic synthesis
  summaries/     One summary per public source

_templates/      Note templates (.md = EN, .zh.md = ZH)
```

## Frontmatter Standard

### Required fields (all notes)

```yaml
---
title: "Note Title"
lang: en                           # en (primary) | zh (translation)
type: concept | entity | comparison | synthesis | summary
status: draft | active | deprecated | superseded
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [tag1, tag2]
---
```

### Extended fields (knowledge notes)

```yaml
confidence: 0.92                    # 0-1, numeric confidence
review_after: 2026-11-22           # Date to re-check this note
tier: active                        # core | active | dormant | archive (memory decay)
related:                           # Wikilinks to related notes
  - "[[other-note]]"
wikidata: Q58806785                # Wikidata QID (stable cross-language identifier)
source_aliases:                    # Multilingual Wikipedia links
  zh: "https://zh.wikipedia.org/wiki/..."
sources: [grok, deepseek, kimi]    # Which AI/tools contributed
```

## Note Content Structure (GBrain Pattern)

Each note is split into two zones:

```markdown
# Title

## Current Conclusion
(Latest understanding — mutable. Agent updates this section.)

## Definition / Summary
...

## Key Claims
- ...

## Evidence
| Claim | Source | Evidence type | Confidence |
|---|---|---|---|
| ... | [source](url) | primary/secondary | 0.9 |

## Interpretation / Analysis
...

## Open Questions
- ...

---

## Evidence Timeline
(Append-only. Never edit past entries. Add new entries at the bottom.)

- 2026-08-22: Initial version. (reason: ...)
```

## Operations

### 1. Create

1. Research a topic from public sources (Wikipedia, official docs, public papers)
2. Write the knowledge page in English (primary)
3. Commit `.md` to this repo
4. Run translation sync to generate `.zh.md` (Traditional Chinese)

### 2. Translate (sync EN → ZH)

1. Find all `.md` files without `.zh.md` counterpart (or where `.zh.md` is stale)
2. For each: translate content to Traditional Chinese, preserving structure
3. Set `lang: zh` in frontmatter
4. Keep technical terms in English (frontmatter, Wikidata, API names)
5. Save as `original-name.zh.md`
6. Commit with message: `i18n: sync zh translation for [note-name]`

### 3. Query

1. Read `index.md` to find relevant pages
2. Drill into specific wiki pages (use `.zh.md` if querying in Chinese)
3. Answer with citations (note ID + source URL)

### 4. Lint

1. Check `index.md` matches actual files
2. Check for broken `[[wikilinks]]`
3. Check for orphan pages (no incoming links)
4. Check `review_after` dates — flag stale notes
5. Verify external URLs still valid
6. Check `tier` — propose demoting dormant notes to archive
7. **Check bilingual sync**: every `.md` should have a `.zh.md` counterpart
8. **Check translation freshness**: `.zh.md` `updated` should match `.md` `updated`

## Rules

1. **Never include private data.** No content from the private research repo. No API keys, tokens, passwords, internal IPs, agent identifiers, or memory bank references.
2. **Every external factual claim needs at least one source URL.**
3. **Prefer primary sources over summaries.**
4. **Keep source quotes and interpretation separate.**
5. **Do not overwrite a note when a new claim conflicts with it.** Mark the conflict explicitly.
6. **Do not delete old knowledge.** Supersede it with a new version and link the transition.
7. **Never merge directly into main.** Open a PR for review.
8. **Every update must include a change reason** in the Evidence Timeline.
9. **Re-check notes after their `review_after` date.**
10. **Do not mirror full Wikipedia content.** Store summaries, quotes, and metadata only.
11. **Update `updated` field on every change.**
12. **All content is original to this repo.** Do not copy from private repos. Write from public sources.
13. **Keep bilingual sync.** Every English page must have a `.zh.md` translation.
14. **Never edit translations directly.** Fix the English source, then re-sync.

## Memory Decay (Tier System)

```
core     — Always relevant, frequently referenced. Never auto-demote.
active   — Current, in use. Default tier for new notes.
dormant  — Not referenced in 90+ days. Candidate for review.
archive  — Superseded or no longer relevant. Kept for history, not in main index.
```

## Wikidata Integration

When a note corresponds to a Wikidata entity:
1. Add `wikidata: QXXXXXXX` to frontmatter
2. Add `source_aliases` for multilingual Wikipedia links
3. Use Wikidata API for structured properties (founding date, creator, etc.)
4. QID is stable even if Wikipedia pages are renamed

## Future Automation (Not Yet Implemented)

- **Publishing**: Quartz to publish wiki/ as searchable website
- **Agent retrieval**: OKB MCP server for vault semantic search
- **GitHub Actions**: Validate frontmatter, build index.json, dead-link check
