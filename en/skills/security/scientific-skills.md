---
description: >-
  A library of 170+ scientific skills: biology, chemistry, medicine, physics and data analysis.
icon: flask
cover: ../../../.gitbook/assets/cover-en-security.png
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

# Scientific Skills

| | |
| --- | --- |
| **Maker** | K-Dense (community) |
| **Works in** | Claude Code (+ Cursor, Codex and more) |
| **Cost** | Free (open source) |
| **Source** | [github.com/K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) |

## What does it do?

A collection of over 170 research skills: biology, chemistry, medicine, physics, engineering, earth sciences, data analysis and scientific communication. Follows the open Agent Skills standard.

## When do you use it?

* You do (hobby) research or data analysis with scientific sources.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Analyse this measurement data and make a publication-ready chart with an explanation.
```
{% endcode %}

**What you get:** Analysis and chart following scientific conventions.

## Install

{% tabs %}
{% tab title="npx skills" %}
With the open-source [skills CLI](https://github.com/vercel-labs/skills) you install skills for Claude Code and other agents. All you need is Node.js:

```bash
npx skills add K-Dense-AI/scientific-agent-skills
```

Add `-g` to install it globally (for all your projects). `npx skills list` shows what is installed.
{% endtab %}

{% tab title="Manual" %}
Copy the skill folder to your personal skills folder (for all projects) or to `.claude/skills/` in one project:

```bash
git clone https://github.com/K-Dense-AI/scientific-agent-skills.git ~/.agents/skills/scientific-agent-skills
```
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/K-Dense-AI/scientific-agent-skills" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Security & science</a>
