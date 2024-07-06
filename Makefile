install:
	pip install poetry
	yarn install
	poetry install --no-root
	[ "$RUN_E2E_TESTS" = false ] || poetry run playwright install --with-deps

install\:prod:
	pip install poetry
	yarn install
	poetry install --no-root --without dev

dev\:frontend:
	yarn dev

dev\:backend:
	poetry run fastapi dev app/main.py

prod:
	build
	poetry run fastapi run app/main.py

build:
	yarn build

lint: lint\:isort lint\:black lint\:pylint lint\:resources

lint\:isort:
	poetry run isort . --diff

lint\:black:
	poetry run black . --diff

lint\:pylint:
	poetry run pylint app/ tests/

lint\:resources:
	yarn lint

test: test\:unit test\:integration test\:e2e

test\:unit:
	poetry run pytest tests/unit

test\:integration:
	poetry run pytest tests/integration

test\:e2e:
	poetry run pytest tests/e2e --base-url http://127.0.0.1:8000

test\:cov:
	poetry run coverage run --module pytest tests/unit tests/integration
	poetry run coverage xml

format:
	poetry run isort . && poetry run black .
	yarn format

.PHONY: install install\:prod dev\:frontend dev\:backend prod build
.PHONY: lint lint\:isort lint\:black lint\:pylint lint\:resources
.PHONY: test test\:unit test\:integration test\:e2e test\:cov format
