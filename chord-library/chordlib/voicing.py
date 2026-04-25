"""Voicing dataclass: represents a specific chord fingering on the guitar."""

from __future__ import annotations

from dataclasses import dataclass
from functools import cached_property
from typing import Optional

from .theory import Note, ChordFormula, spell_note_in_key, spell_note_for_degree, PREFER_FLATS
from .guitar import Fretboard, GuitarTuning, STANDARD_TUNING


@dataclass(frozen=True)
class Voicing:
    """A specific chord voicing on the guitar.

    frets: tuple of 6 values (low E to high e).
           None = muted (X), 0 = open, 1-24 = fretted.
    root_pc: pitch class of the chord root (0-11).
    formula: the ChordFormula this voicing represents.
    fretboard: the Fretboard used for note lookups.
    """
    frets: tuple[Optional[int], ...]
    root_pc: int
    formula: ChordFormula
    fretboard: Fretboard

    @cached_property
    def notes(self) -> tuple[Optional[Note], ...]:
        """Concrete Note per string, None for muted."""
        result = []
        for s_idx, fret in enumerate(self.frets):
            if fret is None:
                result.append(None)
            else:
                result.append(self.fretboard.note_at(s_idx, fret))
        return tuple(result)

    @cached_property
    def sounding_notes(self) -> tuple[Note, ...]:
        """Only the non-muted notes, ordered low string to high string."""
        return tuple(n for n in self.notes if n is not None)

    @cached_property
    def sounding_indices(self) -> tuple[int, ...]:
        """String indices that are sounding (not muted)."""
        return tuple(i for i, f in enumerate(self.frets) if f is not None)

    @cached_property
    def num_sounding(self) -> int:
        return len(self.sounding_notes)

    @cached_property
    def bass_note(self) -> Note:
        """Lowest sounding note."""
        return self.sounding_notes[0]

    @cached_property
    def top_note(self) -> Note:
        """Highest sounding note (highest string that's not muted)."""
        return self.sounding_notes[-1]

    @cached_property
    def _use_flats(self) -> bool:
        return PREFER_FLATS.get(self.root_pc, False)

    @cached_property
    def note_names(self) -> tuple[Optional[str], ...]:
        """Note name per string, None for muted. Spelled correctly for chord context."""
        result = []
        for n, degree in zip(self.notes, self.interval_names):
            if n is None:
                result.append(None)
            else:
                pc_offset = (n.pitch_class - self.root_pc) % 12
                result.append(spell_note_for_degree(self.root_pc, pc_offset, degree or ""))
        return tuple(result)

    @cached_property
    def interval_names(self) -> tuple[Optional[str], ...]:
        """Chord degree per string (R, b3, 5, etc.), None for muted."""
        result = []
        for n in self.notes:
            if n is None:
                result.append(None)
            else:
                pc_offset = (n.pitch_class - self.root_pc) % 12
                result.append(self.formula.degree_name(pc_offset))
        return tuple(result)

    @cached_property
    def inversion(self) -> int:
        """0 = root position, 1 = first inversion, etc.

        Determined by which chord tone is in the bass.
        """
        bass_pc_offset = (self.bass_note.pitch_class - self.root_pc) % 12
        # Find the position of this interval in the formula's sorted intervals
        sorted_pcs = sorted(set(iv.pitch_class for iv in self.formula.intervals
                                if iv.display_name != "R"))
        if bass_pc_offset == 0:
            return 0
        try:
            return sorted_pcs.index(bass_pc_offset) + 1
        except ValueError:
            return 0

    @cached_property
    def inversion_name(self) -> str:
        inv = self.inversion
        if inv == 0:
            return "root position"
        names = {1: "1st inversion", 2: "2nd inversion", 3: "3rd inversion",
                 4: "4th inversion", 5: "5th inversion"}
        return names.get(inv, f"{inv}th inversion")

    @cached_property
    def fret_span(self) -> int:
        """Difference between highest and lowest fretted (non-open, non-muted) positions."""
        fretted = [f for f in self.frets if f is not None and f > 0]
        if not fretted:
            return 0
        return max(fretted) - min(fretted)

    @cached_property
    def min_fret(self) -> int:
        """Lowest fretted position (excluding open strings). 0 if all open."""
        fretted = [f for f in self.frets if f is not None and f > 0]
        return min(fretted) if fretted else 0

    @cached_property
    def max_fret(self) -> int:
        """Highest fretted position."""
        fretted = [f for f in self.frets if f is not None and f > 0]
        return max(fretted) if fretted else 0

    @cached_property
    def has_inner_mutes(self) -> bool:
        """True if there's a muted string between two sounding strings."""
        sounding = self.sounding_indices
        if len(sounding) < 2:
            return False
        for i in range(sounding[0], sounding[-1] + 1):
            if self.frets[i] is None:
                return True
        return False

    @cached_property
    def pitch_class_set(self) -> frozenset[int]:
        """Set of unique pitch classes in this voicing."""
        return frozenset(n.pitch_class for n in self.sounding_notes)

    def root_on_string(self, string: int) -> bool:
        """Check if the root is on the given string (0-indexed from low E)."""
        n = self.notes[string]
        return n is not None and n.pitch_class == self.root_pc
