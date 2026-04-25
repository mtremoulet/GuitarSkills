"""Tests for the voicing generation engine."""

import pytest
from chordlib.theory import parse_chord_name, lookup_formula
from chordlib.guitar import Fretboard, STANDARD_TUNING
from chordlib.generator import generate_voicings
from chordlib.playability import check_playability
from chordlib.ascii_renderer import render_voicing_compact


@pytest.fixture
def fretboard():
    return Fretboard(STANDARD_TUNING, 15)


class TestKnownChordShapes:
    """Verify that well-known chord shapes appear in generated results."""

    def _has_shape(self, voicings, target_frets):
        """Check if a specific fret pattern exists in the results."""
        for v in voicings:
            if v.frets == target_frets:
                return True
        return False

    def test_open_c_major(self, fretboard):
        root, formula = parse_chord_name("C")
        voicings = generate_voicings(root, formula, fretboard, max_fret=4)
        # X-3-2-0-1-0 (classic open C)
        assert self._has_shape(voicings, (None, 3, 2, 0, 1, 0))

    def test_open_a_minor(self, fretboard):
        root, formula = parse_chord_name("Am")
        voicings = generate_voicings(root, formula, fretboard, max_fret=4)
        # X-0-2-2-1-0 (classic open Am)
        assert self._has_shape(voicings, (None, 0, 2, 2, 1, 0))

    def test_open_g_major(self, fretboard):
        root, formula = parse_chord_name("G")
        voicings = generate_voicings(root, formula, fretboard, max_fret=4)
        # 3-2-0-0-0-3 (classic open G)
        assert self._has_shape(voicings, (3, 2, 0, 0, 0, 3))

    def test_open_e_major(self, fretboard):
        root, formula = parse_chord_name("E")
        voicings = generate_voicings(root, formula, fretboard, max_fret=4)
        # 0-2-2-1-0-0 (classic open E)
        assert self._has_shape(voicings, (0, 2, 2, 1, 0, 0))

    def test_open_d_major(self, fretboard):
        root, formula = parse_chord_name("D")
        voicings = generate_voicings(root, formula, fretboard, max_fret=4)
        # X-X-0-2-3-2 (classic open D)
        assert self._has_shape(voicings, (None, None, 0, 2, 3, 2))

    def test_e_shape_barre_f(self, fretboard):
        root, formula = parse_chord_name("F")
        voicings = generate_voicings(root, formula, fretboard, max_fret=5)
        # 1-3-3-2-1-1 (F barre chord, E shape)
        assert self._has_shape(voicings, (1, 3, 3, 2, 1, 1))

    def test_a_shape_barre_b(self, fretboard):
        root, formula = parse_chord_name("B")
        voicings = generate_voicings(root, formula, fretboard, max_fret=6)
        # X-2-4-4-4-2 (B barre chord, A shape)
        assert self._has_shape(voicings, (None, 2, 4, 4, 4, 2))

    def test_power_chord_e5(self, fretboard):
        root, formula = parse_chord_name("E5")
        voicings = generate_voicings(root, formula, fretboard, max_fret=4)
        # 0-2-2-X-X-X
        assert self._has_shape(voicings, (0, 2, 2, None, None, None))


class TestGeneratorConstraints:
    def test_max_span_respected(self, fretboard):
        root, formula = parse_chord_name("C")
        voicings = generate_voicings(root, formula, fretboard, max_span=3)
        for v in voicings:
            assert v.fret_span <= 3

    def test_min_notes_respected(self, fretboard):
        root, formula = parse_chord_name("C")
        voicings = generate_voicings(root, formula, fretboard, min_notes=4)
        for v in voicings:
            assert v.num_sounding >= 4

    def test_no_inner_mutes(self, fretboard):
        root, formula = parse_chord_name("C")
        voicings = generate_voicings(root, formula, fretboard, allow_inner_mutes=False)
        for v in voicings:
            assert not v.has_inner_mutes

    def test_all_required_pcs_present(self, fretboard):
        root, formula = parse_chord_name("Am7")
        voicings = generate_voicings(root, formula, fretboard)
        required = formula.required_pitch_classes
        for v in voicings:
            actual_pcs = set()
            for n in v.sounding_notes:
                actual_pcs.add((n.pitch_class - root) % 12)
            # All required PCs (relative to root) must be present
            required_relative = set(pc % 12 for pc in required)
            actual_relative = set((pc - root) % 12 for pc in v.pitch_class_set)
            assert required_relative.issubset(actual_relative), \
                f"Missing required PCs in {render_voicing_compact(v)}"


class TestGeneratorPerformance:
    def test_reasonable_count(self, fretboard):
        """Generation should produce a reasonable number of voicings."""
        root, formula = parse_chord_name("C")
        voicings = generate_voicings(root, formula, fretboard, max_fret=12)
        assert len(voicings) > 50
        assert len(voicings) < 5000

    def test_extended_chord_generates(self, fretboard):
        """Extended chords should still generate voicings."""
        root, formula = parse_chord_name("C13")
        voicings = generate_voicings(root, formula, fretboard, max_fret=12)
        assert len(voicings) > 0
