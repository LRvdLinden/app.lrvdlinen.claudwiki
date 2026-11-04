---
description: >-
  Laat Claude Code direct met NotebookLM praten voor antwoorden die alleen op jouw documenten zijn gebaseerd.
icon: book-open-reader
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

# NotebookLM Skill

| | |
| --- | --- |
| **Maker** | PleasePrompto (community) |
| **Werkt in** | Alleen Claude Code (lokaal), niet de web-app |
| **Kosten** | Gratis |
| **Bron** | [github.com/PleasePrompto/notebooklm-skill](https://github.com/PleasePrompto/notebooklm-skill) |

## Wat doet het?

Claude stelt vragen aan je NotebookLM-notebooks en krijgt antwoorden die uitsluitend gebaseerd zijn op de bronnen die jij daar hebt geüpload. Handig als je betrouwbare antwoorden wilt zonder verzinsels.

## Wanneer gebruik je het?

* Je hebt al je beleidsstukken of handleidingen in NotebookLM staan.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Vraag mijn notebook 'Wijkbeleid' wat er staat over groenonderhoud.
```
{% endcode %}

**Wat je krijgt:** Een antwoord met bronverwijzingen uit je notebook.

## Installeren

{% tabs %}
{% tab title="Handmatig" %}
Kopieer de skillmap naar je persoonlijke skills-map (voor alle projecten) of naar `.claude/skills/` in één project:

```bash
mkdir -p ~/.claude/skills && cd ~/.claude/skills
git clone https://github.com/PleasePrompto/notebooklm-skill notebooklm
```
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Er is ook een MCP-versie van dezelfde maker.
{% endhint %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/PleasePrompto/notebooklm-skill" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Productiviteit & tools</a>
