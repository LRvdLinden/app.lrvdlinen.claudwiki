---
description: >-
  Mirrors a simple informational website (practice, restaurant, portfolio) straight into a Next.js project.
icon: copy
cover: ../../../.gitbook/assets/cover-en-klonen.png
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

# Clone to Next.js

| | |
| --- | --- |
| **Maker** | Aisahub (community) |
| **Works in** | Claude Code |
| **Cost** | Free (open source) |
| **Source** | [github.com/Aisahub/skill-clone-to-nextjs](https://github.com/Aisahub/skill-clone-to-nextjs) |

## What does it do?

Meant for simple informational sites like a clinic, restaurant, portfolio or company intro. Every page is rendered in a real Chromium browser (Playwright), scrolled to the bottom so everything loads, after which all assets are downloaded and links rewritten. The result is a Next.js App Router project.

## When do you use it?

* You want to move a small, simple site to Next.js quickly.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Convert our residents' association website into a Next.js project.
```
{% endcode %}

**What you get:** A Next.js project with all pages and images.

## Install

{% tabs %}
{% tab title="Manual" %}
```bash
git clone https://github.com/Aisahub/skill-clone-to-nextjs ~/.claude/skills/clone-to-nextjs
```

The skill is available right away in your next Claude Code session.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Only use this for your own sites and apps, or with permission. Logos, brand assets and copy belong to their owners, and rebuilding a site to impersonate someone (phishing) is illegal. Also check the site's terms of service.
{% endhint %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/Aisahub/skill-clone-to-nextjs" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Clone sites & apps</a>
