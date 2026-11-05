---
description: >-
  Give your agent a URL and it rebuilds the website as a clean Next.js app.
icon: clone
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

# AI Website Cloner

{% hint style="danger" %}
**Spotted on social.** With over 13,000 stars on GitHub the best-known clone skill: one command and your agent rebuilds a website.
{% endhint %}

| | |
| --- | --- |
| **Maker** | JCodesMore (community) |
| **Works in** | Claude Code (+ Codex, Cursor, OpenCode) |
| **Cost** | Free (open source) |
| **Source** | [github.com/JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) |

## What does it do?

A project template with the `/clone-website` skill. Claude works in four steps: **Map** (which page becomes which route), **Observe** (inspect desktop and mobile, extract real images, icons and fonts, try hover and click states), **Build** (build editable components and working interactions, optionally split across subagents) and **Compare** (compare source and clone side by side and repair differences). The result is a Next.js 16 app with React 19, TypeScript, shadcn/ui and Tailwind CSS v4, plus comparison screenshots.

## When do you use it?

* You want to move your own site from WordPress, Webflow or Squarespace to modern code.
* Your site's source code is lost, but the site is still online.
* You want to learn how a professional site achieves its layout and animations.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
/clone-website https://my-old-site.com
```
{% endcode %}

**What you get:** A Next.js project that looks and works the same, ready for further editing.

## Install

{% tabs %}
{% tab title="Claude Code" %}
Make your own copy of the template and open it in Claude Code:

```bash
git clone https://github.com/JCodesMore/ai-website-cloner-template.git my-clone
cd my-clone && npm install
claude
```

Then type in Claude Code:

```
/clone-website https://example.com
```

On GitHub you can also use **Use this template** → **Create repository**.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Works best with Claude Code with browser access (e.g. Claude in Chrome or a Playwright MCP).
* You need Node.js 24 or newer.
* Only use this for your own sites and apps, or with permission. Logos, brand assets and copy belong to their owners, and rebuilding a site to impersonate someone (phishing) is illegal. Also check the site's terms of service.
{% endhint %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/JCodesMore/ai-website-cloner-template" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Clone sites & apps</a>
