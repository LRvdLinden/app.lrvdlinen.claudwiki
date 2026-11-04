from install import *

CATS = [
    # slug, titel, icoon, intro
    ("documenten", "Documenten & kantoor", "file-lines",
     "Skills die Claude echte kantoorbestanden laten maken en bewerken: Word, PDF, PowerPoint en Excel, plus hulp bij interne communicatie en samen schrijven."),
    ("design", "Design & frontend", "palette",
     "Out of the box ziet wat Claude bouwt er vaak een beetje generiek uit. Deze skills geven Claude smaak: stijlen, kleurpaletten, typografie, thema's en presentaties die er professioneel uitzien."),
    ("creatief", "Creatief & video", "film",
     "Animaties en video's in code, generatieve kunst, posters en GIF's. Ideaal voor content creators."),
    ("denken", "Denken & plannen", "brain",
     "Skills die Claude beter laten nadenken voordat hij begint: brainstormen, plannen, je kritisch ondervragen, tegenspreken en werk netjes overdragen."),
    ("ontwikkeling", "Ontwikkelen & code", "code",
     "Voor wie met Claude Code bouwt: engineering-workflows, code reviews, testen, MCP-servers, Vercel/React, Terraform en n8n."),
    ("content", "Schrijven, content & marketing", "pen-nib",
     "Teksten die niet naar AI klinken, Instagram-content, carrousels, trendonderzoek, SEO en marketing."),
    ("kennis", "Kennis & geheugen", "book-bookmark",
     "Laat Claude dingen onthouden tussen sessies, werk samen met je Obsidian-vault en laat Claude zelf nieuwe skills leren."),
    ("zakelijk", "Zakelijk per rol", "briefcase",
     "Complete skillpakketten (plugins) per functie: sales, finance, legal, marketing, data, HR, operations, klantenservice en het mkb."),
    ("security", "Security & wetenschap", "shield-halved",
     "Professionele beveiligingsanalyse van code en een enorme bibliotheek met wetenschappelijke skills."),
    ("bouwen", "Zelf skills bouwen", "screwdriver-wrench",
     "De skills waarmee je je eigen skills maakt, test en verbetert."),
]

S = []

def add(**k):
    S.append(k)

# ───────────────────────── DOCUMENTEN ─────────────────────────
add(slug="docx", name="Word (docx)", cat="documenten", icon="file-word",
    tagline="Maakt, leest en bewerkt Word-documenten met opmaak, inhoudsopgave en wijzigingen bijhouden.",
    maker="Anthropic (officieel)", werkt="Claude-app, Claude Code, API", prijs="Gratis bij betaald abonnement (source-available)",
    bron="https://github.com/anthropics/skills/tree/main/skills/docx",
    wat="De Word-skill is de motor achter de Word-bestanden die Claude voor je maakt. Hij weet hoe een `.docx` van binnen werkt: koppen, stijlen, tabellen, kop- en voetteksten, paginanummers, inhoudsopgaven, afbeeldingen en zelfs **wijzigingen bijhouden** (track changes) en opmerkingen. Ook kan hij bestaande Word-bestanden lezen en aanpassen, of een sjabloon (`.dotx`) als basis gebruiken.",
    wanneer=["Je hebt echt een `.docx` nodig, bijvoorbeeld voor een gemeente, school of klant.",
             "Je wilt een bestaand Word-bestand laten nakijken met zichtbare wijzigingen.",
             "Je wilt een briefsjabloon met huisstijl vullen."],
    voorbeelden=[("Maak van deze notulen een net Word-document met inhoudsopgave, paginanummers en het logo van de wijkraad in de koptekst.", "Een opgemaakt `.docx`-bestand om te downloaden."),
                 ("Lees contract.docx en stel verbeteringen voor als bijgehouden wijzigingen.", "Het originele document met track changes die je in Word kunt accepteren of weigeren.")],
    install=official_doc("docx"),
    tips=["Zeg expliciet 'als Word-bestand' als je een .docx wilt; anders kiest Claude soms een ander formaat.",
          "Upload je eigen sjabloon (.dotx) om je huisstijl te laten gebruiken."])

add(slug="pdf", name="PDF", cat="documenten", icon="file-pdf",
    tagline="Alles met PDF's: tekst en tabellen eruit halen, samenvoegen, splitsen, formulieren invullen, OCR en watermerken.",
    maker="Anthropic (officieel)", werkt="Claude-app, Claude Code, API", prijs="Gratis bij betaald abonnement (source-available)",
    bron="https://github.com/anthropics/skills/tree/main/skills/pdf",
    wat="De PDF-skill geeft Claude een complete gereedschapskist voor PDF-bestanden. Hij haalt tekst en tabellen uit PDF's, voegt bestanden samen of splitst ze, draait pagina's, voegt watermerken toe, vult PDF-formulieren in, versleutelt of ontsleutelt bestanden en maakt gescande PDF's doorzoekbaar met OCR. Ook kan hij nieuwe PDF's maken.",
    wanneer=["Je wilt gegevens uit een stapel facturen of rapporten in een tabel.",
             "Je moet een PDF-formulier invullen.",
             "Je hebt een scan die je wilt doorzoeken."],
    voorbeelden=[("Haal uit deze 12 facturen (PDF) de datum, leverancier en het totaalbedrag en zet het in een tabel.", "Een overzichtstabel, eventueel als Excel."),
                 ("Voeg deze drie PDF's samen, zet pagina 4 rechtop en zet een watermerk 'CONCEPT' op elke pagina.", "Eén nieuwe PDF.")],
    install=official_doc("pdf"),
    tips=["Bij gescande documenten: vraag expliciet om OCR.",
          "Voor grote PDF's: vraag eerst om een inhoudsoverzicht en zoom daarna in."])

add(slug="pptx", name="PowerPoint (pptx)", cat="documenten", icon="file-powerpoint",
    tagline="Maakt en bewerkt PowerPoint-presentaties, inclusief sjablonen, notities en layouts.",
    maker="Anthropic (officieel)", werkt="Claude-app, Claude Code, API", prijs="Gratis bij betaald abonnement (source-available)",
    bron="https://github.com/anthropics/skills/tree/main/skills/pptx",
    wat="Met de PowerPoint-skill bouwt Claude complete presentaties als `.pptx`: dia's met titels, opsommingen, afbeeldingen, grafieken en sprekersnotities. Hij kan ook een bestaande presentatie of een sjabloon (`.potx`) lezen, de tekst eruit halen, dia's aanpassen of presentaties samenvoegen en splitsen.",
    wanneer=["Je moet een presentatie aanleveren als PowerPoint-bestand.",
             "Je wilt een bestaande presentatie in je huisstijl laten bijwerken.",
             "Je wilt de inhoud van een presentatie samenvatten."],
    voorbeelden=[("Maak een presentatie van 10 dia's over de plannen van de wijkraad voor 2027, met sprekersnotities per dia.", "Een `.pptx` die je in PowerPoint of Keynote opent."),
                 ("Gebruik sjabloon huisstijl.potx en zet dit rapport om naar dia's.", "Een presentatie in jouw sjabloon.")],
    install=official_doc("pptx"),
    tips=["Wil je geen bestand maar een snelle webpresentatie? Kijk naar [Frontend Slides](../design/frontend-slides.md)."])

add(slug="xlsx", name="Excel (xlsx)", cat="documenten", icon="file-excel",
    tagline="Spreadsheets openen, opschonen, formules en grafieken toevoegen of nieuwe sheets bouwen.",
    maker="Anthropic (officieel)", werkt="Claude-app, Claude Code, API", prijs="Gratis bij betaald abonnement (source-available)",
    bron="https://github.com/anthropics/skills/tree/main/skills/xlsx",
    wat="De Excel-skill laat Claude echte spreadsheets maken en bewerken: `.xlsx`, `.xlsm`, `.csv` en `.tsv`. Hij voegt kolommen en **werkende formules** toe, maakt grafieken, zet opmaak goed, ruimt rommelige data op (verkeerde kopregels, lege rijen) en zet bestanden om tussen formaten.",
    wanneer=["Je hebt een begroting, planning of overzicht nodig dat je verder bewerkt in Excel.",
             "Je hebt een rommelige export die opgeschoond moet worden.",
             "Je wilt grafieken bij je cijfers."],
    voorbeelden=[("Maak een begroting voor het buurtfeest met inkomsten, uitgaven, een totaalformule en een cirkeldiagram.", "Een `.xlsx` met werkende formules."),
                 ("Deze CSV-export is een rommeltje. Schoon hem op, zet de datums goed en maak er een nette Excel van.", "Een opgeschoonde spreadsheet.")],
    install=official_doc("xlsx"),
    tips=["Vraag Claude om formules te gebruiken in plaats van vaste getallen, dan blijft je sheet bruikbaar als je iets aanpast."])

