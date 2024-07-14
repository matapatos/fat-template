.PHONY: install
install:
	pip install poetry
	yarn install
	poetry install --no-root
	[ "$RUN_E2E_TESTS" = false ] || poetry run playwright install --with-deps

.PHONY: install\:prod
install\:prod:
	pip install poetry
	yarn install
	poetry install --no-root --without dev

.PHONY: dev\:frontend
dev\:frontend:
	yarn dev

.PHONY: dev\:backend
dev\:backend:
	poetry run fastapi dev app/main.py

.PHONY: prod
prod:
	build
	poetry run fastapi run app/main.py

.PHONY: build
build:
	yarn build

.PHONY: lint
lint: lint\:ruff lint\:resources

.PHONY: lint\:ruff
lint\:ruff:
	poetry run ruff check

.PHONY: lint\:resources
lint\:resources:
	yarn lint

.PHONY: test
test: test\:unit test\:integration test\:e2e

.PHONY: test\:unit
test\:unit:
	poetry run pytest tests/unit

.PHONY: test\:integration
test\:integration:
	poetry run pytest tests/integration

.PHONY: test\:e2e
test\:e2e:
	poetry run pytest tests/e2e --base-url http://127.0.0.1:8000

.PHONY: test\:cov
test\:cov:
	poetry run coverage run --module pytest tests/unit tests/integration
	poetry run coverage xml

.PHONY: format
format:
	poetry run ruff format
	yarn format
