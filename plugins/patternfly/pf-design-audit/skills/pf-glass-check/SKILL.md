---
name: pf-glass-check
description: Implement and audit PatternFly Glass Mode screens using the Glass Mode handbook. Use whenever a user mentions Glass Mode while building, generating, editing, or reviewing PatternFly screens, UIs, or prototypes, including Project Felt with glass. Prevent nested glass, preserve default card styling with optional isPlain, and apply accessibility and background image rules from the start.
---

### Objective

Apply the PatternFly Glass Mode handbook before writing new React, HTML, or CSS, and audit existing implementations against it. Keep default card styling unless the user requests plain styling; `isPlain` is optional for children on glass surfaces. Report every violation with its location, severity, and a corrected code example. The most damaging mistake — and the one to flag first — is layering glass on glass by adding `isGlass` to child components inside a container that already has glass enabled.

### Rules

Whenever the user requests Glass Mode for a new or existing PatternFly screen, load this skill and read [references/glass-handbook.md](references/glass-handbook.md) before generating or changing code. Do not wait for an explicit audit request. Use the handbook to guide implementation as well as review. Apply the rules defined in the **Audit Rules** section, checking in severity order: CRITICAL first, then HIGH, MEDIUM, LOW. Report violations using the output format below.

### Quick Reference: Auto-glass vs. manual-glass

| Category | Components | How glass is applied |
|----------|-----------|---------------------|
| **Auto-glass** | Page, Masthead, Navigation, Login page | Automatically receive glass when `.pf-v6-theme-glass` is on `<html>` |
| **Manual-glass** | Card, Hero, Panel | Accept the `isGlass` prop — but ONLY when they are NOT inside an auto-glass or manually-glass container |
| **Glass-surface children** | Card, Hero, Panel | Keep default styling. Optional `isPlain` removes backgrounds and borders on components that support it when the user requests a plain appearance |

### Drawer Rules

- Overlay drawers cover content: never use `isGlass`, even outside a glass parent. Keep the floating background.
- Inline drawers inside glass parents: use `<Drawer isInline>` with `<DrawerPanelContent isPlain>`, no `isGlass`, and no custom panel background or `isNoPlainOnGlass` override.
- Drawer styling props belong on `DrawerPanelContent`, not `Drawer`. These rules take precedence over optional plain styling for cards.

### Output Format

For an audit, use the report below. For implementation work, deliver the code and briefly summarize the glass decisions and validation; use this report only for unresolved violations. Missing `isPlain` on cards is not a violation and must not increase the violation count. Inline drawer panels inside glass parents must use `isPlain` (HIGH-2). Include only applicable key actions.

For every violation found, provide:

**Header:**
```
## Glass Mode Violations Found: {count}
```

**Per violation:**
```
### {n}. [{severity}] {rule-id}: {rule-name}

- **File:** `{path}`
- **Line:** {number}
- **Component:** `{component-name}`
- **Issue:** {one-sentence description of what's wrong}
- **Fix:**
  ```tsx
  // Before
  {current code}

  // After
  {corrected code}
  ```
```

**Summary:**
```
## Summary

| Severity | Count |
|----------|-------|
| CRITICAL | {n} |
| HIGH | {n} |
| MEDIUM | {n} |
| LOW | {n} |

### Key actions
1. Remove `isGlass` from all components inside glass-enabled containers
2. Preserve default card styling; apply optional `isPlain` only when requested
3. Verify Drawer variant matches glass context (overlay = no `isGlass`, floating background; inline inside glass = `DrawerPanelContent isPlain`)
4. Add `prefers-reduced-transparency` and `prefers-contrast` media query support
5. Replace hardcoded glass-related CSS values with glass design tokens
```

### Implementation Workflow

1. Read the handbook before implementing a screen whose prompt includes Glass Mode.
2. Establish theme enablement and identify automatic and manual glass surfaces before choosing child props.
3. Use default cards on glass surfaces without `isGlass` or `isPlain`. If the user requests plain cards, use `isPlain`; preserve an existing explicit styling choice when editing. Do not pause to ask about default versus plain. Mention plain styling as an available option without requiring a choice or adding a UI toggle unless requested.
4. Apply the handbook's drawer, accessibility, token, and background rules while writing the code.
5. Review the resulting component tree and theme styles against the audit rules before delivering the screen.

### Audit Workflow

1. Establish the glass context — is `.pf-v6-theme-glass` active? Which containers have `isGlass`?
2. Build the component tree and identify glass surfaces
3. Scan every component for CRITICAL-1 and HIGH violations first
4. Scan CSS/SCSS for MEDIUM and LOW violations
5. Report violations in severity order with corrected code examples
6. Provide a summary with prioritized actions

### File Type Support

- **React/JSX/TSX** — Component tree analysis for `isGlass`, `isPlain` props and nesting
- **HTML** — `.pf-v6-theme-glass` class detection, inline style scanning
- **CSS/SCSS** — Glass token usage, media query coverage, background image overrides

### Exception Handling

**Do NOT flag:**
1. Standalone `isGlass` outside a glass-enabled container is not nested glass; overlay drawers are still prohibited from using it (HIGH-2)
2. Components in test files or mock data (unless explicitly requested)
3. Glass tokens referenced via `var(--pf-t--...)` syntax
4. Default PatternFly background images (only flag custom overrides)
5. Code inside comments
6. Cards, Hero, and Panel without `isPlain` — default styling is valid and preferred for new cards; this exception does not apply to inline drawer panels inside glass parents
7. Children with `isPlain` — explicitly chosen plain styling is also valid

### Decision Table

Quick-reference for component prop scanning. For drawer rows, `isGlass` and `isPlain` refer to `DrawerPanelContent`; determine overlay versus inline from the enclosing `Drawer`. Report nested overlay glass as CRITICAL-1, otherwise as HIGH-2, without duplicating the same finding.

| Component | On glass surface? | Has `isGlass`? | Has `isPlain`? | Result |
|-----------|-------------------|----------------|----------------|--------|
| Card, Hero, Panel | Yes | Yes | — | Violation: CRITICAL-1 |
| Card, Hero, Panel | Yes | No | No | Pass (preferred default styling; no prompt needed) |
| Card, Hero, Panel | Yes | No | Yes | Pass |
| Card, Hero, Panel | No | Yes | — | Pass (valid standalone use) |
| Card, Hero, Panel | No | No | — | Pass |
| Drawer (overlay) | Yes | Yes | — | Violation: CRITICAL-1 |
| Drawer (overlay) | No | Yes | — | Violation: HIGH-2 |
| Drawer (overlay) | — | No | — | Pass if floating background is preserved |
| Drawer (inline) | Yes | Yes | — | Violation: CRITICAL-1 |
| Drawer (inline) | Yes | No | No | Violation: HIGH-2 (plain panel required) |
| Drawer (inline) | Yes | No | Yes | Pass if no custom background or plain-disabling override |
| Drawer (inline) | No | — | — | Check standalone theme and styling context |
