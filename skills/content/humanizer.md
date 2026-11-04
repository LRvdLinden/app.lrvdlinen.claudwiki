---
description: >-
  Herschrijft AI-achtige tekst zodat hij klinkt alsof een mens hem schreef, zonder de inhoud te veranderen.
icon: user-pen
cover: ../../.gitbook/assets/cover-content.png
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

# Humanizer

{% hint style="danger" %}
**Gespot op social.** De meest virale skill van dit moment volgens Artificial Corner. Let op: er circuleren kopieën die er identiek uitzien, installeer alleen vanaf de officiële repo.
{% endhint %}

| | |
| --- | --- |
| **Maker** | blader (community) |
| **Werkt in** | Claude Code, Claude-app (+ Codex en meer) |
| **Kosten** | Gratis (open source) |
| **Bron** | [github.com/blader/humanizer](https://github.com/blader/humanizer) |

## Wat doet het?

Humanizer is gebaseerd op Wikipedia's lijst *Signs of AI writing*, de gids die Wikipedia-redacteuren gebruiken om AI-tekst te herkennen. De skill haalt typische AI-trucjes weg: 'niet X maar Y'-contrasten, pakkende one-liners aan het eind, gedwongen drietallen, overal gedachtestreepjes, opgeblazen claims, verkooptaal, typische AI-woorden en vetgedrukte labels. Je boodschap blijft gelijk, alleen de toon wordt menselijker.

## Wanneer gebruik je het?

* Je post op LinkedIn of Instagram en wilt niet dat het naar AI ruikt.
* Je wilt een concept van Claude laten 'ontdoen' van AI-tics.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
/humanizer Herschrijf deze LinkedIn-post zodat hij klinkt als mij.
```
{% endcode %}

**Wat je krijgt:** Dezelfde post, maar natuurlijker en zonder AI-patronen.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Voeg eerst de marketplace toe en installeer daarna de plugin. Typ dit in een Claude Code-sessie:

```bash
/plugin marketplace add blader/humanizer
/plugin install humanizer@humanizer
```

Herstart Claude Code als de skill niet meteen verschijnt. Controleer met `/plugin` of hij aanstaat.

De plugin luistert naar `/humanizer:humanizer` en vraagt Claude Code 2.1.142 of nieuwer.
{% endtab %}

{% tab title="npx skills" %}
Met de open-source [skills-CLI](https://github.com/vercel-labs/skills) installeer je skills voor Claude Code én andere agents. Je hebt alleen Node.js nodig:

```bash
npx skills add blader/humanizer --global --agent claude-code
```

Voeg `-g` toe om hem globaal (voor al je projecten) te installeren. Met `npx skills list` zie je wat er geïnstalleerd is.
{% endtab %}

{% tab title="Claude-app" %}
1. Download de repo als ZIP: [github.com/blader/humanizer](https://github.com/blader/humanizer) → **Code → Download ZIP**.
2. Pak uit en zoek de map `humanizer (de hoofdmap van de repo, met SKILL.md)` (daarin staat `SKILL.md`).
3. Maak van **alleen die map** een nieuwe ZIP. De mapnaam moet gelijk zijn aan de skillnaam.
4. Ga naar **Instellingen → Mogelijkheden → Skills** en klik op **Skill uploaden**.
5. Zet de skill aan.

Skills in de Claude-app vragen een Pro-, Max-, Team- of Enterprise-abonnement en **Code-uitvoering en bestanden maken** moet aanstaan.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Check altijd of je de echte repo hebt: github.com/blader/humanizer.
{% endhint %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/blader/humanizer" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Schrijven, content & marketing</a>
