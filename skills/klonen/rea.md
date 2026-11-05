---
description: >-
  Zie je een functie in een app die je mooi vindt? REA zoekt uit hoe hij werkt, tot op binair niveau, zodat je hem kunt nabouwen.
icon: microchip
cover: ../../.gitbook/assets/cover-klonen.png
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

# REA – Reverse Engineer Anything

{% hint style="danger" %}
**Gespot op social.** Viraal gegaan via o.a. 'I Tried 23 Viral Claude Skills' (Artificial Corner).
{% endhint %}

| | |
| --- | --- |
| **Maker** | morluto (community) |
| **Werkt in** | Claude Code (+ Codex, Cursor, Gemini CLI en meer) |
| **Kosten** | Gratis (open source) |
| **Bron** | [github.com/morluto/rea](https://github.com/morluto/rea) |

## Wat doet het?

REA (Reverse Engineer Anything) is de 'clone-skill' voor apps. Hij analyseert native apps, Electron/JavaScript-apps, verpakte programma's, firmware en webapps, legt uit hoe een functie werkt, vergelijkt versies, decompileert code en begeleidt een reconstructie. Voor native analyse kan hij Hopper, Ghidra of IDA gebruiken. Daarnaast kan REA van een live webapp een testomgeving (AgentEnv) bouwen.

## Wanneer gebruik je het?

* Je ziet een functie in een app en wilt een eenvoudigere versie in je eigen app bouwen.
* Je wilt begrijpen wat een programma op je computer precies doet.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Hoe werkt de zoekbalk in deze desktop-app? Bouw een eenvoudige versie voor mijn app.
```
{% endcode %}

**Wat je krijgt:** Een uitleg van de werking plus een eigen, vereenvoudigde implementatie.

## Installeren

{% tabs %}
{% tab title="Installer" %}
```bash
npx rea-agents setup
```

De setup registreert REA bij je agent (Claude Code, Codex, Cursor en meer) en installeert de bijbehorende werkinstructies. Installeer alleen via de officiële bronnen: de repo, [rea.tools](https://rea.tools/) of het npm-pakket `rea-agents`.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Gebruik REA alleen op software waarvoor je dat mag; sommige licenties verbieden reverse engineering.
* Gebruik dit alleen voor je eigen sites en apps, of met toestemming. Logo's, merkuitingen en teksten blijven van de eigenaar, en nabouwen om je als een ander voor te doen (phishing) is verboden. Check ook de gebruiksvoorwaarden van de site.
{% endhint %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/morluto/rea" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Sites & apps klonen</a>
