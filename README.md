# figma-to-html

`figma-to-html` is a structured design-to-code skill for turning Figma frames and prototype flows into faithful, runnable HTML/CSS/SVG/JavaScript implementations.

## What problem does it solve?

Many Figma-to-code workflows lose fidelity during implementation. Common problems include:

- text being flattened into screenshots or outlined SVG paths;
- icons, logos, and illustrations being replaced with rough CSS or glyph approximations;
- incorrect spacing, geometry, image crops, and responsive behavior;
- missing selected, disabled, loading, overlay, and transition states;
- prototype interactions being represented as static screens instead of real frontend behavior;
- visual differences not being checked against a fresh render of the source design.

This skill provides a repeatable workflow for reducing those gaps while keeping the resulting implementation maintainable.

## What it provides

- Live HTML text for headings, labels, body copy, buttons, and other ordinary interface content.
- Exact or source-backed Figma assets for images, SVGs, icons, logos, and compound visual elements.
- Measured reconstruction of stepper lines, circles, connectors, progress states, and other high-salience geometry.
- Explicit modeling of overlays, selected states, disabled states, transitions, and prototype interactions.
- Responsive contracts that preserve the source viewport while making behavior at other sizes intentional and testable.
- Local, reproducible asset packaging instead of temporary Figma URLs.
- Font, asset, geometry, and component checks before visual comparison.
- Fresh browser-render comparison with clear reporting of unresolved visual differences.

## Why it is useful

The goal is not to produce a static screenshot that only looks correct at one moment. The goal is to produce a working frontend that remains readable, interactive, responsive, visually testable, and easy to extend.

It is useful for frontend developers, design engineers, and coding agents who need to:

- reproduce Figma designs as real interfaces;
- convert prototype flows into working HTML/CSS/JavaScript;
- preserve editability and interaction during visual recreation;
- diagnose why an implementation differs from its source design;
- build a reliable visual QA loop for design-to-code work.

## Skill structure

- `SKILL.md` — main workflow and implementation rules.
- `references/` — guidance for Figma inspection, asset handling, geometry, typography, motion, responsive behavior, and visual comparison.
- `scripts/` — lightweight helpers for auditing symbolic graphics and comparing screenshots.
- `agents/openai.yaml` — agent-facing metadata.

Start with [`SKILL.md`](SKILL.md).
