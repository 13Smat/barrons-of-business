# Vendored pstack

Cursor cloud agents load project skills from `.cursor/skills/**/SKILL.md` and project subagents from `.cursor/agents/*.md`. This tree is committed so every cloud agent on this repo gets pstack without an account plugin.

| | |
| --- | --- |
| Source | Cursor plugin `pstack` ([cursor/plugins](https://github.com/cursor/plugins/tree/main/pstack)) |
| Version | 0.15.48 (`plugin.json` on the installed plugin) |
| License | MIT, `.cursor/LICENSE` |
| Layout | Same committed project-skill tree Andy uses: `skills/`, `agents/`, `docs/`, `README.md`, and `LICENSE` under `.cursor/` |

`13Smat/Groundwork` main has Andy's process rules and does not contain this tree. The copy here follows that project-skill layout so both bots in this repo resolve `/poteto-mode` from the checkout.

Upstream install for a laptop is `/add-plugin pstack`. That lands in the user plugin directory, which cloud agents do not inherit. The committed copy is the project-level path Cursor documents for cloud agents.

## Layout

Skill folders stay siblings of `poteto-mode`. The mode skill resolves other skills at `../<name>/SKILL.md`.

| Path | Upstream path | Why it is here |
| --- | --- | --- |
| `.cursor/skills/<name>/` | `skills/<name>/` | Every skill, including `poteto-mode`, `setup-pstack`, `how`, `architect`, `tdd`, `interrogate`, and all `principle-*` skills. |
| `.cursor/agents/` | `agents/` | `poteto-agent` and `comment-sicko`, the subagent types the skills spawn. |
| `.cursor/docs/` | `docs/` | Guide and harness notes. `poteto-help` links to `../../docs/`. |
| `.cursor/README.md` | `README.md` | Same relative link from `poteto-help` (`../../README.md`). |
| `.cursor/LICENSE` | `LICENSE` | MIT notice for this copy. |

## Local patch

`.cursor/agents/poteto-agent.md` has one extra sentence. If the parent omits the skill path, the subagent reads `.cursor/skills/poteto-mode/SKILL.md` from the workspace before it searches `~/.cursor/plugins/`. Upstream only searches the plugin cache, which a cloud agent does not have unless the account plugin is installed.

## Setup

Run `/setup-pstack` once at the beginning, before any other pstack work. That writes `~/.cursor/rules/pstack-models.mdc` for this machine. Do not commit that file. Do not run setup again once the file exists.

## Refresh

Copy `skills/`, `agents/`, `docs/`, `README.md`, and `LICENSE` from the pstack plugin over these paths. Re-apply the `poteto-agent` sentence above. Leave `VENDOR.md` as the only file under `.cursor/skills/` that is not from upstream.
