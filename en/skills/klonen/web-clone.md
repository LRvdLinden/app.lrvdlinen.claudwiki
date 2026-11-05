---
description: >-
  A method for faithfully cloning websites without made-up code: real source first, then rebuild.
icon: code-compare
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

# Web Clone (real source first)

| | |
| --- | --- |
| **Maker** | Jane-xiaoer (community) |
| **Works in** | Claude Code |
| **Cost** | Free (open source) |
| **Source** | [github.com/Jane-xiaoer/claude-skill-web-clone](https://github.com/Jane-xiaoer/claude-skill-web-clone) |

## What does it do?

AI tools often produce 'clone analyses' full of plausible-looking but fabricated code. This skill works differently: a six-step decision tree and scripts that fetch the real source first. Static HTML/CSS sites are mirrored with `wget --mirror`, React, Vue and Next sites are rebuilt on a template, and for multi-page sites all routes are mapped first. There is also an approach for WebGL sites.

## When do you use it?

* You want a clone based on the real code, not guesswork.
* You want to view or study a site offline.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Clone my portfolio site so I can edit it offline.
```
{% endcode %}

**What you get:** A local copy using the best-fitting method.

## Install

{% tabs %}
{% tab title="Manual" %}
```bash
git clone https://github.com/Jane-xiaoer/claude-skill-web-clone.git ~/.claude/skills/web-clone
```
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Only use this for your own sites and apps, or with permission. Logos, brand assets and copy belong to their owners, and rebuilding a site to impersonate someone (phishing) is illegal. Also check the site's terms of service.
{% endhint %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/Jane-xiaoer/claude-skill-web-clone" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Clone sites & apps</a>
