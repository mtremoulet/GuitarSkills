"""Guitar-specific model: tuning, fretboard, note lookups."""

from __future__ import annotations

from dataclasses import dataclass
from functools import cached_property

from .theory import Note, note_name


@dataclass(frozen=True)
class GuitarTuning:
    """Defines the open string pitches for a guitar tuning."""
    name: str
    open_strings: tuple[Note, ...]  # index 0 = lowest string

    @property
    def num_strings(self) -> int:
        return len(self.open_strings)

    @cached_property
    def string_names(self) -> tuple[str, ...]:
        """Display names for each string (e.g., E A D G B e for standard)."""
        names = []
        seen: dict[int, int] = {}
        for s in self.open_strings:
            pc = s.pitch_class
            n = note_name(pc)
            count = seen.get(pc, 0)
            seen[pc] = count + 1
            # Lowercase for repeated note names (e.g., high e vs low E)
            if count > 0:
                n = n.lower()
            names.append(n)
        return tuple(names)


# Standard tuning: E2 A2 D3 G3 B3 E4
STANDARD_TUNING = GuitarTuning(
    name="standard",
    open_strings=(
        Note(4, 2),   # E2
        Note(9, 2),   # A2
        Note(2, 3),   # D3
        Note(7, 3),   # G3
        Note(11, 3),  # B3
        Note(4, 4),   # E4
    ),
)


class Fretboard:
    """Provides note lookups on a guitar fretboard."""

    def __init__(self, tuning: GuitarTuning = STANDARD_TUNING, max_fret: int = 24):
        self.tuning = tuning
        self.max_fret = max_fret
        # Precompute: _notes[string][fret] = Note
        # Precompute: _pc[string][fret] = pitch_class (int 0-11)
        self._notes: list[list[Note]] = []
        self._pc: list[list[int]] = []
        # Precompute: _frets_for_pc[string][pitch_class] = list of frets
        self._frets_for_pc: list[dict[int, list[int]]] = []

        for s_idx, open_note in enumerate(tuning.open_strings):
            string_notes = []
            string_pcs = []
            pc_frets: dict[int, list[int]] = {pc: [] for pc in range(12)}
            for fret in range(max_fret + 1):
                midi = open_note.midi + fret
                pc = midi % 12
                octave = (midi - pc) // 12 - 1
                n = Note(pc, octave)
                string_notes.append(n)
                string_pcs.append(pc)
                pc_frets[pc].append(fret)
            self._notes.append(string_notes)
            self._pc.append(string_pcs)
            self._frets_for_pc.append(pc_frets)

    def note_at(self, string: int, fret: int) -> Note:
        """Get the Note at a given string and fret position."""
        return self._notes[string][fret]

    def pitch_class_at(self, string: int, fret: int) -> int:
        """Get the pitch class (0-11) at a given string and fret position."""
        return self._pc[string][fret]

    def frets_for_pitch_class(self, string: int, pitch_class: int) -> list[int]:
        """Get all fret positions on a string that produce the given pitch class."""
        return self._frets_for_pc[string][pitch_class % 12]

    def frets_for_pitch_classes(self, string: int, pitch_classes: frozenset[int]) -> list[int]:
        """Get all fret positions on a string that produce any of the given pitch classes."""
        result = []
        for pc in pitch_classes:
            result.extend(self._frets_for_pc[string][pc % 12])
        result.sort()
        return result
