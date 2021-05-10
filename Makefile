.ONESHELL:
.PHONY: docs
.DEFAULT_GOAL: all

DEV ?= 1

all: install lint test cover

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
	git submodule update --init  || true
	poetry install --remove-untracked `if [ "${DEV}" = "0" ]; then echo "--no-dev"; fi`

install-kernel:
	poetry run python -m michelson_kernel install

remove-kernel:
	jupyter kernelspec uninstall michelson -f

notebook:
	PYTHONPATH="$$PYTHONPATH:src" poetry run jupyter notebook

debug:
	pip install . --force --no-deps

isort:
	poetry run isort src

black:
	poetry run black src/michelson_kernel
	poetry run black src/pytezos/block
	poetry run black src/pytezos/contract
	poetry run black src/pytezos/michelson/program.py
	poetry run black src/pytezos/michelson/repl.py
	poetry run black src/pytezos/michelson/stack.py
	poetry run black src/pytezos/michelson/tags.py
	poetry run black src/pytezos/operation
	poetry run black src/pytezos/sandbox

pylint:
	poetry run pylint src || poetry run pylint-exit $$?

mypy:
	poetry run mypy src

lint: isort pylint mypy

test:
	poetry run nosetests --with-coverage tests --cover-package pytezos --cover-package michelson_kernel --cover-xml-file coverage.xml

test-verbose:
	poetry run nosetests -v --with-timer --with-coverage tests --cover-package pytezos --cover-package michelson_kernel --cover-xml-file coverage.xml

cover:
	poetry run diff-cover coverage.xml

build:
	poetry build

image:
	docker build . -t michelson-kernel

docs:
	cd docs && rm -rf ./build && $(MAKE) html && cd ..

kernel-docs:
	python scripts/gen_kernel_docs_py.py

rpc-docs:
	python scripts/fetch_docs.py

binder:


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

