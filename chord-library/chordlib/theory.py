"""Music theory primitives: pitch classes, intervals, notes, and chord formulas."""

from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum, Enum
from functools import cached_property
from typing import Optional


class PitchClass(IntEnum):
    C = 0
    Cs = 1
    D = 2
    Ds = 3
    E = 4
    F = 5
    Fs = 6
    G = 7
    Gs = 8
    A = 9
    As = 10
    B = 11


# Maps string names to pitch class values (both sharp and flat spellings)
NOTE_NAMES_SHARP = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
NOTE_NAMES_FLAT = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]

# Preferred spelling per key context: sharp keys use sharps, flat keys use flats
# Index by root pitch class
PREFER_FLATS = {
    PitchClass.C: False,
    PitchClass.Cs: False,  # C# / Db — default to sharps
    PitchClass.D: False,
    PitchClass.Ds: True,   # Eb
    PitchClass.E: False,
    PitchClass.F: True,
    PitchClass.Fs: False,  # F# / Gb — default to sharps
    PitchClass.G: False,
    PitchClass.Gs: True,   # Ab
    PitchClass.A: False,
    PitchClass.As: True,   # Bb
    PitchClass.B: False,
}

# Parse any note name string to a PitchClass
_NAME_TO_PC: dict[str, int] = {}
for i, name in enumerate(NOTE_NAMES_SHARP):
    _NAME_TO_PC[name] = i
    _NAME_TO_PC[name.lower()] = i
for i, name in enumerate(NOTE_NAMES_FLAT):
    _NAME_TO_PC[name] = i
    _NAME_TO_PC[name.lower()] = i
# Additional aliases
_NAME_TO_PC["Db"] = 1
_NAME_TO_PC["db"] = 1
_NAME_TO_PC["Eb"] = 3
_NAME_TO_PC["eb"] = 3
_NAME_TO_PC["Gb"] = 6
_NAME_TO_PC["gb"] = 6
_NAME_TO_PC["Ab"] = 8
_NAME_TO_PC["ab"] = 8
_NAME_TO_PC["Bb"] = 10
_NAME_TO_PC["bb"] = 10


def parse_note_name(name: str) -> int:
    """Parse a note name like 'C', 'F#', 'Bb' to a pitch class integer (0-11)."""
    if name in _NAME_TO_PC:
        return _NAME_TO_PC[name]
    raise ValueError(f"Unknown note name: {name!r}")


def note_name(pc: int, use_flats: bool = False) -> str:
    """Return the display name for a pitch class."""
    pc = pc % 12
    if use_flats:
        return NOTE_NAMES_FLAT[pc]
    return NOTE_NAMES_SHARP[pc]


def spell_note_in_key(pc: int, root_pc: int) -> str:
    """Return the note name for a pitch class, spelled appropriately for the given root."""
    return note_name(pc, use_flats=PREFER_FLATS.get(PitchClass(root_pc), False))


# Diatonic note spelling: maps (root_pc, interval_semitones_mod12) to correct note name.
# The natural letter names cycle: C D E F G A B
_LETTER_NAMES = ["C", "D", "E", "F", "G", "A", "B"]
_LETTER_TO_PC = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}
_PC_TO_LETTER_INDEX = {0: 0, 2: 1, 4: 2, 5: 3, 7: 4, 9: 5, 11: 6}

# Map interval degree number to letter offset from root (0-based)
# degree 1 (root) = 0 letters, degree 2 = 1 letter, ..., degree 7 = 6 letters
_DEGREE_TO_LETTER_OFFSET = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6}

# Map semitone offset (mod 12) to (degree_number, accidental_string)
# This handles the standard interval interpretations
_SEMITONE_TO_DEGREE: dict[int, tuple[int, str]] = {
    0: (1, ""),      # root / octave
    1: (2, "b"),     # b2 / b9
    2: (2, ""),      # 2 / 9
    3: (3, "b"),     # b3
    4: (3, ""),      # 3
    5: (4, ""),      # 4 / 11
    6: (5, "b"),     # b5 / #4/#11 — default to b5
    7: (5, ""),      # 5
    8: (6, "b"),     # b6 / #5 — ambiguous, handle via degree_name
    9: (6, ""),      # 6 / 13 / bb7
    10: (7, "b"),    # b7
    11: (7, ""),     # 7
}

# Override for sharp intervals: when the degree name starts with #, use sharp spelling
_SHARP_DEGREE_SPELLINGS: dict[int, tuple[int, str]] = {
    6: (4, "#"),     # #11 = sharp 4th degree (e.g., F# in C)
    8: (5, "#"),     # #5 = sharp 5th degree (e.g., G# in C)
    15: (2, "#"),    # #9 = sharp 9th = sharp 2nd degree (e.g., D# in C) — but wait, #9 of C is D#
}


