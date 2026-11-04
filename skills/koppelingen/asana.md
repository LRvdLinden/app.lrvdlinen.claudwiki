---
description: >-
  Taken maken en beheren, projecten doorzoeken en voortgang volgen in Asana.
icon: check-double
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

# Asana

| | |
| --- | --- |
| **Maker** | Asana · officiële Claude-marketplace |
| **Werkt in** | Claude Code |
| **Kosten** | Plugin gratis; je hebt een account bij Asana nodig |
| **Bron** | [github.com/anthropics/claude-plugins-public/tree/main/external_plugins/asana](https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/asana) |

## Wat doet het?

De Asana-plugin koppelt Claude aan Asana: taken maken en toewijzen, projecten doorzoeken en voortgang bijhouden. Eenmalig stel je een Asana-app in met het commando `/asana-setup`.

## Wanneer gebruik je het?

* Je plant projecten in Asana.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Maak voor elke actie uit deze notulen een taak in Asana met een deadline.
```
{% endcode %}

**Wat je krijgt:** Asana-taken met eigenaren en deadlines.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Deze plugin staat in de **officiële Anthropic-marketplace**, die standaard al gekoppeld is:

```bash
/plugin install asana@claude-plugins-official
```

Of blader via `/plugin` → **Discover** en kies de plugin uit de lijst.

Daarna eenmalig: `/asana-setup`.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/asana" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Apps koppelen</a>
