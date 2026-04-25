"""Voicing ranking and sorting."""

from __future__ import annotations

from .voicing import Voicing
from .playability import check_playability


def rank_voicing(voicing: Voicing) -> tuple:
    """Return a sort key tuple for ranking voicings. Lower = better.

    Priority order:
    1. Fewer muted strings (more complete voicings first)
    2. Smaller fret span (more compact shapes)
    3. Lower difficulty score
    4. Root in bass preferred (root position first)
    5. Lower position on neck
    """
    num_muted = len(voicing.frets) - voicing.num_sounding
    pr = check_playability(voicing)
    root_in_bass = 0 if voicing.bass_note.pitch_class == voicing.root_pc else 1

    return (
        num_muted,
        voicing.fret_span,
        pr.difficulty,
        root_in_bass,
        voicing.min_fret,
    )


def sort_voicings(voicings: list[Voicing], key: str = "default") -> list[Voicing]:
    """Sort voicings by the given ranking strategy.

    Keys:
        default: balanced ranking (fewer mutes, smaller span, lower difficulty)
        compact: smallest fret span first
        position_asc: lowest fret position first
        position_desc: highest fret position first
        open_strings: most open strings first
    """
    if key == "compact":
        return sorted(voicings, key=lambda v: (v.fret_span, v.min_fret))
    elif key == "position_asc":
        return sorted(voicings, key=lambda v: (v.min_fret, v.fret_span))
    elif key == "position_desc":
        return sorted(voicings, key=lambda v: (-v.min_fret, v.fret_span))
    elif key == "open_strings":
        return sorted(voicings, key=lambda v: (
            -sum(1 for f in v.frets if f == 0),
            v.fret_span,
        ))
    else:
        return sorted(voicings, key=rank_voicing)
