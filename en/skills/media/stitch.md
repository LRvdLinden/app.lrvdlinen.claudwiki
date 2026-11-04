---
description: >-
  Working with Google Stitch: generating designs, extracting design.md and converting to React or shadcn/ui.
icon: object-group
cover: ../../../.gitbook/assets/cover-en-media.png
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

# Google Stitch Skills

| | |
| --- | --- |
| **Maker** | Google Labs (official, by the makers) |
| **Works in** | Claude Code (+ Codex, Gemini CLI, Cursor) |
| **Cost** | Free |
| **Source** | [github.com/google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) |

## What does it do?

Skills for Google Stitch, Google's AI design tool: generating and improving designs, extracting a `design.md` from an existing design, managing your design system and converting designs to React, React Native, shadcn/ui or a Vite dashboard.

## When do you use it?

* You design in Stitch and want to bring it to code quickly.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Convert this Stitch design into React components with shadcn/ui.
```
{% endcode %}

**What you get:** Component code that follows the design.

## Install

{% tabs %}
{% tab title="Claude Code" %}
```bash
npx plugins add google-labs-code/stitch-skills --scope project --target claude-code
```
{% endtab %}

{% tab title="npx skills" %}
With the open-source [skills CLI](https://github.com/vercel-labs/skills) you install skills for Claude Code and other agents. All you need is Node.js:

```bash
npx skills add google-labs-code/stitch-skills
```

Add `-g` to install it globally (for all your projects). `npx skills list` shows what is installed.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/google-labs-code/stitch-skills" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Audio, images & visuals</a>
