---
description: >-
  Expert knowledge for building flawless n8n workflows via the n8n MCP server.
icon: diagram-next
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

# n8n Skills

| | |
| --- | --- |
| **Maker** | czlonkowski (community) |
| **Works in** | Claude Code (with the n8n-mcp server) |
| **Cost** | Free (open source) |
| **Source** | [github.com/czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) |

## What does it do?

Fourteen cooperating skills, a router skill and hooks that teach Claude how n8n really works: expressions, configuring nodes, Code nodes in JavaScript or Python, validation and workflow patterns. Meant to work together with the [n8n-mcp](https://github.com/czlonkowski/n8n-mcp) server, so Claude can build workflows directly in your n8n.

## When do you use it?

* You automate with n8n and want Claude to build or fix workflows.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Build an n8n workflow that fetches the weather forecast every morning and sends it to Telegram.
```
{% endcode %}

**What you get:** A validated workflow in your n8n.

## Install

{% tabs %}
{% tab title="Claude Code" %}
```bash
/plugin install czlonkowski/n8n-skills
```

Or add the marketplace with `/plugin marketplace add czlonkowski/n8n-skills` and then choose via `/plugin`.
{% endtab %}

{% tab title="Manual" %}
Copy the skill folder to your personal skills folder (for all projects) or to `.claude/skills/` in one project:

```bash
git clone https://github.com/czlonkowski/n8n-skills.git
cp -r n8n-skills/skills/* ~/.claude/skills/
```
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Install the n8n-mcp server first; without it Claude can't reach your n8n.
{% endhint %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/czlonkowski/n8n-skills" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Development & code</a>
