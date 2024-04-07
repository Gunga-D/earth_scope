.PHONY: build
build:
	python -m nuitka --follow-imports --onefile bin/cli.py