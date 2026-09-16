---
id: taxonmech
category: Mech
layout: mech_detail
name: TaxonMech
description: >-
  TaxonMech is a knowledge base of microbial taxa and the strains behind them. One record
  per taxon, keyed by NCBI Taxonomy and harmonized with GTDB, LPSN, BacDive, MediaDive,
  GOLD, Madin et al. and BactoTraits through the kg-microbe transforms. Records are species
  and below. Higher taxa appear only in a record's lineage. Each record keeps every source's
  own identifier, mapping predicate and assertion count, the LPSN nomenclature with type
  strain designations, the GTDB species mapping with its genome count, and the BacDive
  strains with their culture-collection deposits. A primary focus is linking strain
  identifiers to genome identifiers: NCBI GenBank and RefSeq assemblies first, then GTDB,
  BV-BRC, IMG and AllTheBacteria records, each link carrying the source record that asserts
  it. Phenotypes, media and isolation sources are left to TraitMech, CultureMech and
  HabitatMech.
activity_status: active
maturity: seeded
homepage_url: https://culturebotai.github.io/TaxonMech/
repository: https://github.com/CultureBotAI/TaxonMech
schema_url: https://github.com/CultureBotAI/TaxonMech/blob/main/src/taxonmech/schema/taxonmech.yaml
collection:
  - x-mech-suite
  - kg-microbe
domains:
  - microbiology
  - organisms
  - genomics
taxon:
  - NCBITaxon:2
  - NCBITaxon:2157
record_type: a microbial taxon at species rank or below
record_count: 625960
record_count_date: 2026-09-16
record_identifier_policy: >-
  Records are keyed by their NCBITaxon CURIE. Filenames are pinned by data/taxa/PATHS.tsv so
  a re-seed never renames an existing record.
ontologies:
  - NCBITaxon
  - GTDB
  - BacDive
  - GOLD
  - insdc.gca
  - refseq
  - biosample
  - bioproject
  - img.taxon
  - brc.genome
data_sources:
  - name: NCBI Taxonomy
    url: https://www.ncbi.nlm.nih.gov/taxonomy
    relation_type: prov:hadPrimarySource
    description: The identity of every record, its rank and its lineage, from a pinned snapshot.
  - name: GTDB
    url: https://gtdb.ecogenomic.org/
    relation_type: prov:wasDerivedFrom
    description: Species mappings with the assemblies behind each, via kg-microbe.
  - name: LPSN
    url: https://lpsn.dsmz.de/
    relation_type: prov:wasDerivedFrom
    description: Nomenclature, authority, correct-name status and type strain designations, via kg-microbe.
  - name: BacDive
    url: https://bacdive.dsmz.de/
    relation_type: prov:wasDerivedFrom
    description: Strain records with culture-collection deposits and genome assertions.
  - name: GOLD
    url: https://gold.jgi.doe.gov/
    relation_type: prov:wasDerivedFrom
    description: Organism, sequencing-project and analysis-project links from the public workbook.
  - name: AllTheBacteria
    url: https://allthebacteria.org/
    relation_type: prov:wasDerivedFrom
    description: Assembly records joined through BioSample evidence.
  - name: StrainInfo
    url: https://straininfo.dsmz.de/
    relation_type: prov:wasDerivedFrom
    description: Deposit-to-NCBI assertions and typed strain, deposit and nucleotide references.
  - name: MediaDive
    url: https://mediadive.dsmz.de/
    relation_type: prov:wasDerivedFrom
    description: Media attestations per taxon.
  - name: Madin et al.
    url: https://doi.org/10.1038/s41597-020-0497-4
    relation_type: prov:wasDerivedFrom
    description: Prokaryotic phenotypic trait compilation, as a source attestation.
  - name: BactoTraits
    url: https://doi.org/10.1016/j.ecolind.2021.108047
    relation_type: prov:wasDerivedFrom
    description: Functional trait database, as a source attestation.
  - name: kg-microbe
    url: https://github.com/Knowledge-Graph-Hub/kg-microbe
    relation_type: prov:used
    description: The harmonized KGX inputs and the GTDB-to-NCBI and LPSN-to-NCBI mappings.
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
    Every causal edge must carry a citation. Seeded descriptive fields carry source
    attestations instead. A strain-to-genome link must name the source record that asserts
    it. Species membership and strain-name matching never supply a link.
  validation:
    - schema
    - corpus_reproduction
  curation_history: true
features:
  - causal_mechanism_graphs
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
  - id: taxonmech.records
    category: RecordCorpus
    name: Taxon records
    description: One YAML file per taxon under data/taxa/<domain>/<slug>.yaml.
    product_url: https://github.com/CultureBotAI/TaxonMech/tree/main/data/taxa
    format: yaml
  - id: taxonmech.schema
    category: DataModelProduct
    name: TaxonMech LinkML schema
    product_url: https://github.com/CultureBotAI/TaxonMech/blob/main/src/taxonmech/schema/taxonmech.yaml
    format: linkml
    compatibility:
      - linkml
      - mech_shared
  - id: taxonmech.browser
    category: GraphicalInterface
    name: TaxonMech browser
    product_url: https://culturebotai.github.io/TaxonMech/
    format: html
  - id: taxonmech.strain_assemblies
    category: RecordCorpus
    name: Strain assembly inventory
    description: >-
      Uncapped inventory of strain-to-NCBI-assembly links, joined to BacDive strains on
      strain_id. Unlisted strains live here and not in the records.
    product_url: https://github.com/CultureBotAI/TaxonMech/blob/main/data/raw/strain_assemblies.tsv
    format: tsv
cross_references:
  - target: dismech
    relation: follows_pattern_of
  - target: traitmech
    relation: hands_off_to
    description: Strain phenotypes are not held in TaxonMech.
  - target: culturemech
    relation: hands_off_to
    description: Growth media are not held in TaxonMech.
  - target: habitatmech
    relation: hands_off_to
    description: Isolation sources are not held in TaxonMech.
creation_date: 2026-09-16
last_modified_date: 2026-09-16
---

The record count is the generated corpus figure in the README at commit
7d1756a on 2026-09-16. Of 625,960 records, 605,695 are Bacteria, 14,013
Archaea and 6,243 Eukaryota. 572,305 are species and 46,325 are strains.
No record is REVIEWED and 14 are DEPRECATED. The rest are SEEDED or
PROPOSED. Records are generated and `just verify-corpus` requires that they
reproduce from the inventories plus `curation/seed_scope.tsv`. 21,071 listed
strains carry genome identifier links.

LPSN and StrainInfo have no Bioregistry prefix, so they are listed under data
sources and not under ontologies. BV-BRC (PATRIC) genome identifiers are
listed as `brc.genome`.
