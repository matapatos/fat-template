install:
	yarn install
	poetry install --no-root
	playwright install

install\:prod:
	yarn install
	poetry install --no-root --without dev

dev\:frontend:
	yarn dev

dev\:backend:
	poetry run fastapi dev app/main.py

prod:
	yarn build
	poetry run fastapi run app/main.py

test: lint test\:unit test\:integration test\:e2e

lint:
	poetry run isort . --diff && black . --diff && pylint app/ tests/
	yarn lint

test\:unit:
	poetry run pytest tests/unit

test\:integration:
	poetry run pytest tests/integration

test\:e2e:
	poetry run pytest tests/e2e

test\:cov:
	poetry run coverage run --module pytest . && coverage report --show-missing

format:
	poetry run isort . && black .
	yarn format

.PHONY: install install\:prod dev\:frontend dev\:backend prod test lint test\:unit test\:integration test\:e2e test\:cov format