add(slug="doc-coauthoring", name="Doc Co-authoring", cat="documenten", icon="people-arrows",
    tagline="Een gestructureerde werkwijze om samen met Claude documenten, voorstellen en specs te schrijven.",
    maker="Anthropic (officieel)", werkt="Claude-app, Claude Code, API", prijs="Gratis (Apache 2.0)",
    bron="https://github.com/anthropics/skills/tree/main/skills/doc-coauthoring",
    wat="In plaats van in één keer een tekst uit te spugen, leidt deze skill je door een vast proces: eerst haalt Claude de context bij je op, daarna schrijft en verfijnt hij in rondes en tot slot controleert hij of het document werkt voor de lezer. Handig voor voorstellen, technische specificaties, beslisdocumenten en beleidsstukken.",
    wanneer=["Je schrijft een voorstel, beleidsnotitie of spec en wilt dat het écht klopt.",
             "Je hebt veel losse informatie die in een helder stuk moet."],
    voorbeelden=[("Help me een voorstel te schrijven aan de gemeente voor meer verlichting in het park.", "Claude stelt eerst gerichte vragen, schrijft dan in stappen en checkt het resultaat vanuit de lezer.")],
    install=official_example("doc-coauthoring"), tips=[])

add(slug="internal-comms", name="Internal Comms", cat="documenten", icon="bullhorn",
    tagline="Schrijft interne communicatie in vaste formats: statusupdates, nieuwsbrieven, FAQ's en incidentrapporten.",
    maker="Anthropic (officieel)", werkt="Claude-app, Claude Code, API", prijs="Gratis (Apache 2.0)",
    bron="https://github.com/anthropics/skills/tree/main/skills/internal-comms",
    wat="Deze skill bevat voorbeeldformats voor allerlei interne communicatie: statusrapporten, updates voor het management, nieuwsbrieven, FAQ's, incidentrapporten en projectupdates. Het idee: je past de formats aan naar hoe jouw organisatie het graag ziet, zodat elk stuk consistent is.",
    wanneer=["Je schrijft regelmatig updates of nieuwsbrieven.",
             "Je wilt dat incidentrapporten altijd dezelfde opbouw hebben."],
    voorbeelden=[("Schrijf een incidentrapport over de storing van gisteravond: oorzaak, impact, oplossing en vervolgacties.", "Een rapport in een vaste, zakelijke structuur.")],
    install=official_example("internal-comms"),
    tips=["Maak een eigen kopie en vervang de voorbeeldformats door die van jouw organisatie."])

# ───────────────────────── DESIGN ─────────────────────────
add(slug="frontend-design", name="Frontend Design", cat="design", icon="wand-magic-sparkles",
    tagline="Geeft Claude een uitgesproken ontwerpsmaak, zodat interfaces niet als standaardsjabloon ogen.",
    maker="Anthropic (officieel)", werkt="Claude-app, Claude Code, API", prijs="Gratis (Apache 2.0)",
    bron="https://github.com/anthropics/skills/tree/main/skills/frontend-design",
    wat="Frontend Design leert Claude om bij elke interface eerst een **duidelijke esthetische richting** te kiezen: typografie, kleur, compositie en details. Het doel is dat een website of app er doordacht uitziet in plaats van 'zoals elke AI-site'. Het is ook als plugin beschikbaar in de officiële Claude Code-marketplace.",
    wanneer=["Je laat Claude een website, landingspagina of app-scherm bouwen.",
             "Je wilt een bestaand ontwerp een eigen gezicht geven."],
    voorbeelden=[("Bouw een landingspagina voor mijn weer-app. Kies een gedurfde, eigen stijl, geen standaard paarse gradient.", "Een pagina met een herkenbare, bewuste stijl.")],
    install=tabs(app_builtin(), cc_official("frontend-design"), npx("npx skills add anthropics/skills --skill frontend-design")),
    tips=["Geef een paar woorden sfeer mee ('Scandinavisch rustig', 'retro-krant', 'luxe nacht') voor nog betere resultaten."])

add(slug="ui-ux-pro-max", name="UI UX Pro Max", cat="design", icon="layer-group",
    tagline="Een doorzoekbare designbibliotheek met tientallen stijlen, 192 kleurpaletten, 74 fontcombinaties en 119 UX-richtlijnen.",
    maker="nextlevelbuilder (community)", werkt="Claude Code (+ Cursor, Copilot, Codex en meer)", prijs="Gratis (open source)",
    bron="https://github.com/nextlevelbuilder/ui-ux-pro-max-skill",
    social="Tip van Bart Boonstra: *'UI UX Pro Max maakt elke layout 1000x professioneler. Letterlijk.'*",
    wat="UI UX Pro Max is een van de populairste community-skills. Hij geeft Claude een lokale, doorzoekbare database met UI-stijlen (glassmorphism, bento grid, brutalism, dark mode…), kleurpaletten per type product, lettertypecombinaties met Google Fonts, UX-richtlijnen en anti-patronen, iconen, animatie-presets en grafiektypen. Claude zoekt bij jouw vraag de best passende stijl, kleuren en typografie op en past ze consequent toe. Het pakket bevat ook extra skills voor banners, huisstijl, designsystemen en slides.",
    wanneer=["Je bouwt een website, dashboard of app en wilt dat het er direct professioneel uitziet.",
             "Je wilt een designsysteem (kleuren, fonts, spacing) laten voorstellen.",
             "Je wilt een bestaand scherm laten reviewen op UX en toegankelijkheid."],
    voorbeelden=[("Maak een dashboard voor een alarmeringsapp. Zoek een passende stijl en een passend kleurpalet.", "Een dashboard met een onderbouwde stijl, palet en fontkeuze."),
                 ("Review dit instellingenscherm op UX-fouten en toegankelijkheid.", "Een lijst met concrete verbeterpunten.")],
    install=tabs(
        cc_market("nextlevelbuilder/ui-ux-pro-max-skill", "ui-ux-pro-max@ui-ux-pro-max-skill"),
        tab("CLI (aanbevolen)", """
De makers raden hun eigen installer aan:

```bash
npm install -g ui-ux-pro-max-cli
cd /pad/naar/je/project
uipro init --ai claude            # alleen dit project
uipro init --ai claude --global   # voor al je projecten (~/.claude/skills/)
```

Gebruik `ui-ux-pro-max-cli`; het oudere pakket `uipro-cli` is verouderd."""),
        app_zip("nextlevelbuilder/ui-ux-pro-max-skill", ".claude/skills/ui-ux-pro-max")),
    tips=["Combineer met [Frontend Design](frontend-design.md) of [Impeccable](impeccable.md) voor nog meer controle."])

add(slug="impeccable", name="Impeccable", cat="design", icon="gem",
    tagline="Een designvocabulaire voor je agent: commando's als polish, bolder, critique en audit, plus een detector voor 'AI-slop'.",
    maker="Paul Bakaus (community)", werkt="Claude Code (+ Cursor, Codex, Copilot en meer)", prijs="Gratis (open source)",
    bron="https://github.com/pbakaus/impeccable",
    wat="Impeccable geeft Claude een gedeelde taal om ontwerpen te sturen. Je zegt bijvoorbeeld *polish*, *bolder*, *critique* of *audit* en Claude weet precies wat je bedoelt. Er zit een detector bij die typische AI-designfouten ('slop') opspoort, en een hook die elk UI-bestand dat Claude aanpast automatisch controleert voordat hij zegt dat hij klaar is. De CLI werkt ook los, bijvoorbeeld in je CI.",
    wanneer=["Je wilt een ontwerp in kleine, gerichte stappen verbeteren.",
             "Je wilt automatisch gewaarschuwd worden voor generiek ogende UI."],
    voorbeelden=[("critique de homepage en daarna polish de hero-sectie", "Eerst een kritische review, daarna een verfijnde hero."),
                 ("npx impeccable detect src/", "Een scan van je code op typische AI-designpatronen.")],
    install=tabs(
        tab("Claude Code", """
```bash
/plugin marketplace add pbakaus/impeccable
```

Open daarna `/plugin` en installeer **Impeccable**. Zeg 'ja' tegen de design-hook: die vangt de meeste fouten automatisch af."""),
        tab("CLI", """
```bash
npx impeccable detect src/                  # map scannen
npx impeccable detect https://example.com   # live pagina scannen
```""")),
    tips=["Documentatie: [impeccable.style/docs](https://impeccable.style/docs)."])

