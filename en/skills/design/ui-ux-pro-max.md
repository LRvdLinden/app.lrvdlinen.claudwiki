---
description: >-
  A searchable design library with dozens of styles, 192 colour palettes, 74 font pairings and 119 UX guidelines.
icon: layer-group
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

# UI UX Pro Max

{% hint style="danger" %}
**Spotted on social.** Tip from Bart Boonstra: *'UI UX Pro Max makes every layout 1000x more professional. Literally.'*
{% endhint %}

| | |
| --- | --- |
| **Maker** | nextlevelbuilder (community) |
| **Works in** | Claude Code (+ Cursor, Copilot, Codex and more) |
| **Cost** | Free (open source) |
| **Source** | [github.com/nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) |

## What does it do?

UI UX Pro Max is one of the most popular community skills. It gives Claude a local, searchable database of UI styles (glassmorphism, bento grid, brutalism, dark mode…), colour palettes per product type, font pairings with Google Fonts, UX guidelines and anti-patterns, icons, animation presets and chart types. Claude looks up the best-fitting style, colours and typography for your request and applies them consistently. The package also includes extra skills for banners, branding, design systems and slides.

## When do you use it?

* You are building a website, dashboard or app and want it to look professional straight away.
* You want a design system (colours, fonts, spacing) proposed.
* You want an existing screen reviewed for UX and accessibility.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Create a dashboard for an alerting app. Find a fitting style and colour palette.
```
{% endcode %}

**What you get:** A dashboard with a well-reasoned style, palette and font choice.

{% code title="Example 2: what you type" overflow="wrap" %}
```
Review this settings screen for UX mistakes and accessibility.
```
{% endcode %}

**What you get:** A list of concrete improvements.

## Install

{% tabs %}
{% tab title="Claude Code" %}
First add the marketplace, then install the plugin. Type this in a Claude Code session:

```bash
/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill
/plugin install ui-ux-pro-max@ui-ux-pro-max-skill
```

Restart Claude Code if the skill doesn't appear right away. Check with `/plugin` that it is enabled.
{% endtab %}

{% tab title="CLI (recommended)" %}
The makers recommend their own installer:

```bash
npm install -g ui-ux-pro-max-cli
cd /path/to/your/project
uipro init --ai claude            # this project only
uipro init --ai claude --global   # for all your projects (~/.claude/skills/)
```

Use `ui-ux-pro-max-cli`; the older `uipro-cli` package is outdated.
{% endtab %}

{% tab title="Claude app" %}
1. Download the repo as a ZIP: [github.com/nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) → **Code → Download ZIP**.
2. Unzip and find the folder `.claude/skills/ui-ux-pro-max` (it contains `SKILL.md`).
3. Zip **only that folder** into a new ZIP. The folder name must match the skill name.
4. Go to **Settings → Capabilities → Skills** and click **Upload skill**.
5. Switch the skill on.

Skills in the Claude app require a Pro, Max, Team or Enterprise plan, and **Code execution and file creation** must be turned on.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Combine with [Frontend Design](frontend-design.md) or [Impeccable](impeccable.md) for even more control.
{% endhint %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/nextlevelbuilder/ui-ux-pro-max-skill" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Design & frontend</a>
