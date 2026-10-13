---
id: aimech
category: Mech
layout: mech_detail
name: AIMech
description: >-
  AIMech extends the Mech curation workflow from biology to artificial intelligence. One
  record is one AI concept: a model, layer, training strategy, task, bias or the like. It
  holds two kinds. Imported records are a deterministic projection of the Artificial
  Intelligence Ontology (AIO), pinned to release 2026-07-22, and are all NOT_REVIEWED.
  Curated records cover concepts absent from AIO, under stable AIMech IDs with primary
  evidence, claim-specific citations and explicit AIO mappings, and are all DRAFT. Ontology
  membership is not taken as evidence of a model's performance, safety or mechanism.
activity_status: active
maturity: curating
homepage_url: https://culturebotai.github.io/AIMech/
repository: https://github.com/CultureBotAI/AIMech
schema_url: https://github.com/CultureBotAI/AIMech/blob/main/src/aimech/schema/aimech.yaml
collection:
  - x-mech-suite
domains:
  - machine learning
  - information technology
record_type: an artificial intelligence concept
record_count: 1088
record_count_date: 2026-10-13
record_count_commit: b9b06695283c1322e58995a000f4a6b6e3e5fb07
record_count_source:
  path: data
  pattern: "*.yaml"
record_identifier_policy: >-
  The AIO CURIE for imported concepts. A stable, minted AIMech CURIE for curated concepts
  absent from AIO.
identifier_prefix: AIMech
ontologies:
  - AIO
  - BFO
data_sources:
  - name: Artificial Intelligence Ontology
    url: https://github.com/berkeleybop/artificial-intelligence-ontology
    relation_type: prov:hadPrimarySource
    description: The 442 named AIO classes, from a pinned release snapshot.
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
  spdx_id: CC-BY-4.0
code_license:
  id: https://opensource.org/license/bsd-3-clause
  label: BSD-3-Clause
  spdx_id: BSD-3-Clause
curation:
  agent_curated: true
  human_review: pull_request
  agents:
    - Claude Code
    - culturebotai-claw
  evidence_policy: >-
    Curated concepts need inspected primary evidence, claim-specific citations, and an
    explicit AIO mapping or a documented no-match assessment. Scientific reviews are saved
    separately from records.
  validation:
    - schema
    - corpus_reproduction
  curation_history: true
features:
  - ontology_grounding
  - append_only_history
  - static_browser
contacts:
  - category: Organization
    label: CultureBotAI
    contact_details:
      - contact_type: github
        value: CultureBotAI
  - category: Individual
    label: Marcin P. Joachimiak
    orcid: 0000-0001-8175-045X
    contact_details:
      - contact_type: email
        value: mjoachimiak@lbl.gov
      - contact_type: github
        value: realmarcin
products:
  - id: aimech.records
    category: RecordCorpus
    name: AI concept records
    description: Imported AIO records under data/aio/ and curated records under data/curated/.
    product_url: https://github.com/CultureBotAI/AIMech/tree/main/data
    format: yaml
  - id: aimech.schema
    category: DataModelProduct
    name: AIMech LinkML schema
    product_url: https://github.com/CultureBotAI/AIMech/blob/main/src/aimech/schema/aimech.yaml
    format: linkml
    compatibility:
      - linkml
      - mech_shared
  - id: aimech.browser
    category: GraphicalInterface
    name: AIMech browser
    product_url: https://culturebotai.github.io/AIMech/
    format: html
cross_references:
  - target: dismech
    relation: follows_pattern_of
    description: Applies the Mech curation workflow outside biology.
creation_date: 2026-10-13
last_modified_date: 2026-10-13
---
The count covers both record kinds: 442 imported from AIO and 646 curated, as of 2026-10-13.
The fleet manifest's record glob covers only the imported records.
