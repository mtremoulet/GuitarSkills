"""ASCII chord diagram renderer."""

from __future__ import annotations

from .voicing import Voicing


def render_voicing(voicing: Voicing, col_width: int = 4) -> str:
    """Render a voicing as a horizontal ASCII diagram.

    Format:
      E    A    D    G    B    e
      X    3    2    0    1    0
      -    C    E    G    C    E
      -    R    3    5    R    3

    Args:
        voicing: The Voicing to render.
        col_width: Width of each column (default 4).

    Returns:
        Multi-line string.
    """
    tuning = voicing.fretboard.tuning
    string_names = tuning.string_names
    frets = voicing.frets
    note_names = voicing.note_names
    interval_names = voicing.interval_names

    def pad(s: str) -> str:
        return s.ljust(col_width)

    # Row 1: String names
    row_strings = "".join(pad(name) for name in string_names)

    # Row 2: Fret numbers
    fret_strs = []
    for f in frets:
        if f is None:
            fret_strs.append("X")
        else:
            fret_strs.append(str(f))
    row_frets = "".join(pad(s) for s in fret_strs)

    # Row 3: Note names
    note_strs = []
    for n in note_names:
        note_strs.append(n if n else "-")
    row_notes = "".join(pad(s) for s in note_strs)

    # Row 4: Chord degrees
    degree_strs = []
    for d in interval_names:
        degree_strs.append(d if d else "-")
    row_degrees = "".join(pad(s) for s in degree_strs)

    return f"{row_strings}\n{row_frets}\n{row_notes}\n{row_degrees}"


def render_voicing_compact(voicing: Voicing) -> str:
    """Render a compact single-line representation: X-3-2-0-1-0."""
    parts = []
    for f in voicing.frets:
        if f is None:
            parts.append("X")
        else:
            parts.append(str(f))
    return "-".join(parts)


def render_voicings(voicings: list[Voicing], header: str = "", max_per_row: int = 3) -> str:
    """Render multiple voicings side by side.

    Args:
        voicings: List of voicings to render.
        header: Optional header text.
        max_per_row: Maximum voicings displayed per row.

    Returns:
        Multi-line string with voicings arranged in groups.
    """
    if not voicings:
        return "No voicings found."

    lines = []
    if header:
        lines.append(header)
        lines.append("")

    col_width = 4
    gap = "    "  # gap between voicing blocks

    for batch_start in range(0, len(voicings), max_per_row):
        batch = voicings[batch_start:batch_start + max_per_row]
        rendered = [render_voicing(v, col_width).split("\n") for v in batch]

        # Each rendered voicing has 4 rows
        for row_idx in range(4):
            parts = []
            for r in rendered:
                parts.append(r[row_idx].rstrip())
            lines.append(gap.join(parts))

        # Add compact notation below each
        compact_parts = []
        for v in batch:
            compact = render_voicing_compact(v)
            compact_parts.append(compact.ljust(col_width * len(v.frets)))
        lines.append(gap.join(compact_parts))
        lines.append("")

    return "\n".join(lines)
