---
description: >-
  Maakt een cv op maat van een vacature, zodat je relevante ervaring bovenaan staat.
icon: id-card
cover: ../../.gitbook/assets/cover-productiviteit.png
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

# Tailored Resume Generator

| | |
| --- | --- |
| **Maker** | ComposioHQ (community) |
| **Werkt in** | Claude Code, Claude-app |
| **Kosten** | Gratis |
| **Bron** | [github.com/ComposioHQ/awesome-claude-skills/tree/master/tailored-resume-generator](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/tailored-resume-generator) |

## Wat doet het?

Analyseert een vacaturetekst en herschrijft je cv zodat de ervaring, vaardigheden en resultaten die voor deze baan tellen het meest opvallen.

## Wanneer gebruik je het?

* Je solliciteert en wilt per vacature een gericht cv.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Hier is mijn cv en de vacature. Maak een cv op maat.
```
{% endcode %}

**Wat je krijgt:** Een aangepast cv met de juiste accenten.

## Installeren

{% tabs %}
{% tab title="Claude-app" %}
1. Download de repo als ZIP: [github.com/ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) → **Code → Download ZIP**.
2. Pak uit en zoek de map `tailored-resume-generator` (daarin staat `SKILL.md`).
3. Maak van **alleen die map** een nieuwe ZIP. De mapnaam moet gelijk zijn aan de skillnaam.
4. Ga naar **Instellingen → Mogelijkheden → Skills** en klik op **Skill uploaden**.
5. Zet de skill aan.

Skills in de Claude-app vragen een Pro-, Max-, Team- of Enterprise-abonnement en **Code-uitvoering en bestanden maken** moet aanstaan.
{% endtab %}

{% tab title="Handmatig" %}
Kopieer de skillmap naar je persoonlijke skills-map (voor alle projecten) of naar `.claude/skills/` in één project:

```bash
git clone https://github.com/ComposioHQ/awesome-claude-skills.git
cp -r awesome-claude-skills/tailored-resume-generator ~/.claude/skills/
```
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Laat het daarna als Word-bestand maken met de [Word-skill](../documenten/docx.md).
{% endhint %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/ComposioHQ/awesome-claude-skills/tree/master/tailored-resume-generator" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Productiviteit & tools</a>
