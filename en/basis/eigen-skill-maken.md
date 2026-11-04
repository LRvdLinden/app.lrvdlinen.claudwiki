---
description: >-
  From idea to working skill: write, test and share a SKILL.md.
icon: wand-magic-sparkles
cover: ../../.gitbook/assets/cover-en-bouwen.png
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
# Create your own skill

Do you notice you keep giving Claude the same explanation? Turn it into a skill.

{% stepper %}
{% step %}
### Let Claude do it for you
The easiest route: say *"Turn the way I do this into a skill"* at the end of a conversation that went well. With the [Skill Creator](../skills/bouwen/skill-creator.md) you get a complete folder right away.
{% endstep %}

{% step %}
### Or create the folder yourself

```bash
mkdir -p ~/.claude/skills/neighbourhood-newsletter
```
{% endstep %}

{% step %}
### Write the SKILL.md

{% code title="~/.claude/skills/neighbourhood-newsletter/SKILL.md" %}
```markdown
---
name: neighbourhood-newsletter
description: Writes the monthly newsletter of the neighbourhood council in the fixed structure. Use for every request for a newsletter, neighbourhood update or announcement to residents.
---

# Neighbourhood newsletter

## Structure
1. Opening: max. 3 sentences, personal.
2. Sections: News · Agenda · Call to action · Contact.

## Style
- Plain language, short sentences, address the reader as 'you'.
- No jargon where a simple word will do.

## Example
See `examples/october.md`.
```
{% endcode %}
{% endstep %}

{% step %}
### Test it
Start a new session and ask something that fits: *"Write the newsletter for December."* Doesn't Claude use your skill? Make the `description` more specific.
{% endstep %}

{% step %}
### Share it
* **Claude app:** zip the folder and upload it via **Settings → Capabilities → Skills**.
* **Team:** put it in `.claude/skills/` in your repo, or turn it into a plugin with your own marketplace.
* **Public:** put it on GitHub; others install it with `npx skills add your-name/your-repo`.
{% endstep %}
{% endstepper %}

## Rules for a good skill

| Do | Don't |
| --- | --- |
| A description with **what** and **when** | A vague description like 'helps with text' |
| Short, concrete steps | A 20-page novel in one file |
| Examples of a good result | Only rules without an example |
| Large reference material in separate files you mention in SKILL.md | Cramming everything into SKILL.md |
| `name` in lowercase with hyphens | Spaces or capitals in the name |
