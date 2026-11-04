---
description: >-
  Create and update issues, manage projects and search in Linear.
icon: list-check
cover: ../../../.gitbook/assets/cover-en-koppelingen.png
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

# Linear

| | |
| --- | --- |
| **Maker** | Linear · official Claude marketplace |
| **Works in** | Claude Code |
| **Cost** | Plugin free; requires a Linear account |
| **Source** | [github.com/anthropics/claude-plugins-public/tree/main/external_plugins/linear](https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/linear) |

## What does it do?

With the Linear plugin Claude creates issues, manages projects, updates statuses and searches your workspaces. Ideal for putting bugs or tasks straight from your code into Linear.

## When do you use it?

* You plan your software work in Linear.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Add these three bugs as issues in Linear, project 'App 2.0', with high priority.
```
{% endcode %}

**What you get:** Three new Linear issues.

## Install

{% tabs %}
{% tab title="Claude Code" %}
This plugin is in the **official Anthropic marketplace**, which is connected by default:

```bash
/plugin install linear@claude-plugins-official
```

Or browse via `/plugin` → **Discover** and pick the plugin from the list.

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/linear" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Connect your apps</a>
