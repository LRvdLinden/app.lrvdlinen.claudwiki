---
description: >-
  Use Airtable as the database and operations layer for your agents: grids, kanban, calendars and more.
icon: table-cells
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

# Airtable

| | |
| --- | --- |
| **Maker** | Airtable · official Claude marketplace |
| **Works in** | Claude Code |
| **Cost** | Plugin free; requires a Airtable account |
| **Source** | [www.airtable.com](https://www.airtable.com) |

## What does it do?

With the Airtable plugin Claude reads and writes structured data in Airtable, for product, marketing, sales, operations, HR or a custom business app. Your data stays visible in the familiar Airtable views.

## When do you use it?

* You keep lists or processes in Airtable.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Add the sign-ups from this email to our 'Volunteers' Airtable.
```
{% endcode %}

**What you get:** New rows in your Airtable base.

## Install

{% tabs %}
{% tab title="Claude Code" %}
This plugin is in the **official Anthropic marketplace**, which is connected by default:

```bash
/plugin install airtable@claude-plugins-official
```

Or browse via `/plugin` → **Discover** and pick the plugin from the list.

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://www.airtable.com" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Connect your apps</a>
