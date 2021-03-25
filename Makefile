.ONESHELL:
.PHONY: docs
.DEFAULT_GOAL: all

DEV ?= 1

all: install lint test cover

install:
	git submodule update --init  || true
	poetry install --remove-untracked `if [ "${DEV}" = "0" ]; then echo "--no-dev"; fi`

install-kernel:
	poetry run python post-install.py

remove-kernel:
	jupyter kernelspec uninstall michelson -f

notebook:
	poetry run jupyter notebook

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
	poetry run pytest --cov-report=term-missing --cov=pytezos --cov-report=xml -v .

cover:
	poetry run diff-cover coverage.xml

build:
	poetry build

image:
	docker build . -t michelson-kernel

docs:
	cd docs && rm -rf ./build && $(MAKE) html
	python -m scripts.gen_docs_py

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

