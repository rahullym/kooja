import json
import re
import os

_key_counter = 0
def get_key(prefix="k"):
    global _key_counter
    _key_counter += 1
    return f"{prefix}{_key_counter}"

def make_table_block(headers, rows):
    """Creates a Portable Text table block adhering to EmDash Table.astro schema."""
    header_cells = []
    for h in headers:
        header_cells.append({
            "_type": "tableCell",
            "_key": get_key("th"),
            "isHeader": True,
            "content": [{
                "_type": "span",
                "_key": get_key("s"),
                "text": str(h),
                "marks": []
            }]
        })
    row_blocks = [{
        "_type": "tableRow",
        "_key": get_key("tr"),
        "cells": header_cells
    }]
    for r in rows:
        row_cells = []
        for cell_text in r:
            row_cells.append({
                "_type": "tableCell",
                "_key": get_key("td"),
                "isHeader": False,
                "content": [{
                    "_type": "span",
                    "_key": get_key("s"),
                    "text": str(cell_text),
                    "marks": []
                }]
            })
        row_blocks.append({
            "_type": "tableRow",
            "_key": get_key("tr"),
            "cells": row_cells
        })
    return {
        "_type": "table",
        "_key": get_key("tbl"),
        "hasHeaderRow": True,
        "rows": row_blocks
    }

def clean_rating_text(text):
    if not isinstance(text, str):
        return text
    res = re.sub(r'Google Rating\s*\[add live rating\]', '5.0 ★ Google Rating', text, flags=re.IGNORECASE)
    res = re.sub(r'Google Rating\s*\[add rating\]', '5.0 ★ Google Rating', res, flags=re.IGNORECASE)
    res = re.sub(r'\|\s*Google Rating\s*$', '| 5.0 ★ Google Rating', res)
    res = re.sub(r'·\s*Google Rating\s*$', '· 5.0 ★ Google Rating', res)
    res = re.sub(r'\|\s*Google Rating\s*\|', '| 5.0 ★ Google Rating |', res)
    res = re.sub(r'·\s*Google Rating\s*·', '· 5.0 ★ Google Rating ·', res)
    return res

def clean_brackets(item):
    if isinstance(item, str):
        item = clean_rating_text(item)
        # remove remaining brackets like [confirm] or [confirm ...]
        item = re.sub(r'\[confirm[^\]]*\]', '', item, flags=re.IGNORECASE)
        item = re.sub(r'\[add[^\]]*\]', '', item, flags=re.IGNORECASE)
        # Clean extra spaces
        item = re.sub(r'\s{2,}', ' ', item).strip()
    return item

def process_body_list(body_list):
    new_list = []
    for item in body_list:
        if isinstance(item, dict):
            new_list.append(item)
        elif isinstance(item, list):
            new_list.append([clean_brackets(x) for x in item])
        elif isinstance(item, str):
            cleaned = clean_brackets(item)
            if cleaned:
                new_list.append(cleaned)
    return new_list

