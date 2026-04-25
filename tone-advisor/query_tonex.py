#!/usr/bin/env python3
"""
Query ToneModels.json for TONEX captures by amp name, stomp name, category, or free text.

Usage:
  python3 query_tonex.py --amp "Deluxe Reverb"
  python3 query_tonex.py --stomp "OCD"
  python3 query_tonex.py --category "CLEAN"
  python3 query_tonex.py --search "benson"
  python3 query_tonex.py --target amp        # filter by TargetOrder type
  python3 query_tonex.py --favorites
  python3 query_tonex.py --stats
"""

import json
import argparse
from pathlib import Path

DB = Path(__file__).parent / "ToneModels.json"

TARGET_LABELS = {
    "0 - AmpAndCab": "Amp+Cab",
    "1 - ComplexRig": "ComplexRig",
    "2 - Stomp": "Stomp",
    "3 - Amp": "Amp",
    "4 - StompAndAmp": "Stomp+Amp",
    "5 - CustomIR": "CustomIR",
}

TARGET_SHORTCUTS = {
    "amp": ["0 - AmpAndCab", "3 - Amp"],
    "stomp": ["2 - Stomp"],
    "rig": ["1 - ComplexRig"],
    "combo": ["4 - StompAndAmp"],
    "ir": ["5 - CustomIR"],
}


def load():
    with open(DB) as f:
        return json.load(f)


def fmt_source(m):
    return "factory" if m.get("Factory") == 1 else "community"


def fmt_target(m):
    return TARGET_LABELS.get(m.get("TargetOrder", ""), m.get("TargetOrder", ""))


def print_results(results, limit=40):
    if not results:
        print("No matches found.")
        return
    print(f"{len(results)} match(es){f' (showing first {limit})' if len(results) > limit else ''}:\n")
    header = f"{'Model Name':<45} {'Type':<12} {'Amp':<30} {'Stomp':<25} {'Source':<10} GUID"
    print(header)
    print("-" * len(header))
    for m in results[:limit]:
        name = (m.get("Tag_ModelName") or "")[:44]
        amp = (m.get("Tag_AmpName") or "")[:29]
        stomp = (m.get("Tag_StompName") or "")[:24]
        ttype = fmt_target(m)
        source = fmt_source(m)
        guid = m.get("GUID", "")
        print(f"{name:<45} {ttype:<12} {amp:<30} {stomp:<25} {source:<10} {guid}")


def cmd_stats(models):
    from collections import Counter
    cats = Counter(m.get("Tag_ModelCategory", "(none)") for m in models)
    targets = Counter(m.get("TargetOrder", "") for m in models)
    print(f"Total models: {len(models)}")
    print(f"  Factory/IK:  {sum(1 for m in models if m.get('Factory') == 1)}")
    print(f"  Community:   {sum(1 for m in models if m.get('Factory') == 0)}")
    print(f"  Favorites:   {sum(1 for m in models if m.get('Favorite') == 1)}")
    print()
    print("By capture type:")
    for k, v in sorted(targets.items(), key=lambda x: -x[1]):
        label = TARGET_LABELS.get(k, k)
        print(f"  {v:5d}  {label}")
    print()
    print("By category:")
    for k, v in sorted(cats.items(), key=lambda x: -x[1]):
        print(f"  {v:5d}  {k}")


def main():
    parser = argparse.ArgumentParser(description="Query TONEX model library")
    parser.add_argument("--amp", help="Search by amp name (case-insensitive substring)")
    parser.add_argument("--stomp", help="Search by stomp/pedal name (case-insensitive substring)")
    parser.add_argument("--category", help="Filter by Tag_ModelCategory (e.g. CLEAN, DRIVE, HI-GAIN)")
    parser.add_argument("--search", help="Free-text search across name, amp, stomp, description, keywords")
    parser.add_argument("--target", choices=["amp", "stomp", "rig", "combo", "ir"],
                        help="Filter by capture type")
    parser.add_argument("--favorites", action="store_true", help="Show only favorites")
    parser.add_argument("--factory", action="store_true", help="Limit to factory/IK models")
    parser.add_argument("--community", action="store_true", help="Limit to community models")
    parser.add_argument("--limit", type=int, default=40, help="Max rows to display (default 40)")
    parser.add_argument("--stats", action="store_true", help="Print library statistics and exit")
    args = parser.parse_args()

    models = load()

    if args.stats:
        cmd_stats(models)
        return

    results = models

    if args.favorites:
        results = [m for m in results if m.get("Favorite") == 1]

    if args.factory:
        results = [m for m in results if m.get("Factory") == 1]
    elif args.community:
        results = [m for m in results if m.get("Factory") == 0]

    if args.target:
        allowed = TARGET_SHORTCUTS[args.target]
        results = [m for m in results if m.get("TargetOrder") in allowed]

    if args.amp:
        q = args.amp.lower()
        results = [m for m in results if q in (m.get("Tag_AmpName") or "").lower()]

    if args.stomp:
        q = args.stomp.lower()
        results = [m for m in results if q in (m.get("Tag_StompName") or "").lower()]

    if args.category:
        q = args.category.lower()
        results = [m for m in results if q in (m.get("Tag_ModelCategory") or "").lower()]

    if args.search:
        q = args.search.lower()
        def matches(m):
            fields = [
                m.get("Tag_ModelName") or "",
                m.get("Tag_AmpName") or "",
                m.get("Tag_StompName") or "",
                m.get("Tag_Description") or "",
                m.get("Tag_Keywords") or "",
                m.get("Tag_ModelComment") or "",
                m.get("Tag_UserName") or "",
            ]
            return any(q in f.lower() for f in fields)
        results = [m for m in results if matches(m)]

    print_results(results, limit=args.limit)


if __name__ == "__main__":
    main()
