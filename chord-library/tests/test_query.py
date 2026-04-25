"""Tests for the query engine."""

from chordlib.theory import parse_note_name, lookup_formula
from chordlib.guitar import Fretboard, STANDARD_TUNING
from chordlib.query import VoicingQuery, execute_query
from chordlib.classifier import VoicingType
from chordlib.ascii_renderer import render_voicing_compact


def fb():
    return Fretboard(STANDARD_TUNING, 24)


class TestQueryEngine:
    def test_basic_query(self):
        q = VoicingQuery(root=0, formula=lookup_formula(""), limit=10)
        result = execute_query(q, fb())
        assert result.total_matches > 0
        assert len(result.voicings) <= 10

    def test_c7_root_on_a_string(self):
        """C7 with root on 5th string (A string, internal index 1)."""
        q = VoicingQuery(
            root=0,
            formula=lookup_formula("7"),
            root_string=1,  # A string
            limit=20,
        )
        result = execute_query(q, fb())
        assert result.total_matches > 0
        # All results should have the root (C) on the A string
        for v in result.voicings:
            assert v.root_on_string(1), f"Root not on A string: {render_voicing_compact(v)}"

    def test_am9_above_8th_fret(self):
        """Am9 starting above the 8th fret."""
        q = VoicingQuery(
            root=parse_note_name("A"),
            formula=lookup_formula("m9"),
            min_fret=8,
            limit=20,
        )
        result = execute_query(q, fb())
        assert result.total_matches > 0
        for v in result.voicings:
            for f in v.frets:
                if f is not None:
                    assert f >= 8, f"Fret {f} below 8 in {render_voicing_compact(v)}"

    def test_gm7b5_bb_on_top(self):
        """Gm7b5 with Bb on top note."""
        q = VoicingQuery(
            root=parse_note_name("G"),
            formula=lookup_formula("m7b5"),
            top_note=parse_note_name("Bb"),
            limit=20,
        )
        result = execute_query(q, fb())
        assert result.total_matches > 0
        for v in result.voicings:
            assert v.top_note.pitch_class == 10, \
                f"Top note is PC {v.top_note.pitch_class}, expected 10 (Bb): {render_voicing_compact(v)}"

    def test_pagination(self):
        q = VoicingQuery(root=0, formula=lookup_formula(""), limit=5, offset=0)
        r1 = execute_query(q, fb())
        q2 = VoicingQuery(root=0, formula=lookup_formula(""), limit=5, offset=5)
        r2 = execute_query(q2, fb())
        # Results should be different
        if r1.total_matches > 5:
            frets1 = {v.frets for v in r1.voicings}
            frets2 = {v.frets for v in r2.voicings}
            assert frets1 != frets2

    def test_voicing_type_filter(self):
        q = VoicingQuery(
            root=0,
            formula=lookup_formula("7"),
            voicing_types={VoicingType.SHELL},
            limit=20,
        )
        result = execute_query(q, fb())
        # Should find shell voicings for C7
        assert result.total_matches > 0

    def test_max_difficulty_filter(self):
        q = VoicingQuery(
            root=0,
            formula=lookup_formula(""),
            max_difficulty=0.3,
            limit=100,
        )
        result = execute_query(q, fb())
        # Easy voicings should exist
        assert result.total_matches > 0