add(slug="theme-factory", name="Theme Factory", cat="design", icon="swatchbook",
    tagline="Tien kant-en-klare thema's (kleur + lettertype) om slides, documenten en webpagina's in één klap te stylen.",
    maker="Anthropic (officieel)", werkt="Claude-app, Claude Code, API", prijs="Gratis (Apache 2.0)",
    bron="https://github.com/anthropics/skills/tree/main/skills/theme-factory",
    wat="Theme Factory is een gereedschapskist met tien vooraf ingestelde thema's met bijpassende kleuren en lettertypen. Je past ze toe op alles wat Claude maakt: presentaties, documenten, rapporten of HTML-pagina's. Past geen enkel thema? Dan verzint Claude er ter plekke een nieuwe.",
    wanneer=["Je wilt snel een consistente look over meerdere stukken.",
             "Je weet niet welke kleuren bij elkaar passen."],
    voorbeelden=[("Laat me de thema's zien en pas daarna het rustigste toe op deze presentatie.", "Een overzicht van thema's en een gestylede presentatie.")],
    install=official_example("theme-factory"), tips=[])

add(slug="brand-guidelines", name="Brand Guidelines", cat="design", icon="copyright",
    tagline="Voorbeeld van een huisstijl-skill: past vaste merkkleuren en typografie toe op alles wat Claude maakt.",
    maker="Anthropic (officieel)", werkt="Claude-app, Claude Code, API", prijs="Gratis (Apache 2.0)",
    bron="https://github.com/anthropics/skills/tree/main/skills/brand-guidelines",
    wat="Deze skill past de huisstijl van Anthropic toe (kleuren en lettertypen). Hij is vooral interessant als **voorbeeld**: kopieer hem, vervang de kleuren en fonts door die van jouw merk en Claude maakt voortaan alles in jouw huisstijl.",
    wanneer=["Je wilt dat Claude standaard jouw merkkleuren en fonts gebruikt.",
             "Je wilt leren hoe een huisstijl-skill is opgebouwd."],
    voorbeelden=[("Maak met mijn huisstijl-skill een flyer voor de buurtavond.", "Een flyer in jouw kleuren en lettertypen.")],
    install=official_example("brand-guidelines"),
    tips=["Zie [Je eigen skill maken](../../basis/eigen-skill-maken.md) om er je eigen huisstijl van te maken."])

add(slug="canvas-design", name="Canvas Design", cat="design", icon="image",
    tagline="Maakt posters, kunst en statische ontwerpen als PNG of PDF, vanuit een eigen ontwerpfilosofie.",
    maker="Anthropic (officieel)", werkt="Claude-app, Claude Code, API", prijs="Gratis (Apache 2.0)",
    bron="https://github.com/anthropics/skills/tree/main/skills/canvas-design",
    wat="Canvas Design laat Claude eerst een ontwerpfilosofie formuleren en daarna een origineel visueel ontwerp maken: een poster, kunstwerk of ander statisch stuk, als `.png` of `.pdf`. De skill is erop gericht om origineel werk te maken in plaats van bestaand werk te kopiëren.",
    wanneer=["Je hebt een poster, uitnodiging of kunstprint nodig."],
    voorbeelden=[("Ontwerp een poster voor de Koningsdag-activiteiten in de wijk, A3, als PDF.", "Een printklare poster.")],
    install=official_example("canvas-design"), tips=[])

add(slug="web-artifacts-builder", name="Web Artifacts Builder", cat="design", icon="cubes",
    tagline="Bouwt grote, complexe webartifacts met React, Tailwind CSS en shadcn/ui.",
    maker="Anthropic (officieel)", werkt="Claude-app, Claude Code, API", prijs="Gratis (Apache 2.0)",
    bron="https://github.com/anthropics/skills/tree/main/skills/web-artifacts-builder",
    wat="Voor simpele pagina's heb je deze skill niet nodig. Maar wil je een groter artifact met meerdere onderdelen, state management of routing? Dan zet deze skill een moderne stack op (React, Tailwind CSS, shadcn/ui) en bundelt alles tot één artifact.",
    wanneer=["Je wilt een uitgebreide tool of mini-app als artifact.",
             "Je hebt meerdere schermen of componenten nodig."],
    voorbeelden=[("Bouw een planningstool voor vrijwilligers met een weekoverzicht, filters en een formulier.", "Een interactieve mini-app als artifact.")],
    install=official_example("web-artifacts-builder"), tips=[])

add(slug="frontend-slides", name="Frontend Slides", cat="design", icon="display",
    tagline="Prachtige, geanimeerde HTML-presentaties maken of PowerPoints omzetten naar het web.",
    maker="Zara Zhang (community)", werkt="Claude Code (de SKILL.md werkt ook in andere agents)", prijs="Gratis (open source)",
    bron="https://github.com/zarazhangrui/frontend-slides",
    wat="Frontend Slides maakt presentaties als één HTML-bestand met animaties, in plaats van een PowerPoint. Je hoeft geen designer te zijn: de skill laat je visueel kiezen tussen stijlen in plaats van abstracte vragen te stellen. Ook kan hij een bestaande `.pptx` omzetten naar een webpresentatie en exporteren naar PDF.",
    wanneer=["Je geeft een talk of pitch en wilt iets dat opvalt.",
             "Je wilt een oude PowerPoint moderniseren."],
    voorbeelden=[("Maak een pitch van 8 slides voor mijn nieuwe app, met strakke animaties.", "Eén HTML-bestand dat je in de browser presenteert.")],
    install=tabs(
        cc_market("https://github.com/zarazhangrui/frontend-slides", "frontend-slides@frontend-slides"),
        manual("git clone https://github.com/zarazhangrui/frontend-slides.git ~/.claude/skills/frontend-slides")),
    tips=["Er is een beginnersvideo in de README van de repo."])

# ───────────────────────── CREATIEF ─────────────────────────
add(slug="remotion", name="Remotion", cat="creatief", icon="clapperboard",
    tagline="Leert Claude video's en animaties maken in code (React), lokaal en onbeperkt.",
    maker="Remotion (officieel van de makers)", werkt="Claude Code (+ Codex, Cursor en meer)", prijs="Skills gratis; Remotion zelf heeft een eigen licentie",
    bron="https://github.com/remotion-dev/skills",
    social="Tip van Bart Boonstra: *'Remotion is de skill die Claude leert om animaties te maken in code. Alle animaties in mijn video's zijn hiermee gebouwd.'*",
    wat="Remotion is een framework om video's te maken met React-code. De officiële Remotion-skills leren Claude de best practices: een project opzetten, animaties en overgangen, ondertitels, kaarten, multimedia, interactiviteit en renderen naar MP4. Je beschrijft wat je wilt zien, Claude schrijft de code en je rendert de video lokaal op je eigen computer.",
    wanneer=["Je maakt content voor social media en wilt animaties of infographics.",
             "Je wilt video's met ondertitels of data-visualisaties genereren.",
             "Je wilt een vaste video-template die je steeds hergebruikt."],
    voorbeelden=[("Maak een Remotion-video van 15 seconden, verticaal 1080x1920, waarin de vijf belangrijkste features van mijn app één voor één binnenvliegen.", "Een Remotion-project dat je rendert tot een MP4."),
                 ("Voeg geanimeerde ondertitels toe aan deze video.", "Een video met ondertitels in je eigen stijl.")],
    install=tabs(npx("npx skills add remotion-dev/skills"),
                 tab("Voorwaarden", "Je hebt Node.js nodig en een Remotion-project (`npx create-video@latest`). Check de [Remotion-licentie](https://www.remotion.dev/license): voor bedrijven boven een bepaalde omvang is een betaalde licentie nodig.")),
    tips=["Begin met de skill `remotion-best-practices`; die verwijst Claude naar de juiste deelskill."])

add(slug="algorithmic-art", name="Algorithmic Art", cat="creatief", icon="shapes",
    tagline="Generatieve kunst met p5.js: flow fields, deeltjessystemen en interactieve parameters.",
    maker="Anthropic (officieel)", werkt="Claude-app, Claude Code, API", prijs="Gratis (Apache 2.0)",
    bron="https://github.com/anthropics/skills/tree/main/skills/algorithmic-art",
    wat="Met deze skill maakt Claude kunst met code in p5.js, met een vaste 'seed' zodat je een mooi resultaat kunt reproduceren. Je krijgt schuifjes om parameters live te verkennen. Bedoeld voor origineel werk, niet om bestaande kunstenaars na te maken.",
    wanneer=["Je wilt een unieke achtergrond, wallpaper of visual.",
             "Je wilt spelen met generatieve kunst."],
    voorbeelden=[("Maak een flow field in de kleuren van de Nederlandse vlag met schuifjes voor dichtheid en snelheid.", "Een interactieve kunstpagina.")],
    install=official_example("algorithmic-art"), tips=[])

