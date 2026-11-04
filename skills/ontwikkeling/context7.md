---
description: >-
  Haalt actuele, versie-specifieke documentatie en codevoorbeelden op, zodat Claude geen verouderde API's gebruikt.
icon: book-open
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

# Context7

| | |
| --- | --- |
| **Maker** | Upstash · officiële Claude-marketplace |
| **Werkt in** | Claude Code |
| **Kosten** | Gratis |
| **Bron** | [github.com/anthropics/claude-plugins-public/tree/main/external_plugins/context7](https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/context7) |

## Wat doet het?

Context7 (van Upstash) koppelt Claude aan een gehoste documentatiedienst. Claude haalt de documentatie en codevoorbeelden op van precies de versie van een bibliotheek die jij gebruikt. Er is geen lokale Node.js nodig.

## Wanneer gebruik je het?

* Claude gebruikt functies die in jouw versie niet (meer) bestaan.
* Je werkt met een snel veranderend framework.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Gebruik context7 en bouw dit met de nieuwste versie van Next.js.
```
{% endcode %}

**Wat je krijgt:** Code volgens de actuele documentatie.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Deze plugin staat in de **officiële Anthropic-marketplace**, die standaard al gekoppeld is:

```bash
/plugin install context7@claude-plugins-official
```

Of blader via `/plugin` → **Discover** en kies de plugin uit de lijst.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/context7" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Ontwikkelen & code</a>
