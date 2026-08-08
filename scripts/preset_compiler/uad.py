"""Universal Audio (UADx) preset compiler module for Paradise, LA-2A, Hitsville, Galaxy, and Studio D."""

from __future__ import annotations

import os
import json
import base64
import struct
import uuid
import math
import re
from typing import Dict, Any, Optional

from scripts.utils.param_types import to_float, to_bool, find_numeric_param, find_boolean_param
from .base import extract_markdown_section


def compile_uad_toneprint(
    filepath: str,
    base_preset: Dict[str, Any],
    output_name: str,
    frontmatter: Dict[str, Any],
) -> bool:
    """Compile Paradise Guitar Studio (Enigmatic, Dream, Woodrow, Ruby, Showtime, Lion) UADx JSON preset."""
    preset_data = frontmatter.get("preset_data", {})
    amp_settings = preset_data.get("amp_settings") if isinstance(preset_data, dict) else None
    amp_str = frontmatter.get("amp", "")

    amp_type = None
    amp_index = None
    cab_index = 2

    if "Dream" in amp_str:
        amp_type = "dream"
        amp_index = 0
        cab_index = 29
    elif "Enigmatic" in amp_str:
        amp_type = "enigmatic"
        amp_index = 1
        cab_index = 2
    elif "Woodrow" in amp_str:
        amp_type = "woodrow"
        amp_index = 5
        cab_index = 2
    elif "Ruby" in amp_str:
        amp_type = "ruby"
        amp_index = 3
        cab_index = 1
    elif "Showtime" in amp_str:
        amp_type = "showtime"
        amp_index = 4
        cab_index = 29
    elif "Lion" in amp_str:
        amp_type = "lion"
        amp_index = 2
        cab_index = 2

    if amp_type is None:
        return False

    boost_enable = None
    boost_amount = None
    reverb_val = None
    mod_val = None

    if amp_settings and isinstance(amp_settings, dict):
        vol = amp_settings.get("Volume")
        vol_mic = amp_settings.get("Volume (Mic)")
        treble = amp_settings.get("Treble")
        mid = amp_settings.get("Middle")
        bass = amp_settings.get("Bass")
        presence = amp_settings.get("Presence")
        master = amp_settings.get("Master")
        tone_cut = amp_settings.get("Tone Cut")
        bright = amp_settings.get("Bright")
        cut_sw = amp_settings.get("Cut")
        reverb_val = amp_settings.get("Reverb")
        mod_val = amp_settings.get("Mod")

        boost_raw = amp_settings.get("Boost")
        boost_sw_raw = amp_settings.get("Boost Switch")

        if boost_raw is not None:
            try:
                boost_amount = float(boost_raw)
            except ValueError:
                boost_enable = to_bool(boost_raw)

        if boost_sw_raw is not None:
            boost_enable = to_bool(boost_sw_raw)
        elif boost_amount is not None:
            boost_enable = boost_amount > 0.0

        if vol is not None: vol = float(vol)
        if vol_mic is not None: vol_mic = float(vol_mic)
        if treble is not None: treble = float(treble)
        if mid is not None: mid = float(mid)
        if bass is not None: bass = float(bass)
        if presence is not None: presence = float(presence)
        if master is not None: master = float(master)
        if tone_cut is not None: tone_cut = float(tone_cut)
        if bright is not None: bright = to_bool(bright)
        if cut_sw is not None: cut_sw = to_bool(cut_sw)
    else:
        with open(filepath, "r") as f:
            content = f.read()
        vol = find_numeric_param(content, ["Volume (Gain)", "Volume", "Volume (Inst)", "inst_volume"])
        vol_mic = find_numeric_param(content, ["Volume (Mic)", "mic_volume"])
        treble = find_numeric_param(content, ["Treble", "Top Boost Treble", "Tone"])
        mid = find_numeric_param(content, ["Middle", "Mids", "Top Boost Mids"])
        bass = find_numeric_param(content, ["Bass", "Top Boost Bass"])
        presence = find_numeric_param(content, ["Presence"])
        master = find_numeric_param(content, ["Master (labeled 6.5)", "Master", "Master volume"])
        tone_cut = find_numeric_param(content, ["Tone Cut"])
        bright = find_boolean_param(content, ["Bright Switch", "Bright / Normal", "Bright"])
        cut_sw = find_boolean_param(content, ["Cut Switch", "Cut"])
        reverb_val = find_numeric_param(content, ["Reverb"])

        boost_amount = find_numeric_param(content, ["Boost Control", "Boost (Stock)", "Boost"])
        boost_enable = find_boolean_param(content, ["Boost Switch", "Boost Button"])
        if boost_enable is None and boost_amount is not None:
            boost_enable = boost_amount > 0.0

    preset_data_json = json.loads(json.dumps(base_preset))
    preset_data_json["name"] = f"Toneprint - {output_name}"
    preset_data_json["uid"] = uuid.uuid4().hex

    controls = preset_data_json["chunk"]["controls"]
    controls["amp"] = {"real_value": amp_index}
    controls["cab_and_mic"] = {"real_value": cab_index}

    if amp_type == "dream":
        if vol is not None: controls["dream_volume"] = {"real_value": vol}
        if treble is not None: controls["dream_treble"] = {"real_value": treble}
        if bass is not None: controls["dream_bass"] = {"real_value": bass}
        if bright is not None: controls["dream_bright"] = {"real_value": bright}
        if boost_enable is not None: controls["dream_boost_enable"] = {"real_value": boost_enable}
        if boost_amount is not None: controls["dream_boost_amount"] = {"real_value": boost_amount}
        controls["dream_reverb_enable"] = {"real_value": True}
        controls["dream_reverb"] = {"real_value": float(reverb_val) if reverb_val is not None else 2.5}
        if mod_val is not None:
            mod_str = str(mod_val).upper()
            if "LEAD" in mod_str:
                controls["dream_amp_mod"] = {"real_value": 1}
            elif "TEX" in mod_str:
                controls["dream_amp_mod"] = {"real_value": 2}
            else:
                controls["dream_amp_mod"] = {"real_value": 0}
    elif amp_type == "enigmatic":
        if vol is not None: controls["enigmatic_volume"] = {"real_value": vol}
        if treble is not None: controls["enigmatic_treble"] = {"real_value": treble}
        if mid is not None: controls["enigmatic_middle"] = {"real_value": mid}
        if bass is not None: controls["enigmatic_bass"] = {"real_value": bass}
        if presence is not None: controls["enigmatic_presence"] = {"real_value": presence}
        if master is not None: controls["enigmatic_master_gain"] = {"real_value": master}
        if bright is not None: controls["enigmatic_bright_enable"] = {"real_value": bright}
        if boost_enable is not None: controls["enigmatic_boost_enable"] = {"real_value": boost_enable}
        voice_val = (amp_settings.get("Voice") or amp_settings.get("Model") or frontmatter.get("voice") if amp_settings else None)
        if voice_val:
            v_str = str(voice_val).upper()
            if "CREAM" in v_str:
                v_idx = 2
            elif "SANTA" in v_str:
                v_idx = 1
            elif "HRM" in v_str:
                v_idx = 3
            else:
                v_idx = 0
        else:
            v_idx = 0
        controls["enigmatic_model"] = {"real_value": v_idx}
        controls["enigmatic_channel"] = {"real_value": 1}
        controls["enigmatic_tone_stack_type"] = {"real_value": 0}
        controls["enigmatic_tone_stack_eq"] = {"real_value": 0}
        controls["enigmatic_overdrive_enable"] = {"real_value": False}
    elif amp_type == "ruby":
        if vol is not None: controls["ruby_volume"] = {"real_value": vol}
        if treble is not None: controls["ruby_treble"] = {"real_value": treble}
        if bass is not None: controls["ruby_bass"] = {"real_value": bass}
        if tone_cut is not None: controls["ruby_cut"] = {"real_value": tone_cut}
        if boost_enable is not None: controls["ruby_boost_enable"] = {"real_value": boost_enable}
        if boost_amount is not None: controls["ruby_boost_amount"] = {"real_value": boost_amount}
        controls["ruby_channel"] = {"real_value": 2}
        controls["ruby_tone_cut"] = {"real_value": 5.0 if cut_sw else 0.0}
    elif amp_type == "woodrow":
        if vol is not None: controls["woodrow_inst_volume"] = {"real_value": vol}
        if vol_mic is not None: controls["woodrow_mic_volume"] = {"real_value": vol_mic}
        if treble is not None: controls["woodrow_tone"] = {"real_value": treble}
        if boost_enable is not None: controls["woodrow_boost_enable"] = {"real_value": boost_enable}
        if boost_amount is not None: controls["woodrow_boost_amount"] = {"real_value": boost_amount}
    elif amp_type == "showtime":
        if vol is not None: controls["showtime_volume"] = {"real_value": vol}
        if treble is not None: controls["showtime_treble"] = {"real_value": treble}
        if mid is not None: controls["showtime_middle"] = {"real_value": mid}
        if bass is not None: controls["showtime_bass"] = {"real_value": bass}
        if bright is not None: controls["showtime_bright"] = {"real_value": bright}

    return True


