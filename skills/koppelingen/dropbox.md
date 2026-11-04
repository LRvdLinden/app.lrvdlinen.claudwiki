---
description: >-
  Zoek en orden je Dropbox-bestanden, sla resultaten op en maak deellinks.
icon: dropbox
cover: ../../.gitbook/assets/cover-koppelingen.png
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

# Dropbox

| | |
| --- | --- |
| **Maker** | Dropbox · officiële Claude-marketplace |
| **Werkt in** | Claude Code |
| **Kosten** | Plugin gratis; je hebt een account bij Dropbox nodig |
| **Bron** | [www.dropbox.com](https://www.dropbox.com) |

## Wat doet het?

De Dropbox-plugin koppelt je Dropbox aan Claude: bestanden zoeken en ordenen, wat Claude maakt direct opslaan en deellinks aanmaken. Je bestaande Dropbox-rechten blijven gelden.

## Wanneer gebruik je het?

* Je bewaart je bestanden in Dropbox.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Sla deze presentatie op in Dropbox/Wijkraad en geef me een deellink.
```
{% endcode %}

**Wat je krijgt:** Het bestand in Dropbox plus een link.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Deze plugin staat in de **officiële Anthropic-marketplace**, die standaard al gekoppeld is:

```bash
/plugin install dropbox@claude-plugins-official
```

Of blader via `/plugin` → **Discover** en kies de plugin uit de lijst.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://www.dropbox.com" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Apps koppelen</a>