add(slug="slack-gif-creator", name="Slack GIF Creator", cat="creatief", icon="face-grin-stars",
    tagline="Maakt geanimeerde GIF's die precies voldoen aan de eisen van Slack.",
    maker="Anthropic (officieel)", werkt="Claude-app, Claude Code, API", prijs="Gratis (Apache 2.0)",
    bron="https://github.com/anthropics/skills/tree/main/skills/slack-gif-creator",
    wat="Een skill met kennis en hulpmiddelen om GIF's te maken die goed werken in Slack: de juiste afmetingen en bestandsgrootte, plus validatie en animatie-ideeën.",
    wanneer=["Je wilt een grappige GIF of custom emoji voor je team."],
    voorbeelden=[("Maak een GIF van een dansende tostiapparaat voor Slack.", "Een geoptimaliseerde GIF.")],
    install=official_example("slack-gif-creator"), tips=[])

# ───────────────────────── DENKEN ─────────────────────────
add(slug="superpowers", name="Superpowers", cat="denken", icon="bolt",
    tagline="Een complete werkmethode: brainstormen, plannen schrijven, test-first bouwen, systematisch debuggen en controleren.",
    maker="Jesse Vincent / obra (community)", werkt="Claude Code (+ Codex, Antigravity en meer)", prijs="Gratis (open source)",
    bron="https://github.com/obra/superpowers",
    social="Tip van Bart Boonstra: *'Superpowers laat Claude écht in stappen denken. Brainstormen en plannen wordt 10x scherper.'*",
    wat="Superpowers is een van de bekendste skillpakketten. Het is een complete ontwikkelmethode, opgebouwd uit losse skills die elkaar aanvullen: **brainstorming** (eerst samen het idee scherp krijgen), **writing-plans** en **executing-plans**, **test-driven-development**, **systematic-debugging**, **verification-before-completion** (eerst bewijzen dat iets werkt), code reviews vragen en ontvangen, werken met git worktrees en subagents. Een start-skill zorgt dat Claude ze ook echt gebruikt. Brainstorming werkt ook buiten software: voor een talk, een bedrijf of een verbouwing.",
    wanneer=["Je begint aan een nieuwe feature of een nieuw project.",
             "Claude springt te snel naar code en mist het grotere plaatje.",
             "Je zit vast met een bug en wilt een systematische aanpak."],
    voorbeelden=[("Ik wil een widget toevoegen aan mijn app. Laten we eerst brainstormen.", "Claude stelt eerst vragen, stelt ontwerpen voor en schrijft daarna een plan voordat hij code schrijft."),
                 ("De tests falen sinds de laatste update. Debug dit systematisch.", "Claude zoekt eerst de oorzaak en bewijst die, voordat hij iets repareert.")],
    install=tabs(
        cc_official("superpowers"),
        tab("Superpowers-marketplace", """
De eigen marketplace van de maker, met extra gerelateerde plugins:

```bash
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
```""")),
    tips=["Gebruik je meerdere tools (Claude Code én Codex)? Installeer Superpowers dan per tool apart."])

add(slug="grill-me", name="Grill Me & Handoff", cat="denken", icon="fire-flame-curved",
    tagline="Laat Claude je plan genadeloos ondervragen voordat hij begint, en vat lange chats samen om verder te gaan.",
    maker="Matt Pocock (community)", werkt="Claude Code (+ Cursor, Codex en andere agents)", prijs="Gratis (open source)",
    bron="https://github.com/mattpocock/skills",
    social="Viraal gegaan via o.a. 'I Tried 23 Viral Claude Skills' (Artificial Corner).",
    wat="Uit de populaire skillcollectie van Matt Pocock springen twee skills eruit. **Grill Me** is een 'meedogenloos interview': Claude vraagt door over je doelen, doelgroep, scope en wat er mis kan gaan, totdat je plan echt scherp is. **Handoff** vat een lang gesprek samen in een overdrachtsdocument, zodat je verder kunt in een nieuwe chat of met een andere agent zonder context kwijt te raken. De collectie bevat verder skills voor TDD, code reviews, specs, tickets en meer.",
    wanneer=["Je hebt een idee maar weet nog niet precies wat je wilt.",
             "Je gesprek wordt te lang en Claude begint dingen te vergeten."],
    voorbeelden=[("/grill-me Ik wil een app maken voor vrijwilligers in de wijk.", "Een reeks scherpe vragen, één voor één, tot alles helder is."),
                 ("/handoff", "Een compact overdrachtsdocument om in een nieuwe sessie te plakken.")],
    install=tabs(
        tab("Claude Code", """
De collectie staat in de officiële marketplace:

```bash
claude plugin install mattpocock-skills@claude-plugins-official
```"""),
        npx("npx skills@latest add mattpocock/skills", "\nKies in de installer welke skills je wilt en neem `setup-matt-pocock-skills` mee. Bijwerken: `npx skills@latest update`.")),
    tips=[])

add(slug="planning-with-files", name="Planning with Files", cat="denken", icon="list-check",
    tagline="Houdt een plan, bevindingen en voortgang bij in bestanden op schijf, zodat Claude nooit de draad kwijtraakt.",
    maker="OthmanAdi (community)", werkt="Claude Code (+ Codex, Cursor, Copilot en 70+ andere agents)", prijs="Gratis (open source)",
    bron="https://github.com/OthmanAdi/planning-with-files",
    wat="Bij lange taken vergeet een AI-agent soms waar hij was. Planning with Files lost dat op met drie bestanden: `task_plan.md`, `findings.md` en `progress.md`. Hooks voegen bij elke beurt de belangrijke planningscontext toe, en het plan overleeft zelfs een `/clear`. Daardoor kan Claude een groot project in stappen afwerken.",
    wanneer=["Je laat Claude een groot, meerstappig project doen.",
             "Je wilt kunnen terugzien wat er is gedaan en gevonden."],
    voorbeelden=[("Plan de migratie van mijn app naar een nieuwe iOS-versie met planning-with-files.", "Een plan op schijf dat Claude stap voor stap afwerkt en bijwerkt.")],
    install=tabs(cc_market("OthmanAdi/planning-with-files", "planning-with-files@planning-with-files"),
                 npx("npx skills add OthmanAdi/planning-with-files")),
    tips=["De hooks werken alleen in Claude Code (en andere agents met hooks), niet in de Claude-app."])

add(slug="debate", name="Debate Skills", cat="denken", icon="comments",
    tagline="Laat AI's met elkaar in debat gaan zodat je eerlijk, tegengesproken advies krijgt in plaats van een ja-knikker.",
    maker="biyachuev (community)", werkt="Claude Code (+ Codex CLI voor de debatten tussen twee modellen)", prijs="Gratis (open source)",
    bron="https://github.com/biyachuev/claude-debate-skills",
    social="Bart Boonstra noemt een 'Debate Skill' zijn favoriet: *'AI praat negen van de tien keer met je mee. Niet meer.'* Welke repo hij precies gebruikt, noemt hij niet in de post; deze is een goed gedocumenteerde variant.",
    wat="Deze collectie bevat drie skills. **strategy-debate**: Claude en Codex (OpenAI) bouwen los van elkaar een standpunt op, bekritiseren elkaar en komen tot een synthese. **creator-critic**: de ene genereert opties, de andere beoordeelt ze; deze werkt ook met alleen Claude. **options-challenge**: vergelijkt meerdere routes, test de afwegingen en rangschikt ze (vereist Codex). Omdat de modellen verschillende blinde vlekken hebben, komt er meer boven tafel dan bij één antwoord.",
    wanneer=["Je staat voor een strategische keuze en wilt geen ja-knikker.",
             "Je wilt ideeën (namen, prijzen, positionering) onder druk testen."],
    voorbeelden=[("/strategy-debate Topic: Moet ik mijn app gratis met advertenties of betaald aanbieden? Constraints: kleine doelgroep, solo-ontwikkelaar.", "Twee onderbouwde standpunten, onderlinge kritiek en een eindadvies."),
                 ("/creator-critic Creator: Claude. Critic: Claude. Finalizer: Claude. Log File: none. Brief: Bedenk namen voor een buurt-app.", "Opties, kritiek en een korte shortlist, alleen met Claude.")],
    install=tabs(
        tab("Claude Code", """
```bash
claude plugin install --source https://github.com/biyachuev/claude-debate-skills.git
```

Voor de debatten tussen twee modellen heb je ook de Codex CLI nodig:

```bash
npm install -g @openai/codex && codex login
```

Installeer daarna in Claude Code de Codex-plugin met `/install-plugin codex`."""),
        manual("git clone https://github.com/biyachuev/claude-debate-skills.git\ncd claude-debate-skills && ./install.sh   # maakt symlinks in ~/.claude/skills/")),
    tips=["Je vraag kan naar zowel Anthropic als OpenAI gaan: zet er geen gevoelige informatie in.",
          "Alleen Claude? Gebruik `creator-critic` met Claude in alle rollen."])

