#!/usr/bin/env python3
"""Compare two same-size screenshots and optionally write a highlighted diff."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image, ImageChops, ImageEnhance


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("reference", type=Path)
    parser.add_argument("actual", type=Path)
    parser.add_argument("--diff", type=Path)
    parser.add_argument("--threshold", type=int, default=12)
    args = parser.parse_args()

    reference = Image.open(args.reference).convert("RGBA")
    actual = Image.open(args.actual).convert("RGBA")
    if reference.size != actual.size:
        raise SystemExit(f"size mismatch: reference={reference.size}, actual={actual.size}")

    delta = ImageChops.difference(reference, actual)
    rgb_delta = delta.convert("RGB")
    changed = 0
    bbox = None
    for y in range(rgb_delta.height):
        for x in range(rgb_delta.width):
            r, g, b = rgb_delta.getpixel((x, y))
            if max(r, g, b) > args.threshold:
                changed += 1
                bbox = (x, y, x + 1, y + 1) if bbox is None else (
                    min(bbox[0], x), min(bbox[1], y), max(bbox[2], x + 1), max(bbox[3], y + 1)
                )

    total = rgb_delta.width * rgb_delta.height
    result = {
        "width": rgb_delta.width,
        "height": rgb_delta.height,
        "threshold": args.threshold,
        "changed_pixels": changed,
        "changed_ratio": changed / total if total else 0,
        "diff_bbox": bbox,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))

    if args.diff:
        highlighted = ImageEnhance.Contrast(rgb_delta).enhance(3.0)
        highlighted.save(args.diff)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
