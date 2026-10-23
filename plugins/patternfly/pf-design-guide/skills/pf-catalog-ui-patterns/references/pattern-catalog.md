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

## When to split this file

This file currently holds the entry schema and every cataloged pattern inline. That's fine while entries are sparse — don't split preemptively. Split once either:

- This file exceeds roughly 400–500 lines (the same soft ceiling `validate-skills.sh` hard-enforces on `SKILL.md`), or
- Any single category accumulates 2+ full entries.

When that threshold hits, split **by category**, not by extracting code out of entries — follow the precedent in `pf-component-check`'s `references/*.md` files (one file per family, plus a thin routing table in `SKILL.md`). Keep each entry's schema fields and `Composition` code together in the same file; the code is governed by that entry's own `Variants` table (e.g., `severity.icon`, `requiresCheckbox`), so separating them risks the two drifting out of sync silently. Move each category's full entries into its own `references/<category>.md` file, then replace the inline `## Categories` section below with a thin index table: `Pattern name | Category | Problem it solves | File` — the "Problem it solves" column is what matching already runs against, so the index alone stays enough to match a need without opening an entry file.

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
- **Required components**: `WarningModal` (from `@patternfly/react-component-groups`) as the default — it wraps `Modal` and accepts all of `Modal`'s own props, so nothing below is lost, while also layering Confirm/Cancel wiring, button variant, and the checkbox-or-typed-confirmation safeguard on top so none of that needs hand-rolling; `List`/`ListItem` (or `DescriptionList`) with `Badge` counts, passed as `WarningModal`'s `children`, to enumerate affected downstream resources on cascade/ripple deletes. **Fallback**, only for codebases not already depending on `@patternfly/react-component-groups`: hand-roll from `Modal` (`ModalHeader`, `ModalBody`, `ModalFooter`), `Button`, and `Checkbox` directly — see the fallback composition below. Choosing the fallback over the default is a deviation to flag per the skill's default-first policy (state the reason, e.g., avoiding the extra dependency), not a silent substitution.
- **Composition**:

  ```tsx
  <WarningModal
    variant="small"
    isOpen={isOpen}
    title={headline}
    titleIconVariant={severity.icon}
    confirmButtonLabel={confirmLabel}
    confirmButtonVariant={severity.buttonVariant}
    cancelButtonLabel="Cancel"
    onConfirm={onConfirm}
    onClose={onClose}
    // Permanent/irreversible, lower blast radius
    withCheckbox={requiresCheckbox}
    checkboxLabel={acknowledgementLabel}
    // Permanent/irreversible, high blast radius — use instead of withCheckbox, not alongside it
    confirmationInputProps={requiresTypedConfirmation ? { type: 'text', isRequired: true } : undefined}
    confirmationText={requiresTypedConfirmation ? resourceName : undefined}
  >
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
  </WarningModal>
  ```

  Fallback composition (no `@patternfly/react-component-groups` dependency) — same required behavior, hand-rolled from `Modal` primitives:

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

      {/* Permanent/irreversible, lower blast radius only */}
      {requiresCheckbox && (
        <Checkbox
          id="confirm-delete"
          label={acknowledgementLabel}
          isChecked={checked}
          onChange={(_e, isChecked) => setChecked(isChecked)}
        />
      )}

      {/* Permanent/irreversible, high blast radius only — in place of the checkbox above */}
      {requiresTypedConfirmation && (
        <TextInput
          id="confirm-delete-text"
          value={typedValue}
          onChange={(_e, value) => setTypedValue(value)}
          placeholder={resourceName}
        />
      )}
    </ModalBody>
    <ModalFooter>
      <Button
        variant={severity.buttonVariant}
        isDisabled={(requiresCheckbox && !checked) || (requiresTypedConfirmation && typedValue !== resourceName)}
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

  Severity and safeguard (from PatternFly's "Confirm a destructive action" guidance, plus `WarningModal`'s own built-in safeguard mechanisms):

  | Severity | When | Title icon | Confirm button | Safeguard |
  |---|---|---|---|---|
  | Non-destructive / reversible | Disabling, unassigning, canceling | None | `primary` | None |
  | Destructive but reversible | Removing something risky to lose track of | `warning` | `danger` | None |
  | Permanent / irreversible | Hard delete | `warning` | `danger` | Checkbox (`withCheckbox` + `checkboxLabel`) — Confirm stays disabled until checked |
  | Permanent / irreversible, high blast radius | Deleting something that cascades broadly, or affects other users/environments (e.g., a production environment, an entire account) | `warning` | `danger` | Typed confirmation (`confirmationInputProps` + `confirmationText`) instead of a checkbox — a checkbox is too easy to dismiss without reading at this blast radius |

  Downstream-impact (orthogonal to severity — combine as needed):

  - **Simple**: No downstream effects. Body text states only what's being deleted.
  - **Cascade**: Deleting this resource also deletes other resources. List each affected type with a count under a "Resources that will be deleted" heading.
  - **Ripple**: Deleting this resource breaks or orphans other resources without deleting them. Same list treatment under a "Resources that will be affected" heading.
  - A resource can be both cascade and ripple at once — show both lists.

