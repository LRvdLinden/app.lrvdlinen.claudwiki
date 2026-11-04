from install import *

NEWCATS = [
    ("mobiel", "Apps & mobiel", "mobile-screen-button",
     "Skills voor iOS-, SwiftUI- en React Native/Expo-ontwikkelaars: van SwiftUI-best practices tot de iOS Simulator besturen."),
    ("cloud", "Data, cloud & betalen", "cloud",
     "Officiële skills van Supabase, Neon, Cloudflare, AWS, Azure, HashiCorp, Hugging Face, Stripe en Sentry."),
    ("productiviteit", "Productiviteit & tools", "toolbox",
     "Handige alledaagse skills: bestanden en facturen ordenen, Google Workspace, NotebookLM, leren van artikelen en video's, en duizend apps koppelen."),
    ("media", "Audio, beeld & visuals", "wave-square",
     "Spraak en muziek met ElevenLabs, afbeeldingen genereren en verbeteren, diagrammen en datavisualisaties."),
]

S2 = []
def add(**k): S2.append(k)

def mk(marketplace, plugin, n=None, nx=None, extra=""):
    t = [cc_market(marketplace, plugin, extra)]
    if nx: t.append(npx(nx))
    return tabs(*t)

# ───────────── MOBIEL ─────────────
add(slug="swiftui-expert", name="SwiftUI Expert (Antoine van der Lee)", cat="mobiel", icon="swift",
    tagline="SwiftUI-best practices: state management, view-opbouw, performance, nieuwe SDK-wijzigingen en Liquid Glass.",
    maker="Antoine van der Lee / SwiftLee (community, Nederlands)", werkt="Claude Code (+ Codex, Cursor en andere agents)", prijs="Gratis (open source)",
    bron="https://github.com/AvdLee/SwiftUI-Agent-Skill",
    wat="Antoine van der Lee (SwiftLee) is een bekende Nederlandse iOS-ontwikkelaar. Deze skill bundelt praktische SwiftUI-kennis in compacte naslag voor agents en code reviews: hoe je state goed beheert, views opbouwt, performance bewaakt, de nieuwste SDK-wijzigingen toepast en **Liquid Glass** adopteert. Een tweede skill, `update-swiftui-apis`, helpt verouderde API's te vervangen.",
    wanneer=["Je bouwt een iOS-, iPadOS- of macOS-app in SwiftUI.", "Je wilt dat Claude moderne SwiftUI schrijft in plaats van verouderde patronen."],
    voorbeelden=[("Review deze SwiftUI-view op state management en performance.", "Concrete verbeteringen, zoals @Observable in plaats van ObservableObject."),
                 ("Pas het instellingenscherm aan naar Liquid Glass.", "Code die de nieuwe designtaal correct gebruikt.")],
    install=tabs(cc_market("AvdLee/SwiftUI-Agent-Skill", "swiftui-expert@swiftui-expert-skill"),
                 npx("npx skills@latest add https://github.com/avdlee/swiftui-agent-skill --skill swiftui-expert-skill")),
    tips=["Van dezelfde maker: [Swift Concurrency](swift-concurrency.md) en [Xcode Build Optimization](xcode-build-optimization.md)."])

add(slug="swiftui-pro", name="SwiftUI Pro (Paul Hudson)", cat="mobiel", icon="mobile-screen",
    tagline="Agent-skill van Hacking with Swift: moderne SwiftUI-code voor iOS 26+ en Swift 6.",
    maker="Paul Hudson / twostraws (community)", werkt="Claude Code (+ Codex, Gemini)", prijs="Gratis (open source)",
    bron="https://github.com/twostraws/SwiftUI-Agent-Skill",
    wat="Paul Hudson, de maker van Hacking with Swift, heeft zijn SwiftUI-kennis in een skill gegoten. Hij is gericht op iOS 26 en nieuwer en recente Swift-versies, en zorgt dat Claude actuele API's en idiomen gebruikt en klassieke valkuilen vermijdt.",
    wanneer=["Je bouwt SwiftUI-apps voor de nieuwste iOS-versies."],
    voorbeelden=[("Bouw een lijst met zoeken, swipe-acties en pull-to-refresh in modern SwiftUI.", "Moderne, compacte SwiftUI-code.")],
    install=tabs(cc_market("twostraws/SwiftUI-Agent-Skill", "swiftui-pro@swiftui-agent-skill"),
                 npx("npx skills add https://github.com/twostraws/swiftui-agent-skill --skill swiftui-pro")),
    tips=["Ook van Paul Hudson: [Swift Testing Pro](swift-testing-pro.md)."])

add(slug="swift-concurrency", name="Swift Concurrency", cat="mobiel", icon="arrows-split-up-and-left",
    tagline="Helpt Claude met async/await, actors, Sendable en de migratie naar Swift 6-strict concurrency.",
    maker="Antoine van der Lee (community, Nederlands)", werkt="Claude Code (+ andere agents)", prijs="Gratis (open source)",
    bron="https://github.com/AvdLee/Swift-Concurrency-Agent-Skill",
    wat="Swift Concurrency is lastig, en AI-agents maken er vaak fouten in. Deze skill geeft Claude de juiste kennis over async/await, actors, `@MainActor`, `Sendable`, tasks en het oplossen van strict-concurrency-waarschuwingen in Swift 6.",
    wanneer=["Je krijgt Swift 6-concurrencyfouten.", "Je wilt oude completion handlers omzetten naar async/await."],
    voorbeelden=[("Los alle Sendable-waarschuwingen in deze module op zonder @unchecked.", "Een correcte, veilige oplossing per waarschuwing.")],
    install=tabs(cc_market("AvdLee/Swift-Concurrency-Agent-Skill", "swift-concurrency@swift-concurrency-agent-skill"),
                 npx("npx skills@latest add https://github.com/avdlee/swift-concurrency-agent-skill --skill swift-concurrency")),
    tips=[])

