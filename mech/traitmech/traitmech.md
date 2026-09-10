---
id: traitmech
category: Mech
layout: mech_detail
name: TraitMech
description: >-
  TraitMech is a knowledge base of microbial ecophysiological traits, seeded from METPO, the
  Microbial Ecophysiological Trait and Phenotype Ontology, and curated incrementally. Each
  trait, such as Gram type, motility, pH optimum or halophily, lives in its own YAML file
  with provenance back to its METPO source class and, where curated, literature evidence and
  a causal mechanism graph. Chemicals, microbes and enzymes are not seeded here. They belong
  to MediaIngredientMech and CultureMech.
activity_status: active
maturity: reviewed
homepage_url: https://culturebotai.github.io/TraitMech/
repository: https://github.com/CultureBotAI/TraitMech
schema_url: https://github.com/CultureBotAI/TraitMech/blob/main/src/traitmech/schema/traitmech.yaml
collection:
  - x-mech-suite
  - kg-microbe
domains:
  - microbiology
  - phenotype
taxon:
  - NCBITaxon:2
  - NCBITaxon:2157
record_type: a microbial ecophysiological trait
record_count: 491
record_count_date: 2026-09-10
record_identifier_policy: Records are keyed by their METPO CURIE.
ontologies:
  - METPO
  - GO
  - NCBITaxon
  - CHEBI
  - UniProt
  - PATO
data_sources:
  - name: METPO
    url: https://w3id.org/metpo
    relation_type: prov:wasDerivedFrom
    description: The seed. Every trait record traces to a METPO class (METPO 2025-11-25).
  - name: PubMed
    url: https://pubmed.ncbi.nlm.nih.gov/
    relation_type: prov:used
    description: Evidence on causal graph edges.
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
    Every CausalEdge carries at least one EvidenceItem with a PMID or DOI. Records carry a
    curation status of SEEDED, PROPOSED, REVIEWED or DEPRECATED.
  validation:
    - schema
    - ontology_terms
    - references
  curation_history: true
features:
  - causal_mechanism_graphs
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
  - id: traitmech.records
    category: RecordCorpus
    name: Trait records
    description: One YAML file per trait under data/traits/<category>/<slug>.yaml.
    product_url: https://github.com/CultureBotAI/TraitMech/tree/main/data/traits
    format: yaml
  - id: traitmech.schema
    category: DataModelProduct
    name: TraitMech LinkML schema
    product_url: https://github.com/CultureBotAI/TraitMech/blob/main/src/traitmech/schema/traitmech.yaml
    format: linkml
    compatibility:
      - linkml
      - mech_shared
  - id: traitmech.browser
    category: GraphicalInterface
    name: TraitMech browser
    product_url: https://culturebotai.github.io/TraitMech/
    format: html
cross_references:
  - target: dismech
    relation: follows_pattern_of
  - target: proteintraitsmech
    relation: adopts_practice_of
    description: TraitMech adopted ProteinTraitsMech's licence-bearing download.yaml source catalogue, and a drift audit keeps shared trait tokens aligned.
  - target: mediaingredientmech
    relation: hands_off_to
    description: Chemicals are not seeded in TraitMech.
  - target: culturemech
    relation: hands_off_to
    description: Growth media are not seeded in TraitMech.
creation_date: 2026-09-10
last_modified_date: 2026-09-10
---
Of 491 record files, 427 are REVIEWED, 50 DEPRECATED and 14 PROPOSED as of the
README on 2026-09-10. 353 reviewed records carry causal graphs.
