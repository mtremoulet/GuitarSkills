"""Apple Logic Pro Native PST preset compiler module (Channel EQ, Compressor, Space Designer)."""

from __future__ import annotations

import os
import re
import struct
import plistlib
from typing import Dict, Any, Optional, List, Tuple

try:
    from Foundation import NSURL, NSURLBookmarkCreationSuitableForBookmarkFile
    FOUNDATION_AVAILABLE = True
except ImportError:
    FOUNDATION_AVAILABLE = False

from scripts.utils.param_types import to_float, to_bool, to_freq, to_db, find_numeric_param
from .base import find_numeric_parameter


def extract_comp_param(content: str, keywords: List[str]) -> Optional[float]:
    val = find_numeric_parameter(content, keywords)
    if val is not None:
        return val

    for line in content.split("\n"):
        line_lower = line.lower()
        if any(kw.lower() in line_lower for kw in keywords):
            parts = [p.strip() for p in line.split("|")]
            text_to_search = parts[2] if len(parts) >= 3 else line
            match = re.search(r"([+-]?\d+(?:\.\d+)?)\s*(?:db|ms|:1)?\b", text_to_search.replace("−", "-"), re.IGNORECASE)
            if match:
                return float(match.group(1))
    return None


def extract_freq(text: str) -> Optional[float]:
    freq_match = re.search(r"(\d+(?:\.\d+)?)\s*(k?Hz)\b", text, re.IGNORECASE)
    if freq_match:
        val = float(freq_match.group(1))
        unit = freq_match.group(2).lower()
        if unit == "khz" or (val < 22.0 and unit == "hz"):
            val *= 1000.0
        return val
    return None


