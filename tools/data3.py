# Extra skills (NL + EN in één keer): partner-plugins uit de officiële marketplace en de losse rol-plugins van Anthropic
from install import tabs, tab, cc_official
from en_data import E
import json, os
_MP = {p["name"]: p for p in json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "marketplace-official.json")))["plugins"]}

NEWCATS3 = [("koppelingen", "Apps koppelen", "plug",
             "Plugins die Claude verbinden met de apps die je al gebruikt: Figma, Notion, Canva, Slack, GitHub, Jira, Zapier en meer. Claude kan er dan zelf dingen in opzoeken en doen.")]
CAT_EN3 = {"koppelingen": ("Connect your apps", "Plugins that connect Claude to the apps you already use: Figma, Notion, Canva, Slack, GitHub, Jira, Zapier and more. Claude can then look things up and take actions in them.")}

S3 = []

def tab_en_official(plugin, extra=""):
    return f'''{{% tabs %}}
{{% tab title="Claude Code" %}}
This plugin is in the **official Anthropic marketplace**, which is connected by default:

```bash
/plugin install {plugin}@claude-plugins-official
```

Or browse via `/plugin` → **Discover** and pick the plugin from the list.
{extra}
{{% endtab %}}
{{% endtabs %}}'''

def mp(slug, plugin, name, cat, icon, vendor, account, nl, en, nl_extra="", en_extra=""):
    """nl/en = (tagline, wat, [wanneer], [(prompt, resultaat)], [tips])"""
    t, w, wa, v, tips = nl
    S3.append(dict(slug=slug, name=name, cat=cat, icon=icon, tagline=t, wat=w, wanneer=wa, voorbeelden=v, tips=tips,
                   maker=f"{vendor} · officiële Claude-marketplace", werkt="Claude Code",
                   prijs=(f"Plugin gratis; {account}" if account else "Gratis"),
                   bron=_MP[plugin].get("homepage") or "https://github.com/anthropics/claude-plugins-official", install=tabs(cc_official(plugin, nl_extra))))
    t2, w2, wa2, v2, tips2 = en
    acc_en = {"je hebt een account bij": "you need an account with", "nodig": ""}
    a_en = account
    if account:
        for k, x in acc_en.items(): a_en = a_en.replace(k, x)
    E[slug] = dict(t=t2, w=w2, wa=wa2, v=v2, tips=tips2, maker=f"{vendor} · official Claude marketplace", werkt="Claude Code",
                   prijs=((f"Plugin free; requires an API key from {vendor}" if "API-sleutel" in account else f"Plugin free; requires a {vendor} account") if account else "Free"), install=tab_en_official(plugin, en_extra))

# ───────── APPS KOPPELEN ─────────
mp("figma", "figma", "Figma", "koppelingen", "figma", "Figma", "je hebt een account bij Figma nodig",
   ("Lees Figma-ontwerpen, haal componenten en design tokens eruit en zet designs om naar code.",
    "Met de Figma-plugin kijkt Claude rechtstreeks in je Figma-bestanden. Hij leest frames en componenten, haalt kleuren, typografie en spacing (design tokens) op en zet een ontwerp om naar werkende code. Zo verdwijnt het overtypen tussen design en development.",
    ["Je ontwerpt in Figma en wilt het snel naar code brengen.", "Je wilt dat de code exact dezelfde kleuren en spacing gebruikt als het ontwerp."],
    [("Bouw het scherm 'Instellingen' uit mijn Figma-bestand na in SwiftUI.", "SwiftUI-code die het ontwerp volgt, met de juiste kleuren en maten.")], []),
   ("Read Figma designs, extract components and design tokens and turn designs into code.",
    "With the Figma plugin Claude looks straight into your Figma files. It reads frames and components, pulls out colours, typography and spacing (design tokens) and turns a design into working code. No more retyping between design and development.",
    ["You design in Figma and want to bring it to code quickly.", "You want the code to use exactly the same colours and spacing as the design."],
    [("Rebuild the 'Settings' screen from my Figma file in SwiftUI.", "SwiftUI code that follows the design, with the right colours and sizes.")], []))
mp("notion", "notion", "Notion", "koppelingen", "book", "Notion", "je hebt een account bij Notion nodig",
   ("Zoek in Notion, maak en wijzig pagina's en beheer databases vanuit Claude.",
    "De Notion-plugin geeft Claude toegang tot je Notion-werkruimte. Hij zoekt pagina's op, maakt nieuwe documenten, werkt bestaande bij en beheert databases. Handig als je documentatie, notulen of planningen in Notion bijhoudt.",
    ["Je team werkt in Notion.", "Je wilt dat Claude documentatie direct op de juiste plek zet."],
    [("Zet de notulen van vandaag als nieuwe pagina in de Notion-database 'Vergaderingen'.", "Een nieuwe Notion-pagina met de notulen.")], []),
   ("Search Notion, create and edit pages and manage databases from Claude.",
    "The Notion plugin gives Claude access to your Notion workspace. It looks up pages, creates new documents, updates existing ones and manages databases. Handy if you keep documentation, minutes or plans in Notion.",
    ["Your team works in Notion.", "You want Claude to put documentation in the right place directly."],
    [("Add today's minutes as a new page in the 'Meetings' Notion database.", "A new Notion page with the minutes.")], []))
mp("canva", "canva", "Canva", "koppelingen", "palette", "Canva", "je hebt een account bij Canva nodig",
   ("Maak, bewerk, verschaal en controleer Canva-ontwerpen op je huisstijl.",
    "Met de Canva-plugin maakt Claude ontwerpen in Canva, past ze aan, zet ze om naar andere formaten (bijvoorbeeld van post naar story) en controleert of ze bij je merk passen. Hij werkt via de officiële Canva MCP-server.",
    ["Je maakt social posts of flyers in Canva.", "Je wilt één ontwerp in meerdere formaten."],
    [("Maak van deze Instagram-post ook een story en een LinkedIn-banner.", "Drie Canva-ontwerpen in de juiste formaten.")], []),
   ("Create, edit, resize and brand-check Canva designs.",
    "With the Canva plugin Claude creates designs in Canva, edits them, resizes them to other formats (for example from post to story) and checks whether they fit your brand. It works through the official Canva MCP server.",
    ["You make social posts or flyers in Canva.", "You want one design in several formats."],
    [("Turn this Instagram post into a story and a LinkedIn banner as well.", "Three Canva designs in the right formats.")], []))
