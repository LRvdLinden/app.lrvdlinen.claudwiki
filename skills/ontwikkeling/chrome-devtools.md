---
description: >-
  Bedien en inspecteer een live Chrome-browser: performance-traces, netwerkverkeer en console-fouten.
icon: chrome
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

# Chrome DevTools

| | |
| --- | --- |
| **Maker** | Google · officiële Claude-marketplace |
| **Werkt in** | Claude Code |
| **Kosten** | Gratis |
| **Bron** | [github.com/ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) |

## Wat doet het?

Met Chrome DevTools MCP kijkt Claude mee in een echte Chrome-browser. Hij neemt performance-traces op, analyseert netwerkverzoeken, leest console-meldingen met leesbare stacktraces en automatiseert acties met Puppeteer.

## Wanneer gebruik je het?

* Je website is traag en je wilt weten waarom.
* Je zoekt een fout die alleen in de browser optreedt.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Neem een performance-trace op van mijn homepage en vertel wat hem traag maakt.
```
{% endcode %}

**Wat je krijgt:** De grootste vertragers met concrete oplossingen.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Deze plugin staat in de **officiële Anthropic-marketplace**, die standaard al gekoppeld is:

```bash
/plugin install chrome-devtools-mcp@claude-plugins-official
```

Of blader via `/plugin` → **Discover** en kies de plugin uit de lijst.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/ChromeDevTools/chrome-devtools-mcp" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Ontwikkelen & code</a>
