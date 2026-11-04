---
description: >-
  25 skills for Gmail, Calendar, Docs, Sheets, Slides, Drive, plus Postgres, Telegram, WhatsApp and more.
icon: google
cover: ../../../.gitbook/assets/cover-en-productiviteit.png
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

# Google Workspace & AI Skills

| | |
| --- | --- |
| **Maker** | sanjay3290 (community) |
| **Works in** | Claude Code (+ Gemini CLI and other agents) |
| **Cost** | Free (open source) |
| **Source** | [github.com/sanjay3290/ai-skills](https://github.com/sanjay3290/ai-skills) |

## What does it do?

A collection of portable skills: Gmail, Google Calendar, Chat, Docs, Sheets, Slides and Drive, but also Deep Research via Gemini, Imagen for images, NotebookLM, Jules, Outline, Atlassian, Azure DevOps, Postgres/MySQL/MSSQL (read-only) and Telegram and WhatsApp.

## When do you use it?

* You want Claude Code to work with your Google account or databases.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Find the latest emails from the municipality in my Gmail and put the appointments in my calendar.
```
{% endcode %}

**What you get:** Calendar items based on your mail.

## Install

{% tabs %}
{% tab title="Claude Code" %}
First add the marketplace, then install the plugin. Type this in a Claude Code session:

```bash
/plugin marketplace add sanjay3290/ai-skills
/plugin install ai-skills@ai-skills
```

Restart Claude Code if the skill doesn't appear right away. Check with `/plugin` that it is enabled.

All 25 skills come in one plugin. Update: `/plugin marketplace update ai-skills`.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* In the Claude app you can also connect Google through Connectors, without a skill.
{% endhint %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/sanjay3290/ai-skills" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Productivity & tools</a>
