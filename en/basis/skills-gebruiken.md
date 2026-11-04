---
description: >-
  Let skills trigger automatically or call them yourself with a slash command.
icon: hand-pointer
cover: ../../.gitbook/assets/cover-en-basis.png
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
# Use skills

## Automatically

Usually you don't have to do anything. Ask for what you want in plain language. If your question matches a skill's description, Claude loads it itself.

```
Turn these meeting minutes into a Word document with a table of contents.
```

→ Claude uses the [Word skill](../skills/documenten/docx.md).

## Call it yourself (Claude Code)

Type `/` followed by the skill's name, optionally with extra text:

```
/grill-me I want to build an app for volunteers
/humanizer:humanizer
```

Skills from a plugin have a prefix: `/plugin-name:skill-name`.

## Mention a skill

Doesn't a skill trigger by itself? Then mention it by name:

```
Use the PDF skill to extract the form fields from application.pdf.
```

## Handy settings for skill authors

| Setting in SKILL.md | What it does |
| --- | --- |
| `disable-model-invocation: true` | Only you can start it, not Claude on its own (handy for e.g. deploying). |
| `user-invocable: false` | Only Claude uses it; it's not in your `/` menu. |
| `allowed-tools` | Tools Claude may use without asking during that skill. |
| `arguments` | Named arguments, like `/migrate $component $from $to`. |

{% hint style="success" %}
**Tip:** does a skill trigger too often or too rarely? Improve the description. The [Skill Creator](../skills/bouwen/skill-creator.md) can test that for you.
{% endhint %}
