# Asset optimization

Apply only the optimizations that preserve the user's chosen fidelity level.

## Format selection

- AVIF or WebP for photographic and textured content.
- JPEG for photographs when broad compatibility or encoder availability matters.
- PNG for transparency, crisp UI pixels, or assets that become visibly damaged when lossy-compressed.
- SVG for simple vectors and icons; remove unnecessary metadata or definitions only after verifying that appearance, transforms, clipping and natural geometry remain intact.

## Sizing and deduplication

- Export at 1x for a size-first result and 2x for a normal viewport result unless the user specifies another DPR.
- Never keep both a source and a converted copy unless the source is needed for future editing.
- Reuse identical assets by reference.
- Prefer an external reusable SVG symbol/sprite for repeated icons over many duplicated inline paths.
- Crop transparent margins and remove pixels outside the visible content when that does not change alignment.
- Remove assets belonging to other routes or unused states from the deliverable package.

## Internal audit

Use these checks internally to decide between live code, region slices, and a full-page screenshot. Do not generate a formal volume report unless the user requests one.

- inspect the largest files;
- detect duplicate or near-duplicate files;
- identify assets not referenced by the active route;
- compare the estimated final package size for competing representation plans.

Do not sacrifice legibility, alpha edges, or the target crop just to meet an arbitrary byte target. If the largest asset dominates the bundle, offer a lower-quality or region-split option instead of silently degrading it.
