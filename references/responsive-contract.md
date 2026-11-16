# Responsive contract

Infer the intended scope from the user, source and project. When the choice materially changes the deliverable and cannot be inferred, ask:

```text
你希望页面如何适配？
A. 固定目标尺寸：最接近 Figma，开发范围和体积最小。
B. 基础自适应：保留主要视觉结构，在常见手机/平板宽度下允许换行和堆叠。
C. 完整自适应：为手机、平板、桌面分别建立布局规则，视觉可能与 Figma 单一画板产生差异。
```

Explain that adaptation is not a free improvement. It can change line breaks, card heights, image crops, spacing, navigation structure, and the number of assets. A fixed Figma frame is not evidence of how unseen widths should behave.

## If BASIC or FULL is selected

- Validate at the supplied Figma design size plus a reference matrix appropriate to the source platform and requested scope, unless the user specifies another matrix.
- For a cross-platform web flow with no project-specific matrix, use these public fallback sizes: phone `390 × 844`, tablet `768 × 1024`, desktop `1440 × 900`. They are fallback validation targets, not universal requirements.
- Treat the Figma design size as the highest-fidelity reference. Additional sizes are validation targets, not evidence that the original design intended those exact breakpoints.
- If the source is a Figma canvas overview, the Figma design size means the actual target viewport Frame size, not the canvas dimensions or the screenshot's displayed pixel size.
- Base breakpoints on content collisions and layout changes, not device names alone.
- Prefer fluid containers and `clamp()` for typography or spacing that should scale continuously.
- Use component-level/container queries when a component's available width controls its layout.
- Test for horizontal overflow, clipped text, unsafe fixed elements, and image crop drift.
- Preserve reading order and keep essential content visible; do not hide content just to match a narrow screenshot.
- Keep the original Figma viewport as the highest-fidelity reference and describe intentional differences at other widths.

These principles are adapted from responsive UI skills that emphasize content-driven breakpoints, container queries, fluid values, multi-viewport checks, and overflow prevention: [frontend-design](https://github.com/PracticalSwan/agent-skills/blob/main/frontend-design/SKILL.md), [mobile-responsive](https://github.com/AsadSumbul/mobile-responsive), and [responsive-design](https://github.com/wshobson/agents/tree/main/plugins/ui-design/skills/responsive-design).
