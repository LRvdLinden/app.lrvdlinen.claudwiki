---
description: >-
  Thirteen skills that run an Instagram account: Reels with scorable hooks, captions, carousels, stories and DMs.
icon: camera-retro
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

# Instagram Agent

{% hint style="danger" %}
**Spotted on social.** Widely shared by Instagram creators; several blogs have written complete installation guides for it.
{% endhint %}

| | |
| --- | --- |
| **Maker** | Jake Schincariol (community) |
| **Works in** | Claude Code, Claude app |
| **Cost** | Free (MIT), no API key needed |
| **Source** | [github.com/Jakeschincariol/instagram-agent-skill](https://github.com/Jakeschincariol/instagram-agent-skill) |

## What does it do?

A pack of thirteen skills (`ig-reel`, `ig-caption`, `ig-carousel`, `ig-story`, `ig-viral`, `ig-plan`, `ig-audit`, `ig-profile`, `ig-dm`, `ig-reply`, `ig-comment`, `ig-repurpose` and `ig-human`). They write Reels based on 26 hook formulas and score the hook, research what goes viral, lint your captions and remove AI language. Nothing needs to be connected.

## When do you use it?

* You want to post consistently for your app or organisation.
* You want better hooks and captions.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Write a 30-second Reel script about 'Why your neighbours are your best security' with a scoring hook.
```
{% endcode %}

**What you get:** A script with a hook score and caption.

{% code title="Example 2: what you type" overflow="wrap" %}
```
Audit my Instagram profile and give 5 improvements.
```
{% endcode %}

**What you get:** A profile audit.

## Install

{% tabs %}
{% tab title="Claude Code" %}
First add the marketplace, then install the plugin. Type this in a Claude Code session:

```bash
/plugin marketplace add Jakeschincariol/instagram-agent-skill
/plugin install instagram-agent
```

Restart Claude Code if the skill doesn't appear right away. Check with `/plugin` that it is enabled.
{% endtab %}

{% tab title="Manual" %}
Copy the skill folder to your personal skills folder (for all projects) or to `.claude/skills/` in one project:

```bash
git clone https://github.com/Jakeschincariol/instagram-agent-skill.git
cp -r instagram-agent-skill/skills/ig-* ~/.claude/skills/
```
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/Jakeschincariol/instagram-agent-skill" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Writing, content & marketing</a>
