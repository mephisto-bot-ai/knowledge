# AGENTS.md — Knowledge Base Schema & Rules

> This file is the schema layer of the Karpathy LLM Wiki pattern.
> It tells agents how the knowledge base is structured, what conventions to follow,
> and what workflows to run when ingesting, querying, or maintaining the wiki.
> Co-evolve this file over time as you figure out what works.

## Purpose

This is the **public knowledge base** — curated, sanitized knowledge pages accessible to anyone.

```
Private repo (research)  → Full research, raw sources, cross-AI surveys, ADRs, sensitive details
Public repo (knowledge)  → THIS REPO — Sanitized wiki pages, concepts, entities, comparisons
```

Content here is derived from the private `research` repo. Sensitive details (internal IPs, credentials, agent identifiers, memory bank references) are removed before publishing.

## Directory Structure

```
wiki/
  concepts/      Core concept pages
  entities/      People, organizations, tools, projects
  comparisons/   A vs B comparisons
  syntheses/     Cross-source thematic synthesis
  summaries/     One summary per source (sanitized)

_templates/      Note templates
```

## Frontmatter Standard

### Required fields (all notes)

```yaml
---
title: "Note Title"
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

### 1. Publish (from private repo)

1. Take a wiki page from the private `research` repo
2. Sanitize: remove internal IPs, credentials, agent names, bank references
3. Replace internal references with public-safe equivalents
4. Commit to this repo

### 2. Query

1. Read `index.md` to find relevant pages
2. Drill into specific wiki pages
3. Answer with citations (note ID + source URL)

### 3. Lint

1. Check `index.md` matches actual files
2. Check for broken `[[wikilinks]]`
3. Check for orphan pages (no incoming links)
4. Check `review_after` dates — flag stale notes
5. Verify external URLs still valid
6. Check `tier` — propose demoting dormant notes to archive

## Rules

1. **Never publish secrets.** No API keys, tokens, passwords, internal IPs, agent identifiers, or memory bank references.
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
12. **Sanitize before publishing.** If in doubt, leave it in the private repo.

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
