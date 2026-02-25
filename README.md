# Cyclop One Skills Hub

The official marketplace for [Cyclop One](https://cyclop.one) skills.

## What is a skill?

A skill is a package that teaches Cyclop One how to automate a specific task. Skills contain:
- **Trigger patterns** — regex phrases that activate the skill
- **Step instructions** — procedural guidance injected into the agent's context
- **Optional tools** — executable scripts (sandboxed) for complex automation

## Installing skills

Skills can be installed directly from the in-app marketplace (Browse tab in the Skills panel).

## Submitting a skill

1. Fork this repo
2. Create a directory under `skills/your-skill-name/`
3. Add `skill.json` (required) and `SKILL.md` (optional)
4. Open a pull request — the CI safety scanner will review it

## skill.json format

```json
{
  "name": "my-skill",
  "version": "1.0.0",
  "description": "What this skill does",
  "author": "your-github-username",
  "triggers": ["phrase that activates it", "another phrase"],
  "steps": [
    "Step 1: Do this first",
    "Step 2: Then do this"
  ],
  "permissions": [],
  "maxIterations": 15
}
```

## Skills index

The `registry/skills-index.json` file is the discovery layer fetched by the in-app marketplace client.
