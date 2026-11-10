import json

def make_pt_table(headers, rows):
    import random
    r = random.randint(1000, 9999)
    tbl = {
        "_type": "table",
        "_key": f"tbl_{r}",
        "hasHeaderRow": True,
        "rows": []
    }
    h_row = {"_type": "tableRow", "_key": f"tr_h_{r}", "cells": []}
    for j, h in enumerate(headers):
        h_row["cells"].append({
            "_type": "tableCell",
            "_key": f"th_{r}_{j}",
            "isHeader": True,
            "content": [{"_type": "span", "_key": f"sh_{r}_{j}", "text": h, "marks": []}]
        })
    tbl["rows"].append(h_row)

    for i, row in enumerate(rows):
        d_row = {"_type": "tableRow", "_key": f"tr_{r}_{i}", "cells": []}
        for j, val in enumerate(row):
            d_row["cells"].append({
                "_type": "tableCell",
                "_key": f"td_{r}_{i}_{j}",
                "isHeader": False,
                "content": [{"_type": "span", "_key": f"sd_{r}_{i}_{j}", "text": val, "marks": []}]
            })
        tbl["rows"].append(d_row)
    return tbl

with open("scripts/seed/uploaded_content.json", "r", encoding="utf-8") as f:
    up = json.load(f)

# ==============================================================================
# 1. RESTORE BLOG HUB (/blog)
# ==============================================================================
t1_blog_topics = make_pt_table(
    ["Category", "What it covers", "Typical read"],
    [
        ["powder coating basics", "How the finish works, how long it lasts, myths", "5–8 min"],
        ["powder coating materials guide", "Which metals and powders work together", "6–9 min"],
        ["powder coating finishes guide", "Colour systems, metallics, gloss, texture", "4–6 min"],
        ["powder coating standards and testing", "Thickness, test methods, certifications", "7–10 min"],
        ["powder coating comparisons", "How it compares with other metal finishes", "6–8 min"],
        ["powder coating applications", "Parts and industries, machinery to gates", "5–7 min"],
        ["powder coating cost and planning", "Budgets, prep before drop-off, questions", "5–8 min"]
    ]
)

t2_blog_which_guide = make_pt_table(
    ["Your situation", "Start with", "Then read"],
    [
        ["New to the finish", "What Is Powder Coating?", "How Long Does It Last?"],
        ["Choosing a metal", "What Metals Can Be Coated?", "Epoxy vs Polyester vs Hybrid"],
        ["Picking a colour", "RAL Colour Matching", "Metallic Finishes Explained"],
        ["Writing a specification", "ASTM Standards", "Thickness (Mil Rating) Guide"],
        ["Comparing finishes", "Powder Coating vs Wet Paint", "Powder Coating vs Galvanizing"],
        ["Budgeting a job", "Cost in Ontario", "How to Prepare Parts"]
    ]
)

t3_blog_accuracy = make_pt_table(
    ["Check", "What it confirms", "When"],
    [
        ["Source check", "Facts match ASTM methods or data sheets", "Before publishing"],
        ["Shop check", "Advice matches real jobs", "Before publishing"],
        ["Owner review", "Nothing unconfirmed goes live", "Every post"],
        ["Date review", "Content is still current", "Annually"]
    ]
)

t4_blog_industries = make_pt_table(
    ["Industry page", "Most useful reading"],
    [
        ["powder coating for metal fabricators", "Surface prep tips and weld cleanup before drop-off"],
        ["powder coating for manufacturers", "Thickness and batch quality checks"],
        ["powder coating for machine shops", "Masking threads and tight tolerances"],
        ["powder coating for contractors", "Durability advice for railings, gates and steel"],
        ["powder coating for food processing equipment", "Finishes for washdown areas"],
        ["agricultural equipment powder coating", "Keeping rust off field equipment"],
        ["powder coating for municipalities", "Bollards, playgrounds and public metalwork"]
    ]
)

t5_blog_comparison = make_pt_table(
    ["Feature", "Our articles", "Data sheets", "Sales pages"],
    [
        ["Written for", "People comparing options", "Specifiers checking one powder", "Buyers being sold to"],
        ["Covers", "Choices, trade-offs, steps", "One product's test values", "One company's offer"],
        ["Best used for", "Learning and planning", "Final specification", "Contact details"]
    ]
)

t6_blog_projects = make_pt_table(
    ["Project card", "What it shows"],
    [
        ["Conveyor Frame for an Automotive Plant", "Prep and coverage on a welded production frame"],
        ["Automation Line Frame", "Masking mounting plates and ground points"],
        ["Robotic Base", "Curing thick steel to part temperature"]
    ]
)

