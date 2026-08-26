CHECKMAKE := go run github.com/checkmake/checkmake/cmd/checkmake@v0.3.2
ACTIONLINT := go run github.com/rhysd/actionlint/cmd/actionlint@v1.7.12

.DEFAULT_GOAL := all

.PHONY: lint.code
lint.code: ## check code formatting
	@echo "Checking python code formatting..."
	@black --check .
	@echo "All python files are formatted correctly."

.PHONY: reformat
reformat: ## reformat the code
	@black .

.PHONY: lint.make
lint.make: ## lint the makefile
	@echo "Checking the Makefile..."
	@$(CHECKMAKE) Makefile
	@echo "The Makefile is OK."

.PHONY: lint
lint: lint.make lint.code lint.workflows ## Run various linters

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
