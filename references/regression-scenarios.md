# Skill regression scenarios

Use when changing the skill. Check the plan against these scenarios; run an implementation when needed to validate the behavior. Record what was actually checked rather than claiming unexecuted scenarios passed.

| Request | Expected outcome |
|---|---|
| A marked P1 with several phone frames | Resolve marked source states; do not recreate the canvas or open new tabs by default. |
| Recreate the entire canvas with clickable frames | Preserve overview geometry, labels, annotations, connectors and layer order; each hotspot opens a live source-backed state. |
| Pixel-perfect fixed screen | Lock source node and viewport; use measured assets/geometry and live text; compare the matching state. |
| Two sibling states and an annotated toast | Keep separate fixtures and source copy/selected states; implement evidenced feedback without merging variants. |
| Source-backed compound icon | Preserve its composition and transformations; parent export or layers are valid when faithful and suitable for the requested behavior. |
| Responsive page | Retain the source viewport as baseline, adapt to relevant widths and verify overflow; avoid freezing every element to a single viewport. |
| Missing source font or vector | Reuse a matching available asset where possible; report material impact and unresolved choice rather than silently claiming parity. |
| Animation supplied only as before/after stills | Implement evidenced endpoints; mark timing and intermediate motion as inferred or pending. |
| Static screenshot specifically requested | Deliver it as a screenshot with its limitations; do not call it an editable frontend. |
| Visual-only request | Retain source states and visual checks without inventing interactions. |
| An existing page shows SVG text while a matching HTML layer is hidden | Trace the visible layer, replace or hide only the relevant old copy, and verify the rendered result without duplicated text. |
| A user requests edits to one desktop copy while another preview is open | Identify the intended file and confirm the preview serves it; do not mutate or claim verification of the other copy. |
| Localized design frames disagree on a business field | Preserve each sourced value, flag the contradiction, and do not silently translate or reconcile it. |
| A page has an independent static PDF download | Determine whether the requested edit includes the PDF; do not claim the PDF was updated merely because the page changed. |
| Replace an animated component but retain its motion | Inspect existing animation ownership, retain the relevant container and test the changed visual and affected playback paths. |
| A source vector includes shadow bleed beyond its slot | Measure and preserve visual bounds, clipping and transforms rather than distorting or redrawing it. |
