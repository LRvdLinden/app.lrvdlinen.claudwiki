---
description: >-
  Leert Claude video's en animaties maken in code (React), lokaal en onbeperkt.
icon: clapperboard
cover: ../../.gitbook/assets/cover-creatief.png
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

# Remotion

{% hint style="danger" %}
**Gespot op social.** Tip van Bart Boonstra: *'Remotion is de skill die Claude leert om animaties te maken in code. Alle animaties in mijn video's zijn hiermee gebouwd.'*
{% endhint %}

| | |
| --- | --- |
| **Maker** | Remotion (officieel van de makers) |
| **Werkt in** | Claude Code (+ Codex, Cursor en meer) |
| **Kosten** | Skills gratis; Remotion zelf heeft een eigen licentie |
| **Bron** | [github.com/remotion-dev/skills](https://github.com/remotion-dev/skills) |

## Wat doet het?

Remotion is een framework om video's te maken met React-code. De officiële Remotion-skills leren Claude de best practices: een project opzetten, animaties en overgangen, ondertitels, kaarten, multimedia, interactiviteit en renderen naar MP4. Je beschrijft wat je wilt zien, Claude schrijft de code en je rendert de video lokaal op je eigen computer.

## Wanneer gebruik je het?

* Je maakt content voor social media en wilt animaties of infographics.
* Je wilt video's met ondertitels of data-visualisaties genereren.
* Je wilt een vaste video-template die je steeds hergebruikt.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Maak een Remotion-video van 15 seconden, verticaal 1080x1920, waarin de vijf belangrijkste features van mijn app één voor één binnenvliegen.
```
{% endcode %}

**Wat je krijgt:** Een Remotion-project dat je rendert tot een MP4.

{% code title="Voorbeeld 2: wat je typt" overflow="wrap" %}
```
Voeg geanimeerde ondertitels toe aan deze video.
```
{% endcode %}

**Wat je krijgt:** Een video met ondertitels in je eigen stijl.

## Installeren

{% tabs %}
{% tab title="npx skills" %}
Met de open-source [skills-CLI](https://github.com/vercel-labs/skills) installeer je skills voor Claude Code én andere agents. Je hebt alleen Node.js nodig:

```bash
npx skills add remotion-dev/skills
```

Voeg `-g` toe om hem globaal (voor al je projecten) te installeren. Met `npx skills list` zie je wat er geïnstalleerd is.
{% endtab %}

{% tab title="Voorwaarden" %}
Je hebt Node.js nodig en een Remotion-project (`npx create-video@latest`). Check de [Remotion-licentie](https://www.remotion.dev/license): voor bedrijven boven een bepaalde omvang is een betaalde licentie nodig.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Begin met de skill `remotion-best-practices`; die verwijst Claude naar de juiste deelskill.
{% endhint %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/remotion-dev/skills" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Creatief & video</a>
