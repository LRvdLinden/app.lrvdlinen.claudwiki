---
description: >-
  Tientallen professionele security-skills van een bekend beveiligingsbedrijf: audits, Semgrep, fuzzing en supply chain.
icon: user-shield
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

# Trail of Bits Security

| | |
| --- | --- |
| **Maker** | Trail of Bits |
| **Werkt in** | Claude Code (+ Codex) |
| **Kosten** | Gratis (open source) |
| **Bron** | [github.com/trailofbits/skills](https://github.com/trailofbits/skills) |

## Wat doet het?

Trail of Bits is een gerenommeerd securitybedrijf. Hun marketplace bevat skills en plugins voor security-analyse: differentiële reviews, statische analyse, Semgrep-regels schrijven, supply-chain-risico's, onveilige standaardinstellingen, property-based testing, mutatietesten, varianten van kwetsbaarheden zoeken en meer.

## Wanneer gebruik je het?

* Je wilt je eigen code (bijvoorbeeld een app met gebruikersdata) laten doorlichten.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Controleer mijn dependencies op supply-chain-risico's.
```
{% endcode %}

**Wat je krijgt:** Een risico-overzicht per pakket.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
```bash
/plugin marketplace add trailofbits/skills
```

Kies daarna via `/plugin` welke plugins je wilt installeren.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Gebruik deze skills alleen op code en systemen waarvoor je toestemming hebt.
{% endhint %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/trailofbits/skills" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Security & wetenschap</a>
