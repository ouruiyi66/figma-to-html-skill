#!/usr/bin/env python3
"""Static audit for source-backed SVG icon usage in a Figma-to-HTML project."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ICON_TOKEN = re.compile(r"(?:icon|glyph|logo|chevron|arrow|badge|control|switch)", re.I)
SVG_SRC = re.compile(r"(?:src|href)=[\"']([^\"']+\.svg(?:\?[^\"']*)?)[\"']", re.I)
PSEUDO_RULE = re.compile(r"([^{}]+)::(?:before|after)\s*\{([^{}]*)\}", re.I | re.S)
ICON_PLACEHOLDER = re.compile(
    r"<(?:span|div|i)\b[^>]*class=[\"'][^\"']*(?:icon|glyph|logo)[^\"']*[\"'][^>]*>\s*</(?:span|div|i)>",
    re.I,
)


def fail(message: str, failures: list[str]) -> None:
    failures.append(f"FAIL: {message}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project", type=Path)
    parser.add_argument("--html", default="index.html")
    parser.add_argument("--css", default="styles.css")
    parser.add_argument("--manifest", default="assets/icon-manifest.json")
    args = parser.parse_args()

    root = args.project.resolve()
    html_path = root / args.html
    css_path = root / args.css
    manifest_path = root / args.manifest
    failures: list[str] = []
    warnings: list[str] = []

    if not html_path.is_file():
        fail(f"missing HTML entry: {html_path}", failures)
        print("\n".join(failures))
        return 1

    html = html_path.read_text(encoding="utf-8")
    css = css_path.read_text(encoding="utf-8") if css_path.is_file() else ""

    for match in PSEUDO_RULE.finditer(css):
        selector, body = match.groups()
        if ICON_TOKEN.search(selector) or "content:" in body:
            fail(f"icon-like pseudo-element or drawn content: {selector.strip()}", failures)

    for match in ICON_PLACEHOLDER.finditer(html):
        tag = match.group(0)
        fail(f"icon placeholder without an SVG element: {tag}", failures)

    svg_paths: set[str] = set()
    for match in SVG_SRC.finditer(html):
        raw = match.group(1).split("?", 1)[0]
        if raw.startswith(("http://", "https://", "data:")):
            fail(f"non-local SVG source: {raw}", failures)
            continue
        target = (html_path.parent / raw).resolve()
        try:
            target.relative_to(root)
        except ValueError:
            fail(f"SVG escapes project root: {raw}", failures)
            continue
        if not target.is_file() or target.stat().st_size == 0:
            fail(f"missing or empty SVG: {raw}", failures)
        svg_paths.add(raw)

    if not manifest_path.is_file():
        fail(f"missing symbolic-asset manifest: {manifest_path}", failures)
    else:
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            entries = manifest.get("icons", [])
            if not isinstance(entries, list):
                raise ValueError("icons must be a list")
            manifest_paths = {entry.get("path") for entry in entries if isinstance(entry, dict)}
            missing = sorted(path for path in svg_paths if path not in manifest_paths)
            for path in missing:
                fail(f"SVG is used but absent from manifest: {path}", failures)
            for entry in entries:
                if not isinstance(entry, dict) or not entry.get("role") or not entry.get("sourceNode"):
                    fail("manifest entry lacks role or sourceNode", failures)
        except (OSError, json.JSONDecodeError, ValueError) as exc:
            fail(f"invalid symbolic-asset manifest: {exc}", failures)

    if re.search(r"source-\d+\.svg", html):
        warnings.append("WARN: ordinal source SVG names remain in HTML; verify each has semantic manifest evidence.")

    for line in warnings:
        print(line)
    if failures:
        print("\n".join(failures))
        return 1
    print(f"PASS: symbolic SVG audit ({len(svg_paths)} rendered SVG references)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
