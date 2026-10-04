# ADR-006: Technology Stack

**Status:** Accepted

## Decision
- Backend: Python 3.13, FastAPI, Pydantic v2
- Persistence: SQLAlchemy 2.x, Alembic, Psycopg 3
- Database: PostgreSQL 18
- Cache/ephemeral coordination: Redis when justified
- Frontend: React + TypeScript + Vite + React Router + TanStack Query
- Backend package management: uv
- Frontend package management: npm
- Backend quality: Ruff, Pyright, pytest
- Frontend quality: ESLint, Vitest, Testing Library; Playwright when E2E flow exists
- Containers: Docker + Docker Compose
- CI: GitHub Actions
- Repository: monorepo

## Why FastAPI
Founder decision. Architecture compensates for missing batteries through explicit choices rather than recreating a framework inside the application.

## Why npm instead of pnpm initially
One web app plus one generated-client package does not justify an additional package-manager dependency. npm workspaces remain available if needed.
