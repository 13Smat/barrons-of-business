# AGENTS.md

Barons of Home Improvement is a multiplayer RTS: PvP and PvE retail war in the home improvement business. Andy Silver (GitHub `13Smat`) co-builds it with a friend. Each of them has their own bot, and both bots work in this repo. Read this file before planning or editing.

The product is not specified in code yet. Current state is `docs/STATUS.md`. Accepted outcomes also get a record in `docs/adr/`. How the two humans and two bots work is `docs/COLLABORATION.md`. That file is the source of truth.

## Stack

The engine and stack are an open decision: [Decision: pick engine/stack](https://github.com/13Smat/barrons-of-business/issues/2). It is labeled `needs-decision`, `decide:both`, and `blocking`. Do not open a second issue for the same call.

Do not choose an engine, language, framework, host, or new dependency. Do not add game code that assumes one. `docs/adr/0001-record-decisions.md` and `docs/adr/0002-github-issues.md` record the decision process and leave the stack open.

## Process

Andy's standing rules, adapted from `13Smat/Groundwork`:

- One ticket, one agent, one branch, one PR.
- Branch names are `<owner>/<ticket-slug>`, for example `andy/add-pause-menu` or `friend/load-level-1`. `setup/agent-rules` is the branch that added these rules.
- Open a draft PR after the first meaningful commit. Link the ticket with `Closes #` in the PR body.
- Keep going until CI is green. Mark the PR ready for review only after CI is green.
- Small commits with meaningful messages.
- Never force-push `main`. Never force-push a branch someone else might use.
- Bots never merge and never push to `main`. Only a human merges.
- Never remove a CI job, a required check, or branch protection unless a human has agreed. That includes skipping a job to land a patch.
- No review-only passes. Reading the diff is not finishing the ticket. Run the checks this repo actually has: markdown lint and the gitleaks secret scan (see Commands). When a decided stack adds typecheck, lint, test, or build, run those too. Do not report a green check the workflow does not run.
- Every bug fix gets a regression test or a lint rule in the same change.
- Test behavior, not implementation, once there is behavior to test.
- Read existing code first and match its conventions.
- Explain the why in the PR: how to run and test it, what is risky, and what is out of scope. Use `.github/pull_request_template.md`.
- Verify APIs and versions against docs or by running code.
- Prefer boring, proven tools. A new dependency waits for a decision issue. See `docs/COLLABORATION.md`.

## Security

This repo is public. No secrets, tokens, or credentials in git. `.env.example` holds empty placeholders only. Real values stay in an untracked `.env`.

Least privilege. Validate inputs at the boundary once a stack exists.

## pstack

pstack is vendored under `.cursor/` so both bots get the same skills from the checkout. The pin, layout, and the one local patch are in `.cursor/skills/VENDOR.md`.

- Run `/setup-pstack` once at the beginning, before any other pstack work. It writes `~/.cursor/rules/pstack-models.mdc` on that machine. Skip it once that file exists. Do not commit the file.
- Use `/poteto-mode` for non-trivial work. `poteto-mode` sets `disable-model-invocation: true`, so read `.cursor/skills/poteto-mode/SKILL.md` and follow the matched playbook. Put that file's absolute path in every `poteto-agent` prompt.
- Spawn code-writing and helper subagents with `subagent_type: "poteto-agent"` (`.cursor/agents/poteto-agent.md`). A `generalPurpose` delegate skips the required read and drifts. When a routed skill names its own subagent type, use that type. Comment review goes through the `no-comments` skill, which spawns `comment-sicko`.

A fully specified one-line edit can stay in the chat. A feature, bug fix, refactor, investigation, or any change you have to check goes through the playbook.

## Two humans, two bots

Read `docs/COLLABORATION.md` before you take work. In short:

- A ticket is a GitHub issue. The owner is the label `owner:andy` or `owner:friend`. You work only issues owned by your human.
- You do not make the calls in that file on your own. Open a `Decision: ...` issue, then stop the blocked ticket.
- Before you edit, check open `needs-decision` issues and your owner's `status:ready` issues. Open issues win over `docs/STATUS.md`.

Folder ownership is not decided. Do not invent paths or GitHub handles. A shared interface, and any folder the other person owns, needs that human's OK on a decision issue or on the ticket.

## Status and handoff

- Update `docs/STATUS.md` in each PR.
- An ADR records a decision after humans have made it. Start from `docs/adr/0000-template.md`.
- A handoff uses `docs/handoff-template.md`, pasted as a comment on the ticket.
- An open design question is a `Decision: ...` issue. Do not guess it in the PR.

## Commands

Until the stack decision lands, these are the checks:

```bash
npx --yes markdownlint-cli2
gitleaks detect --source . --redact --no-banner --exit-code 1
```

CI on pull requests runs the same two checks. Markdown lint ignores the vendored `.cursor/` tree. The secret scan covers the whole tree, including history on the pull request.
