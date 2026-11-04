---
description: >-
  Het web doorzoeken en lezen voor je agent: zoeken, pagina's scrapen, leads, SEO-audits en diepgaand onderzoek.
icon: spider
cover: ../../.gitbook/assets/cover-cloud.png
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

# Firecrawl

| | |
| --- | --- |
| **Maker** | Firecrawl (officieel van de makers) |
| **Werkt in** | Claude Code (API-sleutel nodig) |
| **Kosten** | Plugin gratis; Firecrawl-diensten volgens hun prijzen |
| **Bron** | [github.com/firecrawl/firecrawl-claude-plugin](https://github.com/firecrawl/firecrawl-claude-plugin) |

## Wat doet het?

Koppelt Claude aan de zoek- en scrapetools van Firecrawl, met skills voor diepgaand onderzoek, documentatie lezen, leads vinden en verrijken, vacatures, merkidentiteit en SEO-audits.

## Wanneer gebruik je het?

* Je wilt grondig webonderzoek met nette, schone pagina-inhoud.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Doe diepgaand onderzoek naar buurtpreventie-apps in Nederland en vat het samen.
```
{% endcode %}

**Wat je krijgt:** Een rapport met bronnen.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Voeg eerst de marketplace toe en installeer daarna de plugin. Typ dit in een Claude Code-sessie:

```bash
/plugin marketplace add firecrawl/firecrawl-claude-plugin
/plugin install firecrawl@firecrawl
```

Herstart Claude Code als de skill niet meteen verschijnt. Controleer met `/plugin` of hij aanstaat.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/firecrawl/firecrawl-claude-plugin" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Data, cloud & betalen</a>
