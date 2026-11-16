# Icon and geometry audit

Use this reference for fixed-size Figma replicas and any task where the user provides side-by-side screenshots.

The IDs, names, dimensions, and paths below are illustrative placeholders. Replace them with values resolved from the current Figma source; do not reuse them across projects.

## State matrix

Create one row per reference frame or screenshot:

| State key | Figma node ID | Frame name | viewport | scale | scroll | visible condition |
|---|---|---|---|---|---|---|
| `state-a` | `123:456` | `Example frame` | `<sourceWidth>×<sourceHeight>` | `2x` | `0,0` | initial/placeholder state |

The HTML must expose the same state deterministically, through a route, query parameter, fixture, or a documented interaction path. Never use a filled or modified state to validate a blank Figma frame.

### Source identity lock

For each row, also keep the exact supplied URL node and its resolved identity:

| state key | supplied node ID | resolved frame name | parent/page | source kind | preview URL |
|---|---|---|---|---|---|
| `state-a` | `123:456` | `Example frame` | `Example page / variant A` | `FRAME` | `?state=state-a` |

Do not replace the supplied node with a sibling that merely has the same name or dimensions. If a parent contains multiple role branches or repeated Frames, keep each branch as a separate baseline.

### Fixture assertions

Before capture, assert the exact visible text sequence for high-salience and repeated content, tab count/order when present, repeated item/step count, selected controls, enabled/disabled controls, overlay visibility, and sticky/fixed-control bounds when present. A real data value is not evidence that the control is visually selected; fixtures must distinguish `placeholder`, `selected`, `default data`, and `disabled`. A blank or placeholder field may coexist with a checked radio, selected tab, selected option, or enabled control; do not collapse those into one global empty state.

## Stepper, timeline, and process-flow geometry

Treat a process flow as a compound visual with independent source layers, not as a generic vertical list. This applies to confirmation flows, progress steps, timelines, approval chains, and any source containing step circles plus connector lines.

- Inventory every step node and every connector segment separately. Record each node's source ID, natural bounds, fill/ring state, stroke width, and z-order, plus each connector's source ID, endpoints, width, color, cap/join behavior, and clipping.
- Preserve the source's state segmentation: a completed or active segment may be purple while a pending or disabled segment is gray. Never replace mixed-state segments with one continuous line whose color is inferred from the first or last node.
- Prefer the exact Figma exports for `Progress-step item`, connector/path, and related compound assets when available. A CSS circle, pseudo-element, border, text glyph, or hand-drawn approximation is not an acceptable substitute for an available source asset.
- If the source exposes vector connector geometry rather than an exportable asset, recreate each segment from its measured source bounds. Anchor the line to the node centers, render it behind the nodes, and preserve segment-specific color and length; do not draw a single line from the first node to the last.
- Keep node size, inner dot size, ring thickness, connector width, and gaps as explicit fixture values. Do not normalize siblings that intentionally differ by state.
- Add fixture assertions for node count, connector count, active/selected/pending node, per-segment color, and the visible text attached to each step. A page can have correct copy and still fail if the stepper geometry or state colors are wrong.
- Verify the compound in isolation and in its parent frame. A source-backed parent export is acceptable only when it preserves the same composition and the steps do not need independent interaction or state changes.

## Geometry manifest

Record the source bounds in CSS pixels, not only screenshot pixels. At minimum include:

- screen/frame: `x, y, width, height`, background fill;
- visible system/application chrome as separate regions (for example status/navigation bars, header, top navigation, or sidebar);
- visible navigation and utility controls (for example back, title, overflow/menu, search, or account controls);
- content wrapper and every nested card/panel, including fills and insets;
- first and last visible text baseline;
- repeated row/card bounds and spacing;
- sticky/fixed control bounds and safe-area indicators when present;
- scroll viewport, clipping boundaries, and overlay bounds when present.

For high-salience anchors in a fixed replica, target rendered geometry within approximately 2 CSS px when the source font and assets are available. If the font is unavailable, separate font-metric differences from layout differences and report them instead of silently compensating with arbitrary margins.

## Icon inventory

Every visible icon gets one inventory row:

| icon | Figma node ID | source | local path | natural size/viewBox | rendered slot | state |
|---|---|---|---|---|---|---|
| example-icon | `123:789` | Figma SVG export | `assets/icons/example.svg` | source-resolved | source-resolved slot | `state-a` |

Rules:

1. Prefer the exact Figma SVG export for icons, system chrome, logos, arrows, status indicators, and simple vector illustrations.
2. Save it locally with a stable relative path and verify it is non-empty before delivery.
3. Preserve the SVG root `width`, `height`, and `viewBox`; size the callsite to the measured rendered slot. Do not force all SVGs to `100% × 100%`.
4. Do not replace an available SVG with text glyphs, emoji, icon fonts, CSS borders, pseudo-elements, gradients, or a hand-drawn approximation.
5. If a Figma icon cannot be exported or read, classify it as `PENDING`, explain the fidelity impact, and request approval before substituting.
6. Audit both the asset and the callsite: the file, node mapping, import/reference, rendered bounds, and optical alignment must all be checked.
7. Inspect CSS `::before`/`::after`, text glyphs, and generated content for visual substitutes. If the source asset exists, a glyph or CSS drawing fails the audit even when the browser screenshot looks approximately correct.

### Compound asset inventory

Some visible regions are groups rather than single assets. Record the parent group and every rendered child:

| group | parent node ID | child node IDs | local paths | relative bounds/opacity | composed slot | state |
|---|---|---|---|---|---|---|
| composite-visual | `987:654` | child-a, child-b, child-c | `assets/visuals/composite/*.svg` | measured per child | `x,y,w×h` | `state-a` |

Verify each rendered asset, its callsite, and the composed bounds. A faithful source-backed parent export is suitable for a static compound when it preserves the source composition; keep layers separate when they must animate, change state or retain independent clipping. Do not replace a compound with an approximate drawing.

## Comparison order

When a diff is visible, inspect in this order:

1. state parity and viewport scale;
2. outer frame and chrome geometry;
3. content wrapper/card/background boundaries;
4. sticky/fixed controls and safe-area spacing when present;
5. source-backed icons and their slot positions;
6. text metrics, line breaks, colors, and micro-spacing.

Do not tune typography or icon offsets before correcting a wrong state or an extra wrapper/card. Those structural errors make every local measurement misleading.
