---
name: pf-catalog-ui-patterns
version: 0.1.0
audience: "Developers and designers building PatternFly UIs"
inputs: "A described UI need or feature (e.g., \"let users select multiple rows and delete them\")"
outputs: "The required PatternFly pattern composition to build by default, an explicit deviation when the user overrides it, or confirmation that no cataloged pattern applies"
description: >-
  Enforce PatternFly's documented UI patterns as the required default
  composition for common interface needs, instead of assembling components
  from scratch each time. Use when building a feature, screen, or
  interaction that matches a cataloged pattern such as bulk selection,
  filtering, dashboards, or primary-detail views — only deviate when the
  user explicitly asks to.
---

# PatternFly UI Pattern Catalog

PatternFly documents **patterns**: reusable, best-practice compositions of multiple components that solve one recurring UI problem (for example, bulk selection, filters, dashboards, primary-detail views). This skill operates one level above component- and interaction-level guidance — it answers "what's the standard way to build this whole feature?" instead of "which component do I use?" (see `pf-catalog-interaction-patterns`) or "how do I style this component?" (see `pf-coding-standards`).

## Status: early draft

The catalog in `references/pattern-catalog.md` has one entry so far (Destructive confirmation modal, under Extended categories) plus the entry schema, the synthesis test entries must pass (see below), and the category skeleton for the rest. Most categories still have **no patterns entered yet** — for those, say so plainly and fall back to component-level guidance (`pf-catalog-interaction-patterns`, `pf-coding-standards`, PatternFly MCP) rather than improvising a "pattern" that isn't documented in the catalog.

