---
description: >-
  Ten ready-made themes (colour + font) to style slides, documents and web pages in one go.
icon: swatchbook
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

# Theme Factory

| | |
| --- | --- |
| **Maker** | Anthropic (official) |
| **Works in** | Claude app, Claude Code, API |
| **Cost** | Free (Apache 2.0) |
| **Source** | [github.com/anthropics/skills/tree/main/skills/theme-factory](https://github.com/anthropics/skills/tree/main/skills/theme-factory) |

## What does it do?

Theme Factory is a toolkit with ten preset themes with matching colours and fonts. You apply them to anything Claude makes: presentations, documents, reports or HTML pages. If no theme fits, Claude invents a new one on the spot.

## When do you use it?

* You quickly want a consistent look across several pieces.
* You don't know which colours go together.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Show me the themes and then apply the calmest one to this presentation.
```
{% endcode %}

**What you get:** An overview of themes and a styled presentation.

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
npx skills add anthropics/skills --skill theme-factory
```

Add `-g` to install it globally (for all your projects). `npx skills list` shows what is installed.
{% endtab %}
{% endtabs %}

<a href="https://github.com/anthropics/skills/tree/main/skills/theme-factory" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Design & frontend</a>
