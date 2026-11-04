---
description: >-
  Keeps a plan, findings and progress in files on disk, so Claude never loses track.
icon: list-check
cover: ../../../.gitbook/assets/cover-en-denken.png
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

# Planning with Files

| | |
| --- | --- |
| **Maker** | OthmanAdi (community) |
| **Works in** | Claude Code (+ Codex, Cursor, Copilot and 70+ other agents) |
| **Cost** | Free (open source) |
| **Source** | [github.com/OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) |

## What does it do?

On long tasks an AI agent sometimes forgets where it was. Planning with Files solves that with three files: `task_plan.md`, `findings.md` and `progress.md`. Hooks add the important planning context on every turn, and the plan even survives a `/clear`. That lets Claude work through a big project step by step.

## When do you use it?

* You let Claude do a large, multi-step project.
* You want to be able to look back at what was done and found.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Plan the migration of my app to a new iOS version with planning-with-files.
```
{% endcode %}

**What you get:** A plan on disk that Claude works through and updates step by step.

## Install

{% tabs %}
{% tab title="Claude Code" %}
First add the marketplace, then install the plugin. Type this in a Claude Code session:

```bash
/plugin marketplace add OthmanAdi/planning-with-files
/plugin install planning-with-files@planning-with-files
```

Restart Claude Code if the skill doesn't appear right away. Check with `/plugin` that it is enabled.
{% endtab %}

{% tab title="npx skills" %}
With the open-source [skills CLI](https://github.com/vercel-labs/skills) you install skills for Claude Code and other agents. All you need is Node.js:

```bash
npx skills add OthmanAdi/planning-with-files
```

Add `-g` to install it globally (for all your projects). `npx skills list` shows what is installed.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* The hooks only work in Claude Code (and other agents with hooks), not in the Claude app.
{% endhint %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/OthmanAdi/planning-with-files" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Thinking & planning</a>
