---
description: >-
  Automatically turns any documentation website, GitHub repo, PDF or video into a Claude skill.
icon: magnifying-glass-plus
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

# Skill Seekers

| | |
| --- | --- |
| **Maker** | yusufkaraaslan (community) |
| **Works in** | Standalone tool (Python), output works in Claude |
| **Cost** | Free (open source) |
| **Source** | [github.com/yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) |

## What does it do?

Skill Seekers fetches documentation (websites, GitHub repos, PDFs, videos, notebooks) and packages it as a skill. That way you give Claude expert knowledge of a tool or API it doesn't know yet, in a few minutes.

## When do you use it?

* You work with a niche API or tool Claude knows little about.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
skill-seekers scrape --url https://docs.example.com
```
{% endcode %}

**What you get:** A ready-made skill folder to install.

## Install

{% tabs %}
{% tab title="Install" %}
```bash
pip install skill-seekers
```

Then follow the quickstart in the README.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/yusufkaraaslan/Skill_Seekers" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Productivity & tools</a>
