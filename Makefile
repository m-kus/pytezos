.ONESHELL:
.PHONY: docs
.DEFAULT_GOAL: all

all: install lint test cover

debug:
	pip install . --force --no-deps

update:
	wget https://gitlab.com/tzip/tzip/-/raw/master/proposals/tzip-16/metadata-schema.json -O src/pytezos/contract/metadata-schema.json
	wget https://gitlab.com/tzip/tzip/-/raw/master/proposals/tzip-16/examples/example-000.json -O tests/unit_tests/test_contract/metadata/example-000.json
	wget https://gitlab.com/tzip/tzip/-/raw/master/proposals/tzip-16/examples/example-001.json -O tests/unit_tests/test_contract/metadata/example-001.json
	wget https://gitlab.com/tzip/tzip/-/raw/master/proposals/tzip-16/examples/example-002.json -O tests/unit_tests/test_contract/metadata/example-002.json
	wget https://gitlab.com/tzip/tzip/-/raw/master/proposals/tzip-16/examples/example-003.json -O tests/unit_tests/test_contract/metadata/example-003.json
	wget https://gitlab.com/tzip/tzip/-/raw/master/proposals/tzip-16/examples/example-004.json -O tests/unit_tests/test_contract/metadata/example-004.json
	wget https://gitlab.com/tzip/tzip/-/raw/master/proposals/tzip-16/examples/example-005.json -O tests/unit_tests/test_contract/metadata/example-005.json

	wget https://gitlab.com/tzip/tzip/-/raw/master/proposals/tzip-21/metadata-schema.json -O src/pytezos/contract/token_metadata-schema.json
	wget https://gitlab.com/tzip/tzip/-/raw/master/proposals/tzip-21/examples/example-000-base.json -O tests/unit_tests/test_contract/token_metadata/example-000-base.json
	wget https://gitlab.com/tzip/tzip/-/raw/master/proposals/tzip-21/examples/example-010-fungible-tz21.json -O tests/unit_tests/test_contract/token_metadata/example-010-fungible-tz21.json
	wget https://gitlab.com/tzip/tzip/-/raw/master/proposals/tzip-21/examples/example-020-digital-collectible.json -O tests/unit_tests/test_contract/token_metadata/example-020-digital-collectible.json


install:
	git submodule update --init
	poetry install --remove-untracked

notebook:
	PYTHONPATH="$$PYTHONPATH:src" poetry run jupyter notebook

isort:
	poetry run isort src

pylint:
	poetry run pylint src || poetry run pylint-exit $$?

mypy:
	poetry run mypy src

lint: isort pylint mypy

test:
	PYTHONPATH="$$PYTHONPATH:src" poetry run pytest --cov-report=term-missing --cov=pytezos --cov-report=xml -v .

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