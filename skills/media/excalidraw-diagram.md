---
description: >-
  Maakt mooie Excalidraw-diagrammen uit gewone taal: diagrammen die iets uitleggen, niet alleen boxen en pijlen.
icon: pen-to-square
cover: ../../.gitbook/assets/cover-media.png
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

# Excalidraw Diagram

| | |
| --- | --- |
| **Maker** | Cole Medin (community) |
| **Werkt in** | Claude Code (+ OpenCode) |
| **Kosten** | Gratis |
| **Bron** | [github.com/coleam00/excalidraw-diagram-skill](https://github.com/coleam00/excalidraw-diagram-skill) |

## Wat doet het?

De vormen in het diagram volgen het idee dat ze uitleggen: waaiers voor één-op-veel, tijdlijnen voor volgordes, samenkomende lijnen voor bundeling. Zo krijg je geen saaie kaartjesraster maar een diagram dat iets vertelt.

## Wanneer gebruik je het?

* Je wilt een architectuur, proces of idee visueel uitleggen.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Teken hoe een melding van de meldkamer via de server naar de app gaat.
```
{% endcode %}

**Wat je krijgt:** Een .excalidraw-bestand.

## Installeren

{% tabs %}
{% tab title="Handmatig" %}
Kopieer de skillmap naar je persoonlijke skills-map (voor alle projecten) of naar `.claude/skills/` in één project:

```bash
git clone https://github.com/coleam00/excalidraw-diagram-skill.git
cp -r excalidraw-diagram-skill .claude/skills/excalidraw-diagram   # of ~/.claude/skills/ voor al je projecten
```
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/coleam00/excalidraw-diagram-skill" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Audio, beeld & visuals</a>
