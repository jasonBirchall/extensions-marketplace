.PHONY: help lint format lint-backend format-backend lint-frontend format-frontend test test-backend run-backend run-frontend setup

help:
	@echo "Available commands:"
	@echo "  make setup           - Install all dependencies (backend + frontend)"
	@echo "  make lint            - Run linters on backend and frontend"
	@echo "  make format          - Format code (backend + frontend)"
	@echo "  make lint-backend    - Run ruff linter on backend"
	@echo "  make format-backend  - Format backend code with ruff"
	@echo "  make test            - Run all tests"
	@echo "  make test-backend    - Run backend tests"
	@echo "  make run-backend     - Start Django dev server"
	@echo "  make migrate         - Run Django migrations"
	@echo "  make migrations      - Create new Django migrations"

# Backend commands
lint-backend:
		cd backend && uv run ruff check .

format-backend:
		cd backend && uv run ruff format .
		cd backend && uv run ruff check --fix .

test-backend:
		cd backend && uv run python manage.py test

run-backend:
		cd backend && uv run python manage.py runserver

migrate:
		cd backend && uv run python manage.py migrate

migrations:
		cd backend && uv run python manage.py makemigrations

# Frontend commands (will add these when we set up frontend)
lint-frontend:
		@echo "Frontend not set up yet"

format-frontend:
		@echo "Frontend not set up yet"

# Combined commands
lint: lint-backend lint-frontend

format: format-backend format-frontend

test: test-backend

# Setup
setup:
		cd backend && uv sync
		@echo "Backend setup complete. Frontend setup coming soon!"