def spell_note_for_degree(root_pc: int, semitone_offset: int, degree_name: str = "") -> str:
    """Spell a note correctly based on its chord degree context.

    Uses the degree name hint to determine whether to use sharp or flat spelling.
    E.g., b7 of C → Bb (not A#), #5 of C → G# (not Ab).
    """
    pc = (root_pc + semitone_offset) % 12

    # Find the root's letter
    # First, determine root's natural letter name
    root_letter_idx = _find_root_letter_index(root_pc)

    semitone_mod = semitone_offset % 12

    # Check if degree name suggests sharp or flat
    is_sharp_degree = degree_name.startswith("#")
    is_flat_degree = degree_name.startswith("b") and degree_name != "bb7"
    is_double_flat = degree_name.startswith("bb")

    if is_double_flat:
        # bb7: degree 7, double-flatted
        degree_num = 7
        letter_offset = _DEGREE_TO_LETTER_OFFSET[degree_num]
        target_letter_idx = (root_letter_idx + letter_offset) % 7
        target_letter = _LETTER_NAMES[target_letter_idx]
        natural_pc = _LETTER_TO_PC[target_letter]
        diff = (pc - natural_pc) % 12
        if diff == 0:
            return target_letter
        elif diff == 10:  # -2 semitones
            return target_letter + "bb"
        elif diff == 11:  # -1 semitone
            return target_letter + "b"
        # Fallback
        return note_name(pc, use_flats=True)
    elif is_sharp_degree and semitone_mod in _SHARP_DEGREE_SPELLINGS:
        degree_num, accidental = _SHARP_DEGREE_SPELLINGS[semitone_mod]
        letter_offset = _DEGREE_TO_LETTER_OFFSET[degree_num]
        target_letter_idx = (root_letter_idx + letter_offset) % 7
        target_letter = _LETTER_NAMES[target_letter_idx]
        return target_letter + accidental
    elif semitone_mod in _SEMITONE_TO_DEGREE:
        degree_num, accidental = _SEMITONE_TO_DEGREE[semitone_mod]

        # Override for #5 when degree name says so
        if is_sharp_degree:
            # For any sharp degree, compute from the base degree
            try:
                base_degree = int(degree_name.lstrip("#"))
                if base_degree > 7:
                    base_degree = ((base_degree - 1) % 7) + 1
                degree_num = base_degree
                accidental = "#"
            except ValueError:
                pass

        letter_offset = _DEGREE_TO_LETTER_OFFSET[degree_num]
        target_letter_idx = (root_letter_idx + letter_offset) % 7
        target_letter = _LETTER_NAMES[target_letter_idx]
        natural_pc = _LETTER_TO_PC[target_letter]
        diff = (pc - natural_pc) % 12
        if diff == 0:
            return target_letter
        elif diff == 1:
            return target_letter + "#"
        elif diff == 11:
            return target_letter + "b"
        elif diff == 10:
            return target_letter + "bb"
        elif diff == 2:
            return target_letter + "##"
        # Fallback
        return note_name(pc, use_flats=(accidental == "b"))

    # Fallback
    return note_name(pc, use_flats=PREFER_FLATS.get(PitchClass(root_pc), False))


def _find_root_letter_index(root_pc: int) -> int:
    """Find the letter index (0-6) for a root pitch class.

    For natural notes, this is exact. For sharps/flats, prefer the most common spelling.
    """
    root_pc = root_pc % 12
    if root_pc in _PC_TO_LETTER_INDEX:
        return _PC_TO_LETTER_INDEX[root_pc]
    # For accidentals, use the common spelling
    # C#/Db=1 → C# (letter C, idx 0) or Db (letter D, idx 1)
    # We prefer: Db→D, Eb→E, F#→F, Ab→A, Bb→B
    accidental_map = {1: 1, 3: 2, 6: 3, 8: 5, 10: 6}  # Db, Eb, Gb, Ab, Bb
    return accidental_map.get(root_pc, 0)


class Interval(IntEnum):
    UNISON = 0
    MINOR_2ND = 1
    MAJOR_2ND = 2
    MINOR_3RD = 3
    MAJOR_3RD = 4
    PERFECT_4TH = 5
    TRITONE = 6
    PERFECT_5TH = 7
    MINOR_6TH = 8
    MAJOR_6TH = 9
    MINOR_7TH = 10
    MAJOR_7TH = 11
    OCTAVE = 12
    MINOR_9TH = 13
    MAJOR_9TH = 14
    AUGMENTED_9TH = 15
    MINOR_10TH = 15
    MAJOR_10TH = 16
    PERFECT_11TH = 17
    SHARP_11TH = 18
    PERFECT_12TH = 19
    MINOR_13TH = 20
    MAJOR_13TH = 21


