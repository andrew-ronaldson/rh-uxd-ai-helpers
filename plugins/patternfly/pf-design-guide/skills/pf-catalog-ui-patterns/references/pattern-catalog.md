# PatternFly UI Pattern Catalog (reference)

This catalog mirrors PatternFly's official **Patterns** documentation (`patternfly://docs/patterns`, patternfly.org/patterns) — reusable, best-practice compositions of multiple components that solve one recurring UI problem.

**This file is scaffolding only.** The category skeleton below exists so entries can be added later; none have been written yet. Do not treat an empty category as "no pattern exists" — it means the pattern hasn't been cataloged here yet, not that PatternFly has no guidance for it. Check `patternfly://docs/patterns` or patternfly.org/patterns directly until an entry is added.

## Before adding an entry: the synthesis test

This catalog's enforcement model (see `pf-catalog-ui-patterns`'s default-first policy) only makes sense for content that's genuinely a *pattern* — not for content that's really just one component's own docs restated. Restating a single component's docs here creates a second copy that can silently go stale while still being enforced as a rule, and it duplicates what `patternfly://docs/*` (via PatternFly MCP) and `pf-coding-standards` already cover live.

Before adding an entry, check it against all of the following. If it fails any one, it's not catalog-worthy as written:

1. **Synthesizes, doesn't restate** — does it combine 2+ independently-documented components/subsystems into a composition that isn't spelled out as one ready recipe anywhere in PatternFly's own docs? If it's really one component's own prop/variant table in different words, it fails this check.
2. **Adds judgment PatternFly's docs don't give** — does it carry a decision tree, severity model, or "when to deviate" logic layered on top of PatternFly's primitives, rather than just mapping a prop to a value?
3. **Drift-safe to enforce** — if PatternFly changes the underlying component's docs, does this entry's value survive that change (because it's judgment/composition), or does it become silently wrong (because it was a copy of a specific table)?
4. **Not already covered by the fallback** — would an agent already reach the correct answer by fetching PatternFly MCP docs directly or following `pf-coding-standards`, without this entry existing? If yes, the entry adds maintenance surface without adding capability.

If something fails this test but still seems worth capturing, prefer a short pointer (component name + `patternfly://docs/...` URI) over a full restated entry.

If an entry is sourced from a downstream product's own convention rather than from PatternFly's docs, fill in `Provenance` with only what's actually known — the product(s) it's been observed in, and nothing claimed beyond that. There's no way to centrally verify how many products use a given composition, so don't infer or imply broader cross-product adoption than what's been directly confirmed. A single-source entry is still catalog-worthy if it passes the synthesis test above; it's just honest about its evidence.

## Entry schema

Each pattern entry must include all of the following fields:

| Field | Purpose |
|---|---|
| **Name** | Matches the official PatternFly pattern name exactly. |
| **Problem it solves** | The UI need in one sentence — this is what a described need gets matched against. |
| **Trigger phrases** | Example user descriptions that should match this pattern, so matching works even when the user doesn't name the pattern (e.g., "let users pick several rows and act on them" → Bulk selection). |
| **Required components** | The components that make up the default composition, each with its role. |
| **Composition** | A structural skeleton (component tree or markup shape) showing how the required components fit together. |
| **Variants** | PatternFly-approved variations of the pattern and when to use each. |
| **Do not deviate on** | The parts of the pattern that are structural or accessibility-load-bearing — changing these counts as a deviation that must be flagged per the skill's default-first policy. |
| **Adaptable by default** | The parts a user can customize (labels, icon choice, column content, etc.) without it counting as a deviation from the pattern. |
| **Source** | Link to the official PatternFly pattern doc the entry was sourced from. |
| **Provenance** | Which product(s) this composition has been directly observed in, and its upstream-proposal status (not proposed / drafted / submitted / accepted into PatternFly docs). Record only what's confirmed — don't imply cross-product adoption beyond what's actually known. |

### Entry template

```markdown
#### [Pattern name]

- **Problem it solves**:
- **Trigger phrases**:
- **Required components**:
- **Composition**:
- **Variants**:
- **Do not deviate on**:
- **Adaptable by default**:
- **Source**:
- **Provenance**:
```

## Categories

Categories mirror `patternfly://docs/patterns`. Add new categories here as PatternFly publishes more patterns, or as this catalog deliberately expands beyond PatternFly's official pattern pages (e.g., wizards, empty states) — see [Contributing patterns](../SKILL.md#contributing-patterns) in the skill file before adding anything that isn't sourced from PatternFly's own docs.

### Actions

_No patterns added yet._

### Bulk selection

_No patterns added yet._

### Card view

_No patterns added yet._

### Component usage and behavior

_No patterns added yet._

### Dashboard

_No patterns added yet._

### Filters

_No patterns added yet._

### Primary-detail

_No patterns added yet._

### Status and severity

_No patterns added yet._

## Extended categories

These categories are not among PatternFly's 8 official `patternfly://docs/patterns` pages. An entry can land here through either of two legitimate paths:

1. **Grounded in other official PatternFly documentation** — component design guidelines, accessibility docs, or an official `@patternfly/react-component-groups` component — that doesn't have its own dedicated Patterns page.
2. **Observed in one of our own products as a recurring composition** worth standardizing across the org, documented here as a default pending (or regardless of) adoption into PatternFly's own docs. See `Provenance` on the entry — single-source entries are still valid, just honest about what's confirmed.

Either way, extend this section deliberately, not casually — per [Contributing patterns](../SKILL.md#contributing-patterns), new entries are added one at a time, in their own PR, as real needs arise. Don't bulk-populate this catalog speculatively.

### Confirmation modals

Sourced from PatternFly's [Modal design guidelines](https://www.patternfly.org/components/modal/design-guidelines) ("Confirmation modals" / "Confirm a destructive action") rather than a dedicated Patterns page.

#### Destructive confirmation modal

- **Problem it solves**: Before a user deletes, removes, disables, or otherwise acts on a resource with real consequences, confirm the action and communicate what will happen — scaled to how severe and reversible the action is.
- **Trigger phrases**: "confirm before deleting", "are you sure modal", "delete confirmation", "warn the user before removing/disabling X", "make the user acknowledge this is permanent"
- **Required components**: `Modal` (`ModalHeader`, `ModalBody`, `ModalFooter`) with `titleIconVariant`; `Button` for Confirm/Cancel; `Checkbox` for the acknowledgment step on permanent deletes; `List`/`ListItem` (or `DescriptionList`) with `Badge` counts to enumerate affected downstream resources on cascade/ripple deletes.
- **Composition**:

  ```tsx
  <Modal variant="small" titleIconVariant={severity.icon} onClose={onClose}>
    <ModalHeader title={headline} />
    <ModalBody>
      {bodyText}

      {/* Cascade/ripple only */}
      {affectedResources.length > 0 && (
        <>
          <Content component="h4">{affectedHeading}</Content>
          <List isPlain>
            {affectedResources.map((r) => (
              <ListItem key={r.type}>
                {r.label} <Badge isRead>{r.count}</Badge>
              </ListItem>
            ))}
          </List>
        </>
      )}

      {/* Permanent/irreversible delete only */}
      {requiresAcknowledgement && (
        <Checkbox
          id="confirm-delete"
          label={acknowledgementLabel}
          isChecked={checked}
          onChange={(_e, isChecked) => setChecked(isChecked)}
        />
      )}
    </ModalBody>
    <ModalFooter>
      <Button
        variant={severity.buttonVariant}
        isDisabled={requiresAcknowledgement && !checked}
        onClick={onConfirm}
      >
        {confirmLabel}
      </Button>
      <Button variant="link" onClick={onClose}>
        Cancel
      </Button>
    </ModalFooter>
  </Modal>
  ```

- **Variants**:

  Severity (from PatternFly's "Confirm a destructive action" guidance):

  | Severity | When | Title icon | Confirm button | Checkbox |
  |---|---|---|---|---|
  | Non-destructive / reversible | Disabling, unassigning, canceling | None | `primary` | No |
  | Destructive but reversible | Removing something risky to lose track of | `warning` | `danger` | No |
  | Permanent / irreversible | Hard delete | `warning` | `danger` | Required — Confirm button stays disabled until checked |

  Downstream-impact (orthogonal to severity — combine as needed):

  - **Simple**: No downstream effects. Body text states only what's being deleted.
  - **Cascade**: Deleting this resource also deletes other resources. List each affected type with a count under a "Resources that will be deleted" heading.
  - **Ripple**: Deleting this resource breaks or orphans other resources without deleting them. Same list treatment under a "Resources that will be affected" heading.
  - A resource can be both cascade and ripple at once — show both lists.

- **Do not deviate on**:
  - The checkbox-gated Confirm button for permanent/irreversible deletes — don't let users skip acknowledgement on a hard delete.
  - `titleIconVariant="warning"` on any destructive confirmation — irreversible actions must be visually flagged per PatternFly's guidance.
  - `danger` button variant for destructive confirms.
  - Naming the specific downstream resources/counts on cascade or ripple deletes — a bare "Are you sure?" is insufficient once other resources are affected.
- **Adaptable by default**:
  - Exact headline/body copy, as long as the action verb stays consistent with the triggering button (per PatternFly's content guidance).
  - Modal size — `small` is typical; use `medium` if body content needs more room (e.g., long affected-resource lists).
  - Whether impact is shown as a list with badge counts vs. plain descriptive text, when counts aren't available.
- **Source**: PatternFly [Modal design guidelines](https://www.patternfly.org/components/modal/design-guidelines) → "Confirmation modals" (`patternfly://docs/modal`). The same severity/checkbox composition is also available pre-built as `WarningModal` from `@patternfly/react-component-groups` (`withCheckbox`, `checkboxLabel`, `confirmButtonVariant` props) for teams that prefer not to hand-roll from `Modal` primitives — note this as a deviation from the primitive composition above if used instead, since it changes the required-components list.
- **Provenance**: Observed in Syntara's `frontend-patternfly-ux` skill (confirmation-modal section, originally built on a custom `SynConfirmationDialog`). This is currently the only confirmed source — not yet validated against other products. Upstream status: not proposed (see `/tmp/patternfly-modal-confirmation-contribution-draft.md` for a drafted, not-yet-submitted proposal covering the severity/checkbox guidance). If this composition turns up independently in another product, update this field rather than assuming it already applies broadly.

  **Why this entry still earns its place even if parts of it get upstreamed:** The icon/button-variant-by-severity row and "use a safeguard step for permanent deletes" are generalizable PatternFly guidance worth contributing upstream (PatternFly's own Modal docs already gesture at this loosely). But the three-tier severity *naming*, the cascade/ripple downstream-impact taxonomy, and the choice of raw `Modal` vs. `WarningModal` as this codebase's standard are product-specific conventions layered on top of PatternFly's intentionally general, multi-valid-approach guidance — PatternFly's docs shouldn't (and realistically wouldn't) mandate one taxonomy for every consumer. Docs are reference material someone has to rediscover and choose to apply each time; this entry is what makes applying it the default instead of optional. If PatternFly's docs ever grow to fully specify the severity/impact taxonomy as one ready recipe, re-run this entry through the [synthesis test](#before-adding-an-entry-the-synthesis-test) — it may by then qualify for the same removal `pf-catalog-ui-patterns` gave the "Empty state selection" entry.

<!--
Considered and deliberately NOT added: "Empty state selection" (EmptyState icon/status/variant-per-scenario
mapping). It failed the synthesis test above — it restated EmptyState's own documented icon table almost
verbatim with no multi-component synthesis, so it's one component's own usage guidance, not a pattern. For
that need, fetch `patternfly://docs/emptystate` directly (via PatternFly MCP) or rely on `pf-coding-standards`
— don't re-add it here unless it grows real cross-component synthesis beyond EmptyState's own API.
-->
