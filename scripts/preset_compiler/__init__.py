"""Preset compiler package for GuitarSkills rig automation."""

from .base import parse_yaml_frontmatter, extract_markdown_section, replace_binary_parameter
from .neural import compile_neural_toneprint
from .uad import (
    compile_uad_toneprint,
    compile_la2a_toneprint,
    compile_hitsville_toneprint,
    compile_galaxy_toneprint,
    compile_studio_d_toneprint,
)
from .mixwave import compile_mixwave_toneprint
from .valhalla import compile_supermassive_toneprint
from .logic import (
    compile_logic_eq_toneprint,
    compile_logic_compressor_toneprint,
    compile_logic_space_designer_toneprint,
)
from .yamaha import compile_yamaha_thr_toneprint
from .nembrini import (
    compile_nembrini_xml_preset,
    compile_nembrini_stomp_presets,
    compile_kuassa_stomp_presets,
)

__all__ = [
    "parse_yaml_frontmatter",
    "extract_markdown_section",
    "replace_binary_parameter",
    "compile_neural_toneprint",
    "compile_uad_toneprint",
    "compile_la2a_toneprint",
    "compile_hitsville_toneprint",
    "compile_galaxy_toneprint",
    "compile_studio_d_toneprint",
    "compile_mixwave_toneprint",
    "compile_supermassive_toneprint",
    "compile_logic_eq_toneprint",
    "compile_logic_compressor_toneprint",
    "compile_logic_space_designer_toneprint",
    "compile_yamaha_thr_toneprint",
    "compile_nembrini_xml_preset",
    "compile_nembrini_stomp_presets",
    "compile_kuassa_stomp_presets",
]