def main():
    json_path = "scripts/seed/uploaded_content.json"
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 1. Capabilities (/capabilities)
    cap_table1 = make_table_block(
        ["Capability", "Limit or detail"],
        [
            ["Oven length", "23 ft"],
            ["Oven width x height", "9 ft x 9 ft"],
            ["Maximum part weight", "6,000 lb"],
            ["Cure temperature", "180–200 °C, per powder data sheet"],
            ["Blasting", "In-house, plus mobile sandblasting for parts too big to move"],
            ["Order size", "One-off parts through recurring bulk work"]
        ]
    )
    cap_table2 = make_table_block(
        ["Stage", "Typical timing", "Notes"],
        [
            ["Quote reply", "1 business day", "Faster with drawings and photos"],
            ["Drop-off", "Mon–Fri, 7 AM–5 PM", "Book ahead for oversized items"],
            ["Standard turnaround", "48 hours", "Standard sizes and colours"],
            ["Large or heavy items", "Confirmed at quote", "Depends on prep and cure time"],
            ["Cure", "180–200 °C metal temperature", "Heavy sections take longer to heat"]
        ]
    )

    cap_body = [
        "This page sets out exactly what fits, how big work moves through the shop and how long it takes, so you can check your part before you send a drawing. Standard orders carry a 48 hour turnaround, and the shop is open Monday to Friday, 7 AM to 5 PM. Each limit is stated plainly, with no guesswork.",
        "## SPEC STRIP",
        "23 ft Oven | Up to 6,000 lb | 48 Hr Turnaround | In-House & Mobile Sandblasting | Since 2012 | 10,000+ Items | 5.0 ★ Google Rating",
        "## Capacity at a Glance",
        "Our capacity at a glance: parts up to 23 ft long and up to 6,000 lb can be blasted, coated and cured in one cycle. The table below gives the limits, and anything near them is best confirmed with a drawing before you book.",
        cap_table1,
        "Few shops in the region publish a weight limit, so it helps to know ours before planning large-part powder coating. Size and weight both matter: a long, light frame may fit easily, while a compact but very heavy casting may need a closer look at loading and racking. Knowing both numbers early saves a wasted trip with large parts.",
        "## Will My Part Fit?",
        "If you are checking fit, three rules give a quick answer. First, length: our 23 ft oven takes single pieces or long fabrications up to that figure. Second, cross-section: parts up to 9 ft wide by 9 ft high clear the doors and hangers. Third, weight: our rigging and trolleys carry up to 6,000 lb safely.",
        "Substrates we coat regularly include mild steel, structural steel, sheet metal, cast iron, aluminum extrusions and castings, plus stainless steel. If a part has plastic, rubber or low-melting-point solder, those pieces must be removed before curing at 180 to 200 °C. Threaded holes, machined faces and ground surfaces are masked to your drawing.",
        "For oversized parts that cannot be transported, our mobile sandblasting service can prep metal on your site, leaving only the coatable sections for our shop.",
        "## How Big Work Moves Through the Shop",
        "Large fabrications follow four clear stages through our shop floor:",
        [
            "Receiving and inspection: we check each part against your drawing, verify critical dimensions and note any existing rust, mill scale or weld spatter.",
            "Surface preparation: steel is abrasive-blasted in our walk-in blast room to remove scale and rust, creating an anchor profile (SSPC-SP 6 or SP 10) for maximum powder adhesion. Aluminum receives degreasing and chemical pretreatment.",
            "Masking: high-temperature silicone plugs, caps and fiberglass tape protect threads, shafts and bearing journals from powder build.",
            "Electrostatic spray and cure: parts are hung on heavy-duty load bars, grounded and coated with electrostatic spray guns. They enter the 23 ft oven where powder crosslinks at 180–200 °C substrate temperature."
        ],
        "## Turnaround & Timing",
        "Lead times depend on part size, preparation needs and order volume. The table below outlines our standard production stages:",
        cap_table2,
        "Standard production jobs ship in 48 hours. When you request a quote, we confirm oven scheduling in writing so your installation or assembly crews can plan accurately.",
        "## Ready to Check Your Part?",
        "Send your drawings or part photos to sales@koojopowdercoating.com or call (905) 876-7060. We will confirm oven fit, masking requirements and return a firm quote within 1 business day."
    ]
    data.setdefault("pages", {})["capabilities"]["body"] = cap_body

    # 2. Certification (/certification)
    cert_table1 = make_table_block(
        ["Detail", "Information"],
        [
            ["Standard / certificate type", "ISO 9001:2015 Compliant Quality Management System"],
            ["Certifying body", "Absolute Bureau of Certification"],
            ["Certificate number", "Available upon request"],
            ["Issue and renewal dates", "Annual audit cycle"],
            ["Scope", "Custom and production powder coating, sandblasting and surface preparation for industrial, commercial and architectural metal"],
            ["Facility address", "10874 Steeles Ave E, Milton, ON L9T 2X8"]
        ]
    )
    cert_table2 = make_table_block(
        ["Stage", "What we check", "When"],
        [
            ["Receiving inspection", "Incoming condition, damage, oil/grease, alloy type and drawing specs", "Upon arrival"],
            ["Surface preparation check", "Cleanliness, blast profile depth (SP 6 / SP 10) and masking accuracy", "Before powder application"],
            ["Application check", "Even powder spray, gun grounding, faraday corners and target mil build", "During coating"],
            ["Cure verification", "Oven air temperature, soak time and infrared surface temperature (180–200 °C)", "During each bake cycle"],
            ["Post-cure inspection", "Dry film thickness (ASTM D7091), cross-hatch adhesion (ASTM D3359), cure solvent rub and gloss", "After cooling"],
            ["Final packing & sign-off", "Visual defects, packaging protection and QC log sign-off", "Before release"]
        ]
    )
    cert_table3 = make_table_block(
        ["Test", "Method", "What it shows"],
        [
            ["Dry Film Thickness (DFT)", "Magnetic or eddy-current gauge (ASTM D7091)", "Verifies coating thickness meets specification"],
            ["Cross-Hatch Adhesion", "Cross-cut blade with pressure tape (ASTM D3359)", "Confirms adhesion of powder coat to prepared substrate"],
            ["MEK / Solvent Rub Cure Test", "Solvent rub resistance test (ASTM D5402)", "Confirms complete polymer crosslinking and cure"],
            ["Impact Resistance", "Falling dart impact tester (ASTM D2794)", "Measures coating resistance to cracking upon mechanical shock"],
            ["Gloss Level Verification", "60° gloss meter", "Verifies surface gloss matches approved master sample"]
        ]
    )

    cert_body = [
        "Quality assurance is built into every step of our coating process at Koojo Custom Powder Coating. Operating from our Milton facility since 2012, we hold formal certification through the Absolute Bureau of Certification, demonstrating adherence to documented quality procedures across all production runs.",
        "## SPEC STRIP",
        "Certified Quality Management | ASTM D7091 Thickness Verification | 48 Hr Turnaround | Since 2012 | 5.0 ★ Google Rating",
        "## Certificate Details",
        "Our facility certification verifies that our operational processes, testing methods, calibration schedules and traceability records meet rigorous third-party industrial standards:",
        cert_table1,
        "## Quality Assurance Checkpoints",
        "Every job passing through our shop is logged and verified at six mandatory quality checkpoints:",
        cert_table2,
        "## Standard Testing & Inspection Methods",
        "We test coated parts using standardized ASTM protocols to ensure long-term durability and corrosion protection:",
        cert_table3,
        "## Traceability & Documentation",
        "For defense, automotive, structural and municipal contracts, we supply formal inspection certificates detailing batch numbers, powder manufacturer data sheets, dry film thickness readings and cure logs upon request.",
        "## Discuss Quality Requirements",
        "If your project requires compliance with specific engineering standards (CGSB, ASTM, AAMA or SSPC), contact our quality assurance team at (905) 876-7060 or include your quality spec with your quote request."
    ]
    data["pages"]["certification"]["body"] = cert_body

    # 3. Contact Us (/contact-us)
    contact_table1 = make_table_block(
        ["Detail", "Information"],
        [
            ["Shop address", "10874 Steeles Ave E, Milton, ON L9T 2X8"],
            ["Telephone", "(905) 876-7060"],
            ["Email", "sales@koojopowdercoating.com"],
            ["Operating hours", "Monday to Friday, 7 AM to 5 PM; closed weekends and statutory holidays"],
            ["Drop-off dock", "Drive-in loading bay with forklift capacity up to 6,000 lb"]
        ]
    )
    contact_table2 = make_table_block(
        ["Method", "Best for", "Typical reply"],
        [
            ["Request a Quote form", "Standard or production pricing with drawings or photos", "1 business day"],
            ["Phone (905-876-7060)", "Urgent questions, same-day drop-off checks and active jobs", "Immediate during shop hours"],
            ["Email", "RFPs, multi-part BOMs and specifications", "1 business day"],
            ["Shop visit", "Colour chip review, physical part fit checks and drop-off", "Mon–Fri, 7 AM–5 PM"]
        ]
    )
    contact_table3 = make_table_block(
        ["Stage", "What we do", "Timing"],
        [
            ["Review and quote", "Check drawings/photos, confirm oven fit, prep scope and calculate price", "Within 1 business day"],
            ["Drop-off & booking", "Book drop-off dock, check parts on arrival, record lot and queue for prep", "Scheduled at quote"],
            ["Blasting & prep", "Chemical degreasing, abrasive blasting to profile, masking critical surfaces", "Day 1 of production"],
            ["Coating & cure", "Electrostatic powder spray and cure at 180–200 °C in our 23 ft oven", "Day 1–2 of production"],
            ["Inspection & pickup", "ASTM thickness/adhesion checks, packaging and notification for pickup/delivery", "48 hr standard turnaround"]
        ]
    )

    contact_body = [
        "Reach the Koojo Custom Powder Coating team directly. Whether you need a quick quote on a production run, want to drop off parts at our Milton facility, or need technical advice on powder selection and masking, our shop-floor team is ready to assist.",
        "## SPEC STRIP",
        "10874 Steeles Ave E, Milton | Mon–Fri 7 AM–5 PM | 23 ft Oven | Up to 6,000 lb | 5.0 ★ Google Rating",
        "## Facility & Contact Details",
        "Our powder coating shop is conveniently located just minutes off Highway 401 in Milton, serving fabricators, manufacturers and contractors across Halton Region and the Greater Toronto Area:",
        contact_table1,
        "## Best Way to Contact Us",
        "Choose the method that best matches your project timeline and documentation:",
        contact_table2,
        "## What Happens After You Contact Us",
        "We respect tight production schedules. Here is the straightforward process when you work with Koojo:",
        contact_table3,
        "## Drop-Off and Loading Bay Access",
        "Our facility features a ground-level drive-in bay and forklift capability for loading and unloading flatbeds, trailers and pickup trucks. Oversized parts up to 23 ft and 6,000 lb can be offloaded safely. Please call ahead if you are bringing items requiring dedicated crane or multi-person handling.",
        "## Request a Quote Online",
        "For the fastest written quote, submit your part dimensions, substrate, preferred RAL colour code and photos using our online quote form. We respond within 1 business day."
    ]
    data["pages"]["contact-us"]["body"] = contact_body

    # 4. Get a Quote (/get-a-quote)
    quote_table1 = make_table_block(
        ["Form field", "Why we ask", "Required?"],
        [
            ["Contact name & company", "To address the formal quotation and job file", "Required"],
            ["Email & phone", "To deliver the written quote and contact you for clarifications", "Required"],
            ["Part dimensions & weight", "To verify fit in our 23 ft oven and confirm handling limits", "Required"],
            ["Substrate metal", "To determine blast abrasive, chemical wash and primer needs", "Required"],
            ["Powder finish / RAL code", "To price the specified powder chemistry and gloss level", "Required"],
            ["Quantity & timeline", "To apply production volume tiers and schedule oven capacity", "Optional"],
            ["Drawings or photos", "Speeds quote turnaround and reveals critical masking areas", "Recommended"]
        ]
    )
    quote_table2 = make_table_block(
        ["Step", "What happens", "Typical timing"],
        [
            ["1. Submit details", "Send dimensions, photos/drawings, substrate and colour requirements", "Immediate"],
            ["2. Technical review", "Shop team verifies oven fit (23 ft max), masking requirements and powder selection", "Within 1 business day"],
            ["3. Written quote", "Formal itemized quotation delivered with turnaround commitment and prep specifications", "Same or next business day"],
            ["4. Drop-off & coat", "Parts received at 10874 Steeles Ave E, processed through prep, coating and QC", "48 hr standard turnaround"]
        ]
    )

    quote_body = [
        "Get a transparent, itemized powder coating quote from our experienced Milton team. We quote accurately based on metal condition, surface preparation requirements, part dimensions and required coating chemistry, ensuring no hidden charges on collection.",
        "## SPEC STRIP",
        "Fast 1-Day Quote Reply | 48 Hr Standard Turnaround | 23 ft Oven | Up to 6,000 lb | 5.0 ★ Google Rating",
        "## What to Include for an Accurate Quote",
        "To help us provide a precise quotation with the fastest possible turnaround, the table below explains the key information we review:",
        quote_table1,
        "## How Our Quoting Process Works",
        "From your first inquiry to finished parts ready for collection, here is how we handle your quote:",
        quote_table2,
        "## Volume Pricing & Recurring Commercial Work",
        "We support both one-off custom prototypes and high-volume production runs. Recurring manufacturing orders and regular fabrication batches benefit from dedicated racking, scheduled weekly oven slots and volume-tiered pricing. Contact us directly to discuss recurring supply contracts.",
        "## Drop-Off Consultation",
        "If you prefer to inspect colour swatches or discuss complex masking in person, bring your parts to our shop at 10874 Steeles Ave E in Milton, Monday to Friday between 7 AM and 5 PM."
    ]
    data["pages"]["get-a-quote"]["body"] = quote_body

    # 5. Services Hub (/services)
    serv_table1 = make_table_block(
        ["Capability", "Limit or detail"],
        [
            ["Oven length", "23 ft"],
            ["Oven width x height", "9 ft x 9 ft"],
            ["Maximum part weight", "6,000 lb"],
            ["Cure temperature", "180–200 °C"],
            ["Batch sizes", "One-off custom prototypes to recurring production runs"],
            ["Turnaround", "48 hours on standard work"]
        ]
    )
    serv_table2 = make_table_block(
        ["Test", "Method", "Frequency"],
        [
            ["Dry film thickness (DFT)", "Magnetic or eddy-current gauge to ASTM D7091", "Every production batch"],
            ["Cross-hatch adhesion", "Cross-cut test with pressure tape to ASTM D3359", "Daily control panels and on request"],
            ["Cure solvent rub", "MEK solvent rub test to ASTM D5402", "Daily oven verification"],
            ["Gloss level", "60° gloss meter", "Every custom color batch"],
            ["Visual inspection", "100% surface check for pinholes, orange peel or thin areas", "Every single part"]
        ]
    )
    serv_table3 = make_table_block(
        ["Metric", "Powder coating", "Wet paint", "Galvanizing"],
        [
            ["Durability", "High impact, chip, scratch and UV resistance", "Moderate; prone to chipping and scratching", "Very high abrasion and corrosion resistance"],
            ["Finish quality", "Smooth, uniform, drip-free; available in 100s of RAL colors & textures", "Smooth but prone to runs, drips and brush marks", "Dull grey crystalline zinc; no color variety"],
            ["Turnaround", "48 hours standard", "3–7 days (long drying/curing cycles)", "1–2 weeks (outside galvanizing bath)"],
            ["Environmental", "Zero VOCs, no hazardous solvents, recyclable overspray", "High VOC solvent emissions", "Acid wash and molten zinc bath"],
            ["Cost profile", "Most cost-effective long-term value for fabricated metal", "Lower initial cost for field touchups, high lifetime maintenance", "High cost for smaller or custom architectural items"]
        ]
    )

    serv_body = [
        "Koojo Custom Powder Coating provides full-service metal finishing from our Milton, Ontario facility. Combining complete in-house abrasive blasting, automated chemical cleaning, precision masking and a 23 ft curing oven, we deliver tough, uniform and visually flawless powder finishes for fabricators, manufacturers, contractors and automotive clients across Southern Ontario.",
        "## SPEC STRIP",
        "23 ft Oven | Up to 6,000 lb | In-House & Mobile Blasting | 48 Hr Turnaround | 5.0 ★ Google Rating",
        "## Size, Weight and Volume Capabilities",
        "Our shop floor handles small precision brackets through to massive structural frames up to 23 ft long:",
        serv_table1,
        "## Complete Service Overview",
        "We offer dedicated services tailored to specific metal types and operating environments:",
        [
            "Industrial Powder Coating: high-durability epoxy and polyester coatings for machinery, conveyor frames and factory equipment.",
            "Surface Preparation: degreasing, chemical iron phosphating and multi-stage washing for superior adhesion.",
            "Sandblasting Services: in-house walk-in blast room and mobile blasting units for rust and mill scale removal.",
            "Custom Colours & Finishes: exact RAL colour matching, metallics, textures, wrinkles, vein finishes and clear coats.",
            "Restoration & Recoating: complete finish stripping back to bare metal, repair patching and fresh powder application.",
            "Automotive Powder Coating: suspension subframes, roll cages, engine components and chassis assemblies.",
            "Wheel & Rim Powder Coating: full four-wheel rim refinishing, curb rash repair and multi-coat custom finishes.",
            "Architectural Metal Finishing: gates, railings, exterior panels and facade metalwork with super-durable powders."
        ],
        "## Testing and Quality Verification",
        "Every production run is evaluated to confirm coating integrity, mil build and full thermal crosslinking:",
        serv_table2,
        "## Powder Coating vs Alternative Finishes",
        "Comparing powder coating to traditional liquid painting and hot-dip galvanizing:",
        serv_table3,
        "## Schedule Your Work",
        "Contact our Milton production desk at (905) 876-7060 or request a quote online. We guarantee quick reviews and 48-hour standard turnaround."
    ]
    data["pages"]["services"]["body"] = serv_body

    # 6. Industries Hub (/industries)
    ind_table1 = make_table_block(
        ["Industry / Sector", "Typical parts", "Key finishing requirements"],
        [
            ["Metal Fabricators & Welding", "Frames, assemblies, architectural brackets, railings", "Weld spatter removal, corner coverage, 48 hr turnaround"],
            ["Manufacturing & Automation", "Conveyor frames, robotics bases, safety guarding, enclosures", "Tight masking of machined faces, RAL color matching, 6,000 lb capacity"],
            ["Machine Shops", "Precision CNC components, manifolds, tooling, mounting brackets", "Tolerance control, thread and tapped hole masking, scratch resistance"],
            ["Contractors & Construction", "Structural lintels, exterior gates, fences, stairs, canopies", "High-durability architectural polyester, UV resistance, rust protection"],
            ["Food Processing Equipment", "Sanitary frame assemblies, washdown covers, processing stands", "Chemical washdown resistance, smooth hygienic non-porous finish"],
            ["Agricultural & Heavy Equipment", "Tractor implements, chassis parts, booms, trailers, hitches", "Zinc primer base, heavy impact resistance, SSPC-SP 6 grit blast"],
            ["Municipal & Institutional", "Safety bollards, park benches, transit railings, street light poles", "Anti-graffiti finish, OSHA safety yellow, high weatherability"]
        ]
    )

    ind_body = [
        "Different industries place unique demands on coated metal: food plants require washdown chemical resistance, outdoor construction needs ten-year UV stability, and automated machine builders require micro-tolerance masking on precision surfaces. Koojo Custom Powder Coating formulates the blast profile, primer system and powder chemistry to match your industry's exact operational environment.",
        "## SPEC STRIP",
        "Serving 7 Core Industrial Sectors | Custom Masking | ASTM Testing | 48 Hr Turnaround | 5.0 ★ Google Rating",
        "## Finishing Requirements by Industry Sector",
        "The table below outlines how our surface preparation, masking standards and powder formulations adapt to different operating environments:",
        ind_table1,
        "## Dedicated Sector Capabilities",
        [
            "Metal Fabricators & Welders: fast turnarounds that keep your shop floor moving and meet your customer delivery deadlines.",
            "Automation Builders: expert masking of linear rail mounts, bearing pockets, sensor brackets and dowel holes.",
            "Machine Shops: thin-film precision application that respects mechanical clearances and eliminates post-coat machining.",
            "Construction Contractors: AAMA 2604/2605 compliant architectural powders backed by manufacturer weather warranties.",
            "Food Equipment Makers: washdown-tolerant hybrids that withstand high-pressure hot water and sanitizing chemicals.",
            "Heavy Equipment OEMs: zinc-rich epoxy primers beneath super-durable topcoats for harsh aggregate and chemical exposure.",
            "Municipal Authorities: standardized transit, park and highway finishes adhering to provincial and municipal specifications."
        ],
        "## Partner with Koojo",
        "To review your project's technical specifications or set up a commercial account, call our team at (905) 876-7060 or submit a quote request."
    ]
    data["pages"]["industries"]["body"] = ind_body

    # 7. Locations Hub (/locations)
    loc_table1 = make_table_block(
        ["City", "Approximate drive time", "Main route to Milton"],
        [
            ["Milton", "Local (5–10 mins)", "Steeles Ave E / Hwy 401"],
            ["Oakville", "20–25 mins", "Trafalgar Rd / Hwy 407 / Hwy 401"],
            ["Burlington", "25–30 mins", "Guelph Line / Appleby Line north to Hwy 401"],
            ["Mississauga", "20–30 mins", "Hwy 401 westbound directly to Steeles Ave E exit"],
            ["Halton Hills / Georgetown", "15–20 mins", "Trafalgar Rd / Mountainview Rd south to Steeles"],
            ["Brampton", "25–35 mins", "Hwy 407 / Queen St / Steeles Ave W"],
            ["Guelph", "30–35 mins", "Hwy 401 eastbound directly to Milton"],
            ["Cambridge", "35–45 mins", "Hwy 401 eastbound to Milton exits"],
            ["Hamilton", "35–45 mins", "Hwy 403 / Hwy 6 north to Hwy 401 east"]
        ]
    )

    loc_body = [
        "Centrally located at 10874 Steeles Ave E in Milton, Ontario, Koojo Custom Powder Coating serves metal fabricators, manufacturers, machine shops and contractors across the Greater Toronto Area and the Golden Horseshoe. With straightforward highway access off Highway 401 and Highway 407, our facility is an easy drop-off and pickup hub for businesses throughout the region.",
        "## SPEC STRIP",
        "Milton Facility | Easy 401/407 Access | Serving 9 Surrounding Municipalities | 48 Hr Turnaround | 5.0 ★ Google Rating",
        "## Drive Times & Highway Routes to Our Shop",
        "Our shop features drive-in loading bays and forklift unloading to accommodate clients from across Southern Ontario:",
        loc_table1,
        "## Regional Pickup and Drop-off Options",
        "We understand shop logistics. Customers can drop parts off directly at our Milton facility Monday through Friday from 7 AM to 5 PM. For recurring commercial clients and large structural runs, scheduled pickup and return freight can be arranged across Halton, Peel, Wellington and Waterloo regions.",
        "## Mobile Sandblasting Across Southern Ontario",
        "When parts or structures cannot be transported due to size or weight, our mobile abrasive blasting rigs travel on-site throughout Milton, Oakville, Burlington, Mississauga, Brampton, Guelph and Hamilton to perform surface preparation.",
        "## Visit or Book an Order",
        "Call (905) 876-7060 to confirm oven capacity or check today's receiving queue before heading to our Milton facility."
    ]
    data["pages"]["locations"]["body"] = loc_body

    # 8. Blog Hub (/blog)
    blog_table1 = make_table_block(
        ["Your situation", "Recommended guide", "Why start here"],
        [
            ["Comparing coating options for fabricated metal", "Powder Coating vs Wet Paint vs Galvanizing", "Clear cost, durability and lifespan comparison"],
            ["Specifying dry film thickness for drawings", "Powder Coating Thickness (Mils) Rating Guide", "Explains ASTM D7091 standards and mil targets"],
            ["Designing outdoor parts for harsh Canadian winters", "Corrosion Resistance Ratings for Coated Metal", "Covers ISO 12944 environments and salt spray testing"],
            ["Choosing powder chemistry (epoxy vs polyester vs urethane)", "Powder Coating Finishes & Polymers Guide", "Explains UV stability, chemical resistance and hardness differences"],
            ["Preparing old or rusted parts for recoating", "Sandblasting & Surface Preparation Standards", "Covers SSPC and NACE blast cleanliness grades"]
        ]
    )

    blog_body = [
        "Welcome to the Koojo Custom Powder Coating knowledge base. Written by shop-floor coating technicians with decades of hands-on experience, our guides provide objective engineering insights into powder selection, surface preparation standards, film thickness testing and corrosion prevention.",
        "## SPEC STRIP",
        "Shop-Floor Technical Guides | ASTM Standards Explained | Written by Coating Specialists | 5.0 ★ Google Rating",
        "## Which Technical Guide Should You Read First?",
        "Select the guide matching your current engineering or procurement question:",
        blog_table1,
        "## Core Topics Covered",
        [
            "Materials & Substrates: how steel, aluminum, cast iron, galvanized metal and stainless behave during electrostatic coating and thermal cure.",
            "Finishes, Polymers & Colours: comparing TGIC polyester, super-durables, epoxies, urethanes, fluoropolymers, texture effects and RAL colour standards.",
            "Testing, Standards & Quality: understanding mil thickness measurement (ASTM D7091), cross-hatch adhesion, solvent rub testing and salt fog ratings.",
            "Maintenance & Restoration: stripping old coatings, surface degreasing, sandblasting profiles and recoating weathered metal."
        ],
        "## Ask a Technical Question",
        "If your drawing has unusual coating callouts or environmental exposure requirements not covered in our guides, call our Milton team at (905) 876-7060 for straightforward shop-floor advice."
    ]
    data["pages"]["blog"]["body"] = blog_body

    # 9. All 6 Project Case Studies
    projects_data = {
        "church-gates": {
            "title": "Church Gates",
            "snapshot": [
                ["Client industry", "Institutional (Architectural Restoration)"],
                ["Part", "Ornamental gate leaves (pair, 8 ft x 6 ft each) and posts"],
                ["Metal", "Wrought iron & structural steel"],
                ["Size / Weight", "8 ft x 6 ft per leaf, approx. 450 lb total"],
                ["Powder", "Super-durable architectural polyester"],
                ["Colour Code", "Satin Architectural Black (RAL 9005)"],
                ["Turnaround", "48 hours"]
            ],
            "specs": [
                ["DFT (dry film thickness)", "3.0–4.0 mils, measured to ASTM D7091"],
                ["Prep grade", "Abrasive blast stripping to bare metal (SSPC-SP 10 Near-White)"],
                ["Powder", "Super-durable architectural polyester, satin finish"],
                ["Cure", "180–200 °C per powder data sheet, 15–20 minutes part temperature"]
            ]
        },
        "automation-line-frame": {
            "title": "Automation Line Frame",
            "snapshot": [
                ["Client industry", "Manufacturing & Automation"],
                ["Part", "Welded automation equipment line frame"],
                ["Metal", "Structural steel tube & plate weldment"],
                ["Size / Weight", "18 ft x 4 ft x 5 ft, approx. 1,800 lb"],
                ["Powder", "Thermoset TGIC polyester powder"],
                ["Colour Code", "RAL 7016 Anthracite Grey, Satin"],
                ["Turnaround", "48 hours"]
            ],
            "specs": [
                ["DFT (dry film thickness)", "3.0–4.5 mils, measured to ASTM D7091"],
                ["Prep grade", "Commercial blast (SSPC-SP 6 / NACE No. 3) + iron phosphate rinse"],
                ["Powder", "Super-durable polyester powder coating"],
                ["Cure", "180–200 °C per powder data sheet, 15–20 minutes part temperature"]
            ]
        },
        "conveyor-frame-automotive-plant": {
            "title": "Conveyor Frame for Automotive Plant",
            "snapshot": [
                ["Client industry", "Automotive Manufacturing (Tier-1)"],
                ["Part", "Overhead conveyor section frame"],
                ["Metal", "Carbon steel tube and plate"],
                ["Size / Weight", "20 ft x 3 ft x 4 ft, approx. 2,100 lb"],
                ["Powder", "High-durability hybrid/polyester powder coating"],
                ["Colour Code", "Safety Yellow (RAL 1023) / Tier-1 Plant Standard"],
                ["Turnaround", "48 hours"]
            ],
            "specs": [
                ["DFT (dry film thickness)", "3.5–5.0 mils, measured to ASTM D7091"],
                ["Prep grade", "Commercial blast clean (SSPC-SP 6 / ISO 8501-1 Sa 2) + iron phosphate"],
                ["Powder", "High-durability hybrid/polyester powder coating"],
                ["Cure", "180–200 °C per powder data sheet, 15–20 minutes part temperature"]
            ]
        },
        "food-processing-line-frame": {
            "title": "Food Processing Line Frame",
            "snapshot": [
                ["Client industry", "Food Processing Equipment"],
                ["Part", "Welded line frame for a food processing line (non-food-contact)"],
                ["Metal", "Structural carbon steel with stainless mounting points"],
                ["Size / Weight", "16 ft x 4 ft x 4 ft, approx. 1,400 lb"],
                ["Powder", "Chemical and washdown-resistant epoxy/polyester hybrid"],
                ["Colour Code", "Clean Machine White (RAL 9010)"],
                ["Turnaround", "48 hours"]
            ],
            "specs": [
                ["DFT (dry film thickness)", "3.0–4.5 mils, measured to ASTM D7091"],
                ["Prep grade", "Near-white abrasive blast (SSPC-SP 10) + washdown pretreatment"],
                ["Powder", "Washdown-rated TGIC-free polyester, high gloss white"],
                ["Cure", "180–200 °C per powder data sheet, 15–20 minutes part temperature"]
            ]
        },
        "robotic-base": {
            "title": "Robotic Base",
            "snapshot": [
                ["Client industry", "Manufacturing Automation & Robotics"],
                ["Part", "Heavy robotic arm mounting pedestal & base weldment"],
                ["Metal", "Heavy plate steel (1.5 in base plate) & structural weldment"],
                ["Size / Weight", "6 ft x 6 ft x 3 ft, approx. 2,200 lb"],
                ["Powder", "High-impact industrial polyester powder"],
                ["Colour Code", "Machine Grey (RAL 7035)"],
                ["Turnaround", "48 hours"]
            ],
            "specs": [
                ["DFT (dry film thickness)", "3.5–5.0 mils, measured to ASTM D7091"],
                ["Prep grade", "Abrasive blast (SSPC-SP 6) + iron phosphate rinse"],
                ["Powder", "Industrial grade TGIC polyester, textured finish"],
                ["Cure", "180–200 °C part temperature per powder data sheet, 20 minutes"]
            ]
        },
        "safety-bollards": {
            "title": "Safety Bollards",
            "snapshot": [
                ["Client industry", "Municipal and Institutional Metalwork"],
                ["Part", "Steel safety bollards (batch of 24 units)"],
                ["Metal", "Heavy-wall 6-inch steel pipe with 12-inch welded base plates"],
                ["Size / Weight", "6 in dia x 48 in height, approx. 65 lb each"],
                ["Powder", "UV-resistant exterior polyester powder"],
                ["Colour Code", "OSHA Safety Yellow (RAL 1023)"],
                ["Turnaround", "48 hours"]
            ],
            "specs": [
                ["DFT (dry film thickness)", "3.5–5.0 mils, measured to ASTM D7091"],
                ["Prep grade", "Commercial abrasive blast (SSPC-SP 6) + zinc-rich primer base"],
                ["Powder", "Super-durable exterior polyester, high-visibility gloss"],
                ["Cure", "180–200 °C per powder data sheet, 15–20 minutes"]
            ]
        }
    }

    data.setdefault("projects", {})
    for slug, pinfo in projects_data.items():
        snap_table = make_table_block(["Item", "This job"], pinfo["snapshot"])
        spec_table = make_table_block(["Spec", "Value"], pinfo["specs"])
        
        # Build clean project body
        curr_body = data["projects"].get(slug, {}).get("body", [])
        clean_text_paragraphs = []
        for b in curr_body:
            if isinstance(b, str):
                cleaned = clean_brackets(b)
                # Skip duplicate table lines from previous flattening
                if cleaned in ["Item", "This job", "Spec", "Value", "Capability", "Limit or detail"]:
                    continue
                if any(cleaned.startswith(k[0]) for k in pinfo["snapshot"]):
                    continue
                if any(cleaned.startswith(k[0]) for k in pinfo["specs"]):
                    continue
                if cleaned.startswith("## The Challenge") or cleaned.startswith("## Our Approach") or cleaned.startswith("## The Result") or cleaned.startswith("## Services Used") or cleaned.startswith("## Client Feedback") or cleaned.startswith("## Have a Similar"):
                    clean_text_paragraphs.append(cleaned)
                elif len(cleaned) > 25 and not cleaned.startswith("SECTION") and not "koojopowdercoating.com" in cleaned:
                    clean_text_paragraphs.append(cleaned)

        # Assemble canonical body with tables
        proj_assembled_body = [
            clean_text_paragraphs[0] if clean_text_paragraphs else f"Case study detailing the powder coating process for {pinfo['title']}.",
            "## Project Snapshot",
            snap_table,
            "## The Challenge",
            clean_text_paragraphs[1] if len(clean_text_paragraphs) > 1 else "Restoring and coating this assembly required rigorous surface preparation, removing existing oxidation, and achieving full coverage across recessed angles and welds.",
            clean_text_paragraphs[2] if len(clean_text_paragraphs) > 2 else "Operating conditions demanded high mechanical durability, impact resistance, and corrosion protection against harsh environmental exposure.",
            "## Our Approach",
            clean_text_paragraphs[3] if len(clean_text_paragraphs) > 3 else "Parts were degreased, abrasive-blasted in our walk-in blast room to establish a deep anchor profile, masked on all precision mating faces, and coated with electrostatically charged powder.",
            clean_text_paragraphs[4] if len(clean_text_paragraphs) > 4 else "Curing was conducted in our 23 ft industrial oven, with infrared temperature verification confirming the metal reached full crosslinking temperature.",
            "## Specs at a Glance",
            spec_table,
            "## The Result",
            "The completed assembly achieved a uniform, pinhole-free finish that fully met the client's engineering specifications. Quality control logs verified mil thickness and cross-hatch adhesion, and parts were packaged for scratch-free transport within our 48-hour turnaround commitment.",
            "## Have a Similar Part?",
            "Whether you need an individual prototype or an ongoing production schedule, contact Koojo Custom Powder Coating at (905) 876-7060 or request a quote online for your next fabrication project."
        ]
        data["projects"][slug]["body"] = proj_assembled_body

    # 10. Clean and update all remaining Services, Industries and Locations
    for slug, serv in data.get("services", {}).items():
        if serv.get("body"):
            serv["body"] = process_body_list(serv["body"])
            if not any("5.0 ★ Google Rating" in str(x) for x in serv["body"][:3]):
                serv["body"].insert(0, "Since 2012 | 10,000+ Items Finished | 48 Hr Turnaround | 5.0 ★ Google Rating")

    for slug, ind in data.get("industries", {}).items():
        if ind.get("body"):
            ind["body"] = process_body_list(ind["body"])
            if not any("5.0 ★ Google Rating" in str(x) for x in ind["body"][:3]):
                ind["body"].insert(0, "Custom Industrial Finishing | 23 ft Oven | 48 Hr Turnaround | 5.0 ★ Google Rating")

    for city, loc in data.get("locations", {}).items():
        if loc.get("body"):
            loc["body"] = process_body_list(loc["body"])
            if not any("5.0 ★ Google Rating" in str(x) for x in loc["body"][:3]):
                loc["body"].insert(0, f"Serving {city} & GTA | Milton Facility | 48 Hr Turnaround | 5.0 ★ Google Rating")

    # Clean home page rating
    if "pages" in data and "home" in data["pages"] and data["pages"]["home"].get("body"):
        data["pages"]["home"]["body"] = process_body_list(data["pages"]["home"]["body"])

    # Clean about-us page rating
    if "pages" in data and "about-us" in data["pages"] and data["pages"]["about-us"].get("body"):
        data["pages"]["about-us"]["body"] = process_body_list(data["pages"]["about-us"]["body"])

    # Write back clean uploaded_content.json
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("Master content restoration complete! All tables and ratings structured natively in uploaded_content.json.")

if __name__ == "__main__":
    main()
