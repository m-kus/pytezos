.ONESHELL:
.PHONY: $(MAKECMDGOALS)
##
##    🚧 PyTezos developer tools
##
##  DEV=1               Whether to install dev dependencies
DEV=1
##  TAG=latest          Tag for the `image` command
TAG=latest

##

help:              ## Show this help (default)
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

all:               ## Run a whole CI pipeline: lint, run tests, build docs
	make install lint test docs

install:           ## Install project dependencies
	poetry install \
	`if [ "${DEV}" = "0" ]; then echo "--no-dev"; fi`

lint:              ## Lint with all tools
	make isort black flake mypy

test:              ## Run test suite
	poetry run sh -c "pytest --cov-report=term-missing --cov=pytezos --cov=michelson_kernel --cov-report=xml -n auto -s -v tests/contract_tests tests/integration_tests tests/unit_tests && pytest -v tests/sandbox_tests"

docs:              ## Build docs
	make kernel-docs rpc-docs
	cd docs
	rm -r build || true
	poetry run make html
	cd ..

##

isort:             ## Format with isort
	poetry run isort src tests scripts

black:             ## Format with black
	# poetry run black src tests scripts --exclude ".*/docs.py"

flake:             ## Lint with flake8
	poetry run flakeheaven lint src tests scripts || true

mypy:              ## Lint with mypy
	poetry run mypy src scripts  # tests

cover:             ## Print coverage for the current branch
	poetry run diff-cover --compare-branch `git symbolic-ref refs/remotes/origin/HEAD | sed 's@^refs/remotes/origin/@@'` coverage.xml

build:             ## Build Python wheel package
	poetry build

image:             ## Build Docker image
	docker buildx build . -t pytezos:${TAG}

release-patch:     ## Release patch version
	bumpversion patch
	git push --tags
	git push

release-minor:     ## Release minor version
	bumpversion minor
	git push --tags
	git push

release-major:     ## Release major version
	bumpversion major
	git push --tags
	git push

clean:             ## Remove all files from .gitignore except for `.venv`
	git clean -xdf --exclude=".venv"

##

install-kernel:    ## Install Michelson IPython kernel
	poetry run michelson-kernel install

remove-kernel:     ## Remove Michelson IPython kernel
	jupyter kernelspec uninstall michelson -f

notebook:          ## Run Jupyter notebook
	poetry run jupyter notebook

##

update-tzips:      ## Update TZIP-16 schema and tests
	wget https://gitlab.com/tzip/tzip/-/raw/master/proposals/tzip-16/metadata-schema.json -O src/pytezos/contract/metadata-schema.json
	wget https://gitlab.com/tzip/tzip/-/raw/master/proposals/tzip-16/examples/example-000.json -O tests/unit_tests/test_contract/metadata/example-000.json
	wget https://gitlab.com/tzip/tzip/-/raw/master/proposals/tzip-16/examples/example-001.json -O tests/unit_tests/test_contract/metadata/example-001.json
	wget https://gitlab.com/tzip/tzip/-/raw/master/proposals/tzip-16/examples/example-002.json -O tests/unit_tests/test_contract/metadata/example-002.json
	wget https://gitlab.com/tzip/tzip/-/raw/master/proposals/tzip-16/examples/example-003.json -O tests/unit_tests/test_contract/metadata/example-003.json
	wget https://gitlab.com/tzip/tzip/-/raw/master/proposals/tzip-16/examples/example-004.json -O tests/unit_tests/test_contract/metadata/example-004.json
	wget https://gitlab.com/tzip/tzip/-/raw/master/proposals/tzip-16/examples/example-005.json -O tests/unit_tests/test_contract/metadata/example-005.json

update-contracts:  ## Update contract tests
	rm -r tests/contract_tests/dexter_usdtz_xtz || true
	rm -r tests/contract_tests/KT1* || true

	poetry run python scripts/fetch_contract_data.py KT1Tr2eG3eVmPRbymrbU2UppUmKjFPXomGG9 dexter_usdtz_xtz
	poetry run python scripts/fetch_contract_data.py KT1SWHFFrgtRJF7LecghRCA9sPWqUyURHUUW ""
	# poetry run python scripts/fetch_contract_data.py

	poetry run python scripts/generate_contract_tests.py
	poetry run pytest -v tests/contract_tests

kernel-docs:       ## Build docs for Michelson IPython kernel
	poetry run python scripts/generate_kernel_docs.py

rpc-docs:          ## Build docs for Tezos node RPC
	poetry run python scripts/fetch_rpc_docs.py
