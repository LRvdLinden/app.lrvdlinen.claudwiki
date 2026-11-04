---
description: >-
  Continuous memory for Claude Code: conversations are summarised into daily logs.
icon: brain
cover: ../../../.gitbook/assets/cover-en-kennis.png
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

# Remember

| | |
| --- | --- |
| **Maker** | Community · official Claude marketplace |
| **Works in** | Claude Code |
| **Cost** | Free |
| **Source** | [github.com/Digital-Process-Tools/claude-remember](https://github.com/Digital-Process-Tools/claude-remember) |

## What does it do?

Remember extracts the essence of your conversations, summarises them and compresses them into daily logs. That way Claude still knows tomorrow what you did yesterday.

## When do you use it?

* You work on the same project every day.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Where did we leave off yesterday?
```
{% endcode %}

**What you get:** A summary of yesterday's work.

## Install

{% tabs %}
{% tab title="Claude Code" %}
This plugin is in the **official Anthropic marketplace**, which is connected by default:

```bash
/plugin install remember@claude-plugins-official
```

Or browse via `/plugin` → **Discover** and pick the plugin from the list.

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/Digital-Process-Tools/claude-remember" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Knowledge & memory</a>
