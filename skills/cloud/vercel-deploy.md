---
description: >-
  Deployments beheren, buildstatus en logs bekijken en domeinen instellen op Vercel.
icon: rocket
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

# Vercel (deployen)

| | |
| --- | --- |
| **Maker** | Vercel · officiële Claude-marketplace |
| **Werkt in** | Claude Code |
| **Kosten** | Plugin gratis; je hebt een Vercel-account nodig |
| **Bron** | [github.com/vercel/vercel-plugin](https://github.com/vercel/vercel-plugin) |

## Wat doet het?

De Vercel-plugin laat Claude je frontend-infrastructuur besturen: deployments beheren, buildstatus en logs bekijken en domeinen configureren. Combineer met de [Vercel Agent Skills](../ontwikkeling/vercel-agent-skills.md) voor de best practices.

## Wanneer gebruik je het?

* Je host je website of app op Vercel.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Waarom faalde de laatste deployment? Laat de buildlog zien.
```
{% endcode %}

**Wat je krijgt:** De fout uit de log en een oplossing.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Deze plugin staat in de **officiële Anthropic-marketplace**, die standaard al gekoppeld is:

```bash
/plugin install vercel@claude-plugins-official
```

Of blader via `/plugin` → **Discover** en kies de plugin uit de lijst.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/vercel/vercel-plugin" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Data, cloud & betalen</a>
