---
description: >-
  Skills are folders with instructions, scripts and files that Claude loads when they're needed.
icon: lightbulb
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
# What are skills?

A **skill** is a folder with instructions (and sometimes scripts and example files) that teaches Claude how to do a particular task well and consistently. Think of a work instruction you give a new colleague: *this is how we make a newsletter*, *this is our house style*, *this is how you test this app*.

The clever part: Claude only loads a skill **when it needs it**. Of every skill, Claude first sees only the name and a short description. Only when your question matches does it read the full instructions. That's why you can install dozens of skills without Claude getting slower or more confused.

## What does a skill look like?

```
my-skill/
├── SKILL.md          ← required: description + instructions
├── examples/         ← optional: example files
└── scripts/          ← optional: scripts Claude may run
```

{% code title="SKILL.md" %}
```markdown
---
name: neighbourhood-newsletter
description: Writes the monthly newsletter of the neighbourhood council in our fixed structure. Use for every request for a newsletter, neighbourhood update or announcement to residents.
---

# Neighbourhood newsletter

1. Start with a short personal opening (max. 3 sentences).
2. Then the fixed sections: News, Agenda, Call to action, Contact.
3. Write in plain language and address the reader as 'you'.
```
{% endcode %}

The **description** is the most important part: Claude uses it to decide whether the skill fits your question.

## Skills vs. the rest

| What | What is it? | Example |
| --- | --- | --- |
| **Skill** | A folder with instructions that Claude loads when relevant. | 'This is how we make an invoice.' |
| **Plugin** | A package that bundles skills, slash commands, agents, hooks and connections. | Superpowers, Anthropic's role plugins. |
| **MCP / connector** | A connection to an external service, so Claude can do things there. | Google Calendar, Notion, GitHub. |
| **Project** | A workspace in the Claude app with its own documents and instructions. | 'Council 2027' with all minutes. |
| **CLAUDE.md** | An instruction file for one code project in Claude Code. | 'Always use Swift 6 and test with XCTest.' |

{% hint style="info" %}
**One standard for everything.** Skills follow the open [Agent Skills standard](https://agentskills.io). A skill you write once works in the Claude app, in Claude Code and via the API, and often in other AI agents such as Codex and Cursor too.
{% endhint %}

## Where do skills work?

* **Claude app** (web, desktop, mobile): on Pro, Max, Team and Enterprise, with *Code execution and file creation* turned on.
* **Claude Code**: in your personal folder `~/.claude/skills/`, in a project in `.claude/skills/`, or via plugins.
* **Claude API**: ready-made and custom skills via the [Skills API](https://docs.claude.com/en/api/skills-guide).

<a href="skills-installeren.md" class="button primary" data-icon="arrow-right">Next: install skills</a>
