---
description: >-
  Pixel-perfect Instagram carousels in your own brand style, exported to PNG and PDF.
icon: images
cover: ../../../.gitbook/assets/cover-en-content.png
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

# Instagram Carousel

| | |
| --- | --- |
| **Maker** | Jeevan Bavandla (community) |
| **Works in** | Claude Code, Claude app |
| **Cost** | Free (MIT) |
| **Source** | [github.com/jeevanbavandla/instagram-carousel-skill](https://github.com/jeevanbavandla/instagram-carousel-skill) |

## What does it do?

On first use you set up your brand once (name, handle, photo, accent colour, style). After that Claude creates carousels in four styles: Bold Impact, Tweet Post, Clean Editorial and Product Showcase, with a progress bar, arrows and a CTA slide. Export to PNG and PDF.

## When do you use it?

* You want to make carousels quickly without Canva.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Create a 6-slide carousel: '5 tips for a safer neighbourhood'.
```
{% endcode %}

**What you get:** Six slides in your brand style, ready to post.

## Install

{% tabs %}
{% tab title="npx skills" %}
With the open-source [skills CLI](https://github.com/vercel-labs/skills) you install skills for Claude Code and other agents. All you need is Node.js:

```bash
npx skills add jeevanbavandla/instagram-carousel-skill -g
```

Add `-g` to install it globally (for all your projects). `npx skills list` shows what is installed.
{% endtab %}

{% tab title="Claude app" %}
The repo has a separate `claude-ai` folder with instructions for using the skill in the Claude app (paste a file, about 5 minutes).
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/jeevanbavandla/instagram-carousel-skill" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Writing, content & marketing</a>