add(slug="xcode-build-optimization", name="Xcode Build Optimization", cat="mobiel", icon="gauge-high",
    tagline="Zes skills die je Xcode-builds meten en versnellen: clean, incrementeel, compile-hotspots en SPM.",
    maker="Antoine van der Lee (community, Nederlands)", werkt="Claude Code (+ andere agents)", prijs="Gratis (open source)",
    bron="https://github.com/AvdLee/Xcode-Build-Optimization-Agent-Skill",
    wat="Een orchestrator-skill met vijf specialisten: benchmark, compilatie-analyse, projectinstellingen, Swift Package Manager-analyse en een fixer. Claude meet eerst hoe lang je builds duren, zoekt de knelpunten en stelt gerichte verbeteringen voor.",
    wanneer=["Je builds zijn traag en je wilt weten waarom."],
    voorbeelden=[("Benchmark mijn project en maak de incrementele build sneller.", "Metingen vooraf en achteraf, met de aanpassingen ertussen.")],
    install=tabs(cc_market("AvdLee/Xcode-Build-Optimization-Agent-Skill", "xcode-build-skills@xcode-build-skills"),
                 npx("npx skills add https://github.com/avdlee/xcode-build-optimization-agent-skill")),
    tips=["Installeer alle zes de skills: de orchestrator heeft de specialisten nodig."])

add(slug="swift-testing-pro", name="Swift Testing Pro", cat="mobiel", icon="flask-vial",
    tagline="Goede tests schrijven met het nieuwe Swift Testing-framework (@Test, #expect).",
    maker="Paul Hudson / twostraws (community)", werkt="Claude Code (+ Codex, Gemini)", prijs="Gratis (open source)",
    bron="https://github.com/twostraws/Swift-Testing-Agent-Skill",
    wat="Leert Claude het moderne Swift Testing-framework: `@Test`, `#expect`, geparametriseerde tests, traits en het omzetten van XCTest naar Swift Testing.",
    wanneer=["Je wilt tests toevoegen aan je Swift-app.", "Je migreert van XCTest."],
    voorbeelden=[("Schrijf Swift Testing-tests voor deze DateFormatter-helper, inclusief randgevallen.", "Geparametriseerde tests met duidelijke namen.")],
    install=tabs(cc_market("twostraws/Swift-Testing-Agent-Skill", "swift-testing-pro@swift-testing-agent-skill"),
                 npx("npx skills add https://github.com/twostraws/swift-testing-agent-skill --skill swift-testing-pro")),
    tips=[])

add(slug="ios-simulator", name="iOS Simulator Skill", cat="mobiel", icon="tablet-screen-button",
    tagline="Laat Claude je iOS-app bouwen, starten en testen in de Simulator, met 30 hulpscripts.",
    maker="Conor Luddy (community)", werkt="Claude Code op macOS met Xcode", prijs="Gratis (open source)",
    bron="https://github.com/conorluddy/ios-simulator-skill",
    wat="Met deze skill kan Claude de iOS Simulator bedienen: apps bouwen en installeren, tikken en navigeren via de toegankelijkheidsboom, screenshots maken, logs lezen en problemen debuggen. De 30 scripts zijn geoptimaliseerd voor zowel mensen als agents.",
    wanneer=["Je wilt dat Claude zelf controleert of zijn wijziging in de app werkt."],
    voorbeelden=[("Bouw de app, open hem in de iPhone-simulator en test of het onboardingscherm goed werkt.", "Een testverslag met screenshots.")],
    install=tabs(cc_market("conorluddy/ios-simulator-skill", "ios-simulator-skill@conorluddy")),
    tips=["Liever een MCP-server? De maker heeft ook XC-MCP."])

add(slug="expo", name="Expo Skills", cat="mobiel", icon="react",
    tagline="Officiële Expo-skills: React Native-apps bouwen, Expo Router, EAS Build/Update en publiceren in de stores.",
    maker="Expo (officieel van de makers)", werkt="Claude Code (+ Codex, Cursor en meer)", prijs="Gratis",
    bron="https://github.com/expo/skills",
    wat="Ruim twintig skills van Expo zelf: projectstructuur, Expo Router, native UI en animaties, data ophalen, modules maken, upgraden, web-naar-native, App Clips en de EAS-diensten (builds, updates, hosting, workflows en publicatie in de App Store en Play Store).",
    wanneer=["Je bouwt een cross-platform app met React Native en Expo."],
    voorbeelden=[("Upgrade dit Expo-project naar de nieuwste SDK.", "Een begeleide upgrade met de juiste stappen."),
                 ("Zet EAS Update op zodat ik fixes zonder nieuwe build kan uitrollen.", "Configuratie en uitleg.")],
    install=tabs(cc_official("expo"), npx("npx skills@latest add expo/skills --skill '*'")),
    tips=[])

# ───────────── CLOUD ─────────────
add(slug="supabase", name="Supabase", cat="cloud", icon="bolt-lightning",
    tagline="Officiële Supabase-skills en Postgres-best practices voor database, auth en storage.",
    maker="Supabase (officieel van de makers)", werkt="Claude Code (+ 18 andere agents)", prijs="Gratis",
    bron="https://github.com/supabase/agent-skills",
    wat="Twee skills: **supabase** (werken met het Supabase-platform: database, auth, storage, edge functions) en **supabase-postgres-best-practices** (goede schema's, indexen, row level security en query's).",
    wanneer=["Je app gebruikt Supabase als backend."],
    voorbeelden=[("Ontwerp een schema voor meldingen met row level security per gebruiker.", "SQL-migraties met RLS-policies.")],
    install=tabs(tab("Claude Code", "```bash\nclaude plugin marketplace add supabase/agent-skills\nclaude plugin install supabase@supabase-agent-skills\nclaude plugin install postgres-best-practices@supabase-agent-skills\n```"),
                 npx("npx skills add supabase/agent-skills")),
    tips=["Staat ook in de officiële marketplace als `supabase`."])

add(slug="neon", name="Neon Postgres", cat="cloud", icon="database",
    tagline="Skills voor Neon serverless Postgres: database, auth, functions, object storage en realtime.",
    maker="Neon (officieel van de makers)", werkt="Claude Code (+ andere agents)", prijs="Gratis",
    bron="https://github.com/neondatabase/agent-skills",
    wat="Neon's eigen skills voor hun serverless Postgres-platform, inclusief branches voor elke feature, Neon Auth, functions, object storage, realtime en de AI-gateway.",
    wanneer=["Je gebruikt (of overweegt) Neon als database."],
    voorbeelden=[("Maak een Neon-branch voor deze feature en draai de migratie daarop.", "Een aparte databasebranch om veilig te testen.")],
    install=mk("neondatabase/agent-skills", "neon-postgres@neon", nx="npx skills add neondatabase/agent-skills"),
    tips=[])

