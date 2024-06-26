install:
	poetry install --no-root

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

test: test\:lint test\:run

test\:lint:
	poetry run isort . --diff && black . --diff && pylint app/ tests/

test\:run:
	poetry run pytest .

test\:cov:
	poetry run coverage run --module pytest . && coverage report --show-missing

format:
	poetry run isort . && black .

.PHONY: install install\:prod dev\:frontend dev\:backend prod test test\:lint test\:run test\:cov format
