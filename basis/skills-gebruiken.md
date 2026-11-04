---
description: >-
  Laat skills automatisch afgaan of roep ze zelf aan met een slash-commando.
icon: hand-pointer
cover: ../.gitbook/assets/cover-basis.png
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
# Skills gebruiken

## Automatisch

Meestal hoef je niets te doen. Vraag in gewone taal wat je wilt. Past je vraag bij de beschrijving van een skill, dan laadt Claude hem zelf.

```
Maak van deze notulen een Word-document met inhoudsopgave.
```

→ Claude gebruikt de [Word-skill](../skills/documenten/docx.md).

## Zelf aanroepen (Claude Code)

Typ `/` gevolgd door de naam van de skill, eventueel met extra tekst:

```
/grill-me Ik wil een app voor vrijwilligers bouwen
/humanizer:humanizer
```

Skills uit een plugin hebben een voorvoegsel: `/plugin-naam:skill-naam`.

## Een skill noemen

Werkt een skill niet vanzelf? Noem hem dan bij naam:

```
Gebruik de PDF-skill om de formuliervelden uit aanvraag.pdf te halen.
```

## Handige instellingen voor makers

| Instelling in SKILL.md | Wat het doet |
| --- | --- |
| `disable-model-invocation: true` | Alleen jij kunt hem starten, Claude niet uit zichzelf (handig voor bijv. deployen). |
| `user-invocable: false` | Alleen Claude gebruikt hem; hij staat niet in je `/`-menu. |
| `allowed-tools` | Tools die Claude zonder te vragen mag gebruiken tijdens die skill. |
| `arguments` | Benoemde argumenten, zoals `/migreer $component $van $naar`. |

{% hint style="success" %}
**Tip:** gaat een skill te vaak of te weinig af? Verbeter de beschrijving. De [Skill Creator](../skills/bouwen/skill-creator.md) kan dat voor je testen.
{% endhint %}
