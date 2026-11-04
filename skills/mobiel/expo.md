---
description: >-
  Officiële Expo-skills: React Native-apps bouwen, Expo Router, EAS Build/Update en publiceren in de stores.
icon: react
cover: ../../.gitbook/assets/cover-mobiel.png
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

# Expo Skills

| | |
| --- | --- |
| **Maker** | Expo (officieel van de makers) |
| **Werkt in** | Claude Code (+ Codex, Cursor en meer) |
| **Kosten** | Gratis |
| **Bron** | [github.com/expo/skills](https://github.com/expo/skills) |

## Wat doet het?

Ruim twintig skills van Expo zelf: projectstructuur, Expo Router, native UI en animaties, data ophalen, modules maken, upgraden, web-naar-native, App Clips en de EAS-diensten (builds, updates, hosting, workflows en publicatie in de App Store en Play Store).

## Wanneer gebruik je het?

* Je bouwt een cross-platform app met React Native en Expo.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Upgrade dit Expo-project naar de nieuwste SDK.
```
{% endcode %}

**Wat je krijgt:** Een begeleide upgrade met de juiste stappen.

{% code title="Voorbeeld 2: wat je typt" overflow="wrap" %}
```
Zet EAS Update op zodat ik fixes zonder nieuwe build kan uitrollen.
```
{% endcode %}

**Wat je krijgt:** Configuratie en uitleg.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Deze plugin staat in de **officiële Anthropic-marketplace**, die standaard al gekoppeld is:

```bash
/plugin install expo@claude-plugins-official
```

Of blader via `/plugin` → **Discover** en kies de plugin uit de lijst.
{% endtab %}

{% tab title="npx skills" %}
Met de open-source [skills-CLI](https://github.com/vercel-labs/skills) installeer je skills voor Claude Code én andere agents. Je hebt alleen Node.js nodig:

```bash
npx skills@latest add expo/skills --skill '*'
```

Voeg `-g` toe om hem globaal (voor al je projecten) te installeren. Met `npx skills list` zie je wat er geïnstalleerd is.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/expo/skills" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Apps & mobiel</a>
