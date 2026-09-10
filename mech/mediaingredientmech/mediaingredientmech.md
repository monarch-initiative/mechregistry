---
id: mediaingredientmech
category: Mech
layout: mech_detail
name: MediaIngredientMech
synonyms:
  - MIM
description: >-
  MediaIngredientMech is an LLM-assisted curation system for culture-media ingredient
  ontology mappings, with full audit trails. It manages the ingredient records aggregated
  from media recipes in CultureMech and owns ingredient identity for the X-Mech fleet. An
  ingredient record denotes a specific chemical someone can order. Where sources disagree
  about which form a recipe means, the record picks one by convention, preferring the term
  that carries the commercial CAS number, and keeps every raw form as a resolvable synonym.
activity_status: active
maturity: curating
homepage_url: https://culturebotai.github.io/MediaIngredientMech/
repository: https://github.com/CultureBotAI/MediaIngredientMech
schema_url: https://github.com/CultureBotAI/MediaIngredientMech/blob/main/src/mediaingredientmech/schema/mediaingredientmech.yaml
collection:
  - x-mech-suite
  - kg-microbe
domains:
  - chemistry and biochemistry
  - nutrition
  - microbiology
record_type: a culture-media ingredient
record_count: 2954
record_count_date: 2026-09-10
ontologies:
  - CHEBI
  - CAS
  - NCIT
  - FOODON
  - ENVO
  - MESH
data_sources:
  - name: CultureMech
    url: https://github.com/CultureBotAI/CultureMech
    relation_type: prov:wasDerivedFrom
    description: Unmapped ingredient strings and occurrence counts from recipes become the curation backlog.
  - name: ChEBI
    url: https://www.ebi.ac.uk/chebi/
    relation_type: prov:used
    description: Primary mapping target for chemical ingredients.
  - name: FOODON
    url: https://foodon.org/
    relation_type: prov:used
    description: Mapping target for complex and food-derived ingredients.
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
    Every mapping carries a MappingEvidence record and every curation action carries an
    event noting whether an LLM assisted.
  validation:
    - schema
    - ontology_terms
    - cross_field
  curation_history: true
  curation_guide_url: https://github.com/CultureBotAI/MediaIngredientMech/blob/main/MAPPING_SEMANTICS.md
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
  - id: mediaingredientmech.records
    category: RecordCorpus
    name: Ingredient records
    description: Mapped and unmapped ingredient records under data/ingredients/.
    product_url: https://github.com/CultureBotAI/MediaIngredientMech/tree/main/data/ingredients
    format: yaml
  - id: mediaingredientmech.schema
    category: DataModelProduct
    name: MediaIngredientMech LinkML schema
    product_url: https://github.com/CultureBotAI/MediaIngredientMech/blob/main/src/mediaingredientmech/schema/mediaingredientmech.yaml
    format: linkml
    compatibility:
      - linkml
      - mech_shared
  - id: mediaingredientmech.sssom
    category: MappingProduct
    name: Ingredient mappings (SSSOM)
    description: Ingredient to ontology mappings exported as SSSOM.
    product_url: https://github.com/CultureBotAI/MediaIngredientMech
    format: sssom
    compatibility:
      - sssom
  - id: mediaingredientmech.browser
    category: GraphicalInterface
    name: MediaIngredientMech browser
    product_url: https://culturebotai.github.io/MediaIngredientMech/
    format: html
cross_references:
  - target: dismech
    relation: follows_pattern_of
  - target: culturemech
    relation: consumes
    description: Unmapped ingredient strings and occurrence counts become the curation backlog. Records link back to recipes by stable id with the CultureMechReference class.
  - target: culturemech
    relation: provides_to
    description: Curated ChEBI and FOODON mappings sync back to recipes. CultureMech vendors the ingredient-role enums and consumes the immutable label index.
creation_date: 2026-09-10
last_modified_date: 2026-09-10
warnings:
  - The repository carries no LICENSE file as of 2026-09-10. The CC0 license recorded here is the one the X-Mech suite page states for the fleet.
---
The record count is the sum of the mapped and unmapped ingredient YAML files
in the repository on 2026-09-10.
