---
description: >-
  Anthropic's own Claude Code plugins: code review, feature-dev, commits, PR review, security and hooks.
icon: puzzle-piece
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

# Official dev plugins

| | |
| --- | --- |
| **Maker** | Anthropic (official) |
| **Works in** | Claude Code |
| **Cost** | Free |
| **Source** | [github.com/anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |

## What does it do?

The official marketplace contains plugins that Anthropic maintains itself. A selection:

| Plugin | What it does |
| --- | --- |
| `code-review` | Automated PR review with several specialised agents and a confidence score |
| `feature-dev` | Complete feature workflow: explore the codebase, design the architecture, quality check |
| `commit-commands` | Quick commands to commit, push and create PRs |
| `pr-review-toolkit` | Review agents for comments, tests, error handling, types and simplification |
| `security-guidance` | Warns about insecure code (injection, XSS, SSRF, hardcoded secrets and more) |
| `hookify` | Easily create hooks to prevent unwanted behaviour |
| `claude-md-management` | Keeps your CLAUDE.md files up to date and in good shape |
| `claude-code-setup` | Analyses your codebase and suggests fitting hooks, skills and MCP servers |
| `code-simplifier` | Makes code clearer without changing behaviour |
| `playground` | Creates interactive HTML playgrounds with live preview |
| `ralph-loop` | Lets Claude keep working in a loop until a task is really done |

There are also language plugins (LSP) for Swift, TypeScript, Python, Kotlin and Rust, among others.

## When do you use it?

* You work with Claude Code on a real codebase.
* You want to standardise reviews and commits.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
/code-review
```
{% endcode %}

**What you get:** A review of your current PR with findings and scores.

{% code title="Example 2: what you type" overflow="wrap" %}
```
/feature-dev Add dark mode to the settings
```
{% endcode %}

**What you get:** A guided workflow from exploring to shipping.

## Install

{% tabs %}
{% tab title="Claude Code" %}
This plugin is in the **official Anthropic marketplace**, which is connected by default:

```bash
/plugin install code-review@claude-plugins-official
```

Or browse via `/plugin` → **Discover** and pick the plugin from the list.

Replace `code-review` with the plugin you want, for example `feature-dev`, `swift-lsp` or `security-guidance`.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* The `swift-lsp` plugin is also handy if you build iOS apps.
{% endhint %}

<a href="https://github.com/anthropics/claude-plugins-official" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Development & code</a>
