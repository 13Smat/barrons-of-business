# ADR 0001: Record decisions before an ADR

## Status

Accepted (2026-11-26). Superseded by [ADR 0002](0002-github-issues.md) (2026-11-26).

## Context

Two humans and two bots share this repo. A bot must not, on its own, set design pillars or scope, edit the other person's area or a shared interface, add a dependency or an engine, license art, delete or rename shared things, merge, or spend money.

The engine and stack are an open decision for both humans. `13Smat/Groundwork` keeps accepted decisions in `docs/adr/`. This game also needs a list both bots can read before any code exists.

## Decision

Product and collaboration decisions are logged with options and a recommendation before any ADR. The bot notifies the humans who must decide and tells its own human. A human records the outcome. After that, the bot adds or updates an ADR in `docs/adr/`.

This record does not choose an engine, language, framework, host, or dependency.

[ADR 0002](0002-github-issues.md) places that log on GitHub issues.

## Alternatives

- Choose the stack in the agent-setup change. Rejected because the stack decision is open for both humans, and a bot does not make that call.
- Keep decisions only in pull request comments. Rejected because both bots need one list to check at the start of a session.

## Consequences

Agents check open decisions at the start of a session. `docs/adr/` stores decided outcomes. The stack stays open until that decision is accepted. Later decisions follow ADR 0002.

## References

- [ADR 0002](0002-github-issues.md)
- [Collaboration](../COLLABORATION.md)
- [Decision: pick engine/stack](https://github.com/13Smat/barrons-of-business/issues/2)
- [0000](0000-template.md)
