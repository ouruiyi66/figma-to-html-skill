# Motion reconstruction

Use when the user requests motion or the in-scope source explicitly includes it. A Figma still, sequence of frames or annotation may establish states without establishing a complete animation.

1. Map trigger, before/after node IDs, affected layers, intermediate states, duration, delay, easing, repeat behavior and feedback. Distinguish explicit Figma prototype data and annotations from inferences; mark missing or conflicting timing and behavior `PENDING` or clearly identify any proposed interpretation.
2. Preserve the source geometry and appearance at both endpoints before adding motion. Separate only the source artwork that needs independent animation; keep controls and ordinary text live.
3. Use CSS transitions/keyframes for simple transform, opacity and color. Use SVG masks or `clip-path` for source-backed reveals. Canvas or JavaScript animation may be suitable for complex particles or compositing, but must not replace ordinary UI text or controls with pixels. Reuse the existing project animation system when appropriate.
4. Expose deterministic start, keyframe and end checkpoints; allow time or progress to be controlled during verification. Confirm the triggering action, final state, interruptions/replay if in scope, and performance at the target viewport. Compare source-backed checkpoints against matching source states; do not assert exact motion parity when only stills exist.
5. Respect reduced-motion preferences where applicable without changing the underlying completed state; verify that feedback and controls remain usable.

When editing a component with existing motion, inspect the animation owner, trigger, timing, transforms, masks, state transitions and language variants before replacing content. Prefer retaining the existing motion container and changing only the requested layer. Exercise affected entry, exit, interruption/replay and language-switch paths when relevant, verifying the visible result as well as animation configuration. If playback or a checkpoint cannot be observed, report that limitation instead of inferring success from code alone.