add(slug="cloudflare", name="Cloudflare", cat="cloud", icon="cloudflare",
    tagline="Bouwen op Cloudflare: Workers, Durable Objects, Agents SDK, Wrangler, Turnstile en meer.",
    maker="Cloudflare (officieel van de makers)", werkt="Claude Code (+ andere agents)", prijs="Gratis",
    bron="https://github.com/cloudflare/skills",
    wat="Een collectie skills voor het Cloudflare Developer Platform: Workers-best practices, Durable Objects, de Agents SDK, Wrangler, Next.js op Cloudflare, web-performance, Turnstile en de e-maildienst. De plugin installeert ook de Cloudflare MCP-server.",
    wanneer=["Je host je website of API op Cloudflare."],
    voorbeelden=[("Zet deze API om naar een Cloudflare Worker met caching.", "Een Worker plus wrangler-configuratie.")],
    install=mk("cloudflare/skills", "cloudflare@cloudflare", nx="npx skills add https://github.com/cloudflare/skills"),
    tips=[])

add(slug="aws-skills", name="AWS Skills", cat="cloud", icon="aws",
    tagline="AWS-ontwikkeling: CDK, serverless/event-driven architectuur, kostenoptimalisatie en Bedrock AgentCore.",
    maker="zxkane (community)", werkt="Claude Code", prijs="Gratis (open source)",
    bron="https://github.com/zxkane/aws-skills",
    wat="Plugins voor AWS met MCP-koppelingen: CDK-best practices, serverless en event-driven patronen, kostenbeheer, SST en het uitrollen van AI-agents met Bedrock AgentCore. Met de AWS Documentation MCP gebruikt Claude actuele AWS-documentatie.",
    wanneer=["Je bouwt of beheert infrastructuur op AWS."],
    voorbeelden=[("Analyseer mijn AWS-kosten en geef de drie grootste besparingen.", "Een kostenrapport met acties.")],
    install=tabs(tab("Claude Code", "```bash\n/plugin marketplace add zxkane/aws-skills\n/plugin install aws-common@aws-skills\n/plugin install aws-iac@aws-skills\n/plugin install aws-cost-ops@aws-skills\n```\n\nAndere plugins: `serverless-eda`, `aws-agentic-ai`.")),
    tips=["In de officiële marketplace staan ook AWS-plugins van Amazon zelf, zoals `aws-core` en `aws-serverless`. Zie de [catalogus](../../catalogus/README.md)."])

add(slug="microsoft-azure", name="Microsoft Azure Skills", cat="cloud", icon="microsoft",
    tagline="Honderden skills van Microsoft voor Azure-SDK's, AKS, Application Insights en Microsoft AI Foundry.",
    maker="Microsoft (officieel van de makers)", werkt="Claude Code (+ Copilot en andere agents)", prijs="Gratis",
    bron="https://github.com/microsoft/skills",
    wat="Skills, agents, AGENTS.md-sjablonen en MCP-configuraties voor wie met Azure werkt: van Azure SDK's in Python, .NET, Java en TypeScript tot AKS-troubleshooting, kostenoptimalisatie en Microsoft AI Foundry. Er is ook een `deep-wiki`-plugin.",
    wanneer=["Je bouwt op Azure of met Microsoft AI-diensten."],
    voorbeelden=[("Voeg Application Insights toe aan deze Node-app.", "Instrumentatie volgens Microsoft's richtlijnen.")],
    install=mk("microsoft/skills", "azure@skills", nx="npx skills add microsoft/skills"),
    tips=["Installeer niet alles tegelijk: kies de skills voor jouw taal en diensten."])

add(slug="hashicorp", name="HashiCorp Terraform & Packer", cat="cloud", icon="cubes-stacked",
    tagline="Officiële skills voor Terraform (stijlgids, tests, stacks, modules) en Packer-images.",
    maker="HashiCorp (officieel van de makers)", werkt="Claude Code (+ andere agents)", prijs="Gratis",
    bron="https://github.com/hashicorp/agent-skills",
    wat="De makers van Terraform leveren skills voor de Terraform-stijlgids, testen, stacks, policies, importeren van bestaande resources, modules refactoren en zelfs eigen providers bouwen. Voor Packer zijn er skills om AWS-, Azure- en Windows-images te bouwen.",
    wanneer=["Je beheert infrastructuur met Terraform of bouwt machine-images met Packer."],
    voorbeelden=[("Importeer deze bestaande S3-buckets in Terraform.", "Import-blokken en de bijbehorende configuratie.")],
    install=tabs(tab("Claude Code", "```bash\nclaude plugin marketplace add hashicorp/agent-skills\nclaude plugin install terraform@hashicorp\nclaude plugin install packer@hashicorp\n```"),
                 npx("npx skills add hashicorp/agent-skills")),
    tips=["Zie ook de community-variant [Terraform Skill](../ontwikkeling/terraform-skill.md)."])

add(slug="huggingface", name="Hugging Face", cat="cloud", icon="face-smile",
    tagline="AI/ML-taken: datasets, modellen trainen en evalueren, Spaces, Gradio en de Hugging Face Hub.",
    maker="Hugging Face (officieel van de makers)", werkt="Claude Code (+ andere agents)", prijs="Gratis",
    bron="https://github.com/huggingface/skills",
    wat="Skills voor machine learning op de Hugging Face Hub: de `hf`-CLI, datasets, Spaces en Gradio, modellen trainen (TRL, LoRA, vision, sentence-transformers), evaluaties, papers publiceren en lokaal modellen draaien.",
    wanneer=["Je wilt een eigen model finetunen of een demo-Space maken."],
    voorbeelden=[("Maak een Gradio-Space die Nederlandse tekst samenvat.", "Een werkende Space-repo.")],
    install=mk("huggingface/skills", "hf-cli@huggingface/skills"),
    tips=[])

add(slug="stripe", name="Stripe", cat="cloud", icon="stripe",
    tagline="Officiële Stripe-skills en best practices voor betalingen, Connect en upgrades van de API.",
    maker="Stripe (officieel van de makers)", werkt="Claude Code (+ andere agents)", prijs="Gratis",
    bron="https://github.com/stripe/ai",
    wat="Stripe's eigen skills: best practices voor betalingen, Stripe Connect, Stripe Apps, documentatie opzoeken en de API upgraden. Gecombineerd met de Stripe MCP-server kan Claude veilig met je Stripe-account werken.",
    wanneer=["Je wilt betalingen of abonnementen in je app of website."],
    voorbeelden=[("Voeg een maandabonnement toe met Stripe Checkout en een webhook.", "Checkout-integratie plus webhook-handler.")],
    install=tabs(cc_official("stripe"), npx("npx skills add https://docs.stripe.com")),
    tips=["Handmatig geïnstalleerde skills updaten niet vanzelf: `npx skills update -y`."])

