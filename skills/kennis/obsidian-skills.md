---
description: >-
  Officiële skills van de Obsidian-maker: notities, Bases, JSON Canvas en de Obsidian CLI.
icon: note-sticky
cover: ../../.gitbook/assets/cover-kennis.png
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

# Obsidian Skills

| | |
| --- | --- |
| **Maker** | Steph Ango / kepano (maker van Obsidian) |
| **Werkt in** | Claude Code (+ Codex, OpenCode) |
| **Kosten** | Gratis |
| **Bron** | [github.com/kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) |

## Wat doet het?

Skills om met je Obsidian-vault te werken: **obsidian-markdown** (de Obsidian-variant van Markdown), **obsidian-bases**, **json-canvas**, **obsidian-cli** (notities lezen, maken en doorzoeken via de CLI) en **defuddle** (webpagina's schoon binnenhalen).

## Wanneer gebruik je het?

* Je gebruikt Obsidian als tweede brein.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Maak van de notulen van vandaag een notitie in mijn vault met links naar de betrokken projecten.
```
{% endcode %}

**Wat je krijgt:** Een nette Obsidian-notitie met [[links]].

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Voeg eerst de marketplace toe en installeer daarna de plugin. Typ dit in een Claude Code-sessie:

```bash
/plugin marketplace add kepano/obsidian-skills
/plugin install obsidian@obsidian-skills
```

Herstart Claude Code als de skill niet meteen verschijnt. Controleer met `/plugin` of hij aanstaat.
{% endtab %}

{% tab title="npx skills" %}
Met de open-source [skills-CLI](https://github.com/vercel-labs/skills) installeer je skills voor Claude Code én andere agents. Je hebt alleen Node.js nodig:

```bash
npx skills add https://github.com/kepano/obsidian-skills
```

Voeg `-g` toe om hem globaal (voor al je projecten) te installeren. Met `npx skills list` zie je wat er geïnstalleerd is.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Wil je diagrammen in Obsidian? Kijk naar [Axton's Obsidian Visual Skills](https://github.com/axtonliu/axton-obsidian-visual-skills) voor Excalidraw, Mermaid en Canvas.
{% endhint %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/kepano/obsidian-skills" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Kennis & geheugen</a>
