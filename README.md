# Ana (آنا)

Ana is a B2B real-estate collaboration network, initially focused on agencies in Najafabad, Isfahan.

## Sprint 0 status

The repository contains the agreed architecture baseline, ADRs, domain vocabulary, module boundaries,
backend/frontend scaffolds, database migration baseline, tests, and CI.

## Local development

### Backend

```bash
cd apps/backend
uv sync --all-groups
uv run alembic upgrade head
uv run uvicorn ana.main:app --reload
```

### Frontend

```bash
cd apps/web
npm install
npm run dev
```

### Docker Compose

```bash
docker compose up --build
```

Redis is intentionally optional in Sprint 0 and can be started with:

```bash
docker compose --profile cache up --build
```

## Engineering workflow

- `main` is the integration branch and should be protected in GitHub.
- Work happens on short-lived branches.
- Merge through Pull Requests.
- CI must pass before merge.
- Production CD is intentionally deferred until the deployment target is selected.

See `docs/sprints/sprint-0.md` and `docs/engineering/git-workflow.md`.
