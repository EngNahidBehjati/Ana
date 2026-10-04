# Git Workflow

The repository is designed for 2-3 contributors without heavyweight process.

## Branches
- `main`: always mergeable/deployable, protected on GitHub.
- Work branches: `feature/<name>`, `fix/<name>`, `chore/<name>`.
- No long-lived `develop` branch.

## Pull requests
- PR required to merge to `main` once more than one human contributor is active.
- CI must pass.
- At least one human review is recommended when a second developer exists.
- Squash merge is preferred to keep history readable.

## Commit style
Use clear imperative messages; Conventional Commits are optional, not mandatory.

## GitHub settings to enable after remote repository creation
1. Protect `main`.
2. Require status checks: backend + frontend CI.
3. Block force pushes/deletion.
4. Require PRs when a second human contributor joins.
5. Enable Dependabot/security alerts if available.
