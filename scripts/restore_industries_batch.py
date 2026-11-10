import json
import re

# Helper to build portable text tables
def make_pt_table(headers, rows):
    import random
    r = random.randint(100, 999)
    tbl = {
        "_type": "table",
        "_key": f"tbl_{r}",
        "hasHeaderRow": True,
        "rows": []
    }
    # Header row
    h_row = {
        "_type": "tableRow",
        "_key": f"tr_h_{r}",
        "cells": []
    }
    for j, h in enumerate(headers):
        h_row["cells"].append({
            "_type": "tableCell",
            "_key": f"th_{r}_{j}",
            "isHeader": True,
            "content": [{
                "_type": "span",
                "_key": f"sh_{r}_{j}",
                "text": h,
                "marks": []
            }]
        })
    tbl["rows"].append(h_row)

    # Data rows
    for i, row in enumerate(rows):
        d_row = {
            "_type": "tableRow",
            "_key": f"tr_{r}_{i}",
            "cells": []
        }
        for j, val in enumerate(row):
            d_row["cells"].append({
                "_type": "tableCell",
                "_key": f"td_{r}_{i}_{j}",
                "isHeader": False,
                "content": [{
                    "_type": "span",
                    "_key": f"sd_{r}_{i}_{j}",
                    "text": val,
                    "marks": []
                }]
            })
        tbl["rows"].append(d_row)
    return tbl

with open("scripts/seed/uploaded_content.json", "r", encoding="utf-8") as f:
    up = json.load(f)

# 1. RESTORE PAGES["industries"] (Hub Page)
tbl_glance = make_pt_table(
    ["Sector", "Typical parts", "Main concern", "Preparation and finish focus"],
    [
        ["Fabricators and welders", "Brackets, frames, tanks, structural assemblies", "Weld seams and sharp edges", "Spatter removal and even coverage"],
        ["Manufacturing", "Conveyor frames, guards, enclosures", "Matching colour across parts", "Controlled batches and records"],
        ["Machine shops", "Machined components", "Tolerances", "Careful masking"],
        ["Construction", "Rails, stairs, structural steel", "UV, rain and road salt", "Outdoor-rated finishes"],
        ["Food processing", "Line frames, supports", "Washdown", "Smooth, cleanable surface"],
        ["Agriculture", "Implements, trailers, attachments", "Rust and chipping", "Bare-metal cleaning, tough film"],
        ["Municipal", "Bollards, gates", "Long service life", "Textured, durable finishes"]
    ]
)

tbl_turnaround = make_pt_table(
    ["Item", "Detail"],
    [
        ["Shop hours", "Monday to Friday, 7 AM to 5 PM"],
        ["Typical turnaround", "48-hour turnaround on many jobs"],
        ["Large or heavy parts", "Schedule confirmed at quoting"],
        ["Pickup and delivery", "Arranged when we quote"],
        ["Quote replies", "During shop hours"]
    ]
)

