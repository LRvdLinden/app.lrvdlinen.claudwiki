---
description: >-
  Search and organise files in Box and let Box AI answer questions about your documents.
icon: box
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

# Box

| | |
| --- | --- |
| **Maker** | Box · official Claude marketplace |
| **Works in** | Claude Code |
| **Cost** | Plugin free; requires a Box account |
| **Source** | [github.com/box/skills](https://github.com/box/skills) |

## What does it do?

With the Box plugin Claude searches files, organises folders and collaborates with your team in Box. Through Box AI it answers questions, summarises documents and extracts data.

## When do you use it?

* Your organisation stores documents in Box.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Summarise every contract in the 'Suppliers 2026' folder.
```
{% endcode %}

**What you get:** A summary per contract.

## Install

{% tabs %}
{% tab title="Claude Code" %}
This plugin is in the **official Anthropic marketplace**, which is connected by default:

```bash
/plugin install box@claude-plugins-official
```

Or browse via `/plugin` → **Discover** and pick the plugin from the list.

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/box/skills" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Connect your apps</a>
