---
description: >-
  Creates and edits PowerPoint presentations, including templates, speaker notes and layouts.
icon: file-powerpoint
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

# PowerPoint (pptx)

| | |
| --- | --- |
| **Maker** | Anthropic (official) |
| **Works in** | Claude app, Claude Code, API |
| **Cost** | Free with a paid plan (source-available) |
| **Source** | [github.com/anthropics/skills/tree/main/skills/pptx](https://github.com/anthropics/skills/tree/main/skills/pptx) |

## What does it do?

With the PowerPoint skill Claude builds complete presentations as `.pptx`: slides with titles, bullet points, images, charts and speaker notes. It can also read an existing presentation or template (`.potx`), extract its text, edit slides, or merge and split presentations.

## When do you use it?

* You need to deliver a presentation as a PowerPoint file.
* You want an existing presentation updated in your house style.
* You want the content of a presentation summarised.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Create a 10-slide presentation about our neighbourhood plans for 2027, with speaker notes on every slide.
```
{% endcode %}

**What you get:** A `.pptx` you can open in PowerPoint or Keynote.

{% code title="Example 2: what you type" overflow="wrap" %}
```
Use template brand.potx and turn this report into slides.
```
{% endcode %}

**What you get:** A presentation in your template.

## Install

{% tabs %}
{% tab title="Claude app" %}
This skill is **already built in** for paid plans.

1. Open **Settings → Capabilities**.
2. Turn on **Code execution and file creation**.
3. Scroll to **Skills** and switch the skill on.

Then just ask for what you want in plain language; Claude loads the skill itself.

In the Claude app, Claude already uses this skill automatically as soon as you ask for a file of this type.
{% endtab %}

{% tab title="Claude Code" %}
First add the marketplace, then install the plugin. Type this in a Claude Code session:

```bash
/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropic-agent-skills
```

Restart Claude Code if the skill doesn't appear right away. Check with `/plugin` that it is enabled.

This installs **document-skills**: Word, PDF, PowerPoint and Excel in one go.
{% endtab %}

{% tab title="npx skills" %}
With the open-source [skills CLI](https://github.com/vercel-labs/skills) you install skills for Claude Code and other agents. All you need is Node.js:

```bash
npx skills add anthropics/skills --skill pptx
```

Add `-g` to install it globally (for all your projects). `npx skills list` shows what is installed.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Want a quick web presentation instead of a file? Have a look at [Frontend Slides](../design/frontend-slides.md).
{% endhint %}

<a href="https://github.com/anthropics/skills/tree/main/skills/pptx" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Documents & office</a>
