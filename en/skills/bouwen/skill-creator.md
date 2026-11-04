---
description: >-
  The skill for making skills: set up, improve, test with evals and optimise the description.
icon: hammer
cover: ../../../.gitbook/assets/cover-en-bouwen.png
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

# Skill Creator

| | |
| --- | --- |
| **Maker** | Anthropic (official) |
| **Works in** | Claude app, Claude Code, API |
| **Cost** | Free (Apache 2.0) |
| **Source** | [github.com/anthropics/skills/tree/main/skills/skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) |

## What does it do?

Skill Creator guides you through making your own skill: what should it do, when should it trigger, which scripts or examples belong with it. Then it tests the skill with evals, measures performance (including variance) and optimises the description so Claude picks it at the right moment.

## When do you use it?

* You notice you keep giving Claude the same instructions.
* Your existing skill doesn't trigger (or triggers too often).

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Turn my standard workflow for publishing an app update into a skill.
```
{% endcode %}

**What you get:** A complete skill folder with SKILL.md, ready to upload.

{% code title="Example 2: what you type" overflow="wrap" %}
```
My skill is never used. Improve the description and test it.
```
{% endcode %}

**What you get:** An improved description with test results.

## Install

{% tabs %}
{% tab title="Claude app" %}
This skill is **already built in** for paid plans.

1. Open **Settings → Capabilities**.
2. Turn on **Code execution and file creation**.
3. Scroll to **Skills** and switch the skill on.

Then just ask for what you want in plain language; Claude loads the skill itself.
{% endtab %}

{% tab title="Claude Code" %}
This plugin is in the **official Anthropic marketplace**, which is connected by default:

```bash
/plugin install skill-creator@claude-plugins-official
```

Or browse via `/plugin` → **Discover** and pick the plugin from the list.
{% endtab %}

{% tab title="npx skills" %}
With the open-source [skills CLI](https://github.com/vercel-labs/skills) you install skills for Claude Code and other agents. All you need is Node.js:

```bash
npx skills add anthropics/skills --skill skill-creator
```

Add `-g` to install it globally (for all your projects). `npx skills list` shows what is installed.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* In the Claude app you can also simply say: 'turn this into a skill'.
{% endhint %}

<a href="https://github.com/anthropics/skills/tree/main/skills/skill-creator" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Build your own skills</a>
