"""Tests for the MechRegistry entries and tools."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

from mechregistry import cli

ROOT = Path(__file__).resolve().parents[1]
ENTRIES = sorted((ROOT / "mech").glob("*/*.md"))


def test_entries_exist():
    assert ENTRIES, "no entries under mech/"


@pytest.mark.parametrize("path", ENTRIES, ids=[p.stem for p in ENTRIES])
def test_entry_validates(path: Path):
    data = cli.load_entry(path)
    assert cli.check_entry(path, data) == []


def test_cross_references_resolve():
    entries = {cli.load_entry(p)["id"]: cli.load_entry(p) for p in ENTRIES}
    assert cli.check_cross_references(entries) == []


def test_dismech_is_the_canonical_mech():
    entries = {cli.load_entry(p)["id"]: cli.load_entry(p) for p in ENTRIES}
    assert "dismech" in entries
    followers = [
        mid
        for mid, m in entries.items()
        for r in m.get("cross_references", [])
        if r["target"] == "dismech" and r["relation"] == "follows_pattern_of"
    ]
    assert len(followers) == len(entries) - 1


def test_validator_rejects_unknown_field(tmp_path: Path):
    src = (ROOT / "mech" / "dismech" / "dismech.md").read_text()
    bad_dir = tmp_path / "bad"
    bad_dir.mkdir()
    bad = bad_dir / "bad.md"
    bad.write_text(src.replace("id: dismech", "id: bad").replace(
        "activity_status: active", "activity_status: bogus\nnot_a_field: 1"
    ))
    errors = cli.check_entry(bad, cli.load_entry(bad))
    joined = "\n".join(errors)
    assert "bogus" in joined
    assert "not_a_field" in joined


def test_concat_and_config(tmp_path: Path):
    out = tmp_path / "mechs.yml"
    assert cli.main(["concat", "-o", str(out)]) == 0
    assert out.exists()
    data = json.loads(out.with_suffix(".json").read_text())
    ids = [m["id"] for m in data["mechs"]]
    assert ids == sorted(ids)
    assert len(ids) == len(ENTRIES)
    summary = json.loads((tmp_path / "mechs-summary.json").read_text())
    assert {m["id"] for m in summary["mechs"]} == set(ids)
    cfg = tmp_path / "_config.yml"
    assert cli.main(["config", "--registry", str(out), "--output", str(cfg)]) == 0
    text = cfg.read_text()
    assert text.startswith("name: MechRegistry")
    assert "\nmechs:\n" in text


def test_cli_validate_exit_code():
    proc = subprocess.run(
        [sys.executable, "-m", "mechregistry.cli", "validate"],
        capture_output=True,
        text=True,
        cwd=ROOT,
        check=False,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
