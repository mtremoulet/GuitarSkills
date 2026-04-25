#!/usr/bin/env python3
"""CLI entry point for the chord voicing library."""

from __future__ import annotations

import argparse
import json
import sys
import time

from chordlib.theory import parse_note_name, lookup_formula, parse_chord_name, CHORD_FORMULAS
from chordlib.guitar import Fretboard, STANDARD_TUNING
from chordlib.voicing import Voicing
from chordlib.query import VoicingQuery, execute_query
from chordlib.classifier import classify, VoicingType
from chordlib.playability import check_playability
from chordlib.ascii_renderer import render_voicing, render_voicing_compact


def voicing_to_dict(v: Voicing) -> dict:
    """Convert a Voicing to a JSON-serializable dict."""
    pr = check_playability(v)
    types = classify(v)
    return {
        "frets": [f if f is not None else None for f in v.frets],
        "notes": [n if n is not None else None for n in v.note_names],
        "degrees": [d if d is not None else None for d in v.interval_names],
        "bass_note": v.note_names[v.sounding_indices[0]],
        "top_note": v.note_names[v.sounding_indices[-1]],
        "inversion": v.inversion_name,
        "fret_span": v.fret_span,
        "min_fret": v.min_fret,
        "max_fret": v.max_fret,
        "voicing_type": sorted(t.value for t in types),
        "difficulty": round(pr.difficulty, 2),
        "finger_count": pr.finger_count,
        "requires_barre": pr.requires_barre,
        "compact": render_voicing_compact(v),
        "ascii": render_voicing(v),
    }


def build_query(args: argparse.Namespace) -> VoicingQuery:
    """Build a VoicingQuery from CLI arguments."""
    root_pc = parse_note_name(args.root)
    formula = lookup_formula(args.quality)

    voicing_types = None
    if args.voicing_type:
        type_map = {
            "open": VoicingType.OPEN,
            "barre": VoicingType.BARRE,
            "shell": VoicingType.SHELL,
            "drop2": VoicingType.DROP_2,
            "drop3": VoicingType.DROP_3,
            "drop24": VoicingType.DROP_2_4,
            "close": VoicingType.CLOSE,
            "spread": VoicingType.SPREAD,
        }
        voicing_types = set()
        for vt in args.voicing_type:
            if vt.lower() in type_map:
                voicing_types.add(type_map[vt.lower()])

    bass_note = parse_note_name(args.bass_note) if args.bass_note else None
    top_note = parse_note_name(args.top_note) if args.top_note else None

    # bass_string: CLI uses guitarist convention (1=high e, 6=low E), internally 0=low E
    root_string = (6 - args.bass_string) if args.bass_string else None

    return VoicingQuery(
        root=root_pc,
        formula=formula,
        min_fret=args.min_fret,
        max_fret=args.max_fret,
        bass_note=bass_note,
        top_note=top_note,
        root_string=root_string,
        inversion=args.inversion,
        voicing_types=voicing_types,
        min_notes=args.min_notes,
        max_notes=args.max_notes,
        max_span=args.max_span,
        allow_inner_mutes=not args.no_inner_mutes,
        max_difficulty=args.max_difficulty,
        playable_only=not args.include_unplayable,
        sort_key=args.sort,
        limit=args.limit,
        offset=args.offset,
    )


def cmd_query(args: argparse.Namespace) -> None:
    """Handle the 'query' subcommand."""
    query = build_query(args)
    fretboard = Fretboard(STANDARD_TUNING, 24)

    t0 = time.time()
    result = execute_query(query, fretboard)
    elapsed = time.time() - t0

    if args.format == "json":
        output = {
            "query": {
                "root": args.root,
                "quality": args.quality,
            },
            "total_matches": result.total_matches,
            "showing": len(result.voicings),
            "offset": query.offset,
            "elapsed_ms": round(elapsed * 1000),
            "voicings": [voicing_to_dict(v) for v in result.voicings],
        }
        print(json.dumps(output, indent=2))
    else:
        # Text format
        from chordlib.theory import note_name, PREFER_FLATS
        root_name = note_name(query.root, PREFER_FLATS.get(query.root, False))
        chord_name = f"{root_name}{query.formula.symbol}"
        print(f"{chord_name} — {result.total_matches} voicings found "
              f"(showing {query.offset + 1}-{query.offset + len(result.voicings)}) "
              f"[{elapsed * 1000:.0f}ms]")
        print()

        for i, v in enumerate(result.voicings, start=query.offset + 1):
            pr = check_playability(v)
            types = classify(v)
            type_str = ", ".join(sorted(t.value for t in types)) if types else "—"
            print(f"  #{i}  [{render_voicing_compact(v)}]  "
                  f"{v.inversion_name}  |  {type_str}  |  "
                  f"difficulty: {pr.difficulty:.1f}  fingers: {pr.finger_count}")
            # Indented ASCII
            for line in render_voicing(v).split("\n"):
                print(f"      {line}")
            print()


