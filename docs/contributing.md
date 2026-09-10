---
layout: doc
title: Contributing
---

# Contributing

## Suggest a Mech

Open a [new Mech issue]({{ site.repo }}/issues/new?template=new-mech.yml). The
form asks for the repository, the homepage, what one record represents, the
license and the curation model. Not every field is required.

## Add or edit an entry directly

1. Copy an existing entry, for example `mech/dismech/dismech.md`, to
   `mech/<id>/<id>.md`. The id is a lowercase slug and must match both the
   directory and the file name.
2. Fill in the front matter. Required fields: `id`, `category: Mech`,
   `layout: mech_detail`, `name`, `description`, `activity_status`,
   `repository`, `domains`, `record_type`, and `curation` with at least
   `agent_curated`. Everything else is optional. The [schema](schema/) documents
   every field and enum.
3. Product ids must start with the Mech id and a dot: `dismech.records`.
4. Cross-reference targets must be Mech ids in the registry.
5. Validate:

```bash
uv sync
uv run mechregistry validate mech/<id>/<id>.md
```

6. Open a pull request. CI validates every entry and builds the site.

## Ontology prefixes

Values in `ontologies` are Bioregistry prefixes. The site links every one to
`https://bioregistry.io/registry/<prefix>`, so a prefix the
[Bioregistry](https://bioregistry.io/) does not know is a dead link. Check with:

```bash
make check-prefixes
```

Use the conventional capitalization (`CHEBI`, `NCBITaxon`, `UniProt`). Lookups are
case-insensitive.

## Keep counts honest

`record_count` counts records in the canonical corpus, not files in the
repository and not intermediate layers. Set `record_count_date` to the date you
counted. Say in the body of the entry, below the front matter, how you counted.

## Local site build

The site is Jekyll. With Docker:

```bash
make all      # validate, build registry/, write _config.yml and schema docs
make site     # jekyll build in the GitHub Pages image
make serve    # jekyll serve on http://localhost:4000/mechregistry/
```

`_config.yml`, `_data/schema.yaml`, `registry/mechs.*` and `docs/schema/` are
generated. Do not edit them by hand and do not commit them. CI regenerates them
on every build.