def compile_la2a_toneprint(
    filepath: str,
    base_preset_path: str,
    output_name: str,
    frontmatter: Dict[str, Any],
) -> bool:
    """Compile UADx Teletronix LA-2A Silver/Gray JSON preset."""
    preset_data = frontmatter.get("preset_data", {})
    la2a_data = preset_data.get("la2a") if isinstance(preset_data, dict) else None

    if la2a_data and isinstance(la2a_data, dict):
        peak_reduction = to_float(la2a_data.get("peak_reduction"))
        gain = to_float(la2a_data.get("gain"))
        mode_compress = to_bool(la2a_data.get("compress"))
    else:
        with open(filepath, "r") as f:
            content = f.read()
        peak_reduction = find_numeric_param(content, ["Peak Reduction"])
        gain = find_numeric_param(content, ["Gain", "Makeup Gain"])
        mode_compress = find_boolean_param(content, ["Compress Mode", "Compress"])

    if peak_reduction is None and gain is None:
        return False

    with open(base_preset_path, "r") as f:
        preset_dict = json.load(f)

    chunk_bytes = bytearray(base64.b64decode(preset_dict["chunk"]))

    if peak_reduction is not None:
        struct.pack_into("f", chunk_bytes, 10 * 4, peak_reduction / 100.0 if peak_reduction > 1.0 else peak_reduction)
    if gain is not None:
        struct.pack_into("f", chunk_bytes, 11 * 4, gain / 100.0 if gain > 1.0 else gain)
    if mode_compress is not None:
        struct.pack_into("f", chunk_bytes, 13 * 4, 1.0 if mode_compress else 0.0)

    preset_dict["chunk"] = base64.b64encode(chunk_bytes).decode("utf-8")
    preset_dict["name"] = f"Toneprint - {output_name}"
    preset_dict["uid"] = uuid.uuid4().hex

    output_dir = os.path.dirname(base_preset_path)
    out_path = os.path.join(output_dir, f"Toneprint - {output_name}.json")
    with open(out_path, "w") as f:
        json.dump(preset_dict, f, indent=4)

    print(f"-> Compiled UADx LA-2A Preset: 'Toneprint - {output_name}'")
    return True


