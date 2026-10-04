.PHONY: api-sync api-test api-lint api-format api-type web-install web-test web-lint web-build check

api-sync:
	cd apps/api && uv sync --all-groups

api-test:
	cd apps/api && uv run pytest

api-lint:
	cd apps/api && uv run ruff check . && uv run ruff format --check .

api-format:
	cd apps/api && uv run ruff check --fix . && uv run ruff format .

api-type:
	cd apps/api && uv run pyright

web-install:
	cd apps/web && npm ci

web-test:
	cd apps/web && npm test

web-lint:
	cd apps/web && npm run lint

web-build:
	cd apps/web && npm run build

check: api-lint api-type api-test web-lint web-test web-build
