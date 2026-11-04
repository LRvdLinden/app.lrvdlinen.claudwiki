---
description: >-
  Best practices for Terraform and OpenTofu: modules, testing, CI/CD and production-ready infrastructure.
icon: cloud
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

# Terraform Skill

| | |
| --- | --- |
| **Maker** | Anton Babenko (community) |
| **Works in** | Claude Code (+ other agents) |
| **Cost** | Free (open source) |
| **Source** | [github.com/antonbabenko/terraform-skill](https://github.com/antonbabenko/terraform-skill) |

## What does it do?

Made by a well-known Terraform expert. The skill helps Claude structure modules, test infrastructure code, set up CI/CD and write secure production code, for AWS, Azure and GCP.

## When do you use it?

* You manage infrastructure as code.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Set up a Terraform module for a static website on AWS, with tests.
```
{% endcode %}

**What you get:** A clean module with a test setup.

## Install

{% tabs %}
{% tab title="Claude Code" %}
First add the marketplace, then install the plugin. Type this in a Claude Code session:

```bash
/plugin marketplace add antonbabenko/agent-plugins
/plugin install terraform-skill@antonbabenko
```

Restart Claude Code if the skill doesn't appear right away. Check with `/plugin` that it is enabled.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/antonbabenko/terraform-skill" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Development & code</a>