def compile_hitsville_toneprint(
    filepath: str,
    base_preset_path: str,
    output_name: str,
    frontmatter: Dict[str, Any],
) -> bool:
    """Compile UADx Hitsville Reverb Chambers JSON preset."""
    preset_data = frontmatter.get("preset_data", {})
    hitsville_data = preset_data.get("hitsville") if isinstance(preset_data, dict) else None

    if hitsville_data and isinstance(hitsville_data, dict):
        mix = to_float(hitsville_data.get("mix"))
        pre_delay = to_float(hitsville_data.get("pre_delay"))
        decay = to_float(hitsville_data.get("decay"))
        chamber = hitsville_data.get("chamber")
        speaker = hitsville_data.get("speaker")
        mic = hitsville_data.get("mic")
    else:
        with open(filepath, "r") as f:
            content = f.read()
        mix = find_numeric_param(content, ["Mix", "Room Mix"])
        pre_delay = find_numeric_param(content, ["Pre-Delay"])
        decay = find_numeric_param(content, ["Decay"])

        m_ch = re.search(r"\|\s*Chamber\s*\|\s*\*\*([A-Za-z0-9/ ]+)\*\*", content, re.IGNORECASE)
        chamber = m_ch.group(1).strip() if m_ch else None
        m_spk = re.search(r"\|\s*Speaker\s*\|\s*\*\*([A-Za-z0-9/ ]+)\*\*", content, re.IGNORECASE)
        speaker = m_spk.group(1).strip() if m_spk else None
        m_mic = re.search(r"\|\s*Mic\s*\|\s*\*\*([A-Za-z0-9/ ]+)\*\*", content, re.IGNORECASE)
        mic = m_mic.group(1).strip() if m_mic else None

    if mix is None and pre_delay is None and decay is None and chamber is None and speaker is None and mic is None:
        return False

    with open(base_preset_path, "r") as f:
        preset_dict = json.load(f)

    chunk_bytes = bytearray(base64.b64decode(preset_dict["chunk"]))

    if chamber is not None:
        ch_str = str(chamber).lower()
        val = 1.0 if ("2644" in ch_str or "2" in ch_str) else 0.0
        struct.pack_into("f", chunk_bytes, 10 * 4, val)

    if speaker is not None:
        spk_str = str(speaker).lower()
        val = 1.0 if ("jbl" in spk_str or "bose" in spk_str or "2" in spk_str or "set 2" in spk_str) else 0.0
        struct.pack_into("f", chunk_bytes, 13 * 4, val)

    if mic is not None:
        mic_str = str(mic).lower()
        if "545" in mic_str or "unidyne" in mic_str or mic_str == "1":
            val = 0.0
        elif "rca" in mic_str or "44" in mic_str or mic_str == "2":
            val = 1.0 / 3.0
        elif "ev" in mic_str or "631" in mic_str or mic_str == "3":
            val = 2.0 / 3.0
        elif "km86" in mic_str or "km 86" in mic_str or mic_str == "4":
            val = 1.0
        else:
            val = 0.0
        struct.pack_into("f", chunk_bytes, 14 * 4, val)

    if pre_delay is not None:
        val_scaled = math.log(pre_delay / 22.9 + 1.0) / math.log(250.0 / 22.9 + 1.0)
        struct.pack_into("f", chunk_bytes, 17 * 4, val_scaled)

    if decay is not None:
        struct.pack_into("f", chunk_bytes, 20 * 4, decay / 10.0)

    if mix is not None:
        struct.pack_into("f", chunk_bytes, 21 * 4, mix / 100.0 if mix > 1.0 else mix)

    struct.pack_into("f", chunk_bytes, 22 * 4, 1.0)
    struct.pack_into("f", chunk_bytes, 18 * 4, 0.5)
    struct.pack_into("f", chunk_bytes, 19 * 4, 0.5)

    preset_dict["chunk"] = base64.b64encode(chunk_bytes).decode("utf-8")
    preset_dict["name"] = f"Toneprint - {output_name}"
    preset_dict["uid"] = uuid.uuid4().hex

    output_dir = os.path.dirname(base_preset_path)
    out_path = os.path.join(output_dir, f"Toneprint - {output_name}.json")
    with open(out_path, "w") as f:
        json.dump(preset_dict, f, indent=4)

    print(f"-> Compiled UADx Hitsville Reverb Preset: 'Toneprint - {output_name}'")
    return True