mp("miro", "miro", "Miro", "koppelingen", "chalkboard", "Miro", "je hebt een account bij Miro nodig",
   ("Lees Miro-borden, maak diagrammen en zet ideeën van het bord om naar code of plannen.",
    "De Miro-plugin geeft Claude veilige toegang tot je Miro-borden. Hij leest wat er op een bord staat, maakt diagrammen en kan een brainstorm of flow op het bord vertalen naar een plan of code.",
    ["Je brainstormt of plant in Miro."],
    [("Maak van de sticky notes op ons retro-bord een lijst met acties.", "Een gestructureerde actielijst.")], []),
   ("Read Miro boards, create diagrams and turn ideas on the board into code or plans.",
    "The Miro plugin gives Claude secure access to your Miro boards. It reads what's on a board, creates diagrams and can translate a brainstorm or flow on the board into a plan or code.",
    ["You brainstorm or plan in Miro."],
    [("Turn the sticky notes on our retro board into a list of actions.", "A structured action list.")], []))
mp("slack", "slack", "Slack", "koppelingen", "slack", "Slack", "je hebt een Slack-werkruimte nodig",
   ("Zoek in Slack-berichten, lees kanalen en threads en vind snel eerdere discussies.",
    "Met de Slack-plugin zoekt Claude in je Slack-werkruimte: berichten, kanalen en threads. Zo vindt hij snel de context van een eerdere discussie of beslissing, zonder dat je zelf hoeft te scrollen.",
    ["Belangrijke afspraken staan ergens in Slack.", "Je wilt een samenvatting van een drukke thread."],
    [("Wat is er vorige week in #ontwikkeling besloten over de release?", "Een samenvatting met links naar de berichten.")], []),
   ("Search Slack messages, read channels and threads and quickly find earlier discussions.",
    "With the Slack plugin Claude searches your Slack workspace: messages, channels and threads. That way it quickly finds the context of an earlier discussion or decision, without you having to scroll.",
    ["Important agreements are buried somewhere in Slack.", "You want a summary of a busy thread."],
    [("What was decided in #development last week about the release?", "A summary with links to the messages.")], []))
mp("github", "github", "GitHub", "koppelingen", "github", "GitHub", "je hebt een GitHub-account nodig",
   ("De officiële GitHub MCP-server: issues, pull requests, code reviews en repo's doorzoeken.",
    "Met de GitHub-plugin werkt Claude rechtstreeks met GitHub: issues aanmaken, pull requests beheren en reviewen, repositories doorzoeken en de volledige GitHub-API gebruiken vanuit Claude Code.",
    ["Je beheert je code en issues op GitHub."],
    [("Maak issues aan voor alle TODO's in deze map en label ze als 'tech-debt'.", "Nieuwe GitHub-issues met labels.")], []),
   ("The official GitHub MCP server: issues, pull requests, code reviews and searching repos.",
    "With the GitHub plugin Claude works with GitHub directly: create issues, manage and review pull requests, search repositories and use the full GitHub API from Claude Code.",
    ["You manage your code and issues on GitHub."],
    [("Create issues for every TODO in this folder and label them 'tech-debt'.", "New GitHub issues with labels.")], []))
mp("gitlab", "gitlab", "GitLab", "koppelingen", "gitlab", "GitLab", "je hebt een GitLab-account nodig",
   ("Repositories, merge requests, CI/CD-pipelines, issues en wiki's in GitLab.",
    "De GitLab-plugin koppelt Claude aan het GitLab DevOps-platform: repositories beheren, merge requests, CI/CD-pipelines volgen, issues en wiki's.",
    ["Je team gebruikt GitLab in plaats van GitHub."],
    [("Waarom faalt de laatste pipeline op main?", "De foutmelding uit de pipeline plus een voorstel voor de oplossing.")], []),
   ("Repositories, merge requests, CI/CD pipelines, issues and wikis in GitLab.",
    "The GitLab plugin connects Claude to the GitLab DevOps platform: manage repositories, merge requests, follow CI/CD pipelines, issues and wikis.",
    ["Your team uses GitLab instead of GitHub."],
    [("Why is the latest pipeline on main failing?", "The error from the pipeline plus a proposed fix.")], []))
mp("linear", "linear", "Linear", "koppelingen", "list-check", "Linear", "je hebt een account bij Linear nodig",
   ("Issues maken en bijwerken, projecten beheren en zoeken in Linear.",
    "Met de Linear-plugin maakt Claude issues aan, beheert projecten, werkt statussen bij en zoekt in je werkruimtes. Ideaal om bugs of taken direct vanuit je code in Linear te zetten.",
    ["Je plant je softwarewerk in Linear."],
    [("Zet deze drie bugs als issues in Linear, project 'App 2.0', met prioriteit hoog.", "Drie nieuwe Linear-issues.")], []),
   ("Create and update issues, manage projects and search in Linear.",
    "With the Linear plugin Claude creates issues, manages projects, updates statuses and searches your workspaces. Ideal for putting bugs or tasks straight from your code into Linear.",
    ["You plan your software work in Linear."],
    [("Add these three bugs as issues in Linear, project 'App 2.0', with high priority.", "Three new Linear issues.")], []))
mp("atlassian", "atlassian", "Atlassian (Jira & Confluence)", "koppelingen", "atlassian", "Atlassian", "je hebt een Atlassian-account nodig",
   ("Zoek en maak Jira-issues, beheer sprints en lees Confluence-documentatie.",
    "De Atlassian-plugin verbindt Claude met Jira en Confluence. Claude zoekt en maakt issues, beheert sprints en raadpleegt documentatie in Confluence, zodat je ontwikkelwerk en documentatie op één lijn blijven.",
    ["Je organisatie werkt met Jira of Confluence."],
    [("Welke Jira-issues staan nog open in de huidige sprint en wie is eigenaar?", "Een overzicht per eigenaar.")], []),
   ("Search and create Jira issues, manage sprints and read Confluence documentation.",
    "The Atlassian plugin connects Claude to Jira and Confluence. Claude searches and creates issues, manages sprints and consults documentation in Confluence, so your development work and docs stay aligned.",
    ["Your organisation works with Jira or Confluence."],
    [("Which Jira issues are still open in the current sprint and who owns them?", "An overview per owner.")], []))
mp("asana", "asana", "Asana", "koppelingen", "check-double", "Asana", "je hebt een account bij Asana nodig",
   ("Taken maken en beheren, projecten doorzoeken en voortgang volgen in Asana.",
    "De Asana-plugin koppelt Claude aan Asana: taken maken en toewijzen, projecten doorzoeken en voortgang bijhouden. Eenmalig stel je een Asana-app in met het commando `/asana-setup`.",
    ["Je plant projecten in Asana."],
    [("Maak voor elke actie uit deze notulen een taak in Asana met een deadline.", "Asana-taken met eigenaren en deadlines.")], []),
   ("Create and manage tasks, search projects and track progress in Asana.",
    "The Asana plugin connects Claude to Asana: create and assign tasks, search projects and track progress. You set up an Asana app once with the `/asana-setup` command.",
    ["You plan projects in Asana."],
    [("Create an Asana task with a deadline for every action in these minutes.", "Asana tasks with owners and deadlines.")], []),
   nl_extra="\nDaarna eenmalig: `/asana-setup`.", en_extra="\nThen once: `/asana-setup`.")
