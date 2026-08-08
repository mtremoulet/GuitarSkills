"""Base utilities and parsing helpers for the GuitarSkills preset compiler package."""

from __future__ import annotations

import re
from typing import Dict, Any, Tuple, List
from scripts.utils.param_types import (
    find_numeric_param as find_numeric_parameter,
    find_boolean_param as find_boolean_parameter,
    to_float,
    to_bool,
    to_db,
    to_freq,
)

__all__ = [
    "parse_yaml_frontmatter",
    "extract_markdown_section",
    "replace_binary_parameter",
    "find_numeric_parameter",
    "find_boolean_parameter",
    "to_float",
    "to_bool",
    "to_db",
    "to_freq",
]


def replace_binary_parameter(data: bytes, param_name: str, new_val_str: str) -> bytes:
    """Replace a named parameter value in a binary chunk (used for Neural DSP binary params)."""
    search_bytes = param_name.encode("utf-8") + b"\x00\x01"
    idx = data.find(search_bytes)
    if idx == -1:
        return data

    length_byte_idx = idx + len(search_bytes)
    old_length = data[length_byte_idx]

    replace_start = length_byte_idx
    replace_end = length_byte_idx + 1 + old_length

    new_val_bytes = new_val_str.encode("utf-8")
    new_length = len(new_val_bytes) + 2
    new_block = bytes([new_length, 0x05]) + new_val_bytes + b"\x00"

    return data[:replace_start] + new_block + data[replace_end:]


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

    tree, _ = build_tree(0, -1)
    return tree, body


def extract_markdown_section(content: str, keywords: List[str]) -> str:
    """Extract a specific device's section from Markdown body matching keywords."""
    lines = content.splitlines()
    section_lines = []
    in_section = False
    in_section_level = 0

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("#"):
            header_level = len(stripped) - len(stripped.lstrip("#"))
            header_text = stripped.lstrip("#").strip().lower()

            if header_level == 1:
                continue

            if in_section:
                if header_level <= in_section_level:
                    break

            if any(kw.lower() in header_text for kw in keywords):
                in_section = True
                in_section_level = header_level
                continue

        if in_section:
            section_lines.append(line)

    if in_section and section_lines:
        return "\n".join(section_lines)
    return content
