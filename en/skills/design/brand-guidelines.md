---
description: >-
  Example of a brand skill: applies fixed brand colours and typography to everything Claude makes.
icon: copyright
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

# Brand Guidelines

| | |
| --- | --- |
| **Maker** | Anthropic (official) |
| **Works in** | Claude app, Claude Code, API |
| **Cost** | Free (Apache 2.0) |
| **Source** | [github.com/anthropics/skills/tree/main/skills/brand-guidelines](https://github.com/anthropics/skills/tree/main/skills/brand-guidelines) |

## What does it do?

This skill applies Anthropic's house style (colours and fonts). It is mainly interesting as an **example**: copy it, replace the colours and fonts with your brand's, and Claude will make everything in your house style from then on.

## When do you use it?

* You want Claude to use your brand colours and fonts by default.
* You want to learn how a brand skill is built.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Use my brand skill to make a flyer for the neighbourhood evening.
```
{% endcode %}

**What you get:** A flyer in your colours and fonts.

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
npx skills add anthropics/skills --skill brand-guidelines
```

Add `-g` to install it globally (for all your projects). `npx skills list` shows what is installed.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* See [Create your own skill](../../basis/eigen-skill-maken.md) to turn it into your own house style.
{% endhint %}

<a href="https://github.com/anthropics/skills/tree/main/skills/brand-guidelines" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Design & frontend</a>
