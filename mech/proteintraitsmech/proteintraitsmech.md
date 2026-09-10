---
id: proteintraitsmech
category: Mech
layout: mech_detail
name: ProteinTraitsMech
synonyms:
  - ProteinTraits
description: >-
  ProteinTraitsMech is a knowledge base of protein sequence, structure, function and
  evolution traits, one YAML record per trait with optional evidence-backed causal graphs.
  Traits run along five axes: sequence (motifs, signal peptides, disordered regions,
  repeats, PTM sites), structure (folds, domains, sites, interfaces, symmetry), mixed
  sequence-structure (transmembrane spans, coiled coils), function (enzymatic activity,
  binding, cofactors, localisation) and evolution (conservation and pangenome partition).
  Records anchor to InterPro, Pfam, PROSITE, SMART, MEROPS, CATH, SCOP, PDB, GO, PR and
  UniProtKB.
activity_status: active
maturity: seeded
homepage_url: https://culturebotai.github.io/proteintraitsmech/
repository: https://github.com/CultureBotAI/proteintraitsmech
schema_url: https://github.com/CultureBotAI/proteintraitsmech/blob/main/src/proteintraitsmech/schema/proteintraitsmech.yaml
collection:
  - x-mech-suite
  - kg-microbe
domains:
  - biological systems
  - chemistry and biochemistry
  - genomics
record_type: a protein sequence, structure, function or evolution trait class
record_count: 429271
record_count_date: 2026-09-10
record_identifier_policy: >-
  Preferably an existing InterPro, Pfam, PROSITE, CATH, SCOP, MEROPS or PR CURIE.
ontologies:
  - InterPro
  - Pfam
  - UniProt
  - Rhea
  - GO
  - CHEBI
  - ARO
  - EC
  - CATH
  - SCOP
  - PDB
  - PR
data_sources:
  - name: InterPro
    url: https://www.ebi.ac.uk/interpro/
    relation_type: prov:wasDerivedFrom
  - name: Pfam
    url: https://www.ebi.ac.uk/interpro/entry/pfam/
    relation_type: prov:wasDerivedFrom
  - name: Rhea
    url: https://www.rhea-db.org/
    relation_type: prov:wasDerivedFrom
  - name: CATH
    url: https://www.cathdb.info/
    relation_type: prov:wasDerivedFrom
  - name: SCOPe
    url: https://scop.berkeley.edu/
    relation_type: prov:wasDerivedFrom
  - name: CARD
    url: https://card.mcmaster.ca/
    relation_type: prov:wasDerivedFrom
  - name: UniProtKB
    url: https://www.uniprot.org/
    relation_type: prov:used
    description: Release-pinned canonical example proteins and grounding assertions.
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
    Every CausalEdge must carry at least one EvidenceItem. Sources are catalogued with
    their licences in a download.yaml before ingestion.
  validation:
    - schema
    - ontology_terms
    - corpus_reproduction
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
  - id: proteintraitsmech.records
    category: RecordCorpus
    name: Protein trait records
    description: One YAML file per trait under data/traits/<axis>/<category>/<slug>.yaml.
    product_url: https://github.com/CultureBotAI/proteintraitsmech/tree/main/data/traits
    format: yaml
  - id: proteintraitsmech.schema
    category: DataModelProduct
    name: ProteinTraitsMech LinkML schema
    product_url: https://github.com/CultureBotAI/proteintraitsmech/blob/main/src/proteintraitsmech/schema/proteintraitsmech.yaml
    format: linkml
    compatibility:
      - linkml
      - mech_shared
  - id: proteintraitsmech.browser
    category: GraphicalInterface
    name: ProteinTraitsMech browser
    product_url: https://culturebotai.github.io/proteintraitsmech/
    format: html
cross_references:
  - target: dismech
    relation: follows_pattern_of
  - target: traitmech
    relation: sibling_of
    description: TraitMech holds organism-level ecophysiological traits. ProteinTraitsMech holds the protein-level machinery.
creation_date: 2026-09-10
last_modified_date: 2026-09-10
---
The record count is the figure published on the X-Mech suite page on 2026-09-10.
The repository is too large to count from the GitHub tree API.
