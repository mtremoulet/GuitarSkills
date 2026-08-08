"""Neural DSP Archetype Cory Wong preset compiler module."""

from __future__ import annotations

import os
from typing import Dict, Any, Union
from scripts.utils.config import NEURAL_OUTPUT_DIR
from scripts.utils.param_types import to_float, to_bool
from .base import (
    replace_binary_parameter,
    find_numeric_parameter,
    find_boolean_parameter,
)

PERCENTAGE_KEYS = {
    "compressorBlend", "compressorCompression", "compressorVolume", "compressorTone",
    "bigRigDrive", "bigRigLevel", "bigRigTone",
    "tuberLevel", "tuberDrive", "tuberTone",
    "washMix", "washDecay", "washLowCut", "washHighCut",
    "snobVolume", "snobMaster", "snobBass", "snobMid", "snobTreble", "snobPresence", "snobOutputLevel",
    "cleanVolume", "cleanBass", "cleanMid", "cleanTreble", "cleanPresence", "cleanOutputLevel",
    "funkVolume", "funkTubeSat", "funkComp",
    "chorusMix", "chorusWidth", "chorusRate",
    "delayMix", "delayFeedback"
}


def compile_neural_toneprint(
    filepath: str,
    base_data: Union[str, bytes],
    output_name: str,
    frontmatter: Dict[str, Any],
) -> bool:
    """Compile a Neural DSP Archetype Cory Wong preset from toneprint markdown and frontmatter."""
    if isinstance(base_data, str) and os.path.exists(base_data):
        with open(base_data, "rb") as f:
            base_bytes = f.read()
    elif isinstance(base_data, bytes):
        base_bytes = base_data
    else:
        print(f"Warning: Invalid base_data provided for Neural compilation: {base_data}")
        return False

    preset_data = frontmatter.get("preset_data", {})
    amp_settings = preset_data.get("amp_settings") if isinstance(preset_data, dict) else None

    settings: Dict[str, str] = {"name": output_name}

    if amp_settings and isinstance(amp_settings, dict):
        for k, v in amp_settings.items():
            if isinstance(v, bool):
                settings[k] = "true" if v else "false"
            elif isinstance(v, (int, float)) and k in PERCENTAGE_KEYS:
                f_val = float(v)
                scaled = f_val / 100.0 if f_val > 1.0 else f_val
                settings[k] = f"{scaled:.4f}"
            else:
                settings[k] = str(v)
    else:
        with open(filepath, "r") as f:
            content = f.read()

        comp_active = find_boolean_parameter(content, ["The 4th Position Compressor", "Compressor Active", "Compressor"])
        if comp_active is not None:
            settings["compressorActive"] = "true" if comp_active else "false"

        for key in ["Blend", "Tone", "Compression", "Volume"]:
            val = find_numeric_parameter(content, [key])
            if val is not None:
                settings["compressor" + key] = f"{val:.2f}"

        settings["selectedAmp"] = "2"
        settings["selectedCab"] = "2"
        settings["ampCabLinkedState"] = "false"

        knobs = {
            "snobBass": ["Bass"],
            "snobMid": ["Middle", "Mids"],
            "snobTreble": ["Treble"],
            "snobPresence": ["Presence"],
            "snobMaster": ["Master"],
            "snobVolume": ["Volume (Gain)", "Volume"],
            "snobOutputLevel": ["Output"]
        }

        for param, names in knobs.items():
            val = find_numeric_parameter(content, names)
            if val is not None:
                settings[param] = f"{val:.2f}"

        drive = find_boolean_parameter(content, ["Drive Switch", "Drive"])
        if drive is not None:
            settings["snobDrive"] = "true" if drive else "false"

        bright = find_boolean_parameter(content, ["Bright Switch", "Bright"])
        if bright is not None:
            settings["snobBright"] = "true" if bright else "false"

        pos = find_numeric_parameter(content, ["Position L", "Position"])
        if pos is not None:
            settings["leftCabPosition"] = f"{pos:.2f}"

        dist = find_numeric_parameter(content, ["Distance L", "Distance"])
        if dist is not None:
            settings["leftCabDistance"] = f"{dist:.2f}"

        room = find_numeric_parameter(content, ["Room Send L", "Room Send"])
        if room is not None:
            settings["leftRoomMicLevel"] = f"{room:.1f}"

        settings["leftCabActive"] = "true"
        settings["leftCab0MicType"] = "4"
        settings["rightCabActive"] = "false"

        eq_active = find_boolean_parameter(content, ["EQ Status", "EQ Active", "snobEQActive"])
        if eq_active is not None:
            settings["snobEQActive"] = "true" if eq_active else "false"

        bands = ["65 Hz", "125 Hz", "250 Hz", "500 Hz", "1 kHz", "2 kHz", "4 kHz", "8 kHz", "16 kHz"]
        for i, band in enumerate(bands, 1):
            val = find_numeric_parameter(content, [band])
            if val is not None:
                settings[f"snobEQBand{i}"] = f"{val:.1f}"

        settings["snobEQHpf"] = "20.0"
        settings["snobEQLpf"] = "20000.0"

        for pedal in ["tuberActive", "bigRigActive", "postalActive", "delayActive", "washActive", "chorusActive"]:
            settings[pedal] = "false"

    settings["inputGain"] = "0.0"
    settings["outputGain"] = "0.0"

    overrides = frontmatter.get("preset_overrides", {})
    if isinstance(overrides, dict):
        for k, v in overrides.items():
            if isinstance(v, bool):
                settings[k] = "true" if v else "false"
            else:
                settings[k] = str(v)

    preset_data_bytes = base_bytes
    for key, val in settings.items():
        preset_data_bytes = replace_binary_parameter(preset_data_bytes, key, val)

    os.makedirs(NEURAL_OUTPUT_DIR, exist_ok=True)
    out_path = os.path.join(NEURAL_OUTPUT_DIR, f"{output_name}.xml")
    with open(out_path, "wb") as f:
        f.write(preset_data_bytes)
    print(f"-> Compiled Neural Preset: '{output_name}'")
    return True
