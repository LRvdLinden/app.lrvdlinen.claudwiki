---
description: >-
  Geeft Claude een uitgesproken ontwerpsmaak, zodat interfaces niet als standaardsjabloon ogen.
icon: wand-magic-sparkles
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

# Frontend Design

| | |
| --- | --- |
| **Maker** | Anthropic (officieel) |
| **Werkt in** | Claude-app, Claude Code, API |
| **Kosten** | Gratis (Apache 2.0) |
| **Bron** | [github.com/anthropics/skills/tree/main/skills/frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) |

## Wat doet het?

Frontend Design leert Claude om bij elke interface eerst een **duidelijke esthetische richting** te kiezen: typografie, kleur, compositie en details. Het doel is dat een website of app er doordacht uitziet in plaats van 'zoals elke AI-site'. Het is ook als plugin beschikbaar in de officiële Claude Code-marketplace.

## Wanneer gebruik je het?

* Je laat Claude een website, landingspagina of app-scherm bouwen.
* Je wilt een bestaand ontwerp een eigen gezicht geven.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Bouw een landingspagina voor mijn weer-app. Kies een gedurfde, eigen stijl, geen standaard paarse gradient.
```
{% endcode %}

**Wat je krijgt:** Een pagina met een herkenbare, bewuste stijl.

## Installeren

{% tabs %}
{% tab title="Claude-app" %}
Deze skill is **al ingebouwd** voor betaalde abonnementen.

1. Open **Instellingen → Mogelijkheden** (Settings → Capabilities).
2. Zet **Code-uitvoering en bestanden maken** aan.
3. Scroll naar **Skills** en zet de skill aan.

Daarna vraag je gewoon in gewone taal wat je wilt; Claude laadt de skill zelf.
{% endtab %}

{% tab title="Claude Code" %}
Deze plugin staat in de **officiële Anthropic-marketplace**, die standaard al gekoppeld is:

```bash
/plugin install frontend-design@claude-plugins-official
```

Of blader via `/plugin` → **Discover** en kies de plugin uit de lijst.
{% endtab %}

{% tab title="npx skills" %}
Met de open-source [skills-CLI](https://github.com/vercel-labs/skills) installeer je skills voor Claude Code én andere agents. Je hebt alleen Node.js nodig:

```bash
npx skills add anthropics/skills --skill frontend-design
```

Voeg `-g` toe om hem globaal (voor al je projecten) te installeren. Met `npx skills list` zie je wat er geïnstalleerd is.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Geef een paar woorden sfeer mee ('Scandinavisch rustig', 'retro-krant', 'luxe nacht') voor nog betere resultaten.
{% endhint %}


<a href="https://github.com/anthropics/skills/tree/main/skills/frontend-design" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Design & frontend</a>
