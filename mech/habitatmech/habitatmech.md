---
id: habitatmech
category: Mech
layout: mech_detail
name: HabitatMech
description: >-
  HabitatMech is a knowledge base of microbial habitats and environments. Four source
  vocabularies that describe where microbes are found, JGI GOLD ecosystem paths, BacDive
  isolation sources, PREGO ontology annotations and the Madin et al. literature curation,
  are harmonized into records grounded in ENVO, UBERON, FOODON and BTO. Each source term
  becomes a source concept, each concept resolves to an identifier, and concepts that resolve
  to the same identifier merge into one record that keeps every source's attestation.
activity_status: active
maturity: curating
homepage_url: https://culturebotai.github.io/HabitatMech/
repository: https://github.com/CultureBotAI/HabitatMech
schema_url: https://github.com/CultureBotAI/HabitatMech/blob/main/src/habitatmech/schema/habitatmech.yaml
collection:
  - x-mech-suite
  - kg-microbe
domains:
  - microbiology
  - environment
taxon:
  - NCBITaxon:2
  - NCBITaxon:2157
record_type: a microbial habitat or environment
record_count: 3205
record_count_date: 2026-09-10
record_identifier_policy: >-
  An ontology CURIE where one is defensible, otherwise a minted, content-hashed CURIE that
  can be re-grounded later.
identifier_prefix: habitatmech
ontologies:
  - ENVO
  - UBERON
  - FOODON
  - BTO
  - NCBITaxon
data_sources:
  - name: JGI GOLD
    url: https://gold.jgi.doe.gov/
    relation_type: prov:hadPrimarySource
    description: Five-level ecosystem classification paths.
  - name: BacDive
    url: https://bacdive.dsmz.de/
    relation_type: prov:hadPrimarySource
    description: Flat isolation-source labels.
  - name: PREGO
    url: https://prego.hcmr.gr/
    relation_type: prov:hadPrimarySource
    description: ENVO-annotated organism-environment associations.
  - name: Madin et al. trait database
    url: https://github.com/bacteria-archaea-traits/bacteria-archaea-traits
    relation_type: prov:hadPrimarySource
    description: Literature-curated habitat assignments.
  - name: KG-Microbe
    url: https://kghub.org/kg-microbe/
    relation_type: prov:used
    description: Environmental parameters attached to records.
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
    Records keep each source's attestation and assertion volume. Causal graphs carry
    evidence items with PMIDs or DOIs on every edge.
  validation:
    - schema
    - ontology_terms
    - references
    - corpus_reproduction
  curation_history: true
  curation_guide_url: https://github.com/CultureBotAI/HabitatMech/blob/main/docs/CURATION.md
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
      - contact_type: url
        value: https://culturebotai.github.io/
  - category: Individual
    label: Marcin P. Joachimiak
    orcid: 0000-0001-8175-045X
    contact_details:
      - contact_type: email
        value: mjoachimiak@lbl.gov
      - contact_type: github
        value: realmarcin
products:
  - id: habitatmech.records
    category: RecordCorpus
    name: Habitat records
    description: One YAML file per habitat, filed by category (host-associated, engineered, aquatic, terrestrial, food, air, clinical, other).
    product_url: https://github.com/CultureBotAI/HabitatMech/tree/main/data/habitats
    format: yaml
  - id: habitatmech.schema
    category: DataModelProduct
    name: HabitatMech LinkML schema
    product_url: https://github.com/CultureBotAI/HabitatMech/blob/main/src/habitatmech/schema/habitatmech.yaml
    format: linkml
    compatibility:
      - linkml
      - mech_shared
  - id: habitatmech.browser
    category: GraphicalInterface
    name: HabitatMech browser
    description: Every record by category, plus the ENVO term requests the project is asking the ontology community for.
    product_url: https://culturebotai.github.io/HabitatMech/
    format: html
cross_references:
  - target: dismech
    relation: follows_pattern_of
  - target: traitmech
    relation: shares_vocabulary_with
    description: Habitat causal graphs use a superset of TraitMech's node vocabulary, so a node may be a TraitMech or METPO trait.
  - target: culturemech
    relation: hands_off_to
    description: The one overlapping concept, BTO:0000316 culture medium, is handed to CultureMech rather than curated twice.
creation_date: 2026-09-10
last_modified_date: 2026-09-10
---
Joined the X-Mech fleet manifest on 2026-09-07.