add(slug="sentry", name="Sentry Skills", cat="cloud", icon="bug",
    tagline="De skills die Sentry intern gebruikt: bugs vinden, code reviews, commits, PR's en security reviews.",
    maker="Sentry (officieel van de makers)", werkt="Claude Code", prijs="Gratis",
    bron="https://github.com/getsentry/skills",
    wat="Sentry deelt de skills van hun eigen engineers: `find-bugs`, `code-review`, `security-review`, `commit`, `pr-writer`, `iterate-pr`, een GitHub Actions-securityreview, `skill-scanner` (controleert skills op risico's) en meer.",
    wanneer=["Je wilt professionele dev-workflows overnemen.", "Je wilt skills van anderen scannen op risico's."],
    voorbeelden=[("/find-bugs", "Een lijst met waarschijnlijke bugs in je huidige wijzigingen.")],
    install=tabs(tab("Claude Code", "```bash\nclaude plugin marketplace add getsentry/skills\nclaude plugin install sentry-skills@sentry-skills\n```")),
    tips=["Voor foutmonitoring zelf: de plugin `sentry` in de officiële marketplace."])

add(slug="firecrawl", name="Firecrawl", cat="cloud", icon="spider",
    tagline="Het web doorzoeken en lezen voor je agent: zoeken, pagina's scrapen, leads, SEO-audits en diepgaand onderzoek.",
    maker="Firecrawl (officieel van de makers)", werkt="Claude Code (API-sleutel nodig)", prijs="Plugin gratis; Firecrawl-diensten volgens hun prijzen",
    bron="https://github.com/firecrawl/firecrawl-claude-plugin",
    wat="Koppelt Claude aan de zoek- en scrapetools van Firecrawl, met skills voor diepgaand onderzoek, documentatie lezen, leads vinden en verrijken, vacatures, merkidentiteit en SEO-audits.",
    wanneer=["Je wilt grondig webonderzoek met nette, schone pagina-inhoud."],
    voorbeelden=[("Doe diepgaand onderzoek naar buurtpreventie-apps in Nederland en vat het samen.", "Een rapport met bronnen.")],
    install=tabs(cc_market("firecrawl/firecrawl-claude-plugin", "firecrawl@firecrawl")),
    tips=[])

# ───────────── PRODUCTIVITEIT ─────────────
add(slug="connect-apps", name="Connect Apps (Composio)", cat="productiviteit", icon="link",
    tagline="Laat Claude echte acties doen in 1000+ apps: mail versturen, issues maken, berichten posten.",
    maker="Composio (community)", werkt="Claude Code", prijs="Gratis te starten; Composio-account nodig",
    bron="https://github.com/ComposioHQ/awesome-claude-skills/tree/master/connect-apps-plugin",
    wat="Met deze plugin voert Claude acties uit in externe apps zoals Gmail, Slack en GitHub. Composio regelt het inloggen en verbindt met meer dan duizend apps. De repo bevat ook honderden 'automation'-skills per app.",
    wanneer=["Je wilt dat Claude dingen dóét in je apps, niet alleen tekst schrijft."],
    voorbeelden=[("Stuur een samenvatting van deze vergadering naar het team in Slack.", "Een bericht in je Slack-kanaal.")],
    install=tabs(tab("Claude Code", "```bash\ngit clone https://github.com/ComposioHQ/awesome-claude-skills.git\ncd awesome-claude-skills\nclaude --plugin-dir ./connect-apps-plugin\n```\n\nVolg daarna de setup in de README.")),
    tips=["In de Claude-app kun je veel apps ook rechtstreeks koppelen via **Instellingen → Connectors**."])

add(slug="file-organizer", name="File Organizer", cat="productiviteit", icon="folder-tree",
    tagline="Ruimt mappen slim op: duplicaten vinden, betere structuur voorstellen en opruimen automatiseren.",
    maker="ComposioHQ (community)", werkt="Claude Code, Claude-app", prijs="Gratis",
    bron="https://github.com/ComposioHQ/awesome-claude-skills/tree/master/file-organizer",
    wat="Claude bekijkt je mappen, begrijpt wat erin staat, vindt dubbele bestanden, stelt een logischere mappenstructuur voor en voert het opruimen voor je uit.",
    wanneer=["Je Downloads- of documentenmap is een chaos."],
    voorbeelden=[("Ruim mijn map Downloads op: groepeer per soort en zoek duplicaten.", "Een voorstel, en na akkoord een opgeruimde map.")],
    install=tabs(manual("git clone https://github.com/ComposioHQ/awesome-claude-skills.git\ncp -r awesome-claude-skills/file-organizer ~/.claude/skills/"),
                 app_zip("ComposioHQ/awesome-claude-skills", "file-organizer")),
    tips=["Laat Claude eerst een voorstel doen voordat hij iets verplaatst."])

add(slug="invoice-organizer", name="Invoice Organizer", cat="productiviteit", icon="file-invoice-dollar",
    tagline="Ordent facturen en bonnetjes voor de belastingaangifte: gegevens eruit halen, hernoemen en sorteren.",
    maker="ComposioHQ (community)", werkt="Claude Code, Claude-app", prijs="Gratis",
    bron="https://github.com/ComposioHQ/awesome-claude-skills/tree/master/invoice-organizer",
    wat="Leest rommelige facturen en bonnetjes, haalt datum, leverancier en bedrag eruit, geeft ze een consistente naam en sorteert ze in logische mappen.",
    wanneer=["Je moet je administratie op orde brengen voor de btw of inkomstenbelasting."],
    voorbeelden=[("Orden alle facturen in deze map per kwartaal en leverancier.", "Netjes hernoemde en gesorteerde bestanden.")],
    install=tabs(manual("git clone https://github.com/ComposioHQ/awesome-claude-skills.git\ncp -r awesome-claude-skills/invoice-organizer ~/.claude/skills/"),
                 app_zip("ComposioHQ/awesome-claude-skills", "invoice-organizer")),
    tips=[])

