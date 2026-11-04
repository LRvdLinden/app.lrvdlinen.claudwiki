---
description: >-
  Search and create Jira issues, manage sprints and read Confluence documentation.
icon: atlassian
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

# Atlassian (Jira & Confluence)

| | |
| --- | --- |
| **Maker** | Atlassian · official Claude marketplace |
| **Works in** | Claude Code |
| **Cost** | Plugin free; requires a Atlassian account |
| **Source** | [github.com/atlassian/atlassian-mcp-server](https://github.com/atlassian/atlassian-mcp-server) |

## What does it do?

The Atlassian plugin connects Claude to Jira and Confluence. Claude searches and creates issues, manages sprints and consults documentation in Confluence, so your development work and docs stay aligned.

## When do you use it?

* Your organisation works with Jira or Confluence.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Which Jira issues are still open in the current sprint and who owns them?
```
{% endcode %}

**What you get:** An overview per owner.

## Install

{% tabs %}
{% tab title="Claude Code" %}
This plugin is in the **official Anthropic marketplace**, which is connected by default:

```bash
/plugin install atlassian@claude-plugins-official
```

Or browse via `/plugin` → **Discover** and pick the plugin from the list.

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/atlassian/atlassian-mcp-server" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Connect your apps</a>
