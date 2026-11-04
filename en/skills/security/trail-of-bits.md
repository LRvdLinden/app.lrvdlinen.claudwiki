---
description: >-
  Dozens of professional security skills from a renowned security firm: audits, Semgrep, fuzzing and supply chain.
icon: user-shield
cover: ../../../.gitbook/assets/cover-en-security.png
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

# Trail of Bits Security

| | |
| --- | --- |
| **Maker** | Trail of Bits |
| **Works in** | Claude Code (+ Codex) |
| **Cost** | Free (open source) |
| **Source** | [github.com/trailofbits/skills](https://github.com/trailofbits/skills) |

## What does it do?

Trail of Bits is a renowned security company. Their marketplace contains skills and plugins for security analysis: differential reviews, static analysis, writing Semgrep rules, supply-chain risks, insecure defaults, property-based testing, mutation testing, finding vulnerability variants and more.

## When do you use it?

* You want your own code (for example an app with user data) audited.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Check my dependencies for supply-chain risks.
```
{% endcode %}

**What you get:** A risk overview per package.

## Install

{% tabs %}
{% tab title="Claude Code" %}
```bash
/plugin marketplace add trailofbits/skills
```

Then choose via `/plugin` which plugins you want to install.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Only use these skills on code and systems you have permission for.
{% endhint %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/trailofbits/skills" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Security & science</a>
