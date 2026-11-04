---
description: >-
  Production-grade engineering workflows: write a spec, break it into tasks, build step by step, test and ship.
icon: diagram-project
cover: ../../../.gitbook/assets/cover-en-ontwikkeling.png
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

# Agent Skills (Addy Osmani)

{% hint style="danger" %}
**Spotted on social.** Went viral through 'I Tried 23 Viral Claude Skills' (Artificial Corner), among others.
{% endhint %}

| | |
| --- | --- |
| **Maker** | Addy Osmani (community) |
| **Works in** | Claude Code (+ other agents) |
| **Cost** | Free (open source) |
| **Source** | [github.com/addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) |

## What does it do?

Addy Osmani (Google Chrome) bundled the workflows and quality gates of senior engineers into about 25 skills. Think **spec-driven-development**, **planning-and-task-breakdown**, **incremental-implementation**, test-driven development, code review, security, performance, documentation and ADRs, CI/CD and launch. Claude records progress in files, so work stays consistent and verifiable.

## When do you use it?

* You build serious software with Claude Code.
* You want Claude to write a spec before it builds.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
First write a spec for the new search feature, split it into tasks and then build them one by one.
```
{% endcode %}

**What you get:** A spec, a task list and incremental commits.

## Install

{% tabs %}
{% tab title="Claude Code" %}
First add the marketplace, then install the plugin. Type this in a Claude Code session:

```bash
/plugin marketplace add addyosmani/agent-skills
/plugin install agent-skills@addy-agent-skills
```

Restart Claude Code if the skill doesn't appear right away. Check with `/plugin` that it is enabled.
{% endtab %}

{% tab title="npx skills" %}
With the open-source [skills CLI](https://github.com/vercel-labs/skills) you install skills for Claude Code and other agents. All you need is Node.js:

```bash
npx skills add addyosmani/agent-skills          # all skills
npx skills add addyosmani/agent-skills --list   # browse first
```

Add `-g` to install it globally (for all your projects). `npx skills list` shows what is installed.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Getting an SSH error on `/plugin install`? Use the HTTPS URL: `/plugin marketplace add https://github.com/addyosmani/agent-skills.git`.
{% endhint %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/addyosmani/agent-skills" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Development & code</a>
