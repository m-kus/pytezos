.PHONY: docs

debug:
	pip install . --force --no-deps

test:
	pytest -v .

docs:
	cd docs && $(MAKE) html