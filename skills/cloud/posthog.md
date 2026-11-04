---
description: >-
  Analytics, feature flags, experimenten en error tracking van PostHog vanuit Claude.
icon: chart-simple
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

# PostHog

| | |
| --- | --- |
| **Maker** | PostHog · officiële Claude-marketplace |
| **Werkt in** | Claude Code |
| **Kosten** | Plugin gratis; je hebt een PostHog-account nodig |
| **Bron** | [posthog.com/docs/model-context-protocol](https://posthog.com/docs/model-context-protocol) |

## Wat doet het?

Met de PostHog-plugin bekijkt Claude je productanalytics, beheert feature flags en experimenten, volgt fouten en haalt inzichten op, zonder dat je het dashboard hoeft te openen.

## Wanneer gebruik je het?

* Je meet het gebruik van je app met PostHog.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Hoeveel gebruikers hebben de nieuwe onboarding afgerond deze week?
```
{% endcode %}

**Wat je krijgt:** Het aantal plus de trend.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Deze plugin staat in de **officiële Anthropic-marketplace**, die standaard al gekoppeld is:

```bash
/plugin install posthog@claude-plugins-official
```

Of blader via `/plugin` → **Discover** en kies de plugin uit de lijst.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://posthog.com/docs/model-context-protocol" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Data, cloud & betalen</a>
