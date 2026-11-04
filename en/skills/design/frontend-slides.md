---
description: >-
  Beautiful, animated HTML presentations, or convert PowerPoints to the web.
icon: display
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

# Frontend Slides

| | |
| --- | --- |
| **Maker** | Zara Zhang (community) |
| **Works in** | Claude Code (the SKILL.md also works in other agents) |
| **Cost** | Free (open source) |
| **Source** | [github.com/zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) |

## What does it do?

Frontend Slides creates presentations as a single HTML file with animations, instead of a PowerPoint. You don't need to be a designer: the skill lets you choose between styles visually instead of asking abstract questions. It can also convert an existing `.pptx` into a web presentation and export to PDF.

## When do you use it?

* You are giving a talk or pitch and want something that stands out.
* You want to modernise an old PowerPoint.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Create an 8-slide pitch for my new app, with slick animations.
```
{% endcode %}

**What you get:** One HTML file you present in the browser.

## Install

{% tabs %}
{% tab title="Claude Code" %}
First add the marketplace, then install the plugin. Type this in a Claude Code session:

```bash
/plugin marketplace add https://github.com/zarazhangrui/frontend-slides
/plugin install frontend-slides@frontend-slides
```

Restart Claude Code if the skill doesn't appear right away. Check with `/plugin` that it is enabled.
{% endtab %}

{% tab title="Manual" %}
Copy the skill folder to your personal skills folder (for all projects) or to `.claude/skills/` in one project:

```bash
git clone https://github.com/zarazhangrui/frontend-slides.git ~/.claude/skills/frontend-slides
```
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* There is a beginner video in the repo's README.
{% endhint %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/zarazhangrui/frontend-slides" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Design & frontend</a>