- **Do not deviate on**:
  - The checkbox-gated Confirm button for permanent/irreversible deletes, or typed-confirmation-gated for high-blast-radius ones — don't let users skip the safeguard on a hard delete, and don't use both safeguards at once (pick one per the severity table).
  - `titleIconVariant="warning"` on any destructive confirmation — irreversible actions must be visually flagged per PatternFly's guidance.
  - `danger` confirm button variant (`confirmButtonVariant` on `WarningModal`, or the `Button` `variant` on the fallback) for destructive confirms.
  - Naming the specific downstream resources/counts on cascade or ripple deletes — a bare "Are you sure?" is insufficient once other resources are affected.
- **Adaptable by default**:
  - Exact headline/body copy, as long as the action verb stays consistent with the triggering button (per PatternFly's content guidance).
  - Modal size — `small` is typical; use `medium` if body content needs more room (e.g., long affected-resource lists).
  - Whether impact is shown as a list with badge counts vs. plain descriptive text, when counts aren't available.
- **Source**: PatternFly [Modal design guidelines](https://www.patternfly.org/components/modal/design-guidelines) → "Confirmation modals" (`patternfly://docs/modal`) for the severity/icon/button guidance. The default composition itself is sourced from `WarningModal`'s own docs (`@patternfly/react-component-groups`, `patternfly://docs/extensionscomponentgroupswarningmodal`), confirmed live: it explicitly documents accepting all `Modal` props plus `withCheckbox`/`checkboxLabel` and `confirmationInputProps`/`confirmationText` as its two safeguard mechanisms — which is also what resolved this entry's earlier open "`Modal` vs. `WarningModal`" question in `WarningModal`'s favor as the default, not just an alternative.
- **Provenance**: Observed in Syntara's `frontend-patternfly-ux` skill (confirmation-modal section, originally built on a custom `SynConfirmationDialog`). This is currently the only confirmed source — not yet validated against other products. Upstream status: not proposed (see `/tmp/patternfly-modal-confirmation-contribution-draft.md` for a drafted, not-yet-submitted proposal covering the severity/checkbox guidance). If this composition turns up independently in another product, update this field rather than assuming it already applies broadly.

  **Why this entry still earns its place even if parts of it get upstreamed:** The icon/button-variant-by-severity row and "use a safeguard step for permanent deletes" are generalizable PatternFly guidance worth contributing upstream (PatternFly's own Modal docs already gesture at this loosely). But the three-tier severity *naming*, the cascade/ripple downstream-impact taxonomy, and the high-blast-radius-vs-checkbox distinction are product-specific conventions layered on top of PatternFly's intentionally general, multi-valid-approach guidance — PatternFly's docs shouldn't (and realistically wouldn't) mandate one taxonomy for every consumer. Docs are reference material someone has to rediscover and choose to apply each time; this entry is what makes applying it the default instead of optional. If PatternFly's docs ever grow to fully specify the severity/impact taxonomy as one ready recipe, re-run this entry through the [synthesis test](#before-adding-an-entry-the-synthesis-test) — it may by then qualify for the same removal `pf-catalog-ui-patterns` gave the "Empty state selection" entry.

<!--
Considered and deliberately NOT added: "Empty state selection" (EmptyState icon/status/variant-per-scenario
mapping). It failed the synthesis test above — it restated EmptyState's own documented icon table almost
verbatim with no multi-component synthesis, so it's one component's own usage guidance, not a pattern. For
that need, fetch `patternfly://docs/emptystate` directly (via PatternFly MCP) or rely on `pf-coding-standards`
— don't re-add it here unless it grows real cross-component synthesis beyond EmptyState's own API.
-->
