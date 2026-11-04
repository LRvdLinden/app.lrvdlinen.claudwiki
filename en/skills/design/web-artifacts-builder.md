---
description: >-
  Builds large, complex web artifacts with React, Tailwind CSS and shadcn/ui.
icon: cubes
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

# Web Artifacts Builder

| | |
| --- | --- |
| **Maker** | Anthropic (official) |
| **Works in** | Claude app, Claude Code, API |
| **Cost** | Free (Apache 2.0) |
| **Source** | [github.com/anthropics/skills/tree/main/skills/web-artifacts-builder](https://github.com/anthropics/skills/tree/main/skills/web-artifacts-builder) |

## What does it do?

You don't need this skill for simple pages. But want a bigger artifact with several parts, state management or routing? Then this skill sets up a modern stack (React, Tailwind CSS, shadcn/ui) and bundles everything into one artifact.

## When do you use it?

* You want an extensive tool or mini app as an artifact.
* You need several screens or components.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Build a volunteer planning tool with a week view, filters and a form.
```
{% endcode %}

**What you get:** An interactive mini app as an artifact.

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
npx skills add anthropics/skills --skill web-artifacts-builder
```

Add `-g` to install it globally (for all your projects). `npx skills list` shows what is installed.
{% endtab %}
{% endtabs %}

<a href="https://github.com/anthropics/skills/tree/main/skills/web-artifacts-builder" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Design & frontend</a>
