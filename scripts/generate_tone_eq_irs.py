#!/usr/bin/env python3
"""
Generate IR (Impulse Response) WAV files from Logic Pro Channel EQ settings in GuitarSkills toneprints.

This script parses all toneprints in GuitarSkills `tones/` (humbuckers, p-90s, single-coils),
extracts their `logic_eq` settings, and computes the exact linear time-invariant (LTI)
impulse response using Robert Bristow-Johnson (RBJ) Audio EQ Cookbook biquad filters.

Output files can be saved to GuitarSkills or SPICEyNAM as standard 24-bit / 48 kHz WAV files,
ready to load directly into NAM's IR slot or any AU IR loader plugin in Standalone.
"""

from __future__ import annotations

import math
import os
import re
import struct
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


def parse_yaml_frontmatter(content: str) -> Tuple[Dict[str, Any], str]:
    """Parse YAML frontmatter and body from Markdown content."""
    match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return {}, content

    yaml_text = match.group(1)
    body = content[match.end():]

    lines = yaml_text.splitlines()
    parsed_lines = []
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        indent = len(line) - len(line.lstrip())
        if ":" in line:
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip()
            if val.startswith("{") and val.endswith("}"):
                inner_dict = {}
                pairs = val[1:-1].split(",")
                for pair in pairs:
                    if ":" in pair:
                        pk, _, pv = pair.partition(":")
                        pk = pk.strip()
                        pv = pv.strip()
                        if pv.startswith('"') and pv.endswith('"'):
                            pv = pv[1:-1]
                        elif pv.startswith("'") and pv.endswith("'"):
                            pv = pv[1:-1]
                        if pv == "":
                            pv = None
                        elif pv.lower() == "true":
                            pv = True
                        elif pv.lower() == "false":
                            pv = False
                        else:
                            try:
                                if "." in pv:
                                    pv = float(pv)
                                else:
                                    pv = int(pv)
                            except ValueError:
                                pass
                        inner_dict[pk] = pv
                val = inner_dict
            else:
                if val.startswith('"') and val.endswith('"'):
                    val = val[1:-1]
                elif val.startswith("'") and val.endswith("'"):
                    val = val[1:-1]

                if val == "":
                    val = None
                elif isinstance(val, str) and val.lower() == "true":
                    val = True
                elif isinstance(val, str) and val.lower() == "false":
                    val = False
                elif isinstance(val, str):
                    try:
                        if "." in val:
                            val = float(val)
                        else:
                            val = int(val)
                    except ValueError:
                        pass
            parsed_lines.append((indent, key, val))

    def build_tree(start_idx: int, parent_indent: int) -> Tuple[Dict[str, Any], int]:
        result = {}
        idx = start_idx
        while idx < len(parsed_lines):
            indent, key, val = parsed_lines[idx]
            if indent <= parent_indent:
                break

            next_idx = idx + 1
            has_children = False
            if next_idx < len(parsed_lines):
                next_indent, _, _ = parsed_lines[next_idx]
                if next_indent > indent:
                    has_children = True

            if has_children:
                child_dict, next_idx = build_tree(next_idx, indent)
                result[key] = child_dict
                idx = next_idx
            else:
                result[key] = val
                idx += 1
        return result, idx

    parsed_dict, _ = build_tree(0, -1)
    return parsed_dict, body


class BiquadFilter:
    """Standard 2nd-order IIR Biquad Filter (Direct Form II Transposed)."""

    def __init__(self, b0: float, b1: float, b2: float, a0: float, a1: float, a2: float):
        self.b0 = b0 / a0
        self.b1 = b1 / a0
        self.b2 = b2 / a0
        self.a1 = a1 / a0
        self.a2 = a2 / a0
        self.s1 = 0.0
        self.s2 = 0.0

    def reset(self):
        self.s1 = 0.0
        self.s2 = 0.0

    def process_sample(self, x: float) -> float:
        y = self.b0 * x + self.s1
        self.s1 = self.b1 * x - self.a1 * y + self.s2
        self.s2 = self.b2 * x - self.a2 * y
        return y

    def process_buffer(self, buffer: List[float]) -> List[float]:
        self.reset()
        output = [0.0] * len(buffer)
        for i, x in enumerate(buffer):
            output[i] = self.process_sample(x)
        return output


def make_peaking_eq(sample_rate: float, freq: float, gain_db: float, q: float) -> BiquadFilter:
    """RBJ Peaking EQ filter."""
    if abs(gain_db) < 1e-4:
        return BiquadFilter(1.0, 0.0, 0.0, 1.0, 0.0, 0.0)
    w0 = 2.0 * math.pi * freq / sample_rate
    alpha = math.sin(w0) / (2.0 * max(q, 0.01))
    A = 10.0 ** (gain_db / 40.0)

    b0 = 1.0 + alpha * A
    b1 = -2.0 * math.cos(w0)
    b2 = 1.0 - alpha * A
    a0 = 1.0 + alpha / A
    a1 = -2.0 * math.cos(w0)
    a2 = 1.0 - alpha / A
    return BiquadFilter(b0, b1, b2, a0, a1, a2)


