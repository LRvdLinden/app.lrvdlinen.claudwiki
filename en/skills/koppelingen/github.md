---
description: >-
  The official GitHub MCP server: issues, pull requests, code reviews and searching repos.
icon: github
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

# GitHub

| | |
| --- | --- |
| **Maker** | GitHub · official Claude marketplace |
| **Works in** | Claude Code |
| **Cost** | Plugin free; requires a GitHub account |
| **Source** | [github.com/anthropics/claude-plugins-public/tree/main/external_plugins/github](https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/github) |

## What does it do?

With the GitHub plugin Claude works with GitHub directly: create issues, manage and review pull requests, search repositories and use the full GitHub API from Claude Code.

## When do you use it?

* You manage your code and issues on GitHub.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Create issues for every TODO in this folder and label them 'tech-debt'.
```
{% endcode %}

**What you get:** New GitHub issues with labels.

## Install

{% tabs %}
{% tab title="Claude Code" %}
This plugin is in the **official Anthropic marketplace**, which is connected by default:

```bash
/plugin install github@claude-plugins-official
```

Or browse via `/plugin` → **Discover** and pick the plugin from the list.

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/github" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Connect your apps</a>
