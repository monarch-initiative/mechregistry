"""Command line tools for MechRegistry.

Every Mech entry is a Markdown file at ``mech/<id>/<id>.md`` whose YAML
front matter is a ``Mech`` object in the LinkML schema. The commands here
validate those files, prettify them, and concatenate them into the
``registry/`` artifacts the Jekyll site and other consumers read.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from functools import lru_cache
from io import StringIO
from pathlib import Path

import frontmatter
import yaml
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml_runtime.linkml_model.meta import SchemaDefinition
from linkml_runtime.loaders import yaml_loader
from ruamel.yaml import YAML

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = ROOT / "src" / "mechregistry" / "schema" / "mechregistry.yaml"
MECH_DIR = ROOT / "mech"
REGISTRY_DIR = ROOT / "registry"


# ----------------------------------------------------------------------------
# Loading
# ----------------------------------------------------------------------------


class RuamelHandler(frontmatter.YAMLHandler):
    """Round-trip YAML handler so prettify keeps key order and comments."""

    def __init__(self) -> None:
        self.rt = YAML()
        self.rt.default_flow_style = False
        self.rt.indent(mapping=2, sequence=4, offset=2)
        self.rt.preserve_quotes = True
        self.rt.width = 1000
        super().__init__()

    def load(self, fm, **kwargs):
        return self.rt.load(fm, **kwargs)

    def export(self, metadata, **kwargs):
        stream = StringIO()
        self.rt.dump(metadata, stream)
        return stream.getvalue().rstrip("\n")


def mech_files(paths: list[str] | None = None) -> list[Path]:
    """Return the Mech entry files to work on, sorted."""
    if paths:
        return [Path(p) for p in paths]
    return sorted(MECH_DIR.glob("*/*.md"))


def _plain(obj):
    """Convert ruamel/date objects into plain JSON-able Python."""
    if isinstance(obj, dict):
        return {str(k): _plain(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_plain(v) for v in obj]
    if isinstance(obj, (dt.date, dt.datetime)):
        return obj.isoformat()
    return obj


def load_entry(path: Path) -> dict:
    """Load one Mech entry's front matter as plain Python."""
    post = frontmatter.load(str(path))
    return _plain(post.metadata)


# ----------------------------------------------------------------------------
# Validation
# ----------------------------------------------------------------------------


@lru_cache(maxsize=1)
def get_validator() -> Validator:
    schema = yaml_loader.load(str(SCHEMA_PATH), target_class=SchemaDefinition)
    return Validator(schema, validation_plugins=[JsonschemaValidationPlugin(closed=True)])


def check_entry(path: Path, data: dict) -> list[str]:
    """Validate one entry. Returns a list of error messages, empty if valid."""
    errors: list[str] = []
    expected_id = path.stem
    if data.get("id") != expected_id:
        errors.append(f"id '{data.get('id')}' does not match file name '{expected_id}'")
    if path.parent.name != expected_id:
        errors.append(f"directory '{path.parent.name}' does not match file name '{expected_id}'")
    if data.get("category") != "Mech":
        errors.append("category must be 'Mech'")
    if data.get("layout") != "mech_detail":
        errors.append("layout must be 'mech_detail'")
    report = get_validator().validate(data, target_class="Mech")
    for result in report.results:
        errors.append(result.message)
    # Product ids must be prefixed by the Mech id.
    for product in data.get("products", []) or []:
        pid = product.get("id", "")
        if not pid.startswith(data.get("id", "") + "."):
            errors.append(f"product id '{pid}' must start with '{data.get('id')}.'")
    return errors


def check_cross_references(entries: dict[str, dict]) -> list[str]:
    """Every cross_reference target must be a Mech in the registry."""
    errors = []
    for mech_id, data in entries.items():
        for ref in data.get("cross_references", []) or []:
            target = ref.get("target")
            if target not in entries:
                errors.append(f"{mech_id}: cross_reference target '{target}' is not in the registry")
    return errors


def validate(args) -> int:
    files = mech_files(args.files)
    entries: dict[str, dict] = {}
    failed = 0
    for path in files:
        try:
            data = load_entry(path)
        except Exception as exc:  # noqa: BLE001
            print(f"FAIL {path}: cannot parse front matter: {exc}")
            failed += 1
            continue
        errors = check_entry(path, data)
        if errors:
            failed += 1
            print(f"FAIL {path}")
            for e in errors:
                print(f"  - {e}")
        else:
            print(f"ok   {path}")
        entries[data.get("id", path.stem)] = data
    if not args.files:
        xerrs = check_cross_references(entries)
        for e in xerrs:
            print(f"FAIL {e}")
        failed += len(xerrs)
    print(f"{len(files)} entries checked, {failed} with errors")
    return 1 if failed else 0


# ----------------------------------------------------------------------------
# Prettify
# ----------------------------------------------------------------------------


def prettify(args) -> int:
    handler = RuamelHandler()
    for path in mech_files(args.files):
        post = frontmatter.load(str(path), handler=handler)
        text = frontmatter.dumps(post, handler=handler)
        path.write_text(text.rstrip("\n") + "\n", encoding="utf-8")
        print(f"prettified {path}")
    return 0


# ----------------------------------------------------------------------------
# Concatenation and derived artifacts
# ----------------------------------------------------------------------------


def build_registry(files: list[Path]) -> dict:
    mechs = [load_entry(p) for p in files]
    mechs.sort(key=lambda m: m["id"])
    return {"mechs": mechs}


