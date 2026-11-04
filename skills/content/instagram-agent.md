---
description: >-
  Dertien skills die een Instagram-account runnen: Reels met scoorbare hooks, captions, carrousels, stories en DM's.
icon: camera-retro
cover: ../../.gitbook/assets/cover-content.png
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

# Instagram Agent

{% hint style="danger" %}
**Gespot op social.** Veel gedeeld door Instagram-creators; diverse blogs schrijven er complete installatiegidsen over.
{% endhint %}

| | |
| --- | --- |
| **Maker** | Jake Schincariol (community) |
| **Werkt in** | Claude Code, Claude-app |
| **Kosten** | Gratis (MIT), geen API-sleutel nodig |
| **Bron** | [github.com/Jakeschincariol/instagram-agent-skill](https://github.com/Jakeschincariol/instagram-agent-skill) |

## Wat doet het?

Een pakket van dertien skills (`ig-reel`, `ig-caption`, `ig-carousel`, `ig-story`, `ig-viral`, `ig-plan`, `ig-audit`, `ig-profile`, `ig-dm`, `ig-reply`, `ig-comment`, `ig-repurpose` en `ig-human`). Ze schrijven Reels op basis van 26 hook-formules en geven de hook een score, onderzoeken wat viraal gaat, linten je captions en halen AI-taal weg. Je hoeft niets te koppelen.

## Wanneer gebruik je het?

* Je wilt consequent posten voor je app of organisatie.
* Je wilt betere hooks en captions.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Schrijf een Reel-script van 30 seconden over 'Waarom je buren je beste beveiliging zijn' met een scorende hook.
```
{% endcode %}

**Wat je krijgt:** Een script met hook-score en caption.

{% code title="Voorbeeld 2: wat je typt" overflow="wrap" %}
```
Audit mijn Instagram-profiel en geef 5 verbeterpunten.
```
{% endcode %}

**Wat je krijgt:** Een profielaudit.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Voeg eerst de marketplace toe en installeer daarna de plugin. Typ dit in een Claude Code-sessie:

```bash
/plugin marketplace add Jakeschincariol/instagram-agent-skill
/plugin install instagram-agent
```

Herstart Claude Code als de skill niet meteen verschijnt. Controleer met `/plugin` of hij aanstaat.
{% endtab %}

{% tab title="Handmatig" %}
Kopieer de skillmap naar je persoonlijke skills-map (voor alle projecten) of naar `.claude/skills/` in één project:

```bash
git clone https://github.com/Jakeschincariol/instagram-agent-skill.git
cp -r instagram-agent-skill/skills/ig-* ~/.claude/skills/
```
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/Jakeschincariol/instagram-agent-skill" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Schrijven, content & marketing</a>
