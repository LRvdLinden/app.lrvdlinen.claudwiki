---
description: >-
  Een complete 'agent harness': agents, skills, commando's, hooks en regels in één groot pakket.
icon: layer-group
cover: ../../.gitbook/assets/cover-ontwikkeling.png
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

# Everything Claude Code (ECC)

| | |
| --- | --- |
| **Maker** | affaan-m (community) |
| **Werkt in** | Claude Code (+ andere agents) |
| **Kosten** | Gratis (open source) |
| **Bron** | [github.com/affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) |

## Wat doet het?

ECC is een uitgebreid systeem van agents, skills, commando's en hooks voor Claude Code, bedoeld als compleet 'besturingssysteem' voor je agent. Groot en uitgebreid: vooral interessant voor ervaren gebruikers.

## Wanneer gebruik je het?

* Je wilt een kant-en-klare, uitgebreide Claude Code-setup.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
(na installatie) /plan Voeg betalingen toe
```
{% endcode %}

**Wat je krijgt:** Een begeleide planning- en bouwflow.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Voeg eerst de marketplace toe en installeer daarna de plugin. Typ dit in een Claude Code-sessie:

```bash
/plugin marketplace add https://github.com/affaan-m/ECC
/plugin install ecc@ecc
```

Herstart Claude Code als de skill niet meteen verschijnt. Controleer met `/plugin` of hij aanstaat.

Kopieer de hooks niet ook nog naar `settings.json`: de plugin laadt ze al.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Kies óf de plugin óf handmatige installatie, niet allebei.
{% endhint %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/affaan-m/everything-claude-code" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Ontwikkelen & code</a>
