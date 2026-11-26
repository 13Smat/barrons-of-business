# AGENTS.md

Barons of Home Improvement is a multiplayer RTS: PvP and PvE retail war in the home improvement business. Andy Silver (GitHub `13Smat`) co-builds it with a friend. Each of them has their own bot, and both bots work in this repo. Read this file before planning or editing.

The product is not specified in code yet. Current state is `docs/STATUS.md`. Accepted outcomes also get a record in `docs/adr/`. How the two humans and two bots work is the [Collaboration Rules](https://app.notion.com/p/424d7924246081bba4f1da68f94b4730) page. The shared hub is [Barons of Home Improvement](https://app.notion.com/p/424d792424608144935ddad53c435fc0).

## Stack

The engine and stack are an open decision on the [Decisions](https://app.notion.com/p/424d7924246081569f07c9bd17646a0a) board: "Pick engine/stack" (Needs Both). Do not choose an engine, language, framework, host, or new dependency. Do not add game code that assumes one. `docs/adr/0001-record-decisions.md` records that process and leaves the stack open.

## Process

Andy's standing rules, adapted from `13Smat/Groundwork`:

- One ticket, one agent, one branch, one PR.
- Branch names are `<owner>/<ticket-slug>`, for example `andy/add-pause-menu` or `friend/load-level-1`. `setup/agent-rules` is the branch that added these rules.
- Open a draft PR after the first meaningful commit. Put the link on the Game Task `Branch/PR` field.
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
- Prefer boring, proven tools. A new dependency waits for a Decisions row (below).

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

### Tickets

Each Game Task has one Owner, Andy or Friend. A bot works only its own human's tickets. Pick a task up when Owner is your human and Status is `Ready for Grok`. Leave every other row alone.

Status names on the [Game Tasks](https://app.notion.com/p/424d7924246081339308d7ebfb5713cf) board:

| Transition | Who |
| --- | --- |
| Backlog to Ready for Grok | The owning human |
| Ready for Grok to In Grok | That human's bot, when it starts |
| In Grok to Review | That bot, when CI is green and the PR is ready for review |
| Review to Done | A human, after merge |
| Anything to Needs Decision | The bot, when a blocking decision is waiting |
| Anything to Backlog | A human |

### Folders

Folder ownership is not decided. `.github/CODEOWNERS` is a commented placeholder. Do not invent paths or GitHub handles. Fill that file after a Decisions row names the folders and the friend's GitHub login.

Shared interfaces, and any folder the other person owns, need the other side's OK before you edit them. OK means a Decisions comment from that human, or a ticket that already says both sides agreed.

### Coordination

Bots coordinate only in places both humans can see:

- Notion ticket Handoff Notes
- Notion Decision comments
- GitHub PR comments

Sign GitHub comments `🤖 (Andy's bot)` or `🤖 (Friend's bot)`. Slack or chat between bots is not a record. If a human decides something in chat, log it on the Decisions board.

When you stop, write the ticket Handoff Notes as Done / Next / Blocked. If you stop before the ticket is finished, also leave `docs/handoff-template.md` filled in on the branch, and delete that copy when the ticket is done.

Blocked on the other side: write `BLOCKED: <one line>` at the top of Handoff Notes, say what you need in a PR comment that @mentions the other human, and stop that ticket.

### Decisions a bot must not make alone

- Design pillars and scope
- The other person's area, or a shared interface
- A new dependency, or the engine
- Art and asset licensing
- Deleting or renaming something shared
- A merge
- Anything that costs money

Log each one on the [Decisions](https://app.notion.com/p/424d7924246081569f07c9bd17646a0a) board with options and a recommendation. Set Needs to Andy, Friend, or Both. Comment on the row and @mention the people in Needs. Tell your own human in their chat. If the call blocks the ticket, tick Blocking and set the Game Task to `Needs Decision`. Then work on something else.

Needs = Both means both humans agree in a comment. The human records Outcome and Decided On and sets Status to Decided. The bot then does the work and links the PR. Copy the outcome into `docs/adr/` from `docs/adr/0000-template.md`.

A reversible implementation detail inside your human's own area can proceed. Log the notable ones as Decided rows so the other bot can see them.

### Session start

Before editing, check:

- Decisions with Status Open
- Game Tasks with Status `Needs Decision`

The boards are linked above. `docs/STATUS.md` has the last snapshot a PR recorded. The boards win when they disagree.

## Status and handoff

- Update `docs/STATUS.md` in each PR.
- An ADR records a decision after humans have made it. Start from `docs/adr/0000-template.md`.
- A handoff uses `docs/handoff-template.md` and the ticket's Handoff Notes.
- An open design question is a Decisions row. Do not guess it in the PR.

## Commands

Until the stack decision lands, these are the checks:

```bash
npx --yes markdownlint-cli2
gitleaks detect --source . --redact --no-banner --exit-code 1
```

CI on pull requests runs the same two checks. Markdown lint ignores the vendored `.cursor/` tree. The secret scan covers the whole tree, including history on the pull request.
