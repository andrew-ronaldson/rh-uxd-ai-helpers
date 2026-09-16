---
name: pf-glass-standards
description: PatternFly Glass Mode standards — glass-on-glass prevention, default card styling with optional isPlain, Drawer variant rules, accessibility overrides, and background image rules. Active when building, generating, or prototyping glass-enabled PatternFly UIs.
---

# PatternFly Glass Mode Standards

Enforce Glass Mode handbook rules when generating PatternFly UI code. These standards apply whenever `.pf-v6-theme-glass` is active or the user requests glass mode, Project Felt with glass, or a glass-enabled prototype.

Before generating or editing code when the user mentions Glass Mode, load `../skills/pf-glass-check/SKILL.md` and read `../skills/pf-glass-check/references/glass-handbook.md` (paths relative to this file). Apply them during implementation without waiting for an audit request.

## Core Principle

Glass is applied at the container level. Children on a glass surface never add their own glass — they either use their default styling (which already has reduced opacity in glass mode) or use `isPlain` to blend seamlessly. Prefer default styling for new cards; use plain styling when requested and preserve existing explicit choices.

## Quick Reference

| Category | Components | Behavior |
|----------|-----------|----------|
| **Auto-glass** | Page, Masthead, Navigation, Login page | Automatically receive glass when `.pf-v6-theme-glass` is on `<html>`. Never add `isGlass` to them or their children. |
| **Manual-glass** | Card, Hero, Panel | Accept `isGlass` prop ONLY when NOT inside an auto-glass or manually-glass container |

## Behavioral Guidance

### Default styling with optional plain

Use default cards inside glass-enabled containers, without `isGlass` or `isPlain`. Do not ask for confirmation before proceeding. If the user requests plain styling, use `isPlain` on supported components; preserve existing explicit styling choices when editing. Plain styling may be offered as an option without blocking the work or adding a UI toggle unless requested.

Missing `isPlain` on cards is not an audit violation. Inline drawer panels inside glass parents are an exception and must use `isPlain`. When correcting nested glass, remove the child's `isGlass` and retain its default styling unless the user has requested plain styling. Drawer backgrounds follow the rules below.

### Drawer variant selection

- **Overlay drawer** (covers content): Never use `isGlass`, regardless of parent. Preserve the floating background token.
- **Inline drawer inside a glass parent**: Use `<Drawer isInline>` with `<DrawerPanelContent isPlain>`. Do not use `isGlass`, custom panel background colors, or `isNoPlainOnGlass`. Styling props belong on `DrawerPanelContent`, not `Drawer`.

## Checklist for New Glass Prototypes

When starting a glass-enabled prototype, verify:

- [ ] `.pf-v6-theme-glass` on `<html>` (plus `.pf-v6-theme-felt` if using Felt)
- [ ] No `isGlass` on components inside auto-glass or manually-glass containers
- [ ] Default card styling used unless plain styling was requested; existing explicit choices preserved
- [ ] Drawers use correct variant: overlay (never `isGlass`, floating background) or inline inside glass (`DrawerPanelContent isPlain`)
- [ ] `prefers-contrast` and `prefers-reduced-transparency` media query handlers included
- [ ] No text placed directly on background images
- [ ] All glass styling uses design tokens, no hardcoded values
