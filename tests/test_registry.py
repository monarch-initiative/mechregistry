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


def test_fix_schema_doc_text_makes_kramdown_render():
    src = (
        "---\nsearch:\n  exclude: true\n---\n"
        "# Enum: X\n\n"
        "URI: [mechregistry:X](https://w3id.org/x/X)\n\n"
        "## Permissible Values\n"
        "| Value | Meaning |\n| --- | --- |\n| a | None |\n"
        "## Slots\n\n| Name |\n| --- |\n| [relation](relation.md) |\n\n"
        "* from schema: https://w3id.org/x\n\n"
        "### Cardinality and Requirements\n\n| Property | Value |\n| --- | --- |\n\n"
        "### Slot Characteristics\n\n| Property | Value |\n| --- | --- |\n| Owner | X |\n\n"
        "<!-- TODO: see https://example.org/keep -->\n\n"
        "<details>\n```yaml\nfrom_schema: https://w3id.org/x\n```\n</details>\n"
    )
    fixed = cli.fix_schema_doc_text(src, "X")
    assert fixed.startswith("---\nlayout: schema_doc\ntitle: X\n---\n\n# Enum: X")
    assert "search:" not in fixed
    # A blank line separates the heading from the table.
    assert "## Permissible Values\n\n| Value |" in fixed
    assert "| a | None |\n\n## Slots" in fixed
    # An existing blank line is not doubled.
    assert "## Slots\n\n\n" not in fixed
    assert "](relation.html)" in fixed
    # Bare URLs become autolinks; linked, commented, and fenced ones are untouched.
    assert "* from schema: <https://w3id.org/x>" in fixed
    assert "[mechregistry:X](https://w3id.org/x/X)" in fixed
    assert "<!-- TODO: see https://example.org/keep -->" in fixed
    assert "from_schema: https://w3id.org/x\n" in fixed
    # An empty table and its heading are dropped; a populated one stays.
    assert "Cardinality and Requirements" not in fixed
    assert "### Slot Characteristics\n\n| Property | Value |\n| --- | --- |\n| Owner | X |" in fixed
    assert '<details markdown="1">\n<summary>Show source</summary>\n\n```yaml' in fixed
