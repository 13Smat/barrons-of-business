# Barons of Business

Rts game where the FTC Announces that "all is fair in love, war, and now TRADE!" Gloves off when it comes to retail. Most of all in the retail space where the companies are sabotaging each other in a fight to the bottom of morals. PVP or PVE against other retailers. Secure factories and resources to further expand your verticals and horizontal monopolies. Crush the competition at all costs by hiring scammers, sabotage production supply lines, and shut down combatant stores in various violent and non violent ways. Welcome to Baron's of Business

Andy Silver (GitHub [13Smat](https://github.com/13Smat)) co-builds this with a friend. Each person has their own bot. Both bots use this repo. Humans merge. Bots do not.

## How to start

There is no game to install or run. The engine and stack are an open decision, [Decision: pick engine/stack](https://github.com/13Smat/barrons-of-business/issues/2), so this repo does not pick a runtime.

1. Read [AGENTS.md](AGENTS.md) before editing.
2. Read [docs/COLLABORATION.md](docs/COLLABORATION.md).
3. Run `/setup-pstack` once, before any other pstack work. pstack is vendored in [`.cursor/`](.cursor/skills/VENDOR.md).
4. Use `/poteto-mode` for the work after that.
5. Take an issue only when it has your human's owner label and `status:ready`.

Copy `.env.example` to `.env` when a later decision names real services. `.env.example` is placeholders only. `.env` stays untracked.

## Checks

Pull requests run markdown lint and a gitleaks secret scan.

```bash
npx --yes markdownlint-cli2
gitleaks detect --source . --redact --no-banner --exit-code 1
```

## Collaboration

- [Collaboration rules](docs/COLLABORATION.md)
- [Open issues](https://github.com/13Smat/barrons-of-business/issues)
- [Current state](docs/STATUS.md)
- [Decision records](docs/adr/README.md)

Repo rules for agents: [AGENTS.md](AGENTS.md). Current state: [docs/STATUS.md](docs/STATUS.md).