add(slug="discernment-nudge", name="Discernment Nudge", cat="denken", icon="circle-question",
    tagline="Voegt na belangrijk advies 2 à 3 slimme controlevragen toe, zodat je de aannames zelf checkt.",
    maker="Anthropic (officieel)", werkt="Claude-app, Claude Code, API", prijs="Gratis",
    bron="https://github.com/anthropics/skills/tree/main/skills/discernment-nudge",
    wat="Nadat Claude je advies, een plan, een schatting of een analyse heeft gegeven, stelt deze skill 2 à 3 korte vervolgvragen die precies op dat antwoord ingaan: welke feiten je moet checken, welke aannames er onder zitten en welke context mogelijk ontbreekt. Maximaal één keer per gesprek, dus niet irritant.",
    wanneer=["Je gebruikt Claude voor beslissingen en wilt kritisch blijven."],
    voorbeelden=[("Maak een begroting voor ons buurtfeest.", "De begroting, met daaronder vragen als 'Klopt het aantal bezoekers waar dit op is gebaseerd?'")],
    install=tabs(npx("npx skills add anthropics/skills --skill discernment-nudge"),
                 app_zip("anthropics/skills", "skills/discernment-nudge")),
    tips=[])

# ───────────────────────── ONTWIKKELING ─────────────────────────
add(slug="agent-skills-addy", name="Agent Skills (Addy Osmani)", cat="ontwikkeling", icon="diagram-project",
    tagline="Productieklare engineering-workflows: spec schrijven, taken opsplitsen, stap voor stap bouwen, testen en opleveren.",
    maker="Addy Osmani (community)", werkt="Claude Code (+ andere agents)", prijs="Gratis (open source)",
    bron="https://github.com/addyosmani/agent-skills",
    social="Viraal gegaan via o.a. 'I Tried 23 Viral Claude Skills' (Artificial Corner).",
    wat="Addy Osmani (Google Chrome) bundelde de werkwijzen en kwaliteitspoorten van senior engineers in zo'n 25 skills. Denk aan **spec-driven-development**, **planning-and-task-breakdown**, **incremental-implementation**, test-driven-development, code review, security, performance, documentatie en ADR's, CI/CD en lancering. Claude legt voortgang vast in bestanden, zodat werk consistent en controleerbaar blijft.",
    wanneer=["Je bouwt serieuze software met Claude Code.",
             "Je wilt dat Claude eerst een spec schrijft voordat hij bouwt."],
    voorbeelden=[("Schrijf eerst een spec voor de nieuwe zoekfunctie, splits die op in taken en bouw ze daarna één voor één.", "Een spec, een takenlijst en incrementele commits.")],
    install=tabs(cc_market("addyosmani/agent-skills", "agent-skills@addy-agent-skills"),
                 npx("npx skills add addyosmani/agent-skills          # alle skills\nnpx skills add addyosmani/agent-skills --list   # eerst bekijken")),
    tips=["Krijg je bij `/plugin install` een SSH-fout? Gebruik de HTTPS-URL: `/plugin marketplace add https://github.com/addyosmani/agent-skills.git`."])

add(slug="official-dev-plugins", name="Officiële dev-plugins", cat="ontwikkeling", icon="puzzle-piece",
    tagline="Anthropics eigen Claude Code-plugins: code review, feature-dev, commits, PR-review, security en hooks.",
    maker="Anthropic (officieel)", werkt="Claude Code", prijs="Gratis",
    bron="https://github.com/anthropics/claude-plugins-official",
    wat="In de officiële marketplace staan plugins die Anthropic zelf onderhoudt. Een greep:\n\n| Plugin | Wat het doet |\n| --- | --- |\n| `code-review` | Automatische PR-review met meerdere gespecialiseerde agents en een betrouwbaarheidsscore |\n| `feature-dev` | Complete feature-workflow: codebase verkennen, architectuur ontwerpen, kwaliteitscheck |\n| `commit-commands` | Snelle commando's om te committen, pushen en PR's te maken |\n| `pr-review-toolkit` | Review-agents voor comments, tests, foutafhandeling, types en vereenvoudiging |\n| `security-guidance` | Waarschuwt bij onveilige code (injectie, XSS, SSRF, hardcoded secrets en meer) |\n| `hookify` | Maakt eenvoudig hooks om ongewenst gedrag te voorkomen |\n| `claude-md-management` | Houdt je CLAUDE.md-bestanden actueel en goed |\n| `claude-code-setup` | Analyseert je codebase en stelt passende hooks, skills en MCP-servers voor |\n| `code-simplifier` | Maakt code helderder zonder gedrag te veranderen |\n| `playground` | Maakt interactieve HTML-playgrounds met live preview |\n| `ralph-loop` | Laat Claude in een lus doorwerken tot een taak echt af is |\n\nDaarnaast zijn er taal-plugins (LSP) voor o.a. Swift, TypeScript, Python, Kotlin en Rust.",
    wanneer=["Je werkt met Claude Code aan een echte codebase.", "Je wilt reviews en commits standaardiseren."],
    voorbeelden=[("/code-review", "Een review van je huidige PR met bevindingen en scores."),
                 ("/feature-dev Voeg dark mode toe aan de instellingen", "Een begeleide workflow van verkennen tot opleveren.")],
    install=tabs(cc_official("code-review", "\nVervang `code-review` door de plugin die je wilt, bijvoorbeeld `feature-dev`, `swift-lsp` of `security-guidance`.")),
    tips=["Ook de plugin `swift-lsp` is handig als je iOS-apps bouwt."])

add(slug="mcp-builder", name="MCP Builder", cat="ontwikkeling", icon="plug",
    tagline="Gids om zelf goede MCP-servers te bouwen in Python (FastMCP) of TypeScript.",
    maker="Anthropic (officieel)", werkt="Claude-app, Claude Code, API", prijs="Gratis (Apache 2.0)",
    bron="https://github.com/anthropics/skills/tree/main/skills/mcp-builder",
    wat="Met MCP (Model Context Protocol) koppel je Claude aan externe diensten via tools. Deze skill begeleidt Claude bij het bouwen van een MCP-server van hoge kwaliteit: goede tool-namen en beschrijvingen, foutafhandeling en testen, in Python (FastMCP) of Node/TypeScript.",
    wanneer=["Je wilt Claude koppelen aan een eigen API, zoals je Homey-app of een database."],
    voorbeelden=[("Bouw een MCP-server die de meldingen uit mijn eigen API als tool beschikbaar maakt.", "Een werkende MCP-server met tools en tests.")],
    install=official_example("mcp-builder"), tips=[])

add(slug="webapp-testing", name="Webapp Testing", cat="ontwikkeling", icon="vial",
    tagline="Test lokale webapps met Playwright: klikken, screenshots maken en browserlogs bekijken.",
    maker="Anthropic (officieel)", werkt="Claude Code (en Claude-app met code-uitvoering)", prijs="Gratis (Apache 2.0)",
    bron="https://github.com/anthropics/skills/tree/main/skills/webapp-testing",
    wat="Een toolkit waarmee Claude je lokale webapplicatie bedient via Playwright: pagina's openen, formulieren invullen, knoppen testen, screenshots maken en console-logs lezen om fouten op te sporen.",
    wanneer=["Je wilt controleren of je website of PWA werkt na een wijziging."],
    voorbeelden=[("Start de app op localhost:3000, test het inlogformulier en maak screenshots van elke stap.", "Een testverslag met screenshots en eventuele fouten.")],
    install=official_example("webapp-testing"), tips=[])

add(slug="claude-api", name="Claude API", cat="ontwikkeling", icon="server",
    tagline="Actuele naslag voor bouwen met de Claude API en SDK's: modellen, prijzen, tools, streaming en caching.",
    maker="Anthropic (officieel)", werkt="Claude Code, Claude-app, API", prijs="Gratis",
    bron="https://github.com/anthropics/skills/tree/main/skills/claude-api",
    wat="Deze skill zorgt dat Claude bij het bouwen van AI-toepassingen niet uit zijn geheugen werkt, maar de actuele documentatie gebruikt: model-ID's, prijzen, parameters, streaming, tool use, MCP, agents, prompt caching en migratie tussen modellen.",
    wanneer=["Je bouwt een app die de Claude API gebruikt."],
    voorbeelden=[("Voeg aan mijn app een functie toe die meldingen samenvat met de Claude API, met prompt caching.", "Code die de juiste, actuele API-aanroepen gebruikt.")],
    install=tabs(cc_market("anthropics/skills", "claude-api@anthropic-agent-skills"),
                 npx("npx skills add anthropics/skills --skill claude-api")),
    tips=[])