up["pages"]["blog"] = {
    "meta_title": "Powder Coating Guides | Expert Answers | Koojo",
    "meta_desc": "Powder coating guides from Koojo's shop team: 30+ free articles in 7 topics on prep, finishes, standards, comparisons and planning. Start reading.",
    "primary_kw": "powder coating guides",
    "h1": "Powder Coating Guides for Buyers, Engineers and Makers",
    "summary": "Powder Coating Guides for Buyers, Engineers and Makers",
    "body": [
        "Powder coating guides from Koojo Custom Powder Coating answer the questions customers ask us every day, in plain-language explanations built on shop-floor experience. Since 2012 we have coated more than 10,000 items in Milton, and these articles share what that work has taught us.",
        "More than 30 free articles sit in seven topic categories, from how the finish works to planning a first order. Use the jump links below or start with the topic closest to your question. Most reads take under ten minutes, and each one is written and checked by our own production team.",
        "30+ Articles · 7 Topics · Written by Our Production Team · Owner-Reviewed · Since 2012 · 10,000+ Items · 5.0 ★ Google Rating",
        "## What Are Powder Coating Guides?",
        "They are short, practical articles that explain one question at a time, written by the people who prepare, coat and inspect parts every day. Each one gives a direct answer first, then the detail and reasons behind it.",
        "Our powder coating blog works as a free knowledge base. Beginner guides explain the basics without jargon, technical articles cover standards explained step by step, and buyer's guides help you compare suppliers. Homeowners and hobbyists read the same pages as engineers and buyers, because a clear answer works for both. Every powder coating guide links to the next logical question.",
        "## What Our Guides Cover: Topics and Depth",
        "Seven topic categories cover the full picture: basics, metals, finishes, testing, comparisons, real-world uses and planning. The table shows what each category covers and the typical reading time, so you can plan your time.",
        t1_blog_topics,
        "Metal substrates, finish selection, colour choices and corrosion protection each have their own posts, with more powder coating guides added as new questions reach us from customers and suppliers. Short how-to articles sit beside longer reference posts, and the planning category helps with [project planning](/blog/categories/cost-planning) before you request a price for any job.",
        "## How Our Powder Coating Guides Are Made",
        "Every article follows the same eight steps, from choosing the question to updating the page later. That process keeps the advice accurate, consistent and grounded in real jobs rather than rewritten web content.",
        [
            "Question Selection: Topics come from real questions asked at our counter, by phone or in quote requests.",
            "Shop Research: We check how the question plays out on actual parts, using job records and photos.",
            "Drafting: A production team member drafts each of these guides in plain language, answer first.",
            "Technical Check: Claims are checked against ASTM methods and powder makers' data sheets.",
            "Owner Review: The owner reviews every draft and removes anything that cannot be confirmed.",
            "Publishing: Each post shows an author, a reviewer and an updated date.",
            "Internal Linking: Each powder coating guide links to related articles and to the service page it supports.",
            "Updating: Content is updated regularly when methods or standards change, and the date changes too."
        ],
        "## Which Article Should You Read First?",
        "It depends on where you are in the project. Match your situation to a starting article in the table, then follow its links; most readers need two or three posts, about 20 to 30 minutes in all.",
        t2_blog_which_guide,
        "This learning path works for most readers. Our most-read articles sit in the middle column, and comparison articles come next once our guides have covered the basics.",
        "## How We Check Every Article for Accuracy",
        "Every claim is checked before publishing and again at each update. The table lists the four checks, what each one confirms and when it runs, so you know how much weight to give the advice.",
        t3_blog_accuracy,
        "These editorial standards make every post fact-checked content. Spot something out of date in these guides? Tell us and we will correct it.",
        "## Articles by Industry and Part",
        "Industry applications have their own group of posts, and each industry page links to the reading that matters most for that sector. Choose your sector below to see both the advice and the matching service.",
        t4_blog_industries,
        "Fabricators and contractors use these cards the most, for surface prep tips and durability advice, because our guides for their work sit next to the service details.",
        "## Our Guides vs Data Sheets vs Sales Pages",
        "Data sheets give one product's numbers and sales pages promote one company, while articles like ours explain the choices behind both. The table below shows which source suits which kind of question.",
        t5_blog_comparison,
        "Use the data sheet to confirm the final powder, and our articles to understand why it was chosen.",
        "## See the Advice in Practice: Recent Projects",
        "Three recent case studies show the advice from these guides on real parts, each with specs, photos and test readings. Open one to see prep, powder and cure decisions explained on an actual job.",
        t6_blog_projects,
        "Every finished job is on our [powder coating projects page](/projects).",
        "## What the Articles Cost and How Long They Take",
        "Every article is free, with no sign-up, and most take five to ten minutes to read. New posts are added as fresh questions reach us, and older ones are reviewed so the advice stays current.",
        "For the price of a real job, read our Ontario guide to [powder coating cost](/post/how-much-does-powder-coating-cost-ontario). Lead times for actual orders, including the 48 hour standard turnaround, are confirmed with each quote, not in our guides. Where a powder coating guide mentions typical timing, treat it as general guidance and check your own dates with us before you plan around them.",
        "## How to Go From Reading to a Quote",
        "Once our powder coating guides have answered your questions, send photos, sizes, quantity and the finish you want. We reply with prep, powder, price and timing, Monday to Friday, 7 AM to 5 PM.",
        "Request a [powder coating quote](/get-a-quote) online or call (905) 876-7060.",
        "## Still Have a Question?",
        "If our guides have not answered it, ask us directly. Call (905) 876-7060 or send photos and sizes through the [quote form](/get-a-quote), and a member of our production team will reply with expert answers. Our office is open Monday to Friday, 7 AM to 5 PM."
    ],
    "faqs": [
        ["Are the articles free to read?", "Yes. There is no sign-up, and any page can be shared with your team or supplier."],
        ["Who writes them?", "Members of our production team write each post, and the owner reviews it before publishing."],
        ["How often are these guides updated?", "Posts are reviewed when methods or standards change, and each shows its last updated date."],
        ["Can I suggest a topic?", "Yes. Call (905) 876-7060 or email sales@koojopowdercoating.com, and we may turn it into a new post."],
        ["Can I ask about my own part?", "Of course. Send photos and sizes for an answer specific to your part."]
    ]
}

# ==============================================================================
# 2. RESTORE AUTOMATION LINE FRAME (/projects/automation-line-frame)
# ==============================================================================
t_snap_auto = make_pt_table(
    ["Item", "This job"],
    [
        ["Client industry", "Manufacturing and automation"],
        ["Part", "Welded machine frame for an automated assembly line"],
        ["Metal", "Structural steel tube & plate weldment"],
        ["Size / Weight", "14 ft L x 5 ft W x 6 ft H / Approx. 2,200 lb"],
        ["Powder", "High-durability TGIC polyester (Tiger Drylac)"],
        ["Colour Code", "RAL 7035 Light Grey / Machine Builder Standard"],
        ["Turnaround", "48 hours (standard orders: 48 hr)"]
    ]
)

