---
description: >-
  Searching and reading the web for your agent: search, scrape pages, leads, SEO audits and deep research.
icon: spider
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

# Firecrawl

| | |
| --- | --- |
| **Maker** | Firecrawl (official, by the makers) |
| **Works in** | Claude Code (API key required) |
| **Cost** | Plugin free; Firecrawl services at their prices |
| **Source** | [github.com/firecrawl/firecrawl-claude-plugin](https://github.com/firecrawl/firecrawl-claude-plugin) |

## What does it do?

Connects Claude to Firecrawl's search and scrape tools, with skills for deep research, reading documentation, finding and enriching leads, job postings, brand identity and SEO audits.

## When do you use it?

* You want thorough web research with clean page content.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Do deep research on neighbourhood watch apps in the Netherlands and summarise it.
```
{% endcode %}

**What you get:** A report with sources.

## Install

{% tabs %}
{% tab title="Claude Code" %}
First add the marketplace, then install the plugin. Type this in a Claude Code session:

```bash
/plugin marketplace add firecrawl/firecrawl-claude-plugin
/plugin install firecrawl@firecrawl
```

Restart Claude Code if the skill doesn't appear right away. Check with `/plugin` that it is enabled.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/firecrawl/firecrawl-claude-plugin" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Data, cloud & payments</a>
