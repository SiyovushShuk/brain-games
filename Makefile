install:
	uv sync

run:
	uv run brain-games-app

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=brain_games_package --cov-report xml

lint:
	uv run ruff check

check: test lint

build:
	uv build

.PHONY: install test lint selfcheck check build
