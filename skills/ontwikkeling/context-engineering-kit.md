---
description: >-
  Geavanceerde technieken: DDD, kaizen, subagent-driven development, critique en prompt engineering.
icon: sliders
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

# Context Engineering Kit

| | |
| --- | --- |
| **Maker** | NeoLab (community) |
| **Werkt in** | Claude Code (+ OpenCode, Cursor en meer) |
| **Kosten** | Gratis (open source) |
| **Bron** | [github.com/NeoLabHQ/context-engineering-kit](https://github.com/NeoLabHQ/context-engineering-kit) |

## Wat doet het?

Een grote set plugins met technieken voor betere AI-ontwikkeling: software-architectuur en DDD, kaizen (continu verbeteren), subagent-driven development, reflectie en kritiek, prompt engineering, documentatie en eigen commando's, hooks en skills maken.

## Wanneer gebruik je het?

* Je wilt het maximale uit Claude Code halen bij grote projecten.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
/critique
```
{% endcode %}

**Wat je krijgt:** Een kritische beoordeling van het laatste werk door meerdere 'juryleden'.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
```bash
/plugin marketplace add NeoLabHQ/context-engineering-kit
/plugin install ddd@NeoLabHQ/context-engineering-kit
```

Andere plugins: `customaize-agent`, `docs`, `fpf`, `kaizen`, `sadd` en meer.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Documentatie: [neolab.gitbook.io/cek](https://neolab.gitbook.io/cek/).
{% endhint %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/NeoLabHQ/context-engineering-kit" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Ontwikkelen & code</a>
