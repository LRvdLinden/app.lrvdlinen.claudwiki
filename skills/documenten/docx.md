---
description: >-
  Maakt, leest en bewerkt Word-documenten met opmaak, inhoudsopgave en wijzigingen bijhouden.
icon: file-word
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

# Word (docx)

| | |
| --- | --- |
| **Maker** | Anthropic (officieel) |
| **Werkt in** | Claude-app, Claude Code, API |
| **Kosten** | Gratis bij betaald abonnement (source-available) |
| **Bron** | [github.com/anthropics/skills/tree/main/skills/docx](https://github.com/anthropics/skills/tree/main/skills/docx) |

## Wat doet het?

De Word-skill is de motor achter de Word-bestanden die Claude voor je maakt. Hij weet hoe een `.docx` van binnen werkt: koppen, stijlen, tabellen, kop- en voetteksten, paginanummers, inhoudsopgaven, afbeeldingen en zelfs **wijzigingen bijhouden** (track changes) en opmerkingen. Ook kan hij bestaande Word-bestanden lezen en aanpassen, of een sjabloon (`.dotx`) als basis gebruiken.

## Wanneer gebruik je het?

* Je hebt echt een `.docx` nodig, bijvoorbeeld voor een gemeente, school of klant.
* Je wilt een bestaand Word-bestand laten nakijken met zichtbare wijzigingen.
* Je wilt een briefsjabloon met huisstijl vullen.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Maak van deze notulen een net Word-document met inhoudsopgave, paginanummers en het logo van de wijkraad in de koptekst.
```
{% endcode %}

**Wat je krijgt:** Een opgemaakt `.docx`-bestand om te downloaden.

{% code title="Voorbeeld 2: wat je typt" overflow="wrap" %}
```
Lees contract.docx en stel verbeteringen voor als bijgehouden wijzigingen.
```
{% endcode %}

**Wat je krijgt:** Het originele document met track changes die je in Word kunt accepteren of weigeren.

## Installeren

{% tabs %}
{% tab title="Claude-app" %}
Deze skill is **al ingebouwd** voor betaalde abonnementen.

1. Open **Instellingen → Mogelijkheden** (Settings → Capabilities).
2. Zet **Code-uitvoering en bestanden maken** aan.
3. Scroll naar **Skills** en zet de skill aan.

Daarna vraag je gewoon in gewone taal wat je wilt; Claude laadt de skill zelf.

In de Claude-app gebruikt Claude deze skill ook al automatisch zodra je om een bestand van dit type vraagt.
{% endtab %}

{% tab title="Claude Code" %}
Voeg eerst de marketplace toe en installeer daarna de plugin. Typ dit in een Claude Code-sessie:

```bash
/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropic-agent-skills
```

Herstart Claude Code als de skill niet meteen verschijnt. Controleer met `/plugin` of hij aanstaat.

Dit installeert **document-skills**: Word, PDF, PowerPoint en Excel in één keer.
{% endtab %}

{% tab title="npx skills" %}
Met de open-source [skills-CLI](https://github.com/vercel-labs/skills) installeer je skills voor Claude Code én andere agents. Je hebt alleen Node.js nodig:

```bash
npx skills add anthropics/skills --skill docx
```

Voeg `-g` toe om hem globaal (voor al je projecten) te installeren. Met `npx skills list` zie je wat er geïnstalleerd is.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Zeg expliciet 'als Word-bestand' als je een .docx wilt; anders kiest Claude soms een ander formaat.
* Upload je eigen sjabloon (.dotx) om je huisstijl te laten gebruiken.
{% endhint %}


<a href="https://github.com/anthropics/skills/tree/main/skills/docx" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Documenten & kantoor</a>