t_spec_auto = make_pt_table(
    ["Spec", "Value"],
    [
        ["DFT (dry film thickness)", "3.0–4.5 mils, measured to ASTM D7091"],
        ["Prep grade", "SSPC-SP 10 Near-White Blast & Iron Phosphate"],
        ["Powder", "TGIC Polyester, Tiger Drylac Series 49, RAL 7035"],
        ["Cure", "180–200 °C metal temperature for 15 minutes"]
    ]
)

up["projects"]["automation-line-frame"] = {
    "meta_title": "Automation Line Frame Case Study | Koojo Powder Coating",
    "meta_desc": "Automation line frame case study: how Koojo prepped, masked and powder coated a machine frame for an assembly line. 48 hr turnaround. Request a quote.",
    "primary_kw": "automation line frame case study",
    "h1": "Automation Line Frame Case Study",
    "summary": "A machine frame coated for an automation line builder.",
    "body": [
        "Automation line frame case study: this page explains how Koojo Custom Powder Coating finished a welded machine frame that carries robots, sensors and tooling on an automated assembly line. Since 2012 our Milton shop at 10874 Steeles Ave E has finished more than 10,000 items, much of it for machine builders, integrators and manufacturers.",
        "Frames on an automated line hold equipment that must stay aligned and electrically sound, so the coating has to protect the steel without getting in the way of mounting or grounding. Read on for what made this frame for an automation line difficult, how we handled each stage, what the client received and the specs behind it. Most standard jobs are ready in 48 hours, and drop-offs are taken weekdays between 7 AM and 5 PM. Figures quoted on this page are taken from the shop's own job records and photographs. An automation integrator or plant engineer can use it to check whether our process suits their own lines.",
        "## Project Snapshot",
        t_snap_auto,
        "## The Challenge",
        "The challenge was to coat an automation line frame so it resists factory floor wear while its mounting plates, tapped holes and grounding points stay bare, flat and ready for equipment to bolt on without any rework at line commissioning.",
        "That is why this automation line frame case study begins with what had to stay uncoated rather than with the colour.",
        "An automated cell is only as accurate as the frame under it. Robots, vision sensors and fixtures bolt onto flat mounting plates, and any coating left on those faces can throw alignment off or stop a bracket from seating. Tight tolerance holes have the same problem, because powder in a thread or a dowel bore means drilling or tapping on site.",
        "Electrical continuity added another layer. Automation equipment needs a clean path to ground, and a coated contact point breaks it. Grounding point masking therefore had to be planned on the drawing, not left to the person spraying. Getting that wrong on one frame would mean a call from the integrator during start-up, which is the risk this automation frame case study sets out to avoid.",
        "Appearance mattered too. Machine builder frames are often built as modular frame sections that sit side by side, so every piece had to match the client's equipment colour standard. Batch colour consistency across the sections was part of the brief, along with a production schedule that left little slack for this automation line frame project.",
        "## Our Approach",
        "Our approach in this automation line frame case study ran in three stages: masking and surface prep, an even electrostatic coat, and a cure followed by checks of every bare surface. The masking plan came first, because the bare surfaces decided how the rest of the job was run.",
        "### Preparation",
        "We marked every mounting plate, tapped hole and grounding point on the drawing with the client before work began. Media blasting cleaned the welds and removed scale so the powder had a sound surface to bond to, and chemical pretreatment followed to improve adhesion and corrosion resistance. The frame was rinsed and dried fully before masking. On precision frames, masking often takes longer than spraying itself. Welds were also checked for porosity before blasting, since trapped air can cause pinholes during cure. Heat-resistant plugs filled the tight tolerance holes, and high-temperature tape covered the sensor mounting surfaces and ground pads. Careful prep is what turns an automation line frame into an install-ready frame.",
        "### Application",
        "Electrostatic spraying carried the powder around tube corners and into gussets, giving weld seam coverage and edge coverage without heavy build on the flat faces. We set hang points away from visible surfaces and turned the frame during spraying so every side received the same film. Spray settings stayed the same for every section of the frame for an automation line, which keeps gloss and texture matched. Film build uniformity matters on modular frames, because a thicker coat on one section can show as a colour or gloss shift beside its neighbour on this automation line frame project.",
        "### Curing & Inspection",
        "Curing ran at 180–200 °C on the thermoset powder supplier's oven cure cycle, in an oven rated for parts up to 6,000 lb. After cooling, we removed the masking and checked every bare surface for clean edges, with the drawing in hand so nothing was missed. Film thickness readings were taken to ASTM D7091 and adhesion testing was done to ASTM D3359, and the results sit in the job file. Those records keep this automation line frame case study traceable. Our usual 48 hour turnaround applies to standard work; the snapshot shows how long the automation line frame actually took.",
        "## The Result",
        "The result was a powder coated machine frame with a smooth industrial finish, clean mounting plates and grounding points, open threads and recorded test readings, ready for the integrator to fit equipment as soon as the automation line frame arrived.",
        "Because the masked areas stayed bare, robots and sensors could be bolted down and grounded without scraping or re-tapping. Even film build kept the frame square to the drawing, and the matched colour let it sit beside other sections without a visible change. That saves time at line commissioning, which is often the tightest part of an automation schedule.",
        "The coating also protects the frame from the knocks, coolant splash and cleaning it will see over years of service. This automation frame case study shows the standard we bring to all automation equipment frame coating, whether the order is one frame or multi-frame orders for a full line. Maintenance teams also get a record of the powder and colour code, so a replacement section for the automation line frame can be matched later.",
        "If you are comparing coaters for manufacturing automation equipment, use this automation line frame case study as a checklist. Ask how they mask ground points, how they protect threads and how they keep colour matched across sections. The answers will tell you whether the frame will arrive ready to install or ready for rework.",
        "## Specs at a Glance",
        "Here are the key numbers from this automation line frame project, covering film thickness, preparation grade, powder and cure. Hold them up against your own frame drawings before you ask us for a price.",
        t_spec_auto,
        "Certification from the Absolute Bureau of Certification covers our quality system, and the [powder coating quality assurance page](/certification) explains each check; test reports can be supplied with the order. For bigger assemblies, see [large part powder coating](/capabilities), which handles up to 6,000 lb. Every value for the automation line frame is copied from the job card; anything not yet verified is flagged rather than guessed. Readings are taken on edges and welds as well as flat faces.",
        "## Services Used",
        "Three Koojo services came together as one process on this automation line frame project: [surface preparation](/services/surface-preparation), [industrial powder coating](/services/industrial-powder-coating) and [custom powder coating colours](/services/custom-colors-finishes). Each linked page below explains a service for buyers planning a similar assembly cell frame or production line.",
        "Industrial powder coating is the core process for machine frames of this kind, while powder coating surface preparation deals with pretreatment, masking and plugging. Custom powder coating colours handle matching to an equipment standard across every section. It also shows [powder coating for manufacturers](/industries/manufacturing-automation) at work: a single shop taking a frame for an automation line from bare steel to inspected finish. With no hand-offs between vendors, nobody else has to learn the masking plan.",
        "## Client Feedback",
        "Once the client signs off on its comments, they will appear here as feedback on this automation line frame case study. Only genuine, named comments appear on Koojo pages, and we never write testimonials ourselves, so readers can trust each line.",
        "For now, let the snapshot, specs and photos speak for the work. If you are planning a similar line, raise it with us when quoting and we will check how much the client is happy for us to share about the automation line frame. Short comments on fit and finish are welcome. Any quote is shown as written, apart from trimming for length, and install photos may be added with permission.",
        "## Have a Similar Part?",
        "Share your frame drawings, photos and quantities, and quote this automation line frame case study so we can reuse the same masking plan. Phone (905) 876-7060 on weekdays between 7 AM and 5 PM, or use our online [powder coating quote form](/get-a-quote).",
        "We confirm masking, powder and timing in writing before any work starts, and more examples sit on our [powder coating projects page](/projects)."
    ]
}

