---
description: >-
  Official MongoDB plugin: connect, explore data, optimise queries and generate reliable code.
icon: leaf
cover: ../../../.gitbook/assets/cover-en-cloud.png
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

# MongoDB

| | |
| --- | --- |
| **Maker** | MongoDB · official Claude marketplace |
| **Works in** | Claude Code |
| **Cost** | Free |
| **Source** | [www.mongodb.com/docs/mcp-server/overview/](https://www.mongodb.com/docs/mcp-server/overview/) |

## What does it do?

The official MongoDB plugin (MCP server plus skills) lets Claude connect to your databases, explore data, manage collections, optimise queries and write code following best practices.

## When do you use it?

* You use MongoDB or MongoDB Atlas.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Why is this query slow? Suggest an index.
```
{% endcode %}

**What you get:** An analysis and a fitting index.

## Install

{% tabs %}
{% tab title="Claude Code" %}
This plugin is in the **official Anthropic marketplace**, which is connected by default:

```bash
/plugin install mongodb@claude-plugins-official
```

Or browse via `/plugin` → **Discover** and pick the plugin from the list.

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://www.mongodb.com/docs/mcp-server/overview/" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Data, cloud & payments</a>
