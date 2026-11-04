---
description: >-
  Official Supabase skills and Postgres best practices for database, auth and storage.
icon: bolt-lightning
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

# Supabase

| | |
| --- | --- |
| **Maker** | Supabase (official, by the makers) |
| **Works in** | Claude Code (+ 18 other agents) |
| **Cost** | Free |
| **Source** | [github.com/supabase/agent-skills](https://github.com/supabase/agent-skills) |

## What does it do?

Two skills: **supabase** (working with the Supabase platform: database, auth, storage, edge functions) and **supabase-postgres-best-practices** (good schemas, indexes, row level security and queries).

## When do you use it?

* Your app uses Supabase as its backend.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Design a schema for notifications with row level security per user.
```
{% endcode %}

**What you get:** SQL migrations with RLS policies.

## Install

{% tabs %}
{% tab title="Claude Code" %}
```bash
claude plugin marketplace add supabase/agent-skills
claude plugin install supabase@supabase-agent-skills
claude plugin install postgres-best-practices@supabase-agent-skills
```
{% endtab %}

{% tab title="npx skills" %}
With the open-source [skills CLI](https://github.com/vercel-labs/skills) you install skills for Claude Code and other agents. All you need is Node.js:

```bash
npx skills add supabase/agent-skills
```

Add `-g` to install it globally (for all your projects). `npx skills list` shows what is installed.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Also in the official marketplace as `supabase`.
{% endhint %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/supabase/agent-skills" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Data, cloud & payments</a>
