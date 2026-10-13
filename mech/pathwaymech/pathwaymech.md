---
id: pathwaymech
category: Mech
layout: mech_detail
name: PathwayMech
description: >-
  PathwayMech is a knowledge base of pathway-level microbial mechanisms. One record is one
  pathway, held as a small graph: named participants, reactions, and causal edges between
  them, each edge citing a reference declared in the same record. It ports DisMech's
  evidence modules to pathways. Importers read GO-CAM, WikiPathways, Rhea, MetaCyc, KEGG,
  Reactome, BiGG and a dozen other pathway resources into draft records, and identifiers
  are checked against frozen authority snapshots.
activity_status: active
maturity: curating
homepage_url: https://culturebotai.github.io/PathwayMech/
repository: https://github.com/CultureBotAI/PathwayMech
schema_url: https://github.com/CultureBotAI/PathwayMech/blob/main/src/pathwaymech/schema/pathwaymech.yaml
collection:
  - x-mech-suite
domains:
  - pathways
  - microbiology
  - chemistry and biochemistry
record_type: a microbial pathway mechanism
record_count: 242
record_count_date: 2026-10-13
record_count_commit: 995b0ad9b19eaa3a46cc2898e73445cf0cce16db
record_count_source:
  path: data/pathways
  pattern: "*.yaml"
record_identifier_policy: >-
  The source pathway's CURIE, such as a WikiPathways or MetaCyc identifier, with an explicit
  prefix.
ontologies:
  - CHEBI
  - RHEA
  - UniProt
  - GO
  - RO
  - ECO
  - NCBITaxon
data_sources:
  - name: GO-CAM
    url: https://geneontology.org/docs/gocam-overview/
    relation_type: prov:hadPrimarySource
    description: Causal activity models imported as draft pathway records.
  - name: WikiPathways
    url: https://www.wikipathways.org/
    relation_type: prov:hadPrimarySource
    description: Pathway diagrams imported as draft records.
  - name: MetaCyc
    url: https://metacyc.org/
    relation_type: prov:hadPrimarySource
    description: Pathway definitions and reactions.
  - name: Rhea
    url: https://www.rhea-db.org/
    relation_type: prov:used
    description: Reaction identities and directions.
  - name: Reactome
    url: https://reactome.org/
    relation_type: prov:hadPrimarySource
    description: Pathways read from BioPAX.
  - name: KEGG
    url: https://www.kegg.jp/
    relation_type: prov:used
    description: Pathway maps read from KGML.
  - name: PubMed
    url: https://pubmed.ncbi.nlm.nih.gov/
    relation_type: prov:hadPrimarySource
    description: Evidence on mechanistic edges.
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
    Every mechanistic edge cites a reference declared in the record, and evidence quotes are
    kept short enough to review. Structured source assertions carry exact source locations
    and are shown apart from verbatim quotations.
  validation:
    - schema
    - ontology_terms
    - references
    - cross_field
  curation_history: true
features:
  - causal_mechanism_graphs
  - evidence_snippets
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
  - id: pathwaymech.records
    category: RecordCorpus
    name: Pathway records
    product_url: https://github.com/CultureBotAI/PathwayMech/tree/main/data/pathways
    format: yaml
  - id: pathwaymech.schema
    category: DataModelProduct
    name: PathwayMech LinkML schema
    product_url: https://github.com/CultureBotAI/PathwayMech/blob/main/src/pathwaymech/schema/pathwaymech.yaml
    format: linkml
    compatibility:
      - linkml
      - mech_shared
  - id: pathwaymech.browser
    category: GraphicalInterface
    name: PathwayMech browser
    product_url: https://culturebotai.github.io/PathwayMech/
    format: html
cross_references:
  - target: dismech
    relation: follows_pattern_of
    description: Ports DisMech's evidence modules into a pathway-specific schema.
  - target: traitmech
    relation: shares_vocabulary_with
    description: Inventories the UniProtKB proteins TraitMech, ProteinTraitsMech and other siblings hold, and the links they make to PathwayMech records.
creation_date: 2026-10-13
last_modified_date: 2026-10-13
---
Joined the X-Mech fleet manifest on 2026-09-28. Of 242 records, 99 carry a curation history
as of 2026-10-13.
