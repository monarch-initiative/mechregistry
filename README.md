<h1 align="center">MechRegistry</h1>

<p align="center">A registry of Mechs: AI agent-curated, ontology-grounded, evidence-backed knowledge bases.</p>

<p align="center"><a href="https://monarch-initiative.github.io/mechregistry/">Visit the registry</a></p>

A Mech keeps one validated record per entity, with a LinkML schema, ontology-grounded
identifiers, cited evidence and an append-only curation history. AI agents write most of it
and people review it. The canonical Mech is [DisMech](https://dismech.monarchinitiative.org/).
The ten microbial Mechs of the [X-Mech suite](https://culturebotai.github.io/mechs/) follow
its pattern.

MechRegistry is modeled on [KG-Registry](https://kghub.org/kg-registry/): every entry is a
Markdown file with a YAML header, one LinkML schema governs the entries, and a Jekyll site on
GitHub Pages renders them.

## Layout

| Path | What it is |
|---|---|
| `mech/<id>/<id>.md` | One entry per Mech. The YAML front matter is a `Mech` object. |
| `src/mechregistry/schema/mechregistry.yaml` | The LinkML schema. |
| `src/mechregistry/cli.py` | `mechregistry validate`, `prettify`, `concat`, `config`. |
| `registry/` | Generated: `mechs.yml`, `mechs.json`, `mechs-summary.json`. |
| `_layouts/`, `_includes/`, `index.html`, `docs/` | The Jekyll site. |
| `_config_header.yml` | Site settings. `_config.yml` is generated from it plus the registry. |
| `docs/schema/` | Generated schema documentation. |
| `tests/` | Pytest suite. |

## Build

```bash
uv sync --dev
make all       # validate entries, write registry/, _config.yml, _data/schema.yaml, docs/schema/
make test
make lint
make site      # jekyll build via docker, into _site/
make serve     # jekyll serve on http://localhost:4000/mechregistry/
```

Validate one entry:

```bash
uv run mechregistry validate mech/dismech/dismech.md
```

Validation is closed: an unknown field or an unrecognized enum value fails. Product ids must
start with the Mech id and a dot. Cross-reference targets must be Mech ids in the registry.
`make check-prefixes` confirms every ontology prefix resolves at the
[Bioregistry](https://bioregistry.io/), which the site links each one to.

## Adding a Mech

Open a [new Mech issue](https://github.com/monarch-initiative/mechregistry/issues/new?template=new-mech.yml),
or copy an existing entry to `mech/<id>/<id>.md`, fill it in, validate, and open a pull
request. See [Contributing](https://monarch-initiative.github.io/mechregistry/docs/contributing.html).

## Deployment

`.github/workflows/pages.yml` runs `make all`, builds the site with the GitHub Pages Jekyll
action and deploys it. The repository's Pages source must be set to **GitHub Actions**.
`.github/workflows/qc.yml` runs lint, validation, tests and a site build on every push and
pull request.

## Licensing

Registry data are released under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/).
Code is released under the BSD 3-Clause license in [LICENSE](LICENSE). Each Mech carries its
own license, recorded in its entry.
