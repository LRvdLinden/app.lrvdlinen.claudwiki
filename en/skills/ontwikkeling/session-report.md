---
description: >-
  Creates an interactive HTML report of your Claude Code usage: tokens, cache, subagents, skills and the most expensive prompts.
icon: chart-pie
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

# Session Report

| | |
| --- | --- |
| **Maker** | Anthropic · official Claude marketplace |
| **Works in** | Claude Code |
| **Cost** | Free |
| **Source** | [github.com/anthropics/claude-plugins-official/tree/main/plugins/session-report](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/session-report) |

## What does it do?

Session Report reads your local Claude Code transcripts and turns them into an explorable HTML report: how many tokens you used, how well the cache worked, which subagents and skills ran and which prompts cost the most.

## When do you use it?

* You want to know where your usage goes.
* You want to make your prompts more efficient.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
/session-report
```
{% endcode %}

**What you get:** An HTML report about your recent sessions.

## Install

{% tabs %}
{% tab title="Claude Code" %}
This plugin is in the **official Anthropic marketplace**, which is connected by default:

```bash
/plugin install session-report@claude-plugins-official
```

Or browse via `/plugin` → **Discover** and pick the plugin from the list.

{% endtab %}
{% endtabs %}

<a href="https://github.com/anthropics/claude-plugins-official/tree/main/plugins/session-report" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Development & code</a>
