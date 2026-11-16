# Figma design-to-code read protocol

This reference is the Figma-side prerequisite for the `figma-to-html` workflow. Apply it before calling the Figma `get_design_context` tool.

## Context requirements

- Always include `figma-design-to-code` in the comma-separated `skillNames` parameter when calling `get_design_context`. If this reference was loaded through an MCP resource, use the prefixed name `resource:figma-design-to-code`.
- Request a screenshot in the initial `get_design_context` call. If no screenshot is returned, call `get_screenshot` before editing.
- If `get_design_context` reports a sparse response, do not implement from it directly. Correlate its child node IDs with the screenshot and request the visible child nodes in parallel batches until the response is high fidelity.
- Use the high-fidelity `get_design_context` responses as the implementation source. The screenshot is the visual target and comparison reference, never a shipped implementation asset.

## Implementation requirements

- Inspect the likely project paths, existing framework, installed component libraries, assets and tokens before editing. Adapt the returned design context to the project's conventions instead of blindly copying raw absolute-positioned prototype markup.
- Identify the portions that are interactive and implement them as real controls and state transitions. This reference does not override the broader `figma-to-html` scope, source-lock, interaction, or live-text rules.
- Apply Code Connect at mapped nodes and directly reuse connected components unless they cannot express the source.
- Use every visible static image or SVG asset in the exact source slot. Do not omit, redraw, extract paths from, substitute, or incorrectly scale an available source asset. Preserve root `width`, `height`, `viewBox`, aspect ratio, and wrapper transforms; do not apply a broad `100% × 100%` rule that changes natural geometry.
- Download or save all required assets locally according to the Figma response. Do not leave temporary Figma asset URLs in delivered code, and do not use another downloader unless the user explicitly authorizes it.

## Verification requirements

- Verify only the requested screen/component and note; do not modify unrelated pre-existing mismatches.
- For every visible static asset, verify that the local file is non-empty, maps to the correct source layer, is used at the correct callsite, and renders at the correct effective geometry.
- A substituted, mismatched, missing, or misproportioned in-scope asset is a failure and must be repaired or reported as unresolved.