@dataclass(frozen=True)
class Note:
    """A concrete pitch: pitch class + octave."""
    pitch_class: int  # 0-11
    octave: int

    @property
    def midi(self) -> int:
        return (self.octave + 1) * 12 + self.pitch_class

    def __lt__(self, other: Note) -> bool:
        return self.midi < other.midi

    def __le__(self, other: Note) -> bool:
        return self.midi <= other.midi

    def __gt__(self, other: Note) -> bool:
        return self.midi > other.midi

    def __ge__(self, other: Note) -> bool:
        return self.midi >= other.midi

    def name(self, use_flats: bool = False) -> str:
        return note_name(self.pitch_class, use_flats)

    def name_in_key(self, root_pc: int) -> str:
        return spell_note_in_key(self.pitch_class, root_pc)

    def __repr__(self) -> str:
        return f"Note({NOTE_NAMES_SHARP[self.pitch_class]}{self.octave})"


class IntervalRole(Enum):
    REQUIRED = "required"
    PREFERRED = "preferred"
    OPTIONAL = "optional"
    AVOID = "avoid"


@dataclass(frozen=True)
class FormulaInterval:
    """One interval in a chord formula."""
    semitones: int          # 0-23 (compound intervals)
    display_name: str       # "R", "b3", "5", "b7", "9", "#11", "13", etc.
    role: IntervalRole

    @property
    def pitch_class(self) -> int:
        return self.semitones % 12


def _r(semitones: int, name: str, role: str = "required") -> FormulaInterval:
    """Shorthand for building FormulaInterval."""
    return FormulaInterval(semitones, name, IntervalRole(role))


@dataclass(frozen=True)
class ChordFormula:
    """Defines a chord type by its intervals from the root."""
    name: str
    symbol: str
    intervals: tuple[FormulaInterval, ...]
    aliases: tuple[str, ...] = ()

    @cached_property
    def pitch_classes(self) -> frozenset[int]:
        return frozenset(iv.pitch_class for iv in self.intervals if iv.role != IntervalRole.AVOID)

    @cached_property
    def required_pitch_classes(self) -> frozenset[int]:
        return frozenset(
            iv.pitch_class for iv in self.intervals
            if iv.role in (IntervalRole.REQUIRED, IntervalRole.PREFERRED)
        )

    @cached_property
    def interval_by_pc(self) -> dict[int, FormulaInterval]:
        """Map pitch class offset -> FormulaInterval (first match wins for display)."""
        result: dict[int, FormulaInterval] = {}
        for iv in self.intervals:
            if iv.role != IntervalRole.AVOID and iv.pitch_class not in result:
                result[iv.pitch_class] = iv
        return result

    def degree_name(self, pc_offset: int) -> str:
        """Return the degree display name for a pitch class offset from root."""
        iv = self.interval_by_pc.get(pc_offset % 12)
        return iv.display_name if iv else "?"


# ─── Complete Chord Formula Registry ────────────────────────────────────────

CHORD_FORMULAS: dict[str, ChordFormula] = {}


def _register(formula: ChordFormula) -> None:
    CHORD_FORMULAS[formula.symbol] = formula
    for alias in formula.aliases:
        CHORD_FORMULAS[alias] = formula


# ── Triads ──

_register(ChordFormula(
    "major", "",
    (_r(0, "R"), _r(4, "3"), _r(7, "5")),
    aliases=("maj", "major", "M"),
))

_register(ChordFormula(
    "minor", "m",
    (_r(0, "R"), _r(3, "b3"), _r(7, "5")),
    aliases=("min", "minor", "-"),
))

_register(ChordFormula(
    "diminished", "dim",
    (_r(0, "R"), _r(3, "b3"), _r(6, "b5")),
    aliases=("o",),
))

_register(ChordFormula(
    "augmented", "aug",
    (_r(0, "R"), _r(4, "3"), _r(8, "#5")),
    aliases=("+",),
))

_register(ChordFormula(
    "suspended 2nd", "sus2",
    (_r(0, "R"), _r(2, "2"), _r(7, "5")),
))

_register(ChordFormula(
    "suspended 4th", "sus4",
    (_r(0, "R"), _r(5, "4"), _r(7, "5")),
    aliases=("sus",),
))

