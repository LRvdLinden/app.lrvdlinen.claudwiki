---
description: >-
  Building on Cloudflare: Workers, Durable Objects, Agents SDK, Wrangler, Turnstile and more.
icon: cloudflare
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

# Cloudflare

| | |
| --- | --- |
| **Maker** | Cloudflare (official, by the makers) |
| **Works in** | Claude Code (+ other agents) |
| **Cost** | Free |
| **Source** | [github.com/cloudflare/skills](https://github.com/cloudflare/skills) |

## What does it do?

A collection of skills for the Cloudflare Developer Platform: Workers best practices, Durable Objects, the Agents SDK, Wrangler, Next.js on Cloudflare, web performance, Turnstile and the email service. The plugin also installs the Cloudflare MCP server.

## When do you use it?

* You host your website or API on Cloudflare.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Convert this API to a Cloudflare Worker with caching.
```
{% endcode %}

**What you get:** A Worker plus wrangler configuration.

## Install

{% tabs %}
{% tab title="Claude Code" %}
First add the marketplace, then install the plugin. Type this in a Claude Code session:

```bash
/plugin marketplace add cloudflare/skills
/plugin install cloudflare@cloudflare
```

Restart Claude Code if the skill doesn't appear right away. Check with `/plugin` that it is enabled.
{% endtab %}

{% tab title="npx skills" %}
With the open-source [skills CLI](https://github.com/vercel-labs/skills) you install skills for Claude Code and other agents. All you need is Node.js:

```bash
npx skills add https://github.com/cloudflare/skills
```

Add `-g` to install it globally (for all your projects). `npx skills list` shows what is installed.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/cloudflare/skills" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Data, cloud & payments</a>
