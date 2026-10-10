---
id: kg-registry
category: Mech
layout: mech_detail
name: KG-Registry
description: >-
  KG-Registry is a registry of knowledge graphs and the resources they are built from: data
  sources, ontologies, data models and aggregators. One record per resource: each record holds
  the resource's description, domains, taxa, license, contacts, publications and activity
  status, and lists its products (graph dumps, APIs, browsers, mappings, documentation) with
  the upstream resources each product was derived from. Those provenance links make the
  registry a graph of where biomedical knowledge comes from and where it goes. Agents expand
  stub records and refresh stale ones with skills kept in the repository, scripted syncs pull
  records from the OBO Foundry, FRINK, KG-Bioportal and Translator, and every agent change
  arrives by pull request. KG-Registry is not strictly a Mech: its records are metadata about
  other resources rather than evidence-backed claims, and it keeps no append-only curation
  history beyond the repository's own. It keeps the Mech practices of one record per entity in
  a closed LinkML schema, agent curation behind human review, and publication references
  checked against cached sources. MechRegistry is modeled on it.
activity_status: active
maturity: curating
homepage_url: https://kghub.org/kg-registry/
repository: https://github.com/Knowledge-Graph-Hub/kg-registry
schema_url: https://github.com/Knowledge-Graph-Hub/kg-registry/blob/main/src/kg_registry/kg_registry_schema/schema/kg_registry_schema.yaml
domains:
  - biomedical
record_type: >-
  a knowledge resource (knowledge graph, data source, ontology, data model or aggregator) and
  its products
record_count: 1137
record_count_date: 2026-10-10
record_count_commit: b7fd67feaa3b5014f902a2cd064749530cbaeb1c
record_count_source:
  path: resource
  pattern: "*.md"
  exclude:
    - "*.*.md"
    - "*_eval*.md"
record_identifier_policy: >-
  Records are keyed by a lowercase slug and stored as resource/<id>/<id>.md. Products take the
  resource id followed by a dot and a short name, and their pages are generated next to the
  resource page. Many resources also carry their Biolink Information Resource (infores)
  identifier.
ontologies:
  - NCBITaxon
  - MESH
  - NCIT
data_sources:
  - name: OBO Foundry
    url: https://obofoundry.org/
    relation_type: prov:wasDerivedFrom
    description: The OBO Foundry ontology registry, synced into ontology records.
  - name: FRINK OKN registry
    url: https://github.com/frink-okn/okn-registry
    relation_type: prov:wasDerivedFrom
    description: >-
      The Proto-OKN knowledge graph registry, synced into records with FRINK endpoint products.
  - name: KG-Bioportal
    url: https://github.com/ncbo/kg-bioportal
    relation_type: prov:wasDerivedFrom
    description: KGX transforms of BioPortal ontologies, added as graph products.
  - name: Translator
    url: https://kghub.org/kg-registry/resource/translator/translator.html
    relation_type: prov:wasDerivedFrom
    description: The current Translator KGX release products.
  - name: Biolink Information Resource Registry
    url: https://github.com/biolink/information-resource-registry
    relation_type: prov:used
    description: Infores identifiers for resources and stubs for resources not yet curated.
license:
  id: https://creativecommons.org/publicdomain/zero/1.0/
  label: CC0 1.0
  spdx_id: CC0-1.0
code_license:
  id: https://opensource.org/licenses/BSD-3-Clause
  label: BSD 3-Clause License
  spdx_id: BSD-3-Clause
curation:
  agent_curated: true
  human_review: pull_request
  agents:
    - Claude Code
    - dragon-ai-agent
  evidence_policy: >-
    Records describe resources rather than make claims, so evidence is the resource's own
    homepage, repository and publications. Publication titles, years, DOIs and first authors
    are checked against cached reference metadata, and provenance links must name registry
    identifiers rather than free text or URLs.
  validation:
    - schema
    - references
  curation_history: false
  curation_guide_url: https://kghub.org/kg-registry/docs/intro/agent-skills.html
features:
  - static_browser
contacts:
  - category: Organization
    label: Knowledge Graph Hub
    contact_details:
      - contact_type: github
        value: Knowledge-Graph-Hub
  - category: Individual
    label: J. Harry Caufield
    orcid: 0000-0001-5705-7831
    contact_details:
      - contact_type: email
        value: jhc@lbl.gov
      - contact_type: github
        value: caufieldjh
products:
  - id: kg-registry.records
    category: RecordCorpus
    name: Resource pages
    description: >-
      One Markdown file with a YAML header per resource under resource/<id>/, next to the
      generated pages for its products.
    product_url: https://github.com/Knowledge-Graph-Hub/kg-registry/tree/main/resource
    format: markdown
  - id: kg-registry.schema
    category: DataModelProduct
    name: KG-Registry LinkML schema
    product_url: https://github.com/Knowledge-Graph-Hub/kg-registry/blob/main/src/kg_registry/kg_registry_schema/schema/kg_registry_schema.yaml
    format: linkml
    compatibility:
      - linkml
  - id: kg-registry.app
    category: GraphicalInterface
    name: KG-Registry site
    description: >-
      A browser of every resource and product, with SQL search over the Parquet tables, a
      data quality dashboard and an interactive graph of resources and their sources.
    product_url: https://kghub.org/kg-registry/
    format: html
  - id: kg-registry.yaml
    category: OtherProduct
    name: Registry YAML
    description: Every resource in one YAML file. JSON-LD and Turtle versions sit beside it.
    product_url: https://kghub.org/kg-registry/registry/kgs.yml
    format: yaml
  - id: kg-registry.parquet
    category: OtherProduct
    name: Registry Parquet tables
    description: >-
      Resources, domains, products and taxa as Parquet tables, which the read-only discovery
      skills query over HTTP.
    product_url: https://kghub.org/kg-registry/registry/parquet-downloads.html
    format: other
  - id: kg-registry.docs
    category: DocumentationProduct
    name: KG-Registry documentation
    product_url: https://kghub.org/kg-registry/docs/intro/
    format: html
tags:
  - Mech-like
creation_date: 2026-10-10
last_modified_date: 2026-10-10
---

KG-Registry is in the registry as a Mech-like resource. It shares the
Mech curation practices, but a record describes a resource held
elsewhere rather than making evidence-backed claims about an entity.

At commit b7fd67f on 2026-10-10, `resource/` held 1,137 resource pages.
The record count takes one page per resource, `resource/<id>/<id>.md`.
The same folders hold 4,982 product pages generated from each
resource's front matter (`<id>.<product>.md`) and 125 automated
evaluation pages (`<id>_eval_automated.md`), which are not counted.
Resource identifiers contain no dots, so the `*.*.md` exclusion takes
only product pages.

Every agent-co-authored commit on the main branch since 2026-04-01
arrived through a merged pull request. The dragon-ai-agent workflow
that answers mentions on issues is switched off and runs only when
dispatched by hand.

KG-Registry has no cross-references here: none of the Mechs in this
registry has a KG-Registry record yet.