mp("airtable", "airtable", "Airtable", "koppelingen", "table-cells", "Airtable", "je hebt een account bij Airtable nodig",
   ("Gebruik Airtable als database en werklaag voor je agents: tabellen, kanban, kalenders en meer.",
    "Met de Airtable-plugin leest en schrijft Claude gestructureerde data in Airtable, voor product, marketing, sales, operations, HR of een eigen bedrijfsapp. Je data blijft zichtbaar in de vertrouwde Airtable-weergaven.",
    ["Je houdt lijsten of processen bij in Airtable."],
    [("Voeg de inschrijvingen uit deze mail toe aan onze Airtable 'Vrijwilligers'.", "Nieuwe rijen in je Airtable-basis.")], []),
   ("Use Airtable as the database and operations layer for your agents: grids, kanban, calendars and more.",
    "With the Airtable plugin Claude reads and writes structured data in Airtable, for product, marketing, sales, operations, HR or a custom business app. Your data stays visible in the familiar Airtable views.",
    ["You keep lists or processes in Airtable."],
    [("Add the sign-ups from this email to our 'Volunteers' Airtable.", "New rows in your Airtable base.")], []))
mp("zapier", "zapier", "Zapier", "koppelingen", "bolt", "Zapier", "je hebt een account bij Zapier nodig",
   ("Verbind meer dan 8.000 apps en voer Zapier-acties uit vanuit Claude.",
    "De Zapier-plugin opent de deur naar meer dan 8.000 apps. Claude zoekt de juiste Zapier-actie, zet hem aan en voert hem uit: van een rij in Google Sheets tot een sms of een bericht in Teams.",
    ["De app die je wilt koppelen heeft geen eigen plugin.", "Je gebruikt Zapier al voor automatiseringen."],
    [("Zet elke nieuwe aanmelding uit dit formulier in Google Sheets en stuur me een sms.", "Een werkende Zapier-actie.")], []),
   ("Connect 8,000+ apps and run Zapier actions from Claude.",
    "The Zapier plugin opens the door to more than 8,000 apps. Claude finds the right Zapier action, enables it and runs it: from a row in Google Sheets to a text message or a Teams message.",
    ["The app you want to connect has no plugin of its own.", "You already use Zapier for automations."],
    [("Put every new sign-up from this form into Google Sheets and send me a text.", "A working Zapier action.")], []))
mp("box", "box", "Box", "koppelingen", "box", "Box", "je hebt een account bij Box nodig",
   ("Zoek en organiseer bestanden in Box en laat Box AI vragen beantwoorden over je documenten.",
    "Met de Box-plugin zoekt Claude bestanden, ordent mappen en werkt samen met je team in Box. Via Box AI beantwoordt hij vragen, vat hij documenten samen en haalt hij gegevens eruit.",
    ["Je organisatie bewaart documenten in Box."],
    [("Vat alle contracten in de map 'Leveranciers 2026' samen.", "Een samenvatting per contract.")], []),
   ("Search and organise files in Box and let Box AI answer questions about your documents.",
    "With the Box plugin Claude searches files, organises folders and collaborates with your team in Box. Through Box AI it answers questions, summarises documents and extracts data.",
    ["Your organisation stores documents in Box."],
    [("Summarise every contract in the 'Suppliers 2026' folder.", "A summary per contract.")], []))
mp("dropbox", "dropbox", "Dropbox", "koppelingen", "dropbox", "Dropbox", "je hebt een account bij Dropbox nodig",
   ("Zoek en orden je Dropbox-bestanden, sla resultaten op en maak deellinks.",
    "De Dropbox-plugin koppelt je Dropbox aan Claude: bestanden zoeken en ordenen, wat Claude maakt direct opslaan en deellinks aanmaken. Je bestaande Dropbox-rechten blijven gelden.",
    ["Je bewaart je bestanden in Dropbox."],
    [("Sla deze presentatie op in Dropbox/Wijkraad en geef me een deellink.", "Het bestand in Dropbox plus een link.")], []),
   ("Search and organise your Dropbox files, save results and create sharing links.",
    "The Dropbox plugin connects your Dropbox to Claude: search and organise files, save what Claude makes straight away and create sharing links. Your existing Dropbox permissions stay in place.",
    ["You keep your files in Dropbox."],
    [("Save this presentation in Dropbox/Council and give me a sharing link.", "The file in Dropbox plus a link.")], []))
mp("hubspot-sales", "hubspot-sales", "HubSpot Sales", "koppelingen", "hubspot", "HubSpot", "je hebt een HubSpot-account nodig",
   ("Je hele HubSpot-salesdag vanuit Claude: contacten importeren, ochtendbriefing, gespreksvoorbereiding en follow-ups.",
    "Skills van HubSpot zelf voor de complete salesdag: contacten en deals importeren, een geprioriteerde ochtendbriefing, gesprekken voorbereiden met alle CRM-context en persoonlijke follow-ups opstellen.",
    ["Je verkoopt met HubSpot als CRM."],
    [("Geef me mijn ochtendbriefing: welke deals vragen vandaag aandacht?", "Een geprioriteerde lijst met acties.")], []),
   ("Your whole HubSpot sales day from Claude: importing contacts, morning brief, call prep and follow-ups.",
    "Skills from HubSpot itself for the complete sales day: import contacts and deals, a prioritised morning brief, prepare calls with full CRM context and draft personalised follow-ups.",
    ["You sell with HubSpot as your CRM."],
    [("Give me my morning brief: which deals need attention today?", "A prioritised list of actions.")], []))
mp("monday-crm", "monday-crm", "monday CRM", "koppelingen", "calendar-week", "monday.com", "je hebt een account bij monday.com nodig",
   ("Je monday CRM in gewone taal: pipeline opzetten, dealbriefing, forecast-dashboard en data opschonen.",
    "Met deze plugin bestuur je monday CRM in gewone taal. Bouw een pipeline vanaf nul, begin de dag met een gerangschikte dealbriefing, maak een forecast-dashboard, controleer de gezondheid van je borden, schoon rommelige data op en maak van vergadernotities deal-updates.",
    ["Je gebruikt monday.com als CRM."],
    [("Maak van deze vergadernotities updates voor de juiste deals.", "Bijgewerkte deals in monday CRM.")], []),
   ("Your monday CRM in plain language: build a pipeline, deal briefing, forecast dashboard and data clean-up.",
    "With this plugin you run monday CRM in plain language. Build a pipeline from scratch, start the day with a ranked deal briefing, create a forecast dashboard, audit board health, clean up messy data and turn meeting notes into deal updates.",
    ["You use monday.com as your CRM."],
    [("Turn these meeting notes into updates for the right deals.", "Updated deals in monday CRM.")], []))
