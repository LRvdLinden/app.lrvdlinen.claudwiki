---
description: >-
  Skills for Neon serverless Postgres: database, auth, functions, object storage and realtime.
icon: database
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

# Neon Postgres

| | |
| --- | --- |
| **Maker** | Neon (official, by the makers) |
| **Works in** | Claude Code (+ other agents) |
| **Cost** | Free |
| **Source** | [github.com/neondatabase/agent-skills](https://github.com/neondatabase/agent-skills) |

## What does it do?

Neon's own skills for its serverless Postgres platform, including branches for every feature, Neon Auth, functions, object storage, realtime and the AI gateway.

## When do you use it?

* You use (or are considering) Neon as your database.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Create a Neon branch for this feature and run the migration on it.
```
{% endcode %}

**What you get:** A separate database branch to test safely.

## Install

{% tabs %}
{% tab title="Claude Code" %}
First add the marketplace, then install the plugin. Type this in a Claude Code session:

```bash
/plugin marketplace add neondatabase/agent-skills
/plugin install neon-postgres@neon
```

Restart Claude Code if the skill doesn't appear right away. Check with `/plugin` that it is enabled.
{% endtab %}

{% tab title="npx skills" %}
With the open-source [skills CLI](https://github.com/vercel-labs/skills) you install skills for Claude Code and other agents. All you need is Node.js:

```bash
npx skills add neondatabase/agent-skills
```

Add `-g` to install it globally (for all your projects). `npx skills list` shows what is installed.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/neondatabase/agent-skills" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Data, cloud & payments</a>
