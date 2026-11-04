---
description: >-
  Official skills for Terraform (style guide, tests, stacks, modules) and Packer images.
icon: cubes-stacked
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

# HashiCorp Terraform & Packer

| | |
| --- | --- |
| **Maker** | HashiCorp (official, by the makers) |
| **Works in** | Claude Code (+ other agents) |
| **Cost** | Free |
| **Source** | [github.com/hashicorp/agent-skills](https://github.com/hashicorp/agent-skills) |

## What does it do?

The makers of Terraform provide skills for the Terraform style guide, testing, stacks, policies, importing existing resources, refactoring modules and even building your own providers. For Packer there are skills to build AWS, Azure and Windows images.

## When do you use it?

* You manage infrastructure with Terraform or build machine images with Packer.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Import these existing S3 buckets into Terraform.
```
{% endcode %}

**What you get:** Import blocks and the matching configuration.

## Install

{% tabs %}
{% tab title="Claude Code" %}
```bash
claude plugin marketplace add hashicorp/agent-skills
claude plugin install terraform@hashicorp
claude plugin install packer@hashicorp
```
{% endtab %}

{% tab title="npx skills" %}
With the open-source [skills CLI](https://github.com/vercel-labs/skills) you install skills for Claude Code and other agents. All you need is Node.js:

```bash
npx skills add hashicorp/agent-skills
```

Add `-g` to install it globally (for all your projects). `npx skills list` shows what is installed.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* See also the community variant [Terraform Skill](../ontwikkeling/terraform-skill.md).
{% endhint %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/hashicorp/agent-skills" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Data, cloud & payments</a>
