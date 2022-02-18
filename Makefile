# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment (for all but SOURCEDIR)
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
BUILDDIR      ?= build
SOURCEDIR     = source

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

preview:
	./scripts/previewer -w "$(SOURCEDIR)" "$(BUILDDIR)"/html

.PHONY: help preview Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
