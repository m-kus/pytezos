.ONESHELL:
.PHONY: docs
.DEFAULT_GOAL: all

DEV ?= 1

all: install lint test cover

update:
	wget https://gitlab.com/tzip/tzip/-/raw/master/proposals/tzip-16/metadata-schema.json -O pytezos/contract/metadata-schema.json
	wget https://gitlab.com/tzip/tzip/-/raw/master/proposals/tzip-16/examples/example-000.json -O tests/metadata/example-000.json
	wget https://gitlab.com/tzip/tzip/-/raw/master/proposals/tzip-16/examples/example-001.json -O tests/metadata/example-001.json
	wget https://gitlab.com/tzip/tzip/-/raw/master/proposals/tzip-16/examples/example-002.json -O tests/metadata/example-002.json
	wget https://gitlab.com/tzip/tzip/-/raw/master/proposals/tzip-16/examples/example-003.json -O tests/metadata/example-003.json
	wget https://gitlab.com/tzip/tzip/-/raw/master/proposals/tzip-16/examples/example-004.json -O tests/metadata/example-004.json
	wget https://gitlab.com/tzip/tzip/-/raw/master/proposals/tzip-16/examples/example-005.json -O tests/metadata/example-005.json

install:
	git submodule update --init  || true
	poetry install --remove-untracked `if [ "${DEV}" = "0" ]; then echo "--no-dev"; fi`

install-kernel:
	poetry run python post-install.py

remove-kernel:
	jupyter kernelspec uninstall michelson -f

notebook:
	PYTHONPATH="$$PYTHONPATH:src" poetry run jupyter notebook

debug:
	pip install . --force --no-deps

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

image:
	docker build . -t michelson-kernel

docs:
	cd docs && rm -rf ./build && $(MAKE) html && cd ..
	python scripts/gen_docs_py.py

rpc-docs:
	python scripts/fetch_docs.py

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

