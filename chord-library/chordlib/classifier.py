"""Voicing type classification: open, barre, shell, drop-2, drop-3, etc."""

from __future__ import annotations

from enum import Enum

from .voicing import Voicing
from .playability import check_playability


class VoicingType(Enum):
    OPEN = "open"
    BARRE = "barre"
    SHELL = "shell"
    DROP_2 = "drop_2"
    DROP_3 = "drop_3"
    DROP_2_4 = "drop_2_4"
    CLOSE = "close"
    SPREAD = "spread"


def classify(voicing: Voicing) -> set[VoicingType]:
    """Classify a voicing into one or more types.

    A voicing can have multiple classifications (e.g., open + shell).
    """
    types: set[VoicingType] = set()

    # Open position: uses at least one open string, all fretted notes within frets 1-4
    has_open = any(f == 0 for f in voicing.frets if f is not None)
    all_low = all(f <= 4 for f in voicing.frets if f is not None and f > 0)
    if has_open and all_low:
        types.add(VoicingType.OPEN)

    # Barre: check via playability
    pr = check_playability(voicing)
    if pr.requires_barre:
        types.add(VoicingType.BARRE)

    # Shell voicing: 3-4 sounding notes, must include root + (3rd or sus) + 7th
    if voicing.num_sounding in (3, 4):
        pc_offsets = set()
        for n in voicing.sounding_notes:
            pc_offsets.add((n.pitch_class - voicing.root_pc) % 12)
        has_root = 0 in pc_offsets
        has_third = bool(pc_offsets & {3, 4, 5})  # b3, 3, or 4(sus)
        has_seventh = bool(pc_offsets & {9, 10, 11})  # 6, b7, or 7
        if has_root and has_third and has_seventh:
            types.add(VoicingType.SHELL)

    # Drop voicing detection
    drop_type = _detect_drop_voicing(voicing)
    if drop_type:
        types.add(drop_type)

    # Close voicing: all sounding notes within one octave
    if voicing.num_sounding >= 3:
        notes_sorted = sorted(voicing.sounding_notes, key=lambda n: n.midi)
        span_semitones = notes_sorted[-1].midi - notes_sorted[0].midi
        if span_semitones <= 12:
            types.add(VoicingType.CLOSE)

    # Spread: notes span more than 2 octaves
    if voicing.num_sounding >= 3:
        notes_sorted = sorted(voicing.sounding_notes, key=lambda n: n.midi)
        if notes_sorted[-1].midi - notes_sorted[0].midi > 24:
            types.add(VoicingType.SPREAD)

    return types


def _detect_drop_voicing(voicing: Voicing) -> VoicingType | None:
    """Detect if a voicing is a drop-2, drop-3, or drop-2-4 voicing.

    Works by checking if the voicing matches the pattern of a close-position
    chord with specific voices displaced down by an octave.
    """
    sounding = voicing.sounding_notes
    if len(sounding) != 4:
        return None

    # Get the 4 pitch classes in this voicing
    pcs = [(n.pitch_class - voicing.root_pc) % 12 for n in sounding]
    midi_vals = [n.midi for n in sounding]

    # Sort by MIDI to get actual low-to-high order
    indexed = sorted(zip(midi_vals, pcs), key=lambda x: x[0])
    actual_pcs_low_to_high = [pc for _, pc in indexed]
    actual_midis = [m for m, _ in indexed]

    # Build the close-position voicing (all within one octave, stacked high-to-low)
    unique_pcs = []
    seen = set()
    for pc in actual_pcs_low_to_high:
        if pc not in seen:
            unique_pcs.append(pc)
            seen.add(pc)

    if len(unique_pcs) != 4:
        # Has doubled notes — not a standard drop voicing
        return None

    # The close position arrangement stacks these PCs within one octave
    # from the top note down. The "top" voice in close position is the
    # highest note's PC.
    # Close position (top to bottom): voice1 (top), voice2, voice3, voice4 (bottom)
    # In our actual voicing, we check which close-position voice was dropped.

    # Sort PCs to establish close-position order (ascending from root perspective)
    sorted_pcs = sorted(unique_pcs)

    # Find which rotation puts the top note of the actual voicing on top
    top_pc = actual_pcs_low_to_high[-1]

    # Rotate so top_pc is last (highest in close position)
    rotation = None
    for rot in range(4):
        rotated = sorted_pcs[rot:] + sorted_pcs[:rot]
        if rotated[-1] == top_pc:
            rotation = rotated
            break

    if rotation is None:
        return None

    # Close position (bottom to top): rotation[0], rotation[1], rotation[2], rotation[3]
    # Drop-2: voice 2 from top (rotation[2]) drops an octave → becomes the bass
    # Drop-3: voice 3 from top (rotation[1]) drops an octave → becomes the bass
    # Drop-2-4: voices 2 and 4 from top drop

    # Check: is the bass note's PC the one that "should" be voice 2 from top?
    bass_pc = actual_pcs_low_to_high[0]

    # Voice numbering from top: 1=rotation[3], 2=rotation[2], 3=rotation[1], 4=rotation[0]
    voice_2_from_top = rotation[2]
    voice_3_from_top = rotation[1]

    if bass_pc == voice_2_from_top:
        # Verify: the bass note is roughly an octave below where it would be in close position
        # (it was dropped down)
        return VoicingType.DROP_2

    if bass_pc == voice_3_from_top:
        return VoicingType.DROP_3

    # Drop 2-4: both voice 2 and voice 4 from top are in the lower half
    # voice 4 from top = rotation[0], voice 2 from top = rotation[2]
    # In drop 2-4, the bottom two notes should be voice 4 and voice 2
    if len(actual_pcs_low_to_high) >= 4:
        bottom_two_pcs = set(actual_pcs_low_to_high[:2])
        if bottom_two_pcs == {rotation[0], rotation[2]}:
            return VoicingType.DROP_2_4

    return None
