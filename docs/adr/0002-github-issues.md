# ADR 0002: Record decisions as GitHub issues

## Status

Accepted (2026-11-26)

## Context

Andy decided to keep tickets and decisions in this repo. A hosted wiki would charge, so the log lives on GitHub issues. He sent that decision with the change that adds this file.

[Issue #2](https://github.com/13Smat/barrons-of-business/issues/2), `Decision: pick engine/stack`, already holds the engine options. It stays the open stack decision.

## Decision

Tickets are GitHub issues. Decisions are issues titled `Decision: ...`, with the labels in [Collaboration](../COLLABORATION.md). A human comments the outcome. The bot then writes an ADR and closes the issue.

This record does not choose an engine, language, framework, host, or dependency.

## Alternatives

- Pay for a hosted wiki. Rejected because Andy dropped it.
- Keep decisions only in pull request comments. Rejected because session start needs a list of open decisions, and that list is the `needs-decision` label.

## Consequences

`docs/COLLABORATION.md` is the working rules. Issue #2 stays open. The next free ADR number is 0003.

## References

- [Collaboration](../COLLABORATION.md)
- [Decision: pick engine/stack](https://github.com/13Smat/barrons-of-business/issues/2)
- [0001](0001-record-decisions.md)
- [0000](0000-template.md)
