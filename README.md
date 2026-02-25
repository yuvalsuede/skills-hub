# Cyclop One Skills Hub

> Community skills for [Cyclop One](https://cyclop.one) — the macOS desktop automation agent.

[![Skills](https://img.shields.io/badge/skills-3-blue)](skills/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## What are Skills?

Skills teach Cyclop One how to interact with specific apps. When you say _"compose an email to John"_, Cyclop One loads the `gmail-compose` skill to guide the agent step-by-step.

Skills are just two files — a JSON manifest and a Markdown description. No code required for UI automation.

## Browse Skills

| Skill | Description | Category |
|---|---|---|
| [gmail-compose](skills/gmail-compose/SKILL.md) | Compose and send Gmail emails | communication |
| [whatsapp-send](skills/whatsapp-send/SKILL.md) | Send WhatsApp messages | communication |
| [twitter-post](skills/twitter-post/SKILL.md) | Post on X (Twitter) | social |

## Install a Skill

Skills are available in the Cyclop One marketplace (in the app under the Skills tab). You can also install via command:

```
# Install from the Skills tab in Cyclop One
# Or run a command that matches the skill's triggers — Cyclop One will prompt to install
```

## Adding a Skill

Want to share a skill with the community? See [CONTRIBUTING.md](CONTRIBUTING.md).

It takes about 5 minutes to add a skill — just create a directory with `skill.json` and `SKILL.md`, then open a PR.

## Registry

The machine-readable index is at [`registry/index.json`](registry/index.json) and is auto-generated from the `skills/` directory when changes are merged.

## License

MIT
