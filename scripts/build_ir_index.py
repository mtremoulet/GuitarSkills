import os
import re

def build_ir_index():
    base_dir = "/Users/miketremoulet/Music/Logic Pro Library.bundle/Impulse Responses"
    if not os.path.exists(base_dir):
        print(f"Error: Path {base_dir} does not exist.")
        return
        
    sdir_files = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.lower().endswith(".sdir"):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, base_dir)
                sdir_files.append((rel_path, full_path))
                
    sdir_files.sort()
    
    # Categorize by parent directories
    categories = {}
    for rel_path, full_path in sdir_files:
        parts = rel_path.split("/")
        if len(parts) >= 2:
            main_cat = parts[0]
            sub_cat = parts[1] if len(parts) > 2 else "General"
            cat_name = f"{main_cat} / {sub_cat}"
        else:
            cat_name = "Other"
            
        if cat_name not in categories:
            categories[cat_name] = []
            
        # Try to parse decay time from filename (e.g., 0.6s, 14.8s, 09.0s, etc.)
        decay_match = re.search(r"([0-9.]+)\s*s", parts[-1], re.IGNORECASE)
        decay = decay_match.group(1) + " s" if decay_match else "N/A"
        
        # Clean up the name for display
        display_name = parts[-1].replace(".SDIR", "").replace(".sdir", "")
        
        categories[cat_name].append({
            "name": display_name,
            "filename": parts[-1],
            "decay": decay,
            "rel_path": rel_path,
            "full_path": full_path
        })
        
    # Generate Markdown
    md_content = []
    md_content.append("# Logic Pro Space Designer — Built-in Impulse Responses Index\n")
    md_content.append("This is an authoritative, categorized index of all built-in Space Designer impulse response (`.SDIR`) files available in the Logic Pro Library bundle.\n")
    
    # Table of Contents
    md_content.append("## Categories\n")
    for cat in sorted(categories.keys()):
        count = len(categories[cat])
        anchor = cat.lower().replace(" ", "-").replace("/", "").replace("--", "-")
        md_content.append(f"- [{cat}](#{anchor}) ({count} IRs)")
    md_content.append("\n---\n")
    
    # Detail sections
    for cat in sorted(categories.keys()):
        md_content.append(f"## {cat}\n")
        md_content.append("| IR Name | Est. Decay | Filename | Relative Path |")
        md_content.append("| :--- | :--- | :--- | :--- |")
        for ir in categories[cat]:
            md_content.append(f"| **{ir['name']}** | {ir['decay']} | `{ir['filename']}` | `{ir['rel_path']}` |")
        md_content.append("\n")
        
    output_path = "/Users/miketremoulet/claude-projects/GuitarSkills/references/space-designer-irs.md"
    with open(output_path, "w") as f:
        f.write("\n".join(md_content))
    print(f"Generated IR index at: {output_path}")

if __name__ == "__main__":
    build_ir_index()
