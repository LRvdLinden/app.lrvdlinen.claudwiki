---
description: >-
  Ruimt mappen slim op: duplicaten vinden, betere structuur voorstellen en opruimen automatiseren.
icon: folder-tree
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

# File Organizer

| | |
| --- | --- |
| **Maker** | ComposioHQ (community) |
| **Werkt in** | Claude Code, Claude-app |
| **Kosten** | Gratis |
| **Bron** | [github.com/ComposioHQ/awesome-claude-skills/tree/master/file-organizer](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/file-organizer) |

## Wat doet het?

Claude bekijkt je mappen, begrijpt wat erin staat, vindt dubbele bestanden, stelt een logischere mappenstructuur voor en voert het opruimen voor je uit.

## Wanneer gebruik je het?

* Je Downloads- of documentenmap is een chaos.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Ruim mijn map Downloads op: groepeer per soort en zoek duplicaten.
```
{% endcode %}

**Wat je krijgt:** Een voorstel, en na akkoord een opgeruimde map.

## Installeren

{% tabs %}
{% tab title="Handmatig" %}
Kopieer de skillmap naar je persoonlijke skills-map (voor alle projecten) of naar `.claude/skills/` in één project:

```bash
git clone https://github.com/ComposioHQ/awesome-claude-skills.git
cp -r awesome-claude-skills/file-organizer ~/.claude/skills/
```
{% endtab %}

{% tab title="Claude-app" %}
1. Download de repo als ZIP: [github.com/ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) → **Code → Download ZIP**.
2. Pak uit en zoek de map `file-organizer` (daarin staat `SKILL.md`).
3. Maak van **alleen die map** een nieuwe ZIP. De mapnaam moet gelijk zijn aan de skillnaam.
4. Ga naar **Instellingen → Mogelijkheden → Skills** en klik op **Skill uploaden**.
5. Zet de skill aan.

Skills in de Claude-app vragen een Pro-, Max-, Team- of Enterprise-abonnement en **Code-uitvoering en bestanden maken** moet aanstaan.
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Laat Claude eerst een voorstel doen voordat hij iets verplaatst.
{% endhint %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/ComposioHQ/awesome-claude-skills/tree/master/file-organizer" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Productiviteit & tools</a>
