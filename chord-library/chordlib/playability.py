"""Playability analysis: finger counting, barre detection, difficulty scoring."""

from __future__ import annotations

from dataclasses import dataclass, field

from .voicing import Voicing


@dataclass
class PlayabilityResult:
    is_playable: bool
    difficulty: float          # 0.0 (easy) to 1.0 (very hard)
    requires_barre: bool
    finger_count: int          # fingers needed (barre = 1)
    barre_fret: int | None     # fret of the barre, if any
    barre_span: tuple[int, int] | None  # (low_string, high_string) of barre
    flags: list[str] = field(default_factory=list)


def check_playability(voicing: Voicing, max_fingers: int = 4) -> PlayabilityResult:
    """Analyze whether a voicing is physically playable and rate its difficulty.

    Returns a PlayabilityResult with detailed analysis.
    """
    frets = voicing.frets
    num_strings = len(frets)

    # Collect fretted positions (string_idx, fret) where fret > 0
    fretted: list[tuple[int, int]] = []
    for s, f in enumerate(frets):
        if f is not None and f > 0:
            fretted.append((s, f))

    if not fretted:
        # All open or muted — trivially playable
        return PlayabilityResult(
            is_playable=True, difficulty=0.0, requires_barre=False,
            finger_count=0, barre_fret=None, barre_span=None,
        )

    # Group by fret value
    fret_groups: dict[int, list[int]] = {}  # fret -> [string_indices]
    for s, f in fretted:
        fret_groups.setdefault(f, []).append(s)

    # Try to find a valid barre assignment
    best = _find_best_fingering(frets, fretted, fret_groups, num_strings, max_fingers)

    if best is None:
        return PlayabilityResult(
            is_playable=False, difficulty=1.0, requires_barre=False,
            finger_count=len(fretted), barre_fret=None, barre_span=None,
            flags=["too_many_fingers"],
        )

    finger_count, barre_fret, barre_span = best
    requires_barre = barre_fret is not None

    # Calculate difficulty
    difficulty = _calculate_difficulty(voicing, finger_count, requires_barre, barre_span)

    flags = []
    if voicing.has_inner_mutes:
        flags.append("inner_mute")
    if voicing.fret_span >= 4:
        flags.append("wide_stretch")
    if requires_barre and voicing.min_fret <= 2:
        flags.append("low_barre")

    return PlayabilityResult(
        is_playable=True,
        difficulty=difficulty,
        requires_barre=requires_barre,
        finger_count=finger_count,
        barre_fret=barre_fret,
        barre_span=barre_span,
        flags=flags,
    )


def _find_best_fingering(
    frets: tuple[int | None, ...],
    fretted: list[tuple[int, int]],
    fret_groups: dict[int, list[int]],
    num_strings: int,
    max_fingers: int,
) -> tuple[int, int | None, tuple[int, int] | None] | None:
    """Try to find a valid fingering. Returns (finger_count, barre_fret, barre_span) or None."""

    distinct_fret_values = sorted(fret_groups.keys())

    # First, try without barre
    if len(fretted) <= max_fingers:
        return (len(fretted), None, None)

    # Try barre on each fret that has 2+ strings
    best_fingers = 999
    best_barre_fret = None
    best_barre_span = None

    for barre_fret in distinct_fret_values:
        strings_at_fret = fret_groups[barre_fret]
        if len(strings_at_fret) < 2:
            continue

        # Barre must span contiguous strings (low to high)
        barre_low = min(strings_at_fret)
        barre_high = max(strings_at_fret)

        # Check barre validity: no string in the barre range can be:
        # - fretted at a LOWER fret than the barre (finger would block it)
        # - open (0) — the barre would press it
        barre_valid = True
        for s in range(barre_low, barre_high + 1):
            f = frets[s]
            if f is not None and 0 < f < barre_fret:
                barre_valid = False
                break
            if f == 0:
                # Open string inside barre range — barre would fret it
                barre_valid = False
                break

        if not barre_valid:
            continue

        # Count fingers: barre = 1, plus each other fretted position not covered by barre
        extra_fingers = 0
        for s, f in fretted:
            if f == barre_fret and barre_low <= s <= barre_high:
                continue  # Covered by barre
            extra_fingers += 1

        total = 1 + extra_fingers
        if total <= max_fingers and total < best_fingers:
            best_fingers = total
            best_barre_fret = barre_fret
            best_barre_span = (barre_low, barre_high)

    if best_barre_fret is not None:
        return (best_fingers, best_barre_fret, best_barre_span)

    return None


def _calculate_difficulty(
    voicing: Voicing,
    finger_count: int,
    requires_barre: bool,
    barre_span: tuple[int, int] | None,
) -> float:
    """Calculate a difficulty score from 0.0 (easy) to 1.0 (very hard)."""
    score = 0.0

    # Finger count contribution (0-4 fingers → 0.0-0.4)
    score += finger_count * 0.1

    # Fret span contribution
    span = voicing.fret_span
    if span >= 4:
        score += 0.2
    elif span >= 3:
        score += 0.1

    # Barre adds difficulty
    if requires_barre:
        score += 0.15
        # Wide barre is harder
        if barre_span and (barre_span[1] - barre_span[0]) >= 4:
            score += 0.1

    # Low fret stretches are harder (frets are wider apart)
    if voicing.min_fret <= 2 and span >= 3:
        score += 0.1

    # Inner mutes add difficulty (require careful muting technique)
    if voicing.has_inner_mutes:
        score += 0.15

    # More sounding strings is slightly harder to fret cleanly
    if voicing.num_sounding >= 5:
        score += 0.05

    return min(score, 1.0)
