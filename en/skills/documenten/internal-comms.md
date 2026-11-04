---
description: >-
  Writes internal communication in fixed formats: status updates, newsletters, FAQs and incident reports.
icon: bullhorn
cover: ../../../.gitbook/assets/cover-en-documenten.png
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

# Internal Comms

| | |
| --- | --- |
| **Maker** | Anthropic (official) |
| **Works in** | Claude app, Claude Code, API |
| **Cost** | Free (Apache 2.0) |
| **Source** | [github.com/anthropics/skills/tree/main/skills/internal-comms](https://github.com/anthropics/skills/tree/main/skills/internal-comms) |

## What does it do?

This skill contains example formats for all kinds of internal communication: status reports, leadership updates, newsletters, FAQs, incident reports and project updates. The idea: you adapt the formats to how your organisation likes it, so every piece is consistent.

## When do you use it?

* You regularly write updates or newsletters.
* You want incident reports to always have the same structure.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Write an incident report about last night's outage: cause, impact, fix and follow-up actions.
```
{% endcode %}

**What you get:** A report in a fixed, businesslike structure.

## Install

{% tabs %}
{% tab title="Claude app" %}
This skill is **already built in** for paid plans.

1. Open **Settings → Capabilities**.
2. Turn on **Code execution and file creation**.
3. Scroll to **Skills** and switch the skill on.

Then just ask for what you want in plain language; Claude loads the skill itself.
{% endtab %}

{% tab title="Claude Code" %}
First add the marketplace, then install the plugin. Type this in a Claude Code session:

```bash
/plugin marketplace add anthropics/skills
/plugin install example-skills@anthropic-agent-skills
```

Restart Claude Code if the skill doesn't appear right away. Check with `/plugin` that it is enabled.

This installs the whole **example-skills** pack (including this skill).
{% endtab %}

{% tab title="npx skills" %}
With the open-source [skills CLI](https://github.com/vercel-labs/skills) you install skills for Claude Code and other agents. All you need is Node.js:

```bash
npx skills add anthropics/skills --skill internal-comms
```

Add `-g` to install it globally (for all your projects). `npx skills list` shows what is installed.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Make your own copy and replace the example formats with your organisation's.
{% endhint %}

<a href="https://github.com/anthropics/skills/tree/main/skills/internal-comms" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Documents & office</a>
