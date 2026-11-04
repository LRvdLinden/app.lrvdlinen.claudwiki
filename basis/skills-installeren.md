---
description: >-
  Stap voor stap een skill installeren in de Claude-app, in Claude Code, via npx of handmatig.
icon: download
cover: ../.gitbook/assets/cover-basis.png
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
# Skills installeren

Er zijn vier manieren. Welke je kiest hangt af van waar je Claude gebruikt.

{% tabs %}
{% tab title="Claude-app" %}
**Ingebouwde skills aanzetten**

1. Ga naar **Instellingen → Mogelijkheden** (Settings → Capabilities).
2. Zet **Code-uitvoering en bestanden maken** aan.
3. Scroll naar **Skills** en zet de skills aan die je wilt.

**Een eigen of community-skill uploaden**

{% stepper %}
{% step %}
### Download de skill
Download de map met de `SKILL.md`, bijvoorbeeld via GitHub → **Code → Download ZIP**.
{% endstep %}
{% step %}
### Maak er een ZIP van
Zip **alleen de skillmap**. De mapnaam moet gelijk zijn aan de skillnaam.
{% endstep %}
{% step %}
### Upload
Ga naar **Instellingen → Mogelijkheden → Skills** en klik op **Skill uploaden**.
{% endstep %}
{% step %}
### Aanzetten
Zet de skill aan in de lijst. Klaar!
{% endstep %}
{% endstepper %}

{% hint style="info" %}
Bij Pro en Max zijn eigen skills privé. Bij Team en Enterprise kunnen eigenaren skills voor de hele organisatie klaarzetten.
{% endhint %}
{% endtab %}

{% tab title="Claude Code (plugins)" %}
De meeste skills worden verspreid als **plugin** via een **marketplace** (een GitHub-repo met een lijst plugins).

```bash
# 1. Marketplace toevoegen (eenmalig)
/plugin marketplace add anthropics/skills

# 2. Plugin installeren
/plugin install document-skills@anthropic-agent-skills

# Bekijken, aan/uit zetten en bijwerken
/plugin
```

De **officiële marketplace** van Anthropic (`claude-plugins-official`) is standaard al gekoppeld:

```bash
/plugin install superpowers@claude-plugins-official
```

Je kunt dezelfde commando's ook buiten een sessie in je terminal draaien, bijvoorbeeld `claude plugin install …`.
{% endtab %}

{% tab title="npx skills" %}
De open-source [skills-CLI](https://github.com/vercel-labs/skills) installeert skills voor Claude Code en tientallen andere agents. Vind skills op [skills.sh](https://skills.sh).

```bash
npx skills add remotion-dev/skills                 # alles uit een repo
npx skills add anthropics/skills --skill pdf       # één skill
npx skills add blader/humanizer -g                 # globaal, voor al je projecten
npx skills list                                    # wat heb ik?
npx skills check                                   # updates?
```
{% endtab %}

{% tab title="Handmatig" %}
Een skill is gewoon een map. Zet hem op de juiste plek:

| Plek | Map | Werkt in |
| --- | --- | --- |
| Persoonlijk | `~/.claude/skills/<naam>/SKILL.md` | Al je projecten op deze computer |
| Project | `.claude/skills/<naam>/SKILL.md` | Alleen dit project (commit hem voor je team) |

```bash
git clone https://github.com/blader/Claudeception.git ~/.claude/skills/claudeception
```

Herstart Claude Code daarna.
{% endtab %}
{% endtabs %}

## Werkt het?

* Typ in Claude Code `/` en kijk of de skill in de lijst staat.
* Of vraag gewoon: *"Welke skills heb je beschikbaar?"*

<a href="skills-gebruiken.md" class="button primary" data-icon="arrow-right">Volgende: skills gebruiken</a>
