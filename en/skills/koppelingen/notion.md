---
description: >-
  Search Notion, create and edit pages and manage databases from Claude.
icon: book
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

# Notion

| | |
| --- | --- |
| **Maker** | Notion · official Claude marketplace |
| **Works in** | Claude Code |
| **Cost** | Plugin free; requires a Notion account |
| **Source** | [github.com/makenotion/claude-code-notion-plugin](https://github.com/makenotion/claude-code-notion-plugin) |

## What does it do?

The Notion plugin gives Claude access to your Notion workspace. It looks up pages, creates new documents, updates existing ones and manages databases. Handy if you keep documentation, minutes or plans in Notion.

## When do you use it?

* Your team works in Notion.
* You want Claude to put documentation in the right place directly.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Add today's minutes as a new page in the 'Meetings' Notion database.
```
{% endcode %}

**What you get:** A new Notion page with the minutes.

## Install

{% tabs %}
{% tab title="Claude Code" %}
This plugin is in the **official Anthropic marketplace**, which is connected by default:

```bash
/plugin install notion@claude-plugins-official
```

Or browse via `/plugin` → **Discover** and pick the plugin from the list.

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/makenotion/claude-code-notion-plugin" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Connect your apps</a>
