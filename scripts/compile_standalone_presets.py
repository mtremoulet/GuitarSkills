#!/usr/bin/env python3
"""
CLI script to compile serial toneprints into native Standalone (.json) rack presets.
"""

from __future__ import annotations

import sys
import argparse
from pathlib import Path

# Add workspace root to sys.path
WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
if str(WORKSPACE_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT))

from scripts.utils.config import TONES_DIR
from scripts.preset_compiler.standalone import compile_all_standalone_presets, STANDALONE_PRESETS_DIR


def main():
    parser = argparse.ArgumentParser(description="Compile guitar toneprints into Standalone rack presets.")
    parser.add_argument("-f", "--filter", help="Filter target toneprints by name/path substring (case-insensitive).")
    parser.add_argument("-o", "--output", default=str(STANDALONE_PRESETS_DIR), help="Output directory for Standalone presets.")
    args = parser.parse_args()

    print("==================================================")
    print("STANDALONE RACK PRESET COMPILER")
    print(f"Source: {TONES_DIR}")
    print(f"Destination: {args.output}")
    if args.filter:
        print(f"Filter: '{args.filter}'")
    print("==================================================")

    count = compile_all_standalone_presets(
        tones_dir=TONES_DIR,
        output_dir=args.output,
        filter_substr=args.filter,
    )

    print("==================================================")
    print(f"Successfully compiled {count} Standalone presets in {args.output}")
    print("==================================================")


if __name__ == "__main__":
    main()
