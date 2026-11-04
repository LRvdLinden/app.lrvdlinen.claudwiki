---
description: >-
  AWS development: CDK, serverless/event-driven architecture, cost optimisation and Bedrock AgentCore.
icon: aws
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

# AWS Skills

| | |
| --- | --- |
| **Maker** | zxkane (community) |
| **Works in** | Claude Code |
| **Cost** | Free (open source) |
| **Source** | [github.com/zxkane/aws-skills](https://github.com/zxkane/aws-skills) |

## What does it do?

Plugins for AWS with MCP integrations: CDK best practices, serverless and event-driven patterns, cost management, SST and deploying AI agents with Bedrock AgentCore. With the AWS Documentation MCP, Claude uses up-to-date AWS documentation.

## When do you use it?

* You build or manage infrastructure on AWS.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Analyse my AWS costs and give the three biggest savings.
```
{% endcode %}

**What you get:** A cost report with actions.

## Install

{% tabs %}
{% tab title="Claude Code" %}
```bash
/plugin marketplace add zxkane/aws-skills
/plugin install aws-common@aws-skills
/plugin install aws-iac@aws-skills
/plugin install aws-cost-ops@aws-skills
```

Other plugins: `serverless-eda`, `aws-agentic-ai`.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* The official marketplace also contains AWS plugins from Amazon itself, such as `aws-core` and `aws-serverless`. See the [catalogue](../../catalogus/README.md).
{% endhint %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/zxkane/aws-skills" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Data, cloud & payments</a>