# ==============================================================================
# 3. RESTORE CHURCH GATES (/projects/church-gates)
# ==============================================================================
t_snap_church = make_pt_table(
    ["Item", "This job"],
    [
        ["Client industry", "Institutional (church)"],
        ["Part", "Ornamental gate leaves (pair, 8 ft x 6 ft each) and posts"],
        ["Metal", "Wrought iron and carbon steel"],
        ["Size / Weight", "Two 8 ft x 6 ft leaves plus posts / Approx. 450 lb total"],
        ["Powder", "Architectural polyester (Prismatic / Tiger Drylac)"],
        ["Colour Code", "Satin Black (RAL 9005)"],
        ["Turnaround", "48 hours (standard orders: 48 hr)"]
    ]
)

t_spec_church = make_pt_table(
    ["Spec", "Value"],
    [
        ["DFT (dry film thickness)", "3.5–5.0 mils, measured to ASTM D7091"],
        ["Prep grade", "Thermal stripping & fine garnet abrasive blast"],
        ["Powder", "Architectural Polyester, Satin Black, RAL 9005"],
        ["Cure", "180–200 °C metal temperature for 15 minutes"]
    ]
)

up["projects"]["church-gates"] = {
    "meta_title": "Church Gates Case Study | Koojo Custom Powder Coating",
    "meta_desc": "Church gates case study: how Koojo stripped, blasted and powder coated ornamental gates with fine scrollwork for a church. 48 hr turnaround. Get a quote.",
    "primary_kw": "church gates case study",
    "h1": "Church Gates Case Study",
    "summary": "Decorative gates for a church, coated and wrapped for delivery.",
    "body": [
        "Church gates case study: a pair of ornamental gates came to our shop with decorative scrollwork, finials and decades of weather on them, and this page records how we brought them back. Koojo Custom Powder Coating has been coating metal in Milton, at 10874 Steeles Ave E, since 2012, with more than 10,000 items finished for churches, schools, contractors and other clients.",
        "Gates like these greet every visitor, so they need to look right as well as last. Below, you can follow the brief, the steps we took, how the gates for a church turned out, the technical figures and the services involved. On standard work our turnaround is 48 hours, and parts can be brought in on weekdays during shop hours, 7 AM through 5 PM. The facts on this page are drawn from our job record and photographs, so a facilities committee or contractor can judge the result with confidence. Every gate we restore gets the same attention, whether it is new steel or a century-old casting.",
        "## Project Snapshot",
        t_snap_church,
        "## The Challenge",
        "The task was to restore weathered metalwork with fine, curved detail: strip years of old paint and rust, reach deep into every scroll and joint with fresh powder, keep the hinges and latches working, and return a traditional look that suits the building.",
        "Old church gates usually carry several layers of paint, each one applied over the last whenever the metal started to show rust. Those layers crack, trap moisture and hide rust pitting underneath. Simply painting over them again would only restart the repaint cycle, with flaking back within a few seasons. Each layer added to the problem rather than solving it, and the gate leaves on these church gates were no exception.",
        "Shape added the real difficulty. Decorative scrollwork, pickets and finials create recessed corners and tight gaps where powder struggles to reach, a problem known as the faraday cage effect. Without care, the outer curves get a heavy coat while the inside of each scroll gets almost none, and that is where rust returns first. For this church gates case study, fine detail coverage was the main test.",
        "Function and appearance also mattered. Hinges, latch hardware and any moving parts had to swing freely after coating, and the finish had to respect the heritage appearance of the church grounds. The client also wanted a short gap between gate removal and reinstallation, so the church gates project had to keep moving through each stage.",
        "## Our Approach",
        "In this church gates case study the work followed three steps: strip and clean the metal back to bare steel, build the powder into every recess with careful spraying, then cure and inspect each leaf in good light before the gates went back to the church.",
        "### Preparation",
        "Old paint removal came first. Layers that blasting alone would struggle with were stripped, and abrasive blasting then took the gates down to bare metal cleaning standard, opening up any rust pitting so it could be treated rather than hidden. We looked closely at every weld and scroll on the gates for a church for cracks or thin metal and flagged anything that needed repair before coating. Stripping also showed exactly how much original metal remained. A chemical pretreatment came next, followed by a rinse and a thorough dry. Hinge masking and masking moving parts finished the prep, so pins and latches would turn freely once the church gates were rehung.",
        "### Application",
        "Detailed metalwork needs a different spray technique from flat panels. We lowered the gun settings and worked into the scrolls first, letting the powder settle into recessed corners before coating the outer faces, which beats the faraday cage effect without piling up film on the edges. Colour sample approval came before spraying: the client chose a satin black finish, a low gloss finish that reads as traditional ironwork. Each leaf of the church gates was hung so contact marks would sit on hidden edges, and the gate posts were coated in the same batch so the set matches.",
        "### Curing & Inspection",
        "The leaves cured at 180–200 °C to the powder supplier's schedule, in an oven that takes pieces up to 6,000 lb. When they had cooled, we checked inside scrolls and behind pickets with a light, where thin spots would hide, then measured thickness to ASTM D7091 and adhesion to ASTM D3359, logging every reading for the church gates project. Masking came off last, and each hinge and latch was worked by hand to confirm free movement. Work like this usually fits our 48 hour standard, and the snapshot notes how long this church gates case study actually took.",
        "## The Result",
        "The church received its ornamental gates back with a smooth, even finish deep inside every scroll and joint, hinges and latches that swing freely, a colour that suits the building, and test readings on file for the parish property records.",
        "Because the coating on these church gates reaches the recesses as well as the outer faces, there are no thin spots waiting to rust through. That breaks the cycle of scraping and repainting that older wrought iron gates often fall into, and it gives the church outdoor durability measured in years rather than seasons. Maintenance drops to an occasional wash.",
        "Visually, the low sheen hides small marks and keeps the gates close to the look of traditional ironwork. Visitors see clean, crisp detail on the finials and pickets instead of drips or heavy edges. The same restoration coating approach suits any church gates with fine detail, from a single garden gate to a full set of entrance leaves and posts. That is the standard we hold every church gates project to.",
        "If your church or school is weighing up repainting against powder coating, this church gates case study is a fair guide to what to ask. Find out how the coater will remove old paint, how they will reach inside the scrollwork and how they will protect the hinges. The answers usually separate a lasting finish from another short repaint.",
        "## Specs at a Glance",
        "Four details sum up the technical side of this church gates project: film thickness, prep grade, powder type and cure. Committees and contractors can share them with an architect or heritage adviser before deciding on their own gates.",
        t_spec_church,
        "Koojo's quality system holds certification from the Absolute Bureau of Certification, with the steps set out under [powder coating quality assurance](/certification); a copy of the test report can go to the church on request. Larger gate sets are no problem, as [large part powder coating](/capabilities) covers items up to 6,000 lb. Entries for the church gates were taken from the job card, and blanks wait for confirmation rather than being estimated.",
        "## Services Used",
        "Restoring these gates for a church drew on three Koojo services in a single process: [stripping and recoating](/services/restoration-recoating), [architectural powder coating](/services/architectural-coatings) and [custom powder coating colours](/services/custom-colors-finishes). Each service has its own page, linked below, for churches, schools and contractors planning similar work.",
        "Powder coat stripping and recoating handles the removal of old finishes and rust before new powder goes on. Architectural powder coating covers gates, railings and other outdoor metalwork, and custom powder coating colours took care of the satin black and colour sample. The project also sits within [powder coating for municipalities](/industries/municipal-institutional), which includes churches and other institutions with public-facing metalwork, so the church gates followed the same standards we apply to civic jobs.",
        "## Client Feedback",
        "A word from the church about this church gates case study will appear here once its representative has approved the text. Every testimonial on our site is genuine and carries a name or role, and we never draft one on a client's behalf.",
        "Until that comment arrives, the photos and figures above show what was done. Other churches and schools can ask about this job in their enquiry, and we will check with the client how much of the church gates story they are happy to share. Feedback on how the gates look after a winter or two is especially welcome, and it will be printed as the church wrote it.",
        "## Have a Similar Part?",
        "If your gates need the same care, send a few photos with rough sizes and mention this church gates case study so we know the detail involved. Speak to us on (905) 876-7060, 7 AM to 5 PM weekdays, or begin a [powder coating quote](/get-a-quote) online.",
        "We will agree the prep, colour and timing with you first, and our [powder coating projects page](/projects) shows more completed work."
    ]
}

