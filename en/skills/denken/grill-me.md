---
description: >-
  Have Claude grill your plan relentlessly before it starts, and summarise long chats so you can continue.
icon: fire-flame-curved
cover: ../../../.gitbook/assets/cover-en-denken.png
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

# Grill Me & Handoff

{% hint style="danger" %}
**Spotted on social.** Went viral through 'I Tried 23 Viral Claude Skills' (Artificial Corner), among others.
{% endhint %}

| | |
| --- | --- |
| **Maker** | Matt Pocock (community) |
| **Works in** | Claude Code (+ Cursor, Codex and other agents) |
| **Cost** | Free (open source) |
| **Source** | [github.com/mattpocock/skills](https://github.com/mattpocock/skills) |

## What does it do?

Two skills stand out in Matt Pocock's popular collection. **Grill Me** is a 'relentless interview': Claude keeps asking about your goals, audience, scope and what can go wrong, until your plan is really sharp. **Handoff** condenses a long conversation into a handoff document, so you can continue in a new chat or with another agent without losing context. The collection also contains skills for TDD, code reviews, specs, tickets and more.

## When do you use it?

* You have an idea but don't know exactly what you want yet.
* Your conversation is getting too long and Claude starts forgetting things.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
/grill-me I want to build an app for volunteers in my neighbourhood.
```
{% endcode %}

**What you get:** A series of sharp questions, one at a time, until everything is clear.

{% code title="Example 2: what you type" overflow="wrap" %}
```
/handoff
```
{% endcode %}

**What you get:** A compact handoff document to paste into a new session.

## Install

{% tabs %}
{% tab title="Claude Code" %}
The collection is in the official marketplace:

```bash
claude plugin install mattpocock-skills@claude-plugins-official
```
{% endtab %}

{% tab title="npx skills" %}
With the open-source [skills CLI](https://github.com/vercel-labs/skills) you install skills for Claude Code and other agents. All you need is Node.js:

```bash
npx skills@latest add mattpocock/skills
```

Add `-g` to install it globally (for all your projects). `npx skills list` shows what is installed.

Pick the skills you want in the installer and include `setup-matt-pocock-skills`. Update: `npx skills@latest update`.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/mattpocock/skills" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Thinking & planning</a>
