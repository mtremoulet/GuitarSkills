import pytest
from scripts.utils.param_types import (
    to_float,
    to_bool,
    to_db,
    to_freq,
    find_numeric_param,
    find_boolean_param,
)

def test_to_float():
    assert to_float("5.5") == 5.5
    assert to_float("5.5%") == 5.5
    assert to_float("5.5%", scale_percent=True) == 0.055
    assert to_float("−12.5") == -12.5
    assert to_float("~3.0 dB") == 3.0
    assert to_float(None, default=1.0) == 1.0
    assert to_float("invalid", default=2.5) == 2.5
    assert to_float(10, min_val=0, max_val=5) == 5.0

def test_to_bool():
    assert to_bool("ON") is True
    assert to_bool("bright") is True
    assert to_bool("OFF") is False
    assert to_bool("bypassed") is False
    assert to_bool(True) is True
    assert to_bool(0) is False
    assert to_bool(None, default=False) is False

def test_to_db():
    assert to_db("+3.5 dB") == 3.5
    assert to_db("-6dB") == -6.0
    assert to_db("−12.0") == -12.0

def test_to_freq():
    assert to_freq("1.5 kHz") == 1500.0
    assert to_freq("800 Hz") == 800.0
    assert to_freq(250.0) == 250.0

def test_find_numeric_param():
    md = "| Volume | **50%** |\n| Bass | -3.5 dB |"
    assert find_numeric_param(md, ["Volume"]) == 0.5
    assert find_numeric_param(md, ["Bass"]) == -3.5
    assert find_numeric_param(md, ["Treble"]) is None

def test_find_boolean_param():
    md = "| Compressor | ON |\n| Gate | OFF |"
    assert find_boolean_param(md, ["Compressor"]) is True
    assert find_boolean_param(md, ["Gate"]) is False
    assert find_boolean_param(md, ["Drive"]) is None
