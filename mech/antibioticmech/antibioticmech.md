---
id: antibioticmech
category: Mech
layout: mech_detail
name: AntibioticMech
description: >-
  AntibioticMech is a knowledge base of individual chemical structures with antimicrobial
  activity, harmonized from ChEBI and CARD's Antibiotic Resistance Ontology. One record is
  one chemical structure, keyed by its ChEBI identifier and carrying SMILES, InChI and
  InChIKey. A class such as macrolide antibiotic is not a record. It is a structural_class
  on the records it covers. Each record carries what the compound hits, how microbes resist
  it, and the evidence for both.
activity_status: active
maturity: curating
homepage_url: https://culturebotai.github.io/AntibioticMech/
repository: https://github.com/CultureBotAI/AntibioticMech
schema_url: https://github.com/CultureBotAI/AntibioticMech/blob/main/src/antibioticmech/schema/antibioticmech.yaml
collection:
  - x-mech-suite
  - kg-microbe
domains:
  - chemistry and biochemistry
  - pharmacology
  - microbiology
record_type: an antimicrobial chemical structure
record_count: 2934
record_count_date: 2026-09-10
record_identifier_policy: >-
  A ChEBI CURIE where the entry has a structure, otherwise a minted, content-hashed CURIE.
  A record with no InChIKey is never written.
identifier_prefix: antibioticmech
ontologies:
  - CHEBI
  - ARO
  - CAS
  - PubChem
  - DrugBank
  - NCBITaxon
data_sources:
  - name: ChEBI
    url: https://www.ebi.ac.uk/chebi/
    relation_type: prov:hadPrimarySource
    description: Structures, definitions and antimicrobial class terms.
  - name: CARD
    url: https://card.mcmaster.ca/
    relation_type: prov:hadPrimarySource
    description: Antibiotic Resistance Ontology classification, molecular targets and resistance determinants.
  - name: PubChem
    url: https://pubchem.ncbi.nlm.nih.gov/
    relation_type: prov:used
    description: The structures CARD's cross-references point at.
license:
  id: https://creativecommons.org/licenses/by/4.0/
  label: CC BY 4.0
  spdx_id: CC-BY-4.0
code_license:
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
    Targets and resistance determinants carry evidence. Candidate sources are ranked in a
    source queue and their licences verified and recorded before ingestion.
  validation:
    - schema
    - ontology_terms
    - references
    - corpus_reproduction
  curation_history: true
features:
  - causal_mechanism_graphs
  - ontology_grounding
  - append_only_history
  - knowledge_gaps
  - static_browser
  - embeddings_explorer
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
  - id: antibioticmech.records
    category: RecordCorpus
    name: Antibiotic records
    description: One YAML file per structure under data/antibiotics/<class>/.
    product_url: https://github.com/CultureBotAI/AntibioticMech/tree/main/data/antibiotics
    format: yaml
  - id: antibioticmech.schema
    category: DataModelProduct
    name: AntibioticMech LinkML schema
    product_url: https://github.com/CultureBotAI/AntibioticMech/blob/main/src/antibioticmech/schema/antibioticmech.yaml
    format: linkml
    compatibility:
      - linkml
      - mech_shared
  - id: antibioticmech.browser
    category: GraphicalInterface
    name: AntibioticMech browser
    description: Every record by antimicrobial class, with structures, sources, CARD targets and resistance determinants.
    product_url: https://culturebotai.github.io/AntibioticMech/
    format: html
cross_references:
  - target: dismech
    relation: follows_pattern_of
  - target: naturalproductmech
    relation: provides_to
    description: Supplies antimicrobial classification and cross-corpus links.
  - target: cellstructuremech
    relation: provides_to
    description: Wrote the licensed source-queue pattern that CellStructureMech adapted.
creation_date: 2026-09-10
last_modified_date: 2026-09-10
---