add(slug="meeting-insights", name="Meeting Insights Analyzer", cat="productiviteit", icon="people-group",
    tagline="Analyseert vergadertranscripten op communicatiepatronen en geeft persoonlijke feedback.",
    maker="ComposioHQ (community)", werkt="Claude Code, Claude-app", prijs="Gratis",
    bron="https://github.com/ComposioHQ/awesome-claude-skills/tree/master/meeting-insights-analyzer",
    wat="Leest transcripten van vergaderingen en laat zien waar je conflict vermijdt, veel stopwoorden gebruikt, het gesprek domineert of kansen mist om te luisteren. Handig om je gespreksleiding te verbeteren.",
    wanneer=["Je zit veel vergaderingen voor en wilt beter leiden."],
    voorbeelden=[("Analyseer de transcripten van de laatste drie vergaderingen en geef me feedback als voorzitter.", "Patronen en concrete tips.")],
    install=tabs(manual("git clone https://github.com/ComposioHQ/awesome-claude-skills.git\ncp -r awesome-claude-skills/meeting-insights-analyzer ~/.claude/skills/"),
                 app_zip("ComposioHQ/awesome-claude-skills", "meeting-insights-analyzer")),
    tips=[])

add(slug="changelog-generator", name="Changelog Generator", cat="productiviteit", icon="clock-rotate-left",
    tagline="Maakt van je git-commits heldere release notes voor gebruikers.",
    maker="ComposioHQ (community)", werkt="Claude Code", prijs="Gratis",
    bron="https://github.com/ComposioHQ/awesome-claude-skills/tree/master/changelog-generator",
    wat="Analyseert je commitgeschiedenis, deelt wijzigingen in (nieuw, verbeterd, opgelost) en vertaalt technische commits naar duidelijke, klantvriendelijke release notes.",
    wanneer=["Je publiceert een nieuwe versie van je app en wilt 'Wat is er nieuw'-tekst."],
    voorbeelden=[("Maak release notes voor alles sinds tag v2.3.0, in het Nederlands en Engels.", "Release notes in twee talen.")],
    install=tabs(manual("git clone https://github.com/ComposioHQ/awesome-claude-skills.git\ncp -r awesome-claude-skills/changelog-generator ~/.claude/skills/")),
    tips=[])

add(slug="tailored-resume", name="Tailored Resume Generator", cat="productiviteit", icon="id-card",
    tagline="Maakt een cv op maat van een vacature, zodat je relevante ervaring bovenaan staat.",
    maker="ComposioHQ (community)", werkt="Claude Code, Claude-app", prijs="Gratis",
    bron="https://github.com/ComposioHQ/awesome-claude-skills/tree/master/tailored-resume-generator",
    wat="Analyseert een vacaturetekst en herschrijft je cv zodat de ervaring, vaardigheden en resultaten die voor deze baan tellen het meest opvallen.",
    wanneer=["Je solliciteert en wilt per vacature een gericht cv."],
    voorbeelden=[("Hier is mijn cv en de vacature. Maak een cv op maat.", "Een aangepast cv met de juiste accenten.")],
    install=tabs(app_zip("ComposioHQ/awesome-claude-skills", "tailored-resume-generator"),
                 manual("git clone https://github.com/ComposioHQ/awesome-claude-skills.git\ncp -r awesome-claude-skills/tailored-resume-generator ~/.claude/skills/")),
    tips=["Laat het daarna als Word-bestand maken met de [Word-skill](../documenten/docx.md)."])

add(slug="domain-brainstormer", name="Domain Name Brainstormer", cat="productiviteit", icon="globe",
    tagline="Bedenkt creatieve domeinnamen en controleert of ze vrij zijn op .com, .io, .dev, .ai en meer.",
    maker="ComposioHQ (community)", werkt="Claude Code, Claude-app", prijs="Gratis",
    bron="https://github.com/ComposioHQ/awesome-claude-skills/tree/master/domain-name-brainstormer",
    wat="Genereert domeinnamen die passen bij je project en checkt de beschikbaarheid over meerdere extensies.",
    wanneer=["Je start een nieuw project of nieuwe app."],
    voorbeelden=[("Bedenk 15 domeinnamen voor een buurt-app en check of .nl en .app vrij zijn.", "Een lijst met beschikbare opties.")],
    install=tabs(app_zip("ComposioHQ/awesome-claude-skills", "domain-name-brainstormer")),
    tips=[])

add(slug="raffle-winner-picker", name="Raffle Winner Picker", cat="productiviteit", icon="ticket",
    tagline="Kiest eerlijk en transparant willekeurige winnaars uit een lijst of spreadsheet.",
    maker="ComposioHQ (community)", werkt="Claude Code, Claude-app", prijs="Gratis",
    bron="https://github.com/ComposioHQ/awesome-claude-skills/tree/master/raffle-winner-picker",
    wat="Voor winacties, loterijen en verlotingen: Claude kiest willekeurige winnaars uit een lijst, CSV of Google Sheet, op een controleerbare manier.",
    wanneer=["Je organiseert een winactie of verloting."],
    voorbeelden=[("Kies 3 winnaars uit deze lijst van inschrijvers, zonder dubbele e-mailadressen.", "Drie winnaars met uitleg van de trekking.")],
    install=tabs(app_zip("ComposioHQ/awesome-claude-skills", "raffle-winner-picker")),
    tips=[])

add(slug="google-workspace-skills", name="Google Workspace & AI Skills", cat="productiviteit", icon="google",
    tagline="25 skills voor Gmail, Agenda, Docs, Sheets, Slides, Drive, plus Postgres, Telegram, WhatsApp en meer.",
    maker="sanjay3290 (community)", werkt="Claude Code (+ Gemini CLI en andere agents)", prijs="Gratis (open source)",
    bron="https://github.com/sanjay3290/ai-skills",
    wat="Een collectie draagbare skills: Gmail, Google Agenda, Chat, Docs, Sheets, Slides en Drive, maar ook Deep Research via Gemini, Imagen voor afbeeldingen, NotebookLM, Jules, Outline, Atlassian, Azure DevOps, Postgres/MySQL/MSSQL (alleen-lezen) en Telegram en WhatsApp.",
    wanneer=["Je wilt Claude Code laten werken met je Google-account of databases."],
    voorbeelden=[("Zoek in mijn Gmail de laatste mails van de gemeente en zet de afspraken in mijn agenda.", "Agenda-items op basis van je mail.")],
    install=tabs(cc_market("sanjay3290/ai-skills", "ai-skills@ai-skills", "\nAlle 25 skills komen in één plugin. Bijwerken: `/plugin marketplace update ai-skills`.")),
    tips=["In de Claude-app kun je Google ook koppelen via Connectors, zonder skill."])

