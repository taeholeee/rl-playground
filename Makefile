SHELL := /bin/bash
POETRY := $(shell command -v poetry 2> /dev/null)
REPO_ROOT := $(shell git rev-parse --show-toplevel)
PROTOC := $(shell command -v protoc 2> /dev/null)


pre-commit:
	poetry run pre-commit run

pre-commit-all:
	poetry run pre-commit run --all-files

utest:
	poetry run pytest tests -s --verbose --cov=mnflow/ --cov-report=html --cov-report=term-missing --ignore=tests/components

init-dev:
ifndef POETRY
	@echo "Poetry could not be found. Installing it ..."
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
else
	poetry run pip install --upgrade pip
	poetry install

	rm -f $(REPO_ROOT)/.git/hooks/pre-commit && rm -f $(REPO_ROOT)/.git/hooks/pre-commit.legacy
	cd $(REPO_ROOT)
	poetry run pre-commit install

	poetry run python hooks/add_submodules.py $(REPO_ROOT)
	git submodule init
	git submodule update --recursive
endif
