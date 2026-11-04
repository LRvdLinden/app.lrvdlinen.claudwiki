---
description: >-
  Analyseert een afbeelding, website of Figma-bestand en maakt er een gestructureerde design.md van.
icon: eye-dropper
cover: ../../.gitbook/assets/cover-design.png
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

# AnyDesign

| | |
| --- | --- |
| **Maker** | uxKero (community) |
| **Werkt in** | Claude Code, Claude-app |
| **Kosten** | Gratis |
| **Bron** | [github.com/uxKero/anydesign](https://github.com/uxKero/anydesign) |

## Wat doet het?

Zet afbeeldingen, websites en Figma-bestanden om in een leesbare designspecificatie: designsysteem, componentenoverzicht en instructies om het na te bouwen. Losse elementen (een navbar, een 3D-illustratie) kun je kopiëren als 'rebuild-prompt'.

## Wanneer gebruik je het?

* Je wilt de stijl van een eigen ontwerp vastleggen om consequent verder te bouwen.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Maak een design.md van deze screenshot van mijn app.
```
{% endcode %}

**Wat je krijgt:** Kleuren, typografie, spacing en componenten op een rij.

## Installeren

{% tabs %}
{% tab title="Handmatig" %}
Kopieer de skillmap naar je persoonlijke skills-map (voor alle projecten) of naar `.claude/skills/` in één project:

```bash
git clone https://github.com/uxKero/anydesign.git
cp -r anydesign ~/.claude/skills/
```
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Gebruik dit voor je eigen ontwerpen of met toestemming; kopieer niet zomaar andermans design.
{% endhint %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/uxKero/anydesign" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Design & frontend</a>
