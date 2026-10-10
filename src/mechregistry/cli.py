"""Command line tools for MechRegistry.

Every Mech entry is a Markdown file at ``mech/<id>/<id>.md`` whose YAML
front matter is a ``Mech`` object in the LinkML schema. The commands here
validate those files, prettify them, and concatenate them into the
``registry/`` artifacts the Jekyll site and other consumers read.
"""

from __future__ import annotations

import argparse
import datetime as dt
import fnmatch
import json
import os
import re
import subprocess
import sys
import tempfile
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
        "record_count_error": mech.get("record_count_error"),
        "record_count_error_date": mech.get("record_count_error_date"),
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
# Bioregistry prefix check
# ----------------------------------------------------------------------------

BIOREGISTRY_API = "https://bioregistry.io/api/registry/"


def check_prefixes(args) -> int:
    """Confirm every value in ``ontologies`` resolves at the Bioregistry.

    The site links each ontology chip to ``https://bioregistry.io/registry/<prefix>``,
    so a prefix the Bioregistry does not know is a dead link. Needs the network.
    """
    import json as _json
    import urllib.error
    import urllib.request

    prefixes: dict[str, set[str]] = {}
    for path in mech_files(args.files):
        data = load_entry(path)
        for prefix in data.get("ontologies", []) or []:
            prefixes.setdefault(prefix, set()).add(data.get("id", path.stem))
    failed = 0
    for prefix in sorted(prefixes):
        url = BIOREGISTRY_API + prefix.lower()
        try:
            with urllib.request.urlopen(url, timeout=30) as resp:
                record = _json.load(resp)
            canonical = record.get("prefix")
            note = "" if canonical == prefix.lower() else f" (Bioregistry canonical: {canonical})"
            print(f"ok   {prefix}{note}")
        except urllib.error.HTTPError as exc:
            failed += 1
            print(f"FAIL {prefix}: HTTP {exc.code} at {url}; used by {', '.join(sorted(prefixes[prefix]))}")
        except Exception as exc:  # noqa: BLE001
            failed += 1
            print(f"FAIL {prefix}: {exc}")
    print(f"{len(prefixes)} prefixes checked, {failed} unresolved")
    return 1 if failed else 0


# ----------------------------------------------------------------------------
# Record count refresh
# ----------------------------------------------------------------------------

# A refreshed count below this fraction of the old one is treated as an
# error and not written. A Mech that moved its records looks like a Mech
# that lost them, and a person should look before the registry says so.
MIN_COUNT_RATIO = 0.5

COUNT_KEYS = ("record_count", "record_count_date", "record_count_commit")
ERROR_KEYS = ("record_count_error", "record_count_error_date")


class CountError(Exception):
    """A record count could not be taken."""


def _git(*args: str, cwd: Path | None = None, timeout: int = 900) -> str:
    proc = subprocess.run(
        ["git", *args], cwd=cwd, capture_output=True, text=True, timeout=timeout, check=False
    )
    if proc.returncode != 0:
        lines = proc.stderr.strip().splitlines()
        msg = next((ln for ln in lines if ln.startswith("fatal:")), None) or (
            lines[-1] if lines else f"exit {proc.returncode}"
        )
        raise CountError(f"Git {args[0]} failed: {msg}")
    return proc.stdout


