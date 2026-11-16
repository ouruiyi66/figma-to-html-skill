# Font packaging

In a live frontend, visible copy remains live HTML. Font files are companion assets; an explicitly requested static screenshot can contain rendered text and needs no separate font asset.

Recommended project layout:

```text
index.html
styles.css
assets/
  fonts/
    Brand-Regular.woff2
    Brand-Medium.woff2
    Brand-Bold.woff2
```

Declare only the weights actually used:

```css
@font-face {
  font-family: "Brand";
  src: url("assets/fonts/Brand-Regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

First check the project's existing assets and matching system fonts. Having access to a font in Figma or installed locally does not itself establish permission to distribute it: confirm the applicable license before packaging or converting it. Package only the necessary families, weights and styles; WOFF2 is preferred for browser delivery where supported. If a source font is unavailable or cannot be packaged, identify a named fallback and its visual impact. When exact typography is essential and the fallback would materially change the result, request the font or the user's choice; do not silently claim an exact match. Keep ordinary text live and record the decision. Subsetting can reduce large fonts but must cover all expected characters and be permitted by the font license.

Before comparison, wait for fonts and inspect the browser's actual rendered faces for representative text, numbers, languages and weights; a declared family does not prove it loaded or covers every character. Supply real bold/italic faces where available and disable synthetic weight/style when needed for fidelity; report unavailable faces and any resulting fallback or synthetic rendering. Recheck wrapping and alignment after loading, not just the CSS declarations.
