---
description: >-
  Manage Postgres databases with Prisma: schema migrations, SQL queries and provisioning Prisma Postgres.
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

# Prisma

| | |
| --- | --- |
| **Maker** | Prisma · official Claude marketplace |
| **Works in** | Claude Code |
| **Cost** | Free |
| **Source** | [prisma.io](https://prisma.io) |

## What does it do?

With the Prisma plugin Claude provisions Prisma Postgres databases, runs schema migrations, executes SQL queries and manages connection strings, straight from your development environment.

## When do you use it?

* You use Prisma as your ORM.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Add a 'read' field to Notification and create the migration.
```
{% endcode %}

**What you get:** An updated schema and a migration.

## Install

{% tabs %}
{% tab title="Claude Code" %}
This plugin is in the **official Anthropic marketplace**, which is connected by default:

```bash
/plugin install prisma@claude-plugins-official
```

Or browse via `/plugin` → **Discover** and pick the plugin from the list.

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://prisma.io" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Data, cloud & payments</a>
