# Visual comparison contract

Visual comparison is a required completion gate. Source inspection, a DOM check, or an old screenshot does not replace a fresh comparison of the latest rendered page.

## Baseline

Use the approved Figma export or user-supplied reference as the baseline. Record the exact supplied node ID and resolved frame identity, visible state key, target viewport, device scale, browser/OS, scroll position, font availability, and whether the image is full-page, isolated overlay, or a region. Do not compare images captured at different CSS dimensions or silently resize either side. A blank/disabled reference must be compared to a blank/disabled HTML fixture, not a filled/enabled route that happens to share the same frame title. If the supplied node is a parent/canvas group, resolve and record the selected child Frame before capture.

## Stable render

Before capture:

- wait for fonts and images to finish loading;
- disable animations, transitions, caret blinking, and dynamic timestamps;
- use the same viewport and device scale as the reference;
- set the same scroll position;
- keep text live in the implementation;
- render the exact deterministic preview state named in the baseline;
- mask only genuinely nondeterministic regions, and record each mask.

For edits, establish the target file or build, preview URL, active browser tab and state before changing anything; confirm the preview actually serves the edited version and reload or rebuild as appropriate. When the target is a component inside an existing page, inspect its visible DOM and composited layers in the requested state and language, including hidden/duplicate old text. An edit to an inactive, covered or stale source is not a successful visible change.

A fresh render of the latest implementation is mandatory evidence. If the browser preview, screenshot capture, or equivalent visual review cannot be established, keep the affected fixture `UNRESOLVED`; source inspection, static checks, or an older screenshot do not count as visual verification.

Playwright's `toHaveScreenshot()` is a good default when Playwright is available because it can keep a baseline and compare later renders with configurable thresholds. Its documentation also warns that browser, OS, hardware, and rendering mode can change results, so keep the comparison environment stable: [Playwright visual comparisons](https://playwright.dev/docs/test-snapshots).

## Comparison loop

1. Assert the fixture's source node, exact visible text/child count, state labels, selected controls, overlay visibility, and viewport. If the route does not resolve to the supplied node/state, stop with `FAIL`; do not continue to image diffing.
2. Capture the whole target frame or isolated overlay at its natural size.
3. Compare the latest render against the matching approved baseline.
4. Inspect the diff and group mismatches into source/state identity, text/child parity, chrome geometry, content-wrapper geometry, icon/compound asset parity, rendered substitutes, typography, crop, color/surface, and fixed-position issues.
5. Fix only the 1–3 dominant mismatches.
6. Capture again and repeat a bounded number of times for every fixture.
7. After the final change, compare the affected component and its parent context again; use a full-frame comparison where the requested scope or change could affect it.

When no automated pixel comparator is available, use model vision or a side-by-side image review and state that the result is visually reviewed rather than pixel-diff verified. If neither a fresh render nor a current visual review is available, report the fixture as `UNRESOLVED` and do not claim visual parity.

## Interpretation

Do not fail a page because of unavoidable antialiasing alone. Do fail or continue iterating when the source node/state is wrong, text wraps differently, element bounds drift, image crops differ, fixed elements move, a compound asset is missing a child, or large surfaces show a visible mismatch. Never call the page “pixel perfect” without fresh comparison evidence for every in-scope fixture.
