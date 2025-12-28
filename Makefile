.PHONY: help lint format lint-backend format-backend lint-frontend format-frontend test test-backend run-backend run-frontend setup

help:
	@echo "Available commands:"
	@echo "  make setup           - Install all dependencies (backend + frontend)"
	@echo "  make lint            - Run linters on backend and frontend"
	@echo "  make format          - Format code (backend + frontend)"
	@echo "  make lint-backend    - Run ruff linter on backend"
	@echo "  make format-backend  - Format backend code with ruff"
	@echo "  make lint-frontend   - Lint frontend code with ESLint"
	@echo "  make test            - Run all tests"
	@echo "  make test-backend    - Run backend tests"
	@echo "  make run-backend     - Start Django dev server"
	@echo "  make run-frontend    - Start Vite dev server"
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

# Frontend commands
lint-frontend:
		cd frontend && npm run lint

format-frontend:
		cd frontend && npm run format || echo "Format script not configured yet"

run-frontend:
	cd frontend && npm run dev

build-frontend:
	cd frontend && npm run build

install-frontend:
	cd frontend && npm run install

# Combined commands
dev:
	@echo "Start backend with: make run-backend"
	@echo "Start frontend with: make run-backend"
	@echo "Run both in separate terminal panes"

lint: lint-backend lint-frontend

format: format-backend format-frontend

test: test-backend

# Setup
setup:
		cd backend && uv sync
		cd frontend && npm install
		@echo "Setup complete! Run 'make dev' to see how to start both servers"