add(slug="vercel-agent-skills", name="Vercel Agent Skills", cat="ontwikkeling", icon="rocket",
    tagline="React- en Next.js-best practices, webdesign-richtlijnen en deployen naar Vercel.",
    maker="Vercel (officieel van de makers)", werkt="Claude Code (+ andere agents)", prijs="Gratis",
    bron="https://github.com/vercel-labs/agent-skills",
    wat="Vercel publiceert skills met hun eigen best practices: **react-best-practices**, **composition-patterns**, **react-native-skills**, **react-view-transitions**, **web-design-guidelines**, **writing-guidelines**, **deploy-to-vercel** en **vercel-optimize** (een audit op kosten, performance en caching).",
    wanneer=["Je bouwt met React, Next.js of React Native.", "Je host op Vercel."],
    voorbeelden=[("Review deze pagina op de web-design-guidelines.", "Een lijst met concrete verbeteringen."),
                 ("Deploy dit project naar Vercel.", "Een live preview-URL.")],
    install=tabs(npx("npx skills add vercel-labs/agent-skills\nnpx skills add vercel-labs/agent-skills --skill web-design-guidelines -a claude-code")),
    tips=["Op [skills.sh](https://skills.sh) vind je duizenden skills die je met dezelfde CLI installeert."])

add(slug="n8n-skills", name="n8n Skills", cat="ontwikkeling", icon="diagram-next",
    tagline="Expertkennis om foutloze n8n-workflows te bouwen via de n8n-MCP-server.",
    maker="czlonkowski (community)", werkt="Claude Code (met de n8n-mcp-server)", prijs="Gratis (open source)",
    bron="https://github.com/czlonkowski/n8n-skills",
    wat="Veertien samenwerkende skills, een router-skill en hooks die Claude leren hoe n8n echt werkt: expressies, nodes configureren, Code-nodes in JavaScript of Python, validatie en workflow-patronen. Bedoeld om samen te werken met de [n8n-mcp](https://github.com/czlonkowski/n8n-mcp)-server, zodat Claude workflows direct in je n8n kan bouwen.",
    wanneer=["Je automatiseert met n8n en wilt dat Claude workflows bouwt of repareert."],
    voorbeelden=[("Bouw een n8n-workflow die elke ochtend het weerbericht ophaalt en naar Telegram stuurt.", "Een gevalideerde workflow in je n8n.")],
    install=tabs(tab("Claude Code", "```bash\n/plugin install czlonkowski/n8n-skills\n```\n\nOf voeg de marketplace toe met `/plugin marketplace add czlonkowski/n8n-skills` en kies daarna via `/plugin`."),
                 manual("git clone https://github.com/czlonkowski/n8n-skills.git\ncp -r n8n-skills/skills/* ~/.claude/skills/")),
    tips=["Installeer eerst de n8n-mcp-server; zonder die server kan Claude niet bij je n8n."])

add(slug="terraform-skill", name="Terraform Skill", cat="ontwikkeling", icon="cloud",
    tagline="Best practices voor Terraform en OpenTofu: modules, testen, CI/CD en productieklare infrastructuur.",
    maker="Anton Babenko (community)", werkt="Claude Code (+ andere agents)", prijs="Gratis (open source)",
    bron="https://github.com/antonbabenko/terraform-skill",
    wat="Gemaakt door een bekende Terraform-expert. De skill helpt Claude bij het structureren van modules, het testen van infrastructuurcode, het opzetten van CI/CD en het schrijven van veilige productiecode, voor AWS, Azure en GCP.",
    wanneer=["Je beheert infrastructuur als code."],
    voorbeelden=[("Zet een Terraform-module op voor een statische website op AWS met tests.", "Een nette module met testopzet.")],
    install=tabs(cc_market("antonbabenko/agent-plugins", "terraform-skill@antonbabenko")),
    tips=[])

# ───────────────────────── CONTENT ─────────────────────────
add(slug="humanizer", name="Humanizer", cat="content", icon="user-pen",
    tagline="Herschrijft AI-achtige tekst zodat hij klinkt alsof een mens hem schreef, zonder de inhoud te veranderen.",
    maker="blader (community)", werkt="Claude Code, Claude-app (+ Codex en meer)", prijs="Gratis (open source)",
    bron="https://github.com/blader/humanizer",
    social="De meest virale skill van dit moment volgens Artificial Corner. Let op: er circuleren kopieën die er identiek uitzien, installeer alleen vanaf de officiële repo.",
    wat="Humanizer is gebaseerd op Wikipedia's lijst *Signs of AI writing*, de gids die Wikipedia-redacteuren gebruiken om AI-tekst te herkennen. De skill haalt typische AI-trucjes weg: 'niet X maar Y'-contrasten, pakkende one-liners aan het eind, gedwongen drietallen, overal gedachtestreepjes, opgeblazen claims, verkooptaal, typische AI-woorden en vetgedrukte labels. Je boodschap blijft gelijk, alleen de toon wordt menselijker.",
    wanneer=["Je post op LinkedIn of Instagram en wilt niet dat het naar AI ruikt.",
             "Je wilt een concept van Claude laten 'ontdoen' van AI-tics."],
    voorbeelden=[("/humanizer Herschrijf deze LinkedIn-post zodat hij klinkt als mij.", "Dezelfde post, maar natuurlijker en zonder AI-patronen.")],
    install=tabs(cc_market("blader/humanizer", "humanizer@humanizer", "\nDe plugin luistert naar `/humanizer:humanizer` en vraagt Claude Code 2.1.142 of nieuwer."),
                 npx("npx skills add blader/humanizer --global --agent claude-code"),
                 app_zip("blader/humanizer", "humanizer (de hoofdmap van de repo, met SKILL.md)")),
    tips=["Check altijd of je de echte repo hebt: github.com/blader/humanizer."])

add(slug="marketingskills", name="Marketing Skills", cat="content", icon="chart-line",
    tagline="Een grote collectie marketingskills: copywriting, social, contentstrategie, CRO, SEO en marketingpsychologie.",
    maker="Corey Haines (community)", werkt="Claude Code (+ Codex, Cursor en meer)", prijs="Gratis (MIT)",
    bron="https://github.com/coreyhaines31/marketingskills",
    wat="Een collectie voor marketeers en founders. Onder andere **copywriting** (pagina's, posts en advertenties), **social** (content voor zes platforms, waaronder Instagram en TikTok), **content-strategy** (van doel naar contentplan en kalender), **marketing-psychology** (overtuigingsprincipes, hooks en call-to-actions), plus conversie-optimalisatie, SEO en analytics.",
    wanneer=["Je wilt een landingspagina of advertentie die converteert.", "Je wilt een contentkalender voor je app."],
    voorbeelden=[("Schrijf drie varianten van de App Store-beschrijving voor mijn app, met verschillende hooks.", "Drie onderbouwde varianten."),
                 ("Maak een contentplan voor 4 weken Instagram voor de lancering van mijn app.", "Een kalender met onderwerpen, formats en hooks.")],
    install=tabs(cc_market("coreyhaines31/marketingskills", "marketing-skills", "\n`/plugin` werkt alleen in een interactieve Claude Code-sessie."),
                 npx("npx skills add coreyhaines31/marketingskills -a claude-code")),
    tips=[])

add(slug="instagram-agent", name="Instagram Agent", cat="content", icon="camera-retro",
    tagline="Dertien skills die een Instagram-account runnen: Reels met scoorbare hooks, captions, carrousels, stories en DM's.",
    maker="Jake Schincariol (community)", werkt="Claude Code, Claude-app", prijs="Gratis (MIT), geen API-sleutel nodig",
    bron="https://github.com/Jakeschincariol/instagram-agent-skill",
    social="Veel gedeeld door Instagram-creators; diverse blogs schrijven er complete installatiegidsen over.",
    wat="Een pakket van dertien skills (`ig-reel`, `ig-caption`, `ig-carousel`, `ig-story`, `ig-viral`, `ig-plan`, `ig-audit`, `ig-profile`, `ig-dm`, `ig-reply`, `ig-comment`, `ig-repurpose` en `ig-human`). Ze schrijven Reels op basis van 26 hook-formules en geven de hook een score, onderzoeken wat viraal gaat, linten je captions en halen AI-taal weg. Je hoeft niets te koppelen.",
    wanneer=["Je wilt consequent posten voor je app of organisatie.", "Je wilt betere hooks en captions."],
    voorbeelden=[("Schrijf een Reel-script van 30 seconden over 'Waarom je buren je beste beveiliging zijn' met een scorende hook.", "Een script met hook-score en caption."),
                 ("Audit mijn Instagram-profiel en geef 5 verbeterpunten.", "Een profielaudit.")],
    install=tabs(cc_market("Jakeschincariol/instagram-agent-skill", "instagram-agent"),
                 manual("git clone https://github.com/Jakeschincariol/instagram-agent-skill.git\ncp -r instagram-agent-skill/skills/ig-* ~/.claude/skills/")),
    tips=[])

