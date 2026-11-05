---
description: >-
  See a feature you like in an app? REA works out how it works, down to the binary level, so you can rebuild it.
icon: microchip
cover: ../../../.gitbook/assets/cover-en-klonen.png
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

# REA – Reverse Engineer Anything

{% hint style="danger" %}
**Spotted on social.** Went viral through 'I Tried 23 Viral Claude Skills' (Artificial Corner), among others.
{% endhint %}

| | |
| --- | --- |
| **Maker** | morluto (community) |
| **Works in** | Claude Code (+ Codex, Cursor, Gemini CLI and more) |
| **Cost** | Free (open source) |
| **Source** | [github.com/morluto/rea](https://github.com/morluto/rea) |

## What does it do?

REA (Reverse Engineer Anything) is the 'clone skill' for apps. It analyses native apps, Electron/JavaScript apps, packaged programs, firmware and web apps, explains how a feature works, compares versions, decompiles code and guides a reconstruction. For native analysis it can use Hopper, Ghidra or IDA. REA can also build a test environment (AgentEnv) from a live web app.

## When do you use it?

* You see a feature in an app and want to build a simpler version in your own app.
* You want to understand exactly what a program on your computer does.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
How does the search bar in this desktop app work? Build a simple version for my app.
```
{% endcode %}

**What you get:** An explanation of how it works plus your own, simplified implementation.

## Install

{% tabs %}
{% tab title="Installer" %}
```bash
npx rea-agents setup
```

Setup registers REA with your agent (Claude Code, Codex, Cursor and more) and installs the matching workflow instructions. Only install from the official sources: the repo, [rea.tools](https://rea.tools/) or the `rea-agents` npm package.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Only use REA on software you're allowed to analyse; some licences forbid reverse engineering.
* Only use this for your own sites and apps, or with permission. Logos, brand assets and copy belong to their owners, and rebuilding a site to impersonate someone (phishing) is illegal. Also check the site's terms of service.
{% endhint %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/morluto/rea" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Clone sites & apps</a>