def make_low_shelf(sample_rate: float, freq: float, gain_db: float, q: float = 0.7071) -> BiquadFilter:
    """RBJ Low Shelf filter."""
    if abs(gain_db) < 1e-4:
        return BiquadFilter(1.0, 0.0, 0.0, 1.0, 0.0, 0.0)
    w0 = 2.0 * math.pi * freq / sample_rate
    A = 10.0 ** (gain_db / 40.0)
    alpha = math.sin(w0) / (2.0 * max(q, 0.01))
    cos_w0 = math.cos(w0)
    two_sqrt_A_alpha = 2.0 * math.sqrt(A) * alpha

    b0 = A * ((A + 1.0) - (A - 1.0) * cos_w0 + two_sqrt_A_alpha)
    b1 = 2.0 * A * ((A - 1.0) - (A + 1.0) * cos_w0)
    b2 = A * ((A + 1.0) - (A - 1.0) * cos_w0 - two_sqrt_A_alpha)
    a0 = (A + 1.0) + (A - 1.0) * cos_w0 + two_sqrt_A_alpha
    a1 = -2.0 * ((A - 1.0) + (A + 1.0) * cos_w0)
    a2 = (A + 1.0) + (A - 1.0) * cos_w0 - two_sqrt_A_alpha
    return BiquadFilter(b0, b1, b2, a0, a1, a2)


def make_high_shelf(sample_rate: float, freq: float, gain_db: float, q: float = 0.7071) -> BiquadFilter:
    """RBJ High Shelf filter."""
    if abs(gain_db) < 1e-4:
        return BiquadFilter(1.0, 0.0, 0.0, 1.0, 0.0, 0.0)
    w0 = 2.0 * math.pi * freq / sample_rate
    A = 10.0 ** (gain_db / 40.0)
    alpha = math.sin(w0) / (2.0 * max(q, 0.01))
    cos_w0 = math.cos(w0)
    two_sqrt_A_alpha = 2.0 * math.sqrt(A) * alpha

    b0 = A * ((A + 1.0) + (A - 1.0) * cos_w0 + two_sqrt_A_alpha)
    b1 = -2.0 * A * ((A - 1.0) + (A + 1.0) * cos_w0)
    b2 = A * ((A + 1.0) - (A - 1.0) * cos_w0 - two_sqrt_A_alpha)
    a0 = (A + 1.0) - (A - 1.0) * cos_w0 + two_sqrt_A_alpha
    a1 = 2.0 * ((A - 1.0) - (A + 1.0) * cos_w0)
    a2 = (A + 1.0) - (A - 1.0) * cos_w0 - two_sqrt_A_alpha
    return BiquadFilter(b0, b1, b2, a0, a1, a2)


