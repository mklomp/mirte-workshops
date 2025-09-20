# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = ./docs/workshops/pioneer_line_follow
BUILDDIR      = _build
DIRS          = workshops/pioneer_line_follow homepage workshops/assemble

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)


.PHONY: help Makefile
.PHONY: build_en
build_lang:
	python3 scripts/build.py --dir=$(DIR)
	python3 scripts/dedup.py --dir=$(DIR)
	python3 scripts/create_pwa.py
# python will fail if not in venv

build_all:
	@for dir in $(DIRS); do \
		$(MAKE) build_lang DIR=$$dir; \
	done
	cp scripts/index.html _build/html/index.html

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
