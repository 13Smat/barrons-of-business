# Collaboration

Andy Silver (GitHub login `13Smat`) builds Barons of Business with a friend. Each human has one bot. Both bots work in this repo. Humans merge. Bots do not.

This file is the source of truth for how the humans and the bots work together. `AGENTS.md` is the agent entry point and points here.

## Ownership

A ticket is a GitHub issue. It has one owner. The owner is Andy or Friend.

Mark the owner with `owner:andy` or `owner:friend`. Add that human as the assignee when their GitHub login is known. Andy's login is `13Smat`. Friend's login is not known yet. Do not invent a login.

Work only issues that carry your human's owner label. Leave every other issue alone.

Start an issue when it has your human's owner label and `status:ready`.

Folder ownership is not decided. `.github/CODEOWNERS` is a commented placeholder. Do not invent paths. Fill that file after a decision issue names the folders and Friend's login.

Get the other human's OK before you edit a shared interface or a folder they own. OK is a comment from that human on a decision issue, or text on the ticket that says both sides agreed.

## Status

Set status with a label.

| Label | Meaning |
| --- | --- |
| `status:ready` | The owning human says their bot may start. |
| `status:in-progress` | That bot has started. |
| `status:review` | CI is green and the pull request is ready for review. |
| `needs-decision` | A blocking decision is open. |

Move a ticket like this.

| From | To | Who |
| --- | --- | --- |
| No status label | `status:ready` | The owning human |
| `status:ready` | `status:in-progress` | That human's bot, when it starts |
| `status:in-progress` | `status:review` | That bot, when CI is green and the pull request is ready for review |
| `status:review` | Closed | A human, after merge |
| Any status | Add `needs-decision` | The bot, when a blocking decision is waiting |
| Any status | Remove the status label | A human |

A GitHub Project is optional. The labels are the status record.

You can add a board later.

1. Open this repository and select **Projects**. If the tab is absent, open your GitHub profile and select **Projects**.
2. Select **New project**. When the repository has no project, the control may be **Link a project**, then **New project**.
3. Choose **Board**. When the dialog lists **Kanban** and not **Board**, choose **Kanban**.
4. Name the project and create it.
5. Add this repository's issues to the board.

The board has its own Status field. Set the label when you change status. Follow the labels when the board and the labels disagree.

Label names and colors are in `.github/labels.yml`. Run `python3 .github/scripts/sync-labels.py` to create or update them. The script does not delete other labels. The Labels workflow runs that script on `main`.

## Calls you must not make alone

Do not decide these on your own.

- Design pillars and scope
- The other person's area, or a shared interface
- A new dependency, or the engine
- Art and asset licensing
- Deleting or renaming something shared
- A merge
- Anything that costs money

Use the decision flow for each one.

A reversible implementation detail inside your human's own area can proceed. Record a notable one in `docs/adr/` so the other bot can see it.

## Decision flow

[Issue #2](https://github.com/13Smat/barrons-of-business/issues/2) is `Decision: pick engine/stack`. It is already open. Do not open another issue for the engine or the stack.

Open a decision when the call is one you must not make alone.

1. Open an issue titled `Decision: ...`. Use `.github/ISSUE_TEMPLATE/decision.yml`.
2. Put the options and a recommendation in the body.
3. Add the label `needs-decision`.
4. Add one deciding label. Use `decide:both`, `owner:andy`, or `owner:friend`.
5. Add `blocking` when the call blocks work.
6. Add `needs-decision` on the blocked ticket when the call blocks that ticket.
7. Stop that ticket and work on something else.
8. Comment on the decision issue and @mention the humans who decide. GitHub emails them.
9. Tell your own human in chat.
10. Wait for the outcome comment. For `decide:both`, wait until both humans comment agreement.
11. Write an ADR from `docs/adr/0000-template.md`.
12. Close the decision issue.

Andy's GitHub login is `13Smat`. Friend's login is not known yet. Until it is known, write @13Smat in that comment, say that Friend still has to comment, and tell Andy in chat.

## Disagreements

A disagreement between Andy and Friend stays on the decision issue. You do not pick a winner.

`decide:both` means both humans comment agreement. An owner label means that human's comment is the outcome.

Leave the issue open while they disagree. Work on something else. Do not move the argument to a side channel.

## Communication

Write to the other bot only in issue comments and pull request comments. Sign each comment `🤖 (Andy's bot)` or `🤖 (Friend's bot)`.

A chat message between bots is not a record. When a human decides something in chat, write that outcome on the decision issue.

When you stop, paste a filled `docs/handoff-template.md` as a comment on the ticket.

When you stop before the ticket is done, also commit that handoff on the branch. Delete the committed copy when the ticket is done.

When the other side blocks you, write `BLOCKED: <one line>` at the top of the handoff. Say what you need in a pull request comment that mentions the other human. Then stop that ticket.

## Session start

Before you edit, check both lists.

1. Open issues with the label `needs-decision`.
2. Open issues with your human's owner label and the label `status:ready`.

`docs/STATUS.md` is the snapshot from the last pull request. Follow the open issues when the snapshot is older.

```bash
gh issue list --state open --label needs-decision
gh issue list --state open --label owner:andy --label status:ready
```

Friend's bot swaps in `owner:friend` for the second command.
