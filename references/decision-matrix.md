# Representation decision matrix

Use this matrix to make the tradeoff explicit rather than defaulting to all screenshots or all SVG.

| Content | Preferred representation | Use a raster slice when | Avoid rasterizing when |
|---|---|---|---|
| Body text and headings | Live HTML/CSS | In an explicitly requested static screenshot, text and fonts are baked in | Text must be editable, selectable, localized, or responsive |
| Buttons and navigation | HTML/CSS/JavaScript | Only its non-text decorative artwork is a source-backed visual leaf | Its label, layout or interaction must remain live |
| Simple icon | SVG | The icon is a complex painted illustration | It repeats and could be shared through a symbol/sprite |
| Photo or complex illustration | WebP/AVIF/JPEG | Always reasonable for a static visual | The visual needs independent animation or live data |
| Texture or grain | Optimized raster background | The texture is expensive to reproduce | A CSS gradient/noise approximation is visibly equivalent |
| Card with complex decoration | Region-level image plus live HTML overlay | The decoration is expensive to rebuild and the text remains live | Text, data, or layout needs to change independently |
| Complete page | Live HTML/CSS/SVG/JS | Only for an explicitly requested static screenshot deliverable, with the limitations explained | A runnable frontend with live text, responsive behavior or interaction is requested |

When uncertain, use a hybrid: keep the semantic shell and controls live, and rasterize only the visually expensive region.

For important raster decisions, record the target CSS size, source pixel size, format, quality and reason. If a static screenshot is requested, explain the resulting editability, interaction and responsiveness limitations.
