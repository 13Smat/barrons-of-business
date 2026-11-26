# Status

Updated 2026-11-26. Checked the Notion boards the same day.

## Now

No game code. This repo has agent rules, a vendored copy of pstack, and CI that lints markdown and scans for secrets.

The engine and stack are not chosen.

## Open

- Decision [Pick engine/stack](https://app.notion.com/424d79242460811db3cece979f70c7f0) is Open. Needs Both. Blocking is off. Options and Recommendation are empty. Do not choose a stack until that row is Decided.
- Game Tasks in Needs Decision: none.
- Folder ownership is unset. `.github/CODEOWNERS` is commented placeholders. The friend's GitHub login is not recorded here.

## In this change

- `AGENTS.md` with Andy's process rules and the two-human rules.
- Pull request template, CODEOWNERS placeholder, handoff template, ADR 0001.
- pstack under `.cursor/` (see `.cursor/skills/VENDOR.md`).
- CI: markdown lint and gitleaks.

## Waiting on humans

- Decide the engine and stack on the Decisions board.
- Name folder owners and the friend's GitHub login, then uncomment CODEOWNERS.
- Branch protection on `main` (require a PR, green CI, no force-push). Bots do not change protection.
