# Makefile for Pybricks projects

# Default filename (can be overridden from command line)
filename ?= ./scripts/demos/demo.py

# Temporary file
TEMP_FILE := ./main.py

# Run command
run:
	@echo "Copying $(filename) to $(TEMP_FILE)"
	@cp $(filename) $(TEMP_FILE)
	@echo "Running pybricksdev with $(TEMP_FILE)"
	pybricksdev run ble --name "InventorHub" $(TEMP_FILE)
	@echo "Removing $(TEMP_FILE)"
	@rm $(TEMP_FILE)

# Help command to display usage
help:
	@echo "Usage:"
	@echo "  make run [filename=<path/to/your/script.py>]"
	@echo ""
	@echo "If no filename is specified, ./scripts/remote-controller/demo.py will be used by default."
	@echo "The specified file will be copied to ./main.py, executed, and then ./main.py will be removed."