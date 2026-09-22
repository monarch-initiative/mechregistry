---
id: somamech
category: Mech
layout: mech_detail
name: SOMAMech
description: >-
  SOMAMech is a paper-extraction knowledge base for environmental health sciences. It
  curates publications on PM2.5, smoke and other inhaled exposures and their effects on
  airway biology into data that validate against the SOMA LinkML schema. One record per
  publication: each record is a Container that holds the paper's study subjects, exposures,
  protocols, assays and measurements, linked to Key Events and Adverse Outcome Pathways.
  Assay classes cover ciliary function, airway surface liquid, mucociliary clearance,
  oxidative stress, CFTR ion transport, EGFR signaling, mucin and goblet cell biology,
  inflammatory markers in BALF and sputum, lung function and gene expression. Every
  extracted measurement carries an evidence block that quotes the paper, and the quote is
  checked against the paper text. Papers enter through a stub queue, are claimed one at a
  time by GitHub issue, and arrive by pull request. SOMAMech follows the DisMech curation
  pattern.
activity_status: active
maturity: seeded
homepage_url: https://github.com/EHS-Data-Standards/somamech
repository: https://github.com/EHS-Data-Standards/somamech
schema_url: https://github.com/EHS-Data-Standards/somamech/blob/main/src/soma/schema/soma.yaml
domains:
  - environment
  - biomedical
  - phenotype
  - biological systems
taxon:
  - NCBITaxon:9606
  - NCBITaxon:10090
record_type: a publication, extracted into its assays, measurements and Key Events
record_count: 0
record_count_date: 2026-09-22
record_identifier_policy: >-
  Records are named Container-<author><year>.yaml and name their source paper by PMID in
  source_publication. KeyEvent identifiers are shared across papers. Every other entity
  identifier belongs to exactly one paper.
ontologies:
  - CHEBI
  - GO
  - CL
  - UBERON
  - HP
  - PATO
  - ENVO
  - MONDO
  - NCBITaxon
  - OBI
  - UO
  - PR
  - CLO
  - ECTO
  - ExO
  - XCO
data_sources:
  - name: PubMed
    url: https://pubmed.ncbi.nlm.nih.gov/
    relation_type: prov:hadPrimarySource
    description: >-
      The extracted publications. Evidence quotes are checked against cached abstracts and
      full text.
  - name: Zotero library
    relation_type: prov:used
    description: >-
      The seed corpus of papers and PDFs, resolved to PMIDs and DOIs in corpus.csv and
      turned into queue stubs.
  - name: SOMA
    url: https://github.com/EHS-Data-Standards/soma
    relation_type: prov:used
    description: The SOMA data model for Key Event and outcome assays, vendored as the schema.
license:
  id: https://opensource.org/licenses/MIT
  label: MIT License
  spdx_id: MIT
curation:
  agent_curated: true
  human_review: pull_request
  agents:
    - Claude Code
  evidence_policy: >-
    Every extracted measurement carries an evidence block that quotes the paper verbatim.
    Quotes are checked against the cached paper text. Where only the abstract can be cached,
    a local check against the full text writes a hash-bound verification receipt, and CI
    rejects any quote without one.
  validation:
    - schema
    - ontology_terms
    - references
  curation_history: false
features:
  - evidence_snippets
  - ontology_grounding
contacts:
  - category: Organization
    label: EHS-Data-Standards
    contact_details:
      - contact_type: github
        value: EHS-Data-Standards
  - category: Individual
    label: Sierra Moxon
    orcid: 0000-0002-8719-7760
    contact_details:
      - contact_type: email
        value: smoxon@lbl.gov
      - contact_type: github
        value: sierra-moxon
products:
  - id: somamech.records
    category: RecordCorpus
    name: Publication extractions
    description: One Container YAML file per extracted publication under kb/publications/.
    product_url: https://github.com/EHS-Data-Standards/somamech/tree/main/kb/publications
    format: yaml
  - id: somamech.schema
    category: DataModelProduct
    name: SOMA LinkML schema
    product_url: https://github.com/EHS-Data-Standards/somamech/blob/main/src/soma/schema/soma.yaml
    format: linkml
    compatibility:
      - linkml
  - id: somamech.queue
    category: OtherProduct
    name: Paper queue
    description: >-
      One stub per candidate paper, with screening status and decision. Stubs are the
      extraction queue and are not records.
    product_url: https://github.com/EHS-Data-Standards/somamech/tree/main/stubs
    format: yaml
cross_references:
  - target: dismech
    relation: follows_pattern_of
creation_date: 2026-09-22
last_modified_date: 2026-09-22
---

SOMAMech is new. The repository was created on 2026-09-17. At commit 2e32037
on 2026-09-22, `kb/publications/` held no records. The record count is 0 for
that reason. 137 paper stubs sat in the queue and 26 extraction pull requests
were open. The maturity is `seeded` because nothing has been merged
yet. It will move to `curating` once extractions land.

The Mech has no browser site yet. The homepage is the repository. The SOMA
documentation at https://ehs-data-standards.github.io/soma/ describes the
schema and not this corpus. A pooled Excel workbook is planned as a rolling
`workbook-latest` release and did not exist on 2026-09-22.

The code and records are under the MIT License, as the repository LICENSE
states.