def count_records(repository: str, source: dict) -> tuple[int, str]:
    """Count the files ``source`` names in ``repository``.

    Clones with no blobs and depth 1, so only commit and tree objects are
    fetched. TaxonMech's 625,960 records come down as about 20 MB.
    Returns the count and the commit it was taken at.
    """
    path = source["path"].strip("/")
    pattern = source.get("pattern") or "*.yaml"
    with tempfile.TemporaryDirectory() as tmp:
        dest = Path(tmp) / "repo"
        clone = ["clone", "--quiet", "--filter=blob:none", "--no-checkout", "--depth", "1"]
        if source.get("branch"):
            clone += ["--branch", source["branch"]]
        try:
            _git(*clone, repository.rstrip("/"), str(dest))
            sha = _git("rev-parse", "HEAD", cwd=dest).strip()
            kind = subprocess.run(
                ["git", "cat-file", "-t", f"HEAD:{path}"],
                cwd=dest, capture_output=True, text=True, check=False,
            ).stdout.strip()
            if kind != "tree":
                raise CountError(f"Directory {path} not found at commit {sha[:7]}")
            # -z keeps non-ASCII file names unquoted, so the pattern sees them.
            out = _git("ls-tree", "-r", "-z", "--name-only", "HEAD", "--", path, cwd=dest)
        except subprocess.TimeoutExpired as exc:
            raise CountError(f"Git timed out after {exc.timeout} s") from exc
    excludes = source.get("exclude") or []
    names = [n.rsplit("/", 1)[-1] for n in out.split("\0") if n]
    count = sum(
        1
        for n in names
        if fnmatch.fnmatchcase(n, pattern)
        and not any(fnmatch.fnmatchcase(n, x) for x in excludes)
    )
    return count, sha


def set_front_matter_keys(text: str, values: dict, after: str) -> str:
    """Set or remove top-level scalar keys in a Markdown file's front matter.

    Edits lines in place so the rest of the file keeps its formatting. A
    round trip through a YAML library would reflow it. A key set to None
    is removed. A key not yet present goes after the key set before it, or
    after ``after``, which must be a scalar key. Failing that it goes last.
    """
    if not text.startswith("---\n"):
        raise ValueError("no front matter")
    end = text.index("\n---", 4)
    lines = text[4:end].split("\n")
    rest = text[end:]

    def find(key: str) -> int | None:
        return next((i for i, ln in enumerate(lines) if ln.startswith(key + ":")), None)

    anchor = after
    for key, value in values.items():
        i = find(key)
        if value is None:
            if i is not None:
                del lines[i]
            continue
        line = f"{key}: {value}"
        if i is not None:
            lines[i] = line
        else:
            j = find(anchor)
            lines.insert(len(lines) if j is None else j + 1, line)
        anchor = key
    return "---\n" + "\n".join(lines) + rest


def refresh_entry(path: Path, today: dt.date, counter=count_records) -> tuple[str, str]:
    """Refresh one entry's record count in place.

    Returns a status (``ok``, ``error`` or ``skip``) and a message. On
    error the old count stays and the error and its date are written next
    to it, for the site to show.
    """
    data = load_entry(path)
    source = data.get("record_count_source")
    if not source:
        return "skip", "no record_count_source"
    old = data.get("record_count")
    try:
        count, sha = counter(data["repository"], source)
        if old and count < old * MIN_COUNT_RATIO:
            raise CountError(
                f"Count fell from {old} to {count} at commit {sha[:7]} and was not applied"
            )
    except CountError as exc:
        status, message = "error", str(exc)
        # One line, double-quoted. JSON string syntax is valid YAML.
        values = {
            "record_count_error": json.dumps(message[:300]),
            "record_count_error_date": today.isoformat(),
        }
    else:
        status, message = "ok", f"{old} -> {count} at {sha[:7]}"
        values = {
            "record_count": str(count),
            "record_count_date": today.isoformat(),
            "record_count_commit": sha,
            "record_count_error": None,
            "record_count_error_date": None,
        }
    # The anchor must be a scalar key. Inserting after a block key would
    # split it from its children.
    after = "record_count_commit" if "record_count_commit" in data else "record_count_date"
    text = path.read_text(encoding="utf-8")
    path.write_text(set_front_matter_keys(text, values, after=after), encoding="utf-8")
    return status, message


def refresh_counts(args) -> int:
    """Refresh record counts from each Mech's repository.

    A failure for one Mech is recorded in its entry and does not stop the
    others. The exit code is 0 unless an entry could not be written.
    """
    today = dt.date.fromisoformat(args.date) if args.date else dt.datetime.now(dt.timezone.utc).date()
    rows = []
    for path in mech_files(args.files):
        status, message = refresh_entry(path, today)
        rows.append((path.stem, status, message))
        print(f"{status:5} {path.stem}: {message}")
    errors = sum(1 for r in rows if r[1] == "error")
    print(f"{len(rows)} entries, {errors} could not be refreshed")
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as fh:
            fh.write(f"### Record counts, {today.isoformat()}\n\n| Mech | Status | Detail |\n|---|---|---|\n")
            for mid, status, message in rows:
                fh.write(f"| {mid} | {status} | {message.replace('|', '/')} |\n")
    return 0


