---
description: >-
  Creates animated GIFs that meet Slack's requirements exactly.
icon: face-grin-stars
cover: ../../../.gitbook/assets/cover-en-creatief.png
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

# Slack GIF Creator

| | |
| --- | --- |
| **Maker** | Anthropic (official) |
| **Works in** | Claude app, Claude Code, API |
| **Cost** | Free (Apache 2.0) |
| **Source** | [github.com/anthropics/skills/tree/main/skills/slack-gif-creator](https://github.com/anthropics/skills/tree/main/skills/slack-gif-creator) |

## What does it do?

A skill with knowledge and tools for making GIFs that work well in Slack: the right dimensions and file size, plus validation and animation ideas.

## When do you use it?

* You want a funny GIF or custom emoji for your team.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Make a GIF of a dancing toaster for Slack.
```
{% endcode %}

**What you get:** An optimised GIF.

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
First add the marketplace, then install the plugin. Type this in a Claude Code session:

```bash
/plugin marketplace add anthropics/skills
/plugin install example-skills@anthropic-agent-skills
```

Restart Claude Code if the skill doesn't appear right away. Check with `/plugin` that it is enabled.

This installs the whole **example-skills** pack (including this skill).
{% endtab %}

{% tab title="npx skills" %}
With the open-source [skills CLI](https://github.com/vercel-labs/skills) you install skills for Claude Code and other agents. All you need is Node.js:

```bash
npx skills add anthropics/skills --skill slack-gif-creator
```

Add `-g` to install it globally (for all your projects). `npx skills list` shows what is installed.
{% endtab %}
{% endtabs %}

<a href="https://github.com/anthropics/skills/tree/main/skills/slack-gif-creator" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Creative & video</a>
