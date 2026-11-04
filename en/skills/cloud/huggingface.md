---
description: >-
  AI/ML tasks: datasets, training and evaluating models, Spaces, Gradio and the Hugging Face Hub.
icon: face-smile
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

# Hugging Face

| | |
| --- | --- |
| **Maker** | Hugging Face (official, by the makers) |
| **Works in** | Claude Code (+ other agents) |
| **Cost** | Free |
| **Source** | [github.com/huggingface/skills](https://github.com/huggingface/skills) |

## What does it do?

Skills for machine learning on the Hugging Face Hub: the `hf` CLI, datasets, Spaces and Gradio, training models (TRL, LoRA, vision, sentence-transformers), evaluations, publishing papers and running models locally.

## When do you use it?

* You want to fine-tune your own model or build a demo Space.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Create a Gradio Space that summarises Dutch text.
```
{% endcode %}

**What you get:** A working Space repo.

## Install

{% tabs %}
{% tab title="Claude Code" %}
First add the marketplace, then install the plugin. Type this in a Claude Code session:

```bash
/plugin marketplace add huggingface/skills
/plugin install hf-cli@huggingface/skills
```

Restart Claude Code if the skill doesn't appear right away. Check with `/plugin` that it is enabled.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/huggingface/skills" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Data, cloud & payments</a>
