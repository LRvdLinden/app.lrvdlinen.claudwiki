---
description: >-
  Lets AIs debate each other so you get honest, challenged advice instead of a yes-man.
icon: comments
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

# Debate Skills

{% hint style="danger" %}
**Spotted on social.** Bart Boonstra calls a 'Debate Skill' his favourite: *'AI agrees with you nine times out of ten. Not anymore.'* He doesn't say which repo he uses exactly; this is a well-documented variant.
{% endhint %}

| | |
| --- | --- |
| **Maker** | biyachuev (community) |
| **Works in** | Claude Code (+ Codex CLI for the two-model debates) |
| **Cost** | Free (open source) |
| **Source** | [github.com/biyachuev/claude-debate-skills](https://github.com/biyachuev/claude-debate-skills) |

## What does it do?

This collection contains three skills. **strategy-debate**: Claude and Codex (OpenAI) each build a position independently, critique each other and reach a synthesis. **creator-critic**: one generates options, the other assesses them; this one also works with Claude alone. **options-challenge**: compares several routes, tests the trade-offs and ranks them (requires Codex). Because the models have different blind spots, more comes to the surface than with a single answer.

## When do you use it?

* You face a strategic choice and don't want a yes-man.
* You want to pressure-test ideas (names, prices, positioning).

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
/strategy-debate Topic: Should I offer my app for free with ads or as a paid app? Constraints: small audience, solo developer.
```
{% endcode %}

**What you get:** Two well-argued positions, mutual critique and final advice.

{% code title="Example 2: what you type" overflow="wrap" %}
```
/creator-critic Creator: Claude. Critic: Claude. Finalizer: Claude. Log File: none. Brief: Come up with names for a neighbourhood app.
```
{% endcode %}

**What you get:** Options, critique and a short shortlist, with Claude only.

## Install

{% tabs %}
{% tab title="Claude Code" %}
```bash
claude plugin install --source https://github.com/biyachuev/claude-debate-skills.git
```

For the two-model debates you also need the Codex CLI:

```bash
npm install -g @openai/codex && codex login
```

Then install the Codex plugin in Claude Code with `/install-plugin codex`.
{% endtab %}

{% tab title="Manual" %}
Copy the skill folder to your personal skills folder (for all projects) or to `.claude/skills/` in one project:

```bash
git clone https://github.com/biyachuev/claude-debate-skills.git
cd claude-debate-skills && ./install.sh   # creates symlinks in ~/.claude/skills/
```
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Your question may go to both Anthropic and OpenAI: don't put sensitive information in it.
* Claude only? Use `creator-critic` with Claude in all roles.
{% endhint %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/biyachuev/claude-debate-skills" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Thinking & planning</a>
