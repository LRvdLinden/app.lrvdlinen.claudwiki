---
description: >-
  Een bibliotheek met 170+ wetenschappelijke skills: biologie, chemie, geneeskunde, natuurkunde en data-analyse.
icon: flask
cover: ../../.gitbook/assets/cover-security.png
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

# Scientific Skills

| | |
| --- | --- |
| **Maker** | K-Dense (community) |
| **Werkt in** | Claude Code (+ Cursor, Codex en meer) |
| **Kosten** | Gratis (open source) |
| **Bron** | [github.com/K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) |

## Wat doet het?

Een collectie van ruim 170 skills voor onderzoek: biologie, chemie, geneeskunde, natuurkunde, techniek, aardwetenschappen, data-analyse en wetenschappelijke communicatie. Volgt de open Agent Skills-standaard.

## Wanneer gebruik je het?

* Je doet (hobby)onderzoek of data-analyse met wetenschappelijke bronnen.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Analyseer deze meetdata en maak een publicatieklare grafiek met uitleg.
```
{% endcode %}

**Wat je krijgt:** Analyse en grafiek volgens wetenschappelijke conventies.

## Installeren

{% tabs %}
{% tab title="npx skills" %}
Met de open-source [skills-CLI](https://github.com/vercel-labs/skills) installeer je skills voor Claude Code én andere agents. Je hebt alleen Node.js nodig:

```bash
npx skills add K-Dense-AI/scientific-agent-skills
```

Voeg `-g` toe om hem globaal (voor al je projecten) te installeren. Met `npx skills list` zie je wat er geïnstalleerd is.
{% endtab %}

{% tab title="Handmatig" %}
Kopieer de skillmap naar je persoonlijke skills-map (voor alle projecten) of naar `.claude/skills/` in één project:

```bash
git clone https://github.com/K-Dense-AI/scientific-agent-skills.git ~/.agents/skills/scientific-agent-skills
```
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/K-Dense-AI/scientific-agent-skills" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Security & wetenschap</a>
