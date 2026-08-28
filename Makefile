CHECKMAKE_VERSION := v0.3.2
ACTIONLINT_VERSION := v1.7.12
MARKDOWNLINT_IMAGE_VERSION := v0.22.0
BLACK_VERSION := 26.5.1
CHECKMAKE := go run github.com/checkmake/checkmake/cmd/checkmake@$(CHECKMAKE_VERSION)
ACTIONLINT := go run github.com/rhysd/actionlint/cmd/actionlint@$(ACTIONLINT_VERSION)


# detect whether CONTAINER_CMD is set
ifeq ($(origin CONTAINER_CMD),undefined)
# try podman first
CONTAINER_CMD=$(shell podman version >/dev/null 2>&1 && echo podman)
ifeq ($(CONTAINER_CMD),)
#try docker if podman is not available
CONTAINER_CMD=$(shell docker version >/dev/null 2>&1 && echo docker)
endif
endif



.PHONY: check.container.runtime
check.container.runtime:
	$(if $(shell $(CONTAINER_CMD) version >/dev/null 2>&1 && echo available),,$(error no usable container runtime found. Install docker or podman, or set CONTAINER_CMD to a working command.))


LOCAL_MARKDOWNLINT := $(shell command -v markdownlint-cli2 2>/dev/null)
ifneq ($(LOCAL_MARKDOWNLINT),)
MARKDOWNLINT := $(LOCAL_MARKDOWNLINT)
else
MARKDOWNLINT := $(CONTAINER_CMD) run --rm -v $$PWD:/workdir --user $$(id -u):$$(id -g) --workdir /workdir davidanson/markdownlint-cli2:$(MARKDOWNLINT_IMAGE_VERSION)
MARKDOWNLINT_REQUIREMENTS := check.container.runtime
endif

LOCAL_BLACK := $(shell command -v black 2>/dev/null)
ifneq ($(LOCAL_BLACK),)
BLACK := $(LOCAL_BLACK)
else
BLACK := $(CONTAINER_CMD) run --rm --volume $$PWD:/src --user $$(id -u):$$(id -g) --workdir /src pyfound/black:$(BLACK_VERSION) black
BLACK_REQUIREMENTS := check.container.runtime
endif

.DEFAULT_GOAL := all

.PHONY: lint.code
lint.code: $(BLACK_REQUIREMENTS) ## check code formatting
	@echo "Checking python code formatting..."
	@$(BLACK) --check .
	@echo "All python files are formatted correctly."

.PHONY: reformat
reformat: $(BLACK_REQUIREMENTS) ## reformat the code
	@$(BLACK) .

.PHONY: lint.make
lint.make: ## lint the makefile
	@echo "Checking the Makefile..."
	@$(CHECKMAKE) Makefile
	@echo "The Makefile is OK."

.PHONY: lint
lint: lint.make lint.code lint.markdown lint.workflows ## Run various linters

.PHONY: test
test: lint
	@pytest

.PHONY: check
check: test

.PHONY: all
all: clean check

#clean is only added to silence checkmake.
.PHONY: clean
clean:
	@echo "cleaning..."
	@echo "All clean now."

.PHONY: lint.workflows
lint.workflows:
	@echo "linting GitHub workflows..."
	@$(ACTIONLINT) --color
	@echo "all workflows are good."

.PHONY: lint.markdown
lint.markdown: $(MARKDOWNLINT_REQUIREMENTS)
	@echo "linting markdown files..."
	@$(MARKDOWNLINT) --verbose "**/**.md"
	@echo "all markdown files are good."

.PHONY: fix.markdown
fix.markdown: $(MARKDOWNLINT_REQUIREMENTS)
	@$(MARKDOWNLINT) --verbose --fix "**/**.md"
