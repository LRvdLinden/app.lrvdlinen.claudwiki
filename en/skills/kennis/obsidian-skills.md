---
description: >-
  Official skills from Obsidian's creator: notes, Bases, JSON Canvas and the Obsidian CLI.
icon: note-sticky
cover: ../../../.gitbook/assets/cover-en-kennis.png
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

# Obsidian Skills

| | |
| --- | --- |
| **Maker** | Steph Ango / kepano (creator of Obsidian) |
| **Works in** | Claude Code (+ Codex, OpenCode) |
| **Cost** | Free |
| **Source** | [github.com/kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) |

## What does it do?

Skills for working with your Obsidian vault: **obsidian-markdown** (Obsidian's flavour of Markdown), **obsidian-bases**, **json-canvas**, **obsidian-cli** (read, create and search notes via the CLI) and **defuddle** (pull in web pages cleanly).

## When do you use it?

* You use Obsidian as a second brain.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Turn today's meeting notes into a note in my vault with links to the projects involved.
```
{% endcode %}

**What you get:** A clean Obsidian note with [[links]].

## Install

{% tabs %}
{% tab title="Claude Code" %}
First add the marketplace, then install the plugin. Type this in a Claude Code session:

```bash
/plugin marketplace add kepano/obsidian-skills
/plugin install obsidian@obsidian-skills
```

Restart Claude Code if the skill doesn't appear right away. Check with `/plugin` that it is enabled.
{% endtab %}

{% tab title="npx skills" %}
With the open-source [skills CLI](https://github.com/vercel-labs/skills) you install skills for Claude Code and other agents. All you need is Node.js:

```bash
npx skills add https://github.com/kepano/obsidian-skills
```

Add `-g` to install it globally (for all your projects). `npx skills list` shows what is installed.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Want diagrams in Obsidian? Have a look at [Axton's Obsidian Visual Skills](https://github.com/axtonliu/axton-obsidian-visual-skills) for Excalidraw, Mermaid and Canvas.
{% endhint %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/kepano/obsidian-skills" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Knowledge & memory</a>
