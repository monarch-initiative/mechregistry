---
id: dufmech
category: Mech
layout: mech_detail
name: DUFMech
description: >-
  DUFMech is a knowledge base of protein domains of unknown function. One record is one Pfam
  family whose public InterPro metadata still reads like a domain or protein of unknown
  function (DUF or UPF), including families since renamed. Records are generated from a
  frozen, versioned InterPro/Pfam worklist. Scientific curation lives in separate overlays,
  so imported descriptions and seed labels never become functional claims. Every record is
  currently SEEDED.
activity_status: active
maturity: seeded
homepage_url: https://culturebotai.github.io/DUFMech/
repository: https://github.com/CultureBotAI/DUFMech
schema_url: https://github.com/CultureBotAI/DUFMech/blob/main/src/dufmech/schema/dufmech.yaml
collection:
  - x-mech-suite
domains:
  - genomics
  - microbiology
record_type: a Pfam domain family of unknown function
record_count: 8296
record_count_date: 2026-10-13
record_count_commit: 70a64554005fa4317a83a530e28ed217e3c3e0d2
record_count_source:
  path: data/families
  pattern: "*.yaml"
record_identifier_policy: The Pfam family accession.
ontologies:
  - Pfam
  - InterPro
  - UniProt
  - PDB
data_sources:
  - name: InterPro
    url: https://www.ebi.ac.uk/interpro/
    relation_type: prov:hadPrimarySource
    description: Pfam family metadata, read through the InterPro API into frozen worklists.
  - name: Pfam
    url: https://www.ebi.ac.uk/interpro/entry/pfam/
    relation_type: prov:hadPrimarySource
    description: The families themselves, and their earlier names.
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
    Imported descriptions and automated seed labels are not functional claims. Reference
    correspondence and Pfam/InterPro associations do not promote a SEEDED record; curation
    is a separate overlay.
  validation:
    - schema
    - ontology_terms
    - corpus_reproduction
  curation_history: true
features:
  - ontology_grounding
  - append_only_history
  - knowledge_gaps
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
  - id: dufmech.records
    category: RecordCorpus
    name: Family records
    product_url: https://github.com/CultureBotAI/DUFMech/tree/main/data/families
    format: yaml
  - id: dufmech.schema
    category: DataModelProduct
    name: DUFMech LinkML schema
    product_url: https://github.com/CultureBotAI/DUFMech/blob/main/src/dufmech/schema/dufmech.yaml
    format: linkml
    compatibility:
      - linkml
      - mech_shared
  - id: dufmech.kgx
    category: GraphProduct
    name: DUFMech KGX export
    product_url: https://github.com/CultureBotAI/DUFMech/tree/main/exports/kgx
    format: kgx
  - id: dufmech.sssom
    category: MappingProduct
    name: DUFMech SSSOM export
    product_url: https://github.com/CultureBotAI/DUFMech/tree/main/exports/sssom
    format: sssom
  - id: dufmech.browser
    category: GraphicalInterface
    name: DUFMech dashboard
    product_url: https://culturebotai.github.io/DUFMech/
    format: html
cross_references:
  - target: dismech
    relation: follows_pattern_of
  - target: proteintraitsmech
    relation: consumes
    description: A dated cross-Mech inventory lists the DUF-containing proteins that sibling Mechs hold, nearly all of them from ProteinTraitsMech.
creation_date: 2026-10-13
last_modified_date: 2026-10-13
---
The worklist was first frozen on 2026-10-01 with 6,532 families. The current snapshot,
`interpro-pfam-duf-2026-10-10`, holds 8,296, including families Pfam has renamed away from
DUF or UPF names.
