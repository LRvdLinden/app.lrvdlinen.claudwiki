---
description: >-
  The skills Sentry uses internally: finding bugs, code reviews, commits, PRs and security reviews.
icon: bug
cover: ../../../.gitbook/assets/cover-en-cloud.png
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

# Sentry Skills

| | |
| --- | --- |
| **Maker** | Sentry (official, by the makers) |
| **Works in** | Claude Code |
| **Cost** | Free |
| **Source** | [github.com/getsentry/skills](https://github.com/getsentry/skills) |

## What does it do?

Sentry shares the skills of its own engineers: `find-bugs`, `code-review`, `security-review`, `commit`, `pr-writer`, `iterate-pr`, a GitHub Actions security review, `skill-scanner` (checks skills for risks) and more.

## When do you use it?

* You want to adopt professional dev workflows.
* You want to scan other people's skills for risks.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
/find-bugs
```
{% endcode %}

**What you get:** A list of likely bugs in your current changes.

## Install

{% tabs %}
{% tab title="Claude Code" %}
```bash
claude plugin marketplace add getsentry/skills
claude plugin install sentry-skills@sentry-skills
```
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* For error monitoring itself: the `sentry` plugin in the official marketplace.
{% endhint %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/getsentry/skills" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Data, cloud & payments</a>