mp("intercom", "intercom", "Intercom", "koppelingen", "comments", "Intercom", "je hebt een Intercom-werkruimte nodig",
   ("Zoek in klantgesprekken, analyseer supportpatronen en zoek contacten en bedrijven op.",
    "De Intercom-plugin geeft Claude realtime inzicht in je klantcontact: gesprekken doorzoeken, patronen in supportvragen analyseren, contacten en bedrijven opzoeken en zelfs de Intercom Messenger installeren.",
    ["Je doet klantenservice via Intercom."],
    [("Wat zijn de vijf meest gestelde vragen van deze maand?", "Een top 5 met voorbeelden.")], []),
   ("Search customer conversations, analyse support patterns and look up contacts and companies.",
    "The Intercom plugin gives Claude real-time insight into your customer contact: search conversations, analyse patterns in support questions, look up contacts and companies and even install the Intercom Messenger.",
    ["You do customer support through Intercom."],
    [("What are the five most-asked questions this month?", "A top 5 with examples.")], []))

# ───────── ONTWIKKELING ─────────
mp("context7", "context7", "Context7", "ontwikkeling", "book-open", "Upstash", "",
   ("Haalt actuele, versie-specifieke documentatie en codevoorbeelden op, zodat Claude geen verouderde API's gebruikt.",
    "Context7 (van Upstash) koppelt Claude aan een gehoste documentatiedienst. Claude haalt de documentatie en codevoorbeelden op van precies de versie van een bibliotheek die jij gebruikt. Er is geen lokale Node.js nodig.",
    ["Claude gebruikt functies die in jouw versie niet (meer) bestaan.", "Je werkt met een snel veranderend framework."],
    [("Gebruik context7 en bouw dit met de nieuwste versie van Next.js.", "Code volgens de actuele documentatie.")], []),
   ("Fetches up-to-date, version-specific documentation and code examples, so Claude doesn't use outdated APIs.",
    "Context7 (by Upstash) connects Claude to a hosted documentation service. Claude pulls the documentation and code examples for exactly the version of a library you use. No local Node.js required.",
    ["Claude uses functions that don't (or no longer) exist in your version.", "You work with a fast-changing framework."],
    [("Use context7 and build this with the latest version of Next.js.", "Code that follows the current documentation.")], []))
mp("playwright-mcp", "playwright", "Playwright (MCP)", "ontwikkeling", "masks-theater", "Microsoft", "",
   ("De Playwright MCP-server van Microsoft: Claude bedient een browser, maakt screenshots en test je webapp.",
    "Met deze plugin krijgt Claude een echte browser via de Playwright MCP-server van Microsoft. Hij opent pagina's, klikt, vult formulieren in, maakt screenshots en voert end-to-end-tests uit.",
    ["Je wilt dat Claude zelf controleert of je website werkt."],
    [("Open mijn site, log in met het testaccount en controleer of het dashboard laadt.", "Een testverslag met screenshots.")], []),
   ("Microsoft's Playwright MCP server: Claude drives a browser, takes screenshots and tests your web app.",
    "With this plugin Claude gets a real browser through Microsoft's Playwright MCP server. It opens pages, clicks, fills in forms, takes screenshots and runs end-to-end tests.",
    ["You want Claude to check for itself that your website works."],
    [("Open my site, log in with the test account and check that the dashboard loads.", "A test report with screenshots.")], []))
mp("chrome-devtools", "chrome-devtools-mcp", "Chrome DevTools", "ontwikkeling", "chrome", "Google", "",
   ("Bedien en inspecteer een live Chrome-browser: performance-traces, netwerkverkeer en console-fouten.",
    "Met Chrome DevTools MCP kijkt Claude mee in een echte Chrome-browser. Hij neemt performance-traces op, analyseert netwerkverzoeken, leest console-meldingen met leesbare stacktraces en automatiseert acties met Puppeteer.",
    ["Je website is traag en je wilt weten waarom.", "Je zoekt een fout die alleen in de browser optreedt."],
    [("Neem een performance-trace op van mijn homepage en vertel wat hem traag maakt.", "De grootste vertragers met concrete oplossingen.")], []),
   ("Control and inspect a live Chrome browser: performance traces, network traffic and console errors.",
    "With Chrome DevTools MCP Claude looks along in a real Chrome browser. It records performance traces, analyses network requests, reads console messages with source-mapped stack traces and automates actions with Puppeteer.",
    ["Your website is slow and you want to know why.", "You're hunting a bug that only happens in the browser."],
    [("Record a performance trace of my homepage and tell me what makes it slow.", "The biggest bottlenecks with concrete fixes.")], []))
mp("output-styles", "learning-output-style", "Learning & Explanatory output styles", "ontwikkeling", "chalkboard-user", "Anthropic", "",
   ("Laat Claude uitleggen wat hij doet (Explanatory) of jou zelf stukken code laten schrijven om van te leren (Learning).",
    "Twee plugins van Anthropic die de manier van antwoorden veranderen. **learning-output-style** vraagt je op belangrijke momenten zelf een stukje code te schrijven, zodat je leert in plaats van alleen kijkt. **explanatory-output-style** voegt uitleg toe over waarom Claude bepaalde keuzes maakt en welke patronen in je codebase zitten.",
    ["Je wilt programmeren leren terwijl je met Claude bouwt.", "Je wilt begrijpen waarom Claude iets op een bepaalde manier doet."],
    [("(na installatie) Voeg een zoekfunctie toe aan mijn app.", "Claude bouwt mee en laat jou het belangrijkste stuk schrijven, met uitleg.")],
    ["Voor de uitlegvariant: `/plugin install explanatory-output-style@claude-plugins-official`."]),
   ("Have Claude explain what it does (Explanatory) or let you write pieces of code yourself to learn from (Learning).",
    "Two plugins from Anthropic that change how Claude answers. **learning-output-style** asks you to write a bit of code yourself at key moments, so you learn instead of just watching. **explanatory-output-style** adds explanations about why Claude makes certain choices and which patterns are in your codebase.",
    ["You want to learn to code while building with Claude.", "You want to understand why Claude does something a certain way."],
    [("(after installing) Add a search feature to my app.", "Claude builds with you and lets you write the key part, with explanations.")],
    ["For the explanatory variant: `/plugin install explanatory-output-style@claude-plugins-official`."]))
