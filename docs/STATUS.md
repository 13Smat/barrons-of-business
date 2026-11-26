# Status

Updated 2026-11-26.

## Now

No game code. This repo has agent rules, a vendored copy of pstack, and CI that lints markdown and scans for secrets.

Tickets and decisions are GitHub issues. The rules are `docs/COLLABORATION.md`.

The engine and stack are not chosen.

## Open

- [Decision: pick engine/stack](https://github.com/13Smat/barrons-of-business/issues/2) is open. It needs the labels `needs-decision`, `decide:both`, and `blocking`. Do not choose a stack, and do not add game code, until a human comments the outcome and the issue is closed.
- [Set up repo + AGENTS.md follow-ups](https://github.com/13Smat/barrons-of-business/issues/4) is open. It needs the labels `owner:andy` and `status:ready`. The steps are for Andy. A bot does not invite collaborators, change branch protection, or invent a GitHub login.
- Folder ownership is unset. `.github/CODEOWNERS` is commented placeholders. Friend's GitHub login is not recorded here.

## In this change

- `docs/COLLABORATION.md` is the working rules.
- Issue forms, `.github/labels.yml`, and a label sync script and workflow.
- ADR 0002 records decisions as GitHub issues. ADR 0001 is superseded.
- Issue #2 stays the engine decision. Issue #4 is the repo setup follow-up.

## Waiting on humans

- Comment the outcome on issue #2. Both Andy and Friend agree in a comment.
- On issue #4, add Friend as a collaborator, turn on branch protection for `main`, and fill in CODEOWNERS after a decision names the folders and Friend's login.

## Label writes from this agent

The agent `gh` token can open issues. It cannot create labels or edit issues. GitHub returned HTTP 403, `Resource not accessible by integration`.

These labels already existed: `needs-decision`, `decide:both`, `owner:andy`, `owner:friend`.

These labels were not created by that token: `blocking`, `status:ready`, `status:in-progress`, `status:review`.

Issue #2 and issue #4 have no labels yet. `.github/labels.yml` holds the definitions. The Labels workflow syncs them with the Actions token.
