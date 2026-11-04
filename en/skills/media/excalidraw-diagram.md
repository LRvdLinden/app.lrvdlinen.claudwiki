---
description: >-
  Creates beautiful Excalidraw diagrams from plain language: diagrams that explain, not just boxes and arrows.
icon: pen-to-square
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

# Excalidraw Diagram

| | |
| --- | --- |
| **Maker** | Cole Medin (community) |
| **Works in** | Claude Code (+ OpenCode) |
| **Cost** | Free |
| **Source** | [github.com/coleam00/excalidraw-diagram-skill](https://github.com/coleam00/excalidraw-diagram-skill) |

## What does it do?

The shapes in the diagram follow the idea they explain: fans for one-to-many, timelines for sequences, converging lines for aggregation. So you don't get a boring grid of cards but a diagram that tells a story.

## When do you use it?

* You want to explain an architecture, process or idea visually.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Draw how an alert travels from the control room via the server to the app.
```
{% endcode %}

**What you get:** An .excalidraw file.

## Install

{% tabs %}
{% tab title="Manual" %}
Copy the skill folder to your personal skills folder (for all projects) or to `.claude/skills/` in one project:

```bash
git clone https://github.com/coleam00/excalidraw-diagram-skill.git
cp -r excalidraw-diagram-skill .claude/skills/excalidraw-diagram   # or ~/.claude/skills/ for all your projects
```
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/coleam00/excalidraw-diagram-skill" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Audio, images & visuals</a>
