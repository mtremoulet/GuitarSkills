"""Tests for music theory module."""

import pytest
from chordlib.theory import (
    PitchClass, parse_note_name, note_name, spell_note_for_degree,
    ChordFormula, FormulaInterval, IntervalRole,
    parse_chord_name, lookup_formula, CHORD_FORMULAS,
)


class TestParseNoteName:
    def test_naturals(self):
        assert parse_note_name("C") == 0
        assert parse_note_name("D") == 2
        assert parse_note_name("E") == 4
        assert parse_note_name("F") == 5
        assert parse_note_name("G") == 7
        assert parse_note_name("A") == 9
        assert parse_note_name("B") == 11

    def test_sharps(self):
        assert parse_note_name("C#") == 1
        assert parse_note_name("F#") == 6

    def test_flats(self):
        assert parse_note_name("Bb") == 10
        assert parse_note_name("Eb") == 3
        assert parse_note_name("Db") == 1
        assert parse_note_name("Ab") == 8

    def test_invalid(self):
        with pytest.raises(ValueError):
            parse_note_name("X")


class TestNoteSpelling:
    def test_c7_b7_is_bb(self):
        # b7 of C (semitone 10) should be Bb, not A#
        assert spell_note_for_degree(0, 10, "b7") == "Bb"

    def test_c_major_third(self):
        # 3 of C (semitone 4) should be E
        assert spell_note_for_degree(0, 4, "3") == "E"

    def test_c_root(self):
        assert spell_note_for_degree(0, 0, "R") == "C"

    def test_g_sharp_five(self):
        # #5 of C (semitone 8) should be G#, not Ab
        assert spell_note_for_degree(0, 8, "#5") == "G#"

    def test_gm7b5_b5_is_db(self):
        # b5 of G (semitone 6) should be Db
        assert spell_note_for_degree(7, 6, "b5") == "Db"

    def test_gm7b5_b3_is_bb(self):
        # b3 of G (semitone 3) should be Bb
        assert spell_note_for_degree(7, 3, "b3") == "Bb"


class TestChordFormulas:
    def test_major_exists(self):
        f = lookup_formula("")
        assert f.name == "major"
        assert len(f.intervals) == 3

    def test_major_by_alias(self):
        assert lookup_formula("maj") == lookup_formula("")

    def test_minor_seventh(self):
        f = lookup_formula("m7")
        pcs = f.pitch_classes
        assert 0 in pcs  # root
        assert 3 in pcs  # b3
        assert 7 in pcs  # 5
        assert 10 in pcs  # b7

    def test_dominant_seventh(self):
        f = lookup_formula("7")
        assert f.name == "dominant 7th"
        pcs = f.pitch_classes
        assert 4 in pcs  # 3
        assert 10 in pcs  # b7

    def test_half_diminished(self):
        f = lookup_formula("m7b5")
        pcs = f.pitch_classes
        assert 3 in pcs  # b3
        assert 6 in pcs  # b5
        assert 10 in pcs  # b7

    def test_13th_has_avoid_11(self):
        f = lookup_formula("13")
        roles = {iv.display_name: iv.role for iv in f.intervals}
        assert roles["11"] == IntervalRole.AVOID
        assert roles["9"] == IntervalRole.PREFERRED

    def test_unknown_raises(self):
        with pytest.raises(KeyError):
            lookup_formula("xyz123")

    def test_registry_has_many_types(self):
        # Should have at least 35 unique formulas
        unique = set(id(f) for f in CHORD_FORMULAS.values())
        assert len(unique) >= 35


class TestParseChordName:
    def test_cmaj(self):
        root, formula = parse_chord_name("C")
        assert root == 0
        assert formula.name == "major"

    def test_am7(self):
        root, formula = parse_chord_name("Am7")
        assert root == 9
        assert formula.symbol == "m7"

    def test_fsharp_dim7(self):
        root, formula = parse_chord_name("F#dim7")
        assert root == 6
        assert formula.symbol == "dim7"

    def test_bb13(self):
        root, formula = parse_chord_name("Bb13")
        assert root == 10
        assert formula.symbol == "13"

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            parse_chord_name("")
