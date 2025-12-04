# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile container-toolkit driver-containers edge gpu-operator gpu-telemetry kubernetes openshift partner-validated secure-services-istio-keycloak review all

# Target for building all documentation
all: container-toolkit driver-containers edge gpu-operator gpu-telemetry kubernetes openshift partner-validated secure-services-istio-keycloak review

container-toolkit:
	@$(SPHINXBUILD) -W -b html -d /tmp container-toolkit _build/docs/container-toolkit $(SPHINXOPTS) $(O)

driver-containers:
	@$(SPHINXBUILD) -W -b html -d /tmp driver-containers _build/docs/driver-containers $(SPHINXOPTS) $(O)

edge:
	@$(SPHINXBUILD) -W -b html -d /tmp edge _build/docs/edge $(SPHINXOPTS) $(O)

gpu-operator:
	@$(SPHINXBUILD) -W -b html -d /tmp gpu-operator _build/docs/gpu-operator $(SPHINXOPTS) $(O)

gpu-telemetry:
	@$(SPHINXBUILD) -W -b html -d /tmp gpu-operator _build/docs/gpu-operator $(SPHINXOPTS) $(O)

kubernetes:
	@$(SPHINXBUILD) -W -b html -d /tmp kubernetes _build/docs/kubernetes $(SPHINXOPTS) $(O)

openshift:
	@$(SPHINXBUILD) -W -b html -d /tmp openshift _build/docs/openshift $(SPHINXOPTS) $(O)

partner-validated:
	@$(SPHINXBUILD) -W -b html -d /tmp partner-validated _build/docs/partner-validated $(SPHINXOPTS) $(O)

secure-services-istio-keycloak:
	@$(SPHINXBUILD) -W -b html -d /tmp secure-services-istio-keycloak _build/docs/secure-services-istio-keycloak $(SPHINXOPTS) $(O)

review:
	@$(SPHINXBUILD) -W -b html -d /tmp review _build/docs/review $(SPHINXOPTS) $(O)


# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
