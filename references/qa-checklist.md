# Visual and technical QA checklist

Check at the exact target viewport and exact target state. For `BASIC` or `FULL`, also check the source-appropriate reference matrix defined in `references/responsive-contract.md`.

For a prototype flow, check every in-scope screen/state inside the same source viewport and platform context. Do not compare the HTML against the full Figma canvas layout.

## Visual

- source identity lock: exact supplied node, resolved frame name, variant branch, and fixture route match;
- exact visible text sequence, repeated card/step/item count, and selected-control set match the source fixture;
- overall frame width and content height;
- visible page chrome (header, top/side navigation, status area, back control, logo, or fixed controls); verify each present region separately;
- parent/child background fills, content insets, and unintended card/gutter wrappers;
- icon inventory: every visible icon maps to a local source asset, has the correct natural dimensions/viewBox, and lands in the correct rendered slot;
- compound assets: the source-backed parent export or separately rendered child layers preserve their opacity, offsets, clipping and composed bounds;
- typography, line breaks, font weight, line height, and text color;
- actual loaded font faces, fallbacks and synthetic bold/italic where they affect fidelity;
- image crop, scale, focal point, and transparency;
- card radius, borders, shadows, gradients, and background texture;
- vertical rhythm and section spacing;
- bottom navigation, safe-area padding, or other sticky/fixed control position when present;
- scroll position and sticky/fixed behavior.

## Interaction

- buttons have the requested click behavior;
- route or tab changes preserve the correct active state;
- scrolling does not expose accidental overflow;
- fixed elements do not cover content;
- no unrequested animation causes layout shift.
- existing in-scope interaction and motion survive component replacement; if playback was not observed, say so.

## State and asset parity

- the screenshot and the HTML use the same Figma node/state;
- the route fixture asserts visible labels, tab count/order, selected controls, enabled/disabled controls, and overlay visibility;
- blank/filled, disabled/enabled, modal/toast, and scroll variants are not mixed;
- every referenced SVG/raster file is local, non-empty, and reachable from the delivered relative path;
- no Unicode, emoji, icon font, CSS pseudo-element, or CSS gradient substitutes an available Figma icon;
- computed CSS `::before`/`::after` content has been audited so generated glyphs are not hiding a source-icon mismatch;
- the preview state can be reproduced deterministically for a fresh comparison.
- for edited pages, the target file/build and preview URL match, the changed layer is actually visible, and old outlined text or overlays do not duplicate it;
- compare corresponding language fields for material meaning conflicts, preserving source copy and reporting unresolved discrepancies;
- identify relevant downloads or exports as dynamic or independent static derivatives; verify and update only when requested or authorized, and report stale or unverified outputs.

## Technical

- no broken local asset paths;
- no console errors for the active route;
- no unused large assets in the final package;
- no external dependency is required unless approved;
- `index.html` works from the requested delivery method;
- direct `file://` opening and HTTP-server serving are reported as separate checks; do not claim one from the other;
- report known differences instead of claiming pixel perfection without evidence.

Fix the largest visible mismatch first, then recheck the affected region and total size.
