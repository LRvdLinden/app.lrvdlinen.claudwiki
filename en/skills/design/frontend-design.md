---
description: >-
  Gives Claude a distinct design taste, so interfaces don't look like a standard template.
icon: wand-magic-sparkles
cover: ../../../.gitbook/assets/cover-en-design.png
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

# Frontend Design

| | |
| --- | --- |
| **Maker** | Anthropic (official) |
| **Works in** | Claude app, Claude Code, API |
| **Cost** | Free (Apache 2.0) |
| **Source** | [github.com/anthropics/skills/tree/main/skills/frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) |

## What does it do?

Frontend Design teaches Claude to choose a **clear aesthetic direction** for every interface first: typography, colour, composition and details. The goal is for a website or app to look deliberate instead of 'like every AI site'. It is also available as a plugin in the official Claude Code marketplace.

## When do you use it?

* You let Claude build a website, landing page or app screen.
* You want to give an existing design its own character.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Build a landing page for my weather app. Pick a bold, distinctive style, no standard purple gradient.
```
{% endcode %}

**What you get:** A page with a recognisable, deliberate style.

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
This plugin is in the **official Anthropic marketplace**, which is connected by default:

```bash
/plugin install frontend-design@claude-plugins-official
```

Or browse via `/plugin` → **Discover** and pick the plugin from the list.
{% endtab %}

{% tab title="npx skills" %}
With the open-source [skills CLI](https://github.com/vercel-labs/skills) you install skills for Claude Code and other agents. All you need is Node.js:

```bash
npx skills add anthropics/skills --skill frontend-design
```

Add `-g` to install it globally (for all your projects). `npx skills list` shows what is installed.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Add a few words of atmosphere ('calm Scandinavian', 'retro newspaper', 'luxury night') for even better results.
{% endhint %}

<a href="https://github.com/anthropics/skills/tree/main/skills/frontend-design" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Design & frontend</a>