mp("session-report", "session-report", "Session Report", "ontwikkeling", "chart-pie", "Anthropic", "",
   ("Maakt een interactief HTML-rapport van je Claude Code-gebruik: tokens, cache, subagents, skills en de duurste prompts.",
    "Session Report leest je lokale Claude Code-transcripten en maakt er een verkenbaar HTML-rapport van: hoeveel tokens je gebruikte, hoe goed de cache werkte, welke subagents en skills draaiden en welke prompts het meest kostten.",
    ["Je wilt weten waar je gebruik naartoe gaat.", "Je wilt je prompts efficiënter maken."],
    [("/session-report", "Een HTML-rapport over je recente sessies.")], []),
   ("Creates an interactive HTML report of your Claude Code usage: tokens, cache, subagents, skills and the most expensive prompts.",
    "Session Report reads your local Claude Code transcripts and turns them into an explorable HTML report: how many tokens you used, how well the cache worked, which subagents and skills ran and which prompts cost the most.",
    ["You want to know where your usage goes.", "You want to make your prompts more efficient."],
    [("/session-report", "An HTML report about your recent sessions.")], []))

# ───────── CLOUD / DATA ─────────
mp("firebase", "firebase", "Firebase", "cloud", "fire", "Google", "je hebt een Firebase-project nodig",
   ("Beheer Firestore, Authentication, Cloud Functions, Hosting en Storage vanuit Claude.",
    "De Firebase-plugin geeft Claude toegang tot je Firebase-backend: Firestore-databases, authenticatie, cloud functions, hosting en opslag. Handig voor apps die Firebase als backend gebruiken, zoals veel iOS-apps.",
    ["Je app gebruikt Firebase."],
    [("Maak een Firestore-regel zodat gebruikers alleen hun eigen meldingen kunnen lezen.", "Firestore security rules plus uitleg.")], []),
   ("Manage Firestore, Authentication, Cloud Functions, Hosting and Storage from Claude.",
    "The Firebase plugin gives Claude access to your Firebase backend: Firestore databases, authentication, cloud functions, hosting and storage. Handy for apps that use Firebase as their backend, like many iOS apps.",
    ["Your app uses Firebase."],
    [("Write a Firestore rule so users can only read their own notifications.", "Firestore security rules plus explanation.")], []))
mp("mongodb", "mongodb", "MongoDB", "cloud", "leaf", "MongoDB", "",
   ("Officiële MongoDB-plugin: verbinden, data verkennen, query's optimaliseren en betrouwbare code genereren.",
    "De officiële MongoDB-plugin (MCP-server plus skills) laat Claude verbinden met je databases, data verkennen, collecties beheren, query's optimaliseren en code schrijven volgens de best practices.",
    ["Je gebruikt MongoDB of MongoDB Atlas."],
    [("Waarom is deze query traag? Stel een index voor.", "Een analyse en een passende index.")], []),
   ("Official MongoDB plugin: connect, explore data, optimise queries and generate reliable code.",
    "The official MongoDB plugin (MCP server plus skills) lets Claude connect to your databases, explore data, manage collections, optimise queries and write code following best practices.",
    ["You use MongoDB or MongoDB Atlas."],
    [("Why is this query slow? Suggest an index.", "An analysis and a fitting index.")], []))
mp("prisma", "prisma", "Prisma", "cloud", "database", "Prisma", "",
   ("Postgres-databases beheren met Prisma: schema-migraties, SQL-query's en Prisma Postgres aanmaken.",
    "Met de Prisma-plugin maakt Claude Prisma Postgres-databases aan, voert schema-migraties uit, draait SQL-query's en beheert connection strings, rechtstreeks vanuit je ontwikkelomgeving.",
    ["Je gebruikt Prisma als ORM."],
    [("Voeg een veld 'gelezen' toe aan Melding en maak de migratie.", "Een bijgewerkt schema en een migratie.")], []),
   ("Manage Postgres databases with Prisma: schema migrations, SQL queries and provisioning Prisma Postgres.",
    "With the Prisma plugin Claude provisions Prisma Postgres databases, runs schema migrations, executes SQL queries and manages connection strings, straight from your development environment.",
    ["You use Prisma as your ORM."],
    [("Add a 'read' field to Notification and create the migration.", "An updated schema and a migration.")], []))
mp("vercel-deploy", "vercel", "Vercel (deployen)", "cloud", "rocket", "Vercel", "je hebt een Vercel-account nodig",
   ("Deployments beheren, buildstatus en logs bekijken en domeinen instellen op Vercel.",
    "De Vercel-plugin laat Claude je frontend-infrastructuur besturen: deployments beheren, buildstatus en logs bekijken en domeinen configureren. Combineer met de [Vercel Agent Skills](../ontwikkeling/vercel-agent-skills.md) voor de best practices.",
    ["Je host je website of app op Vercel."],
    [("Waarom faalde de laatste deployment? Laat de buildlog zien.", "De fout uit de log en een oplossing.")], []),
   ("Manage deployments, check build status and logs and configure domains on Vercel.",
    "The Vercel plugin lets Claude control your frontend infrastructure: manage deployments, check build status and logs and configure domains. Combine with the [Vercel Agent Skills](../ontwikkeling/vercel-agent-skills.md) for best practices.",
    ["You host your website or app on Vercel."],
    [("Why did the last deployment fail? Show me the build log.", "The error from the log and a fix.")], []))
mp("netlify", "netlify-skills", "Netlify", "cloud", "cloud-arrow-up", "Netlify", "je hebt een Netlify-account nodig",
   ("Netlify-skills: functions, edge functions, blobs, database, formulieren, caching en deployen.",
    "Skills voor het hele Netlify-platform: (edge) functions, blobs, database, image CDN, formulieren, configuratie, de CLI, frameworks, caching, de AI-gateway en deployen.",
    ["Je host op Netlify."],
    [("Voeg een contactformulier toe met Netlify Forms en een bedankpagina.", "Een werkend formulier zonder eigen backend.")], []),
   ("Netlify skills: functions, edge functions, blobs, database, forms, caching and deployment.",
    "Skills for the whole Netlify platform: (edge) functions, blobs, database, image CDN, forms, configuration, the CLI, frameworks, caching, the AI gateway and deployment.",
    ["You host on Netlify."],
    [("Add a contact form with Netlify Forms and a thank-you page.", "A working form without your own backend.")], []))
mp("resend", "resend", "Resend", "cloud", "envelope", "Resend", "je hebt een account bij Resend nodig",
   ("E-mail versturen en ontvangen met Resend: API, agent-inbox, React Email en goede bezorgbaarheid.",
    "Skills van Resend voor e-mail in je app: de e-mail-API, een inbox voor agents, de CLI, React Email-componenten en best practices voor bezorgbaarheid (zodat je mail niet in spam belandt). Inclusief de Resend MCP-server.",
    ["Je app moet e-mails versturen, zoals een welkomstmail of wachtwoordreset."],
    [("Maak een welkomstmail met React Email en verstuur hem via Resend na registratie.", "Een e-mailtemplate en de verzendcode.")], []),
   ("Send and receive email with Resend: API, agent inbox, React Email and good deliverability.",
    "Skills from Resend for email in your app: the email API, an inbox for agents, the CLI, React Email components and deliverability best practices (so your mail doesn't land in spam). Includes the Resend MCP server.",
    ["Your app needs to send emails, like a welcome mail or password reset."],
    [("Create a welcome email with React Email and send it via Resend after sign-up.", "An email template and the sending code.")], []))
