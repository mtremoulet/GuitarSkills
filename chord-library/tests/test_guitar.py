"""Tests for guitar fretboard model."""

from chordlib.theory import Note
from chordlib.guitar import Fretboard, STANDARD_TUNING


class TestFretboard:
    def setup_method(self):
        self.fb = Fretboard(STANDARD_TUNING, 24)

    def test_open_strings(self):
        # E2, A2, D3, G3, B3, E4
        assert self.fb.pitch_class_at(0, 0) == 4   # E
        assert self.fb.pitch_class_at(1, 0) == 9   # A
        assert self.fb.pitch_class_at(2, 0) == 2   # D
        assert self.fb.pitch_class_at(3, 0) == 7   # G
        assert self.fb.pitch_class_at(4, 0) == 11  # B
        assert self.fb.pitch_class_at(5, 0) == 4   # E

    def test_12th_fret_is_octave(self):
        for s in range(6):
            assert self.fb.pitch_class_at(s, 12) == self.fb.pitch_class_at(s, 0)

    def test_frets_for_pitch_class(self):
        # C (pc=0) on the A string (string 1) should be at fret 3, 15
        c_frets = self.fb.frets_for_pitch_class(1, 0)
        assert 3 in c_frets
        assert 15 in c_frets

    def test_note_at(self):
        # A2 is string 1, fret 0
        n = self.fb.note_at(1, 0)
        assert n.pitch_class == 9
        assert n.octave == 2

    def test_fifth_fret_rule(self):
        # 5th fret on low E = A
        assert self.fb.pitch_class_at(0, 5) == 9  # A
        # 5th fret on A = D
        assert self.fb.pitch_class_at(1, 5) == 2  # D
        # 5th fret on D = G
        assert self.fb.pitch_class_at(2, 5) == 7  # G
        # 5th fret on G = B (wait, it's 4th fret on G to B)
        assert self.fb.pitch_class_at(3, 4) == 11  # B on G string at fret 4


class TestStandardTuning:
    def test_string_names(self):
        assert STANDARD_TUNING.string_names == ("E", "A", "D", "G", "B", "e")

    def test_num_strings(self):
        assert STANDARD_TUNING.num_strings == 6
