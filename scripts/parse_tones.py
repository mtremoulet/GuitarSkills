#!/usr/bin/env python3
import os
import re

tones_dir = "/Users/miketremoulet/claude-projects/GuitarSkills/tones"
all_tones = []

for root, dirs, files in os.walk(tones_dir):
    for f in files:
        if not f.endswith(".md") or f == "INDEX.md":
            continue
        path = os.path.join(root, f)
        with open(path, "r") as file:
            content = file.read()
        
        # Extract title (H1 header)
        title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else f
        
        # Extract YAML frontmatter
        fm_match = re.search(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
        amp = "Unknown"
        pickup = "Unknown"
        guitar = "Unknown"
        status = "Unknown"
        
        if fm_match:
            fm = fm_match.group(1)
            amp_match = re.search(r"^amp:\s*[\"|\']?(.*?)[\"|\']?$", fm, re.MULTILINE)
            if amp_match:
                amp = amp_match.group(1).strip()
            
            pick_match = re.search(r"^pickup_type:\s*(.*?)$", fm, re.MULTILINE)
            if pick_match:
                pickup = pick_match.group(1).strip()
            
            gui_match = re.search(r"^guitar:\s*[\"|\']?(.*?)[\"|\']?$", fm, re.MULTILINE)
            if gui_match:
                guitar = gui_match.group(1).strip()
            
            st_match = re.search(r"^status:\s*(.*?)$", fm, re.MULTILINE)
            if st_match:
                status = st_match.group(1).strip()
            
        # Check generated status
        generated = "❌ No"
        
        # Cross reference with active compilers
        if "cory-wong" in f:
            generated = "✅ Yes (Neural DSP)"
        elif "paradise-enigmatic" in f or "ruby-paradise" in f:
            generated = "✅ Yes (UAD Paradise)"
        elif "dream-65" in f:
            generated = "✅ Yes (UAD Paradise)"
        elif "ruby-63" in f or "ruby-les-paul" in f:
            generated = "✅ Yes (UAD Paradise)"
        elif "woodrow-sweet-spot" in f:
            generated = "✅ Yes (UAD Paradise)"
        elif "jazz-clean-intimate" in f:
            generated = "✅ Yes (UAD Paradise)"
            
        all_tones.append({
            "title": title,
            "amp": amp,
            "guitar": guitar,
            "pickup": pickup,
            "status": status,
            "generated": generated
        })

print("| Title | Amp Model | Pickup | Preset Generated? |")
print("| :--- | :--- | :--- | :--- |")
for t in sorted(all_tones, key=lambda x: x["title"]):
    print(f"| {t['title']} | {t['amp']} | {t['pickup']} | {t['generated']} |")