def ms_to_galaxy_knob(ms_val: float, head_mode: int) -> float:
    mode_heads = {
        1: [1], 2: [2], 3: [3], 4: [1, 2], 5: [1, 2],
        6: [3], 7: [1, 3], 8: [2, 3], 9: [1], 10: [1, 2, 3],
        11: [2], 12: []
    }
    heads_in_mode = mode_heads.get(head_mode, [1])
    ranges = {1: (69.0, 177.0), 2: (131.0, 337.0), 3: (189.0, 489.0)}
    target_head = None
    for h in heads_in_mode:
        r_min, r_max = ranges[h]
        if r_min <= ms_val <= r_max:
            target_head = h
            break
    if target_head is None:
        for h in [1, 2, 3]:
            r_min, r_max = ranges[h]
            if r_min <= ms_val <= r_max:
                target_head = h
                break
    if target_head is None:
        target_head = heads_in_mode[0] if heads_in_mode else 1

    r_min, r_max = ranges[target_head]
    knob = (r_max - ms_val) / (r_max - r_min)
    return max(0.0, min(1.0, knob))


def scale_galaxy_value(val_raw: Any, is_rate: bool = False, head_mode: int = 1) -> Optional[float]:
    if val_raw is None:
        return None
    val_str = str(val_raw).strip()
    if "%" in val_str:
        match = re.search(r"([-+]?[0-9]*\.?[0-9]+)", val_str)
        if match:
            return float(match.group(1)) / 100.0
    if "ms" in val_str.lower() or "sec" in val_str.lower() or ("s" in val_str.lower() and "ms" not in val_str.lower()):
        match = re.search(r"([~0-9.+−-]+)", val_str)
        if match:
            ms_val = float(match.group(1).replace("−", "-").replace("~", ""))
            if ("s" in val_str.lower() or "sec" in val_str.lower()) and "ms" not in val_str.lower():
                ms_val *= 1000.0
            return ms_to_galaxy_knob(ms_val, head_mode)
    match = re.search(r"([-+]?[0-9]*\.?[0-9]+)", val_str)
    if match:
        val = float(match.group(1))
        if is_rate:
            return ms_to_galaxy_knob(val, head_mode) if val > 10.0 else val / 10.0
        return val / 10.0
    return None