up["pages"]["industries"] = {
    "meta_title": "Powder Coating by Industry | Koojo Custom Powder Coating",
    "meta_desc": "Powder coating by industry for fabricators, manufacturers, machine shops and food plants. Durable finishes, 48-hour turnaround, Mon–Fri. Get a quote.",
    "primary_kw": "powder coating by industry",
    "h1": "Powder Coating by Industry: Durable Finishes for Ontario Businesses",
    "summary": "Powder Coating by Industry: Durable Finishes for Ontario Businesses",
    "body": [
        "Powder coating by industry means choosing the coating, preparation and checks that suit the sector using the part, not just the metal underneath. Koojo Custom Powder Coating, based in Ontario, applies this approach for seven sectors as a trusted industrial coating partner and B2B powder coating shop. Pick your sector below, or send photos and drawings through the [quote form](/get-a-quote) for a clear plan. Each sector page explains typical parts, finishes and checks.",
        "## Quick facts",
        [
            "Serving businesses since 2012",
            "More than 10,000 items coated",
            "Shop hours: Monday to Friday, 7 AM to 5 PM",
            "Typical turnaround: 48 hours on many jobs",
            "Base: 10874 Steeles Ave E, Milton, ON",
            "Sectors covered: seven",
            "Large parts: load capacity up to 6,000 lb",
            "Quality: certified through the Absolute Bureau of Certification",
            "Quote replies: during shop hours"
        ],
        "## Industries We Serve",
        "We serve seven sectors: fabrication, manufacturing, machine shops, construction, food processing, agriculture and public institutions. Powder coating by industry gives each one preparation and a finish suited to its parts, so a bracket for a plant floor and a gate for a church are treated differently. Select a sector to see typical parts and recommended finishes.",
        "### [Metal Fabricators and Welding Shops](/industries/metal-fabricators-welding-shops)",
        "Brackets, frames, tanks and structural assemblies need welded assembly finishing that covers seams evenly. We handle weld spatter removal before pretreatment, so Ontario metal fabricators receive fabricated steel parts ready to install. Send drawings and part counts for a quick plan. Related project: [Automation Line Frame](/projects/automation-line-frame).",
        "### [Manufacturing and Automation](/industries/manufacturing-automation)",
        "Conveyor frames, machine guards and enclosures must match in colour and still fit after coating. Our OEM finishing programs cover equipment frame finishing in controlled batches, with colour and powder traceability records for reorders. Parts are checked for fit after coating so assembly goes smoothly. Related projects: [Conveyor Frame for an Automotive Plant](/projects/conveyor-frame-automotive-plant) and [Robotic Base](/projects/robotic-base).",
        "### [Machine Shops](/industries/machine-shops)",
        "Machined components need protection without changing tolerances. We use masking for tight-tolerance parts, and masking and plugging for threads and bores, in small batches or single prototypes. Threaded features stay clean, and one-off parts are welcome. See more finished work in our [portfolio](/projects).",
        "### [Contractors and Construction](/industries/contractors-construction)",
        "Handrails, stair components and structural steel must arrive on schedule and survive the weather. We offer jobsite delivery coordination and outdoor metalwork finishes cured for UV, rain and road salt, and delivery can be timed to your site schedule. Related project: [Safety Bollards](/projects/safety-bollards).",
        "### [Food Processing Equipment](/industries/food-processing-equipment)",
        "Line frames, supports and guards face constant washing. Cleaning-tolerant coatings resist flaking where moisture is steady, and we discuss food-contact powder options for surfaces near product. We record the powder used so your quality team has documentation. Related project: [Food Processing Line Frame](/projects/food-processing-line-frame).",
        "### [Agricultural and Heavy Equipment](/industries/agricultural-heavy-equipment)",
        "Implements, trailers and attachments face mud, fertilizer and sun. We clean older equipment to bare metal and apply a tough finish for rust prevention for equipment, including heavy steel fabrications. Parts return ready to work, and heavy items are discussed at quoting. Browse related work in our [portfolio](/projects).",
        "### [Municipal and Institutional](/industries/municipal-institutional)",
        "Bollards, gates and railings must stay safe and presentable for years. Our institutional metalwork finishing covers public space metalwork, with scratch-hiding textures that suit busy sites. Documented checks are available with your quote. Related project: [Church Gates](/projects/church-gates).",
        "## Powder Coating by Industry at a Glance",
        "This table summarizes how finish needs change from one sector to the next.",
        tbl_glance,
        "## How We Match a Finish to Your Sector",
        "We match a finish to your sector in four steps: review, prepare, apply and cure, then inspect. Because powder coating by industry depends on how each part is used, every step is adjusted to the sector instead of following one fixed recipe.",
        [
            "1. Review: We ask where the part will be used, how it is cleaned and which surfaces must stay bare. Photos, drawings and part counts help us give an accurate plan. Early review prevents rework and surprise costs.",
            "2. Prepare: Pretreatment before coating drives adhesion and corrosion protection for steel. Depending on the metal, we degrease, treat, remove rust, then finish with careful masking. Skipping this stage is the most common reason coatings fail early.",
            "3. Apply and cure: Electrostatic powder application wraps thermoset powder evenly around the part, which then enters the curing oven at roughly 180–200 °C. Our load capacity is up to 6,000 lb; see [capabilities](/capabilities). Heavy parts need longer oven time to reach temperature all the way through.",
            "4. Inspect: We check coverage, appearance and film thickness before release, then pack parts to protect the finish. Any part that misses the standard is corrected before release."
        ],
        "## Projects by Industry",
        "Each project below shows finished work for a sector we serve. Reading a case study is the quickest way to judge whether our work fits your needs, and you can browse them all on our [projects page](/projects).",
        [
            "[Conveyor Frame for an Automotive Plant](/projects/conveyor-frame-automotive-plant): manufacturing and automation.",
            "[Automation Line Frame](/projects/automation-line-frame): manufacturing and fabrication.",
            "[Food Processing Line Frame](/projects/food-processing-line-frame): food processing.",
            "[Robotic Base](/projects/robotic-base): manufacturing and automation.",
            "[Safety Bollards](/projects/safety-bollards): construction and municipal work.",
            "[Church Gates](/projects/church-gates): institutional metalwork."
        ],
        "## Quality and Certification",
        "Our quality process is certified through the Absolute Bureau of Certification. We check adhesion against ASTM D3359 adhesion methods, measure dry film thickness following ASTM D7091, and treat ASTM B117 results as a reference for salt spray resistance. Test reports on request and quality assurance documentation are available for audited customers. These checks apply to every sector, and the depth of documentation depends on what your buyer or auditor requires. Ask for the reports you need when you request a quote, so they are prepared with the job instead of after it. Details are on our [certification page](/certification).",
        "## Don't See Your Industry?",
        "Other sectors are welcome. We often coat HVAC and ductwork, playground and park equipment and church gates and religious metalwork. For one-off pieces, prototypes and art, see [specialty and custom projects](/services/specialty-custom-projects), or send photos and we will say honestly whether powder coating is the right fit. We also review parts that arrive with old paint or rust and explain what preparation is realistic. Tell us the metal, size and use, and we will reply with a straight answer.",
        "## Turnaround, Hours and Delivery Times",
        "Planning around times keeps production moving. Times depend on part size, preparation and shop load, so we confirm a date when we quote rather than promise one in advance.",
        tbl_turnaround,
        "## Why Ontario Businesses Choose Koojo",
        "Experience supports every recommendation we make. Since 2012 we have coated more than 10,000 items, so we know how powder coating by industry plays out on real parts. Our shop has access to Highways 401 and 407, which supports delivery across Halton and Peel Region, and customers can read feedback on our Google Business Profile. We explain the options, document the work and give a date at quoting. We would rather give you a clear plan than a vague promise. Buyers return because the plan, the schedule and the finish match what we said at quoting. That record of real parts is why buyers return with new work. Browse our [powder coating services](/services).",
        "Ready to plan powder coating by industry for your parts? Request a quote today. Call (905) 876-7060 or email us, and we will reply during shop hours, Monday to Friday, 7 AM to 5 PM."
    ],
    "faqs": [
        [
            "How do I know which finish suits my sector?",
            "Start with where the part will be used and how it is cleaned. Outdoor parts need weather-stable powders and machined parts need careful masking. Send us the details and we will recommend durable metal coatings before you commit. Photos of the part and a note on its environment make that recommendation faster and more accurate."
        ],
        [
            "Can one order include parts for different sectors?",
            "Yes. Each part is prepared and coated to its own requirement, and we note the specification on the job so records stay clear. This keeps mixed orders organized and prevents a finish meant for one use from being applied to another."
        ],
        [
            "Do you handle repeat production runs?",
            "Yes. We keep powder and colour details on file, so later runs match earlier ones and keep batch consistency across orders. Standing schedules can be arranged with your planner. Tell us your usual volumes and delivery dates so we can plan oven time ahead."
        ],
        [
            "Can you coat parts that will touch food?",
            "We can discuss suitable powders for surfaces near product. The right choice depends on the part and your compliance rules, so share your requirement with your quote request. We will document the powder used so your quality team has a record for audits."
        ],
        [
            "How does the sector affect my quote?",
            "The sector decides preparation, masking, finish and paperwork, which drive the price. Send photos, quantity, size, metal and exposure, and we will explain the basis of the price. The more detail you share, the fewer assumptions we need to make."
        ]
    ]
}

