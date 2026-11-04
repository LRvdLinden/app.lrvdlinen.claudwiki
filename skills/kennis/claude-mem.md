---
description: >-
  Geeft Claude Code een blijvend geheugen: wat in eerdere sessies gebeurde, komt automatisch terug.
icon: memory
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

# Claude-Mem

| | |
| --- | --- |
| **Maker** | thedotmack (community) |
| **Werkt in** | Claude Code (+ andere agents) |
| **Kosten** | Gratis open source; de gehoste geheugendienst heeft 30 dagen gratis proef, daarna je eigen abonnement of API-sleutel |
| **Bron** | [github.com/thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) |

## Wat doet het?

Claude-Mem is een 'persistent memory compression system'. Via hooks legt het vast wat er in je sessies gebeurt, comprimeert het en voegt relevante herinneringen toe aan nieuwe sessies. Er is een lokale webviewer om je geheugen te doorzoeken. Na installatie vraagt het om in te loggen via een e-mail-link.

## Wanneer gebruik je het?

* Je werkt lang aan hetzelfde project en wilt niet steeds opnieuw context geven.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
(gewoon verder werken)
```
{% endcode %}

**Wat je krijgt:** Claude weet in een nieuwe sessie nog welke beslissingen en bugfixes eerder zijn gedaan.

## Installeren

{% tabs %}
{% tab title="Installer (aanbevolen)" %}
```bash
npx claude-mem install
```

De installer zet alles klaar en vraagt je daarna in te loggen via een e-maillink (geen creditcard). Daarna kies je je geheugen-provider: de claude-mem observer (30 dagen gratis proef), een eigen OpenRouter- of Gemini-sleutel, of je Anthropic-abonnement.
{% endtab %}

{% tab title="Claude Code" %}
Voeg eerst de marketplace toe en installeer daarna de plugin. Typ dit in een Claude Code-sessie:

```bash
/plugin marketplace add thedotmack/claude-mem
/plugin install claude-mem
```

Herstart Claude Code als de skill niet meteen verschijnt. Controleer met `/plugin` of hij aanstaat.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Lees de privacy-informatie in de repo: standaard wordt de gehoste opslag gebruikt.
{% endhint %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/thedotmack/claude-mem" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Kennis & geheugen</a>
