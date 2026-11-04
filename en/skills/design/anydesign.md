---
description: >-
  Analyses an image, website or Figma file and turns it into a structured design.md.
icon: eye-dropper
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

# AnyDesign

| | |
| --- | --- |
| **Maker** | uxKero (community) |
| **Works in** | Claude Code, Claude app |
| **Cost** | Free |
| **Source** | [github.com/uxKero/anydesign](https://github.com/uxKero/anydesign) |

## What does it do?

Turns images, websites and Figma files into a readable design specification: design system, component inventory and instructions to rebuild it. Single elements (a navbar, a 3D illustration) can be copied as a 'rebuild prompt'.

## When do you use it?

* You want to capture the style of your own design so you can keep building consistently.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Make a design.md from this screenshot of my app.
```
{% endcode %}

**What you get:** Colours, typography, spacing and components at a glance.

## Install

{% tabs %}
{% tab title="Manual" %}
Copy the skill folder to your personal skills folder (for all projects) or to `.claude/skills/` in one project:

```bash
git clone https://github.com/uxKero/anydesign.git
cp -r anydesign ~/.claude/skills/
```
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Use this for your own designs or with permission; don't just copy someone else's design.
{% endhint %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/uxKero/anydesign" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Design & frontend</a>
