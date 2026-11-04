---
description: >-
  Voor wie met Claude Code bouwt: engineering-workflows, code reviews, testen, MCP-servers, Vercel/React, Terraform en n8n.
icon: code
cover: ../../.gitbook/assets/cover-ontwikkeling.png
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
# Ontwikkelen & code

Voor wie met Claude Code bouwt: engineering-workflows, code reviews, testen, MCP-servers, Vercel/React, Terraform en n8n.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody>
<tr><td><strong>Agent Skills (Addy Osmani)</strong></td><td>Productieklare engineering-workflows: spec schrijven, taken opsplitsen, stap voor stap bouwen, testen en opleveren.</td><td><a href="agent-skills-addy.md">agent-skills-addy.md</a></td><td></td></tr>
<tr><td><strong>Officiële dev-plugins</strong></td><td>Anthropics eigen Claude Code-plugins: code review, feature-dev, commits, PR-review, security en hooks.</td><td><a href="official-dev-plugins.md">official-dev-plugins.md</a></td><td></td></tr>
<tr><td><strong>MCP Builder</strong></td><td>Gids om zelf goede MCP-servers te bouwen in Python (FastMCP) of TypeScript.</td><td><a href="mcp-builder.md">mcp-builder.md</a></td><td></td></tr>
<tr><td><strong>Webapp Testing</strong></td><td>Test lokale webapps met Playwright: klikken, screenshots maken en browserlogs bekijken.</td><td><a href="webapp-testing.md">webapp-testing.md</a></td><td></td></tr>
<tr><td><strong>Claude API</strong></td><td>Actuele naslag voor bouwen met de Claude API en SDK's: modellen, prijzen, tools, streaming en caching.</td><td><a href="claude-api.md">claude-api.md</a></td><td></td></tr>
<tr><td><strong>Vercel Agent Skills</strong></td><td>React- en Next.js-best practices, webdesign-richtlijnen en deployen naar Vercel.</td><td><a href="vercel-agent-skills.md">vercel-agent-skills.md</a></td><td></td></tr>
<tr><td><strong>n8n Skills</strong></td><td>Expertkennis om foutloze n8n-workflows te bouwen via de n8n-MCP-server.</td><td><a href="n8n-skills.md">n8n-skills.md</a></td><td></td></tr>
<tr><td><strong>Terraform Skill</strong></td><td>Best practices voor Terraform en OpenTofu: modules, testen, CI/CD en productieklare infrastructuur.</td><td><a href="terraform-skill.md">terraform-skill.md</a></td><td></td></tr>
<tr><td><strong>Playwright Skill</strong></td><td>Laat Claude zelf Playwright-scripts schrijven en draaien, van simpele paginatests tot lange flows.</td><td><a href="playwright-skill.md">playwright-skill.md</a></td><td></td></tr>
<tr><td><strong>Context Engineering Kit</strong></td><td>Geavanceerde technieken: DDD, kaizen, subagent-driven development, critique en prompt engineering.</td><td><a href="context-engineering-kit.md">context-engineering-kit.md</a></td><td></td></tr>
<tr><td><strong>Everything Claude Code (ECC)</strong></td><td>Een complete 'agent harness': agents, skills, commando's, hooks en regels in één groot pakket.</td><td><a href="everything-claude-code.md">everything-claude-code.md</a></td><td></td></tr>
<tr><td><strong>Context7</strong></td><td>Haalt actuele, versie-specifieke documentatie en codevoorbeelden op, zodat Claude geen verouderde API's gebruikt.</td><td><a href="context7.md">context7.md</a></td><td></td></tr>
<tr><td><strong>Playwright (MCP)</strong></td><td>De Playwright MCP-server van Microsoft: Claude bedient een browser, maakt screenshots en test je webapp.</td><td><a href="playwright-mcp.md">playwright-mcp.md</a></td><td></td></tr>
<tr><td><strong>Chrome DevTools</strong></td><td>Bedien en inspecteer een live Chrome-browser: performance-traces, netwerkverkeer en console-fouten.</td><td><a href="chrome-devtools.md">chrome-devtools.md</a></td><td></td></tr>
<tr><td><strong>Learning & Explanatory output styles</strong></td><td>Laat Claude uitleggen wat hij doet (Explanatory) of jou zelf stukken code laten schrijven om van te leren (Learning).</td><td><a href="output-styles.md">output-styles.md</a></td><td></td></tr>
<tr><td><strong>Session Report</strong></td><td>Maakt een interactief HTML-rapport van je Claude Code-gebruik: tokens, cache, subagents, skills en de duurste prompts.</td><td><a href="session-report.md">session-report.md</a></td><td></td></tr>
</tbody></table>

## Snel overzicht

| Skill | Werkt in | Maker |
| --- | --- | --- |
| [Agent Skills (Addy Osmani)](agent-skills-addy.md) | Claude Code (+ andere agents) | Addy Osmani (community) |
| [Officiële dev-plugins](official-dev-plugins.md) | Claude Code | Anthropic (officieel) |
| [MCP Builder](mcp-builder.md) | Claude-app, Claude Code, API | Anthropic (officieel) |
| [Webapp Testing](webapp-testing.md) | Claude Code (en Claude-app met code-uitvoering) | Anthropic (officieel) |
| [Claude API](claude-api.md) | Claude Code, Claude-app, API | Anthropic (officieel) |
| [Vercel Agent Skills](vercel-agent-skills.md) | Claude Code (+ andere agents) | Vercel (officieel van de makers) |
| [n8n Skills](n8n-skills.md) | Claude Code (met de n8n-mcp-server) | czlonkowski (community) |
| [Terraform Skill](terraform-skill.md) | Claude Code (+ andere agents) | Anton Babenko (community) |
| [Playwright Skill](playwright-skill.md) | Claude Code (+ Cursor en meer) | lackeyjb (community) |
| [Context Engineering Kit](context-engineering-kit.md) | Claude Code (+ OpenCode, Cursor en meer) | NeoLab (community) |
| [Everything Claude Code (ECC)](everything-claude-code.md) | Claude Code (+ andere agents) | affaan-m (community) |
| [Context7](context7.md) | Claude Code | Upstash · officiële Claude-marketplace |
| [Playwright (MCP)](playwright-mcp.md) | Claude Code | Microsoft · officiële Claude-marketplace |
| [Chrome DevTools](chrome-devtools.md) | Claude Code | Google · officiële Claude-marketplace |
| [Learning & Explanatory output styles](output-styles.md) | Claude Code | Anthropic · officiële Claude-marketplace |
| [Session Report](session-report.md) | Claude Code | Anthropic · officiële Claude-marketplace |
