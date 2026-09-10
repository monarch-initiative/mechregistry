---
layout: doc
title: About MechRegistry
---

# About MechRegistry

MechRegistry is a registry of Mechs. A Mech is an AI agent-curated knowledge base
that keeps one validated, ontology-grounded, evidence-backed record per entity,
with a LinkML schema and an append-only curation history. The canonical Mech is
[DisMech](https://dismech.monarchinitiative.org/), the Disorder Mechanisms
Knowledge Base. [What is a Mech?](what-is-a-mech.html) says more.

The registry records, for each Mech:

- what one record represents, and how many records there are
- how records are identified and which ontologies ground them
- which upstream sources the records are seeded or harmonized from
- the curation model: which agents write it, what human review gates it, what
  evidence a claim must carry, and what validation runs in CI
- its products: record corpus, schema, browser, exports and documentation
- its licenses, contacts and publications
- typed relations to other Mechs

## How it is built

Every Mech is one Markdown file at `mech/<id>/<id>.md`. Its YAML front matter is
a `Mech` object in the [MechRegistry LinkML schema](schema/). A build step
validates every entry against the schema with closed validation, so a misspelled
field or an unknown enum value fails the build, and then concatenates the entries
into the registry files the site and other tools read:

- [`registry/mechs.yml`]({{ '/registry/mechs.yml' | relative_url }}), the full registry as YAML
- [`registry/mechs.json`]({{ '/registry/mechs.json' | relative_url }}), the same as JSON
- [`registry/mechs-summary.json`]({{ '/registry/mechs-summary.json' | relative_url }}), a slim per-Mech summary

The site is a Jekyll site on GitHub Pages. The design follows
[KG-Registry](https://kghub.org/kg-registry/): Markdown with YAML headers, one
LinkML model, static pages, no server.

## Licensing

Registry data are released under the
[CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) waiver.
The repository code is released under the BSD 3-Clause license. Each Mech carries
its own license, shown on its page.

## Who maintains it

MechRegistry is maintained by the [Monarch Initiative](https://monarchinitiative.org).
Source and issues are on [GitHub]({{ site.repo }}).
