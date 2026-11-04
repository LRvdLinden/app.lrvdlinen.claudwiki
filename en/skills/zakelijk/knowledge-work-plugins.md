---
description: >-
  Ready-made packs of skills, commands and connectors per job function: sales, finance, legal, marketing and more.
icon: briefcase
cover: ../../../.gitbook/assets/cover-en-zakelijk.png
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

# Anthropic role plugins

| | |
| --- | --- |
| **Maker** | Anthropic (official) |
| **Works in** | Claude app (desktop), Claude Code |
| **Cost** | Free (open source) |
| **Source** | [github.com/anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |

## What does it do?

Anthropic made a plugin per job function. Each plugin bundles **skills** (domain knowledge Claude uses automatically), **commands** (like `/sales:call-prep` or `/data:write-query`) and **connectors** to the tools of that role (Slack, HubSpot, Notion, Jira, Snowflake…). They are meant as a starting point: adapt them with your own terms, processes and tools.

| Plugin | For |
| --- | --- |
| `productivity` | **Productivity**: Tasks, calendars, daily workflows and personal context |
| `sales` | **Sales**: Researching prospects, preparing calls, pipeline, outreach and battlecards |
| `customer-support` | **Customer support**: Triaging tickets, drafting replies, escalations and knowledge base articles |
| `product-management` | **Product management**: Specs, roadmaps, user research and stakeholder updates |
| `marketing` | **Marketing**: Content, campaigns, brand voice, competition and reporting |
| `legal` | **Legal**: Contract review, NDA triage, compliance and risk |
| `finance` | **Finance**: Journal entries, reconciliations, financial statements and audits |
| `data` | **Data**: SQL, statistics, dashboards and validation |
| `design` | **Design**: Design critique, accessibility, handoff, UX copy and research |
| `engineering` | **Engineering**: Architecture, reviews, debugging, incidents and standups |
| `human-resources` | **HR**: Recruiting, onboarding, reviews and policy |
| `operations` | **Operations**: Processes, risks, runbooks and status reports |
| `enterprise-search` | **Enterprise search**: One query across mail, chat, documents and wikis |
| `small-business` | **Small business**: Chasing invoices, cash flow, social content, proposals and more |
| `bio-research` | **Bio research**: Literature, genomics and preclinical research |

## When do you use it?

* You want to use Claude as a specialist for a particular role.
* You want your team to get consistent results.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
/sales:call-prep Meeting with a municipality about a new neighbourhood app
```
{% endcode %}

**What you get:** Call preparation with background and questions.

{% code title="Example 2: what you type" overflow="wrap" %}
```
/small-business:invoice-chase
```
{% endcode %}

**What you get:** Overview of outstanding invoices with draft reminders.

## Install

{% tabs %}
{% tab title="Claude app" %}
Install the plugins in the Claude desktop app via [claude.com/plugins](https://claude.com/plugins/). They activate themselves; skills switch on automatically and the commands appear in your session.
{% endtab %}

{% tab title="Claude Code" %}
```bash
claude plugin marketplace add anthropics/knowledge-work-plugins
claude plugin install sales@knowledge-work-plugins
```

Replace `sales` with the plugin you want.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Use the `cowork-plugin-management` plugin to create or adapt a plugin for your own role.
{% endhint %}

<a href="https://github.com/anthropics/knowledge-work-plugins" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Business by role</a>
