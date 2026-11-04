---
description: >-
  Hundreds of skills from Microsoft for Azure SDKs, AKS, Application Insights and Microsoft AI Foundry.
icon: microsoft
cover: ../../../.gitbook/assets/cover-en-cloud.png
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

# Microsoft Azure Skills

| | |
| --- | --- |
| **Maker** | Microsoft (official, by the makers) |
| **Works in** | Claude Code (+ Copilot and other agents) |
| **Cost** | Free |
| **Source** | [github.com/microsoft/skills](https://github.com/microsoft/skills) |

## What does it do?

Skills, agents, AGENTS.md templates and MCP configurations for anyone working with Azure: from Azure SDKs in Python, .NET, Java and TypeScript to AKS troubleshooting, cost optimisation and Microsoft AI Foundry. There is also a `deep-wiki` plugin.

## When do you use it?

* You build on Azure or with Microsoft AI services.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Add Application Insights to this Node app.
```
{% endcode %}

**What you get:** Instrumentation following Microsoft's guidelines.

## Install

{% tabs %}
{% tab title="Claude Code" %}
First add the marketplace, then install the plugin. Type this in a Claude Code session:

```bash
/plugin marketplace add microsoft/skills
/plugin install azure@skills
```

Restart Claude Code if the skill doesn't appear right away. Check with `/plugin` that it is enabled.
{% endtab %}

{% tab title="npx skills" %}
With the open-source [skills CLI](https://github.com/vercel-labs/skills) you install skills for Claude Code and other agents. All you need is Node.js:

```bash
npx skills add microsoft/skills
```

Add `-g` to install it globally (for all your projects). `npx skills list` shows what is installed.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Don't install everything at once: pick the skills for your language and services.
{% endhint %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/microsoft/skills" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Data, cloud & payments</a>
