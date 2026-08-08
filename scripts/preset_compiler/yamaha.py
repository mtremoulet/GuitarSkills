"""Yamaha THR-II L6Preset JSON generator module."""

from __future__ import annotations

import os
import json
from typing import Dict, Any, Union

from scripts.utils.config import YAMAHA_THR_OUTPUT_DIR
from scripts.utils.param_types import to_float, to_bool

THR_MODELS = {
    "envelope": {
        "device": 2359296,
        "device_version": 22020194,
        "schema": "L6Preset",
        "version": 5,
        "outer_meta": {"original": 0, "pbn": 0, "premium": 0},
        "default_tempo": 110,
        "gate_threshold_db": {
            "slope": 0.96,
            "ui_offset": 100,
            "min_db": -96.0,
            "max_db": 0.0,
            "default_ui": 65
        }
    },
    "amps": {
        "guitar": {
            "Classic":  {"Clean": "THR10C_Deluxe",  "Crunch": "THR10C_DC30", "Lead": "THR10_Lead",    "Hi Gain": "THR10_Modern", "Special": "THR10X_Brown1"},
            "Boutique": {"Clean": "THR10C_BJunior2", "Crunch": "THR30_SR101", "Lead": "THR30_Blondie", "Hi Gain": "THR30_FLead",  "Special": "THR10X_South"},
            "Modern":   {"Clean": "THR30_Carmen",    "Crunch": "THR10C_Mini", "Lead": "THR10_Brit",    "Hi Gain": "THR10X_Brown2", "Special": "THR30_Stealth"}
        },
        "bass": {"Classic": "THR10_Bass_Eden_Marcus", "Boutique": "THR10_Bass_Mesa", "Modern": "THR30_JKBass2"},
        "acoustic": {
            "Condenser": "THR10_Aco_Condenser1",
            "Dynamic": "THR10_Aco_Dynamic1",
            "Tube": "THR10_Aco_Tube1",
            "Nylon": "THR10_Aco_Nylon1"
        },
        "flat": {"default": "THR10_Flat", "Classic": "THR10_Flat", "Boutique": "THR10_Flat_B", "Modern": "THR10_Flat_V", "V": "THR10_Flat_V", "A": "THR10_Flat_A", "B": "THR10_Flat_B", "plain": "THR10_Flat"}
    },
    "cabinets": {
        "British 4x12": 0, "American 4x12": 1, "Brown 4x12": 2, "Vintage 4x12": 3,
        "Fuel 4x12": 4, "Juicy 4x12": 5, "Mods 4x12": 6, "American 2x12": 7,
        "British 2x12": 8, "British Blues 2x12": 9, "Boutique 2x12": 10,
        "Yamaha 2x12": 11, "California 1x12": 12, "American 1x12": 13,
        "American 4x10": 14, "Boutique 1x12": 15, "None": 16, "Flat": 16, "BYPASS": 16
    },
    "fx": {
        "gate": {"group": "THRGroupGate", "asset": "noiseGate", "params": ["Thresh", "Decay"]},
        "compressor": {"group": "THRGroupFX1Compressor", "asset": "RedComp", "params": ["Sustain", "Level"]},
        "modulation": {
            "group": "THRGroupFX2Effect",
            "has_wetDry": True,
            "types": {
                "Chorus":   {"asset": "StereoSquareChorus", "params": ["Depth", "Feedback", "Freq", "Pre"]},
                "Tremolo":  {"asset": "BiasTremolo",        "params": ["Depth", "Speed"]},
                "Flanger":  {"asset": "L6Flanger",          "params": ["Depth", "Freq"]},
                "Phaser":   {"asset": "Phaser",             "params": ["Feedback", "Speed"]}
            }
        },
        "echo": {
            "group": "THRGroupFX3EffectEcho",
            "has_wetDry": True,
            "types": {
                "Tape":          {"asset": "TapeEcho",       "params": ["Time", "Bass", "Treble", "Feedback"]},
                "Digital Delay": {"asset": "L6DigitalDelay", "params": ["Time", "Bass", "Treble", "Feedback"]}
            }
        },
        "reverb": {
            "group": "THRGroupFX4EffectReverb",
            "has_wetDry": True,
            "types": {
                "Hall":   {"asset": "ReallyLargeHall", "params": ["Decay", "PreDelay", "Tone"]},
                "Plate":  {"asset": "LargePlate1",     "params": ["Decay", "PreDelay", "Tone"]},
                "Room":   {"asset": "SmallRoom1",      "params": ["Decay", "PreDelay", "Tone"]},
                "Spring": {"asset": "StandardSpring",  "params": ["Time", "Tone"]}
            }
        },
        "cab": {"group": "THRGroupCab", "asset": "speakerSimulator", "params": ["SpkSimType"]},
        "amp": {"group": "THRGroupAmp", "params": ["Drive", "Bass", "Mid", "Treble", "Master"]}
    },
    "all_known_assets": {
        "amps": [
            "THR10C_Deluxe", "THR10C_DC30", "THR10C_Mini", "THR10C_BJunior2",
            "THR10X_Brown1", "THR10X_Brown2", "THR10X_South",
            "THR10_Lead", "THR10_Modern", "THR10_Brit", "THR10_Flat", "THR10_Flat_A", "THR10_Flat_B", "THR10_Flat_V",
            "THR10_Bass_Eden_Marcus", "THR10_Bass_Mesa",
            "THR10_Aco_Condenser1", "THR10_Aco_Dynamic1", "THR10_Aco_Tube1", "THR10_Aco_Nylon1",
            "THR30_Carmen", "THR30_SR101", "THR30_Blondie", "THR30_FLead", "THR30_Stealth", "THR30_JKBass2"
        ],
        "fx_assets": [
            "noiseGate", "RedComp", "speakerSimulator",
            "StereoSquareChorus", "L6SineChorus", "BiasTremolo", "L6Flanger", "Phaser",
            "TapeEcho", "L6DigitalDelay",
            "ReallyLargeHall", "LargePlate1", "SmallRoom1", "StandardSpring"
        ]
    }
}


