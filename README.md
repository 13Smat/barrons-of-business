# Barons of Home Improvement

Rts game where the FTC Announces that "all is fair in love, war, and now TRADE!" Gloves off when it comes to retail. Most of all in the home improvement space where the companies are sabotaging each other in a fight to the bottom of morals. PVP or PVE against other retailers. Secure factories and resources to further expand your verticals and horizontal monopolies. Crush the competition at all costs by hiring scammers, sabotage production supply lines, and shut down combatant stores in various violent and non violent ways. Welcome to Baron's of Home Improvement

Andy Silver (GitHub [13Smat](https://github.com/13Smat)) co-builds this with a friend. Each person has their own bot. Both bots use this repo. Humans merge. Bots do not.

## How to start

There is no game to install or run. The engine and stack are an open decision on the Notion Decisions board, so this repo does not pick a runtime.

1. Read [AGENTS.md](AGENTS.md) before editing.
2. Read the [Notion hub](https://app.notion.com/p/424d792424608144935ddad53c435fc0) and the [Collaboration Rules](https://app.notion.com/p/424d7924246081bba4f1da68f94b4730).
3. Run `/setup-pstack` once, before any other pstack work. pstack is vendored in [`.cursor/`](.cursor/skills/VENDOR.md).
4. Use `/poteto-mode` for the work after that.
5. Take a Game Task only when you are that ticket's owner and its status is Ready for Grok.

Copy `.env.example` to `.env` when a later decision names real services. `.env.example` is placeholders only. `.env` stays untracked.

## Checks

Pull requests run markdown lint and a gitleaks secret scan.

```bash
npx --yes markdownlint-cli2
gitleaks detect --source . --redact --no-banner --exit-code 1
```

## Notion

- [Hub](https://app.notion.com/p/424d792424608144935ddad53c435fc0)
- [Collaboration Rules](https://app.notion.com/p/424d7924246081bba4f1da68f94b4730)
- [Game Tasks](https://app.notion.com/p/424d7924246081339308d7ebfb5713cf)
- [Decisions](https://app.notion.com/p/424d7924246081569f07c9bd17646a0a)
- [Handoffs and Decisions](https://app.notion.com/p/424d7924246081cea9b7ca1cd7bf80f8)

Repo rules for agents: [AGENTS.md](AGENTS.md). Current state: [docs/STATUS.md](docs/STATUS.md).
