---
id: ai-gene-review
category: Mech
layout: mech_detail
name: ai-gene-review
description: >-
  ai-gene-review is an agent-curated knowledge base of Gene Ontology annotation reviews. One
  record per gene product: each record takes every existing GO annotation for the gene from
  GOA and gives it a review action (ACCEPT, MODIFY, REMOVE, MARK_AS_OVER_ANNOTATED,
  KEEP_AS_NON_CORE and others) with a reason and supporting evidence. The record also holds a
  standalone summary of the gene, its core functions as GO-CAM-like activities, proposed new
  GO terms, and suggested questions and experiments for experts. Reviews cover human, mouse,
  worm, yeast, fly, plant and many microbial gene products. Agents fetch the UniProt record,
  the GOA annotations and the cited publications, add deep research and bioinformatics, and
  write the review, which arrives by pull request. ai-gene-review is not strictly a Mech:
  each record reviews annotations that another resource holds, rather than being the
  canonical record for its gene. It keeps the Mech practices of a LinkML schema, ontology
  grounding, verbatim evidence and an append-only curation history.
activity_status: active
maturity: curating
homepage_url: https://ai4curation.github.io/ai-gene-review
repository: https://github.com/ai4curation/ai-gene-review
schema_url: https://github.com/ai4curation/ai-gene-review/blob/main/src/ai_gene_review/schema/gene_review.yaml
domains:
  - genomics
  - biological systems
  - pathways
  - organisms
record_type: a gene product and the review of its existing GO annotations
record_count: 6172
record_count_date: 2026-10-06
record_count_commit: 484ec6e0b95dfb08654501b92a390e1a334d72a8
record_count_source:
  path: genes
  pattern: "*-ai-review.yaml"
record_identifier_policy: >-
  Records are keyed by UniProtKB accession and named <GENE>-ai-review.yaml under
  genes/<organism>/<GENE>/. Organisms are a common name (human, mouse, worm, yeast) or a
  UniProt species code (ARATH, PSEPK). Gene symbols follow the nomenclature for the species.
ontologies:
  - GO
  - ECO
  - NCBITaxon
data_sources:
  - name: GOA
    url: https://www.ebi.ac.uk/QuickGO/
    relation_type: prov:hadPrimarySource
    description: >-
      The existing GO annotations under review, downloaded through the QuickGO API.
  - name: UniProtKB
    url: https://www.uniprot.org/
    relation_type: prov:hadPrimarySource
    description: The UniProt record for each gene product, which supplies the record identifier.
  - name: PubMed
    url: https://pubmed.ncbi.nlm.nih.gov/
    relation_type: prov:used
    description: >-
      Cited publications, cached as text so that supporting quotes can be checked.
  - name: Reactome
    url: https://reactome.org/
    relation_type: prov:used
    description: Cached Reactome entries used as pathway context.
  - name: GO-CAM
    url: https://geneontology.cloud/
    relation_type: prov:used
    description: Cached production GO-CAM models, indexed by gene product.
  - name: PANTHER
    url: https://www.pantherdb.org/
    relation_type: prov:used
    description: Protein family membership for family-level review and propagation.
license:
  id: https://opensource.org/licenses/BSD-3-Clause
  label: BSD 3-Clause License
  spdx_id: BSD-3-Clause
curation:
  agent_curated: true
  human_review: pull_request
  agents:
    - Claude Code
    - dragon-ai-agent
    - Codex
    - goose
  evidence_policy: >-
    Each review action carries a reason. Conclusive decisions on experimental annotations
    are expected to cite a PMID or DOI with supporting text quoted from the paper, and
    validation checks reference identifiers, titles and quotes against cached publication
    text. Ontology term identifiers are checked against their labels to catch fabricated
    terms.
  validation:
    - schema
    - ontology_terms
    - references
  curation_history: true
  curation_guide_url: https://github.com/ai4curation/ai-gene-review/blob/main/CLAUDE.md
features:
  - evidence_snippets
  - ontology_grounding
  - append_only_history
  - knowledge_gaps
  - static_browser
contacts:
  - category: Organization
    label: AI4Curation
    contact_details:
      - contact_type: github
        value: ai4curation
  - category: Individual
    label: Christopher J. Mungall
    orcid: 0000-0002-6601-2165
    contact_details:
      - contact_type: email
        value: cjmungall@lbl.gov
      - contact_type: github
        value: cmungall
products:
  - id: ai-gene-review.records
    category: RecordCorpus
    name: Gene reviews
    description: >-
      One <GENE>-ai-review.yaml file per gene product under genes/<organism>/<GENE>/, next to
      the UniProt record, GOA annotations, notes and deep research it was written from.
    product_url: https://github.com/ai4curation/ai-gene-review/tree/main/genes
    format: yaml
  - id: ai-gene-review.schema
    category: DataModelProduct
    name: Gene review LinkML schema
    product_url: https://github.com/ai4curation/ai-gene-review/blob/main/src/ai_gene_review/schema/gene_review.yaml
    format: linkml
    compatibility:
      - linkml
  - id: ai-gene-review.app
    category: GraphicalInterface
    name: Gene review browser
    description: >-
      A searchable browser of the reviews. Review pages take thumbs-up and thumbs-down votes
      on individual decisions.
    product_url: https://ai4curation.io/ai-gene-review/app/index.html
    format: html
  - id: ai-gene-review.annotations
    category: OtherProduct
    name: Exported annotations
    description: One row per reviewed annotation, with the review action, reason and supporting text.
    product_url: https://github.com/ai4curation/ai-gene-review/blob/main/exports/exported_annotations.csv
    format: csv
  - id: ai-gene-review.stats
    category: DocumentationProduct
    name: Statistics report
    product_url: https://ai4curation.io/ai-gene-review/docs/stats_report.html
    format: html
cross_references:
  - target: dismech
    relation: adopts_practice_of
    description: >-
      The history/ directory of append-only curation session records, with its schema,
      layout, scaffolder and validation, is ported from DisMech.
tags:
  - Mech-like
creation_date: 2026-10-06
last_modified_date: 2026-10-06
---

ai-gene-review is in the registry as a Mech-like resource. It shares the
Mech curation practices, but a record is a review of annotations held
elsewhere, in GOA, rather than the canonical record for its gene.

At commit 484ec6e on 2026-10-06, `genes/` held 6,172 reviews across 210
organism folders. Human has the most at 2,656, then *Pseudomonas putida*
KT2440 (PSEPK) at 955 and *Arabidopsis thaliana* at 257. The record count
takes only `*-ai-review.yaml` files. The same folders hold 644 other YAML
files, reviews of computational predictions and generated descriptions,
which are not counted. `history/` held 5,831 curation session records.

The repository also holds reviews of GO-CAM models, functional modules,
Pfam and InterPro entries, and GO mappings for Rhea, TCDB, CAZy and other
resources. These are outside the record count.

The repository LICENSE is BSD 3-Clause. Its copyright line still reads
"Copyright (c) 2025 My Name", the project template's placeholder.
