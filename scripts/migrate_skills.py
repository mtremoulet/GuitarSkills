#!/usr/bin/env python3
import os
import re
from pathlib import Path

def main():
    project_root = Path(__file__).resolve().parent.parent
    source_dir = project_root / ".claude" / "commands"
    dest_dir = project_root / ".agents" / "skills"

    if not source_dir.exists():
        print(f"Source directory {source_dir} does not exist. Nothing to migrate.")
        return

    print(f"Scanning {source_dir} for skills...")
    md_files = list(source_dir.glob("*.md"))
    
    if not md_files:
        print("No markdown skill files found.")
        return

    dest_dir.mkdir(parents=True, exist_ok=True)
    
    migrated_count = 0
    for src_file in md_files:
        try:
            content = src_file.read_text(encoding="utf-8")
            
            # Extract name from frontmatter
            name_match = re.search(r"^name:\s*([^\s\n]+)", content, re.MULTILINE)
            if name_match:
                skill_name = name_match.group(1).strip().strip('"').strip("'")
            else:
                skill_name = src_file.stem
                
            skill_folder = dest_dir / skill_name
            skill_folder.mkdir(parents=True, exist_ok=True)
            
            dest_file = skill_folder / "SKILL.md"
            
            # Write to SKILL.md
            dest_file.write_text(content, encoding="utf-8")
            print(f"Migrated: {src_file.name} -> .agents/skills/{skill_name}/SKILL.md")
            migrated_count += 1
        except Exception as e:
            print(f"Failed to migrate {src_file.name}: {e}")

    print(f"\nMigration completed! Successfully migrated {migrated_count} skills to .agents/skills/")

if __name__ == "__main__":
    main()
