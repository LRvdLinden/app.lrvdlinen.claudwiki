---
description: >-
  About the Claude Wiki: who makes it, why it is unofficial and how you can add a skill or improvement yourself.
icon: circle-info
cover: ../../.gitbook/assets/cover-en-home.png
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
# About this wiki

The **Claude Wiki** is an unofficial guide to Claude skills in Dutch and English, made by **LRvdLinden**. This wiki is not affiliated with Anthropic. Claude is a product of Anthropic.

## Contribute

Missing a skill or is something out of date? The wiki is on GitHub: [LRvdLinden/app.lrvdlinen.claudwiki](https://github.com/LRvdLinden/app.lrvdlinen.claudwiki). Open an issue or pull request.

### Adding a new skill

Add an `add(...)` block in `tools/data.py` (Dutch) and the matching entry in `tools/en_data.py` (English), then run the build scripts. Keep this structure:

1. What does it do?
2. When do you use it?
3. Examples (what you type and what you get)
4. Install (tabs per platform)
5. Tips

*Last updated: November 2026.*
