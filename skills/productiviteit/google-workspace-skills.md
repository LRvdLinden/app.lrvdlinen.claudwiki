---
description: >-
  25 skills voor Gmail, Agenda, Docs, Sheets, Slides, Drive, plus Postgres, Telegram, WhatsApp en meer.
icon: google
cover: ../../.gitbook/assets/cover-productiviteit.png
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

# Google Workspace & AI Skills

| | |
| --- | --- |
| **Maker** | sanjay3290 (community) |
| **Werkt in** | Claude Code (+ Gemini CLI en andere agents) |
| **Kosten** | Gratis (open source) |
| **Bron** | [github.com/sanjay3290/ai-skills](https://github.com/sanjay3290/ai-skills) |

## Wat doet het?

Een collectie draagbare skills: Gmail, Google Agenda, Chat, Docs, Sheets, Slides en Drive, maar ook Deep Research via Gemini, Imagen voor afbeeldingen, NotebookLM, Jules, Outline, Atlassian, Azure DevOps, Postgres/MySQL/MSSQL (alleen-lezen) en Telegram en WhatsApp.

## Wanneer gebruik je het?

* Je wilt Claude Code laten werken met je Google-account of databases.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Zoek in mijn Gmail de laatste mails van de gemeente en zet de afspraken in mijn agenda.
```
{% endcode %}

**Wat je krijgt:** Agenda-items op basis van je mail.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Voeg eerst de marketplace toe en installeer daarna de plugin. Typ dit in een Claude Code-sessie:

```bash
/plugin marketplace add sanjay3290/ai-skills
/plugin install ai-skills@ai-skills
```

Herstart Claude Code als de skill niet meteen verschijnt. Controleer met `/plugin` of hij aanstaat.

Alle 25 skills komen in één plugin. Bijwerken: `/plugin marketplace update ai-skills`.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* In de Claude-app kun je Google ook koppelen via Connectors, zonder skill.
{% endhint %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/sanjay3290/ai-skills" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Productiviteit & tools</a>
