---
description: >-
  A structured way to write documents, proposals and specs together with Claude.
icon: people-arrows
cover: ../../../.gitbook/assets/cover-en-documenten.png
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

# Doc Co-authoring

| | |
| --- | --- |
| **Maker** | Anthropic (official) |
| **Works in** | Claude app, Claude Code, API |
| **Cost** | Free (Apache 2.0) |
| **Source** | [github.com/anthropics/skills/tree/main/skills/doc-coauthoring](https://github.com/anthropics/skills/tree/main/skills/doc-coauthoring) |

## What does it do?

Instead of producing a text in one go, this skill guides you through a fixed process: first Claude gathers the context from you, then it writes and refines in rounds, and finally it checks whether the document works for the reader. Useful for proposals, technical specifications, decision documents and policy papers.

## When do you use it?

* You are writing a proposal, policy note or spec and want it to be really solid.
* You have lots of loose information that needs to become one clear piece.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Help me write a proposal to the municipality for more lighting in the park.
```
{% endcode %}

**What you get:** Claude first asks targeted questions, then writes in steps and checks the result from the reader's point of view.

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
npx skills add anthropics/skills --skill doc-coauthoring
```

Add `-g` to install it globally (for all your projects). `npx skills list` shows what is installed.
{% endtab %}
{% endtabs %}

<a href="https://github.com/anthropics/skills/tree/main/skills/doc-coauthoring" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Documents & office</a>