add(slug="instagram-carousel", name="Instagram Carousel", cat="content", icon="images",
    tagline="Pixel-perfecte Instagram-carrousels in je eigen huisstijl, export naar PNG en PDF.",
    maker="Jeevan Bavandla (community)", werkt="Claude Code, Claude-app", prijs="Gratis (MIT)",
    bron="https://github.com/jeevanbavandla/instagram-carousel-skill",
    wat="Bij het eerste gebruik stel je eenmalig je merk in (naam, handle, foto, accentkleur, stijl). Daarna maakt Claude carrousels in vier stijlen: Bold Impact, Tweet Post, Clean Editorial en Product Showcase, met voortgangsbalk, pijltjes en een CTA-slide. Exporteren kan als PNG en PDF.",
    wanneer=["Je wilt snel carrousels maken zonder Canva."],
    voorbeelden=[("Maak een carrousel van 6 slides: '5 tips voor een veiligere wijk'.", "Zes slides in je huisstijl, klaar om te posten.")],
    install=tabs(npx("npx skills add jeevanbavandla/instagram-carousel-skill -g"),
                 tab("Claude-app", "De repo heeft een aparte map `claude-ai` met instructies om de skill in de Claude-app te gebruiken (bestand plakken, ±5 minuten).")),
    tips=[])

add(slug="last30days", name="Last 30 Days", cat="content", icon="magnifying-glass-chart",
    tagline="Onderzoekt wat mensen de afgelopen 30 dagen écht zeggen over een onderwerp: Reddit, X, YouTube, TikTok en meer.",
    maker="mvanhorn (community)", werkt="Claude Code (+ andere agents)", prijs="Gratis (open source)",
    bron="https://github.com/mvanhorn/last30days-skill",
    wat="In plaats van redactionele artikelen zoekt deze skill naar wat **mensen** zeggen: posts en engagement van Reddit, X, YouTube, TikTok, Hacker News, Polymarket, GitHub en het web, uit de laatste 30 dagen. Met een `doctor`-check zie je welke bronnen werken.",
    wanneer=["Je wilt weten wat er nu speelt rond een onderwerp of concurrent.", "Je zoekt inspiratie voor actuele content."],
    voorbeelden=[("/last30days Claude skills", "Een overzicht van wat er de afgelopen maand over Claude-skills gezegd is, met bronnen.")],
    install=tabs(cc_market("mvanhorn/last30days-skill", "last30days"),
                 npx("npx skills add mvanhorn/last30days-skill -g")),
    tips=["Installeer niet via beide methodes tegelijk; Claude Code ontdubbelt dat niet."])

add(slug="claude-seo", name="Claude SEO", cat="content", icon="ranking-star",
    tagline="Complete SEO-audit: techniek, Core Web Vitals, schema.org, lokale SEO en zichtbaarheid in AI-zoekmachines.",
    maker="Agrici Daniel (community)", werkt="Claude Code", prijs="Gratis (MIT)",
    bron="https://github.com/AgriciDaniel/claude-seo",
    wat="Een SEO-plugin met tientallen subskills en gespecialiseerde agents: technische SEO, Core Web Vitals, E-E-A-T, schema.org, AI-zoekmachines (GEO), lokale SEO, e-commerce en internationale SEO.",
    wanneer=["Je wilt je website laten doorlichten voordat je hem promoot."],
    voorbeelden=[("Doe een volledige SEO-audit van https://jouwwebsite.nl", "Een rapport met prioriteiten en concrete fixes.")],
    install=tabs(cc_market("AgriciDaniel/claude-seo", "claude-seo@agricidaniel-claude-seo")),
    tips=[])

# ───────────────────────── KENNIS ─────────────────────────
add(slug="claude-mem", name="Claude-Mem", cat="kennis", icon="memory",
    tagline="Geeft Claude Code een blijvend geheugen: wat in eerdere sessies gebeurde, komt automatisch terug.",
    maker="thedotmack (community)", werkt="Claude Code (+ andere agents)", prijs="Gratis open source; de gehoste geheugendienst heeft 30 dagen gratis proef, daarna je eigen abonnement of API-sleutel",
    bron="https://github.com/thedotmack/claude-mem",
    wat="Claude-Mem is een 'persistent memory compression system'. Via hooks legt het vast wat er in je sessies gebeurt, comprimeert het en voegt relevante herinneringen toe aan nieuwe sessies. Er is een lokale webviewer om je geheugen te doorzoeken. Na installatie vraagt het om in te loggen via een e-mail-link.",
    wanneer=["Je werkt lang aan hetzelfde project en wilt niet steeds opnieuw context geven."],
    voorbeelden=[("(gewoon verder werken)", "Claude weet in een nieuwe sessie nog welke beslissingen en bugfixes eerder zijn gedaan.")],
    install=tabs(tab("Installer (aanbevolen)", "```bash\nnpx claude-mem install\n```\n\nDe installer zet alles klaar en vraagt je daarna in te loggen via een e-maillink (geen creditcard). Daarna kies je je geheugen-provider: de claude-mem observer (30 dagen gratis proef), een eigen OpenRouter- of Gemini-sleutel, of je Anthropic-abonnement."), cc_market("thedotmack/claude-mem", "claude-mem")),
    tips=["Lees de privacy-informatie in de repo: standaard wordt de gehoste opslag gebruikt."])

add(slug="claudeception", name="Claudeception", cat="kennis", icon="infinity",
    tagline="Laat Claude Code zelf nieuwe skills schrijven van wat hij tijdens het werk ontdekt.",
    maker="blader (community)", werkt="Claude Code", prijs="Gratis (open source)",
    bron="https://github.com/blader/Claudeception",
    wat="Elke sessie begint een AI-agent vanaf nul. Heeft Claude een uur een obscure fout opgelost, dan ben je die kennis de volgende keer kwijt. Claudeception lost dat op: als Claude iets niet-voor-de-hand-liggends ontdekt (een workaround, debugtruc of projectpatroon), slaat hij het op als nieuwe skill. Bij een vergelijkbaar probleem wordt die skill automatisch geladen.",
    wanneer=["Je loopt vaak tegen dezelfde soort problemen aan.", "Je wilt dat je setup slimmer wordt naarmate je meer werkt."],
    voorbeelden=[("/claudeception", "Claude bekijkt de sessie en maakt er waar zinvol een nieuwe skill van."),
                 ("Sla dit op als skill.", "Een nieuwe SKILL.md in je skills-map.")],
    install=tabs(manual("git clone https://github.com/blader/Claudeception.git ~/.claude/skills/claudeception", "\nOptioneel: kopieer de activator-hook naar `~/.claude/hooks/` (zie de README).")),
    tips=[])

add(slug="obsidian-skills", name="Obsidian Skills", cat="kennis", icon="note-sticky",
    tagline="Officiële skills van de Obsidian-maker: notities, Bases, JSON Canvas en de Obsidian CLI.",
    maker="Steph Ango / kepano (maker van Obsidian)", werkt="Claude Code (+ Codex, OpenCode)", prijs="Gratis",
    bron="https://github.com/kepano/obsidian-skills",
    wat="Skills om met je Obsidian-vault te werken: **obsidian-markdown** (de Obsidian-variant van Markdown), **obsidian-bases**, **json-canvas**, **obsidian-cli** (notities lezen, maken en doorzoeken via de CLI) en **defuddle** (webpagina's schoon binnenhalen).",
    wanneer=["Je gebruikt Obsidian als tweede brein."],
    voorbeelden=[("Maak van de notulen van vandaag een notitie in mijn vault met links naar de betrokken projecten.", "Een nette Obsidian-notitie met [[links]].")],
    install=tabs(cc_market("kepano/obsidian-skills", "obsidian@obsidian-skills"),
                 npx("npx skills add https://github.com/kepano/obsidian-skills")),
    tips=["Wil je diagrammen in Obsidian? Kijk naar [Axton's Obsidian Visual Skills](https://github.com/axtonliu/axton-obsidian-visual-skills) voor Excalidraw, Mermaid en Canvas."])

# ───────────────────────── ZAKELIJK ─────────────────────────
KWP = [("productivity", "Productiviteit", "Taken, agenda's, dagelijkse workflows en persoonlijke context"),
       ("sales", "Sales", "Prospects onderzoeken, calls voorbereiden, pipeline, outreach en battlecards"),
       ("customer-support", "Klantenservice", "Tickets triëren, antwoorden opstellen, escalaties en kennisbankartikelen"),
       ("product-management", "Productmanagement", "Specs, roadmaps, gebruikersonderzoek en stakeholder-updates"),
       ("marketing", "Marketing", "Content, campagnes, merkstem, concurrentie en rapportages"),
       ("legal", "Juridisch", "Contracten reviewen, NDA's triëren, compliance en risico's"),
       ("finance", "Finance", "Journaalposten, afstemmingen, jaarrekeningen en audits"),
       ("data", "Data", "SQL, statistiek, dashboards en validatie"),
       ("design", "Design", "Design-kritiek, toegankelijkheid, handoff, UX-copy en onderzoek"),
       ("engineering", "Engineering", "Architectuur, reviews, debuggen, incidenten en standups"),
       ("human-resources", "HR", "Werving, onboarding, beoordelingen en beleid"),
       ("operations", "Operations", "Processen, risico's, runbooks en statusrapporten"),
       ("enterprise-search", "Zoeken in de organisatie", "Eén zoekvraag over mail, chat, documenten en wiki's"),
       ("small-business", "Mkb / kleine ondernemers", "Facturen najagen, cashflow, social content, offertes en meer"),
       ("bio-research", "Bio-onderzoek", "Literatuur, genomics en preklinisch onderzoek")]
