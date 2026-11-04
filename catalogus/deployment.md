---
description: >-
  9 plugins uit de officiële Claude Code-marketplace in de categorie Deployen & hosting.
icon: rocket
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
# Deployen & hosting

9 plugins. Installeren in Claude Code: `/plugin install <naam>@claude-plugins-official`.

| Plugin | Maker | Wat het doet (beschrijving van de maker) | Installeren |
| --- | --- | --- | --- |
| [**azure**](https://github.com/microsoft/azure-skills) |  | Transform Claude into an Azure expert. This plugin integrates the Azure MCP server and specialized Azure skills to move beyond generic advice. It enables Claude to perform real-world tasks: listing resources, validating deployments, diagnosing infrastructure issues, and optimizing costs across 50+ Azure services. | `/plugin install azure@claude-plugins-official` |
| [**cloudflare**](https://github.com/cloudflare/skills) |  | Skills for the Cloudflare developer platform: Workers, Durable Objects, Agents SDK, MCP servers, Wrangler CLI, and web performance. | `/plugin install cloudflare@claude-plugins-official` |
| [**deploy-on-aws**](https://github.com/awslabs/agent-plugins) |  | Deploy applications to AWS with architecture recommendations, cost estimates, and IaC deployment. | `/plugin install deploy-on-aws@claude-plugins-official` |
| [**google-cloud-storage**](https://cloud.google.com/storage) | Google LLC | Official Google Cloud Storage (GCS) plugin. Manage buckets and objects, transfer data, and configure MCP, FUSE, IAM, security, lifecycle rules, signed URLs, Terraform, and the CLI. | `/plugin install google-cloud-storage@claude-plugins-official` |
| [**hostinger**](https://www.hostinger.com) | Hostinger | Deploy, manage and monitor your Hostinger services directly from Claude Code. The plugin connects Claude to Hostinger's remote MCP server, so you can ship sites and apps, manage domains and DNS, run WordPress and operate VPS servers without leaving your coding environment. There's nothing to install on your machine: no Node.js, no npm, no local server. Key features include one-prompt deployments for static sites, Node.js apps (built on Hostinger), full WordPress site imports, and WordPress plugins and themes, plus static and PHP sites on the Agency Plan. Beyond deployments, Claude can search and register domains, edit DNS records and snapshots, check build logs, and manage mailboxes, online stores, email marketing contacts, subscriptions and orders. It can also control VPS firewalls, snapshots and monitoring. Sign in through your browser (OAuth) on first use, or set a `HOSTINGER_API_TOKEN` from hPanel. How to use: there are no commands to memorize. Describe what you want and Claude picks the right tool or deployment skill. Try "deploy my static site to Hostinger", "deploy this Next.js app to example.com", "create an A record pointing example.com to 1.2.3.4", or "show VPS metrics for the last 24 hours." | `/plugin install hostinger@claude-plugins-official` |
| [**railway**](https://docs.railway.com/ai/claude-code-plugin) |  | Deploy and manage apps, databases, and infrastructure on Railway. Covers project setup, deploys, environment configuration, networking, troubleshooting, and monitoring. | `/plugin install railway@claude-plugins-official` |
| [**render**](https://render.com) | Render | Deploy, debug, and monitor applications on Render. Includes skills, an agent, slash commands, and a render.yaml validation hook. | `/plugin install render@claude-plugins-official` |
| [**valtown**](https://val.town) | Val Town | Build and deploy on Val Town. Bundles the Val Town MCP server and platform skills (HTTP vals, cron/intervals, SQLite, email, OAuth, React UI, third-party integrations, templates). | `/plugin install valtown@claude-plugins-official` |
| [**vercel**](https://github.com/vercel/vercel-plugin) |  | Vercel deployment platform integration. Manage deployments, check build status, access logs, configure domains, and control your frontend infrastructure directly from Claude Code. | `/plugin install vercel@claude-plugins-official` |