def extract_slope(text: str) -> Optional[float]:
    slope_match = re.search(r"(\d+)\s*db", text, re.IGNORECASE)
    if slope_match:
        db_val = int(slope_match.group(1))
        mapping = {6: 1.0, 12: 2.0, 18: 3.0, 24: 4.0, 30: 5.0, 36: 6.0, 48: 7.0}
        if db_val in mapping:
            return mapping[db_val]
        return float(db_val // 6)
    return None


def parse_eq_bands(content: str) -> Dict[int, Dict[str, Optional[float]]]:
    bands = {i: {"on": None, "freq": None, "gain_or_slope": None, "q": None} for i in range(1, 9)}
    in_eq_section = False

    for line in content.split("\n"):
        line_lower = line.lower()

        if line.strip().startswith("#"):
            if "channel eq" in line_lower or "surgical shaping" in line_lower:
                in_eq_section = True
                continue
            else:
                in_eq_section = False
                continue

        if not in_eq_section:
            continue

        if "|" not in line:
            if "high-pass" in line_lower or "hpf" in line_lower or "low cut" in line_lower:
                freq = extract_freq(line)
                slope = extract_slope(line)
                if freq is not None:
                    bands[1]["on"] = 1.0
                    bands[1]["freq"] = freq
                if slope is not None:
                    bands[1]["gain_or_slope"] = slope
            elif "low-pass" in line_lower or "lpf" in line_lower or "high cut" in line_lower or "high-cut" in line_lower:
                freq = extract_freq(line)
                slope = extract_slope(line)
                if freq is not None:
                    bands[8]["on"] = 1.0
                    bands[8]["freq"] = freq
                if slope is not None:
                    bands[8]["gain_or_slope"] = slope
            continue

        parts = [p.strip() for p in line.split("|")]
        if len(parts) < 3:
            continue

        first_col = parts[1].lower()
        band_num = None
        if "band 1" in first_col or "low cut" in first_col or "hpf" in first_col or "high-pass" in first_col:
            band_num = 1
        elif "band 2" in first_col or "low shelf" in first_col:
            band_num = 2
        elif "band 3" in first_col or "peak 1" in first_col:
            band_num = 3
        elif "band 4" in first_col or "peak 2" in first_col or ("peak" in first_col and "250 hz" in line_lower):
            band_num = 4
        elif "band 5" in first_col or "peak 3" in first_col:
            band_num = 5
        elif "band 6" in first_col or "peak 4" in first_col:
            band_num = 6
        elif "band 7" in first_col or "high shelf" in first_col:
            band_num = 7
        elif "band 8" in first_col or "high cut" in first_col or "lpf" in first_col or "low-pass" in first_col or "high-cut" in first_col:
            band_num = 8
        elif "peak" in first_col:
            band_num = 3

        if band_num is None:
            continue

        col_text = " ".join(parts[2:])
        freq = extract_freq(col_text)
        gain_or_slope = None
        q = None

        if band_num in [1, 8]:
            gain_or_slope = extract_slope(col_text)
        else:
            gain_match = re.search(r"([+-]?\d+(?:\.\d+)?)\s*db\b", col_text.replace("−", "-"), re.IGNORECASE)
            if gain_match:
                gain_or_slope = float(gain_match.group(1))

        q_match = re.search(r"\bq(?:-factor)?(?:\s*:\s*|\s+)(\d+(?:\.\d+)?)\b", col_text, re.IGNORECASE)
        if q_match:
            q = float(q_match.group(1))

        bands[band_num]["on"] = 1.0
        if freq is not None: bands[band_num]["freq"] = freq
        if gain_or_slope is not None: bands[band_num]["gain_or_slope"] = gain_or_slope
        if q is not None: bands[band_num]["q"] = q

    return bands


def compile_logic_eq_toneprint(
    filepath: str,
    base_preset_path: str,
    output_name: str,
    frontmatter: Dict[str, Any],
) -> bool:
    """Compile Logic Pro Channel EQ PST binary preset."""
    preset_data = frontmatter.get("preset_data", {})
    eq_data = preset_data.get("logic_eq") if isinstance(preset_data, dict) else None

    if eq_data and isinstance(eq_data, dict):
        bands = {i: {"on": None, "freq": None, "gain_or_slope": None, "q": None} for i in range(1, 9)}
        for band_str, params in eq_data.items():
            if not band_str.startswith("band") or not band_str[4:].isdigit():
                continue
            band_num = int(band_str[4:])
            if band_num < 1 or band_num > 8:
                continue

            if "on" in params:
                bands[band_num]["on"] = 1.0 if params["on"] else 0.0
            if "freq" in params:
                bands[band_num]["freq"] = to_freq(params["freq"])
            if band_num in [1, 8]:
                if "slope" in params:
                    bands[band_num]["gain_or_slope"] = to_float(params["slope"])
            else:
                if "gain" in params:
                    bands[band_num]["gain_or_slope"] = to_float(params["gain"])
                if "q" in params:
                    bands[band_num]["q"] = to_float(params["q"])
    else:
        with open(filepath, "r") as f:
            content = f.read()
        bands = parse_eq_bands(content)

    any_configured = any(p["on"] is not None for p in bands.values())
    if not any_configured:
        return False

    with open(base_preset_path, "rb") as f:
        preset_bytes = bytearray(f.read())

    for band_num, params in bands.items():
        if params["on"] is None and params["freq"] is None:
            continue

        if band_num == 1:
            if params["on"] is not None: struct.pack_into("f", preset_bytes, 8 + 5 * 4, params["on"])
            if params["freq"] is not None: struct.pack_into("f", preset_bytes, 8 + 6 * 4, params["freq"])
            if params["gain_or_slope"] is not None: struct.pack_into("f", preset_bytes, 8 + 7 * 4, params["gain_or_slope"])
        elif band_num == 8:
            if params["on"] is not None: struct.pack_into("f", preset_bytes, 8 + 33 * 4, params["on"])
            if params["freq"] is not None: struct.pack_into("f", preset_bytes, 8 + 34 * 4, params["freq"])
            if params["gain_or_slope"] is not None: struct.pack_into("f", preset_bytes, 8 + 35 * 4, params["gain_or_slope"])
        else:
            base_idx = 9 + (band_num - 2) * 4
            if params["on"] is not None: struct.pack_into("f", preset_bytes, 8 + base_idx * 4, params["on"])
            if params["freq"] is not None: struct.pack_into("f", preset_bytes, 8 + (base_idx + 1) * 4, params["freq"])
            if params["gain_or_slope"] is not None: struct.pack_into("f", preset_bytes, 8 + (base_idx + 2) * 4, params["gain_or_slope"])
            if params["q"] is not None: struct.pack_into("f", preset_bytes, 8 + (base_idx + 3) * 4, params["q"])

    output_dir = os.path.dirname(base_preset_path)
    out_path = os.path.join(output_dir, f"Toneprint - {output_name}.pst")
    with open(out_path, "wb") as f:
        f.write(preset_bytes)

    print(f"-> Compiled Logic Channel EQ Preset: 'Toneprint - {output_name}'")
    return True


def compile_logic_compressor_toneprint(
    filepath: str,
    base_preset_path: str,
    output_name: str,
    frontmatter: Dict[str, Any],
) -> bool:
    """Compile Logic Pro Compressor PST binary preset."""
    preset_data = frontmatter.get("preset_data", {})
    comp_data = preset_data.get("logic_compressor") if isinstance(preset_data, dict) else None

    if comp_data and isinstance(comp_data, dict):
        threshold = to_float(comp_data.get("threshold"))
        ratio = to_float(comp_data.get("ratio"))
        attack = to_float(comp_data.get("attack"))
        release = to_float(comp_data.get("release"))
        gain = to_float(comp_data.get("makeup_gain"))
        knee = to_float(comp_data.get("knee"))
    else:
        with open(filepath, "r") as f:
            content = f.read()
        threshold = extract_comp_param(content, ["Threshold"])
        ratio = extract_comp_param(content, ["Ratio"])
        attack = extract_comp_param(content, ["Attack"])
        release = extract_comp_param(content, ["Release"])
        gain = extract_comp_param(content, ["Gain", "Makeup Gain"])
        knee = extract_comp_param(content, ["Knee"])

    if threshold is None and ratio is None and attack is None and release is None:
        return False

    with open(base_preset_path, "rb") as f:
        preset_bytes = bytearray(f.read())

    if threshold is not None: struct.pack_into("f", preset_bytes, 8 + 5 * 4, threshold)
    if ratio is not None: struct.pack_into("f", preset_bytes, 8 + 6 * 4, ratio)
    if attack is not None: struct.pack_into("f", preset_bytes, 8 + 7 * 4, attack)
    if release is not None: struct.pack_into("f", preset_bytes, 8 + 8 * 4, release)
    if gain is not None: struct.pack_into("f", preset_bytes, 8 + 9 * 4, gain)
    if knee is not None: struct.pack_into("f", preset_bytes, 8 + 10 * 4, knee)

    output_dir = os.path.dirname(base_preset_path)
    out_path = os.path.join(output_dir, f"Toneprint - {output_name}.pst")
    with open(out_path, "wb") as f:
        f.write(preset_bytes)

    print(f"-> Compiled Logic Compressor Preset: 'Toneprint - {output_name}'")
    return True


def parse_db_value(val_str: Optional[str]) -> Optional[float]:
    if not val_str:
        return None
    val_str_clean = val_str.lower().replace("−", "-")
    if "inf" in val_str_clean or "off" in val_str_clean or "∞" in val_str_clean:
        return -80.0
    match = re.search(r"([+-]?\d+(?:\.\d+)?)", val_str_clean)
    if match:
        return float(match.group(1))
    return None


def parse_space_designer_params(content: str) -> Dict[str, Optional[str]]:
    params: Dict[str, Optional[str]] = {
        "ir": None, "predelay": None, "size": None, "dry": None, "wet": None
    }
    in_section = False
    for line in content.split("\n"):
        line_lower = line.lower()
        if "###" in line_lower and ("space designer" in line_lower or "reverb aux" in line_lower):
            in_section = True
            continue
        elif in_section and "###" in line:
            in_section = False

        if in_section and "|" in line:
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 3:
                key = parts[1].lower()
                val_str = parts[2]
                if "ir" in key: params["ir"] = val_str
                elif "predelay" in key or "pre-delay" in key: params["predelay"] = val_str
                elif "size" in key: params["size"] = val_str
                elif "dry" in key: params["dry"] = val_str
                elif "wet" in key: params["wet"] = val_str
    return params


def get_sdir_list() -> List[Tuple[str, str]]:
    base_dir = "/Users/miketremoulet/Music/Logic Pro Library.bundle/Impulse Responses"
    if not os.path.exists(base_dir):
        return []
    sdir_files = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.lower().endswith(".sdir"):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, base_dir)
                sdir_files.append((rel_path, full_path))
    return sdir_files


