---
description: >-
  Interactieve datavisualisaties met D3.js: grafieken, netwerken en kaarten.
icon: chart-area
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

# D3.js Visualisatie

| | |
| --- | --- |
| **Maker** | Chris von Csefalvay (community) |
| **Werkt in** | Claude Code, Claude-app |
| **Kosten** | Gratis |
| **Bron** | [github.com/chrisvoncsefalvay/claude-d3js-skill](https://github.com/chrisvoncsefalvay/claude-d3js-skill) |

## Wat doet het?

Leert Claude om met D3.js aangepaste grafieken, netwerkdiagrammen en geografische visualisaties te maken, met volledige controle over overgangen en interactie.

## Wanneer gebruik je het?

* Standaardgrafieken zijn niet genoeg en je wilt iets op maat.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Maak een interactieve kaart van Nederland met het aantal meldingen per gemeente.
```
{% endcode %}

**Wat je krijgt:** Een D3-kaart met tooltips.

## Installeren

{% tabs %}
{% tab title="Claude-app" %}
1. Download de repo als ZIP: [github.com/chrisvoncsefalvay/claude-d3js-skill](https://github.com/chrisvoncsefalvay/claude-d3js-skill) → **Code → Download ZIP**.
2. Pak uit en zoek de map `(de hoofdmap, hernoem naar d3-viz)` (daarin staat `SKILL.md`).
3. Maak van **alleen die map** een nieuwe ZIP. De mapnaam moet gelijk zijn aan de skillnaam.
4. Ga naar **Instellingen → Mogelijkheden → Skills** en klik op **Skill uploaden**.
5. Zet de skill aan.

Skills in de Claude-app vragen een Pro-, Max-, Team- of Enterprise-abonnement en **Code-uitvoering en bestanden maken** moet aanstaan.
{% endtab %}

{% tab title="Handmatig" %}
Kopieer de skillmap naar je persoonlijke skills-map (voor alle projecten) of naar `.claude/skills/` in één project:

```bash
git clone https://github.com/chrisvoncsefalvay/claude-d3js-skill.git ~/.claude/skills/d3-viz
```
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/chrisvoncsefalvay/claude-d3js-skill" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Audio, beeld & visuals</a>
