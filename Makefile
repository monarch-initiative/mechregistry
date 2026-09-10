# MechRegistry build.
#
# Entries live in mech/<id>/<id>.md as YAML front matter. This Makefile
# validates them, concatenates them into registry/, and writes the Jekyll
# _config.yml the site reads. Run `make all` before `jekyll build`.
#
# Requires uv (https://docs.astral.sh/uv/). Recipe lines are tab-indented.

RUN = uv run

SCHEMA = src/mechregistry/schema/mechregistry.yaml
SCHEMA_ALL = src/mechregistry/schema/mechregistry_all.yaml
SCHEMA_JSON = src/mechregistry/schema/mechregistry.schema.json
SCHEMA_DOC_DIR = docs/schema
MECHS := $(shell find mech -type f -name '*.md' | LC_ALL=C sort)

.PHONY: all validate validate-file prettify check-prefixes clean schema-docs test lint site serve

all: validate registry/mechs.yml _config.yml _data/schema.yaml schema-docs

# Validate every entry against the LinkML schema (closed).
validate:
	$(RUN) mechregistry validate

# Validate one entry: make validate-file FILE=mech/dismech/dismech.md
validate-file:
	$(RUN) mechregistry validate $(FILE)

prettify:
	$(RUN) mechregistry prettify

# Every ontology prefix in the entries must resolve at the Bioregistry,
# because the site links each one there. Needs the network.
check-prefixes:
	$(RUN) mechregistry check-prefixes

registry/mechs.yml: $(MECHS) $(SCHEMA)
	$(RUN) mechregistry concat

_config.yml: _config_header.yml registry/mechs.yml
	$(RUN) mechregistry config

# The combined schema, exposed to Liquid as site.data.schema so templates
# can look up enum descriptions.
$(SCHEMA_ALL): $(SCHEMA)
	$(RUN) gen-linkml -f yaml -o $@ $<

_data/schema.yaml: $(SCHEMA_ALL)
	mkdir -p _data
	cp $< $@

$(SCHEMA_JSON): $(SCHEMA)
	$(RUN) gen-json-schema $< > $@

# Schema documentation pages, rendered by Jekyll with the schema_doc layout.
schema-docs: $(SCHEMA)
	rm -rf $(SCHEMA_DOC_DIR)
	$(RUN) gen-doc -d $(SCHEMA_DOC_DIR) $(SCHEMA)
	$(RUN) mechregistry fix-schema-docs $(SCHEMA_DOC_DIR)

test:
	$(RUN) pytest -q

lint:
	$(RUN) ruff check src tests
	$(RUN) linkml-lint --validate-only $(SCHEMA)

# Build the site with the same image GitHub Pages uses. Needs docker.
PAGES_IMAGE = ghcr.io/actions/jekyll-build-pages:v1.0.13
site: all
	docker run --rm -v "$(PWD):/github/workspace" \
	  -e GITHUB_WORKSPACE=/github/workspace -e GITHUB_REPOSITORY=monarch-initiative/mechregistry \
	  -e GITHUB_API_URL=https://api.github.com \
	  -e INPUT_SOURCE=. -e INPUT_DESTINATION=_site -e INPUT_FUTURE=false \
	  -e INPUT_BUILD_REVISION= -e INPUT_VERBOSE=false -e INPUT_TOKEN= \
	  $(PAGES_IMAGE)

# Serve _site/ locally after `make site`.
serve: site
	@echo "Serving http://localhost:4000/mechregistry/"
	cd _site && python3 -m http.server 4000

clean:
	rm -rf registry/mechs.yml registry/mechs.json registry/mechs-summary.json _config.yml _data/schema.yaml $(SCHEMA_ALL) $(SCHEMA_JSON) $(SCHEMA_DOC_DIR) _site .jekyll-cache
