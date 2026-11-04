---
description: >-
  Veelgestelde vragen over Claude-skills.
icon: circle-question
cover: ../.gitbook/assets/cover-bronnen.png
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
# Veelgestelde vragen

<details>
<summary>Kosten skills geld?</summary>

De skills zelf zijn bijna altijd gratis. In de Claude-app heb je wel een Pro-, Max-, Team- of Enterprise-abonnement nodig. Sommige skills gebruiken externe diensten (zoals Remotion voor grote bedrijven of gehoste geheugendiensten) die eigen voorwaarden hebben.
</details>

<details>
<summary>Werkt een skill uit Claude Code ook in de Claude-app?</summary>

Vaak wel: het is dezelfde standaard. Zip de skillmap en upload hem. Skills die afhangen van **hooks**, lokale programma's of de terminal werken alleen in Claude Code.
</details>

<details>
<summary>Hoeveel skills kan ik installeren?</summary>

Veel. Claude ziet eerst alleen de naam en beschrijving en laadt de rest pas als het nodig is. Te veel skills met overlappende beschrijvingen kunnen wel verwarring geven: ruim op wat je niet gebruikt.
</details>

<details>
<summary>Mijn skill wordt niet gebruikt. Wat nu?</summary>

1. Check of hij aanstaat (`/plugin` in Claude Code, Instellingen → Mogelijkheden in de app).
2. Herstart Claude Code.
3. Maak de `description` concreter: wat doet hij **en** wanneer moet hij gebruikt worden.
4. Roep hem expliciet aan met `/naam`.
</details>

<details>
<summary>Wat is het verschil tussen /plugin en npx skills?</summary>

`/plugin` is ingebouwd in Claude Code en installeert complete plugins (skills, commando's, hooks) met automatische updates. `npx skills` is een losse open-source CLI die alleen skills installeert, maar dan voor tientallen verschillende agents.
</details>

<details>
<summary>Kan ik skills delen met mijn team?</summary>

In Claude Code: zet ze in `.claude/skills/` in je repo of maak een eigen marketplace. In de Claude-app kunnen eigenaren van Team- en Enterprise-organisaties skills voor iedereen klaarzetten.
</details>
