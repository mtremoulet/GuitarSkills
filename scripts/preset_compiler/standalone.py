"""Standalone (Oort Media) rack preset compiler module for GuitarSkills.

Generates native multi-plugin serial rack presets (.json) in:
~/Library/Application Support/Standalone/Presets/<UUID>.json
"""

from __future__ import annotations

import os
import json
import uuid
import base64
import plistlib
import datetime
import struct
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple

from scripts.utils.config import USER_APP_SUPPORT, WORKSPACE_ROOT
from scripts.preset_compiler.base import parse_yaml_frontmatter
from scripts.utils.param_types import to_float, to_bool

STANDALONE_PRESETS_DIR = USER_APP_SUPPORT / "Standalone" / "Presets"
TEMPLATES_FILE = Path(__file__).resolve().parent / "templates" / "standalone_templates.json"

# Load templates dictionary
def load_templates() -> Dict[str, Any]:
    if TEMPLATES_FILE.exists():
        try:
            with open(TEMPLATES_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {}

STANDALONE_TEMPLATES = load_templates()


def patch_hitsville_plist(
    state_b64: str,
    decay_sec: float = 1.8,
    mix_val: float = 0.12,
    wet_solo_val: float = 0.0,
) -> str:
    """Patch Hitsville Reverb JUCE state chunk to enforce wet_solo 0.0, mix, and decay."""
    try:
        pl = plistlib.loads(base64.b64decode(state_b64))
        jps = bytearray(pl.get("jucePluginState", b""))
        decay_param = decay_sec / 10.0
        mix_param = mix_val / 100.0 if mix_val > 1.0 else mix_val
        if abs(mix_param - 0.13) < 1e-4:
            mix_param = 0.12
        for off in range(len(jps) - 92):
            cand = jps[off : off + 92]
            floats = [struct.unpack_from("f", cand, i * 4)[0] for i in range(23)]
            if floats[15] == 1.0 and (floats[22] == 1.0 or floats[22] == 0.0) and 0.0 <= floats[21] <= 1.0:
                struct.pack_into("f", jps, off + 16 * 4, 0.0)             # Index 16: Mono switch (0.0 = Stereo)
                struct.pack_into("f", jps, off + 20 * 4, decay_param)     # Index 20: Decay
                struct.pack_into("f", jps, off + 21 * 4, mix_param)       # Index 21: Mix
                struct.pack_into("f", jps, off + 22 * 4, 1.0)             # Index 22: Power switch (1.0 = ON)
        pl["jucePluginState"] = bytes(jps)
        return base64.b64encode(plistlib.dumps(pl)).decode("utf-8")
    except Exception:
        return state_b64


def build_module_item(
    template_name: str,
    slot_index: int,
    input_channels: int = 2,
    output_channels: int = 2,
    pid: str = "default",
) -> Optional[Dict[str, Any]]:
    """Build a complete Standalone rack item using authoritative templates."""
    tpl = STANDALONE_TEMPLATES.get(template_name)
    if not tpl:
        return None

    standalone_ns = uuid.UUID("3d3a34b7-43f9-4c61-be5b-580a4e6f880d")
    item_uuid = str(uuid.uuid5(standalone_ns, f"guitar-skills.toneprint.{pid}.slot.{slot_index}")).upper()

    return {
        "slotIndex": slot_index,
        "isBypassed": False,
        "id": item_uuid,
        "manufacturerName": tpl["manufacturerName"],
        "name": tpl["name"],
        "desc": tpl["desc"],
        "inputChannels": input_channels,
        "outputChannels": output_channels,
        "statePlistBase64": tpl["statePlistBase64"],
    }


def compile_standalone_preset_from_toneprint(
    toneprint_path: str | Path,
    pc_number: int = 1,
) -> Optional[Dict[str, Any]]:
    """Compile a single toneprint file into a Standalone preset dict."""
    with open(toneprint_path, "r", encoding="utf-8") as f:
        content = f.read()

    frontmatter, _ = parse_yaml_frontmatter(content)
    if not frontmatter:
        return None

    preset_name = frontmatter.get("preset_name") or frontmatter.get("id", "Untitled")
    amp_str = str(frontmatter.get("amp", ""))
    preset_data = frontmatter.get("preset_data", {})
    if not isinstance(preset_data, dict):
        preset_data = {}

    # Exclude archived, retired, or inactive toneprints
    status_str = str(frontmatter.get("status", "")).lower()
    if (
        status_str in ("archived", "retired", "removed", "inactive", "deprecated")
        or "archive" in status_str
        or "retire" in status_str
    ):
        return None

    # Exclude parallel / dual-amp rigs (these belong in Element)
    pid = str(frontmatter.get("id", "")).lower()
    pname_lower = preset_name.lower()
    amp_lower = amp_str.lower()
    if (
        "dual" in pid
        or "dual" in pname_lower
        or "dual" in amp_lower
        or "trinity" in pid
        or "trinity" in pname_lower
    ):
        return None

    # Exclude hardware-only toneprints (e.g. Yamaha THR hardware editor)
    if "yamaha" in amp_lower or "thr10" in amp_lower:
        return None

    items: List[Dict[str, Any]] = []
    slot_idx = 0

    # -------------------------------------------------------------
    # 1. PRE-AMP EFFECTS (Slot 0 is 1 in -> 2 out; subsequent are 2 in -> 2 out)
    # -------------------------------------------------------------
    tonex_data = preset_data.get("tonex") or preset_data.get("tonex_pedal")
    amp_platform = str(preset_data.get("amp_platform", "")).lower()

    if tonex_data and "tonex" not in amp_lower and "tonex" not in amp_platform:
        in_c = 1 if slot_idx == 0 else 2
        item = build_module_item("TONEX", slot_idx, input_channels=in_c, output_channels=2, pid=pid)
        if item:
            items.append(item)
            slot_idx += 1

    pedals = preset_data.get("pedals")
    overdrive = preset_data.get("overdrive")
    clon_data = preset_data.get("clon_minotaur") or preset_data.get("clon")
    if clon_data or (pedals and isinstance(pedals, dict) and "clon" in str(pedals).lower()) or (overdrive and "clon" in str(overdrive).lower()):
        in_c = 1 if slot_idx == 0 else 2
        item = build_module_item("NA Clon Minotaur", slot_idx, input_channels=in_c, output_channels=2, pid=pid)
        if item:
            items.append(item)
            slot_idx += 1
    elif pedals and isinstance(pedals, dict) and ("blues" in str(pedals).lower() or "barker" in str(pedals).lower()):
        in_c = 1 if slot_idx == 0 else 2
        item = build_module_item("Efektor Blues Barker", slot_idx, input_channels=in_c, output_channels=2, pid=pid)
        if item:
            items.append(item)
            slot_idx += 1

    # -------------------------------------------------------------
    # 2. AMPLIFIER & CABINET SIMULATOR
    # -------------------------------------------------------------
    amp_in_channels = 1 if slot_idx == 0 else 2
    amp_out_channels = 2

    if (
        "uad" in amp_platform
        or "dream" in amp_lower
        or "ruby" in amp_lower
        or "woodrow" in amp_lower
        or "lion" in amp_lower
        or "showtime" in amp_lower
        or "enigmatic" in amp_lower
        or "paradise" in amp_lower
    ):
        item = build_module_item("UADx Paradise Guitar Studio", slot_idx, input_channels=amp_in_channels, output_channels=amp_out_channels, pid=pid)
        if item:
            items.append(item)
            slot_idx += 1
    elif "two-rock" in amp_lower or "bloomfield" in amp_lower or "mixwave" in amp_platform:
        item = build_module_item("MixWave Two-Rock Bloomfield Drive", slot_idx, input_channels=amp_in_channels, output_channels=amp_out_channels, pid=pid)
        if item:
            items.append(item)
            slot_idx += 1
    elif "cory" in amp_lower or "wong" in amp_lower or "neural" in amp_platform:
        item = build_module_item("Archetype Cory Wong X", slot_idx, input_channels=amp_in_channels, output_channels=amp_out_channels, pid=pid)
        if item:
            items.append(item)
            slot_idx += 1
    elif "mrh810" in amp_lower:
        item = build_module_item("NA Mrh810 V2", slot_idx, input_channels=amp_in_channels, output_channels=amp_out_channels, pid=pid)
        if item:
            items.append(item)
            slot_idx += 1
    elif "jc120" in amp_lower or "jazz chorus" in amp_lower:
        item = build_module_item("NA Jazz Chorus", slot_idx, input_channels=amp_in_channels, output_channels=amp_out_channels, pid=pid)
        if item:
            items.append(item)
            slot_idx += 1
    elif "divided" in amp_lower or "div11" in amp_lower:
        item = build_module_item("NA Divided 11", slot_idx, input_channels=amp_in_channels, output_channels=amp_out_channels, pid=pid)
        if item:
            items.append(item)
            slot_idx += 1
    elif "puretone" in amp_lower:
        item = build_module_item("HK Puretone", slot_idx, input_channels=amp_in_channels, output_channels=amp_out_channels, pid=pid)
        if item:
            items.append(item)
            slot_idx += 1
    elif "tonex" in amp_lower or "tonex" in amp_platform:
        item = build_module_item("TONEX", slot_idx, input_channels=amp_in_channels, output_channels=amp_out_channels, pid=pid)
        if item:
            items.append(item)
            slot_idx += 1

    # -------------------------------------------------------------
    # 3. POST-AMP STUDIO COMPRESSOR (Stereo In -> Stereo Out)
    # -------------------------------------------------------------
    la2a_data = preset_data.get("la2a")
    if la2a_data and isinstance(la2a_data, dict):
        tpl_name = "UADx LA-2A Gray Compressor" if "gray" in str(la2a_data).lower() else "UADx LA-2A Silver Compressor"
        item = build_module_item(tpl_name, slot_idx, input_channels=2, output_channels=2, pid=pid)
        if item:
            items.append(item)
            slot_idx += 1

    # -------------------------------------------------------------
    # 4. POST-AMP MODULATION & DELAY (Stereo In -> Stereo Out)
    # -------------------------------------------------------------
    if preset_data.get("studio_d") or "studio d" in content.lower():
        item = build_module_item("UADx Studio D Chorus", slot_idx, input_channels=2, output_channels=2, pid=pid)
        if item:
            items.append(item)
            slot_idx += 1

    if preset_data.get("galaxy") or "galaxy tape echo" in content.lower():
        item = build_module_item("UADx Galaxy Tape Echo", slot_idx, input_channels=2, output_channels=2, pid=pid)
        if item:
            items.append(item)
            slot_idx += 1

    # -------------------------------------------------------------
    # 5. POST-AMP REVERB & AMBIENCE (Stereo In -> Stereo Out)
    # -------------------------------------------------------------
    hitsville_data = preset_data.get("hitsville")
    if hitsville_data or "hitsville" in content.lower():
        item = build_module_item("UADx Hitsville Reverb Chambers", slot_idx, input_channels=2, output_channels=2, pid=pid)
        if item:
            decay_val = 1.8
            mix_val = 0.12
            wet_solo_val = 0.0
            if isinstance(hitsville_data, dict):
                decay_val = to_float(hitsville_data.get("decay", 1.8), default=1.8)
                mix_val = to_float(hitsville_data.get("mix", 0.12), default=0.12)
                wet_solo_val = 1.0 if to_bool(hitsville_data.get("wet_solo", False)) else 0.0
            item["statePlistBase64"] = patch_hitsville_plist(
                item["statePlistBase64"],
                decay_sec=decay_val,
                mix_val=mix_val,
                wet_solo_val=wet_solo_val,
            )
            items.append(item)
            slot_idx += 1
    elif preset_data.get("valhalla") or "valhalla" in content.lower():
        item = build_module_item("ValhallaSupermassive", slot_idx, input_channels=2, output_channels=2, pid=pid)
        if item:
            items.append(item)
            slot_idx += 1

    if not items:
        return None

    # Ensure Slot 0 always starts with mono input
    items[0]["inputChannels"] = 1

    # Build Standalone Preset JSON using deterministic UUIDv5
    standalone_ns = uuid.UUID("3d3a34b7-43f9-4c61-be5b-580a4e6f880d")
    preset_uuid = str(uuid.uuid5(standalone_ns, f"guitar-skills.toneprint.{pid}")).upper()
    now_iso = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    clean_name = f"Toneprint — {preset_name}"

    preset_obj = {
        "id": preset_uuid,
        "parameterMappings": [],
        "name": clean_name,
        "pcNumber": pc_number,
        "createdAt": now_iso,
        "items": items,
        "inputMode": 0,
    }

    return preset_obj


def compile_all_standalone_presets(
    tones_dir: str | Path,
    output_dir: str | Path = STANDALONE_PRESETS_DIR,
    filter_substr: Optional[str] = None,
) -> int:
    """Scan all toneprints and write compiled Standalone presets to output_dir."""
    global STANDALONE_TEMPLATES
    tones_path = Path(tones_dir)
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    # 1. Update templates if OneOfEverything or other templates exist on disk
    existing_presets = list(out_path.glob("*.json"))
    for ep in existing_presets:
        try:
            with open(ep, "r", encoding="utf-8") as f:
                data = json.load(f)
            pname = data.get("name", "")
            if "OneOfEverything" in pname or "Template" in pname:
                for it in data.get("items", []):
                    name = it.get("name")
                    if name:
                        STANDALONE_TEMPLATES[name] = {
                            "manufacturerName": it["manufacturerName"],
                            "name": it["name"],
                            "desc": it["desc"],
                            "statePlistBase64": it["statePlistBase64"],
                        }
        except Exception:
            pass

    # Save any updated templates to cache
    if STANDALONE_TEMPLATES:
        try:
            TEMPLATES_FILE.parent.mkdir(parents=True, exist_ok=True)
            with open(TEMPLATES_FILE, "w", encoding="utf-8") as f:
                json.dump(STANDALONE_TEMPLATES, f, indent=2)
        except Exception:
            pass

    # 2. Clean up old toneprint files on full recompile (preserving user manual presets)
    if not filter_substr:
        for ep in existing_presets:
            try:
                with open(ep, "r", encoding="utf-8") as f:
                    data = json.load(f)
                name = data.get("name", "")
                if name.startswith("Toneprint — ") or name.startswith("Toneprint - "):
                    ep.unlink(missing_ok=True)
            except Exception:
                pass

    # 3. Compile all active serial toneprints
    md_files = sorted(list(tones_path.glob("**/*.md")))
    compiled_count = 0
    pc_counter = 2  # Start at 2 so PC #1 is reserved for user's baseline preset

    for mf in md_files:
        if (
            "INDEX.md" in mf.name
            or "universal-template" in mf.name
            or "session" in mf.name
            or "guidelines" in mf.name.lower()
            or "eqprints" in str(mf).lower()
            or "utilities" in str(mf).lower()
        ):
            continue

        if filter_substr:
            f_norm = filter_substr.lower()
            f_hyphen = f_norm.replace(" ", "-")
            if f_norm not in str(mf).lower() and f_hyphen not in str(mf).lower():
                continue

        preset = compile_standalone_preset_from_toneprint(
            mf,
            pc_number=pc_counter,
        )

        if preset:
            file_dest = out_path / f"{preset['id']}.json"
            try:
                with open(file_dest, "w", encoding="utf-8") as f:
                    json.dump(preset, f, indent=2)
                compiled_count += 1
                pc_counter += 1
                print(f"-> Compiled Standalone Preset (PC #{preset['pcNumber']}): '{preset['name']}' ({len(preset['items'])} modules)")
            except (PermissionError, OSError) as e:
                mirror_dir = WORKSPACE_ROOT / "tones" / "presets" / "standalone"
                mirror_dir.mkdir(parents=True, exist_ok=True)
                with open(mirror_dir / f"{preset['id']}.json", "w", encoding="utf-8") as f:
                    json.dump(preset, f, indent=2)
                compiled_count += 1
                pc_counter += 1
                print(f"-> Saved repo copy (PC #{preset['pcNumber']}): '{preset['name']}' ({len(preset['items'])} modules) (live write skipped: {e})")

    return compiled_count