Not everything that looks like PatternFly guidance belongs here — see [Contributing patterns](#contributing-patterns) below. An "Empty state selection" entry was proposed and deliberately rejected because it just restated `EmptyState`'s own icon/status table with no multi-component synthesis; `references/pattern-catalog.md` keeps a note on why, as a precedent for future entries.

## Default-first policy

This is the behavior that makes cataloged patterns **rules, not suggestions**, once they're populated:

1. **A matched pattern is the implementation, not one option among several.** If a described need matches a cataloged pattern, build that pattern's composition by default. Don't present it alongside alternative custom compositions as if they were equally valid.
2. **Don't ask permission to use the default.** Don't open with "would you like the standard pattern or a custom build?" — build the cataloged pattern, then let the user react.
3. **The user can always override.** If the user explicitly asks to deviate, adapt a part of the pattern, or has a constraint the pattern doesn't fit, follow their instruction.
4. **Never swap silently.** Every time the output differs from a cataloged pattern, say which pattern it deviates from and what changed, so the user can confirm or revert. Silent substitution defeats the point of having a default.
5. **No match is not a license to invent a "pattern."** If nothing in the catalog fits, state that clearly and fall back to standard component-level composition — don't force a mismatched pattern onto the need.
6. **Respect the schema's deviation boundaries.** Each catalog entry marks which parts are structural (`Do not deviate on`) versus freely customizable (`Adaptable by default`) — see the schema in `references/pattern-catalog.md`. Treat requests to change a structural part as a deviation that must be flagged, even if the user doesn't realize it's structural.

## PatternFly MCP

If `@patternfly/patternfly-mcp` is available, use it to confirm current props, examples, and version-specific details for the components a matched pattern requires — **after** selecting the pattern from this catalog, not instead of it.

## When to use this skill

- Building a feature that matches a known multi-component UI need (bulk select + act on rows, a filterable data view, a dashboard, a primary-detail layout, and so on).
- The user describes a UI need in behavioral terms rather than naming a pattern ("let users pick several rows and delete them").
- Reviewing whether an existing implementation reinvents something PatternFly already defines as a pattern.

## Pattern catalog

The catalog lives in `references/pattern-catalog.md`, organized by category mirroring PatternFly's official Patterns documentation (`patternfly://docs/patterns`): Actions, Bulk selection, Card view, Component usage and behavior, Dashboard, Filters, Primary-detail, Status and severity — plus an **Extended categories** section for patterns either grounded in other official PatternFly docs (e.g., Modal design guidelines) or observed as a recurring composition across our own products and standardized here ahead of (or regardless of) upstream adoption. Read that file for the entry schema and to check whether a category has any entries yet.

## Workflow

1. Match the described need to a category — and, once populated, a specific entry — in `references/pattern-catalog.md`. A single request can contain more than one need (e.g., a table plus a destructive action on its rows) — match each piece independently rather than forcing the whole request into one bucket.
2. **Entry found:** present that pattern's composition as what will be built, using the output format below. This is the default, not a proposal.
3. **Entry has multiple variants and the description doesn't fully specify which applies:** pick the more conservative/protective variant (the stricter severity tier, the safer behavior) and state that choice as an explicit assumption rather than a silent guess — an unstated pick is still a silent substitution under the "Never swap silently" rule. Don't block on asking first; state the assumption and keep going, inviting correction.
4. **User asks to deviate:** apply their instruction, but explicitly name the pattern and the specific deviation per the "Never swap silently" rule above.
5. **No entry or empty category:** state that no cataloged pattern applies, then fall back to component-level guidance (`pf-catalog-interaction-patterns`, `pf-coding-standards`, or PatternFly MCP) to assemble a composition.
6. **Composite need — part matches, part doesn't:** apply steps 2–5 to each piece independently in the same response (see the composite example in Output format below). Don't force a multi-part request into a single template, and don't let an unmatched part block presenting the part that did match.
7. **User disputes the match:** discuss the fit. Once they confirm a deviation or a fully custom approach, proceed with it while still naming what default was overridden.

## Output format

When a pattern matches:

```
## Using the [Pattern name] pattern (PatternFly default)

This need matches PatternFly's [Pattern name] pattern. Building with:
- [Component A] — [role in the composition]
- [Component B] — [role in the composition]

[Composition skeleton]

This is the default PatternFly approach for this need — tell me if you need to adapt it.
```

When deviating from a matched pattern:

```
## Deviating from the [Pattern name] pattern

Per your request, this differs from PatternFly's default [Pattern name] pattern: [what changed and why].

[Adapted composition]
```

When nothing in the catalog matches:

```
No cataloged PatternFly pattern matches this need yet. Falling back to component-level guidance to assemble a composition.
```

When the matched entry has variants the description doesn't fully pin down, name the assumed variant in the same template instead of silently picking one:

```
## Using the [Pattern name] pattern (PatternFly default)

This need matches PatternFly's [Pattern name] pattern. Building with:
- [Component A] — [role in the composition]
- [Component B] — [role in the composition]

Assuming [variant] since the description didn't specify — tell me if that's wrong.

[Composition skeleton]

This is the default PatternFly approach for this need — tell me if you need to adapt it.
```

When the request is composite — part of it matches a cataloged entry, part doesn't — combine the matched-entry and no-match templates in one response instead of forcing the whole thing into either:

```
## Using the [Pattern name] pattern (PatternFly default)

This need matches PatternFly's [Pattern name] pattern for [the matching part]. Building with:
- [Component A] — [role in the composition]

[Composition skeleton]

[The non-matching part] has no cataloged PatternFly pattern yet — building it with standard
component-level composition instead.
```

## Contributing patterns

Before adding an entry, run it through the **synthesis test** in `references/pattern-catalog.md#before-adding-an-entry-the-synthesis-test`: it must combine 2+ independently-documented things into a composition PatternFly's own docs don't already give as one recipe, not just restate one component's prop/variant table. Content that only restates a single component's docs belongs behind a live PatternFly MCP lookup or `pf-coding-standards`, not a static catalog entry — a static copy of someone else's docs will drift while still being enforced as a rule.

If an entry passes the test, add it to `references/pattern-catalog.md` following its schema — fill in every field, especially `Do not deviate on` / `Adaptable by default`, since the default-first policy above depends on that boundary being unambiguous. Source each entry from the official PatternFly pattern docs (`patternfly://docs/patterns`) rather than inventing new "patterns" that PatternFly hasn't documented, unless the team has deliberately decided to extend the catalog.

For entries sourced from a downstream product's own convention rather than PatternFly's docs, fill in `Provenance` honestly: name only the product(s) directly confirmed to use the composition. There's no way to verify from here how many products share a given pattern, so don't claim or imply broader adoption than what's actually known — a single-source entry is still valid as long as it passed the synthesis test.

Add entries one at a time, each in its own PR, as real needs arise. Don't batch-populate the catalog speculatively — a pattern earns its entry when it's actually encountered, not in anticipation of it.

## Evals

Deferred until the catalog has at least one populated entry — a lookup skill with an empty catalog has no discriminating behavior to test yet. Add an eval under `eval/` (see `pf-catalog-interaction-patterns/eval/` for the format) once real entries exist.
