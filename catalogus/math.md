---
description: >-
  2 plugins uit de officiële Claude Code-marketplace in de categorie Wiskunde.
icon: square-root-variable
cover: ../.gitbook/assets/cover-catalogus.png
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
# Wiskunde

2 plugins. Installeren in Claude Code: `/plugin install <naam>@claude-plugins-official`.

| Plugin | Maker | Wat het doet (beschrijving van de maker) | Installeren |
| --- | --- | --- | --- |
| [**math-olympiad**](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/math-olympiad) | Anthropic | Solve competition math (IMO, Putnam, USAMO) with adversarial verification that catches what self-verification misses. Fresh-context verifiers attack proofs with specific failure patterns. Calibrated abstention over bluffing. | `/plugin install math-olympiad@claude-plugins-official` |
| [**math-proof**](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/math-proof) | Anthropic | Two skills for hard mathematics problems, each ending in a self-contained proof.md: /math-proof:solo has the session work the problem itself in stages with a notes file; /math-proof:siege works on it for hours in rounds of judge and worker sub-agents and says plainly what is and is not proved. | `/plugin install math-proof@claude-plugins-official` |