add(slug="notebooklm", name="NotebookLM Skill", cat="productiviteit", icon="book-open-reader",
    tagline="Laat Claude Code direct met NotebookLM praten voor antwoorden die alleen op jouw documenten zijn gebaseerd.",
    maker="PleasePrompto (community)", werkt="Alleen Claude Code (lokaal), niet de web-app", prijs="Gratis",
    bron="https://github.com/PleasePrompto/notebooklm-skill",
    wat="Claude stelt vragen aan je NotebookLM-notebooks en krijgt antwoorden die uitsluitend gebaseerd zijn op de bronnen die jij daar hebt geüpload. Handig als je betrouwbare antwoorden wilt zonder verzinsels.",
    wanneer=["Je hebt al je beleidsstukken of handleidingen in NotebookLM staan."],
    voorbeelden=[("Vraag mijn notebook 'Wijkbeleid' wat er staat over groenonderhoud.", "Een antwoord met bronverwijzingen uit je notebook.")],
    install=tabs(manual("mkdir -p ~/.claude/skills && cd ~/.claude/skills\ngit clone https://github.com/PleasePrompto/notebooklm-skill notebooklm")),
    tips=["Er is ook een MCP-versie van dezelfde maker."])

add(slug="tapestry", name="Tapestry (Learn This)", cat="productiviteit", icon="graduation-cap",
    tagline="Eén commando: van een URL (video, artikel, PDF) naar schone tekst én een actieplan om het toe te passen.",
    maker="Michal Parkola (community)", werkt="Claude Code", prijs="Gratis",
    bron="https://github.com/michalparkola/tapestry-skills-for-claude-code",
    wat="Zeg `learn-this <URL>` en de skill herkent het type inhoud (YouTube, artikel, PDF), haalt de tekst schoon binnen en maakt er een **Ship-Learn-Next**-actieplan van. Losse skills: youtube-transcript, article-extractor, ship-learn-next, scrum-sage, session-log en unblock-action.",
    wanneer=["Je kijkt veel tutorials en wilt er ook echt iets mee doen."],
    voorbeelden=[("learn-this https://www.youtube.com/watch?v=...", "Transcript plus een concreet stappenplan.")],
    install=tabs(manual("git clone https://github.com/michalparkola/tapestry-skills-for-claude-code.git\ncd tapestry-skills-for-claude-code\ncp -r learn-this youtube-transcript article-extractor ship-learn-next ~/.claude/skills/")),
    tips=[])

add(slug="epub", name="Markdown to EPUB", cat="productiviteit", icon="book",
    tagline="Zet markdown, onderzoek of chatsamenvattingen om naar een net e-book (EPUB3).",
    maker="smerchek (community)", werkt="Claude Code, Claude-app", prijs="Gratis",
    bron="https://github.com/smerchek/claude-epub-skill",
    wat="Maakt van markdown-documenten professionele EPUB3-e-books die werken op Apple Books, Kobo, e-readers en meer. Perfect om onderzoek of lange artikelen offline te lezen.",
    wanneer=["Je wilt een lang document of deze wiki als e-book lezen."],
    voorbeelden=[("Maak van deze 5 artikelen één e-book met inhoudsopgave.", "Een .epub-bestand.")],
    install=tabs(app_zip("smerchek/claude-epub-skill", "markdown-to-epub")),
    tips=[])

add(slug="skill-seekers", name="Skill Seekers", cat="productiviteit", icon="magnifying-glass-plus",
    tagline="Zet elke documentatiewebsite, GitHub-repo, PDF of video automatisch om in een Claude-skill.",
    maker="yusufkaraaslan (community)", werkt="Losse tool (Python), output werkt in Claude", prijs="Gratis (open source)",
    bron="https://github.com/yusufkaraaslan/Skill_Seekers",
    wat="Skill Seekers haalt documentatie op (websites, GitHub-repo's, PDF's, video's, notebooks) en verpakt die als skill. Zo geef je Claude in een paar minuten expertkennis van een tool of API die hij nog niet kent.",
    wanneer=["Je werkt met een niche-API of tool waar Claude weinig van weet."],
    voorbeelden=[("skill-seekers scrape --url https://docs.voorbeeld.nl", "Een kant-en-klare skillmap om te installeren.")],
    install=tabs(tab("Installeren", "```bash\npip install skill-seekers\n```\n\nVolg daarna de quickstart in de README.")),
    tips=[])

# ───────────── MEDIA ─────────────
add(slug="elevenlabs", name="ElevenLabs", cat="media", icon="microphone-lines",
    tagline="Tekst-naar-spraak, spraak-naar-tekst, muziek, geluidseffecten, dubbing en voice agents.",
    maker="ElevenLabs (officieel van de makers)", werkt="Claude Code (+ andere agents)", prijs="Skills gratis; ElevenLabs-API volgens hun prijzen",
    bron="https://github.com/elevenlabs/skills",
    wat="Skills voor de ElevenLabs-API: tekst-naar-spraak, spraak-naar-tekst, muziek, geluidseffecten, dubbing, voice changer, stemisolatie, realtime en het bouwen van spraakagents.",
    wanneer=["Je wilt een voice-over, podcastintro of spraakfunctie in je app."],
    voorbeelden=[("Maak een Nederlandse voice-over van dit script met een rustige stem.", "Een audiobestand.")],
    install=tabs(npx("npx skills add elevenlabs/skills")),
    tips=["Je hebt een ElevenLabs-API-sleutel nodig; de skill `setup-api-key` helpt je."])

