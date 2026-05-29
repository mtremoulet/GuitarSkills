#!/usr/bin/env python3
import os
import re

tones_dir = "/Users/miketremoulet/claude-projects/GuitarSkills/tones"

def parse_dynamic_uad_toneprint(filepath):
    with open(filepath, "r") as f:
        content = f.read()
        
    # Check frontmatter
    fm_match = re.search(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not fm_match:
        return None
        
    fm = fm_match.group(1)
    
    # Check amp model in frontmatter
    amp_match = re.search(r"^amp:\s*[\"|\']?(.*?)[\"|\']?$", fm, re.MULTILINE)
    if not amp_match:
        return None
    amp_str = amp_match.group(1).strip()
    
    # Identify target amp type
    amp_type = None
    amp_index = None
    cab_index = 2 # default Boutique D65
    
    if "Dream" in amp_str:
        amp_type = "dream"
        amp_index = 0
        cab_index = 29 # Deluxe Reverb
    elif "Enigmatic" in amp_str:
        amp_type = "enigmatic"
        amp_index = 1
        cab_index = 2 # Boutique D65
    elif "Woodrow" in amp_str:
        amp_type = "woodrow"
        amp_index = 2
        cab_index = 2 # Tweed 1x12
    elif "Ruby" in amp_str:
        amp_type = "ruby"
        amp_index = 3
        cab_index = 1 # AC30 Blue
    elif "Showtime" in amp_str:
        amp_type = "showtime"
        amp_index = 4
        cab_index = 29
    elif "Lion" in amp_str:
        amp_type = "lion"
        amp_index = 2 # Wait, Lion is index 2, Woodrow is index 5
        cab_index = 2
        
    # Correcting Woodrow and Lion indices based on verified mapping
    if amp_type == "woodrow":
        amp_index = 5
    elif amp_type == "lion":
        amp_index = 2
        
    if amp_type is None:
        return None
        
    controls = {}
    
    # 1. Parse standard controls using regexes on tables
    # Helper to find a numeric setting (e.g. **5.5** or **75%**)
    def find_numeric(param_names):
        for name in param_names:
            # Match standard numbers like **5.5** or **7.0**
            match = re.search(r"\|\s*" + re.escape(name) + r"\s*\|\s*\*\*([0-9.]+)\*\*", content, re.IGNORECASE)
            if match:
                return float(match.group(1))
            # Match percentage like **75%** or **35%**
            pct_match = re.search(r"\|\s*" + re.escape(name) + r"\s*\|\s*\*\*([0-9]+)%\*\*", content, re.IGNORECASE)
            if pct_match:
                return float(pct_match.group(1)) / 100.0
        return None
        
    # Helper to find a boolean switch (e.g. **ON**, **OFF**, **Normal**, **Bright**)
    def find_boolean(param_names):
        for name in param_names:
            match = re.search(r"\|\s*" + re.escape(name) + r"\s*\|\s*\*\*([A-Za-z/ ]+)\*\*", content, re.IGNORECASE)
            if match:
                val = match.group(1).strip().upper()
                if val in ["ON", "ACTIVE", "BRIGHT", "YES"]:
                    return True
                if val in ["OFF", "NORMAL", "BYPASSED", "NO"]:
                    return False
        return None

    # Parse common knobs
    vol = find_numeric(["Volume (Gain)", "Volume", "Volume (Inst)", "inst_volume"])
    treble = find_numeric(["Treble", "Top Boost Treble", "Tone"]) # Woodrow uses Tone knob
    mid = find_numeric(["Middle", "Mids"])
    bass = find_numeric(["Bass", "Top Boost Bass"])
    presence = find_numeric(["Presence"])
    master = find_numeric(["Master (labeled 6.5)", "Master", "Master volume"])
    tone_cut = find_numeric(["Tone Cut"])
    
    # Parse switches
    bright = find_boolean(["Bright Switch", "Bright / Normal", "Bright"])
    boost = find_boolean(["Boost Button", "Boost Switch", "Boost (Stock)", "Boost"])
    
    # Inject mapped parameters based on active amp module
    if amp_type == "dream":
        if vol is not None: controls["dream_volume"] = vol
        if treble is not None: controls["dream_treble"] = treble
        if bass is not None: controls["dream_bass"] = bass
        if bright is not None: controls["dream_bright"] = bright
        if boost is not None: controls["dream_boost_enable"] = boost
        # Reverb defaults
        controls["dream_reverb_enable"] = True
        controls["dream_reverb"] = 2.5
    elif amp_type == "enigmatic":
        if vol is not None: controls["enigmatic_volume"] = vol
        if treble is not None: controls["enigmatic_treble"] = treble
        if mid is not None: controls["enigmatic_middle"] = mid
        if bass is not None: controls["enigmatic_bass"] = bass
        if presence is not None: controls["enigmatic_presence"] = presence
        if master is not None: controls["enigmatic_master_gain"] = master
        if bright is not None: controls["enigmatic_bright_enable"] = bright
        if boost is not None: controls["enigmatic_boost_enable"] = boost
        
        # Tone stack defaults based on Suede/Skyline/Jazz
        controls["enigmatic_model"] = 0        # Suede
        controls["enigmatic_channel"] = 1      # NOR input
        controls["enigmatic_tone_stack_type"] = 0 # Skyline
        controls["enigmatic_tone_stack_eq"] = 0   # Jazz
        controls["enigmatic_overdrive_enable"] = False
    elif amp_type == "ruby":
        if vol is not None: controls["ruby_volume"] = vol
        if treble is not None: controls["ruby_treble"] = treble
        if bass is not None: controls["ruby_bass"] = bass
        if tone_cut is not None: controls["ruby_tone_cut"] = tone_cut
        if boost is not None: controls["ruby_boost_enable"] = boost
        
        # Brilliant channel defaults
        controls["ruby_channel"] = 2
        controls["ruby_cut"] = 5.0
    elif amp_type == "woodrow":
        if vol is not None: controls["woodrow_inst_volume"] = vol
        if treble is not None: controls["woodrow_tone"] = treble # Woodrow tone knob
        if boost is not None: controls["woodrow_boost_enable"] = boost
        controls["woodrow_mic_volume"] = 2.0  # Default mic channel blend
    elif amp_type == "showtime":
        if vol is not None: controls["showtime_volume"] = vol
        if treble is not None: controls["showtime_treble"] = treble
        if mid is not None: controls["showtime_middle"] = mid
        if bass is not None: controls["showtime_bass"] = bass
        if bright is not None: controls["showtime_bright"] = bright
        
    return {
        "title": amp_str,
        "amp_type": amp_type,
        "amp_index": amp_index,
        "cab_index": cab_index,
        "controls": controls
    }

# Run the test on Woodrow Sweet Spot SC
result = parse_dynamic_uad_toneprint("/Users/miketremoulet/claude-projects/GuitarSkills/tones/single-coils/woodrow-sweet-spot.md")
print("Parsed Dynamic Woodrow Settings:")
if result:
    print(f"  Title: {result['title']}")
    print(f"  Amp Index: {result['amp_index']}")
    print(f"  Controls: {result['controls']}")
else:
    print("  Failed to parse!")