_register(ChordFormula(
    "power chord", "5",
    (_r(0, "R"), _r(7, "5")),
))

# ── Seventh Chords ──

_register(ChordFormula(
    "dominant 7th", "7",
    (_r(0, "R"), _r(4, "3"), _r(7, "5", "optional"), _r(10, "b7")),
    aliases=("dom7",),
))

_register(ChordFormula(
    "major 7th", "maj7",
    (_r(0, "R"), _r(4, "3"), _r(7, "5", "optional"), _r(11, "7")),
    aliases=("M7", "major7"),
))

_register(ChordFormula(
    "minor 7th", "m7",
    (_r(0, "R"), _r(3, "b3"), _r(7, "5", "optional"), _r(10, "b7")),
    aliases=("min7", "-7"),
))

_register(ChordFormula(
    "diminished 7th", "dim7",
    (_r(0, "R"), _r(3, "b3"), _r(6, "b5"), _r(9, "bb7")),
    aliases=("o7",),
))

_register(ChordFormula(
    "half-diminished 7th", "m7b5",
    (_r(0, "R"), _r(3, "b3"), _r(6, "b5"), _r(10, "b7")),
    aliases=("ø", "ø7", "min7b5"),
))

_register(ChordFormula(
    "minor-major 7th", "mMaj7",
    (_r(0, "R"), _r(3, "b3"), _r(7, "5", "optional"), _r(11, "7")),
    aliases=("mM7", "minMaj7"),
))

_register(ChordFormula(
    "augmented 7th", "aug7",
    (_r(0, "R"), _r(4, "3"), _r(8, "#5"), _r(10, "b7")),
    aliases=("7#5", "+7"),
))

_register(ChordFormula(
    "augmented major 7th", "augMaj7",
    (_r(0, "R"), _r(4, "3"), _r(8, "#5"), _r(11, "7")),
    aliases=("maj7#5", "+M7"),
))

_register(ChordFormula(
    "dominant 7th sus4", "7sus4",
    (_r(0, "R"), _r(5, "4"), _r(7, "5", "optional"), _r(10, "b7")),
    aliases=("7sus",),
))

_register(ChordFormula(
    "dominant 7th flat 5", "7b5",
    (_r(0, "R"), _r(4, "3"), _r(6, "b5"), _r(10, "b7")),
))

# ── Sixth Chords ──

_register(ChordFormula(
    "major 6th", "6",
    (_r(0, "R"), _r(4, "3"), _r(7, "5", "optional"), _r(9, "6")),
    aliases=("maj6",),
))

_register(ChordFormula(
    "minor 6th", "m6",
    (_r(0, "R"), _r(3, "b3"), _r(7, "5", "optional"), _r(9, "6")),
    aliases=("min6", "-6"),
))

_register(ChordFormula(
    "6/9", "6/9",
    (_r(0, "R"), _r(4, "3"), _r(7, "5", "optional"), _r(9, "6"), _r(14, "9")),
    aliases=("69",),
))

_register(ChordFormula(
    "minor 6/9", "m6/9",
    (_r(0, "R"), _r(3, "b3"), _r(7, "5", "optional"), _r(9, "6"), _r(14, "9")),
    aliases=("min69",),
))

# ── Ninth Chords ──

_register(ChordFormula(
    "dominant 9th", "9",
    (_r(0, "R"), _r(4, "3"), _r(7, "5", "optional"), _r(10, "b7"), _r(14, "9")),
    aliases=("dom9",),
))

_register(ChordFormula(
    "major 9th", "maj9",
    (_r(0, "R"), _r(4, "3"), _r(7, "5", "optional"), _r(11, "7"), _r(14, "9")),
    aliases=("M9",),
))

_register(ChordFormula(
    "minor 9th", "m9",
    (_r(0, "R"), _r(3, "b3"), _r(7, "5", "optional"), _r(10, "b7"), _r(14, "9")),
    aliases=("min9", "-9"),
))

_register(ChordFormula(
    "dominant 7th sharp 9", "7#9",
    (_r(0, "R"), _r(4, "3"), _r(7, "5", "optional"), _r(10, "b7"), _r(15, "#9")),
))

_register(ChordFormula(
    "dominant 7th flat 9", "7b9",
    (_r(0, "R"), _r(4, "3"), _r(7, "5", "optional"), _r(10, "b7"), _r(13, "b9")),
))

_register(ChordFormula(
    "dominant 9th sharp 5", "9#5",
    (_r(0, "R"), _r(4, "3"), _r(8, "#5"), _r(10, "b7"), _r(14, "9")),
))

