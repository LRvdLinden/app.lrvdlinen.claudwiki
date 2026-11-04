---
description: >-
  Zet markdown, onderzoek of chatsamenvattingen om naar een net e-book (EPUB3).
icon: book
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

# Markdown to EPUB

| | |
| --- | --- |
| **Maker** | smerchek (community) |
| **Werkt in** | Claude Code, Claude-app |
| **Kosten** | Gratis |
| **Bron** | [github.com/smerchek/claude-epub-skill](https://github.com/smerchek/claude-epub-skill) |

## Wat doet het?

Maakt van markdown-documenten professionele EPUB3-e-books die werken op Apple Books, Kobo, e-readers en meer. Perfect om onderzoek of lange artikelen offline te lezen.

## Wanneer gebruik je het?

* Je wilt een lang document of deze wiki als e-book lezen.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Maak van deze 5 artikelen één e-book met inhoudsopgave.
```
{% endcode %}

**Wat je krijgt:** Een .epub-bestand.

## Installeren

{% tabs %}
{% tab title="Claude-app" %}
1. Download de repo als ZIP: [github.com/smerchek/claude-epub-skill](https://github.com/smerchek/claude-epub-skill) → **Code → Download ZIP**.
2. Pak uit en zoek de map `markdown-to-epub` (daarin staat `SKILL.md`).
3. Maak van **alleen die map** een nieuwe ZIP. De mapnaam moet gelijk zijn aan de skillnaam.
4. Ga naar **Instellingen → Mogelijkheden → Skills** en klik op **Skill uploaden**.
5. Zet de skill aan.

Skills in de Claude-app vragen een Pro-, Max-, Team- of Enterprise-abonnement en **Code-uitvoering en bestanden maken** moet aanstaan.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/smerchek/claude-epub-skill" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Productiviteit & tools</a>
