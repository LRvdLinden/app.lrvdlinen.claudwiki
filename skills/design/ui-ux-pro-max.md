---
description: >-
  Een doorzoekbare designbibliotheek met tientallen stijlen, 192 kleurpaletten, 74 fontcombinaties en 119 UX-richtlijnen.
icon: layer-group
cover: ../../.gitbook/assets/cover-design.png
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

# UI UX Pro Max

{% hint style="danger" %}
**Gespot op social.** Tip van Bart Boonstra: *'UI UX Pro Max maakt elke layout 1000x professioneler. Letterlijk.'*
{% endhint %}

| | |
| --- | --- |
| **Maker** | nextlevelbuilder (community) |
| **Werkt in** | Claude Code (+ Cursor, Copilot, Codex en meer) |
| **Kosten** | Gratis (open source) |
| **Bron** | [github.com/nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) |

## Wat doet het?

UI UX Pro Max is een van de populairste community-skills. Hij geeft Claude een lokale, doorzoekbare database met UI-stijlen (glassmorphism, bento grid, brutalism, dark mode…), kleurpaletten per type product, lettertypecombinaties met Google Fonts, UX-richtlijnen en anti-patronen, iconen, animatie-presets en grafiektypen. Claude zoekt bij jouw vraag de best passende stijl, kleuren en typografie op en past ze consequent toe. Het pakket bevat ook extra skills voor banners, huisstijl, designsystemen en slides.

## Wanneer gebruik je het?

* Je bouwt een website, dashboard of app en wilt dat het er direct professioneel uitziet.
* Je wilt een designsysteem (kleuren, fonts, spacing) laten voorstellen.
* Je wilt een bestaand scherm laten reviewen op UX en toegankelijkheid.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Maak een dashboard voor een alarmeringsapp. Zoek een passende stijl en een passend kleurpalet.
```
{% endcode %}

**Wat je krijgt:** Een dashboard met een onderbouwde stijl, palet en fontkeuze.

{% code title="Voorbeeld 2: wat je typt" overflow="wrap" %}
```
Review dit instellingenscherm op UX-fouten en toegankelijkheid.
```
{% endcode %}

**Wat je krijgt:** Een lijst met concrete verbeterpunten.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Voeg eerst de marketplace toe en installeer daarna de plugin. Typ dit in een Claude Code-sessie:

```bash
/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill
/plugin install ui-ux-pro-max@ui-ux-pro-max-skill
```

Herstart Claude Code als de skill niet meteen verschijnt. Controleer met `/plugin` of hij aanstaat.
{% endtab %}

{% tab title="CLI (aanbevolen)" %}
De makers raden hun eigen installer aan:

```bash
npm install -g ui-ux-pro-max-cli
cd /pad/naar/je/project
uipro init --ai claude            # alleen dit project
uipro init --ai claude --global   # voor al je projecten (~/.claude/skills/)
```

Gebruik `ui-ux-pro-max-cli`; het oudere pakket `uipro-cli` is verouderd.
{% endtab %}

{% tab title="Claude-app" %}
1. Download de repo als ZIP: [github.com/nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) → **Code → Download ZIP**.
2. Pak uit en zoek de map `.claude/skills/ui-ux-pro-max` (daarin staat `SKILL.md`).
3. Maak van **alleen die map** een nieuwe ZIP. De mapnaam moet gelijk zijn aan de skillnaam.
4. Ga naar **Instellingen → Mogelijkheden → Skills** en klik op **Skill uploaden**.
5. Zet de skill aan.

Skills in de Claude-app vragen een Pro-, Max-, Team- of Enterprise-abonnement en **Code-uitvoering en bestanden maken** moet aanstaan.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Combineer met [Frontend Design](frontend-design.md) of [Impeccable](impeccable.md) voor nog meer controle.
{% endhint %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/nextlevelbuilder/ui-ux-pro-max-skill" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Design & frontend</a>