# ----------------------------------------------------------------------------
# Schema docs
# ----------------------------------------------------------------------------


TABLE_SEPARATOR = re.compile(r"^\|(\s*:?-+:?\s*\|)+\s*$")


def drop_empty_tables(lines: list[str]) -> list[str]:
    """Remove tables that have a header and separator but no rows.

    gen-doc writes one under "Cardinality and Requirements" for a slot with
    no constraints. kramdown renders such a table as paragraph text. The
    heading directly above the table goes with it.
    """
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        nxt = lines[i + 1] if i + 1 < len(lines) else ""
        after = lines[i + 2] if i + 2 < len(lines) else ""
        if line.startswith("|") and TABLE_SEPARATOR.match(nxt) and not after.startswith("|"):
            while out and not out[-1].strip():
                out.pop()
            if out and out[-1].startswith("#"):
                out.pop()
            i += 2
            continue
        out.append(line)
        i += 1
    return out


BARE_URL = re.compile(r"(?<![\[(<\w/])(https?://[^\s<>()\[\]]+)")


def fix_schema_doc_text(text: str, title: str) -> str:
    """Rewrite one gen-doc Markdown page so kramdown renders it.

    gen-doc writes MkDocs-flavoured Markdown. kramdown, which GitHub Pages
    uses, differs in ways that break the page:

    * a table must have a blank line before and after it, and gen-doc puts
      the permissible values table straight under its heading and some
      headings straight under a table, and a table with no rows is not a
      table at all;
    * bare URLs are not autolinked, so wrap them in ``<...>``;
    * ``<details>`` content is raw HTML unless marked ``markdown="1"``, so the
      fenced YAML source came out as literal backticks.

    Also replace the ``search:`` front matter with a Jekyll one and point
    ``.md`` links at ``.html``.
    """
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            text = text[end + 5 :]
    text = text.replace(".md)", ".html)")

    out: list[str] = []
    in_fence = False
    for line in drop_empty_tables(text.split("\n")):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue
        if stripped == "<details>":
            out.append('<details markdown="1">')
            out.append("<summary>Show source</summary>")
            out.append("")
            continue
        # A table needs a blank line on both sides or kramdown reads it as
        # paragraph text.
        if out and out[-1].strip() and stripped and line.startswith("|") != out[-1].startswith("|"):
            out.append("")
        if not stripped.startswith("<!--"):
            line = BARE_URL.sub(r"<\1>", line)
        out.append(line)
    text = "\n".join(out)
    return f"---\nlayout: schema_doc\ntitle: {title}\n---\n\n" + text.lstrip("\n")


def fix_schema_docs(args) -> int:
    """Make gen-doc output renderable by Jekyll.

    See :func:`fix_schema_doc_text` for the per-page rewrites. Also rename the
    ``license`` slot page so that it does not collide with the ``License``
    class page on case-insensitive filesystems.
    """
    doc_dir = Path(args.dir)
    for path in sorted(doc_dir.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        path.write_text(fix_schema_doc_text(text, path.stem), encoding="utf-8")
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

    p = sub.add_parser("check-prefixes", help="check ontology prefixes against the Bioregistry")
    p.add_argument("files", nargs="*")
    p.set_defaults(func=check_prefixes)

    p = sub.add_parser("refresh-counts", help="refresh record counts from Mech repositories")
    p.add_argument("files", nargs="*")
    p.add_argument("--date", help="date to record, ISO 8601 (default: today, UTC)")
    p.set_defaults(func=refresh_counts)

    p = sub.add_parser("fix-schema-docs", help="make gen-doc output renderable by Jekyll")
    p.add_argument("dir", nargs="?", default=str(ROOT / "docs" / "schema"))
    p.set_defaults(func=fix_schema_docs)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