def compile_galaxy_toneprint(
    filepath: str,
    base_preset_path: str,
    output_name: str,
    frontmatter: Dict[str, Any],
) -> bool:
    """Compile UADx Galaxy Tape Echo JSON preset."""
    preset_data = frontmatter.get("preset_data", {})
    galaxy_data = preset_data.get("galaxy") if isinstance(preset_data, dict) else None

    try:
        with open(filepath, "r") as f:
            full_content = f.read()
        content = extract_markdown_section(full_content, ["Galaxy Tape Echo", "Galaxy"])
    except Exception as e:
        print(f"Error reading tone file for Galaxy parsing: {e}")
        content = ""

    echo_rate_raw = None
    feedback_raw = None
    echo_volume_raw = None
    reverb_volume_raw = None
    head_select_raw = None
    tape_age_raw = None

    if galaxy_data and isinstance(galaxy_data, dict):
        echo_rate_raw = galaxy_data.get("echo_rate")
        feedback_raw = galaxy_data.get("feedback")
        echo_volume_raw = galaxy_data.get("echo_volume")
        reverb_volume_raw = galaxy_data.get("reverb_volume")
        head_select_raw = galaxy_data.get("head_select")
        tape_age_raw = galaxy_data.get("tape_age")

    if echo_rate_raw is None:
        echo_rate_raw = find_numeric_param(content, ["Echo Rate", "Rate"])
    if feedback_raw is None:
        feedback_raw = find_numeric_param(content, ["Feedback"])
    if echo_volume_raw is None:
        echo_volume_raw = find_numeric_param(content, ["Echo Volume", "Volume (Echo)", "Echo Vol", "Mix / Wet Solo", "Mix / Wet", "Mix"])
    if reverb_volume_raw is None:
        reverb_volume_raw = find_numeric_param(content, ["Reverb Volume", "Reverb Vol"])
    if head_select_raw is None:
        m_hs = re.search(r"\|\s*(?:Head Select|Head|Mode)\s*\|\s*([^|]+)\s*\|", content, re.IGNORECASE)
        head_select_raw = m_hs.group(1).strip() if m_hs else None
    if tape_age_raw is None:
        m_ta = re.search(r"\|\s*Tape Age\s*\|\s*([^|]+)\s*\|", content, re.IGNORECASE)
        tape_age_raw = m_ta.group(1).strip() if m_ta else None

    head_mode = 1
    if head_select_raw is not None:
        hs_str = str(head_select_raw).lower()
        if "1+2+3" in hs_str or "1,2,3" in hs_str or "all" in hs_str:
            head_mode = 10
        elif "1+3" in hs_str or "1,3" in hs_str:
            head_mode = 7
        elif "2+3" in hs_str or "2,3" in hs_str:
            head_mode = 8
        elif "1+2" in hs_str or "1,2" in hs_str:
            head_mode = 5 if ("reverb" in hs_str or "rev" in hs_str) else 4
        elif "reverb" in hs_str:
            head_mode = 12
        else:
            clean_hs = "".join(c for c in hs_str if c.isdigit() or c == ".")
            if clean_hs:
                try:
                    head_mode = int(float(clean_hs))
                except ValueError:
                    head_mode = 1

    echo_rate = scale_galaxy_value(echo_rate_raw, is_rate=True, head_mode=head_mode)
    feedback = scale_galaxy_value(feedback_raw, is_rate=False, head_mode=head_mode)
    echo_volume = scale_galaxy_value(echo_volume_raw, is_rate=False, head_mode=head_mode)
    reverb_volume = scale_galaxy_value(reverb_volume_raw, is_rate=False, head_mode=head_mode)

    tape_age = None
    if tape_age_raw is not None:
        ta_lower = str(tape_age_raw).lower()
        if "new" in ta_lower: tape_age = 0.0
        elif "used" in ta_lower: tape_age = 0.5
        elif "old" in ta_lower: tape_age = 1.0
        else: tape_age = to_float(tape_age_raw, default=0.0)

    if echo_rate is None and feedback is None and echo_volume is None:
        return False

    with open(base_preset_path, "r") as f:
        preset_data_json = json.load(f)

    chunk_bytes = bytearray(base64.b64decode(preset_data_json["chunk"]))

    if echo_rate is not None: struct.pack_into("f", chunk_bytes, 19 * 4, echo_rate)
    if reverb_volume is not None: struct.pack_into("f", chunk_bytes, 20 * 4, reverb_volume)
    if feedback is not None: struct.pack_into("f", chunk_bytes, 21 * 4, feedback)
    if echo_volume is not None: struct.pack_into("f", chunk_bytes, 22 * 4, echo_volume)
    if tape_age is not None: struct.pack_into("f", chunk_bytes, 23 * 4, tape_age)
    if head_select_raw is not None: struct.pack_into("f", chunk_bytes, 14 * 4, (head_mode - 1) / 11.0)

    preset_data_json["chunk"] = base64.b64encode(chunk_bytes).decode("utf-8")
    preset_data_json["name"] = f"Toneprint - {output_name}"
    preset_data_json["uid"] = uuid.uuid4().hex

    output_dir = os.path.dirname(base_preset_path)
    out_path = os.path.join(output_dir, f"Toneprint - {output_name}.json")

    with open(out_path, "w") as f:
        json.dump(preset_data_json, f, indent=4)
    print(f"-> Compiled UADx Galaxy Tape Echo Preset: 'Toneprint - {output_name}'")
    return True


