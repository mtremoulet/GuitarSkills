"""Voicing generation engine: finds all physically playable chord voicings."""

from __future__ import annotations

from .theory import ChordFormula, IntervalRole
from .guitar import Fretboard, STANDARD_TUNING
from .voicing import Voicing


def generate_voicings(
    root_pc: int,
    formula: ChordFormula,
    fretboard: Fretboard | None = None,
    *,
    max_fret: int = 24,
    max_span: int = 4,
    min_notes: int = 3,
    max_notes: int = 6,
    allow_inner_mutes: bool = True,
) -> list[Voicing]:
    """Generate all physically playable voicings for a chord.

    Args:
        root_pc: Root pitch class (0-11).
        formula: The chord formula to voice.
        fretboard: Fretboard instance (defaults to standard tuning, 24 frets).
        max_fret: Maximum fret to consider.
        max_span: Maximum fret span for fretted notes.
        min_notes: Minimum sounding strings.
        max_notes: Maximum sounding strings.
        allow_inner_mutes: Allow muted strings between sounding strings.

    Returns:
        List of valid Voicing objects, deduplicated.
    """
    if fretboard is None:
        fretboard = Fretboard(STANDARD_TUNING, max_fret)

    num_strings = fretboard.tuning.num_strings

    # Compute target pitch classes (offset from root, mod 12)
    target_pcs = set()
    for iv in formula.intervals:
        if iv.role != IntervalRole.AVOID:
            target_pcs.add((root_pc + iv.semitones) % 12)

    required_pcs = set()
    for iv in formula.intervals:
        if iv.role in (IntervalRole.REQUIRED, IntervalRole.PREFERRED):
            required_pcs.add((root_pc + iv.semitones) % 12)

    # For each string, precompute which frets produce chord tones
    # chord_frets[string] = list of (fret, pitch_class) for valid chord tones
    chord_frets: list[list[tuple[int, int]]] = []
    for s in range(num_strings):
        frets_for_string = []
        for pc in target_pcs:
            for fret in fretboard.frets_for_pitch_class(s, pc):
                if fret <= max_fret:
                    frets_for_string.append((fret, pc))
        frets_for_string.sort()
        chord_frets.append(frets_for_string)

    # Results collected here
    seen: set[tuple[int | None, ...]] = set()
    results: list[Voicing] = []

    def _search(
        string: int,
        assignment: list[int | None],
        fretted_min: int,
        fretted_max: int,
        sounding: int,
        pcs_covered: set[int],
        last_sounding: int,
    ) -> None:
        """Backtracking search, string by string from low to high.

        Args:
            string: Current string index being assigned.
            assignment: Fret assignments so far (list of length num_strings, partially filled).
            fretted_min: Minimum fretted value so far (999 if no fretted notes yet).
            fretted_max: Maximum fretted value so far (0 if no fretted notes yet).
            sounding: Number of sounding strings assigned so far.
            pcs_covered: Set of pitch classes covered so far.
            last_sounding: Index of the last sounding string (-1 if none).
        """
        if string == num_strings:
            # Check completeness
            if sounding < min_notes:
                return
            if not required_pcs.issubset(pcs_covered):
                return
            fret_tuple = tuple(assignment)
            if fret_tuple not in seen:
                seen.add(fret_tuple)
                results.append(Voicing(fret_tuple, root_pc, formula, fretboard))
            return

        remaining_strings = num_strings - string
        max_possible_sounding = sounding + remaining_strings

        # Pruning: can we still reach min_notes?
        if max_possible_sounding < min_notes:
            return

        # Pruning: can we still cover all required PCs?
        # Check which required PCs are still missing
        missing_pcs = required_pcs - pcs_covered
        if missing_pcs:
            # Can remaining strings provide the missing PCs?
            coverable = set()
            for s in range(string, num_strings):
                for _, pc in chord_frets[s]:
                    coverable.add(pc)
            if not missing_pcs.issubset(coverable):
                return

        # Option 1: Mute this string
        if sounding + remaining_strings >= min_notes:  # Can still reach min_notes
            # Inner mute check
            can_mute = True
            if not allow_inner_mutes and last_sounding >= 0:
                # If we mute here, any future sounding string creates an inner mute
                # We allow it tentatively; the final check catches it
                pass
            if can_mute:
                assignment[string] = None
                _search(string + 1, assignment, fretted_min, fretted_max,
                        sounding, pcs_covered, last_sounding)

        # Option 2: Play this string at each valid chord tone fret
        if sounding < max_notes:
            for fret, pc in chord_frets[string]:
                # Span check
                if fret > 0:
                    new_min = min(fretted_min, fret)
                    new_max = max(fretted_max, fret)
                    if new_max - new_min > max_span:
                        continue
                else:
                    new_min = fretted_min
                    new_max = fretted_max

                # Inner mute check: if we have a gap since last sounding string
                if not allow_inner_mutes and last_sounding >= 0 and string - last_sounding > 1:
                    # There's at least one muted string between last_sounding and this one
                    continue

                new_pcs = pcs_covered | {pc}
                assignment[string] = fret
                _search(string + 1, assignment, new_min, new_max,
                        sounding + 1, new_pcs, string)

        # Restore (backtrack)
        assignment[string] = None

    # Run the search
    assignment = [None] * num_strings
    _search(0, assignment, 999, 0, 0, set(), -1)

    return results
