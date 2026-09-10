---
id: culturemech
category: Mech
layout: mech_detail
name: CultureMech
synonyms:
  - Microbial Culture Media Knowledge Graph
description: >-
  CultureMech is a versioned knowledge base of microbial culture-media recipes from
  MediaDive, TogoMedium, KOMODO and the major culture collections. It combines LinkML
  validation, ontology grounding, provenance, deduplication, browser exports and static
  recipe pages. The corpus has four layers: immutable raw source payloads, mechanical
  source-shaped YAML, authoritative normalized records that preserve source-specific
  formulations, and reproducible merged records that are the deduplicated canonical output.
  The merged layer is what this entry counts.
activity_status: active
maturity: curating
homepage_url: https://culturebotai.github.io/CultureMech/
repository: https://github.com/CultureBotAI/CultureMech
schema_url: https://github.com/CultureBotAI/CultureMech/blob/main/src/culturemech/schema/culturemech.yaml
collection:
  - x-mech-suite
  - kg-microbe
domains:
  - microbiology
  - nutrition
  - chemistry and biochemistry
taxon:
  - NCBITaxon:2
  - NCBITaxon:2157
  - NCBITaxon:4751
record_type: a culture-medium recipe
record_count: 6286
record_count_date: 2026-09-10
ontologies:
  - CHEBI
  - KEGG
  - FOODON
  - UBERON
  - CAS
  - NCBITaxon
data_sources:
  - name: MediaDive
    url: https://mediadive.dsmz.de/
    relation_type: prov:hadPrimarySource
    description: DSMZ culture-media recipes and solution volumes.
  - name: TogoMedium
    url: https://togomedium.org/
    relation_type: prov:hadPrimarySource
  - name: KOMODO
    url: https://komodo.modelseed.org/
    relation_type: prov:hadPrimarySource
    description: Recipes and base volumes.
  - name: MediaIngredientMech
    url: https://github.com/CultureBotAI/MediaIngredientMech
    relation_type: prov:used
    description: Curated ingredient identity and ontology mappings synced back into recipes.
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
  spdx_id: CC0-1.0
curation:
  agent_curated: true
  human_review: pull_request
  agents:
    - Claude Code
    - culturebotai-claw
  evidence_policy: >-
    Every recipe keeps its source provenance. Normalized records preserve source-specific
    formulations and merged records record which normalized records they combine.
  validation:
    - schema
    - ontology_terms
    - cross_field
    - corpus_reproduction
  curation_history: true
  curation_guide_url: https://github.com/CultureBotAI/CultureMech/blob/main/docs/DATA_LAYERS.md
features:
  - ontology_grounding
  - append_only_history
  - knowledge_gaps
  - static_browser
  - sssom_export
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
  - id: culturemech.records
    category: RecordCorpus
    name: Merged recipe records
    description: Reproducible, deduplicated canonical recipes. The normalized layer holds 15,878 source-specific records behind them.
    product_url: https://github.com/CultureBotAI/CultureMech/tree/main/data/merge_yaml/merged
    format: yaml
  - id: culturemech.normalized
    category: RecordCorpus
    name: Normalized recipe records
    description: Authoritative curated and validated records, one per source formulation.
    product_url: https://github.com/CultureBotAI/CultureMech/tree/main/data/normalized_yaml
    format: yaml
  - id: culturemech.schema
    category: DataModelProduct
    name: CultureMech LinkML schema
    product_url: https://github.com/CultureBotAI/CultureMech/blob/main/src/culturemech/schema/culturemech.yaml
    format: linkml
    compatibility:
      - linkml
      - mech_shared
  - id: culturemech.browser
    category: GraphicalInterface
    name: CultureMech browser
    description: Browser-based exploration and static recipe pages.
    product_url: https://culturebotai.github.io/CultureMech/
    format: html
publications:
  - id: doi:10.1093/gigascience/giag077
    title: "KG-Microbe: Building Modular and Scalable Knowledge Graphs for Microbiome and Microbial Sciences"
    authors:
      - Santangelo BE
      - Hegde H
      - Caufield JH
      - Reese J
      - Kliegr T
      - Hunter LE
      - Lozupone CA
      - Mungall CJ
      - Joachimiak MP
    journal: GigaScience
    year: "2026"
    doi: 10.1093/gigascience/giag077
  - id: doi:10.64898/2026.06.04.729985
    title: "MicroGrowAgents: An Agentic AI System for Microbial Cultivation Engineering"
    authors:
      - Naseem S
      - Miller MA
      - Martinez-Gomez NC
      - Sun N
      - Joachimiak MP
    journal: bioRxiv
    year: "2026"
    doi: 10.64898/2026.06.04.729985
cross_references:
  - target: dismech
    relation: follows_pattern_of
  - target: mediaingredientmech
    relation: provides_to
    description: Unmapped ingredient strings and occurrence counts become MediaIngredientMech's curation backlog.
  - target: mediaingredientmech
    relation: consumes
    description: Vendors MediaIngredientMech's ingredient-role enums and consumes its immutable label index.
  - target: communitymech
    relation: provides_to
    description: Community records cite the medium they were cultivated in by CultureMech id.
creation_date: 2026-09-10
last_modified_date: 2026-09-10
---
The two publications describe KG-Microbe and MicroGrowAgents, which CultureMech
feeds. Neither is a CultureMech paper.
