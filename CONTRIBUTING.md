# Contributing

See [AGENTS.md](AGENTS.md) for the complete schema, rules, and workflows.

## Quick Summary

1. Read `AGENTS.md` for the full guide.
2. Search `index.md`, `claims/registry.yaml`, `gaps/registry.yaml`, and `conflicts/registry.yaml` before starting.
3. Claim an open gap when the work addresses a known missing, weak, stale, or disputed topic.
4. Use templates from `_templates/` and write content in Simple English.
5. Give every independently checkable factual statement a stable claim ID and evidence record.
6. Record duplicates and disagreements instead of silently deleting older knowledge.
7. Run `python scripts/validate_knowledge.py` before opening a PR.
8. Never include secrets or internal infrastructure details.
9. Open a PR — never push directly to main.

## Review model

A research agent may propose sources and claims, but an independent reviewer should check important claims and conflicts. The PR description must state whether each claim is new, updated, superseded, duplicated, or disputed. A conflict may remain unresolved when the evidence is genuinely mixed, but it must be recorded with the competing claim IDs and the reason no final resolution was made.