mp("twilio", "twilio-developer-kit", "Twilio", "cloud", "comment-sms", "Twilio", "je hebt een Twilio-account nodig",
   ("Kennis voor sms, spraak, WhatsApp, Verify, SendGrid en 30+ andere Twilio-producten.",
    "Twilio Skills vertellen Claude welke API's je gebruikt, in welke volgorde en wat je moet vermijden. Ze dekken sms, spraak, WhatsApp, Verify (verificatiecodes), SendGrid, compliance en meer dan dertig andere producten.",
    ["Je wilt sms- of WhatsApp-meldingen of tweestapsverificatie in je app."],
    [("Voeg tweestapsverificatie via sms toe met Twilio Verify.", "Werkende verificatiecode-flow.")], []),
   ("Knowledge for SMS, voice, WhatsApp, Verify, SendGrid and 30+ other Twilio products.",
    "Twilio Skills tell Claude which APIs to use, in what order and what to avoid. They cover SMS, voice, WhatsApp, Verify (verification codes), SendGrid, compliance and more than thirty other products.",
    ["You want SMS or WhatsApp notifications or two-factor authentication in your app."],
    [("Add two-factor authentication via SMS with Twilio Verify.", "A working verification-code flow.")], []))
mp("posthog", "posthog", "PostHog", "cloud", "chart-simple", "PostHog", "je hebt een PostHog-account nodig",
   ("Analytics, feature flags, experimenten en error tracking van PostHog vanuit Claude.",
    "Met de PostHog-plugin bekijkt Claude je productanalytics, beheert feature flags en experimenten, volgt fouten en haalt inzichten op, zonder dat je het dashboard hoeft te openen.",
    ["Je meet het gebruik van je app met PostHog."],
    [("Hoeveel gebruikers hebben de nieuwe onboarding afgerond deze week?", "Het aantal plus de trend.")], []),
   ("PostHog analytics, feature flags, experiments and error tracking from Claude.",
    "With the PostHog plugin Claude looks at your product analytics, manages feature flags and experiments, tracks errors and pulls insights, without you opening the dashboard.",
    ["You measure your app's usage with PostHog."],
    [("How many users completed the new onboarding this week?", "The number plus the trend.")], []))
mp("shopify", "shopify-ai-toolkit", "Shopify AI Toolkit", "cloud", "shopify", "Shopify", "je hebt een Shopify-winkel of partneraccount nodig",
   ("18 skills om op Shopify te bouwen: documentatie, API-schema's, GraphQL/Liquid-validatie, Hydrogen en Polaris.",
    "De AI Toolkit van Shopify bevat 18 ontwikkelskills: documentatie doorzoeken, API-schema's, GraphQL- en Liquid-code valideren, Hydrogen-storefronts, Polaris UI-extensies en winkelbeheer.",
    ["Je bouwt een Shopify-thema, -app of -winkel."],
    [("Pas het Liquid-template aan zodat de levertijd onder de prijs staat.", "Gevalideerde Liquid-code.")], []),
   ("18 skills for building on Shopify: documentation, API schemas, GraphQL/Liquid validation, Hydrogen and Polaris.",
    "Shopify's AI Toolkit contains 18 development skills: documentation search, API schemas, validating GraphQL and Liquid code, Hydrogen storefronts, Polaris UI extensions and store management.",
    ["You're building a Shopify theme, app or store."],
    [("Change the Liquid template so the delivery time shows below the price.", "Validated Liquid code.")], []))
mp("wix", "wix", "Wix", "cloud", "wix", "Wix", "je hebt een Wix-account nodig",
   ("Wix-sites en -apps bouwen, beheren en publiceren, met het Wix Design System en een MCP-server.",
    "Skills om Wix-sites en -apps te bouwen: dashboard-extensies, backend-API's, site-widgets en service-plugins met het Wix Design System, plus een MCP-server voor sitebeheer.",
    ["Je website draait op Wix."],
    [("Voeg een widget met de komende activiteiten toe aan mijn Wix-site.", "Een werkende site-widget.")], []),
   ("Build, manage and publish Wix sites and apps, with the Wix Design System and an MCP server.",
    "Skills for building Wix sites and apps: dashboard extensions, backend APIs, site widgets and service plugins with the Wix Design System, plus an MCP server for site management.",
    ["Your website runs on Wix."],
    [("Add a widget with upcoming events to my Wix site.", "A working site widget.")], []))
mp("wordpress", "build-with-wordpress", "Build with WordPress", "cloud", "wordpress", "WordPress", "",
   ("Productieklare WordPress-sites en -apps: thema's, plugins, webshops en deployen.",
    "Alles om met WordPress te bouwen: van thema's en plugins tot WooCommerce-webshops en het live zetten van je site.",
    ["Je website draait op WordPress."],
    [("Maak een eenvoudige WordPress-plugin die een melding bovenaan de site toont.", "Een installeerbare plugin.")], []),
   ("Production-grade WordPress sites and apps: themes, plugins, commerce and deployment.",
    "Everything for building with WordPress: from themes and plugins to WooCommerce shops and putting your site live.",
    ["Your website runs on WordPress."],
    [("Create a simple WordPress plugin that shows a notice at the top of the site.", "An installable plugin.")], []))

# ───────── MOBIEL ─────────
mp("revenuecat", "revenuecat", "RevenueCat", "mobiel", "cart-shopping", "RevenueCat", "je hebt een RevenueCat-account nodig",
   ("In-app aankopen en abonnementen instellen: producten, entitlements en offerings in RevenueCat.",
    "Met de RevenueCat-plugin configureert Claude je in-app-aankopen: projecten, apps, producten, entitlements en offerings, zonder dat je het RevenueCat-dashboard hoeft te openen. Ideaal voor iOS- en Android-apps met abonnementen.",
    ["Je wilt een abonnement of eenmalige aankoop in je app."],
    [("Maak een offering 'Pro' met een maand- en jaarabonnement.", "Een kant-en-klare offering in RevenueCat.")], []),
   ("Set up in-app purchases and subscriptions: products, entitlements and offerings in RevenueCat.",
    "With the RevenueCat plugin Claude configures your in-app purchases: projects, apps, products, entitlements and offerings, without opening the RevenueCat dashboard. Ideal for iOS and Android apps with subscriptions.",
    ["You want a subscription or one-time purchase in your app."],
    [("Create a 'Pro' offering with a monthly and a yearly subscription.", "A ready-made offering in RevenueCat.")], []))
