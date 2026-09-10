---
id: dismech
category: Mech
layout: mech_detail
name: DisMech
synonyms:
  - Disorder Mechanisms Knowledge Base
  - Disease Mechanisms KB
description: >-
  DisMech, the Disorder Mechanisms Knowledge Base, is a structured, evidence-backed
  knowledge base of disease pathophysiology. It records how diseases work: the cell types,
  biological processes and causal chains that link a genetic or environmental cause to its
  clinical phenotypes. Every claim carries a citation with a verbatim quote that is checked
  against the source. Each disorder is one YAML file holding pathophysiology, phenotypes,
  genetics, treatments, evidence and ontology term bindings. Conserved pathological
  processes are factored into mechanism modules that disorders declare conformance to.
  DisMech is the canonical Mech: the other Mechs in this registry adopt its curation pattern.
activity_status: active
maturity: curating
version: v0.1.39
homepage_url: https://dismech.monarchinitiative.org/
repository: https://github.com/monarch-initiative/dismech
schema_url: https://github.com/monarch-initiative/dismech/blob/main/src/dismech/schema/dismech.yaml
collection:
  - monarch
domains:
  - biomedical
  - clinical
  - phenotype
  - pathways
  - genomics
taxon:
  - NCBITaxon:9606
record_type: a human disorder or disorder subtype
record_count: 2864
record_count_date: 2026-09-10
record_identifier_policy: >-
  Records are named by disorder and bound to Mondo disease identifiers where a term exists.
ontologies:
  - MONDO
  - HP
  - GO
  - CL
  - UBERON
  - NCIT
  - CHEBI
  - GENO
  - PATO
  - ECTO
  - ENVO
data_sources:
  - name: PubMed
    url: https://pubmed.ncbi.nlm.nih.gov/
    relation_type: prov:hadPrimarySource
    description: Evidence snippets are verbatim quotes from PubMed abstracts, checked at validation time.
  - name: ClinGen
    url: https://clinicalgenome.org/
    relation_type: prov:used
    description: Gene-disease validity used for genetic factors.
  - name: BioModels
    url: https://www.ebi.ac.uk/biomodels/
    relation_type: prov:used
    description: Source of quantitative models attached to disorders.
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
    - dragon-ai-agent
    - goose
  evidence_policy: >-
    Every pathophysiological claim cites a PubMed reference with an exact quote from the
    abstract. The reference validator fetches the abstract and checks that the quote appears
    verbatim. Paraphrases, wrong PMIDs and fabricated citations fail validation.
  validation:
    - schema
    - ontology_terms
    - references
    - compliance
  curation_history: true
  curation_guide_url: https://dismech.monarchinitiative.org/
features:
  - causal_mechanism_graphs
  - evidence_snippets
  - ontology_grounding
  - append_only_history
  - knowledge_gaps
  - mechanism_modules
  - static_browser
  - embeddings_explorer
  - computational_models
disclaimer: >-
  DisMech is AI-curated and AI-maintained. Most content is generated and maintained by AI
  curation agents, with human review as the pull-request gate. Automated validation
  guarantees that citations exist, quoted snippets are exact, and ontology terms are real. It
  does not guarantee scientific correctness. DisMech is not medical advice. If you have a
  health concern, consult a qualified healthcare professional.
contacts:
  - category: Organization
    label: Monarch Initiative
    contact_details:
      - contact_type: url
        value: https://monarchinitiative.org
      - contact_type: github
        value: monarch-initiative
  - category: Individual
    label: Christopher J. Mungall
    orcid: 0000-0002-6601-2165
    contact_details:
      - contact_type: github
        value: cmungall
  - category: Individual
    label: J. Harry Caufield
    orcid: 0000-0001-5705-7831
    contact_details:
      - contact_type: email
        value: jhc@lbl.gov
      - contact_type: github
        value: caufieldjh
products:
  - id: dismech.records
    category: RecordCorpus
    name: Disorder records
    description: One YAML file per disorder in kb/disorders, validated against the DisMech LinkML schema.
    product_url: https://github.com/monarch-initiative/dismech/tree/main/kb/disorders
    format: yaml
  - id: dismech.modules
    category: RecordCorpus
    name: Mechanism modules
    description: Conserved pathological patterns, such as the fibrotic response, that disorders declare conformance to.
    product_url: https://github.com/monarch-initiative/dismech/tree/main/kb/modules
    format: yaml
  - id: dismech.schema
    category: DataModelProduct
    name: DisMech LinkML schema
    product_url: https://github.com/monarch-initiative/dismech/blob/main/src/dismech/schema/dismech.yaml
    format: linkml
    compatibility:
      - linkml
  - id: dismech.browser
    category: GraphicalInterface
    name: Disorder browser
    description: Searchable browser over every disorder, with pathographs, mechanism modules, trajectories and an embeddings explorer.
    product_url: https://dismech.monarchinitiative.org/app/
    format: html
  - id: dismech.docs
    category: DocumentationProduct
    name: DisMech documentation
    product_url: https://dismech.monarchinitiative.org/
    format: html
  - id: dismech.models
    category: ModelProduct
    name: Computational models
    description: Metabolic, kinetic, Boolean and agent-based models attached to disorders, in SBML and Antimony.
    product_url: https://github.com/monarch-initiative/dismech/tree/main/models
    format: sbml
publications:
  - id: https://zenodo.org/records/18720444
    title: "Unlocking Disease Mechanisms: Agentic AI for Clinical Knowledge"
    year: "2026"
cross_references: []
creation_date: 2026-09-10
last_modified_date: 2026-09-10
---
DisMech is the reference implementation of the Mech pattern. The X-Mech suite
vendors two of its record sections, Discussion and Dataset, through the shared
`mech_shared.yaml` module.
