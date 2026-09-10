---
layout: doc
title: What is a Mech?
---

# What is a Mech?

A Mech is a knowledge base built on a specific pattern. The pattern was set by
[DisMech](https://dismech.monarchinitiative.org/) and is followed by the microbial
Mechs of the [X-Mech suite](https://culturebotai.github.io/mechs/). The name comes
from *mechanism*: the first Mechs record how something works, not just that it
exists.

The pattern has these parts.

**One record per entity.** A disorder, a habitat, a community, a trait, a
structure, a protein trait class, a natural product, an antibiotic, an ingredient,
a recipe. Each is one YAML file. The file is the unit of curation, review and
history.

**A LinkML schema.** Records validate against the Mech's own schema, with closed
validation, on every change. The X-Mech suite schemas also import a shared module,
`mech_shared.yaml`, ported from DisMech, that supplies Discussion (open questions,
knowledge gaps, controversies, curation to-dos) and Dataset classes.

**Ontology-grounded identity.** Records are keyed by a public CURIE where one
exists: ChEBI, GO, METPO, ENVO, NCBITaxon, Mondo. Where none does, the Mech mints
a content-hashed CURIE in its own namespace that can be re-grounded later. Every
identifier is stored with its label, and CI checks that the pair still agrees with
the source ontology.

**Evidence and provenance.** Claims carry evidence items with PMIDs or DOIs. In
DisMech every evidence item quotes the cited abstract verbatim and a validator
fetches the abstract and checks the quote. Sources are catalogued with their
licenses before they are ingested.

**Causal mechanism graphs.** Disorders, traits, structures, antibiotics and
habitats can carry directed, evidence-backed graphs of mechanism. The X-Mech
suite shares one node vocabulary so that graphs compare across Mechs.

**Append-only curation history.** Every change is an event in a history
directory that only grows, so agents and people can curate the same corpus at
the same time without conflicts.

**AI agents write most of it. People review it.** Content is generated and
maintained by AI curation agents. The human gate is the pull request. Automated
validation guarantees that citations exist, quotes are exact and ontology terms
are real. It does not guarantee that the science is right, and the Mechs say so.

**A static browser and an open license.** Each Mech publishes a site over its
records and releases them under CC0 or CC BY.

## What a Mech is not

A Mech is not a knowledge graph, though several export to KGX and feed
[KG-Microbe](https://kghub.org/kg-microbe/). A knowledge graph flattens records
into nodes and edges. A Mech keeps the record, with its evidence, its history and
its open questions, as the thing that is curated. For knowledge graphs, see
[KG-Registry](https://kghub.org/kg-registry/).

A Mech is not an ontology. It grounds in ontologies and asks them for terms it
lacks.

## The fleet standard

The X-Mech suite maintains a written standard,
[`MECH_STANDARD.md`](https://github.com/CultureBotAI/culturebotai-claw/blob/main/docs/guides/MECH_STANDARD.md),
derived by measuring the established Mechs. It names what a repository must hold
to be a Mech, what it may reuse, and what is nobody's business but its own. The
fleet is coordinated by
[culturebotai-claw](https://github.com/CultureBotAI/culturebotai-claw), which
holds the fleet manifest, the vendored shared artifacts and the cross-repository
pipelines.
