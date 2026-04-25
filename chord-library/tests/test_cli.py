"""Tests for the CLI interface."""

import json
import subprocess
import sys

import pytest


def run_cli(*args):
    """Run chord_cli.py and return (stdout, stderr, returncode)."""
    result = subprocess.run(
        [sys.executable, "chord_cli.py"] + list(args),
        capture_output=True, text=True, timeout=30,
    )
    return result.stdout, result.stderr, result.returncode


class TestCLI:
    def test_query_json_output(self):
        stdout, _, rc = run_cli("query", "--root", "C", "--quality", "", "--format", "json", "--limit", "3")
        assert rc == 0
        data = json.loads(stdout)
        assert "total_matches" in data
        assert "voicings" in data
        assert len(data["voicings"]) <= 3

    def test_query_text_output(self):
        stdout, _, rc = run_cli("query", "--root", "A", "--quality", "m7", "--format", "text", "--limit", "2")
        assert rc == 0
        assert "Am7" in stdout
        assert "voicings found" in stdout

    def test_list_types(self):
        stdout, _, rc = run_cli("list-types")
        assert rc == 0
        assert "major" in stdout
        assert "minor" in stdout
        assert "dominant 7th" in stdout

    def test_list_types_json(self):
        stdout, _, rc = run_cli("list-types", "--format", "json")
        assert rc == 0
        data = json.loads(stdout)
        assert len(data) > 30
        symbols = {entry["symbol"] for entry in data}
        assert "" in symbols  # major
        assert "m7" in symbols

    def test_json_voicing_structure(self):
        stdout, _, rc = run_cli("query", "--root", "G", "--quality", "7", "--format", "json", "--limit", "1")
        assert rc == 0
        data = json.loads(stdout)
        v = data["voicings"][0]
        assert "frets" in v
        assert "notes" in v
        assert "degrees" in v
        assert "inversion" in v
        assert "ascii" in v
        assert "difficulty" in v
        assert len(v["frets"]) == 6