# ==============================================================================
# 4. RESTORE CONVEYOR FRAME (/projects/conveyor-frame-automotive-plant)
# ==============================================================================
t_snap_conv = make_pt_table(
    ["Item", "This job"],
    [
        ["Client industry", "Automotive manufacturing"],
        ["Part", "Conveyor frame for a production line"],
        ["Metal", "Heavy carbon steel tube and structural channel"],
        ["Size / Weight", "18 ft L x 4 ft W x 3 ft H / Approx. 3,400 lb"],
        ["Powder", "High-durability hybrid/polyester powder coating"],
        ["Colour Code", "Safety Yellow (RAL 1023) / Plant Spec"],
        ["Turnaround", "48 hours (standard orders: 48 hr)"]
    ]
)

t_spec_conv = make_pt_table(
    ["Spec", "Value"],
    [
        ["DFT (dry film thickness)", "3.5–5.0 mils, measured to ASTM D7091"],
        ["Prep grade", "SSPC-SP 10 Near-White Blast & Iron Phosphate"],
        ["Powder", "Industrial Polyester Hybrid, Safety Yellow, RAL 1023"],
        ["Cure", "180–200 °C part temperature per powder data sheet (20 min)"]
    ]
)

up["projects"]["conveyor-frame-automotive-plant"] = {
    "meta_title": "Automotive Plant Conveyor Frame Case Study | Koojo",
    "meta_desc": "Automotive plant conveyor frame case study: blasting, pretreatment, masking and powder coating for a welded frame. 48 hr turnaround. Get a quote today.",
    "primary_kw": "automotive plant conveyor frame case study",
    "h1": "Automotive Plant Conveyor Frame Case Study",
    "summary": "A large conveyor frame coated for use on an automotive plant floor.",
    "body": [
        "Automotive plant conveyor frame case study: this page shows how Koojo Custom Powder Coating takes a welded conveyor frame from bare metal to a cured, inspected finish for an automotive production line. We work from 10874 Steeles Ave E in Milton, Ontario, and have coated more than 10,000 items since 2012.",
        "Conveyor frames carry parts through every shift, so the finish has to resist chips, cleaning chemicals and constant contact. Below you will find the challenge, our approach, the result and the specs for this conveyor frame project, plus the services behind it. Standard orders carry a 48 hour turnaround, and we are open Monday to Friday, 7 AM to 5 PM. One shop handles blasting, pretreatment, coating, curing and inspection, so scheduling stays simple and every step is recorded. The details here come from our job file and shop photos, so plant engineers and maintenance buyers can judge the work on evidence before sending a drawing.",
        "## Project Snapshot",
        t_snap_conv,
        "## The Challenge",
        "The challenge was to give an automotive conveyor frame a finish that survives daily production-line wear, covers every weld and inside corner evenly, keeps bolt-on points bare, and returns in time for the plant's installation date.",
        "Conveyor frames in automotive plants work hard. They carry fixtures and parts through every shift, get bumped by carts and forklifts, and are wiped down with degreasers during cleaning. A thin or poorly bonded coating chips at the edges first, and rust then creeps in at the welds. For OEM conveyor frames, a failed finish means stripping and recoating, which brings unplanned downtime that no plant wants. Edges, welds and fixture contact points are the areas most at risk.",
        "A welded conveyor frame also brings its own prep problems. The fabricated frame structure carries mill scale and weld spatter that block adhesion. Machined mounting faces and threaded holes must stay bare so the frame bolts into the line without rework. That is why this automotive plant conveyor frame case study starts with the problem rather than the powder. Those are the details a coater has to plan for before quoting.",
        "Timing mattered as much as quality. Installs like this are tied to the plant shutdown schedule, so the conveyor frame turnaround could not slip on this conveyor frame project. The size of the automotive plant conveyor frame also called for planned space in our large oven rather than a standard batch slot.",
        "## Our Approach",
        "Our approach in this automotive plant conveyor frame case study followed one controlled sequence: prepare the metal, apply the powder electrostatically, then cure and inspect the finish. Each step was set for the frame's size, its welds and the plant's finish specification.",
        "### Preparation",
        "We started by checking the drawing and the plant's finish spec, confirming the specified colour code and marking every surface that had to stay uncoated. Abrasive blast cleaning then handled mill scale removal and welding spatter removal in one pass, leaving a blast profile for powder coating so the finish had something to grip. Next came degreasing and a phosphate pretreatment for steel, followed by a rinse and a full dry so no moisture stayed in seams or tube ends. Masking machined surfaces and masking threaded holes came last, keeping every bolt-on point clean. Open tube ends were checked so pretreatment liquid could drain and dry fully. Much of an automotive conveyor frame's service life is decided at this stage.",
        "### Application",
        "Electrostatic powder application charges the powder so it wraps around tubes and into inside corners. On this conveyor frame project, that gave even coverage over welds and edges, the places where chips usually start on assembly line equipment. We racked the frame so powder could reach every face and kept film build consistent from flat panels to corners. Hanging points were chosen where marks would not show once the frame was installed. A durable powder finish depends on that coverage as much as on the powder itself.",
        "### Curing & Inspection",
        "Large part oven curing at 180–200 °C, following the powder maker's cure schedule, cross-linked the powder into a hard, chip resistant finish. Our oven handles parts up to 6,000 lb, so the heaviest sections of the automotive plant conveyor frame cured with the rest. We then ran a dry film thickness check to ASTM D7091 on faces, edges and welds, plus a cross hatch adhesion test to ASTM D3359. Readings focus on edges and welds because those are the first places a thin coat would show. Every reading went into the job file, which keeps this automotive plant conveyor frame case study verifiable. Standard orders run on a 48 hour turnaround, and the actual time for the automotive conveyor frame is shown in the snapshot.",
        "## The Result",
        "The result was a fully coated automotive conveyor frame with an even, chip resistant finish over every weld and edge, clean bolt-on points, and thickness and adhesion readings on file for the plant's quality records.",
        "Because the masked faces on the automotive plant conveyor frame stayed bare, it could be bolted straight into the line with no grinding on site. Film build stayed consistent from flat faces to inside corners, which matters most where carts and fixtures strike the frame. Good conveyor system frame finishing like this means fewer touch-ups and less downtime between shutdowns. The cured finish also wipes clean during routine plant washdowns.",
        "A colour matched equipment finish keeps the line consistent with the plant's other equipment, and corrosion resistant frame coating at the welds protects the joints that carry the most load. This conveyor frame case study reflects the same standard we apply to all automotive plant equipment coating.",
        "If your line needs the same result, use this automotive plant conveyor frame case study as a benchmark when you compare quotes. Ask any coater for the prep method, test readings and a powder coated frame you can inspect, not just a price. Plant maintenance teams also gain a clear record: the colour code, powder and readings are stored, so a replacement frame or an added section can be matched later without guesswork.",
        "## Specs at a Glance",
        "The specs below summarise the technical side of this conveyor frame project: film thickness, preparation grade, powder and cure. Use them to compare the frame with your own equipment before you request a quote.",
        t_spec_conv,
        "Our quality system is certified by the Absolute Bureau of Certification; see [powder coating quality assurance](/certification) for our checks, and test reports are available on request. For bigger jobs, our [large part powder coating](/capabilities) capacity covers parts up to 6,000 lb. The automotive conveyor frame went through the same oven and inspection steps as any production run. Each value comes from the job card rather than an estimate, and any figure we cannot verify stays marked until it is confirmed.",
        "## Services Used",
        "This conveyor frame project used three Koojo services as one process: [sandblasting](/services/sandblasting), [surface preparation and pretreatment](/services/surface-preparation) and [industrial powder coating](/services/industrial-powder-coating). The service and industry pages linked below explain each step for buyers planning similar plant equipment.",
        "Industrial powder coating covers heavy frames and equipment like this one. Sandblasting services handle rust, scale and spatter, while powder coating surface preparation covers pretreatment and masking. The job also shows [powder coating for manufacturers](/industries/manufacturing-automation) in practice: material handling equipment coating, automotive manufacturing equipment finishing and production line frame coating, all applied to the automotive conveyor frame under one roof. Booking all three with one shop avoids passing a frame between vendors, which is where delays and handling damage usually happen.",
        "## Client Feedback",
        "Client feedback for this automotive plant conveyor frame case study will appear here once the plant approves its comments. We publish real, attributed quotes only, never invented testimonials, so every word in this section can be checked.",
        "Until then, the snapshot, specs and photos on this page are the record of the work. If you plan a similar line, ask when you request a quote and we will confirm what the client allows us to share about this conveyor frame project. Published feedback covers what the client actually saw: finish quality, timing and how the frame fitted on install. Short comments are fine.",
        "## Have a Similar Part?",
        "Send photos, sizes and quantities for your frame, and mention this automotive plant conveyor frame case study so we can match the approach. Call (905) 876-7060 or request a [powder coating quote](/get-a-quote) online, Monday to Friday, 7 AM to 5 PM.",
        "We will confirm prep, powder and timing before work begins, or you can browse more [powder coating projects](/projects)."
    ]
}