def cmd_list_types(args: argparse.Namespace) -> None:
    """List all available chord types."""
    seen = set()
    types = []
    for symbol, formula in CHORD_FORMULAS.items():
        if id(formula) not in seen:
            seen.add(id(formula))
            intervals = ", ".join(iv.display_name for iv in formula.intervals)
            aliases = ", ".join(formula.aliases) if formula.aliases else ""
            types.append((formula.symbol, formula.name, intervals, aliases))

    if args.format == "json":
        print(json.dumps([
            {"symbol": s, "name": n, "intervals": i, "aliases": a}
            for s, n, i, a in types
        ], indent=2))
    else:
        print(f"{'Symbol':<12} {'Name':<28} {'Intervals':<30} {'Aliases'}")
        print("-" * 90)
        for s, n, i, a in types:
            print(f"{s or '(major)':<12} {n:<28} {i:<30} {a}")


def main():
    parser = argparse.ArgumentParser(
        description="Guitar Chord Voicing Library",
        prog="chord",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # query subcommand
    q = subparsers.add_parser("query", help="Query chord voicings")
    q.add_argument("--root", required=True, help="Root note (C, C#, Db, etc.)")
    q.add_argument("--quality", required=True, help="Chord quality (m7, maj9, 7b5, etc.)")
    q.add_argument("--min-fret", type=int, default=None, help="Minimum fret position")
    q.add_argument("--max-fret", type=int, default=None, help="Maximum fret position")
    q.add_argument("--bass-note", default=None, help="Required bass note name")
    q.add_argument("--top-note", default=None, help="Required top note name")
    q.add_argument("--bass-string", type=int, default=None, help="String with root (1=high e, 6=low E — guitarist convention)")
    q.add_argument("--inversion", type=int, default=None, help="Inversion (0=root, 1=first, etc.)")
    q.add_argument("--voicing-type", nargs="+", default=None,
                    help="Voicing types: open, barre, shell, drop2, drop3, close, spread")
    q.add_argument("--min-notes", type=int, default=3, help="Minimum sounding strings (default: 3)")
    q.add_argument("--max-notes", type=int, default=6, help="Maximum sounding strings (default: 6)")
    q.add_argument("--max-span", type=int, default=4, help="Maximum fret span (default: 4)")
    q.add_argument("--no-inner-mutes", action="store_true", help="Disallow muted strings between sounding ones")
    q.add_argument("--max-difficulty", type=float, default=None, help="Maximum difficulty (0.0-1.0)")
    q.add_argument("--include-unplayable", action="store_true", help="Include physically unplayable voicings")
    q.add_argument("--sort", default="default",
                    choices=["default", "compact", "position_asc", "position_desc", "open_strings"],
                    help="Sort order")
    q.add_argument("--limit", type=int, default=10, help="Max results (default: 10)")
    q.add_argument("--offset", type=int, default=0, help="Skip first N results")
    q.add_argument("--format", choices=["json", "text"], default="text", help="Output format")

    # list-types subcommand
    lt = subparsers.add_parser("list-types", help="List available chord types")
    lt.add_argument("--format", choices=["json", "text"], default="text")

    args = parser.parse_args()

    if args.command == "query":
        cmd_query(args)
    elif args.command == "list-types":
        cmd_list_types(args)


if __name__ == "__main__":
    main()