# 2. RESTORE AGRICULTURAL & HEAVY EQUIPMENT
up["industries"]["agricultural-heavy-equipment"] = {
    "meta_title": "Agricultural Equipment Powder Coating | Koojo",
    "meta_desc": "Agricultural equipment powder coating for implements, trailers and attachments. Rust-resistant finishes, 48-hour turnaround on standard orders. Get a quote.",
    "primary_kw": "agricultural equipment powder coating",
    "h1": "Agricultural Equipment Powder Coating",
    "summary": "Rust protection for implements, trailers and attachments that live outdoors and work in dirt.",
    "body": [
        "Agricultural equipment powder coating is a factory-grade finishing process that bonds a cured, protective layer to fabricated steel, so implements, trailers and attachments resist rust, abrasion and chipping through every season. Koojo Custom Powder Coating works from 10874 Steeles Ave E in Milton, Ontario, and has finished more than 10,000 items since 2012. Our farm equipment powder coating service is built for equipment dealers, builders and Ontario agricultural suppliers who need dependable finishes, predictable scheduling and parts that return ready to bolt on.",
        "Standard orders carry a 48-hour turnaround, and our team is available Monday to Friday, 7 AM to 5 PM. Send photos, drawings or a sample part, and we will confirm the prep method, powder and timing before any work begins. If you already know which hitch, frame or attachment needs finishing, [request a quote](/get-a-quote) and we will reply with a clear plan and a seasonal turnaround you can schedule around. That is what a good finish should deliver: protection that holds up in the field and a supplier that keeps your machines working.",
        "Since 2012 | 10,000+ Items | 48 Hr Turnaround | 5.0 ★ Google Rating",
        "## Coating Challenges in Agricultural & Heavy Equipment",
        "Agricultural machinery powder coating must survive mud and moisture, chemicals and constant impact without flaking or fading. The main challenges are fertilizer corrosion, stone and soil abrasion, chipping at hitch points, and short seasonal windows that leave little room for rework or equipment downtime.",
        "Heavy equipment powder coating is demanding because welded steel frames, booms and buckets combine thick plate with thinner brackets, and those areas heat at different rates in the oven. Grease, mill scale, old paint and field rust block adhesion unless they are removed first. Hitch points and buckets need an abrasion-resistant finish, while hollow tubing can trap moisture and pins, bushings and hydraulic fittings need precise masking. Good agricultural equipment powder coating starts when preparation, powder choice and oven loading are planned together rather than treated as separate steps.",
        "Weld seams, edges and hitch points are the first places where coatings fail, so they get the most attention. Timing is the other pressure. Planting and harvest do not wait, so a finisher has to hold a dependable lead time and speak up early when a part needs extra work. Machines parked outdoors also face sun, mud and winter roads, so powder coating for agricultural equipment depends on a powder that gives road salt protection and long-lasting protection.",
        "## Parts and Metals We Coat for Farm and Heavy Machinery",
        "We coat mild steel, aluminum and welded assemblies used in agricultural and heavy equipment, including implement frames, trailers, hitches, loader buckets and attachments. Parts range from small batches of brackets up to large structures within our 6,000 lb capacity.",
        "Mild steel is the most common metal in agricultural machinery powder coating, and it responds well to blasting and phosphate pre-treatment before coating. Aluminum covers and panels are cleaned and prepared differently so the powder bonds without trapping gases. Our agricultural equipment powder coating program covers the following parts:",
        [
            "Implement powder coating for field tools, cultivator frames and sprayer boom coating",
            "Trailer powder coating and hitch and drawbar coating for flatbeds, wagons and towed units",
            "Tractor attachment powder coating for brackets, mounts and bolt-on attachments",
            "Buckets and quick-attach tools, including loader bucket powder coating, skid steer attachments and excavator attachments",
            "Grain handling equipment and livestock handling equipment such as augers, feeders and handling frames"
        ],
        "Long booms, wide implements and heavy trailers are racked so powder reaches every weld and corner, and parts are supported during curing to prevent distortion. Heavy equipment powder coating on thin sheet covers gets extra care to avoid warping.",
        "Oversized parts are handled in our large oven, and the [capabilities page](/capabilities) lists current size and weight limits so you can check a part before sending it. For farm equipment powder coating, we can finish small brackets and larger frames in the same order, which keeps an assembly's colour consistent across every piece.",
        "## Finishes and Specifications for Field-Ready Equipment",
        "Most agricultural machinery powder coating uses a thermoset polyester, epoxy or hybrid powder, applied by electrostatic spray and cured in the oven at roughly 180–200 °C. We match customer colour samples and offer matte, gloss, textured and metallic finishes.",
        "Choosing the right finish is part of agricultural equipment powder coating done well. Texture is a practical choice because it hides weld marks and minor scratches, while gloss wipes clean more easily after fertilizer or field work. Dealer and brand colours can be matched and recorded, so colour-matched replacement parts arrive looking like the original.",
        "A UV-resistant powder coating keeps colour from fading in strong sun, epoxy suits sheltered parts that need hardness, and hybrids balance the two. An outdoor-grade powder suits exposed frames, and the goal is a chemical-resistant finish with real harsh weather durability, so powder coating for agricultural equipment rests on how the part will be used.",
        "We check quality rather than assume it in heavy equipment powder coating, where a thin edge is the first place rust shows. Thickness is measured with a calibrated gauge to ASTM D7091, adhesion can be tested to ASTM D3359, and ASTM B117 corrosion testing is available when a project calls for it. Test reports are provided on request, and our quality steps are documented with the Absolute Bureau of Certification.",
        "In farm equipment powder coating, threaded holes and sliding surfaces are masked with plugs and tape so the finish never interferes with assembly. We plan pin and bushing masking and hydraulic fitting masking on the work order before coating starts, so tell us which surfaces must stay bare.",
        "## How We Work With Equipment Owners and Dealers",
        "Our powder coating for agricultural equipment process runs from quote to delivery in a fixed sequence: inspection, preparation, masking, coating, curing, quality check and packaging. Standard orders leave in 48 hours, and our shop is open Monday to Friday, 7 AM to 5 PM.",
        [
            "1. Send photos or drawings with the quantity, metal and colour you want.",
            "2. We inspect the parts and confirm the prep method, powder and delivery timing in writing.",
            "3. Parts are degreased, blasted if needed, pre-treated and masked.",
            "4. Powder is applied by electrostatic spray and cured at roughly 180–200 °C.",
            "5. Each batch is inspected, then packed to prevent scratches in transit.",
            "6. You pick up at our Milton shop, or we arrange delivery."
        ],
        "For repeat farm equipment powder coating, we keep colour codes and prep notes on file, so later jobs move faster and look the same. Many owners book off-season refurbishment in winter, and equipment dealers can send OEM replacement parts in batches that we log by colour code. Agricultural equipment powder coating is planned around your calendar, and we update you if timing changes. If a part arrives with heavy grease, rust or old coating, we tell you before coating, not after.",
        "## Services Owners Combine With Coating",
        "Farm equipment powder coating is usually paired with preparation and, for older machines, with stripping and refinishing. These are the services most often combined on one work order, so each job stays simple.",
        "Our [industrial powder coating](/services/industrial-powder-coating) service covers heavy structures and attachments. [Surface preparation and pretreatment](/services/surface-preparation) handles degreasing, phosphate treatment and masking, which determines how well the powder bonds. [Sandblasting](/services/sandblasting) removes rust, mill scale and old paint so a rust-resistant powder coating bonds to clean steel, and mobile blasting is available for machines that cannot be moved easily. For worn machines, [stripping and recoating](/services/restoration-recoating) brings a tired frame back to a clean, protected finish. Together these services make agricultural equipment powder coating a one-supplier job, from bare steel to bolt-on ready parts. Teams that finish trailers and attachments in volume often start with blasting, then move to a repeating schedule once the first batch is approved, which makes heavy equipment powder coating predictable from one order to the next.",
        "## Proof From Our Project Work",
        "Our project work shows how we document, prepare and finish large welded steel frames. Each case study lists the client industry, part, metal, size, powder, colour code and turnaround, so you can compare it with your own requirements.",
        "Our [conveyor frame case study for an automotive plant](/projects/conveyor-frame-automotive-plant) shows how we prepare, rack and finish a large welded frame, the same discipline we apply to implement frames and trailers. You can also browse the [project gallery](/projects) for other fabricated steel parts. Each job reflects how we approach agricultural equipment powder coating: document the part, agree the preparation, record the colour code and deliver on the date we promised. Reviewing these examples helps owners judge whether our heavy equipment powder coating suits their needs before they send parts.",
        "Ready to protect your implements, trailers or attachments with a tough, field-ready finish? Request a quote today. Call (905) 876-7060 or email us, and our team will reply during shop hours, Monday to Friday, 7 AM to 5 PM."
    ],
    "faqs": [
        [
            "Is powder coating suitable for tractor attachments and implements?",
            "Yes. Agricultural machinery powder coating gives attachments and implements a hard, uniform finish that resists soil, chemicals and cleaning. It forms a continuous barrier that resists moisture better than conventional wet paint, and our pretreatment promotes good adhesion to welded steel. Tell us about the working conditions when you request a quote so we can recommend the right powder."
        ],
        [
            "What is your turnaround time on farm equipment?",
            "Standard orders take 48 hours once parts are received and the specification is approved. Large implements or orders requiring heavy sandblasting can take longer, and we confirm the schedule before work starts. If you have a planting or harvest deadline, tell us early so we can reserve oven time."
        ],
        [
            "How do I get a quote for powder coating equipment?",
            "Use our quote form or call (905) 876-7060 with part dimensions, metal type, quantity and current condition. Photos help us identify weld seams, old paint or heavy rust that may need extra preparation. We will reply with a detailed price and lead time during shop hours, Monday to Friday, 7 AM to 5 PM."
        ],
        [
            "Can you coat used or rusted equipment?",
            "Yes. We regularly refinish used implements, trailers and attachments. Old paint, grease and rust are removed through degreasing and sandblasting to achieve clean bare steel before pretreatment and powder application. We inspect every used part and will notify you if repairs or welding are needed before coating."
        ],
        [
            "Do you offer pickup and delivery for heavy parts?",
            "Yes. We can coordinate pickup and delivery across Milton, Halton, Peel, Hamilton and the Waterloo Region for large or heavy equipment. Our shop has forklift capacity up to 6,000 lb for safe offloading. Mention delivery requirements when you submit your quote request."
        ]
    ]
}

