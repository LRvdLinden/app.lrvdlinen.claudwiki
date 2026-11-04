---
description: >-
  Van idee tot werkende skill: SKILL.md schrijven, testen en delen.
icon: wand-magic-sparkles
cover: ../.gitbook/assets/cover-bouwen.png
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
# Je eigen skill maken

Merk je dat je Claude steeds dezelfde uitleg geeft? Maak er een skill van.

{% stepper %}
{% step %}
### Laat Claude het voor je doen
De makkelijkste route: zeg *"Maak een skill van hoe ik dit doe"* aan het eind van een gesprek waarin het goed ging. Met de [Skill Creator](../skills/bouwen/skill-creator.md) krijg je meteen een complete map.
{% endstep %}

{% step %}
### Of maak de map zelf

```bash
mkdir -p ~/.claude/skills/nieuwsbrief-wijkraad
```
{% endstep %}

{% step %}
### Schrijf de SKILL.md

{% code title="~/.claude/skills/nieuwsbrief-wijkraad/SKILL.md" %}
```markdown
---
name: nieuwsbrief-wijkraad
description: Schrijft de maandelijkse nieuwsbrief van de wijkraad in de vaste opbouw. Gebruik bij elke vraag om een nieuwsbrief, buurtupdate of mededeling aan bewoners.
---

# Nieuwsbrief wijkraad

## Opbouw
1. Opening: max. 3 zinnen, persoonlijk.
2. Rubrieken: Nieuws · Agenda · Oproep · Contact.

## Stijl
- B1-niveau, korte zinnen, 'je' in plaats van 'u'.
- Geen Engelse woorden als er een Nederlands woord is.

## Voorbeeld
Zie `voorbeelden/oktober.md`.
```
{% endcode %}
{% endstep %}

{% step %}
### Test hem
Start een nieuwe sessie en vraag iets dat erbij hoort: *"Schrijf de nieuwsbrief voor december."* Gebruikt Claude je skill niet? Maak de `description` specifieker.
{% endstep %}

{% step %}
### Deel hem
* **Claude-app:** zip de map en upload via **Instellingen → Mogelijkheden → Skills**.
* **Team:** zet hem in `.claude/skills/` in je repo, of maak er een plugin met een eigen marketplace van.
* **Openbaar:** zet hem op GitHub; anderen installeren met `npx skills add jouw-naam/jouw-repo`.
{% endstep %}
{% endstepper %}

## Regels voor een goede skill

| Doe | Niet doen |
| --- | --- |
| Beschrijving met **wat** én **wanneer** | Vage beschrijving als 'helpt met tekst' |
| Korte, concrete stappen | Een roman van 20 pagina's in één bestand |
| Voorbeelden van goed resultaat | Alleen regels zonder voorbeeld |
| Grote naslag in losse bestanden die je in SKILL.md noemt | Alles in SKILL.md proppen |
| `name` in kleine letters met streepjes | Spaties of hoofdletters in de naam |
