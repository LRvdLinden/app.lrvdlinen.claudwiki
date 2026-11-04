---
description: >-
  Teaches Claude to make videos and animations in code (React), locally and without limits.
icon: clapperboard
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

# Remotion

{% hint style="danger" %}
**Spotted on social.** Tip from Bart Boonstra: *'Remotion is the skill that teaches Claude to make animations in code. All the animations in my videos are built with it.'*
{% endhint %}

| | |
| --- | --- |
| **Maker** | Remotion (official, by the makers) |
| **Works in** | Claude Code (+ Codex, Cursor and more) |
| **Cost** | Skills free; Remotion itself has its own licence |
| **Source** | [github.com/remotion-dev/skills](https://github.com/remotion-dev/skills) |

## What does it do?

Remotion is a framework for making videos with React code. The official Remotion skills teach Claude the best practices: setting up a project, animations and transitions, captions, maps, multimedia, interactivity and rendering to MP4. You describe what you want to see, Claude writes the code and you render the video locally on your own computer.

## When do you use it?

* You make content for social media and want animations or infographics.
* You want to generate videos with captions or data visualisations.
* You want a fixed video template you reuse again and again.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Make a 15-second vertical Remotion video (1080x1920) in which the five main features of my app fly in one by one.
```
{% endcode %}

**What you get:** A Remotion project you render to an MP4.

{% code title="Example 2: what you type" overflow="wrap" %}
```
Add animated captions to this video.
```
{% endcode %}

**What you get:** A video with captions in your own style.

## Install

{% tabs %}
{% tab title="npx skills" %}
With the open-source [skills CLI](https://github.com/vercel-labs/skills) you install skills for Claude Code and other agents. All you need is Node.js:

```bash
npx skills add remotion-dev/skills
```

Add `-g` to install it globally (for all your projects). `npx skills list` shows what is installed.
{% endtab %}

{% tab title="Requirements" %}
You need Node.js and a Remotion project (`npx create-video@latest`). Check the [Remotion licence](https://www.remotion.dev/license): companies above a certain size need a paid licence.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Start with the `remotion-best-practices` skill; it points Claude to the right sub-skill.
{% endhint %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/remotion-dev/skills" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Creative & video</a>