def compile_studio_d_toneprint(
    filepath: str,
    base_preset_path: str,
    output_name: str,
    frontmatter: Dict[str, Any],
) -> bool:
    """Compile UADx Studio D Chorus JSON preset."""
    preset_data = frontmatter.get("preset_data", {})
    studio_d_data = preset_data.get("studio_d") if isinstance(preset_data, dict) else None

    mode = None
    power = None

    if studio_d_data and isinstance(studio_d_data, dict):
        mode = studio_d_data.get("mode")
        power = to_bool(studio_d_data.get("power"))
    else:
        with open(filepath, "r") as f:
            full_content = f.read()
        content = extract_markdown_section(full_content, ["Studio D Chorus", "Studio D", "Dimension D", "Dimension Chorus"])
        mode_match = re.search(r"\|\s*Mode\s*\|\s*(?:\*\*)?([^|]+?)(?:\*\*)?\s*\|", content, re.IGNORECASE)
        if mode_match:
            mode = mode_match.group(1).strip()
        else:
            mode_num = find_numeric_param(content, ["Mode"])
            if mode_num is not None:
                mode = str(int(mode_num))

        power = find_boolean_param(content, ["Power"])
        bypass = find_boolean_param(content, ["Bypass"])
        if bypass is not None:
            power = not bypass

    if mode is None and power is None:
        return False

    with open(base_preset_path, "r") as f:
        preset_data_json = json.load(f)

    chunk_bytes = bytearray(base64.b64decode(preset_data_json["chunk"]))

    if mode is not None:
        mode_str = str(mode).lower().strip()
        mode_val = 0.0
        if mode_str in ("off", "0", "none", "bypassed"):
            mode_val = 0.0
        elif mode_str in ("all", "secret", "1+2+3+4", "1,2,3,4"):
            mode_val = 1.0
        else:
            parts = re.findall(r"\d", mode_str)
            if parts:
                weight_sum = 0
                for part in parts:
                    n = int(part)
                    if n == 1: weight_sum += 1
                    elif n == 2: weight_sum += 2
                    elif n == 3: weight_sum += 4
                    elif n == 4: weight_sum += 8
                mode_val = min(1.0, max(0.0, weight_sum / 15.0))
            else:
                mode_val = to_float(mode_str, default=0.0)

        struct.pack_into("f", chunk_bytes, 10 * 4, mode_val)

    if power is not None:
        struct.pack_into("f", chunk_bytes, 12 * 4, 1.0 if power else 0.0)

    preset_data_json["chunk"] = base64.b64encode(chunk_bytes).decode("utf-8")
    preset_data_json["name"] = f"Toneprint - {output_name}"
    preset_data_json["uid"] = uuid.uuid4().hex

    output_dir = os.path.dirname(base_preset_path)
    out_path = os.path.join(output_dir, f"Toneprint - {output_name}.json")
    with open(out_path, "w") as f:
        json.dump(preset_data_json, f, indent=4)
    print(f"-> Compiled UADx Studio D Chorus Preset: 'Toneprint - {output_name}'")
    return True