def make_high_pass_stages(sample_rate: float, freq: float, slope_db_oct: float) -> List[BiquadFilter]:
    """Cascaded Butterworth High Pass Filters matching Logic's dB/oct slope."""
    w0 = 2.0 * math.pi * freq / sample_rate
    cos_w0 = math.cos(w0)

    slope = int(round(slope_db_oct)) if slope_db_oct else 12
    if slope <= 6:
        k = math.tan(w0 / 2.0)
        b0 = 1.0 / (1.0 + k)
        b1 = -1.0 / (1.0 + k)
        b2 = 0.0
        a0 = 1.0
        a1 = (k - 1.0) / (1.0 + k)
        a2 = 0.0
        return [BiquadFilter(b0, b1, b2, a0, a1, a2)]

    stages = []
    num_biquads = max(1, slope // 12)
    order = num_biquads * 2
    for k in range(num_biquads):
        angle = math.pi * (2 * k + 1) / (2 * order)
        q = 1.0 / (2.0 * math.cos(angle))
        alpha = math.sin(w0) / (2.0 * q)
        b0 = (1.0 + cos_w0) / 2.0
        b1 = -(1.0 + cos_w0)
        b2 = (1.0 + cos_w0) / 2.0
        a0 = 1.0 + alpha
        a1 = -2.0 * cos_w0
        a2 = 1.0 - alpha
        stages.append(BiquadFilter(b0, b1, b2, a0, a1, a2))
    return stages


def make_low_pass_stages(sample_rate: float, freq: float, slope_db_oct: float) -> List[BiquadFilter]:
    """Cascaded Butterworth Low Pass Filters matching Logic's dB/oct slope."""
    w0 = 2.0 * math.pi * freq / sample_rate
    cos_w0 = math.cos(w0)

    slope = int(round(slope_db_oct)) if slope_db_oct else 12
    if slope <= 6:
        k = math.tan(w0 / 2.0)
        b0 = k / (1.0 + k)
        b1 = k / (1.0 + k)
        b2 = 0.0
        a0 = 1.0
        a1 = (k - 1.0) / (1.0 + k)
        a2 = 0.0
        return [BiquadFilter(b0, b1, b2, a0, a1, a2)]

    stages = []
    num_biquads = max(1, slope // 12)
    order = num_biquads * 2
    for k in range(num_biquads):
        angle = math.pi * (2 * k + 1) / (2 * order)
        q = 1.0 / (2.0 * math.cos(angle))
        alpha = math.sin(w0) / (2.0 * q)
        b0 = (1.0 - cos_w0) / 2.0
        b1 = 1.0 - cos_w0
        b2 = (1.0 - cos_w0) / 2.0
        a0 = 1.0 + alpha
        a1 = -2.0 * cos_w0
        a2 = 1.0 - alpha
        stages.append(BiquadFilter(b0, b1, b2, a0, a1, a2))
    return stages


def build_channel_eq_filters(logic_eq_dict: Dict[str, Any], sample_rate: float = 48000.0) -> List[BiquadFilter]:
    """Construct the list of cascaded biquad filters from a logic_eq dictionary."""
    filters = []

    for key, params in sorted(logic_eq_dict.items()):
        if not isinstance(params, dict):
            continue

        match = re.search(r"\d+", str(key))
        if not match:
            continue
        band_num = int(match.group(0))

        is_on = params.get("on", True)
        if is_on is False or is_on == 0 or str(is_on).lower() == "false":
            continue

        freq = float(params.get("freq", 0.0))
        if freq <= 0.0 or freq >= sample_rate / 2.0:
            continue

        if band_num == 1:
            slope = float(params.get("slope", 12.0))
            filters.extend(make_high_pass_stages(sample_rate, freq, slope))

        elif band_num == 8:
            slope = float(params.get("slope", 12.0))
            filters.extend(make_low_pass_stages(sample_rate, freq, slope))

        elif band_num == 2:
            gain = float(params.get("gain", 0.0))
            q = float(params.get("q", 0.7071))
            if abs(gain) > 1e-4:
                filters.append(make_low_shelf(sample_rate, freq, gain, q))

        elif band_num == 7:
            gain = float(params.get("gain", 0.0))
            q = float(params.get("q", 0.7071))
            if abs(gain) > 1e-4:
                filters.append(make_high_shelf(sample_rate, freq, gain, q))

        else:
            gain = float(params.get("gain", 0.0))
            q = float(params.get("q", 1.0))
            if abs(gain) > 1e-4:
                filters.append(make_peaking_eq(sample_rate, freq, gain, q))

    return filters


def synthesize_ir(filters: List[BiquadFilter], length_samples: int = 4096, sample_rate: float = 48000.0) -> List[float]:
    """Synthesize the impulse response from a cascade of biquads."""
    impulse = [0.0] * length_samples
    impulse[0] = 1.0

    current = impulse
    for f in filters:
        current = f.process_buffer(current)

    fade_len = min(64, length_samples // 4)
    for i in range(fade_len):
        idx = length_samples - 1 - i
        window = 0.5 * (1.0 - math.cos(math.pi * i / fade_len))
        current[idx] *= window

    return current


def write_wav_24bit(filepath: str | Path, samples: List[float], sample_rate: int = 48000):
    """Write 24-bit PCM mono WAV file."""
    filepath = Path(filepath)
    filepath.parent.mkdir(parents=True, exist_ok=True)

    num_samples = len(samples)
    byte_rate = sample_rate * 3
    block_align = 3
    data_size = num_samples * 3

    riff_header = b"RIFF" + struct.pack("<I", 36 + data_size) + b"WAVE"
    fmt_chunk = b"fmt " + struct.pack("<IHHIIHH", 16, 1, 1, sample_rate, byte_rate, block_align, 24)

    pcm_bytes = bytearray()
    for s in samples:
        clamped = max(-1.0, min(1.0, s))
        val = int(clamped * 8388607.0)
        if val < 0:
            val += 16777216
        pcm_bytes.append(val & 0xFF)
        pcm_bytes.append((val >> 8) & 0xFF)
        pcm_bytes.append((val >> 16) & 0xFF)

    data_chunk = b"data" + struct.pack("<I", data_size) + bytes(pcm_bytes)

    with open(filepath, "wb") as f:
        f.write(riff_header + fmt_chunk + data_chunk)


def process_toneprints(tones_dir: str | Path, output_dir: str | Path) -> List[Dict[str, Any]]:
    """Scan toneprints and generate IR wav files for all presets with logic_eq."""
    tones_dir = Path(tones_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    generated = []

    for root, _, files in os.walk(tones_dir):
        if "drafts" in root or "eqprints" in root:
            continue

        for f in sorted(files):
            if not f.endswith(".md") or f == "INDEX.md":
                continue

            md_path = Path(root) / f
            with open(md_path, "r", encoding="utf-8") as file:
                content = file.read()

            fm, _ = parse_yaml_frontmatter(content)
            if not fm:
                continue

            preset_data = fm.get("preset_data", {})
            if not isinstance(preset_data, dict):
                continue

            logic_eq = preset_data.get("logic_eq")
            if not logic_eq or not isinstance(logic_eq, dict):
                continue

            preset_id = fm.get("id") or md_path.stem
            preset_name = fm.get("preset_name") or fm.get("title") or preset_id
            amp = fm.get("amp", "Unknown")
            guitar = fm.get("guitar", "Unknown")
            pickup = fm.get("pickup_type", "Unknown")

            filters = build_channel_eq_filters(logic_eq, sample_rate=48000.0)
            if not filters:
                continue

            ir_samples = synthesize_ir(filters, length_samples=4096, sample_rate=48000.0)

            peak = max(abs(s) for s in ir_samples)
            peak_db = 20.0 * math.log10(peak) if peak > 0 else -120.0

            ir_filename_24 = f"{preset_id}-eq.wav"
            out_path_24 = output_dir / ir_filename_24

            scale = 1.0
            if peak > 0.999:
                scale = 0.999 / peak
            scaled_samples = [s * scale for s in ir_samples]
            write_wav_24bit(out_path_24, scaled_samples, sample_rate=48000)

            band_summaries = []
            for b_name, b_val in sorted(logic_eq.items()):
                if isinstance(b_val, dict) and b_val.get("on", True):
                    freq = b_val.get("freq")
                    if "slope" in b_val:
                        band_summaries.append(f"{b_name.upper()}: {freq}Hz ({b_val.get('slope')}dB/oct)")
                    elif "gain" in b_val:
                        gain = b_val.get("gain", 0.0)
                        q = b_val.get("q", 1.0)
                        band_summaries.append(f"{b_name.upper()}: {freq}Hz ({gain:+.1f}dB, Q={q})")

            info = {
                "id": preset_id,
                "name": preset_name,
                "amp": amp,
                "guitar": guitar,
                "pickup": pickup,
                "filename": ir_filename_24,
                "path": str(out_path_24),
                "peak_db": peak_db,
                "bands": band_summaries,
                "filters_count": len(filters),
            }
            generated.append(info)
            print(f"Generated: {ir_filename_24} ({len(filters)} filters, peak {peak_db:.2f} dBFS)")

    manifest_path = output_dir / "README.md"
    with open(manifest_path, "w", encoding="utf-8") as mf:
        mf.write("# Toneprint Channel EQ Impulse Responses (IRs)\n\n")
        mf.write("These high-resolution **24-bit / 48 kHz mono WAV IR files** capture the exact linear frequency response ")
        mf.write("of Logic Pro's Channel EQ curves configured in GuitarSkills toneprints.\n\n")
        mf.write("## How to Use in Standalone:\n")
        mf.write("1. **Inside Neural Amp Modeler (NAM)**: Load the corresponding `.wav` directly into NAM's built-in **IR slot** alongside your amp profile.\n")
        mf.write("2. **Dedicated AU IR Loader**: Place a lightweight AU IR loader (e.g. NadIR, Space Designer AU, Pulse, etc.) immediately after your amp plugin in Standalone.\n\n")
        mf.write("## Generated IR Library:\n\n")
        mf.write("| Preset / Toneprint | Target Amp | Pickup / Guitar | IR File | Active EQ Bands |\n")
        mf.write("| :--- | :--- | :--- | :--- | :--- |\n")
        for g in generated:
            bands_str = "<br>".join(g["bands"])
            mf.write(f"| **{g['name']}**<br>`{g['id']}` | {g['amp']} | {g['pickup']}<br>*{g['guitar']}* | `{g['filename']}` | {bands_str} |\n")

    return generated


if __name__ == "__main__":
    tones_dir = Path("/Users/miketremoulet/claude-projects/GuitarSkills/tones")
    output_dir = Path("/Users/miketremoulet/claude-projects/SPICEyNAM/tones_irs")

    if len(sys.argv) > 1:
        tones_dir = Path(sys.argv[1])
    if len(sys.argv) > 2:
        output_dir = Path(sys.argv[2])

    print("=" * 60)
    print("GuitarSkills Channel EQ IR Generator")
    print(f"Tones directory: {tones_dir}")
    print(f"Output IR directory: {output_dir}")
    print("=" * 60)

    results = process_toneprints(tones_dir, output_dir)
    print("=" * 60)
    print(f"Successfully generated {len(results)} IR WAV files in '{output_dir}'.")
    print("=" * 60)
