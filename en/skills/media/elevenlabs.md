---
description: >-
  Text-to-speech, speech-to-text, music, sound effects, dubbing and voice agents.
icon: microphone-lines
cover: ../../../.gitbook/assets/cover-en-media.png
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

# ElevenLabs

| | |
| --- | --- |
| **Maker** | ElevenLabs (official, by the makers) |
| **Works in** | Claude Code (+ other agents) |
| **Cost** | Skills free; ElevenLabs API at their prices |
| **Source** | [github.com/elevenlabs/skills](https://github.com/elevenlabs/skills) |

## What does it do?

Skills for the ElevenLabs API: text-to-speech, speech-to-text, music, sound effects, dubbing, voice changer, voice isolation, realtime and building voice agents.

## When do you use it?

* You want a voice-over, podcast intro or speech feature in your app.

## Examples

{% code title="Example 1: what you type" overflow="wrap" %}
```
Make a Dutch voice-over of this script with a calm voice.
```
{% endcode %}

**What you get:** An audio file.

## Install

{% tabs %}
{% tab title="npx skills" %}
With the open-source [skills CLI](https://github.com/vercel-labs/skills) you install skills for Claude Code and other agents. All you need is Node.js:

```bash
npx skills add elevenlabs/skills
```

Add `-g` to install it globally (for all your projects). `npx skills list` shows what is installed.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* You need an ElevenLabs API key; the `setup-api-key` skill helps you.
{% endhint %}

{% hint style="warning" %}
Community skills are not reviewed by Anthropic. Read the `SKILL.md` before you install. See [Install safely](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/elevenlabs/skills" class="button primary" data-icon="github">View on GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Back to Audio, images & visuals</a>
