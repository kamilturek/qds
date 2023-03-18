.PHONY: deps-compile lint

deps-compile:
	pip-compile -o requirements/base.txt pyproject.toml
	pip-compile --extra dev -o requirements/dev.txt pyproject.toml

lint:
	pre-commit run --all-files
