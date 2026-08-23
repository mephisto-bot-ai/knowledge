# AGENTS.md — Knowledge Base Schema & Rules

> This file is the schema layer of the Karpathy LLM Wiki pattern.
> It tells agents how the knowledge base is structured, what conventions to follow,
> and what workflows to run when ingesting, querying, or maintaining the wiki.
> Co-evolve this file over time as you figure out what works.

## Purpose

This is a **public knowledge base** — original, self-contained knowledge pages accessible to anyone.

**Access:** Everyone can read and discuss. Contributions via PR.

This repo is **independent**. It does not contain, derive from, or reference any private research data. All content is originally authored for this repo based on public sources.

## Language

This repo uses **Simple English** only. See [Simple English Wikipedia](https://en.wikipedia.org/wiki/Simple_English) for guidelines.

- Use short, clear sentences
- Avoid complex grammar and rare words
- Explain technical terms when first used
- Target a general audience, not specialists

## Directory Structure

```
wiki/
  concepts/      Core concept pages
  entities/      People, organizations, tools, projects
  comparisons/   A vs B comparisons
  syntheses/     Cross-source thematic synthesis
  summaries/     One summary per public source

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
sources: []                      # Removed — kept blank for backward compatibility
```

> **Note**: `sources` field is deprecated and kept blank for backward compatibility only.

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

## Quick Start

### Create a new concept page

1. Copy `_templates/concept.md` to `wiki/concepts/your-note-name.md`
2. Fill in frontmatter (title, type, status, created, updated, tags)
3. Write content in Simple English
4. Update `index.md` with a link to the new page
5. Add a line to `log.md`
6. Commit your changes

### Fix an existing page

1. Edit the `## Current Conclusion` section (this is mutable)
2. **Do not edit** past entries in `## Evidence Timeline`
3. Add a new entry at the bottom of Evidence Timeline with the reason for your change
4. Update the `updated` field in frontmatter
5. Commit your changes

### When knowledge changes (supersede)

1. Do not delete the old page
2. Mark the old claim as `superseded` in `claims/claim-registry.yaml`
3. Create a new claim with `supersedes` pointing to the old one
4. Record the change in the page's Evidence Timeline

## Operations

### 1. Create

1. Research a topic from public sources (Wikipedia, official docs, public papers)
2. Write the knowledge page in Simple English
3. Commit `.md` to this repo

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

1. **Never include secrets or internal infrastructure.** No API keys, tokens, passwords, IPs, hostnames, port numbers, internal service names, agent identifiers, or memory bank names. GitHub is NOT private — even private repos are visible to GitHub staff and vulnerable to leaks.
2. **Every external factual claim needs at least one source URL.**
3. **Prefer primary sources over summaries.**
4. **Keep source quotes and interpretation separate.**
5. **Do not overwrite a note when a new claim conflicts with it.** Mark the conflict explicitly.
6. **Do not delete old knowledge.** Supersede it with a new version and link the transition.
7. **Never merge directly into main.** Open a PR for review.
7a. **Discuss before large changes.** Open an issue first. State the problem, the proposed change, and the alternatives. Wait for resolution (suggested 72 hours) before opening a PR. Link the PR to the issue. Each PR should solve one well-defined item, not bundle multiple decisions together.
8. **Every update must include a change reason** in the Evidence Timeline.
9. **Re-check notes after their `review_after` date.**
10. **Do not mirror full Wikipedia content.** Store summaries, quotes, and metadata only.
11. **Update `updated` field on every change.**
12. **All content is original to this repo.** Do not copy from private repos. Write from public sources.
13. **Write in Simple English.** Short sentences, clear words, explain technical terms. See [Simple English Wikipedia](https://en.wikipedia.org/wiki/Simple_English).

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
