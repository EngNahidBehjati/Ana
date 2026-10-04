# GitHub Remote Setup

The local repository is initialized in Sprint 0. The current GitHub connector can operate on existing repositories but cannot create a new repository. Create one empty remote repository named `ana`, then run:

```bash
git remote add origin git@github.com:<owner>/ana.git
git push -u origin main
```

Then configure branch protection for `main`:
- Require pull request before merge when a second human contributor is active.
- Require CI backend/frontend status checks.
- Block force push and branch deletion.
- Prefer squash merge.

Do not add a CD workflow until the staging/production deployment target is chosen.