def detect_thr_device_id() -> int:
    """Best-effort detection of connected THR-II device ID."""
    rel = ["Yamaha", "THR Remote", "deviceConnection.json"]
    paths = []
    for env in ("APPDATA", "LOCALAPPDATA", "USERPROFILE"):
        base = os.environ.get(env)
        if base:
            paths.append(os.path.join(base, *rel))
            paths.append(os.path.join(base, "AppData", "Roaming", *rel))
    home = os.path.expanduser("~")
    paths.append(os.path.join(home, "Library", "Application Support", *rel))
    paths.append(os.path.join(home, ".config", *rel))

    for p in paths:
        try:
            if os.path.isfile(p):
                with open(p, "r", encoding="utf-8") as f:
                    d = json.load(f)
                dev = d.get("device") or d.get("deviceId") or d.get("device_id")
                if isinstance(dev, int) and dev > 0:
                    return dev
        except Exception:
            pass
    return THR_MODELS["envelope"]["device"]


def compile_yamaha_thr_toneprint(
    filepath: str,
    output_name: str,
    frontmatter: Dict[str, Any],
) -> bool:
    """Compile Yamaha THR-II (.thrl6p) preset JSON."""
    preset_data = frontmatter.get("preset_data", {})
    thr_data = preset_data.get("yamaha_thr") if isinstance(preset_data, dict) else None

    if not thr_data or not isinstance(thr_data, dict):
        return False

    _DEFAULT = 50

    def _norm(value) -> float:
        return to_float(value, default=_DEFAULT, min_val=0.0, max_val=100.0) / 100.0

    def _gate_thresh_db(ui_value) -> float:
        cfg = THR_MODELS["envelope"]["gate_threshold_db"]
        ui = to_float(ui_value, default=cfg["default_ui"])
        db = (ui - cfg["ui_offset"]) * cfg["slope"]
        return round(max(cfg["min_db"], min(cfg["max_db"], db)), 2)

    def resolve_amp(category: str | None = None, model: str | None = None, asset: str | None = None) -> str:
        if asset:
            if asset not in THR_MODELS["all_known_assets"]["amps"]:
                raise ValueError(f"Unknown amp asset {asset!r}")
            return asset
        if not category:
            raise ValueError("amp spec needs either 'asset' or 'category'")

        cat = category.strip().capitalize()
        amps = THR_MODELS["amps"]
        if cat in amps["guitar"]:
            m_key = model.strip().capitalize() if model else "Clean"
            return amps["guitar"][cat].get(m_key, amps["guitar"][cat]["Clean"])
        if cat == "Bass":
            return amps["bass"].get(model or "Classic", amps["bass"]["Classic"])
        if cat == "Acoustic":
            return amps["acoustic"].get(model or "Condenser", amps["acoustic"]["Condenser"])
        if cat == "Flat":
            return amps["flat"].get(model or "default", amps["flat"]["default"])
        raise ValueError(f"Unknown amp category {category!r}")

    def resolve_cab(cab) -> int:
        cabs = THR_MODELS["cabinets"]
        if cab is None: return cabs["None"]
        if isinstance(cab, int): return cab
        name = str(cab).strip()
        for key, val in cabs.items():
            if key.lower() == name.lower():
                return val
        return cabs["None"]

    def _block_params(spec_block: dict, device_params: list[str]) -> dict:
        out = {}
        for dev_key in device_params:
            out[dev_key] = _norm(spec_block.get(dev_key.lower(), _DEFAULT))
        return out

    def _match_type(name, types: dict) -> str:
        for key in types:
            if key.lower() == str(name).strip().lower():
                return key
        return list(types.keys())[0]

    def _build_typed_fx(spec_block: dict, fx_def: dict, default_type: str) -> dict:
        types = fx_def["types"]
        type_name = spec_block.get("type", default_type)
        chosen = _match_type(type_name, types)
        asset = types[chosen]["asset"]
        block = {"@asset": asset, "@enabled": to_bool(spec_block.get("enabled", False))}
        block.update(_block_params(spec_block, types[chosen]["params"]))
        if fx_def.get("has_wetDry"):
            block["@wetDry"] = _norm(spec_block.get("mix", _DEFAULT))
        return block

    try:
        env = THR_MODELS["envelope"]
        fx = THR_MODELS["fx"]

        amp_spec = thr_data.get("amp", {})
        amp_asset = resolve_amp(amp_spec.get("category"), amp_spec.get("model"), asset=amp_spec.get("asset"))
        cab_type = resolve_cab(thr_data.get("cab"))
        eq = thr_data.get("eq", {})

        amp_block = {
            "@asset": amp_asset,
            "Drive": _norm(eq.get("gain", _DEFAULT)),
            "Bass": _norm(eq.get("bass", _DEFAULT)),
            "Mid": _norm(eq.get("mid", _DEFAULT)),
            "Treble": _norm(eq.get("treble", _DEFAULT)),
            "Master": _norm(eq.get("master", 70)),
        }

        comp_spec = thr_data.get("compressor", {})
        comp_block = {
            "@asset": fx["compressor"]["asset"],
            "@enabled": to_bool(comp_spec.get("enabled", False)),
            "Sustain": _norm(comp_spec.get("sustain", 30)),
            "Level": _norm(comp_spec.get("level", 80)),
        }

        gate_spec = thr_data.get("gate", {})
        gate_block = {
            "@asset": fx["gate"]["asset"],
            "@enabled": to_bool(gate_spec.get("enabled", False)),
            "Thresh": _gate_thresh_db(gate_spec.get("thresh", env["gate_threshold_db"]["default_ui"])),
            "Decay": _norm(gate_spec.get("decay", 20)),
        }

        device_id = detect_thr_device_id()

        preset_json = {
            "schema": env["schema"],
            "version": env["version"],
            "data": {
                "device": device_id,
                "device_version": env["device_version"],
                "meta": {"name": output_name, "tnid": 0},
                "tone": {
                    "THRGroupGate": gate_block,
                    "THRGroupFX1Compressor": comp_block,
                    "THRGroupFX2Effect": _build_typed_fx(thr_data.get("modulation", {}), fx["modulation"], "Chorus"),
                    "THRGroupFX3EffectEcho": _build_typed_fx(thr_data.get("echo", {}), fx["echo"], "Tape"),
                    "THRGroupFX4EffectReverb": _build_typed_fx(thr_data.get("reverb", {}), fx["reverb"], "Hall"),
                    "THRGroupCab": {"@asset": fx["cab"]["asset"], "SpkSimType": cab_type},
                    "THRGroupAmp": amp_block,
                    "global": {"THRPresetParamTempo": int(thr_data.get("tempo", env["default_tempo"]))},
                }
            },
            "meta": env["outer_meta"]
        }

        os.makedirs(YAMAHA_THR_OUTPUT_DIR, exist_ok=True)
        out_path = os.path.join(YAMAHA_THR_OUTPUT_DIR, f"{output_name}.thrl6p")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(preset_json, f, indent=4)
            f.write("\n")

        print(f"-> Compiled Yamaha THR Preset: '{output_name}'")
        return True

    except Exception as e:
        print(f"Error compiling Yamaha THR preset: {e}")
        return False
