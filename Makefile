filename ?= ./projects/demos/demo.py

# Temporary file
TEMP_FILE := ./main.py

# Directories to format and lint
CODE_DIRS := ./projects ./src

# Poetry run prefix
POETRY_RUN := poetry run

# Run command
run:
	@echo "Copying $(filename) to $(TEMP_FILE)"
	@cp $(filename) $(TEMP_FILE)
	@echo "Running pybricksdev with $(TEMP_FILE)"
	$(POETRY_RUN) pybricksdev run ble --name "InventorHub" $(TEMP_FILE)
	@echo "Removing $(TEMP_FILE)"
	@rm $(TEMP_FILE)

# Format code
format:
	@echo "Formatting code with Black"
	$(POETRY_RUN) black --line-length 79 $(CODE_DIRS)
	@echo "Sorting imports with isort"
	$(POETRY_RUN) isort $(CODE_DIRS)

# Lint code
lint:
	@echo "Running Flake8"
	$(POETRY_RUN) flake8 $(CODE_DIRS)
	@echo "Running MyPy"
	$(POETRY_RUN) mypy $(CODE_DIRS)
	@echo "Checking docstring style with pydocstyle"
	$(POETRY_RUN) pydocstyle $(CODE_DIRS)

# Run all pre-commit hooks
pre-commit:
	$(POETRY_RUN) pre-commit run --all-files

# Run all code quality checks
check: format lint pre-commit

# Help command to display usage
help:
	@echo "Usage:"
	@echo "  make run [filename=<path/to/your/script.py>]"
	@echo "  make format               Format code with Black and isort"
	@echo "  make lint                 Lint code with Flake8, MyPy, and pydocstyle"
	@echo "  make pre-commit           Run all pre-commit hooks"
	@echo "  make check                Run all code quality checks (format, lint, pre-commit)"
	@echo ""
	@echo "If no filename is specified for 'make run', $(filename) will be used by default."
	@echo "The specified file will be copied to ./main.py, executed, and then ./main.py will be removed."

.PHONY: run format lint pre-commit check help