# 3. RESTORE CONTRACTORS & CONSTRUCTION
up["industries"]["contractors-construction"] = {
    "meta_title": "Powder Coating for Contractors | Koojo Powder Coating",
    "meta_desc": "Powder coating for contractors: durable finishes on structural steel, stair stringers and site metalwork. 48-hour turnaround on standard orders. Get a quote.",
    "primary_kw": "powder coating for contractors",
    "h1": "Powder Coating for Contractors",
    "summary": "Coated railings, structural pieces and site metalwork for steel erectors and railing installers, packaged for site delivery.",
    "body": [
        "Powder coating for contractors gives structural steel and site-built metalwork a tough, even finish that survives handling, weather and long project schedules. Koojo Custom Powder Coating works from 10874 Steeles Ave E in Milton, Ontario, and has finished more than 10,000 items since 2012. Our contractor powder coating service is built for general contractors, steel installers and railing installers who need dependable lead times and parts that arrive ready to install.",
        "Standard orders carry a 48-hour turnaround, and our team is available Monday to Friday, 7 AM to 5 PM. Send drawings, photos or a sample part, and we will confirm the prep method, powder and delivery date before work begins. If your steel is fabricated and waiting for a finish, [request a quote](/get-a-quote) and we will reply with a clear plan. That is what powder coating for contractors should deliver: a finish that lasts and steel that arrives on time.",
        "Since 2012 | 10,000+ Items | 48 Hr Turnaround | 5.0 ★ Google Rating",
        "## Coating Challenges in Contractors & Construction",
        "Construction powder coating is hard to get right because the steel is large, handled roughly and installed on someone else's schedule. The main challenges are weather exposure, mill scale and rust on raw steel, damage in transport and site delivery windows that leave little room for rework.",
        "Raw steel sections and angles often carry mill scale or surface rust, and both stop powder from bonding unless they are removed first. Large fabrications are heavy, so racking, oven loading and handling need planning to avoid marks. Once installed, a finish faces rain, sun and winter conditions for years, which makes preparation more important than colour. Powder coating for construction succeeds when cleaning, curing and protective packaging are treated as one job.",
        "Schedule is the other pressure. A crew waiting on steel cannot start the next phase, so a finisher has to hold a promised date and speak up early if something changes. Contractor powder coating also has to match across a project: parts coated in different weeks should still look like one set.",
        "Several trades often share one structure, so steel from different suppliers has to look consistent. A contractor who sends parts to more than one shop risks colour drift, which is why many teams keep construction powder coating with one finisher for a whole project.",
        "## Parts and Metals We Coat for Contractors",
        "We coat structural steel and site-built metalwork, including steel beams, lintels, stair stringers, platforms and ladders, canopy frames, brackets and embeds, site hardware, supports and custom metalwork. Parts range from small hardware runs to oversized assemblies within our 6,000 lb capacity.",
        "Mild steel is the most common metal in construction powder coating, and it responds well to blasting and phosphate pre-treatment before coating. Aluminum extrusions and architectural panels are cleaned and pre-treated differently so the powder bonds without blistering. Our powder coating for contractors covers the following components:",
        [
            "Structural steel powder coating: beams, columns, lintels, baseplates and embeds",
            "Architectural metalwork powder coating: railings, guards, handrails and decorative screens",
            "Stair stringers, platforms, catwalks, ladders and safety cages",
            "Canopy frames, shade structures, brackets and facade supports",
            "Site hardware, bollards, sign posts, fence posts and custom construction metalwork"
        ],
        "Long railings, wide frames and heavy beams are racked so powder reaches every surface, and parts are supported during curing to prevent bowing. Powder coating for construction on thin decorative panels gets extra care to prevent heat distortion.",
        "Oversized parts are handled in our large oven, and the [capabilities page](/capabilities) lists current size and weight limits so you can check a part before sending it. For contractor powder coating, we can coat brackets and structural members in the same order, which keeps colour and gloss identical across the entire build.",
        "## Finishes and Specs for Construction Steel",
        "Most construction powder coating uses a thermoset polyester, super-durable polyester or hybrid powder, applied by electrostatic spray and cured in the oven at roughly 180–200 °C. We match project specifications and RAL colour codes, and offer matte, gloss, satin and textured finishes.",
        "Choosing the right finish is part of powder coating for contractors done well. Texture is popular for railings and stairs because it hides weld marks and light site scuffs, while smooth gloss sheds dirt and wipes clean easily. Brand and architect colours can be matched and recorded on the work order, so replacement parts match the original build.",
        "A weather-resistant powder coating protects steel from UV fading and chalking, epoxy primer adds corrosion defense under coastal or de-icing salt exposure, and super-durable polyesters provide ten-year gloss retention. An exterior-rated powder suits exposed canopies and railings, and the goal is an exterior metalwork finish with proven durability.",
        "We verify quality rather than assume it in commercial powder coating, where an exposed weld seam is the first place corrosion begins. Thickness is measured with a calibrated gauge to ASTM D7091, adhesion can be tested to ASTM D3359, and ASTM B117 salt spray testing results can be provided on request. Test reports are available on request, and our quality processes are documented with the Absolute Bureau of Certification.",
        "In powder coating for building contractors, bolt holes, threaded inserts and field-weld margins are masked with plugs and tape so the finish does not interfere with erection. We confirm masking requirements on the work order before coating begins, so let us know which surfaces must stay bare.",
        "## How We Work With Contractors",
        "Our powder coating for contractors process runs from quote to site delivery in a clear, documented sequence: review, cleaning, masking, coating, curing, inspection and protective packaging. Standard orders leave in 48 hours, and our shop is open Monday to Friday, 7 AM to 5 PM.",
        [
            "1. Send drawings or cut lists with quantities, steel sizes and the required finish spec.",
            "2. We review the drawings, confirm prep, powder and schedule in writing.",
            "3. Steel is degreased, blasted to remove mill scale/rust, pretreated and masked.",
            "4. Powder is applied electrostatically and cured at 180–200 °C.",
            "5. Parts are inspected for thickness and coverage, then wrapped for site protection.",
            "6. You pick up in Milton, or we coordinate timed delivery directly to your job site."
        ],
        "For multi-phase construction powder coating, we record colour batch numbers and prep notes on file so steel finished in later phases matches earlier deliveries. Project managers can send phased deliveries that align with crane and erection dates, and we update you promptly on schedule. If steel arrives with heavy mill scale, oil or transport rust, we notify you before work starts.",
        "## Services Contractors Combine",
        "Contractor powder coating is often paired with surface preparation, blasting and specialty finishing. These services are handled under one roof, keeping project management simple.",
        "Our [industrial powder coating](/services/industrial-powder-coating) service handles heavy beams, columns and framing. [Surface preparation and pretreatment](/services/surface-preparation) degreases, cleans and applies conversion coatings for reliable bonding. [Sandblasting](/services/sandblasting) strips mill scale, weld slag and surface rust back to clean metal so powder adheres securely. For architectural elements, [custom colours and finishes](/services/custom-colors-finishes) provides exact RAL colour matching and architectural textures. Together, these services make powder coating for contractors an efficient one-stop process from raw fabrication to site-ready steel.",
        "## Proof From Real Projects",
        "Our project portfolio demonstrates how we manage, prep and finish heavy construction steel and architectural metalwork. Each case study documents the metal, dimensions, finish specification and turnaround.",
        "Our [safety bollards case study](/projects/safety-bollards) illustrates our approach to high-durability exterior finishes for construction and municipal applications. You can also view our [project gallery](/projects) for additional examples of architectural railings and heavy assemblies. Each job demonstrates our commitment to contractor powder coating: understand the project schedule, prep the steel thoroughly, apply an even coat and deliver on the promised date.",
        "Ready to protect your construction steel and architectural metalwork? Request a quote today. Call (905) 876-7060 or email us, and our team will reply during shop hours, Monday to Friday, 7 AM to 5 PM."
    ],
    "faqs": [
        [
            "Is powder coating suitable for outdoor construction steel?",
            "Yes. Powder coating for contractors provides superior protection against UV exposure, rain, snow and road salt when paired with proper blast cleaning and an exterior-grade polyester or super-durable topcoat. It creates a tough, flexible film that resists impact during transit and installation, making it ideal for railings, stairs, canopy framing and site steel."
        ],
        [
            "What is your turnaround time for contractor orders?",
            "Standard orders are completed in 48 hours once steel is received and the finish specification is confirmed. Large structural assemblies or high-volume multi-piece packages may require additional scheduling, which we confirm upfront in writing. We can also coordinate phased deliveries to match your site erection milestones."
        ],
        [
            "How do I submit structural steel drawings for quoting?",
            "Submit your PDF fabrication drawings, cut lists or photos through our online quote form or email them to sales@koojopowdercoating.com. Include part counts, steel grades, required powder or RAL colour codes, and target site delivery dates. We will provide a formal quotation during shop hours."
        ],
        [
            "Can you match architectural colour specifications?",
            "Yes. We stock a broad range of standard RAL colours and can match specific architect codes, brand standards or sample chips. We offer matte, satin, gloss and textured finishes, and we log powder codes on file so replacement parts or later building phases match seamlessly."
        ],
        [
            "How is coated steel protected during transport to the job site?",
            "Every piece is inspected, wrapped in protective foam or plastic sheeting, and packed to prevent metal-to-metal contact during shipping. We load carefully to accommodate forklift or crane offloading at your facility or site."
        ],
        [
            "Do you handle oversized structural sections?",
            "Yes. Our facility features a 23 ft curing oven and crane equipment rated up to 6,000 lb, accommodating long stair stringers, beams, canopy frames and wide gates. Check our capabilities page or call us with part dimensions to confirm rack layout."
        ]
    ]
}

