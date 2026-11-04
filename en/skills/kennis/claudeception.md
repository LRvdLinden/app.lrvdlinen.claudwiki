---
description: >-
  Lets Claude Code write new skills itself from what it discovers while working.
icon: infinity
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

# Claudeception

| | |
| --- | --- |
| **Maker** | blader (community) |
| **Works in** | Claude Code |
| **Cost** | Free (open source) |
| **Source** | [github.com/blader/Claudeception](https://github.com/blader/Claudeception) |

## What does it do?

Every session an AI agent starts from scratch. If Claude spent an hour solving an obscure error, that knowledge is gone next time. Claudeception fixes that: when Claude discovers something non-obvious (a workaround, debugging trick or project pattern), it saves it as a new skill. With a similar problem that skill is loaded automatically.

## When do you use it?

* You often run into the same kind of problems.
* You want your setup to get smarter the more you work.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
/claudeception
```
{% endcode %}

**What you get:** Claude reviews the session and turns it into a new skill where useful.

{% code title="Example 2: what you type" overflow="wrap" %}
```
Save this as a skill.
```
{% endcode %}

**What you get:** A new SKILL.md in your skills folder.

## Install

{% tabs %}
{% tab title="Manual" %}
Copy the skill folder to your personal skills folder (for all projects) or to `.claude/skills/` in one project:

```bash
git clone https://github.com/blader/Claudeception.git ~/.claude/skills/claudeception
```

Optional: copy the activator hook to `~/.claude/hooks/` (see the README).
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/blader/Claudeception" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Knowledge & memory</a>
