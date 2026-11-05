---
description: >-
  Pixel-perfect copy of a web page: paste a URL and get a measured Vite + React replica.
icon: ruler-combined
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

# Perfect Web Clone

| | |
| --- | --- |
| **Maker** | ericshang98 (community) |
| **Works in** | Claude Code (+ other agents) |
| **Cost** | Free (open source) |
| **Source** | [github.com/ericshang98/perfect-web-clone-skill](https://github.com/ericshang98/perfect-web-clone-skill) |

## What does it do?

This skill is a strict playbook for pixel-perfect cloning. After one request (`clone https://…`) the agent must capture, plan, build, measure and repair until the clone passes a set of gates: complete capture, complete structure, real interactions, weight and a visual score per section. The helper tool `pwc` does the measuring and looking.

## When do you use it?

* You want the copy to really look identical down to the pixel.
* You want measurable proof that the clone is right.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
clone https://my-landing-page.com
```
{% endcode %}

**What you get:** A Vite + React project plus a report with scores per section.

## Install

{% tabs %}
{% tab title="Manual" %}
```bash
git clone https://github.com/ericshang98/perfect-web-clone-skill.git ~/.claude/skills/perfect-web-clone
```

For measuring you also need the [Perfect-Web-Clone (pwc)](https://github.com/ericshang98/Perfect-Web-Clone) tool; see the README.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Only use this for your own sites and apps, or with permission. Logos, brand assets and copy belong to their owners, and rebuilding a site to impersonate someone (phishing) is illegal. Also check the site's terms of service.
{% endhint %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/ericshang98/perfect-web-clone-skill" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Clone sites & apps</a>