def find_matching_sdir(text: Optional[str], sdir_list: List[Tuple[str, str]]) -> Optional[Tuple[str, str]]:
    if not text:
        return None
    text_lower = text.lower()
    best_match = None
    best_score = 0
    for rel_path, full_path in sdir_list:
        filename = os.path.basename(full_path).lower().replace(".sdir", "")
        clean_filename = re.sub(r'^[0-9.]+\s*[a-z_-]*', '', filename).strip()
        filename_words = set(re.findall(r'[a-z0-9]+', clean_filename))
        text_words = set(re.findall(r'[a-z0-9]+', text_lower))
        overlap = filename_words.intersection(text_words)
        if len(overlap) > best_score:
            best_score = len(overlap)
            best_match = (rel_path, full_path)
    return best_match


def compile_logic_space_designer_toneprint(
    filepath: str,
    base_preset_path: str,
    output_name: str,
    frontmatter: Dict[str, Any],
) -> bool:
    """Compile Logic Pro Space Designer PST binary preset."""
    if not FOUNDATION_AVAILABLE:
        print("-> Warning: Foundation framework not available. Skipping Space Designer preset compilation.")
        return False

    with open(filepath, "r") as f:
        content = f.read()

    params = parse_space_designer_params(content)
    if not params["ir"]:
        return False

    sdirs = get_sdir_list()
    matched = find_matching_sdir(params["ir"], sdirs)
    if not matched:
        print(f"-> Warning: Could not find matching SDIR file for description '{params['ir']}'")
        return False

    rel_path, full_path = matched
    short_name = os.path.basename(full_path)

    if not os.path.exists(base_preset_path):
        print(f"-> Warning: Space Designer base template not found at {base_preset_path}")
        return False

    with open(base_preset_path, "rb") as f:
        template = bytearray(f.read())

    template[30] = len(short_name)
    for i in range(31, 100):
        template[i] = 0
    template[31:31 + len(short_name)] = short_name.encode('utf-8')

    byte26_val = 5
    if "Indoor Spaces" in full_path: byte26_val = 7
    elif "Plate Reverbs" in full_path: byte26_val = 3
    elif "Halls" in full_path: byte26_val = 2
    template[26] = byte26_val

    if params["dry"]:
        dry_val = parse_db_value(params["dry"])
        if dry_val is not None: struct.pack_into("f", template, 104, dry_val)

    if params["wet"]:
        wet_val = parse_db_value(params["wet"])
        if wet_val is not None: struct.pack_into("f", template, 108, wet_val)

    if params["predelay"]:
        pre_match = re.search(r"(\d+(?:\.\d+)?)", params["predelay"])
        if pre_match: struct.pack_into("f", template, 112, float(pre_match.group(1)))

    try:
        url = NSURL.fileURLWithPath_(full_path)
        opt = NSURLBookmarkCreationSuitableForBookmarkFile
        bookmark_data, error = url.bookmarkDataWithOptions_includingResourceValuesForKeys_relativeToURL_error_(opt, None, None, None)
        if not bookmark_data:
            return False
        bookmark_bytes = bytes(bookmark_data)
    except Exception as e:
        print(f"-> Error generating bookmark: {e}")
        return False

    plist_dict = {'CFileRef_Bookmark': bookmark_bytes}
    plist_payload = plistlib.dumps(plist_dict, fmt=plistlib.FMT_BINARY)
    plist_len = len(plist_payload)

    template[1572:1576] = struct.pack('<I', plist_len)
    for i in range(1576, 3024):
        template[i] = 0
    template[1576:1576 + len(full_path)] = full_path.encode('utf-8')

    out_data = bytearray(template[:3024])
    out_data.extend(plist_payload)

    padding_len = 1165 - plist_len
    if padding_len > 0:
        out_data.extend(b'\x00' * padding_len)

    footer = template[4189:]
    out_data.extend(footer)

    if params["size"]:
        size_match = re.search(r"(\d+(?:\.\d+)?)", params["size"])
        if size_match:
            struct.pack_into("f", out_data, 10196, float(size_match.group(1)))

    output_dir = os.path.dirname(base_preset_path)
    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, f"Toneprint - {output_name}.pst")
    with open(out_path, "wb") as f:
        f.write(out_data)

    print(f"-> Compiled Logic Space Designer Preset: 'Toneprint - {output_name}'")
    return True
