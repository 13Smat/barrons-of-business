#!/usr/bin/env python3
"""Create or update labels from .github/labels.yml. Does not delete other labels."""

import subprocess
import sys
from pathlib import Path


def unquote(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def parse(text: str) -> list[dict[str, str]]:
    labels: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("- name:"):
            if current is not None:
                labels.append(current)
            current = {"name": unquote(line.split(":", 1)[1].strip())}
            continue
        if current is None:
            raise SystemExit(f"line is outside a label: {raw}")
        key, sep, value = line.partition(":")
        if sep != ":" or key not in {"color", "description"}:
            raise SystemExit(f"unsupported line: {raw}")
        current[key] = unquote(value.strip())
    if current is not None:
        labels.append(current)

    seen: set[str] = set()
    for label in labels:
        missing = {"name", "color", "description"} - label.keys()
        if missing:
            raise SystemExit(f"label missing {sorted(missing)}: {label}")
        if label["name"] in seen:
            raise SystemExit(f"duplicate label: {label['name']}")
        seen.add(label["name"])
        color = label["color"].removeprefix("#")
        if len(color) != 6 or any(c not in "0123456789abcdefABCDEF" for c in color):
            raise SystemExit(f"bad color for {label['name']}: {label['color']}")
        label["color"] = color.lower()
        if not label["name"] or not label["description"]:
            raise SystemExit(f"empty name or description: {label}")
    if not labels:
        raise SystemExit("no labels in .github/labels.yml")
    return labels


def gh(args: list[str]) -> None:
    try:
        result = subprocess.run(["gh", *args], text=True, capture_output=True)
    except FileNotFoundError:
        raise SystemExit("gh is not on PATH") from None
    if result.returncode != 0:
        sys.stderr.write(result.stderr)
        sys.stderr.write(result.stdout)
        raise SystemExit(result.returncode)


def main() -> None:
    path = Path(__file__).resolve().parents[1] / "labels.yml"
    labels = parse(path.read_text())
    for label in labels:
        gh(
            [
                "label",
                "create",
                label["name"],
                "--color",
                label["color"],
                "--description",
                label["description"],
                "--force",
            ]
        )
        print(f"synced {label['name']}")


if __name__ == "__main__":
    main()