mp("mapbox", "mapbox", "Mapbox", "mobiel", "map-location-dot", "Mapbox", "je hebt een Mapbox-account nodig",
   ("Locatie-apps bouwen: geo-tools, kaartstijlen en patronen voor web, iOS en Android.",
    "Skills en MCP-servers van Mapbox voor locatiebewuste apps: geografische tools, stijlbeheer en patronen voor web, iOS, Android en AI-agentframeworks.",
    ["Je app toont kaarten of werkt met locaties."],
    [("Toon alle meldingen van vandaag als markers op een Mapbox-kaart in mijn iOS-app.", "SwiftUI-code met een Mapbox-kaart en markers.")], []),
   ("Build location-aware apps: geospatial tools, map styles and patterns for web, iOS and Android.",
    "Skills and MCP servers from Mapbox for location-aware apps: geospatial tools, style management and patterns for web, iOS, Android and AI agent frameworks.",
    ["Your app shows maps or works with locations."],
    [("Show today's alerts as markers on a Mapbox map in my iOS app.", "SwiftUI code with a Mapbox map and markers.")], []))

# ───────── KENNIS / ONDERZOEK ─────────
mp("remember", "remember", "Remember", "kennis", "brain", "Community", "",
   ("Doorlopend geheugen voor Claude Code: gesprekken worden samengevat in dagelijkse logboeken.",
    "Remember haalt de kern uit je gesprekken, vat ze samen en comprimeert ze tot logboeken per dag. Zo weet Claude morgen nog wat je gisteren deed.",
    ["Je werkt elke dag aan hetzelfde project."],
    [("Waar waren we gisteren gebleven?", "Een samenvatting van het werk van gisteren.")], []),
   ("Continuous memory for Claude Code: conversations are summarised into daily logs.",
    "Remember extracts the essence of your conversations, summarises them and compresses them into daily logs. That way Claude still knows tomorrow what you did yesterday.",
    ["You work on the same project every day."],
    [("Where did we leave off yesterday?", "A summary of yesterday's work.")], []))
mp("exa", "exa", "Exa Search", "productiviteit", "magnifying-glass", "Exa", "je hebt een API-sleutel van Exa nodig",
   ("AI-webzoeken en diepgaand onderzoek: mensen, bedrijven, wetenschappelijke artikelen en meer.",
    "Exa geeft Claude krachtige webzoektools en onderzoeksskills: grondig zoeken op het web, mensen en bedrijven onderzoeken, wetenschappelijke papers vinden en inhoud van pagina's ophalen.",
    ["Je doet regelmatig grondig onderzoek."],
    [("Zoek recente wetenschappelijke artikelen over buurtpreventie en vat ze samen.", "Een overzicht met bronnen.")], []),
   ("AI web search and deep research: people, companies, academic papers and more.",
    "Exa gives Claude powerful web search tools and research skills: thorough web search, researching people and companies, finding academic papers and extracting page content.",
    ["You regularly do in-depth research."],
    [("Find recent academic papers on neighbourhood watch and summarise them.", "An overview with sources.")], []))
mp("tavily", "tavily", "Tavily", "productiviteit", "globe", "Tavily", "je hebt een API-sleutel van Tavily nodig",
   ("Realtime webdata voor je AI-apps: zoeken, uitlezen, crawlen en onderzoek via de Tavily-API's.",
    "Met de Tavily-plugin bouwt Claude AI-toepassingen die actuele webdata gebruiken via de zoek-, extract-, crawl- en research-API's van Tavily.",
    ["Je bouwt een app die actuele informatie van het web nodig heeft."],
    [("Bouw een functie die elke ochtend het nieuws over mijn gemeente samenvat.", "Code die Tavily gebruikt om nieuws op te halen.")], []),
   ("Real-time web data for your AI apps: search, extract, crawl and research via Tavily's APIs.",
    "With the Tavily plugin Claude builds AI applications that use current web data through Tavily's search, extract, crawl and research APIs.",
    ["You're building an app that needs current information from the web."],
    [("Build a feature that summarises the news about my town every morning.", "Code that uses Tavily to fetch the news.")], []))

