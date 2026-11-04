---
description: >-
  Up-to-date reference for building with the Claude API and SDKs: models, pricing, tools, streaming and caching.
icon: server
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

# Claude API

| | |
| --- | --- |
| **Maker** | Anthropic (official) |
| **Works in** | Claude Code, Claude app, API |
| **Cost** | Free |
| **Source** | [github.com/anthropics/skills/tree/main/skills/claude-api](https://github.com/anthropics/skills/tree/main/skills/claude-api) |

## What does it do?

This skill makes sure that when building AI applications Claude doesn't work from memory, but uses the current documentation: model IDs, pricing, parameters, streaming, tool use, MCP, agents, prompt caching and migrating between models.

## When do you use it?

* You are building an app that uses the Claude API.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Add a feature to my app that summarises notifications with the Claude API, using prompt caching.
```
{% endcode %}

**What you get:** Code that uses the correct, current API calls.

## Install

{% tabs %}
{% tab title="Claude Code" %}
First add the marketplace, then install the plugin. Type this in a Claude Code session:

```bash
/plugin marketplace add anthropics/skills
/plugin install claude-api@anthropic-agent-skills
```

Restart Claude Code if the skill doesn't appear right away. Check with `/plugin` that it is enabled.
{% endtab %}

{% tab title="npx skills" %}
With the open-source [skills CLI](https://github.com/vercel-labs/skills) you install skills for Claude Code and other agents. All you need is Node.js:

```bash
npx skills add anthropics/skills --skill claude-api
```

Add `-g` to install it globally (for all your projects). `npx skills list` shows what is installed.
{% endtab %}
{% endtabs %}

<a href="https://github.com/anthropics/skills/tree/main/skills/claude-api" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Development & code</a>