add(slug="excalidraw-diagram", name="Excalidraw Diagram", cat="media", icon="pen-to-square",
    tagline="Maakt mooie Excalidraw-diagrammen uit gewone taal: diagrammen die iets uitleggen, niet alleen boxen en pijlen.",
    maker="Cole Medin (community)", werkt="Claude Code (+ OpenCode)", prijs="Gratis",
    bron="https://github.com/coleam00/excalidraw-diagram-skill",
    wat="De vormen in het diagram volgen het idee dat ze uitleggen: waaiers voor één-op-veel, tijdlijnen voor volgordes, samenkomende lijnen voor bundeling. Zo krijg je geen saaie kaartjesraster maar een diagram dat iets vertelt.",
    wanneer=["Je wilt een architectuur, proces of idee visueel uitleggen."],
    voorbeelden=[("Teken hoe een melding van de meldkamer via de server naar de app gaat.", "Een .excalidraw-bestand.")],
    install=tabs(manual("git clone https://github.com/coleam00/excalidraw-diagram-skill.git\ncp -r excalidraw-diagram-skill .claude/skills/excalidraw-diagram   # of ~/.claude/skills/ voor al je projecten")),
    tips=[])

add(slug="obsidian-visual", name="Obsidian Visual Skills", cat="media", icon="diagram-project",
    tagline="Canvas-, Excalidraw- en Mermaid-diagrammen maken vanuit tekst, voor in Obsidian.",
    maker="Axton Liu (community)", werkt="Claude Code", prijs="Gratis",
    bron="https://github.com/axtonliu/axton-obsidian-visual-skills",
    wat="Drie skills: **excalidraw-diagram**, **mermaid-visualizer** en **obsidian-canvas-creator**. Ze zetten tekst om in diagrammen die je direct in Obsidian opent.",
    wanneer=["Je gebruikt Obsidian en wilt notities visualiseren."],
    voorbeelden=[("Maak een Obsidian-canvas van deze projectnotities.", "Een .canvas-bestand met kaarten en verbindingen.")],
    install=mk("axtonliu/axton-obsidian-visual-skills", "obsidian-visual-skills"),
    tips=[])

add(slug="d3-viz", name="D3.js Visualisatie", cat="media", icon="chart-area",
    tagline="Interactieve datavisualisaties met D3.js: grafieken, netwerken en kaarten.",
    maker="Chris von Csefalvay (community)", werkt="Claude Code, Claude-app", prijs="Gratis",
    bron="https://github.com/chrisvoncsefalvay/claude-d3js-skill",
    wat="Leert Claude om met D3.js aangepaste grafieken, netwerkdiagrammen en geografische visualisaties te maken, met volledige controle over overgangen en interactie.",
    wanneer=["Standaardgrafieken zijn niet genoeg en je wilt iets op maat."],
    voorbeelden=[("Maak een interactieve kaart van Nederland met het aantal meldingen per gemeente.", "Een D3-kaart met tooltips.")],
    install=tabs(app_zip("chrisvoncsefalvay/claude-d3js-skill", "(de hoofdmap, hernoem naar d3-viz)"),
                 manual("git clone https://github.com/chrisvoncsefalvay/claude-d3js-skill.git ~/.claude/skills/d3-viz")),
    tips=[])

add(slug="csv-summarizer", name="CSV Data Summarizer", cat="media", icon="table",
    tagline="Upload een CSV en krijg direct een analyse met statistiek, trends en grafieken.",
    maker="coffeefuelbump (community)", werkt="Claude-app, Claude Code", prijs="Gratis",
    bron="https://github.com/coffeefuelbump/csv-data-summarizer-claude-skill",
    wat="Herkent automatisch wat voor data je hebt (verkoop, klanten, financieel, enquête) en maakt een complete analyse met statistieken, verbanden, verdelingen, trends en visualisaties, zonder dat je eerst hoeft te zeggen wat je wilt weten.",
    wanneer=["Je hebt een export en wilt snel weten wat erin zit."],
    voorbeelden=[("(upload enquete.csv)", "Een samenvatting met de belangrijkste inzichten en grafieken.")],
    install=tabs(app_zip("coffeefuelbump/csv-data-summarizer-claude-skill", "(de hoofdmap met SKILL.md)")),
    tips=[])

add(slug="image-enhancer", name="Image Enhancer", cat="media", icon="wand-sparkles",
    tagline="Maakt afbeeldingen en screenshots scherper en duidelijker voor presentaties en social.",
    maker="ComposioHQ (community)", werkt="Claude Code", prijs="Gratis",
    bron="https://github.com/ComposioHQ/awesome-claude-skills/tree/master/image-enhancer",
    wat="Verbetert resolutie, scherpte en helderheid van afbeeldingen, vooral screenshots. Ideaal voor documentatie, presentaties en social media.",
    wanneer=["Je screenshots zien er wazig uit in je presentatie of App Store-pagina."],
    voorbeelden=[("Maak alle screenshots in deze map scherper voor mijn presentatie.", "Verbeterde afbeeldingen.")],
    install=tabs(manual("git clone https://github.com/ComposioHQ/awesome-claude-skills.git\ncp -r awesome-claude-skills/image-enhancer ~/.claude/skills/")),
    tips=[])

add(slug="stitch", name="Google Stitch Skills", cat="media", icon="object-group",
    tagline="Werken met Google Stitch: designs genereren, design.md extraheren en omzetten naar React of shadcn/ui.",
    maker="Google Labs (officieel van de makers)", werkt="Claude Code (+ Codex, Gemini CLI, Cursor)", prijs="Gratis",
    bron="https://github.com/google-labs-code/stitch-skills",
    wat="Skills voor Google Stitch, Google's AI-designtool: designs genereren en verbeteren, een `design.md` uit een bestaand ontwerp halen, je designsysteem beheren en ontwerpen omzetten naar React, React Native, shadcn/ui of een Vite-dashboard.",
    wanneer=["Je ontwerpt in Stitch en wilt het snel naar code brengen."],
    voorbeelden=[("Zet dit Stitch-ontwerp om naar React-componenten met shadcn/ui.", "Componentcode die het ontwerp volgt.")],
    install=tabs(tab("Claude Code", "```bash\nnpx plugins add google-labs-code/stitch-skills --scope project --target claude-code\n```"),
                 npx("npx skills add google-labs-code/stitch-skills")),
    tips=[])

