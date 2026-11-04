---
description: >-
  Tekst-naar-spraak, spraak-naar-tekst, muziek, geluidseffecten, dubbing en voice agents.
icon: microphone-lines
cover: ../../.gitbook/assets/cover-media.png
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

# ElevenLabs

| | |
| --- | --- |
| **Maker** | ElevenLabs (officieel van de makers) |
| **Werkt in** | Claude Code (+ andere agents) |
| **Kosten** | Skills gratis; ElevenLabs-API volgens hun prijzen |
| **Bron** | [github.com/elevenlabs/skills](https://github.com/elevenlabs/skills) |

## Wat doet het?

Skills voor de ElevenLabs-API: tekst-naar-spraak, spraak-naar-tekst, muziek, geluidseffecten, dubbing, voice changer, stemisolatie, realtime en het bouwen van spraakagents.

## Wanneer gebruik je het?

* Je wilt een voice-over, podcastintro of spraakfunctie in je app.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Maak een Nederlandse voice-over van dit script met een rustige stem.
```
{% endcode %}

**Wat je krijgt:** Een audiobestand.

## Installeren

{% tabs %}
{% tab title="npx skills" %}
Met de open-source [skills-CLI](https://github.com/vercel-labs/skills) installeer je skills voor Claude Code én andere agents. Je hebt alleen Node.js nodig:

```bash
npx skills add elevenlabs/skills
```

Voeg `-g` toe om hem globaal (voor al je projecten) te installeren. Met `npx skills list` zie je wat er geïnstalleerd is.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Je hebt een ElevenLabs-API-sleutel nodig; de skill `setup-api-key` helpt je.
{% endhint %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/elevenlabs/skills" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Audio, beeld & visuals</a>
