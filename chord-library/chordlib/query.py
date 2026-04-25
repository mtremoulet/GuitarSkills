"""Query engine: structured queries over generated voicings with filtering and pagination."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, Callable

from .theory import ChordFormula, parse_note_name, lookup_formula
from .guitar import Fretboard, STANDARD_TUNING
from .voicing import Voicing
from .generator import generate_voicings
from .playability import check_playability
from .classifier import classify, VoicingType
from .ranking import sort_voicings


@dataclass
class VoicingQuery:
    """Structured query for finding chord voicings."""
    root: int                                    # pitch class 0-11
    formula: ChordFormula                        # chord quality

    # Position filters
    min_fret: Optional[int] = None
    max_fret: Optional[int] = None

    # Note constraints
    bass_note: Optional[int] = None              # pitch class for lowest note
    top_note: Optional[int] = None               # pitch class for highest note
    root_string: Optional[int] = None            # string index (0=low E) where root must be

    # Voicing constraints
    inversion: Optional[int] = None              # 0=root, 1=first, etc.
    voicing_types: Optional[set[VoicingType]] = None
    min_notes: int = 3
    max_notes: int = 6
    max_span: int = 4
    allow_inner_mutes: bool = True

    # Playability
    max_difficulty: Optional[float] = None
    playable_only: bool = True

    # Output
    sort_key: str = "default"
    limit: int = 10
    offset: int = 0


@dataclass
class QueryResult:
    """Result of executing a VoicingQuery."""
    voicings: list[Voicing]
    total_matches: int
    query: VoicingQuery


def execute_query(query: VoicingQuery, fretboard: Fretboard | None = None) -> QueryResult:
    """Execute a voicing query: generate, filter, rank, paginate."""
    if fretboard is None:
        fretboard = Fretboard(STANDARD_TUNING, 24)

    # Generate all voicings for this root + formula
    gen_max_fret = query.max_fret if query.max_fret is not None else 24
    all_voicings = generate_voicings(
        root_pc=query.root,
        formula=query.formula,
        fretboard=fretboard,
        max_fret=gen_max_fret,
        max_span=query.max_span,
        min_notes=query.min_notes,
        max_notes=query.max_notes,
        allow_inner_mutes=query.allow_inner_mutes,
    )

    # Build filter chain
    filters: list[Callable[[Voicing], bool]] = []

    if query.min_fret is not None:
        min_f = query.min_fret
        # All sounding notes must be at or above min_fret (no open strings allowed)
        filters.append(lambda v, mf=min_f: all(
            f >= mf for f in v.frets if f is not None
        ))

    if query.max_fret is not None:
        max_f = query.max_fret
        filters.append(lambda v, xf=max_f: v.max_fret <= xf)

    if query.bass_note is not None:
        bass_pc = query.bass_note
        filters.append(lambda v, bp=bass_pc: v.bass_note.pitch_class == bp)

    if query.top_note is not None:
        top_pc = query.top_note
        filters.append(lambda v, tp=top_pc: v.top_note.pitch_class == tp)

    if query.root_string is not None:
        rs = query.root_string
        filters.append(lambda v, s=rs: v.root_on_string(s))

    if query.inversion is not None:
        inv = query.inversion
        filters.append(lambda v, i=inv: v.inversion == i)

    if query.voicing_types is not None:
        vtypes = query.voicing_types
        filters.append(lambda v, vt=vtypes: bool(classify(v) & vt))

    if query.playable_only:
        filters.append(lambda v: check_playability(v).is_playable)

    if query.max_difficulty is not None:
        max_d = query.max_difficulty
        filters.append(lambda v, md=max_d: check_playability(v).difficulty <= md)

    # Apply filters
    filtered = all_voicings
    for f in filters:
        filtered = [v for v in filtered if f(v)]

    # Sort
    sorted_voicings = sort_voicings(filtered, key=query.sort_key)

    total = len(sorted_voicings)

    # Paginate
    page = sorted_voicings[query.offset:query.offset + query.limit]

    return QueryResult(voicings=page, total_matches=total, query=query)
