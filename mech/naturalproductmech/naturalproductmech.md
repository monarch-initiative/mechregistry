---
id: naturalproductmech
category: Mech
layout: mech_detail
name: NaturalProductMech
description: >-
  NaturalProductMech is a knowledge base of individual natural product structures. One
  record is one chemical structure made by a living organism, carrying who makes it, from
  which biosynthetic gene cluster, what it does, and the evidence for all three. MIBiG,
  ChEBI, LOTUS, CyanoMetDB, NPClassifier, PubChem BioAssay and BindingDB are harmonized
  onto one record per InChIKey. Every record is currently SEEDED. The biosynthetic pathway
  and causal graph fields are empty and are the work the rest exists for.
activity_status: active
maturity: seeded
repository: https://github.com/CultureBotAI/NaturalProductMech
schema_url: https://github.com/CultureBotAI/NaturalProductMech/blob/main/src/naturalproductmech/schema/naturalproductmech.yaml
collection:
  - x-mech-suite
domains:
  - chemistry and biochemistry
  - microbiology
  - pathways
record_type: a natural product chemical structure
record_count: 3115
record_count_date: 2026-09-10
record_identifier_policy: >-
  A ChEBI CURIE where the entry has a structure, otherwise a minted, content-hashed CURIE.
  A record with no InChIKey is never written.
identifier_prefix: naturalproductmech
ontologies:
  - CHEBI
  - NCBITaxon
  - MIBiG
  - NPAtlas
  - PubChem
  - UniProt
data_sources:
  - name: MIBiG
    url: https://mibig.secondarymetabolites.org/
    relation_type: prov:hadPrimarySource
    description: Structures, producer organisms and biosynthetic gene clusters.
  - name: ChEBI
    url: https://www.ebi.ac.uk/chebi/
    relation_type: prov:hadPrimarySource
    description: Grounding and biological origins.
  - name: LOTUS
    url: https://lotus.naturalproducts.net/
    relation_type: prov:hadPrimarySource
    description: Cited occurrences.
  - name: CyanoMetDB
    relation_type: prov:hadPrimarySource
    description: Cited occurrences for cyanobacterial metabolites.
  - name: NCBI Taxonomy
    url: https://www.ncbi.nlm.nih.gov/taxonomy
    relation_type: prov:used
    description: Name resolution for producers.
  - name: NPClassifier
    url: https://npclassifier.ucsd.edu/
    relation_type: prov:used
    description: The filing pathway for each structure.
  - name: PubChem BioAssay
    url: https://pubchem.ncbi.nlm.nih.gov/
    relation_type: prov:used
    description: Measured activities and targets.
  - name: BindingDB
    url: https://www.bindingdb.org/
    relation_type: prov:used
    description: Measured activities and targets.
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
  evidence_policy: >-
    Producer organisms carry biosynthesis-grade evidence. Occurrences are cited. The corpus
    reproduces offline from committed inventories.
  validation:
    - schema
    - ontology_terms
    - corpus_reproduction
  curation_history: true
features:
  - ontology_grounding
  - append_only_history
  - knowledge_gaps
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
  - id: naturalproductmech.records
    category: RecordCorpus
    name: Natural product records
    description: One YAML file per structure under data/natural_products/<pathway>/.
    product_url: https://github.com/CultureBotAI/NaturalProductMech/tree/main/data/natural_products
    format: yaml
  - id: naturalproductmech.schema
    category: DataModelProduct
    name: NaturalProductMech LinkML schema
    product_url: https://github.com/CultureBotAI/NaturalProductMech/blob/main/src/naturalproductmech/schema/naturalproductmech.yaml
    format: linkml
    compatibility:
      - linkml
      - mech_shared
cross_references:
  - target: dismech
    relation: follows_pattern_of
  - target: antibioticmech
    relation: consumes
    description: Antimicrobial classification and cross-corpus links come from AntibioticMech.
creation_date: 2026-09-10
last_modified_date: 2026-09-10
warnings:
  - No browser site is published yet. The GitHub repository is the only access point.
---
Not yet declared in the X-Mech fleet manifest as of 2026-09-10. It vendors the
governed artifacts one revision behind the other eight.
