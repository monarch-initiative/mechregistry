---
id: cmmmech
category: Mech
layout: mech_detail
name: CMMMech
description: >-
  CMMMech is a knowledge base of critical minerals and materials and the microbial
  mechanisms that extract, transform or recover them. One record is one material: an
  element, a mineral species, or a secondary resource such as spent batteries or smelter
  dust. A record carries its chemical or mineral identity, dated criticality designations
  (US and EU lists), and microbial mechanisms with explicit evidence boundaries, such as
  missing abiotic controls. Elements, minerals and impure experimental feeds are kept
  distinct, and no record inherits criticality it was not designated.
activity_status: active
maturity: curating
homepage_url: https://culturebotai.github.io/CMMMech/
repository: https://github.com/CultureBotAI/CMMMech
schema_url: https://github.com/CultureBotAI/CMMMech/blob/main/src/cmmmech/schema/cmmmech.yaml
collection:
  - x-mech-suite
domains:
  - microbiology
  - chemistry and biochemistry
  - environment
record_type: a critical mineral, element or secondary resource
record_count: 278
record_count_date: 2026-10-13
record_count_commit: 11a0b0f8e2714f1863304faf408da4ce0e7c5b53
record_count_source:
  path: data/records
  pattern: "*.yaml"
record_identifier_policy: A minted CURIE from the material name, such as cmmmech:cobalt, with ChEBI or IMA identifiers attached.
identifier_prefix: cmmmech
ontologies:
  - CHEBI
  - NCBITaxon
data_sources:
  - name: ChEBI
    url: https://www.ebi.ac.uk/chebi/
    relation_type: prov:used
    description: Chemical identity of elements and compounds.
  - name: USGS List of Critical Minerals
    url: https://www.usgs.gov/
    relation_type: prov:hadPrimarySource
    description: Dated US criticality designations.
  - name: EU Critical Raw Materials Act
    url: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1252
    relation_type: prov:hadPrimarySource
    description: Dated EU criticality designations.
  - name: IMA mineral list
    url: https://cnmnc.units.it/
    relation_type: prov:used
    description: Mineral species identity.
  - name: PubMed
    url: https://pubmed.ncbi.nlm.nih.gov/
    relation_type: prov:hadPrimarySource
    description: Evidence on microbial mechanisms.
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
    Each record has a timestamped scientific review. Every microbial mechanism states its
    evidence boundary: what the cited experiment does not establish, such as matched abiotic
    controls or an isolated product yield.
  validation:
    - schema
    - references
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
  - id: cmmmech.records
    category: RecordCorpus
    name: Material records
    product_url: https://github.com/CultureBotAI/CMMMech/tree/main/data/records
    format: yaml
  - id: cmmmech.schema
    category: DataModelProduct
    name: CMMMech LinkML schema
    product_url: https://github.com/CultureBotAI/CMMMech/blob/main/src/cmmmech/schema/cmmmech.yaml
    format: linkml
    compatibility:
      - linkml
      - mech_shared
  - id: cmmmech.browser
    category: GraphicalInterface
    name: CMMMech browser
    product_url: https://culturebotai.github.io/CMMMech/
    format: html
cross_references:
  - target: dismech
    relation: follows_pattern_of
creation_date: 2026-10-13
last_modified_date: 2026-10-13
---
Joined the X-Mech fleet manifest in October 2026. Of 278 records, 216 carry at least one
microbial mechanism as of 2026-10-13.
