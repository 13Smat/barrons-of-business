# ADR 0001: Record decisions on the Notion board

## Status

Accepted (2026-11-26)

## Context

Two humans and two bots share this repo. A bot must not, on its own, set design pillars or scope, edit the other person's area or a shared interface, add a dependency or an engine, license art, delete or rename shared things, merge, or spend money.

The engine and stack are already an open row on the Decisions board: "Pick engine/stack", Needs Both. `13Smat/Groundwork` keeps accepted decisions in `docs/adr/`. This game also needs a board both bots can read before any code exists. That board is the shared Notion workspace.

## Decision

Product and collaboration decisions are logged on the Notion Decisions board with options and a recommendation. The bot @mentions the people in Needs and tells its own human. Humans set Status to Decided and fill Outcome.

After a decision is Decided, the bot that carries it out adds or updates an ADR in `docs/adr/` so the git history has the outcome.

This record does not choose an engine, language, framework, host, or dependency.

## Alternatives

- Choose the stack in the agent-setup change. Rejected because "Pick engine/stack" is open for both humans, and a bot does not make that call.
- Keep decisions only in pull request comments. Rejected because Collaboration Rules name the Decisions board as the log both bots check.

## Consequences

Agents check Open decisions and Game Tasks in Needs Decision at the start of a session. `docs/adr/` stores decided outcomes. The next free number is 0002. The stack stays open until that Decisions row says otherwise.

## References

- [Decisions](https://app.notion.com/p/424d7924246081569f07c9bd17646a0a)
- [Collaboration Rules](https://app.notion.com/p/424d7924246081bba4f1da68f94b4730)
- [Pick engine/stack](https://app.notion.com/424d79242460811db3cece979f70c7f0)
- [0000](0000-template.md)
