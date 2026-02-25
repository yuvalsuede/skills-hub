#!/usr/bin/env python3
"""Auto-generate registry/index.json from skills/ directory.

Run locally:  python3 scripts/build-index.py
Used by:      .github/workflows/build-index.yml
"""
import json
import os
from datetime import datetime, timezone

BASE_URL = "https://raw.githubusercontent.com/yuvalsuede/skills-hub/main"
SKILLS_DIR = "skills"
OUTPUT = "registry/index.json"


def build_entry(name: str, manifest: dict) -> dict:
    return {
        "name": manifest["name"],
        "version": manifest["version"],
        "description": manifest["description"],
        "author": manifest.get("author", "community"),
        "category": manifest.get("category", "other"),
        "tags": manifest.get("tags", []),
        "verified": manifest.get("verified", False),
        "hasExecutableTools": bool(manifest.get("tools")),
        "skillURL": f"/skills/{name}/skill.json",
        "homepage": f"https://github.com/yuvalsuede/skills-hub/tree/main/skills/{name}",
        "permissions": manifest.get("permissions", []),
    }


def main():
    skills = []
    for name in sorted(os.listdir(SKILLS_DIR)):
        path = os.path.join(SKILLS_DIR, name, "skill.json")
        if not os.path.isfile(path):
            continue
        with open(path) as f:
            manifest = json.load(f)
        skills.append(build_entry(name, manifest))

    index = {
        "version": "2.0",
        "updatedAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "baseURL": BASE_URL,
        "skills": skills,
    }

    os.makedirs("registry", exist_ok=True)
    with open(OUTPUT, "w") as f:
        json.dump(index, f, indent=2)
        f.write("\n")

    print(f"Built index with {len(skills)} skills -> {OUTPUT}")


if __name__ == "__main__":
    main()
