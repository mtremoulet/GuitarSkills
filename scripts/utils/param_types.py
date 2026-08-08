"""
Robust parameter type conversion and normalization utilities for GuitarSkills.

Handles heterogenous inputs (floats, ints, strings with units like 'dB', '%', 'Hz',
unicode minus '−', booleans, and Markdown table strings).
"""

from __future__ import annotations

import re
from typing import Any, Optional, Union, Sequence

TRUTHY_STRINGS = {
    "ON", "TRUE", "1", "ACTIVE", "BRIGHT", "YES", "ENABLE", "ENABLED", "HIGH"
}

FALSY_STRINGS = {
    "OFF", "FALSE", "0", "NORMAL", "BYPASSED", "NO", "DISABLE", "DISABLED", "LOW"
}


def to_float(
    val: Any,
    default: float = 0.0,
    min_val: Optional[float] = None,
    max_val: Optional[float] = None,
    scale_percent: bool = False,
) -> float:
    """Safely convert any input value to float.

    Handles string cleaning ('~', '%', 'dB', unicode minus '−', etc.).
    If scale_percent is True and string contains '%', divides by 100.0.
    Returns `default` if parsing fails. Clamps to [min_val, max_val] if provided.
    """
    if val is None:
        return default

    if isinstance(val, (int, float)):
        result = float(val)
    elif isinstance(val, bool):
        result = 1.0 if val else 0.0
    else:
        val_str = str(val).strip().replace("−", "-").replace("~", "")
        is_pct = "%" in val_str
        cleaned = re.sub(r"[^\d.+\-eE]", "", val_str)
        if not cleaned:
            return default
        try:
            result = float(cleaned)
            if is_pct and scale_percent:
                result = result / 100.0
        except ValueError:
            return default

    if min_val is not None:
        result = max(min_val, result)
    if max_val is not None:
        result = min(max_val, result)

    return result


def to_bool(val: Any, default: bool = False) -> bool:
    """Safely convert any input value to boolean."""
    if val is None:
        return default
    if isinstance(val, bool):
        return val
    if isinstance(val, (int, float)):
        return bool(val)

    s = str(val).strip().upper()
    if s in TRUTHY_STRINGS:
        return True
    if s in FALSY_STRINGS:
        return False
    return default


def to_db(val: Any, default: float = 0.0) -> float:
    """Convert decibel string ('+3.5 dB', '-6dB') or float to float dB value."""
    if val is None:
        return default
    if isinstance(val, (int, float)):
        return float(val)

    val_str = str(val).strip().replace("−", "-")
    # Remove 'dB' or 'db' ignoring case
    val_str = re.sub(r"(?i)\s*db", "", val_str)
    return to_float(val_str, default=default)


def to_freq(val: Any, default: float = 1000.0) -> float:
    """Convert frequency string ('1.5 kHz', '800 Hz') or float to Hertz."""
    if val is None:
        return default
    if isinstance(val, (int, float)):
        return float(val)

    val_str = str(val).strip().replace("−", "-")
    m_khz = re.search(r"([\d.+−-]+)\s*k(?:hz)?", val_str, re.IGNORECASE)
    if m_khz:
        return to_float(m_khz.group(1), default=default / 1000.0) * 1000.0

    m_hz = re.search(r"([\d.+−-]+)\s*hz", val_str, re.IGNORECASE)
    if m_hz:
        return to_float(m_hz.group(1), default=default)

    return to_float(val_str, default=default)


def find_numeric_param(content: str, param_names: Sequence[str]) -> Optional[float]:
    """Search Markdown content for a parameter matching any of `param_names` in table rows.

    Matches tables of form `| ParamName | 5.5% |`, `| ParamName | **-3.0 dB** |`, etc.
    Returns float value, auto-scaled if '%' is present in the matched cell.
    """
    clean_content = content.replace("**", "")
    for name in param_names:
        pattern = r"\|\s*" + re.escape(name) + r"\s*\|\s*(?:\*\*)?([~0-9.+−\-a-zA-Z%\s]+)(?:\*\*)?\s*\|"
        match = re.search(pattern, clean_content, re.IGNORECASE)
        if match:
            cell_str = match.group(1).strip()
            return to_float(cell_str, default=0.0, scale_percent=True)
    return None


def find_boolean_param(content: str, param_names: Sequence[str]) -> Optional[bool]:
    """Search Markdown content for a boolean parameter matching `param_names` in table rows.

    Matches tables of form `| Power | ON |` or `| Bypass | Off |`.
    """
    clean_content = content.replace("**", "")
    for name in param_names:
        pattern = r"\|\s*" + re.escape(name) + r"\s*\|\s*(?:\*\*)?([A-Za-z0-9/ ]+)(?:\*\*)?\s*\|"
        match = re.search(pattern, clean_content, re.IGNORECASE)
        if match:
            cell_str = match.group(1).strip()
            return to_bool(cell_str)
    return None
