import unittest
from scripts.utils.param_types import (
    to_float,
    to_bool,
    to_db,
    to_freq,
    find_numeric_param,
    find_boolean_param,
)

class TestParamTypes(unittest.TestCase):
    def test_to_float(self):
        self.assertEqual(to_float("5.5"), 5.5)
        self.assertEqual(to_float("5.5%"), 5.5)
        self.assertEqual(to_float("5.5%", scale_percent=True), 0.055)
        self.assertEqual(to_float("−12.5"), -12.5)
        self.assertEqual(to_float("~3.0 dB"), 3.0)
        self.assertEqual(to_float(None, default=1.0), 1.0)
        self.assertEqual(to_float("invalid", default=2.5), 2.5)
        self.assertEqual(to_float(10, min_val=0, max_val=5), 5.0)

    def test_to_bool(self):
        self.assertIs(to_bool("ON"), True)
        self.assertIs(to_bool("bright"), True)
        self.assertIs(to_bool("OFF"), False)
        self.assertIs(to_bool("bypassed"), False)
        self.assertIs(to_bool(True), True)
        self.assertIs(to_bool(0), False)
        self.assertIs(to_bool(None, default=False), False)

    def test_to_db(self):
        self.assertEqual(to_db("+3.5 dB"), 3.5)
        self.assertEqual(to_db("-6dB"), -6.0)
        self.assertEqual(to_db("−12.0"), -12.0)

    def test_to_freq(self):
        self.assertEqual(to_freq("1.5 kHz"), 1500.0)
        self.assertEqual(to_freq("800 Hz"), 800.0)
        self.assertEqual(to_freq(250.0), 250.0)

    def test_find_numeric_param(self):
        md = "| Volume | **50%** |\n| Bass | -3.5 dB |"
        self.assertEqual(find_numeric_param(md, ["Volume"]), 0.5)
        self.assertEqual(find_numeric_param(md, ["Bass"]), -3.5)
        self.assertIsNone(find_numeric_param(md, ["Treble"]))

    def test_find_boolean_param(self):
        md = "| Compressor | ON |\n| Gate | OFF |"
        self.assertIs(find_boolean_param(md, ["Compressor"]), True)
        self.assertIs(find_boolean_param(md, ["Gate"]), False)
        self.assertIsNone(find_boolean_param(md, ["Drive"]))

if __name__ == "__main__":
    unittest.main()