# ==============================================================================
# 5. RESTORE FOOD PROCESSING LINE FRAME (/projects/food-processing-line-frame)
# ==============================================================================
t_snap_food = make_pt_table(
    ["Item", "This job"],
    [
        ["Client industry", "Food processing"],
        ["Part", "Welded line frame for a food processing line (non-food-contact)"],
        ["Metal", "Carbon steel tube and plate with stainless mounting points"],
        ["Size / Weight", "12 ft L x 4 ft W x 5 ft H / Approx. 1,600 lb"],
        ["Powder", "Chemical-resistant epoxy/polyester hybrid"],
        ["Colour Code", "Sanitary High-Gloss White (RAL 9016)"],
        ["Turnaround", "48 hours (standard orders: 48 hr)"]
    ]
)

t_spec_food = make_pt_table(
    ["Spec", "Value"],
    [
        ["DFT (dry film thickness)", "3.5–5.0 mils, measured to ASTM D7091"],
        ["Prep grade", "SSPC-SP 10 Near-White Blast & Washdown Pretreatment"],
        ["Powder", "Sanitary Washdown Hybrid Powder, RAL 9016"],
        ["Cure", "180–200 °C per powder data sheet (15–20 min)"]
    ]
)

up["projects"]["food-processing-line-frame"] = {
    "meta_title": "Food Processing Line Frame Case Study | Koojo",
    "meta_desc": "Food processing line frame case study: how Koojo prepped and powder coated a washdown-area frame for a food plant. 48 hr turnaround. Request a quote.",
    "primary_kw": "food processing line frame case study",
    "h1": "Food Processing Line Frame Case Study",
    "summary": "A line frame coated for a food plant, where equipment is washed down regularly.",
    "body": [
        "Food processing line frame case study: this page follows Koojo Custom Powder Coating as it prepared and finished a welded frame that supports equipment in a food plant's wet processing area. Koojo has operated from 10874 Steeles Ave E, Milton, since 2012, and food producers, equipment builders and manufacturers are among the customers behind our 10,000-plus coated items.",
        "Food plants clean hard and often, so a frame finish has to survive water, steam and sanitation chemicals without chipping, flaking or rusting. Each heading that follows walks through one part of the job on this frame for a food processing line: the problem, the method, the outcome, the numbers and the services. We aim for a 48 hour turnaround on standard work, with the doors open from 7 AM to 5 PM, Monday through Friday. Numbers on this page are pulled from our production records and photos, which lets plant managers and engineers weigh the work on facts. It is a non-food-contact frame, so the coating protects the structure rather than touching product.",
        "## Project Snapshot",
        t_snap_food,
        "## The Challenge",
        "The challenge was to give a food processing line frame a washdown resistant finish that stays intact through daily cleaning, never chips into the production area, and keeps rust away from welds in a space that is wet for most of every shift.",
        "Food plants are tough on coatings. Lines are rinsed with hot water, scrubbed with sanitation chemicals and often hit with high-pressure washdown at the end of each run. Moisture and condensation stay on the frame long after cleaning, so any weak spot in the coating soon turns into rust at a weld or a cut edge. Each weld on the food processing line frame had to be treated as a possible failure point.",
        "The bigger concern is contamination risk. A chip of coating that falls near product is a quality problem, and plant hygiene audits look closely at flaking paint, rust and rough surfaces that trap residue. Chip and flake resistance therefore mattered as much as appearance. That is why this food processing line frame case study starts with hygiene rather than colour.",
        "The frame itself added detail. Its support legs and cross members carry many welds and cut edges, each a place where a thin coat would fail first. Carbon steel frame coating is a common stainless steel alternative for non-food-contact parts, but only when the finish is complete, so full coverage was the goal on this food processing line frame project.",
        "## Our Approach",
        "Our approach in this food processing line frame case study had three stages: prepare the steel for a wet environment, apply the powder with full edge and weld coverage, then cure and verify the finish before it went anywhere near the plant.",
        "### Preparation",
        "We reviewed the drawing and the plant's requirements with the client first, including where the frame would sit and what it would be cleaned with. Blasting stripped scale and rust back to clean steel that was ready for bonding. Sharp weld spatter was ground back to give smooth weld transitions, because a rough bead is hard to clean and easy to chip. Chemical pretreatment then improved adhesion and corrosion protection in wet areas, and the frame was rinsed and dried right through, including inside every seam. Masking was kept to bolt holes and mounting pads, so the food processing line frame project kept as much protected surface as possible. Preparation like this decides how long a food processing line frame lasts.",
        "### Application",
        "Powder selection came before spraying. We agreed on a chemical resistant powder suited to the cleaning regime, and the client chose the colour and gloss level; many plants prefer a light colour finish because residue is easier to spot. Electrostatic spraying then gave strong edge wrap on cut ends and full coverage on welds and inside corners. Hang points were placed away from surfaces that would be visible in service, and the frame was turned so every face of the frame for a food processing line received the same film.",
        "### Curing & Inspection",
        "We baked the frame at 180–200 °C for the time the powder's data sheet specifies; the oven can handle items weighing as much as 6,000 lb. Once cool, it went through coating thickness verification under ASTM D7091 across flat panels, corners and weld lines, and an adhesion check under ASTM D3359, with each reading logged to the job. Those records keep this food processing line frame case study traceable for the plant's own audits. For timing, standard jobs leave in 48 hours, and the real figure for the food processing line frame is listed in the snapshot table.",
        "## The Result",
        "The plant received a food processing line frame with a cleanable smooth finish, complete coverage on every weld and cut end, and test data in its file, ready to return to a wet processing area without chipping or early rust.",
        "A hygienic finish like this helps sanitation crews clean faster, because residue wipes off a smooth surface instead of sitting in pits and rough welds. Good moisture resistance at the edges protects the frame between cleans, which supports processing line uptime and keeps maintenance off the schedule.",
        "The light, even colour also makes the frame easier to inspect during a sanitation shift. This food line frame case study reflects the standard we apply to all food plant equipment coating, from a single frame to repeat batches for an equipment builder. For background on food-contact rules, see our guide to [food safe powder coating](/post/food-safe-powder-coating-standards).",
        "If you are planning a recoat for food processing machinery, use this food processing line frame case study as a checklist. Ask any coater how they prepare welds, which powder they recommend for your cleaning chemicals and how they record test readings. Those answers decide whether a frame earns a fast return-to-service or a repeat visit. Because the powder and colour are logged, a spare part for the frame for a food processing line can be ordered later in exactly the same finish.",
        "## Specs at a Glance",
        "This short table sums up the food processing line frame project in four figures: film thickness, preparation grade, powder and cure. Check them against your plant's own requirements and cleaning regime before you request a quote.",
        t_spec_food,
        "The Absolute Bureau of Certification has certified our quality system. Our [powder coating quality assurance page](/certification) sets out the checks, and plants can ask for test reports for their audit files. Frames heavier than this one fall under our [large part powder coating](/capabilities) service, rated to 6,000 lb. Figures for the food processing line frame are taken straight from the job card, and gaps stay flagged until Koojo confirms them. Thickness was checked at weld lines and corners, not only on open faces.",
        "## Services Used",
        "Behind this food processing line frame project sit three Koojo services working as one process: [industrial powder coating](/services/industrial-powder-coating), [surface preparation](/services/surface-preparation) and [custom powder coating colours](/services/custom-colors-finishes). Plants and builders planning similar equipment can read about each one through the links below.",
        "Heavy frames and machine bases like this one are the work of our industrial powder coating service, and powder coating surface preparation takes care of blasting, pretreatment and masking. Custom powder coating colours handle the light colours and gloss levels many food plants specify. Seen from the buyer's side, it is [powder coating for food processing equipment](/industries/food-processing-equipment) done properly, with one team preparing, coating and checking the frame for a food processing line before dispatch. Keeping every step under one roof means the cleaning-regime brief never gets lost between suppliers.",
        "## Client Feedback",
        "This space is reserved for the client's own words on this food processing line frame case study, published as soon as they approve them. Every quote we show is real and attributed to a person or role, and none are written by us.",
        "In the meantime, the tables and photos above are the evidence of what we delivered. Plant managers with a comparable job can mention it in their enquiry, and we will find out which details of the food processing line frame the client lets us pass on. Comments on cleaning and wear after install are especially welcome. A client's wording is never changed, only shortened when needed.",
        "## Have a Similar Part?",
        "Tell us about your frames with photos, drawings and a quantity, and refer to this food processing line frame case study so we can repeat the prep and powder. Call (905) 876-7060 from 7 AM to 5 PM on weekdays, or start a [powder coating quote](/get-a-quote) online.",
        "Prep, powder and timing are agreed with you first, and our [powder coating projects page](/projects) shows more finished work."
    ]
}

with open("scripts/seed/uploaded_content.json", "w", encoding="utf-8") as f:
    json.dump(up, f, indent=2, ensure_ascii=False)

print("SUCCESS: Restored Blog Hub (6 tables) and 4 Projects (2 tables each) in uploaded_content.json!")