# 4. RESTORE FOOD PROCESSING EQUIPMENT
up["industries"]["food-processing-equipment"] = {
    "meta_title": "Powder Coating for Food Processing Equipment | Koojo",
    "meta_desc": "Powder coating for food processing equipment: washdown-resistant finishes for conveyor frames, guards and line equipment. 48-hour turnaround. Get a quote.",
    "primary_kw": "powder coating for food processing equipment",
    "h1": "Powder Coating for Food Processing Equipment",
    "summary": "Washdown-resistant coatings for frames, conveyors and guards in food plants, with compliance documentation.",
    "body": [
        "Powder coating for food processing equipment gives conveyor frames, supports and machine guards a smooth, chemical-resistant finish that withstands daily high-pressure washdowns and sanitizing chemicals. Koojo Custom Powder Coating operates from 10874 Steeles Ave E in Milton, Ontario, and has coated more than 10,000 items since 2012. Our food equipment powder coating service is tailored for food plant fabricators, equipment OEMs and facility maintenance managers who need dependable lead times and hygienic, durable finishes.",
        "Standard orders carry a 48-hour turnaround, and our facility operates Monday to Friday, 7 AM to 5 PM. Provide part drawings, photos or equipment specifications, and we will confirm surface preparation, powder selection and turnaround before coating. If you have line frames, brackets or guards scheduled for finishing, [request a quote](/get-a-quote) and our technical team will respond with a clear schedule. That is what sanitary equipment finishing should provide: dependable corrosion defense and a partner who respects plant hygiene standards.",
        "Since 2012 | 10,000+ Items | 48 Hr Turnaround | 5.0 ★ Google Rating",
        "## Coating Challenges in Food Processing Equipment",
        "Food processing powder coating must endure demanding operating conditions: daily hot water washdowns, aggressive cleaning detergents, caustic sanitizers and constant moisture. The core challenges include preventing under-film corrosion, eliminating crevices that harbour bacteria, resisting chemical attack and meeting regulatory hygiene expectations.",
        "Equipment frames and enclosures combine hollow tubing with welded brackets, and trapped moisture or chemical residues inside seams can lead to premature failure if not properly pretreated. Caustic cleaners and acid sanitizers degrade conventional coatings quickly, causing flaking or chipping that risks contaminating food processing lines. Washdown-tolerant powder coating requires thorough degreasing, conversion coating and a continuous, defect-free cured film that seals edges and corners completely.",
        "Tolerance control is equally critical. Conveyor frames, bearing mounts and drive housings require clean bare metal on mating surfaces, shaft journals and threaded adjustment points. Food manufacturing powder coating demands precision masking so that sanitation crews can clean equipment easily while mechanical assemblies fit together without post-coating modification.",
        "Maintenance windows in operating food plants are extremely tight. Facility managers cannot tolerate extended downtime for recoating or delivery delays. A coating supplier must deliver on the promised date so sanitation and maintenance teams can reassemble lines before the next production shift begins.",
        "## Parts and Metals We Coat for Food Plants",
        "We coat carbon steel frames, aluminum guards and stainless brackets used throughout food packaging, sorting and processing environments. Typical components include conveyor frames, sanitary washdown line frames, motor mounts, safety guarding and structural supports up to our 6,000 lb capacity.",
        "Carbon steel is widely coated for non-food-contact frames and structural supports, benefiting from iron phosphate pretreatment and chemical-resistant topcoats. Aluminum covers and guards are prepared to ensure strong adhesion without outgassing. Our powder coating for food processing equipment covers the following components:",
        [
            "Food conveyor powder coating: conveyor frames, roller brackets, guide rails and bed sections",
            "Sanitary frame powder coating: line support frames, work tables, stands and platform structures",
            "Equipment guard powder coating: mesh guards, safety enclosures, drive covers and access panels",
            "Machinery mounts, motor bases, bracketry and electrical enclosure housings",
            "Packaging line frames, sorting chutes, palletizing supports and material handling structures"
        ],
        "Long conveyor beds, bulky frames and heavy support structures are racked to ensure complete powder penetration across all welds and underside surfaces. Food industry metal finishing requires even heat distribution so heavy tubular members reach proper cure temperature throughout.",
        "Oversized frames are processed in our 23 ft curing oven, and the [capabilities page](/capabilities) provides comprehensive dimensions and weight limits. For food equipment manufacturers, we can coat mounting brackets, guards and main line frames in matching batches, ensuring uniform appearance across the complete machine line.",
        "## Finishes and Specs for Washdown Equipment",
        "Most food manufacturing powder coating utilizes thermoset epoxy, hybrid or polyester powders formulated for superior chemical resistance and high-pressure washdown tolerance. We offer smooth high-gloss and semi-gloss finishes that promote easy cleaning and prevent debris retention.",
        "Selecting the proper powder formulation is central to powder coating for food processing equipment. Smooth, non-porous finishes are strongly preferred because they eliminate microscopic surface voids where bacteria or food residue could collect. White and light grey finishes are standard in processing environments because they highlight cleanliness and make residue easily visible during inspections.",
        "Epoxy powder coatings offer unmatched chemical and detergent resistance, making them ideal for splash-zone frames and supports that encounter regular chemical washdowns. Polyester hybrids balance washdown resilience with impact resistance, while exterior-grade topcoats protect components exposed to sunlight in receiving or loading dock areas.",
        "Quality verification is rigorous. Coating thickness is verified with a calibrated electromagnetic gauge per ASTM D7091, cross-hatch adhesion can be tested to ASTM D3359, and salt spray resistance references ASTM B117 standards. Quality documentation and powder manufacturer technical data sheets (TDS) are available on request, and our operations are certified through the Absolute Bureau of Certification.",
        "In hygienic equipment powder coating, precision masking protects sanitary clamp flanges, bearing bores, sensor mounts and threaded leveling feet with high-temperature silicone plugs and tape. We review masking callouts before coating to ensure no powder enters mechanical or electrical interfaces.",
        "## How We Work With Food Equipment Makers and Plants",
        "Our process for food processing powder coating follows a systematic, documented sequence designed to deliver consistent, sanitary finishes on schedule:",
        [
            "Step 1 – Intake and Inspection: Review engineering drawings, verify metal substrate, check for weld spatter or sharp burrs, and confirm sanitary requirements.",
            "Step 2 – Cleaning and Pretreatment: Degrease to remove machining oils, apply phosphate conversion coating for corrosion resistance, and dry thoroughly.",
            "Step 3 – Masking and Powder Application: Apply precision plugs and high-temp tape to mounting pads, bores and threads. Electrostatic application ensures uniform wrap around complex tubing.",
            "Step 4 – Oven Curing: Cure in our 23 ft oven at 180–200 °C metal temperature, ensuring heavy structural sections achieve complete polymerization.",
            "Step 5 – Final Inspection and Handoff: Verify film thickness, inspect for pinholes or voids, wrap in protective materials, and stage for pickup or jobsite delivery."
        ],
        "For equipment OEMs with ongoing production programs, we maintain detailed powder codes, racking configurations and masking templates on file. When plant maintenance schedules demand emergency weekend or turnaround support, we work with facility coordinators to minimize operational downtime.",
        "## Services Food Plants Use Most",
        "Food processing powder coating is frequently paired with specialized surface prep and refurbishing services under one roof:",
        "Our [industrial powder coating](/services/industrial-powder-coating) handles large structural conveyor sections and washdown line assemblies. [Surface preparation and pretreatment](/services/surface-preparation) ensures total removal of oils and residues for maximum coating adhesion. [Sandblasting](/services/sandblasting) strips rust, scale and degraded coatings from older equipment frames prior to recoating. For refurbished lines, our [restoration and recoating](/services/restoration-recoating) service strips existing paint and applies fresh sanitary-grade powder, extending the service life of capital equipment.",
        "## Recent Project: Food Processing Line Frame",
        "Our [food processing line frame case study](/projects/food-processing-line-frame) showcases how we clean, prep, mask and coat large structural frames for food plant service. The project details the steel substrate, chemical washdown requirements, powder specification, precision masking of datum pads and 48-hour delivery timeline.",
        "Reviewing our case study illustrates our rigorous approach to powder coating for food processing equipment: strict adherence to hygiene standards, documented quality control and dependable turnaround. Browse our complete [project gallery](/projects) for additional equipment examples.",
        "Ready to protect your food processing conveyors, frames and line guards? Request a quote today. Call (905) 876-7060 or email us, and our team will respond during shop hours, Monday to Friday, 7 AM to 5 PM."
    ],
    "faqs": [
        [
            "Is powder coating suitable for food-contact surfaces?",
            "Direct food-contact surfaces are typically fabricated from 304 or 316 stainless steel. Powder coating is primarily applied to non-food-contact frames, structural supports, safety guarding, conveyor beds and motor mounts located in splash and non-splash zones. Where specific food-grade or FDA-compliant powder formulations are required near product streams, we review specifications and provide manufacturer compliance documentation."
        ],
        [
            "How does powder coating withstand daily chemical washdowns?",
            "Cured epoxy and hybrid powder coatings form a dense, cross-linked polymer barrier that resists hot water, high-pressure spray, alkaline cleaners and sanitizing chemicals far better than traditional liquid paint. Proper conversion coating underneath prevents under-film moisture migration and corrosion creeping."
        ],
        [
            "What turnaround times do you offer for plant maintenance shutdowns?",
            "Standard production orders are completed in 48 hours. For planned plant maintenance shutdowns or emergency repairs, we can coordinate dedicated oven scheduling to return coated frames and guards within your maintenance window. Contact us ahead of your shutdown to reserve capacity."
        ],
        [
            "Do you provide documentation for plant sanitation audits?",
            "Yes. We can provide powder manufacturer technical data sheets (TDS), safety data sheets (SDS) and coating inspection reports detailing dry film thickness and adhesion test records to support your quality and sanitation audit records."
        ],
        [
            "How do you prevent powder from entering bearing bores and tapped holes?",
            "We utilize high-temperature silicone plugs, tapered caps and specialist masking tapes rated to oven cure temperatures. Mating surfaces, shaft passages, ground points and tapped holes are masked per your engineering drawings and inspected prior to packing."
        ],
        [
            "Can you coat large conveyor frames and bulky washdown assemblies?",
            "Yes. Our 23 ft long oven and 6,000 lb handling capacity easily accommodate long modular conveyor sections, multi-bay equipment stands, overhead hanger rails and heavy drive frames. Consult our capabilities page for details."
        ]
    ]
}

