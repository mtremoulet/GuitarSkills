"""Tests for ASCII chord diagram rendering."""

from chordlib.theory import parse_chord_name
from chordlib.guitar import Fretboard, STANDARD_TUNING
from chordlib.voicing import Voicing
from chordlib.ascii_renderer import render_voicing, render_voicing_compact


def make_voicing(chord_name, frets):
    root, formula = parse_chord_name(chord_name)
    fb = Fretboard(STANDARD_TUNING, 24)
    return Voicing(frets, root, formula, fb)


class TestAsciiRenderer:
    def test_compact_format(self):
        v = make_voicing("C", (None, 3, 2, 0, 1, 0))
        assert render_voicing_compact(v) == "X-3-2-0-1-0"

    def test_horizontal_has_four_rows(self):
        v = make_voicing("C", (None, 3, 2, 0, 1, 0))
        lines = render_voicing(v).split("\n")
        assert len(lines) == 4

    def test_string_names_row(self):
        v = make_voicing("C", (None, 3, 2, 0, 1, 0))
        lines = render_voicing(v).split("\n")
        # First row should have string names
        assert "E" in lines[0]
        assert "A" in lines[0]
        assert "D" in lines[0]
        assert "G" in lines[0]
        assert "B" in lines[0]

    def test_muted_shows_x(self):
        v = make_voicing("C", (None, 3, 2, 0, 1, 0))
        lines = render_voicing(v).split("\n")
        fret_row = lines[1]
        assert fret_row.startswith("X")

    def test_muted_shows_dash_for_notes(self):
        v = make_voicing("C", (None, 3, 2, 0, 1, 0))
        lines = render_voicing(v).split("\n")
        note_row = lines[2]
        assert note_row.startswith("-")
        degree_row = lines[3]
        assert degree_row.startswith("-")

    def test_correct_notes_for_open_c(self):
        v = make_voicing("C", (None, 3, 2, 0, 1, 0))
        # Notes should be: - C E G C E
        note_names = [n for n in v.note_names if n is not None]
        assert note_names == ["C", "E", "G", "C", "E"]

    def test_correct_degrees_for_open_c(self):
        v = make_voicing("C", (None, 3, 2, 0, 1, 0))
        degrees = [d for d in v.interval_names if d is not None]
        assert degrees == ["R", "3", "5", "R", "3"]
