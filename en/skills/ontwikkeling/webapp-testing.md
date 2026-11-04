---
description: >-
  Tests local web apps with Playwright: clicking, taking screenshots and reading browser logs.
icon: vial
cover: ../../../.gitbook/assets/cover-en-ontwikkeling.png
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

# Webapp Testing

| | |
| --- | --- |
| **Maker** | Anthropic (official) |
| **Works in** | Claude Code (and Claude app with code execution) |
| **Cost** | Free (Apache 2.0) |
| **Source** | [github.com/anthropics/skills/tree/main/skills/webapp-testing](https://github.com/anthropics/skills/tree/main/skills/webapp-testing) |

## What does it do?

A toolkit that lets Claude operate your local web application through Playwright: open pages, fill in forms, test buttons, take screenshots and read console logs to track down errors.

## When do you use it?

* You want to check that your website or PWA still works after a change.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Start the app on localhost:3000, test the login form and take a screenshot of every step.
```
{% endcode %}

**What you get:** A test report with screenshots and any errors.

## Install

{% tabs %}
{% tab title="Claude app" %}
This skill is **already built in** for paid plans.

1. Open **Settings → Capabilities**.
2. Turn on **Code execution and file creation**.
3. Scroll to **Skills** and switch the skill on.

Then just ask for what you want in plain language; Claude loads the skill itself.
{% endtab %}

{% tab title="Claude Code" %}
First add the marketplace, then install the plugin. Type this in a Claude Code session:

```bash
/plugin marketplace add anthropics/skills
/plugin install example-skills@anthropic-agent-skills
```

Restart Claude Code if the skill doesn't appear right away. Check with `/plugin` that it is enabled.

This installs the whole **example-skills** pack (including this skill).
{% endtab %}

{% tab title="npx skills" %}
With the open-source [skills CLI](https://github.com/vercel-labs/skills) you install skills for Claude Code and other agents. All you need is Node.js:

```bash
npx skills add anthropics/skills --skill webapp-testing
```

Add `-g` to install it globally (for all your projects). `npx skills list` shows what is installed.
{% endtab %}
{% endtabs %}

<a href="https://github.com/anthropics/skills/tree/main/skills/webapp-testing" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Development & code</a>
