install: ## Install the required Python dependencies
	pip install -r requirements.txt

auto-format: ## Run Ruff to check and fix formatting issues
	ruff check --fix
	ruff format

run: ## Run the main script
	python ./src/support.py

test: ## Run the tests
	pytest -v

help: ## Show this help message
	@echo "Available commands:"
	@awk 'BEGIN {FS = ":.*##"} /^[a-zA-Z0-9_-]+:.*##/ {printf "\033[1;32m  %-15s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)