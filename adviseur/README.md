---
description: >-
  Vertel wat je wilt doen en krijg direct de best passende skill, met installatiecommando.
icon: wand-magic-sparkles
cover: ../.gitbook/assets/cover-adviseur.png
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
# Skill-adviseur

Weet je niet welke skill je nodig hebt? Beschrijf in gewone taal wat je wilt doen, en de adviseur zoekt in **461 skills en plugins** de beste opties voor je, met uitleg en installatiecommando.

<a href="https://lrvdlinden.github.io/app.lrvdlinen.claudwiki/adviseur/" class="button primary" data-icon="magnifying-glass">Open de Skill-adviseur</a>

{% embed url="https://lrvdlinden.github.io/app.lrvdlinen.claudwiki/adviseur/" %}
Skill-adviseur: zoek de beste skill voor jouw taak
{% endembed %}

## Drie manieren om advies te krijgen

{% tabs %}
{% tab title="In je browser" %}
Open de [Skill-adviseur](https://lrvdlinden.github.io/app.lrvdlinen.claudwiki/adviseur/) en typ wat je wilt, bijvoorbeeld:

* *"Ik wil video's maken voor Instagram"*
* *"Mijn teksten klinken te veel als AI"*
* *"Ik bouw een iPhone-app in SwiftUI"*
* *"Ik wil facturen ordenen voor de belasting"*

Je krijgt direct de best passende skills, met waar ze werken en hoe je ze installeert.
{% endtab %}

{% tab title="Als skill in Claude" %}
Installeer de **skill-adviseur** zelf. Daarna vraag je in elk gesprek: *"Welke skill heb ik nodig om …?"* en Claude adviseert uit dezelfde catalogus.

**Claude-app:** download [skill-adviseur.zip](../.gitbook/assets/skill-adviseur.zip) en upload hem via **Instellingen → Mogelijkheden → Skills → Skill uploaden**.

**Claude Code:**

```bash
git clone https://github.com/LRvdLinden/app.lrvdlinen.claudwiki.git
cp -r app.lrvdlinen.claudwiki/skill-adviseur/skill-adviseur ~/.claude/skills/
```
{% endtab %}

{% tab title="Zoeken in de wiki" %}
Gebruik de zoekbalk bovenaan deze wiki (of druk op <kbd>Ctrl</kbd>/<kbd>⌘</kbd> + <kbd>K</kbd>). Staat GitBook AI aan, dan kun je daar ook gewoon een vraag stellen.
{% endtab %}
{% endtabs %}

{% hint style="info" %}
De adviseur kijkt naar alle skills in deze wiki plus alle 315 plugins uit de [officiële marketplace](../catalogus/README.md). Officiële skills krijgen bij gelijke score voorrang.
{% endhint %}