# ───────── LOSSE ROL-PLUGINS VAN ANTHROPIC ─────────
KW = [
 ("sales", "Sales", "chart-line", "Sales",
  "Gesprekken voorbereiden, samenvatten en opvolgen, accounts onderzoeken, je pipeline bewaken en outreach schrijven.",
  "Prep calls, summarise and follow up, research accounts, watch your pipeline and write outreach.",
  "call-prep, call-summary, account-research, daily-briefing, deal-review, draft-outreach, forecast, handle-objection, pipeline-review, win-loss-review"),
 ("customer-support", "Klantenservice", "headset", "Customer support",
  "Tickets triëren, antwoorden opstellen, escalaties voorbereiden en opgeloste vragen omzetten in kennisbankartikelen.",
  "Triage tickets, draft replies, prepare escalations and turn resolved questions into knowledge base articles.",
  "ticket-triage, draft-response, customer-escalation, customer-research, kb-article"),
 ("product-management", "Productmanagement", "diagram-project", "Product management",
  "Feature-specs schrijven, roadmaps plannen, gebruikersonderzoek samenvatten en stakeholders op de hoogte houden.",
  "Write feature specs, plan roadmaps, synthesise user research and keep stakeholders informed.",
  "write-spec, roadmap-update, sprint-planning, synthesize-research, stakeholder-update, competitive-brief, metrics-review, product-brainstorming"),
 ("marketing", "Marketing", "bullhorn", "Marketing",
  "Content maken, campagnes plannen, je merkstem bewaken, concurrenten volgen en resultaten rapporteren.",
  "Create content, plan campaigns, keep your brand voice consistent, track competitors and report results.",
  "content-creation, draft-content, campaign-plan, email-sequence, brand-review, competitive-brief, seo-audit, performance-report"),
 ("legal", "Juridisch", "scale-balanced", "Legal",
  "Contracten reviewen, NDA's triëren, compliance controleren en juridische risico's inschatten.",
  "Review contracts, triage NDAs, check compliance and assess legal risk.",
  "review-contract, triage-nda, compliance-check, legal-risk-assessment, legal-response, meeting-briefing, vendor-check, brief, signature-request"),
 ("finance", "Finance", "coins", "Finance",
  "Journaalposten, afstemmingen, jaarrekeningen, variantieanalyse en de maandafsluiting.",
  "Journal entries, reconciliations, financial statements, variance analysis and month-end close.",
  "journal-entry, reconciliation, financial-statements, variance-analysis, close-management, audit-support, sox-testing"),
 ("data", "Data", "database", "Data",
  "SQL schrijven, datasets verkennen, statistische analyses, visualisaties en dashboards.",
  "Write SQL, explore datasets, run statistical analyses and build visualisations and dashboards.",
  "write-query, sql-queries, explore-data, statistical-analysis, create-viz, build-dashboard, validate-data, analyze"),
 ("design", "Design", "pen-ruler", "Design",
  "Design-kritiek, toegankelijkheidsaudits, designsystemen, UX-teksten, onderzoek en developer-handoff.",
  "Design critique, accessibility audits, design systems, UX copy, research and developer handoff.",
  "design-critique, accessibility-review, design-system, ux-copy, design-handoff, user-research, research-synthesis"),
 ("engineering", "Engineering", "gears", "Engineering",
  "Standups, code reviews, architectuurbeslissingen, incidentrespons en technische documentatie.",
  "Standups, code reviews, architecture decisions, incident response and technical documentation.",
  "standup, code-review, architecture, system-design, debug, incident-response, deploy-checklist, documentation, tech-debt, testing-strategy"),
 ("human-resources", "HR", "user-tie", "HR",
  "Werving, onboarding, beoordelingsgesprekken, salarisanalyse en beleidsvragen.",
  "Recruiting, onboarding, performance reviews, compensation analysis and policy questions.",
  "recruiting-pipeline, interview-prep, draft-offer, onboarding, performance-review, comp-analysis, org-planning, policy-lookup, people-report"),
 ("operations", "Operations", "clipboard-list", "Operations",
  "Leveranciersbeheer, procesdocumentatie, wijzigingsbeheer, capaciteitsplanning en compliance.",
  "Vendor management, process documentation, change management, capacity planning and compliance.",
  "process-doc, runbook, change-request, capacity-plan, risk-assessment, vendor-review, status-report, compliance-tracking, process-optimization"),
 ("productivity", "Productiviteit", "list-check", "Productivity",
  "Taken beheren, je dag plannen en een geheugen opbouwen van belangrijke werkcontext, gekoppeld aan agenda, mail en chat.",
  "Manage tasks, plan your day and build up a memory of important work context, connected to calendar, email and chat.",
  "start, task-management, memory-management, update"),
 ("enterprise-search", "Zoeken in de organisatie", "magnifying-glass", "Enterprise search",
  "Eén zoekvraag over al je bedrijfstools: mail, chat, documenten en wiki's.",
  "One search across all your company tools: email, chat, documents and wikis.",
  "search, search-strategy, digest, knowledge-synthesis, source-management"),
 ("small-business", "Mkb / kleine ondernemers", "store", "Small business",
  "Kant-en-klare workflows om je bedrijf te runnen: facturen najagen, cashflow, social content, offertes, belasting en meer. Bij geld of klanten keur jij elke stap goed.",
  "Ready-made workflows to run your business: chasing invoices, cash flow, social content, proposals, taxes and more. You approve every step that touches money or customers.",
  "monday-brief, invoice-chase, cash-flow-snapshot, proposal-builder, social-content-engine, lead-finder, tax-prep, review-reputation, payroll-prep, close-month"),
 ("bio-research", "Bio-onderzoek", "dna", "Bio research",
  "Koppelingen met preklinische onderzoekstools en databases: literatuur, genomics en het prioriteren van targets.",
  "Connections to preclinical research tools and databases: literature, genomics and target prioritisation.",
  "start, scientific-problem-selection, single-cell-rna-qc, scvi-tools, nextflow-development, instrument-data-to-allotrope"),
]
for plug, nl_name, icon, en_name, nl_t, en_t, skills in KW:
    slug = f"rol-{plug}"
    first = skills.split(",")[0].strip()
    ex_nl = {"sales": ("/sales:call-prep Gesprek met een nieuwe klant morgen om 10:00", "Een voorbereiding met achtergrond, vragen en doelen."),
             "small-business": ("/small-business:invoice-chase", "Openstaande facturen met conceptherinneringen.")}.get(plug, (f"/{plug}:{first}", "De bijbehorende workflow, stap voor stap."))
    ex_en = {"sales": ("/sales:call-prep Meeting with a new customer tomorrow at 10:00", "A preparation with background, questions and goals."),
             "small-business": ("/small-business:invoice-chase", "Outstanding invoices with draft reminders.")}.get(plug, (f"/{plug}:{first}", "The matching workflow, step by step."))
    inst_nl = tabs(tab("Claude-app", "Installeer de plugin in de Claude-desktopapp via [claude.com/plugins](https://claude.com/plugins/). Skills gaan vanzelf aan en de commando's verschijnen in je sessie."),
                   tab("Claude Code", f"```bash\nclaude plugin marketplace add anthropics/knowledge-work-plugins\nclaude plugin install {plug}@knowledge-work-plugins\n```"))
    inst_en = tabs(tab("Claude app", "Install the plugin in the Claude desktop app via [claude.com/plugins](https://claude.com/plugins/). Skills switch on automatically and the commands appear in your session."),
                   tab("Claude Code", f"```bash\nclaude plugin marketplace add anthropics/knowledge-work-plugins\nclaude plugin install {plug}@knowledge-work-plugins\n```"))
    S3.append(dict(slug=slug, name=f"{nl_name} (rol-plugin)", cat="zakelijk", icon=icon, tagline=nl_t,
                   wat=f"De rol-plugin **{plug}** van Anthropic bundelt skills, commando's en koppelingen voor deze functie. {nl_t} Je roept de onderdelen aan als `/{plug}:<skill>`.\n\n**Skills in deze plugin:** {', '.join('`'+x.strip()+'`' for x in skills.split(','))}.\n\nZie ook het [overzicht van alle rol-plugins](knowledge-work-plugins.md).",
                   wanneer=["Je werkt in deze rol en wilt vaste, goede workflows.", "Je wilt de plugin aanpassen met je eigen tools en werkwijze."],
                   voorbeelden=[ex_nl], tips=["Pas de plugin aan je eigen tools aan via het bestand `.mcp.json` in de plugin."],
                   maker="Anthropic (officieel)", werkt="Claude-app (desktop), Claude Code", prijs="Gratis (open source)",
                   bron=f"https://github.com/anthropics/knowledge-work-plugins/tree/main/{plug}", install=inst_nl))
    E[slug] = dict(name=f"{en_name} (role plugin)", t=en_t,
                   w=f"Anthropic's **{plug}** role plugin bundles skills, commands and connectors for this job function. {en_t} You call its parts as `/{plug}:<skill>`.\n\n**Skills in this plugin:** {', '.join('`'+x.strip()+'`' for x in skills.split(','))}.\n\nSee also the [overview of all role plugins](knowledge-work-plugins.md).",
                   wa=["You work in or with this role and want solid, consistent workflows.", "You want to adapt the plugin to your own tools and way of working."],
                   v=[ex_en], tips=["Adapt the plugin to your own tools through the plugin's `.mcp.json` file."], install=inst_en)