def summarize(mech: dict) -> dict:
    """Slim record for the front-page table."""
    lic = mech.get("license") or {}
    return {
        "id": mech["id"],
        "name": mech.get("name"),
        "description": mech.get("description"),
        "activity_status": mech.get("activity_status"),
        "maturity": mech.get("maturity"),
        "collection": mech.get("collection", []),
        "domains": mech.get("domains", []),
        "record_type": mech.get("record_type"),
        "record_count": mech.get("record_count"),
        "record_count_date": mech.get("record_count_date"),
        "homepage_url": mech.get("homepage_url"),
        "repository": mech.get("repository"),
        "license": lic.get("label"),
        "ontologies": mech.get("ontologies", []),
        "agent_curated": (mech.get("curation") or {}).get("agent_curated"),
        "human_review": (mech.get("curation") or {}).get("human_review"),
        "features": mech.get("features", []),
    }


def concat(args) -> int:
    files = mech_files(args.files)
    registry = build_registry(files)
    REGISTRY_DIR.mkdir(exist_ok=True)
    out_yaml = Path(args.output) if args.output else REGISTRY_DIR / "mechs.yml"
    with out_yaml.open("w", encoding="utf-8") as fh:
        fh.write("# Generated by `mechregistry concat`. Do not edit; edit mech/<id>/<id>.md.\n")
        yaml.safe_dump(registry, fh, sort_keys=False, allow_unicode=True, width=1000)
    out_json = out_yaml.with_suffix(".json")
    with out_json.open("w", encoding="utf-8") as fh:
        json.dump(
            {
                "@context": {"@vocab": "https://w3id.org/monarch-initiative/mechregistry/"},
                **registry,
            },
            fh,
            indent=2,
            ensure_ascii=False,
        )
        fh.write("\n")
    out_summary = out_yaml.parent / "mechs-summary.json"
    with out_summary.open("w", encoding="utf-8") as fh:
        json.dump({"mechs": [summarize(m) for m in registry["mechs"]]}, fh, indent=2)
        fh.write("\n")
    print(f"wrote {out_yaml}, {out_json}, {out_summary} ({len(registry['mechs'])} mechs)")
    return 0


def config(args) -> int:
    """Write _config.yml from the header and the concatenated registry."""
    header = Path(args.header).read_text(encoding="utf-8")
    registry_yaml = Path(args.registry).read_text(encoding="utf-8")
    Path(args.output).write_text(header.rstrip("\n") + "\n" + registry_yaml, encoding="utf-8")
    print(f"wrote {args.output}")
    return 0


# ----------------------------------------------------------------------------
# Schema docs
# ----------------------------------------------------------------------------


def fix_schema_docs(args) -> int:
    """Make gen-doc output renderable by Jekyll.

    gen-doc writes MkDocs-flavoured Markdown: a ``search:`` front matter block and
    links to ``.md`` files. Replace the front matter with a Jekyll one and point
    links at ``.html``. Also rename the ``license`` slot page so that it does not
    collide with the ``License`` class page on case-insensitive filesystems.
    """
    doc_dir = Path(args.dir)
    for path in sorted(doc_dir.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        if text.startswith("---\n"):
            end = text.find("\n---\n", 4)
            if end != -1:
                text = text[end + 5 :]
        text = text.replace(".md)", ".html)")
        title = path.stem
        text = f"---\nlayout: schema_doc\ntitle: {title}\n---\n\n" + text.lstrip("\n")
        path.write_text(text, encoding="utf-8")
    lower = doc_dir / "license.md"
    upper = doc_dir / "License.md"
    # On a case-sensitive filesystem both exist as distinct files; on a
    # case-insensitive one the second write clobbered the first.
    distinct = (
        lower.exists()
        and upper.exists()
        and lower.read_text(encoding="utf-8") != upper.read_text(encoding="utf-8")
    )
    if distinct:
        lower.rename(doc_dir / "license_slot.md")
        for path in doc_dir.glob("*.md"):
            text = path.read_text(encoding="utf-8")
            fixed = text.replace("](license.html)", "](license_slot.html)")
            if fixed != text:
                path.write_text(fixed, encoding="utf-8")
    print(f"fixed schema docs in {doc_dir}")
    return 0


# ----------------------------------------------------------------------------
# Entrypoint
# ----------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="MechRegistry tools")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("validate", help="validate Mech entry front matter against the schema")
    p.add_argument("files", nargs="*")
    p.set_defaults(func=validate)

    p = sub.add_parser("prettify", help="normalize YAML front matter formatting")
    p.add_argument("files", nargs="*")
    p.set_defaults(func=prettify)

    p = sub.add_parser("concat", help="concatenate entries into registry/mechs.yml and .json")
    p.add_argument("files", nargs="*")
    p.add_argument("-o", "--output")
    p.set_defaults(func=concat)

    p = sub.add_parser("config", help="write _config.yml from the header and registry")
    p.add_argument("--header", default=str(ROOT / "_config_header.yml"))
    p.add_argument("--registry", default=str(REGISTRY_DIR / "mechs.yml"))
    p.add_argument("--output", default=str(ROOT / "_config.yml"))
    p.set_defaults(func=config)

    p = sub.add_parser("fix-schema-docs", help="make gen-doc output renderable by Jekyll")
    p.add_argument("dir", nargs="?", default=str(ROOT / "docs" / "schema"))
    p.set_defaults(func=fix_schema_docs)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
