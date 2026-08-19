#!/usr/bin/env python3
"""
scripts/quarantine_toneprint.py

Automates archiving toneprints and quarantining their compiled plugin presets.

Usage:
    python3 scripts/quarantine_toneprint.py tones/humbuckers/my-tone.md
    python3 scripts/quarantine_toneprint.py my-tone-id
    python3 scripts/quarantine_toneprint.py --restore tones/humbuckers/my-tone.md
"""

from __future__ import annotations

import os
import sys
import re
import shutil
import argparse
from pathlib import Path

# Workspace Root
WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
TONES_DIR = WORKSPACE_ROOT / "tones"
QUARANTINE_DIR = WORKSPACE_ROOT / "quarantined"
QUARANTINE_README = QUARANTINE_DIR / "README.md"

HOME_DIR = Path.home()
PRESET_SEARCH_DIRS = [
    HOME_DIR / "Documents" / "Universal Audio" / "Presets" / "Plug-Ins",
    HOME_DIR / "Documents" / "Nembrini Audio",
    HOME_DIR / "Music" / "Audio Music Apps" / "Plug-In Settings",
    Path("/Library/Audio/Presets"),
    HOME_DIR / "Library" / "Audio" / "Presets",
    HOME_DIR / "Library" / "Application Support" / "Valhalla DSP, LLC" / "ValhallaSupermassive" / "Presets" / "User",
    TONES_DIR / "presets" / "yamaha",
]


def find_tone_file(target: str) -> Path | None:
    target_path = Path(target)
    if target_path.exists() and target_path.suffix == ".md":
        return target_path.resolve()

    # Search in tones/
    for md_file in TONES_DIR.rglob("*.md"):
        if md_file.name == "INDEX.md":
            continue
        if md_file.stem == target or md_file.name == target:
            return md_file.resolve()

    return None


def update_frontmatter_status(file_path: Path, new_status: str) -> str:
    content = file_path.read_text(encoding="utf-8")
    if re.search(r"^status:\s*.*$", content, re.MULTILINE):
        updated = re.sub(r"^status:\s*.*$", f"status: {new_status}", content, flags=re.MULTILINE)
    else:
        # insert status into frontmatter
        if content.startswith("---"):
            parts = content.split("---", 2)
            updated = f"---{parts[1].rstrip()}\nstatus: {new_status}\n---" + parts[2]
        else:
            updated = f"---\nstatus: {new_status}\n---\n\n" + content

    file_path.write_text(updated, encoding="utf-8")
    return new_status


def parse_frontmatter(file_path: Path) -> dict:
    content = file_path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
    if not match:
        return {}
    data = {}
    for line in match.group(1).splitlines():
        if line.startswith(" ") or line.startswith("\t"):
            continue
        if ":" in line:
            k, _, v = line.partition(":")
            val = v.strip()
            if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                val = val[1:-1]
            data[k.strip()] = val
    return data


def refresh_quarantine_readme():
    lines = [
        "# Quarantined Presets",
        "",
        "This directory holds plugin and DAW presets that have been removed from active plugin directories when toneprints are set to `status: archived`.",
        "",
        "Presets are organized in sub-folders mirroring their original system or user locations (relative to the user home or system root), allowing them to be inspected or restored at any time without destructive deletion.",
        "",
        "## Current Quarantined Files",
        "",
    ]

    found_any = False
    for root, _, files in os.walk(QUARANTINE_DIR):
        for f in sorted(files):
            if f in ["README.md", ".DS_Store", ".gitkeep"]:
                continue
            full_path = Path(root) / f
            rel_to_q = full_path.relative_to(QUARANTINE_DIR)
            lines.append(f"* `{rel_to_q}`")
            found_any = True

    if not found_any:
        lines.append("*(No presets currently quarantined)*")

    QUARANTINE_README.write_text("\n".join(lines) + "\n", encoding="utf-8")


def quarantine_toneprint(tone_file: Path):
    fm = parse_frontmatter(tone_file)
    preset_name = fm.get("preset_name", "")
    tone_id = fm.get("id", tone_file.stem)

    patterns = [p.lower() for p in [preset_name, tone_id, tone_file.stem] if p]

    print(f"Archiving toneprint: {tone_file.name}")
    update_frontmatter_status(tone_file, "archived")

    # Search and quarantine matching presets
    quarantined_count = 0
    for sdir in PRESET_SEARCH_DIRS:
        if not sdir.exists():
            continue
        for root, _, files in os.walk(sdir):
            for f in files:
                f_lower = f.lower()
                if any(p in f_lower for p in patterns):
                    src_file = Path(root) / f
                    if str(HOME_DIR) in str(src_file):
                        rel_path = src_file.relative_to(HOME_DIR)
                    else:
                        rel_path = src_file.relative_to(Path("/"))

                    dest_file = QUARANTINE_DIR / rel_path
                    dest_file.parent.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(src_file), str(dest_file))
                    print(f"  -> Quarantined: {src_file} -> {dest_file}")
                    quarantined_count += 1

    refresh_quarantine_readme()
    print(f"Quarantined {quarantined_count} preset(s).")

    # Rebuild viewer index
    os.system(f"python3 {WORKSPACE_ROOT}/tone-advisor/generate_tone_viewer.py --build-only")


def restore_toneprint(tone_file: Path):
    fm = parse_frontmatter(tone_file)
    preset_name = fm.get("preset_name", "")
    tone_id = fm.get("id", tone_file.stem)

    patterns = [p.lower() for p in [preset_name, tone_id, tone_file.stem] if p]

    print(f"Restoring toneprint from archive: {tone_file.name}")
    update_frontmatter_status(tone_file, "tested")

    restored_count = 0
    for root, _, files in os.walk(QUARANTINE_DIR):
        for f in files:
            if f in ["README.md", ".DS_Store", ".gitkeep"]:
                continue
            f_lower = f.lower()
            if any(p in f_lower for p in patterns):
                q_file = Path(root) / f
                rel_path = q_file.relative_to(QUARANTINE_DIR)
                dest_file = HOME_DIR / rel_path
                dest_file.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(q_file), str(dest_file))
                print(f"  -> Restored: {q_file} -> {dest_file}")
                restored_count += 1

    refresh_quarantine_readme()
    print(f"Restored {restored_count} preset(s).")

    # Rebuild viewer index
    os.system(f"python3 {WORKSPACE_ROOT}/tone-advisor/generate_tone_viewer.py --build-only")


def main():
    parser = argparse.ArgumentParser(description="Archive or restore toneprints and quarantine presets.")
    parser.add_argument("target", help="Toneprint file path or slug ID (e.g. deja-hifi-jazz-humbucker)")
    parser.add_argument("--restore", action="store_true", help="Restore an archived toneprint and its quarantined presets")
    args = parser.parse_args()

    tone_file = find_tone_file(args.target)
    if not tone_file:
        print(f"Error: Could not find toneprint matching '{args.target}' in tones/")
        sys.exit(1)

    if args.restore:
        restore_toneprint(tone_file)
    else:
        quarantine_toneprint(tone_file)


if __name__ == "__main__":
    main()
