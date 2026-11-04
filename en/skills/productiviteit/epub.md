---
description: >-
  Converts markdown, research or chat summaries into a neat e-book (EPUB3).
icon: book
cover: ../../../.gitbook/assets/cover-en-productiviteit.png
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

# Markdown to EPUB

| | |
| --- | --- |
| **Maker** | smerchek (community) |
| **Works in** | Claude Code, Claude app |
| **Cost** | Free |
| **Source** | [github.com/smerchek/claude-epub-skill](https://github.com/smerchek/claude-epub-skill) |

## What does it do?

Turns markdown documents into professional EPUB3 e-books that work on Apple Books, Kobo, e-readers and more. Perfect for reading research or long articles offline.

## When do you use it?

* You want to read a long document or this wiki as an e-book.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Turn these 5 articles into one e-book with a table of contents.
```
{% endcode %}

**What you get:** An .epub file.

## Install

{% tabs %}
{% tab title="Claude app" %}
1. Download the repo as a ZIP: [github.com/smerchek/claude-epub-skill](https://github.com/smerchek/claude-epub-skill) → **Code → Download ZIP**.
2. Unzip and find the folder `markdown-to-epub` (it contains `SKILL.md`).
3. Zip **only that folder** into a new ZIP. The folder name must match the skill name.
4. Go to **Settings → Capabilities → Skills** and click **Upload skill**.
5. Switch the skill on.

Skills in the Claude app require a Pro, Max, Team or Enterprise plan, and **Code execution and file creation** must be turned on.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/smerchek/claude-epub-skill" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Productivity & tools</a>