# ───────────── EXTRA in bestaande categorieën ─────────────
add(slug="playwright-skill", name="Playwright Skill", cat="ontwikkeling", icon="masks-theater",
    tagline="Laat Claude zelf Playwright-scripts schrijven en draaien, van simpele paginatests tot lange flows.",
    maker="lackeyjb (community)", werkt="Claude Code (+ Cursor en meer)", prijs="Gratis (open source)",
    bron="https://github.com/lackeyjb/playwright-skill",
    wat="Een algemene browserautomatisering-skill: Claude schrijft en draait Playwright-code ter plekke, voor tests, het controleren van formulieren of het doorlopen van een complete gebruikersflow.",
    wanneer=["Je wilt je webapp automatisch laten testen of controleren."],
    voorbeelden=[("Test de registratieflow op mijn site en meld wat er misgaat.", "Een testrun met screenshots en bevindingen.")],
    install=mk("lackeyjb/playwright-skill", "playwright-skill@playwright-skill",
               nx="npx skills add lackeyjb/playwright-skill --skill playwright-skill --agent claude-code --global --yes"),
    tips=["Zie ook de officiële [Webapp Testing](webapp-testing.md)."])

add(slug="context-engineering-kit", name="Context Engineering Kit", cat="ontwikkeling", icon="sliders",
    tagline="Geavanceerde technieken: DDD, kaizen, subagent-driven development, critique en prompt engineering.",
    maker="NeoLab (community)", werkt="Claude Code (+ OpenCode, Cursor en meer)", prijs="Gratis (open source)",
    bron="https://github.com/NeoLabHQ/context-engineering-kit",
    wat="Een grote set plugins met technieken voor betere AI-ontwikkeling: software-architectuur en DDD, kaizen (continu verbeteren), subagent-driven development, reflectie en kritiek, prompt engineering, documentatie en eigen commando's, hooks en skills maken.",
    wanneer=["Je wilt het maximale uit Claude Code halen bij grote projecten."],
    voorbeelden=[("/critique", "Een kritische beoordeling van het laatste werk door meerdere 'juryleden'.")],
    install=tabs(tab("Claude Code", "```bash\n/plugin marketplace add NeoLabHQ/context-engineering-kit\n/plugin install ddd@NeoLabHQ/context-engineering-kit\n```\n\nAndere plugins: `customaize-agent`, `docs`, `fpf`, `kaizen`, `sadd` en meer.")),
    tips=["Documentatie: [neolab.gitbook.io/cek](https://neolab.gitbook.io/cek/)."])

add(slug="everything-claude-code", name="Everything Claude Code (ECC)", cat="ontwikkeling", icon="layer-group",
    tagline="Een complete 'agent harness': agents, skills, commando's, hooks en regels in één groot pakket.",
    maker="affaan-m (community)", werkt="Claude Code (+ andere agents)", prijs="Gratis (open source)",
    bron="https://github.com/affaan-m/everything-claude-code",
    wat="ECC is een uitgebreid systeem van agents, skills, commando's en hooks voor Claude Code, bedoeld als compleet 'besturingssysteem' voor je agent. Groot en uitgebreid: vooral interessant voor ervaren gebruikers.",
    wanneer=["Je wilt een kant-en-klare, uitgebreide Claude Code-setup."],
    voorbeelden=[("(na installatie) /plan Voeg betalingen toe", "Een begeleide planning- en bouwflow.")],
    install=tabs(cc_market("https://github.com/affaan-m/ECC", "ecc@ecc", "\nKopieer de hooks niet ook nog naar `settings.json`: de plugin laadt ze al.")),
    tips=["Kies óf de plugin óf handmatige installatie, niet allebei."])

add(slug="superpowers-lab", name="Superpowers Lab", cat="denken", icon="flask",
    tagline="Experimentele Superpowers-skills: dubbele functies opsporen, interactieve terminals met tmux en meer.",
    maker="obra (community)", werkt="Claude Code", prijs="Gratis (open source)",
    bron="https://github.com/obra/superpowers-lab",
    wat="Nieuwe technieken die nog worden verfijnd: `finding-duplicate-functions` (zoekt functies die hetzelfde doen maar anders geschreven zijn, typisch voor AI-code), `using-tmux-for-interactive-commands`, `mcp-cli` en `windows-vm`.",
    wanneer=["Je gebruikt Superpowers al en wilt nieuwe technieken proberen."],
    voorbeelden=[("Zoek dubbele functies in deze codebase.", "Een lijst met functies die je kunt samenvoegen.")],
    install=tabs(tab("Claude Code", "Installeer de plugin rechtstreeks vanaf GitHub:\n\n```bash\nclaude plugin install https://github.com/obra/superpowers-lab\n```\n\nVoor sommige skills heb je `tmux` nodig.")),
    tips=[])

add(slug="family-history", name="Family History Research", cat="productiviteit", icon="tree",
    tagline="Hulp bij het plannen van stamboom- en genealogieonderzoek.",
    maker="emaynard (community)", werkt="Claude-app, Claude Code", prijs="Gratis",
    bron="https://github.com/emaynard/claude-family-history-research-skill",
    wat="Helpt je genealogieonderzoek te structureren: wat weet je al, welke bronnen raadpleeg je, hoe noteer je bevindingen en wat zijn de volgende stappen.",
    wanneer=["Je zoekt je familiegeschiedenis uit."],
    voorbeelden=[("Help me een onderzoeksplan te maken voor mijn overgrootvader, geboren rond 1890 in Gelderland.", "Een plan met bronnen zoals archieven en registers.")],
    install=tabs(app_zip("emaynard/claude-family-history-research-skill", "(de skillmap met SKILL.md)")),
    tips=["Voor Nederland zijn WieWasWie en Open Archieven goede startpunten."])

add(slug="anydesign", name="AnyDesign", cat="design", icon="eye-dropper",
    tagline="Analyseert een afbeelding, website of Figma-bestand en maakt er een gestructureerde design.md van.",
    maker="uxKero (community)", werkt="Claude Code, Claude-app", prijs="Gratis",
    bron="https://github.com/uxKero/anydesign",
    wat="Zet afbeeldingen, websites en Figma-bestanden om in een leesbare designspecificatie: designsysteem, componentenoverzicht en instructies om het na te bouwen. Losse elementen (een navbar, een 3D-illustratie) kun je kopiëren als 'rebuild-prompt'.",
    wanneer=["Je wilt de stijl van een eigen ontwerp vastleggen om consequent verder te bouwen."],
    voorbeelden=[("Maak een design.md van deze screenshot van mijn app.", "Kleuren, typografie, spacing en componenten op een rij.")],
    install=tabs(manual("git clone https://github.com/uxKero/anydesign.git\ncp -r anydesign ~/.claude/skills/")),
    tips=["Gebruik dit voor je eigen ontwerpen of met toestemming; kopieer niet zomaar andermans design."])
