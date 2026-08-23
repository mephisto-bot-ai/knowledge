---
title: "Karpathy LLM Wiki Pattern"
type: concept
status: active
created: 2026-08-23
updated: 2026-08-23
tags: [karpathy, llm-wiki, knowledge-base, pattern]
tier: core
confidence: 0.95
review_after: 2026-11-23
related: []
wikidata:
source_aliases:
---

# Karpathy LLM Wiki Pattern

## Current Conclusion

The Karpathy LLM Wiki Pattern is a way to build a knowledge base that grows over time. It uses three layers: raw sources, wiki pages, and a schema file. An AI agent reads the schema, writes wiki pages from sources, and updates the index. The knowledge base gets better each time the agent runs.

## Definition

Andrej Karpathy shared this pattern as a [GitHub gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). The idea is simple: instead of asking an LLM to answer the same questions again and again, you let it build a wiki. Each time it learns something new, it writes it down. Next time, it reads the wiki first.

## Key Claims

- The pattern has three layers: raw, wiki, schema
- The schema file (like AGENTS.md) tells the agent what to do
- Raw sources are never changed after they are saved
- Wiki pages are owned and updated by the LLM
- The knowledge base compounds over time

## Evidence

| Claim | Source | Evidence type | Confidence |
|-------|--------|--------------|------------|
| Three layers: raw, wiki, schema | [Karpathy gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) | primary | 0.95 |
| Raw sources are immutable | [Karpathy gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) | primary | 0.95 |
| Knowledge compounds over time | [Karpathy gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) | primary | 0.90 |

## Interpretation / Analysis

The pattern works because it separates three things:
1. **What we know** (wiki pages) — can change as we learn more
2. **Where we learned it** (raw sources) — never changes
3. **How we work** (schema) — the rules the agent follows

This separation means the agent can always check its sources. It can update its conclusions without losing the original evidence.

## Open Questions

- How to handle sources that change over time?
- What is the best way to search a wiki like this?
- How to handle conflicts between sources?

---

## Evidence Timeline

- 2026-08-23: Initial version. (reason: Example entry for knowledge base, written in Simple English)