_register(ChordFormula(
    "dominant 9th flat 5", "9b5",
    (_r(0, "R"), _r(4, "3"), _r(6, "b5"), _r(10, "b7"), _r(14, "9")),
))

_register(ChordFormula(
    "dominant 7th sharp 9 sharp 5", "7#9#5",
    (_r(0, "R"), _r(4, "3"), _r(8, "#5"), _r(10, "b7"), _r(15, "#9")),
))

_register(ChordFormula(
    "dominant 7th flat 9 flat 5", "7b9b5",
    (_r(0, "R"), _r(4, "3"), _r(6, "b5"), _r(10, "b7"), _r(13, "b9")),
))

# ── Add Chords ──

_register(ChordFormula(
    "add 9", "add9",
    (_r(0, "R"), _r(4, "3"), _r(7, "5"), _r(14, "9")),
))

_register(ChordFormula(
    "minor add 9", "madd9",
    (_r(0, "R"), _r(3, "b3"), _r(7, "5"), _r(14, "9")),
))

_register(ChordFormula(
    "add 11", "add11",
    (_r(0, "R"), _r(4, "3"), _r(7, "5"), _r(17, "11")),
))

_register(ChordFormula(
    "add 13", "add13",
    (_r(0, "R"), _r(4, "3"), _r(7, "5"), _r(21, "13")),
))

# ── Eleventh Chords ──

_register(ChordFormula(
    "dominant 11th", "11",
    (_r(0, "R"), _r(4, "3", "optional"), _r(7, "5", "optional"),
     _r(10, "b7"), _r(14, "9", "preferred"), _r(17, "11")),
))

_register(ChordFormula(
    "major 11th", "maj11",
    (_r(0, "R"), _r(4, "3", "optional"), _r(7, "5", "optional"),
     _r(11, "7"), _r(14, "9", "preferred"), _r(17, "11")),
))

_register(ChordFormula(
    "minor 11th", "m11",
    (_r(0, "R"), _r(3, "b3"), _r(7, "5", "optional"),
     _r(10, "b7"), _r(14, "9", "preferred"), _r(17, "11")),
    aliases=("min11", "-11"),
))

# ── Thirteenth Chords ──

_register(ChordFormula(
    "dominant 13th", "13",
    (_r(0, "R"), _r(4, "3"), _r(7, "5", "optional"),
     _r(10, "b7"), _r(14, "9", "preferred"),
     _r(17, "11", "avoid"), _r(21, "13")),
))

_register(ChordFormula(
    "major 13th", "maj13",
    (_r(0, "R"), _r(4, "3"), _r(7, "5", "optional"),
     _r(11, "7"), _r(14, "9", "preferred"),
     _r(17, "11", "avoid"), _r(21, "13")),
    aliases=("M13",),
))

_register(ChordFormula(
    "minor 13th", "m13",
    (_r(0, "R"), _r(3, "b3"), _r(7, "5", "optional"),
     _r(10, "b7"), _r(14, "9", "preferred"), _r(21, "13")),
    aliases=("min13", "-13"),
))

# ── Altered ──

_register(ChordFormula(
    "altered dominant", "alt",
    (_r(0, "R"), _r(4, "3"), _r(10, "b7"),
     _r(13, "b9"), _r(15, "#9", "optional"),
     _r(18, "#11", "optional"), _r(20, "b13", "optional")),
    aliases=("altered",),
))

# ── Lookup helper ──

def lookup_formula(symbol: str) -> ChordFormula:
    """Look up a chord formula by symbol or alias. Raises KeyError if not found."""
    if symbol in CHORD_FORMULAS:
        return CHORD_FORMULAS[symbol]
    # Try case variations
    for key in CHORD_FORMULAS:
        if key.lower() == symbol.lower():
            return CHORD_FORMULAS[key]
    raise KeyError(f"Unknown chord type: {symbol!r}. Available: {sorted(set(f.symbol for f in CHORD_FORMULAS.values()))}")


def parse_chord_name(name: str) -> tuple[int, ChordFormula]:
    """Parse a chord name like 'Am7', 'C#maj9', 'Gb13' into (root_pc, formula).

    Returns (root_pitch_class, ChordFormula).
    """
    if not name:
        raise ValueError("Empty chord name")

    # Extract root note (1 or 2 characters)
    if len(name) >= 2 and name[1] in ('#', 'b'):
        root_str = name[:2]
        quality_str = name[2:]
    else:
        root_str = name[:1]
        quality_str = name[1:]

    root_pc = parse_note_name(root_str)
    formula = lookup_formula(quality_str)
    return root_pc, formula