# 5. RESTORE MACHINE SHOPS
up["industries"]["machine-shops"] = {
    "meta_title": "Powder Coating for Machine Shops | Koojo Powder Coating",
    "meta_desc": "Powder coating for machine shops: precision masking of threads and bores, fast turnaround on CNC parts, brackets and housings. Get a quote.",
    "primary_kw": "powder coating for machine shops",
    "h1": "Powder Coating for Machine Shops",
    "summary": "Precision masking of threads, bores and machined faces, and careful handling of small-part batches.",
    "body": [
        "Powder coating for machine shops is defined by what remains uncoated. Precision threads, reamed bores, ground datum faces and sliding interfaces must stay strictly bare and within tolerance, while exposed surfaces receive a durable, uniform protective finish. Koojo Custom Powder Coating operates from 10874 Steeles Ave E in Milton, Ontario, and has coated over 10,000 components since 2012. Our machine shop powder coating service is specifically designed for CNC machinists, tool-and-die shops and precision fabricators who require meticulous masking, dependable 48-hour turnarounds and zero compromise on mechanical fit.",
        "Standard orders carry a 48-hour turnaround, and our shop is open Monday to Friday, 7 AM to 5 PM. Provide drawings with marked masking callouts or sample parts, and we will confirm preparation, masking strategy and turnaround before work starts. If your machined components are deburred and ready for finishing, [request a quote](/get-a-quote) and our technical team will respond promptly. That is what precision coating should provide: exact tolerance protection and finishes that enhance your machined products.",
        "Since 2012 | 10,000+ Items | 48 Hr Turnaround | 5.0 ★ Google Rating",
        "## Coating Challenges in Machine Shops",
        "Powder coating for machined parts is demanding because the finish must protect exterior surfaces without encroaching onto precision dimensions, tapped threads, bearing pockets or sealing faces. The primary challenges include cutting fluid residue, strict tolerance limits, sharp edge coverage, and small batches that still require fast, repeatable turnarounds.",
        "Coolant and cutting oils soak into machined surfaces and microscopic tool marks, causing outgassing, craters or adhesion failure if not completely eliminated during degreasing. Sharp machined corners cause electrostatic Faraday cage effects and can pull powder thin, while powder overspray inside a reamed hole or ground bore will ruin a press fit. Successful powder coating for CNC parts requires thorough chemical cleaning, precise plugging and controlled film thickness.",
        "Batch variability is another continuous factor. A precision shop might send twenty milled brackets today, five large machine bases next week, and a single prototype fixture the following day. Machine shop powder coating relies on recorded masking instructions and archived RAL colour codes so that batch-to-batch consistency remains flawless across recurring production runs.",
        "Handling mixed metals also requires discipline. Aluminum, steel, cast iron and stainless parts require tailored cleaning routines and differing cure profiles. Precision thin-wall components heat faster than heavy machine platens, so a professional coater must plan oven loads carefully so no part is under-cured or overheated.",
        "## Parts and Metals We Coat for Machine Shops",
        "We coat CNC machined components in aluminum, carbon steel, alloy steel and stainless steel, including precision housings, brackets, machine bases, tooling fixtures and protective enclosures up to our 6,000 lb capacity.",
        "Milled aluminum housings and electronic covers are chemically cleaned for optimal adhesion and commonly finished in fine-texture black or custom RAL colours. Steel weldments, plates and machine bases receive degreasing and phosphate conversion coating to resist corrosion. Our powder coating for machine shop parts covers:",
        [
            "CNC machined parts: housings, enclosures, valve bodies, manifolds and sensor brackets",
            "Steel brackets, mounts, motor adaptors, platens and fabricated machine bases",
            "Tooling fixtures, inspection jigs and assembly aids used on your shop floor",
            "Shafts, rollers and spindles with bearing journals and precision diameters masked",
            "Pneumatic, hydraulic and pump components requiring clean sealing faces and ports"
        ],
        "Racking points are planned carefully on non-critical, non-cosmetic areas so hanger marks never appear on functional surfaces. Our [capabilities page](/capabilities) provides complete size and weight parameters so you can verify oversized components before shipping.",
        "Complex geometry is evaluated prior to coating. Blind tapped holes, deep internal cavities and keyways are protected with custom silicone plugs, caps and high-temperature tape. For machine shops producing branded machinery, we can coat precision parts alongside structural frames, ensuring uniform finish across the entire machine.",
        "## Finishes and Specs for Machined Parts",
        "Most machine shop powder coating utilizes thermoset polyester, epoxy or hybrid powders applied electrostatically and cured at 180–200 °C. We match exact RAL colour numbers and provide matte, satin, gloss and fine-texture options.",
        "Film thickness control is vital on machined components. Standard powder coating deposits 2.5 to 4.5 mils (60–115 µm), which significantly impacts sliding fits or tight clearances. We review drawings at the quote stage to confirm whether critical surfaces should be masked or if tolerances allow for coating thickness. Fine-texture matte finishes are especially popular for housings and covers because they mask light tool marks, surface variations and handling marks.",
        "Colour consistency is maintained across reorders. We archive the exact powder manufacturer, product code and application parameters for every customer part number, ensuring repeat runs match earlier shipments perfectly.",
        "Quality control is verified through calibrated instruments. Coating thickness is measured per ASTM D7091, cross-hatch adhesion can be tested per ASTM D3359, and salt spray testing references ASTM B117. Inspection documentation is available on request, and our quality processes are certified through the Absolute Bureau of Certification.",
        "Precision masking is executed with high-grade silicone tapered plugs, threaded caps and polyimide tape rated to withstand 200 °C cure cycles. Every plug and tape application is inspected prior to powder spraying and verified after cure.",
        "## How We Work With Machine Shops",
        "Our process for machine shop powder coating is structured to deliver exact masking compliance and rapid turnarounds:",
        [
            "1. Review drawings or marked-up photos identifying bare faces, tapped holes and critical datum features.",
            "2. Confirm masking requirements, powder chemistry, colour code and schedule in writing.",
            "3. Degrease parts thoroughly to remove all coolant and oil residues, followed by conversion coating.",
            "4. Install silicone plugs, caps and high-temp masking tape according to drawing callouts.",
            "5. Apply powder electrostatically and cure at 180–200 °C with controlled ramp rates.",
            "6. Remove all masking, inspect threads and bores, verify coating thickness, and package parts with protective interleaving."
        ],
        "For recurring CNC production runs, we create dedicated part-masking templates so subsequent orders move through receiving and prep without delay. If a part arrives with burrs, thread damage or heavy oxidation, we contact your production manager before proceeding.",
        "## Services Machine Shops Combine",
        "Machine shops often combine powder coating with specialized preparation and finishing services:",
        "Our [surface preparation and pretreatment](/services/surface-preparation) ensures thorough removal of cutting fluids, machine oils and residues. For heavy weldments or parts with heat treat scale, [sandblasting](/services/sandblasting) delivers a clean, uniform profile for powder adhesion. [Industrial powder coating](/services/industrial-powder-coating) handles large fabricated machine bases and structural frames. For parts requiring exact brand identity, [custom colours and finishes](/services/custom-colors-finishes) provides precise colour matching. Together, these services provide machine shops with an integrated finishing partner for components and assemblies.",
        "## Proof From the Shop Floor",
        "Our [robotic base case study](/projects/robotic-base) illustrates our approach to finishing heavy machined fabrications with precision datum pads and tight tolerance requirements. The study details the structural steel substrate, powder formulation, masking execution and 48-hour delivery timeline.",
        "Reviewing our case studies provides CNC shop managers with concrete evidence of our quality standards, masking accuracy and schedule dependability. Browse our [project gallery](/projects) for additional examples of coated precision equipment.",
        "Ready to protect your CNC machined parts, brackets or machine bases with precision masking? Request a quote today. Call (905) 876-7060 or email us, and our team will respond during shop hours, Monday to Friday, 7 AM to 5 PM."
    ],
    "faqs": [
        [
            "Can you keep powder coating completely out of tapped holes and bores?",
            "Yes. We stock high-temperature silicone tapered plugs, threaded masking plugs and caps in standard metric and imperial sizes. Threads, reamed dowel holes and bearing bores are plugged prior to coating and remain completely free of powder and paint residue."
        ],
        [
            "How much thickness does powder coating add to machined surfaces?",
            "A standard single-coat powder application adds approximately 2.5 to 4.5 mils (60 to 115 microns) of dry film thickness per surface. If a dimension is critical to an assembly fit, flag it on your drawing so we can mask the surface or recommend an appropriate tolerance allowance."
        ],
        [
            "Do you take small batches and prototype quantities from machine shops?",
            "Yes. We routinely handle single prototypes, first-article samples and small production batches of five to fifty pieces. Every job receives the same careful masking and inspection."
        ],
        [
            "How do you remove cutting oils and coolants before coating?",
            "Parts undergo thorough solvent and alkaline degreasing followed by hot water rinsing and forced-air drying to ensure all coolant residues and tramp oils are completely removed from blind holes, slots and surface pores."
        ],
        [
            "What is your standard turnaround time for machined parts?",
            "Standard orders are completed within 48 hours from receiving parts and approved masking instructions. For urgent production runs or assembly deadlines, let us know when booking and we will accommodate your timeline."
        ],
        [
            "Can you match custom RAL colour codes for equipment OEM builds?",
            "Yes. We stock and source thousands of RAL colour codes in matte, satin, gloss and textured finishes. We record the powder formula and cure parameters on file so repeat orders match previous runs exactly."
        ]
    ]
}

with open("scripts/seed/uploaded_content.json", "w", encoding="utf-8") as f:
    json.dump(up, f, indent=2, ensure_ascii=False)

print("SUCCESS: Updated uploaded_content.json with Industries Hub and 4 Subpages!")
