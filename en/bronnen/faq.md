---
description: >-
  Frequently asked questions about Claude skills: what they cost, installing them, the Claude app versus Claude Code and sharing with your team.
icon: circle-question
cover: ../../.gitbook/assets/cover-en-bronnen.png
coverY: 0
layout:
  cover:
    visible: true
    size: full
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---
# Frequently asked questions

<details>
<summary>Do skills cost money?</summary>

The skills themselves are almost always free. In the Claude app you do need a Pro, Max, Team or Enterprise plan. Some skills use external services (like Remotion for large companies or hosted memory services) with their own terms.
</details>

<details>
<summary>Does a skill from Claude Code also work in the Claude app?</summary>

Often it does: it's the same standard. Zip the skill folder and upload it. Skills that depend on **hooks**, local programs or the terminal only work in Claude Code.
</details>

<details>
<summary>How many skills can I install?</summary>

Plenty. Claude first only sees the name and description and loads the rest only when needed. Too many skills with overlapping descriptions can cause confusion though: clean up what you don't use.
</details>

<details>
<summary>My skill isn't being used. What now?</summary>

1. Check that it is enabled (`/plugin` in Claude Code, Settings → Capabilities in the app).
2. Restart Claude Code.
3. Make the `description` more concrete: what it does **and** when it should be used.
4. Call it explicitly with `/name`.
</details>

<details>
<summary>What's the difference between /plugin and npx skills?</summary>

`/plugin` is built into Claude Code and installs complete plugins (skills, commands, hooks) with automatic updates. `npx skills` is a separate open-source CLI that only installs skills, but for dozens of different agents.
</details>

<details>
<summary>Can I share skills with my team?</summary>

In Claude Code: put them in `.claude/skills/` in your repo or create your own marketplace. In the Claude app, owners of Team and Enterprise organisations can provision skills for everyone.
</details>
