---
description: >-
  Beheer Firestore, Authentication, Cloud Functions, Hosting en Storage vanuit Claude.
icon: fire
cover: ../../.gitbook/assets/cover-cloud.png
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

# Firebase

| | |
| --- | --- |
| **Maker** | Google · officiële Claude-marketplace |
| **Werkt in** | Claude Code |
| **Kosten** | Plugin gratis; je hebt een Firebase-project nodig |
| **Bron** | [github.com/anthropics/claude-plugins-public/tree/main/external_plugins/firebase](https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/firebase) |

## Wat doet het?

De Firebase-plugin geeft Claude toegang tot je Firebase-backend: Firestore-databases, authenticatie, cloud functions, hosting en opslag. Handig voor apps die Firebase als backend gebruiken, zoals veel iOS-apps.

## Wanneer gebruik je het?

* Je app gebruikt Firebase.

## Voorbeelden

{% code title="Voorbeeld 1: wat je typt" overflow="wrap" %}
```
Maak een Firestore-regel zodat gebruikers alleen hun eigen meldingen kunnen lezen.
```
{% endcode %}

**Wat je krijgt:** Firestore security rules plus uitleg.

## Installeren

{% tabs %}
{% tab title="Claude Code" %}
Deze plugin staat in de **officiële Anthropic-marketplace**, die standaard al gekoppeld is:

```bash
/plugin install firebase@claude-plugins-official
```

Of blader via `/plugin` → **Discover** en kies de plugin uit de lijst.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Community-skills zijn niet door Anthropic gecontroleerd. Lees de `SKILL.md` voordat je installeert. Zie [Veilig installeren](../../basis/veiligheid.md).
{% endhint %}

<a href="https://github.com/anthropics/claude-plugins-public/tree/main/external_plugins/firebase" class="button primary" data-icon="github">Bekijk op GitHub</a> <a href="./" class="button secondary" data-icon="arrow-left">Terug naar Data, cloud & betalen</a>
