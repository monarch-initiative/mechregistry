---
id: communitymech
category: Mech
layout: mech_detail
name: CommunityMech
synonyms:
  - Microbial Community Mechanisms Knowledge Base
description: >-
  CommunityMech is a knowledge base of microbial communities: their composition, ecological
  interactions, cultivation conditions, environments and supporting evidence. Curated YAML
  is the canonical record format. Validation, the static browser and the KGX export are all
  derived from it. Community records name the culture medium they were cultivated in by
  CultureMech identifier. The project is adapted from DisMech.
activity_status: active
maturity: curating
homepage_url: https://culturebotai.github.io/CommunityMech/
repository: https://github.com/CultureBotAI/CommunityMech
schema_url: https://github.com/CultureBotAI/CommunityMech/blob/main/src/communitymech/schema/communitymech.yaml
collection:
  - x-mech-suite
  - kg-microbe
domains:
  - microbiology
  - environment
  - organisms
taxon:
  - NCBITaxon:2
  - NCBITaxon:2157
record_type: a microbial community
record_count: 328
record_count_date: 2026-09-10
ontologies:
  - NCBITaxon
  - CHEBI
  - GO
  - ENVO
  - GTDB
data_sources:
  - name: PubMed
    url: https://pubmed.ncbi.nlm.nih.gov/
    relation_type: prov:hadPrimarySource
    description: Literature evidence for community composition and interactions, cached in references_cache for reproducible checks.
  - name: GTDB
    url: https://gtdb.ecogenomic.org/
    relation_type: prov:used
    description: Taxonomy for community members.
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
  spdx_id: CC0-1.0
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
    Interactions and cultivation claims carry evidence items with references. Cached source
    text in the repository makes evidence checks reproducible offline.
  validation:
    - schema
    - ontology_terms
    - references
    - cross_field
  curation_history: true
features:
  - evidence_snippets
  - ontology_grounding
  - append_only_history
  - knowledge_gaps
  - static_browser
  - kgx_export
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
  - id: communitymech.records
    category: RecordCorpus
    name: Community records
    description: Canonical MicrobialCommunity records in kb/communities, with reusable CommonTaxon records in kb/taxa.
    product_url: https://github.com/CultureBotAI/CommunityMech/tree/main/kb/communities
    format: yaml
  - id: communitymech.schema
    category: DataModelProduct
    name: CommunityMech LinkML schema
    product_url: https://github.com/CultureBotAI/CommunityMech/blob/main/src/communitymech/schema/communitymech.yaml
    format: linkml
    compatibility:
      - linkml
      - mech_shared
  - id: communitymech.kgx
    category: GraphProduct
    name: KGX export
    description: Nodes and edges emitted by a deterministic Python emitter from the community YAML.
    product_url: https://github.com/CultureBotAI/CommunityMech
    format: kgx
    compatibility:
      - kgx
      - biolink
  - id: communitymech.browser
    category: GraphicalInterface
    name: CommunityMech browser
    product_url: https://culturebotai.github.io/CommunityMech/
    format: html
cross_references:
  - target: dismech
    relation: follows_pattern_of
  - target: culturemech
    relation: consumes
    description: Community records name the medium they were cultivated in by CultureMech id.
  - target: mediaingredientmech
    relation: consumes
    description: The RelatedIngredient.mediaingredientmech_id slot is declared for MediaIngredientMech ingredient ids. No record populates it yet.
creation_date: 2026-09-10
last_modified_date: 2026-09-10
---
