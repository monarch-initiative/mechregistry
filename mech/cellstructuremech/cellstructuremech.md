---
id: cellstructuremech
category: Mech
layout: mech_detail
name: CellStructureMech
description: >-
  CellStructureMech is a knowledge base of microbial cell structures: organelles, envelope
  layers, appendages, microcompartments, inclusions, cytoskeletal systems and the
  multi-protein complexes that build them. One record is a structure you could point to in
  a micrograph, from a whole organelle down to a discrete complex such as the flagellar
  motor. A record holds components with stoichiometry and UniProt examples, taxonomic
  distribution, GO functions with evidence, the TraitMech phenotypes it confers, and causal
  graphs of assembly, operation and regulation with every edge cited. It fills the layer
  between a phenotype in TraitMech and a protein in ProteinTraitsMech.
activity_status: active
maturity: curating
homepage_url: https://culturebotai.github.io/CellStructureMech/
repository: https://github.com/CultureBotAI/CellStructureMech
schema_url: https://github.com/CultureBotAI/CellStructureMech/blob/main/src/cellstructuremech/schema/cellstructuremech.yaml
collection:
  - x-mech-suite
  - kg-microbe
domains:
  - microbiology
  - biological systems
  - anatomy and development
taxon:
  - NCBITaxon:2
  - NCBITaxon:2157
record_type: a microbial cell structure or multi-protein complex
record_count: 92
record_count_date: 2026-09-10
record_identifier_policy: A GO cellular component CURIE where one exists, otherwise a minted CURIE.
ontologies:
  - GO
  - NCBITaxon
  - UniProt
  - METPO
  - Pfam
  - PDB
data_sources:
  - name: UniProtKB
    url: https://www.uniprot.org/
    relation_type: prov:used
    description: Taxon-paired protein examples for components.
  - name: PubMed
    url: https://pubmed.ncbi.nlm.nih.gov/
    relation_type: prov:hadPrimarySource
    description: Evidence on functions and on causal graph edges.
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
    Every causal graph edge and every function claim carries a citation. Candidate sources
    are ranked in a source queue and their licences verified before ingestion.
  validation:
    - schema
    - ontology_terms
    - references
    - corpus_reproduction
  curation_history: true
  curation_guide_url: https://github.com/CultureBotAI/CellStructureMech/blob/main/docs/CURATION.md
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
  - id: cellstructuremech.records
    category: RecordCorpus
    name: Structure records
    product_url: https://github.com/CultureBotAI/CellStructureMech/tree/main/data/structures
    format: yaml
  - id: cellstructuremech.schema
    category: DataModelProduct
    name: CellStructureMech LinkML schema
    product_url: https://github.com/CultureBotAI/CellStructureMech/blob/main/src/cellstructuremech/schema/cellstructuremech.yaml
    format: linkml
    compatibility:
      - linkml
      - mech_shared
  - id: cellstructuremech.browser
    category: GraphicalInterface
    name: CellStructureMech browser
    description: Every record by category, with components, distribution, functions and mechanism graphs, plus a text embedding map with nearest neighbours.
    product_url: https://culturebotai.github.io/CellStructureMech/
    format: html
cross_references:
  - target: dismech
    relation: follows_pattern_of
  - target: traitmech
    relation: consumes
    description: A structure lists the phenotypes it confers as TraitMech or METPO terms, and its causal-graph node vocabulary is TraitMech's plus a STRUCTURE node type.
  - target: proteintraitsmech
    relation: hands_off_to
    description: A single protein is a component of a structure, never a record of its own. It grounds to InterPro or UniProtKB and hands off to ProteinTraitsMech.
  - target: antibioticmech
    relation: adopts_practice_of
    description: Adapted AntibioticMech's licensed source-queue pattern.
creation_date: 2026-09-10
last_modified_date: 2026-09-10
---
All 92 records carry the PROPOSED status as of the README on 2026-09-10.
