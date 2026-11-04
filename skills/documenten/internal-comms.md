---
description: >-
  Schrijft interne communicatie in vaste formats: statusupdates, nieuwsbrieven, FAQ's en incidentrapporten.
icon: bullhorn
cover: ../../.gitbook/assets/cover-documenten.png
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

# Internal Comms

| | |
| --- | --- |
| **Maker** | Anthropic (officieel) |
| **Werkt in** | Claude-app, Claude Code, API |
| **Kosten** | Gratis (Apache 2.0) |
| **Bron** | [github.com/anthropics/skills/tree/main/skills/internal-comms](https://github.com/anthropics/skills/tree/main/skills/internal-comms) |

## Wat doet het?

Deze skill bevat voorbeeldformats voor allerlei interne communicatie: statusrapporten, updates voor het management, nieuwsbrieven, FAQ's, incidentrapporten en projectupdates. Het idee: je past de formats aan naar hoe jouw organisatie het graag ziet, zodat elk stuk consistent is.

## Wanneer gebruik je het?

* Je schrijft regelmatig updates of nieuwsbrieven.
* Je wilt dat incidentrapporten altijd dezelfde opbouw hebben.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Schrijf een incidentrapport over de storing van gisteravond: oorzaak, impact, oplossing en vervolgacties.
```
{% endcode %}

**Wat je krijgt:** Een rapport in een vaste, zakelijke structuur.

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
Voeg eerst de marketplace toe en installeer daarna de plugin. Typ dit in een Claude Code-sessie:

```bash
/plugin marketplace add anthropics/skills
/plugin install example-skills@anthropic-agent-skills
```

Herstart Claude Code als de skill niet meteen verschijnt. Controleer met `/plugin` of hij aanstaat.

Dit installeert het hele pakket **example-skills** (o.a. deze skill).
{% endtab %}

{% tab title="npx skills" %}
Met de open-source [skills-CLI](https://github.com/vercel-labs/skills) installeer je skills voor Claude Code én andere agents. Je hebt alleen Node.js nodig:

```bash
npx skills add anthropics/skills --skill internal-comms
```

Voeg `-g` toe om hem globaal (voor al je projecten) te installeren. Met `npx skills list` zie je wat er geïnstalleerd is.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Maak een eigen kopie en vervang de voorbeeldformats door die van jouw organisatie.
{% endhint %}


<a href="https://github.com/anthropics/skills/tree/main/skills/internal-comms" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Documenten & kantoor</a>
