.ONESHELL:
.PHONY: docs
.DEFAULT_GOAL: all

all: install lint test cover

debug:
	pip install . --force --no-deps

install:
	git submodule update --init
	poetry install

notebook:
	poetry run jupyter notebook

isort:
	poetry run isort pytezos

pylint:
	poetry run pylint pytezos || poetry run pylint-exit $$?

mypy:
	poetry run mypy pytezos

lint: isort pylint mypy

test:
	poetry run pytest --cov-report=term-missing --cov=pytezos --cov-report=xml -v .

cover:
	poetry run diff-cover coverage.xml

build:
	poetry build

docs:
	cd docs && rm -rf ./build && $(MAKE) html

rpc-docs:
	python -m scripts.fetch_docs

release-patch:
	bumpversion patch
	git push --tags
	git push

release-minor:
	bumpversion minor
	git push --tags
	git push

release-major:
	bumpversion major
	git push --tags
	git push