add(slug="knowledge-work-plugins", name="Rol-plugins van Anthropic", cat="zakelijk", icon="briefcase",
    tagline="Kant-en-klare pakketten met skills, commando's en koppelingen per functie: sales, finance, legal, marketing en meer.",
    maker="Anthropic (officieel)", werkt="Claude-app (desktop), Claude Code", prijs="Gratis (open source)",
    bron="https://github.com/anthropics/knowledge-work-plugins",
    wat="Anthropic heeft per functie een plugin gemaakt. Elke plugin bundelt **skills** (domeinkennis die Claude automatisch gebruikt), **commando's** (zoals `/sales:call-prep` of `/data:write-query`) en **connectors** naar de tools van die rol (Slack, HubSpot, Notion, Jira, Snowflake…). Ze zijn bedoeld als startpunt: pas ze aan met je eigen termen, processen en tools.\n\n| Plugin | Waarvoor |\n| --- | --- |\n" + "\n".join(f"| `{a}` | **{b}**: {c} |" for a, b, c in KWP),
    wanneer=["Je wilt Claude als specialist voor een bepaalde rol inzetten.", "Je wilt dat je team consistente uitkomsten krijgt."],
    voorbeelden=[("/sales:call-prep Gesprek met een gemeente over een nieuwe buurt-app", "Een gespreksvoorbereiding met achtergrond en vragen."),
                 ("/small-business:invoice-chase", "Overzicht van openstaande facturen met conceptherinneringen.")],
    install=tabs(
        tab("Claude-app", "Installeer de plugins in de Claude-desktopapp via [claude.com/plugins](https://claude.com/plugins/). Ze activeren zichzelf; skills gaan automatisch aan en de commando's verschijnen in je sessie."),
        tab("Claude Code", """
```bash
claude plugin marketplace add anthropics/knowledge-work-plugins
claude plugin install sales@knowledge-work-plugins
```

Vervang `sales` door de plugin die je wilt.""")),
    tips=["Gebruik de plugin `cowork-plugin-management` om zelf een plugin voor jouw rol te maken of aan te passen."])

# ───────────────────────── SECURITY ─────────────────────────
add(slug="trail-of-bits", name="Trail of Bits Security", cat="security", icon="user-shield",
    tagline="Tientallen professionele security-skills van een bekend beveiligingsbedrijf: audits, Semgrep, fuzzing en supply chain.",
    maker="Trail of Bits", werkt="Claude Code (+ Codex)", prijs="Gratis (open source)",
    bron="https://github.com/trailofbits/skills",
    wat="Trail of Bits is een gerenommeerd securitybedrijf. Hun marketplace bevat skills en plugins voor security-analyse: differentiële reviews, statische analyse, Semgrep-regels schrijven, supply-chain-risico's, onveilige standaardinstellingen, property-based testing, mutatietesten, varianten van kwetsbaarheden zoeken en meer.",
    wanneer=["Je wilt je eigen code (bijvoorbeeld een app met gebruikersdata) laten doorlichten."],
    voorbeelden=[("Controleer mijn dependencies op supply-chain-risico's.", "Een risico-overzicht per pakket.")],
    install=tabs(tab("Claude Code", "```bash\n/plugin marketplace add trailofbits/skills\n```\n\nKies daarna via `/plugin` welke plugins je wilt installeren.")),
    tips=["Gebruik deze skills alleen op code en systemen waarvoor je toestemming hebt."])

add(slug="scientific-skills", name="Scientific Skills", cat="security", icon="flask",
    tagline="Een bibliotheek met 170+ wetenschappelijke skills: biologie, chemie, geneeskunde, natuurkunde en data-analyse.",
    maker="K-Dense (community)", werkt="Claude Code (+ Cursor, Codex en meer)", prijs="Gratis (open source)",
    bron="https://github.com/K-Dense-AI/scientific-agent-skills",
    wat="Een collectie van ruim 170 skills voor onderzoek: biologie, chemie, geneeskunde, natuurkunde, techniek, aardwetenschappen, data-analyse en wetenschappelijke communicatie. Volgt de open Agent Skills-standaard.",
    wanneer=["Je doet (hobby)onderzoek of data-analyse met wetenschappelijke bronnen."],
    voorbeelden=[("Analyseer deze meetdata en maak een publicatieklare grafiek met uitleg.", "Analyse en grafiek volgens wetenschappelijke conventies.")],
    install=tabs(npx("npx skills add K-Dense-AI/scientific-agent-skills"),
                 manual("git clone https://github.com/K-Dense-AI/scientific-agent-skills.git ~/.agents/skills/scientific-agent-skills")),
    tips=[])

# ───────────────────────── BOUWEN ─────────────────────────
add(slug="skill-creator", name="Skill Creator", cat="bouwen", icon="hammer",
    tagline="De skill om skills te maken: opzetten, verbeteren, testen met evals en de beschrijving optimaliseren.",
    maker="Anthropic (officieel)", werkt="Claude-app, Claude Code, API", prijs="Gratis (Apache 2.0)",
    bron="https://github.com/anthropics/skills/tree/main/skills/skill-creator",
    wat="Skill Creator begeleidt je bij het maken van een eigen skill: wat moet hij doen, wanneer moet hij afgaan, welke scripts of voorbeelden horen erbij. Daarna test hij de skill met evals, meet hij prestaties (ook met varianties) en optimaliseert hij de beschrijving zodat Claude hem op het juiste moment kiest.",
    wanneer=["Je merkt dat je Claude steeds dezelfde instructies geeft.", "Je bestaande skill gaat niet (of te vaak) af."],
    voorbeelden=[("Maak een skill van mijn vaste werkwijze voor het publiceren van een app-update.", "Een complete skillmap met SKILL.md, klaar om te uploaden."),
                 ("Mijn skill wordt nooit gebruikt. Verbeter de beschrijving en test het.", "Een verbeterde beschrijving met testresultaten.")],
    install=tabs(app_builtin(), cc_official("skill-creator"), npx("npx skills add anthropics/skills --skill skill-creator")),
    tips=["In de Claude-app kun je ook gewoon zeggen: 'maak hier een skill van'."])

add(slug="writing-skills", name="Writing Skills (Superpowers)", cat="bouwen", icon="pen-ruler",
    tagline="De Superpowers-aanpak om skills te schrijven en te testen, net als code.",
    maker="obra (community)", werkt="Claude Code", prijs="Gratis (open source)",
    bron="https://github.com/obra/superpowers/tree/main/skills/writing-skills",
    wat="Onderdeel van [Superpowers](../denken/superpowers.md). Deze skill behandelt het schrijven van skills als softwareontwikkeling: eerst testen of Claude zonder de skill de fout maakt, dan de skill schrijven en daarna controleren of hij het gedrag echt verandert.",
    wanneer=["Je wilt skills die aantoonbaar werken."],
    voorbeelden=[("Schrijf een skill die ervoor zorgt dat je altijd eerst de tests draait voor een commit.", "Een geteste skill.")],
    install=tabs(cc_official("superpowers", "\nWriting Skills zit in het Superpowers-pakket.")),
    tips=[])

add(slug="template", name="Skill-template & specificatie", cat="bouwen", icon="file-code",
    tagline="Het officiële sjabloon en de open Agent Skills-specificatie als startpunt.",
    maker="Anthropic / agentskills.io", werkt="Alle agents die de standaard ondersteunen", prijs="Gratis",
    bron="https://github.com/anthropics/skills/tree/main/template",
    wat="In de officiële repo staat een minimaal sjabloon en de specificatie van de open **Agent Skills**-standaard ([agentskills.io](https://agentskills.io)). Die standaard wordt inmiddels door tientallen agents ondersteund, dus een skill die je één keer schrijft werkt in Claude Code, Codex, Cursor en meer.",
    wanneer=["Je wilt zelf een skill vanaf nul opzetten."],
    voorbeelden=[("Maak met het officiële template een skill 'wijkraad-notulen'.", "Een map met een geldige SKILL.md.")],
    install=tabs(tab("Starten", "Volg de stappen in [Je eigen skill maken](../../basis/eigen-skill-maken.md).")),
    tips=[])


from data2 import NEWCATS, S2
CATS += NEWCATS
S += S2
