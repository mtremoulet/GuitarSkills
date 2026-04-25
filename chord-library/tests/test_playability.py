"""Tests for playability analysis."""

from chordlib.theory import parse_chord_name
from chordlib.guitar import Fretboard, STANDARD_TUNING
from chordlib.voicing import Voicing
from chordlib.playability import check_playability


def make_voicing(frets):
    root, formula = parse_chord_name("C")
    fb = Fretboard(STANDARD_TUNING, 24)
    return Voicing(frets, root, formula, fb)


class TestPlayability:
    def test_open_c_is_playable(self):
        # X-3-2-0-1-0
        v = make_voicing((None, 3, 2, 0, 1, 0))
        pr = check_playability(v)
        assert pr.is_playable
        assert pr.finger_count == 3
        assert not pr.requires_barre

    def test_f_barre_is_playable(self):
        root, formula = parse_chord_name("F")
        fb = Fretboard(STANDARD_TUNING, 24)
        v = Voicing((1, 3, 3, 2, 1, 1), root, formula, fb)
        pr = check_playability(v)
        assert pr.is_playable
        assert pr.requires_barre
        assert pr.barre_fret == 1
        assert pr.finger_count == 4  # barre + 3 fingers

    def test_all_open_is_easy(self):
        v = make_voicing((0, 0, 0, 0, 0, 0))
        pr = check_playability(v)
        assert pr.is_playable
        assert pr.difficulty == 0.0
        assert pr.finger_count == 0

    def test_five_fretted_no_barre_unplayable(self):
        # 5 different frets, no possible barre = needs 5 fingers
        v = make_voicing((1, 2, 3, 4, 5, None))
        pr = check_playability(v)
        assert not pr.is_playable

    def test_difficulty_increases_with_complexity(self):
        # Simple open chord
        v1 = make_voicing((0, 0, 2, 0, 0, 0))
        # Complex barre chord
        root, formula = parse_chord_name("F")
        fb = Fretboard(STANDARD_TUNING, 24)
        v2 = Voicing((1, 3, 3, 2, 1, 1), root, formula, fb)
        pr1 = check_playability(v1)
        pr2 = check_playability(v2)
        assert pr2.difficulty > pr1.difficulty
