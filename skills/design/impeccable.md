---
description: >-
  Een designvocabulaire voor je agent: commando's als polish, bolder, critique en audit, plus een detector voor 'AI-slop'.
icon: gem
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

# Impeccable

| | |
| --- | --- |
| **Maker** | Paul Bakaus (community) |
| **Werkt in** | Claude Code (+ Cursor, Codex, Copilot en meer) |
| **Kosten** | Gratis (open source) |
| **Bron** | [github.com/pbakaus/impeccable](https://github.com/pbakaus/impeccable) |

## Wat doet het?

Impeccable geeft Claude een gedeelde taal om ontwerpen te sturen. Je zegt bijvoorbeeld *polish*, *bolder*, *critique* of *audit* en Claude weet precies wat je bedoelt. Er zit een detector bij die typische AI-designfouten ('slop') opspoort, en een hook die elk UI-bestand dat Claude aanpast automatisch controleert voordat hij zegt dat hij klaar is. De CLI werkt ook los, bijvoorbeeld in je CI.

## Wanneer gebruik je het?

* Je wilt een ontwerp in kleine, gerichte stappen verbeteren.
* Je wilt automatisch gewaarschuwd worden voor generiek ogende UI.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
critique de homepage en daarna polish de hero-sectie
```
{% endcode %}

**Wat je krijgt:** Eerst een kritische review, daarna een verfijnde hero.

{% code title="Voorbeeld 2: wat je typt" overflow="wrap" %}
```
npx impeccable detect src/
```
{% endcode %}

**Wat je krijgt:** Een scan van je code op typische AI-designpatronen.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
```bash
/plugin marketplace add pbakaus/impeccable
```

Open daarna `/plugin` en installeer **Impeccable**. Zeg 'ja' tegen de design-hook: die vangt de meeste fouten automatisch af.
{% endtab %}

{% tab title="CLI" %}
```bash
npx impeccable detect src/                  # map scannen
npx impeccable detect https://example.com   # live pagina scannen
```
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Tips**

* Documentatie: [impeccable.style/docs](https://impeccable.style/docs).
{% endhint %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/pbakaus/impeccable" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Design & frontend</a>
