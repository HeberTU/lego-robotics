# Makefile for Pybricks projects

# Default filename (can be overridden from command line)
filename ?= demo.py

# Run command
run:
	pybricksdev run ble --name "InventorHub" $(filename)

# Help command to display usage
help:
	@echo "Usage:"
	@echo "  make run [filename=<your_file.py>]"
	@echo ""
	@echo "If no filename is specified, main.py will be used by default."