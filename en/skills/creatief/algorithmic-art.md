---
description: >-
  Generative art with p5.js: flow fields, particle systems and interactive parameters.
icon: shapes
cover: ../../../.gitbook/assets/cover-en-creatief.png
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

# Algorithmic Art

| | |
| --- | --- |
| **Maker** | Anthropic (official) |
| **Works in** | Claude app, Claude Code, API |
| **Cost** | Free (Apache 2.0) |
| **Source** | [github.com/anthropics/skills/tree/main/skills/algorithmic-art](https://github.com/anthropics/skills/tree/main/skills/algorithmic-art) |

## What does it do?

With this skill Claude makes art with code in p5.js, with a fixed 'seed' so you can reproduce a nice result. You get sliders to explore parameters live. Meant for original work, not for imitating existing artists.

## When do you use it?

* You want a unique background, wallpaper or visual.
* You want to play with generative art.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Create a flow field in the colours of the Dutch flag with sliders for density and speed.
```
{% endcode %}

**What you get:** An interactive art page.

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
npx skills add anthropics/skills --skill algorithmic-art
```

Add `-g` to install it globally (for all your projects). `npx skills list` shows what is installed.
{% endtab %}
{% endtabs %}

<a href="https://github.com/anthropics/skills/tree/main/skills/algorithmic-art" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Creative & video</a>
