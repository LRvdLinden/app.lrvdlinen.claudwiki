---
description: >-
  A complete 'agent harness': agents, skills, commands, hooks and rules in one big package.
icon: layer-group
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

# Everything Claude Code (ECC)

| | |
| --- | --- |
| **Maker** | affaan-m (community) |
| **Works in** | Claude Code (+ other agents) |
| **Cost** | Free (open source) |
| **Source** | [github.com/affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) |

## What does it do?

ECC is an extensive system of agents, skills, commands and hooks for Claude Code, meant as a complete 'operating system' for your agent. Big and extensive: mainly interesting for experienced users.

## When do you use it?

* You want a ready-made, extensive Claude Code setup.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
(after installation) /plan Add payments
```
{% endcode %}

**What you get:** A guided planning and build flow.

## Install

{% tabs %}
{% tab title="Claude Code" %}
First add the marketplace, then install the plugin. Type this in a Claude Code session:

```bash
/plugin marketplace add https://github.com/affaan-m/ECC
/plugin install ecc@ecc
```

Restart Claude Code if the skill doesn't appear right away. Check with `/plugin` that it is enabled.

Don't also copy the hooks into `settings.json`: the plugin already loads them.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Choose either the plugin or manual installation, not both.
{% endhint %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/affaan-m/everything-claude-code" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Development & code</a>
