import json

_key_counter = 500
def get_key(prefix="k"):
    global _key_counter
    _key_counter += 1
    return f"{prefix}{_key_counter}"

def make_table_block(headers, rows):
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

def restore_services():
    json_path = "scripts/seed/uploaded_content.json"
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 1. ARCHITECTURAL POWDER COATING (/services/architectural-coatings)
    arch_body = [
        "Architectural powder coating gives railings, fences, window frames and other building metalwork a tough, colour-stable finish that handles sun, rain and winter salt. At Koojo Custom Powder Coating, our Milton team provides architectural metal finishing for contractors, builders, property managers and fabricators. Since 2012, we have finished more than 10,000 items, with a 48-hour turnaround on typical shop orders. Each part is cleaned, prepared, coated and oven-cured in one controlled process, so the finish bonds well and lasts. Call (905) 876-7060, Monday to Friday, 7 AM to 5 PM, or request a quote below to start your architectural powder coating project.",
        "## SPEC STRIP",
        "Since 2012 | 10,000+ Items | 48 Hr Turnaround | 5.0 ★ Google Rating",
        "## What Is Architectural Powder Coating?",
        "Architectural powder coating is a finishing process in which dry, electrostatically charged powder is sprayed onto prepared building metalwork and cured in an oven. It forms a hard, even shell that protects the steel and aluminum parts used on and around buildings.",
        "Unlike liquid paint, powder has no solvent carrier. The charged particles cling to the metal, then melt and cross-link in the oven, typically at 180 to 200 °C. That heat-driven reaction forms a continuous film that resists chipping, scratching and fading better than most sprayed paint, which is why powder coated railings and powder coated fences hold up well to weather.",
        "The term architectural coatings covers finishes for building elements. This page focuses on exterior metal coating for railings, fences, gates and frames. Machinery and equipment belong to our industrial powder coating page, and vehicle parts have their own pages.",
        "Why choose powder over paint for building metal? Architectural powder coating applies in a controlled booth, cures without a solvent carrier and gives a thicker, more uniform finish than most brush or spray paint. It also reaches welds, joints and tube ends evenly, which is hard to do by hand on site. For most projects, professional architectural powder coating is the simpler route to a finish that lasts.",
        "## How Does Our Architectural Powder Coating Process Work?",
        "Our architectural powder coating process follows six stages: inspection, stripping or blasting, pretreatment, masking, powder application and oven curing. Each stage protects the metal, and every part is checked before it leaves our Milton shop.",
        [
            "1. Inspection (on arrival). We check each railing, frame or fence section for rust, weld spatter, old coatings and damage. Please remove glass, gaskets, plastic parts and any hardware that heat could harm. Clear notes on the colour and finish you want help us quote accurately.",
            "2. Stripping and blasting. Old paint, powder or rust is removed so the new finish bonds to bare metal. Heavy rust or mill scale may call for our sandblasting services first.",
            "3. Pretreatment. Washing, degreasing and rinsing remove oil, dirt and weld residue. Our powder coating surface preparation step is where an outdoor finish is won or lost.",
            "4. Masking. Threaded holes, mounting faces and contact points are masked or plugged, so parts still fit and install cleanly on site.",
            "5. Powder application. We spray your chosen colour electrostatically, reaching joints, tube ends and edges evenly. Clean, controlled application is the heart of architectural powder coating, and it is why we keep this step separate from preparation.",
            "6. Oven curing. Each part cures at oven temperature, cools, and is inspected for coverage and smoothness before packing for pickup or delivery."
        ],
        "Timing matters. Typical shop orders follow our standard 48-hour turnaround, and we receive parts Monday to Friday, 7 AM to 5 PM. Long railing runs, heavy rust, several colours or large batches can need more time, so we confirm the schedule when we quote. We pack finished parts carefully for pickup or delivery to your site.",
        "## Which Parts Suit Architectural Powder Coating?",
        "Most steel and aluminum building components suit architectural powder coating, including railings, fences, gates and frames, provided they fit our oven and handle curing heat. Send photos and dimensions, and we will confirm suitability before work starts.",
        [
            "Railings and stairs. Stair railing powder coating, balcony railing powder coating and handrail powder coating protect welded joints and tube ends, where weather attacks first. Aluminum railing powder coating suits lighter systems.",
            "Fences and gates. Fence powder coating and gate powder coating suit steel and aluminum sections. Aluminum fence powder coating keeps lightweight panels uniform, while steel fence finishing seals the metal against rust.",
            "Frames and canopies. Window frame powder coating, door frame powder coating and steel canopy powder coating give a clean, consistent look across a building. Aluminum window frames need careful masking at glazing edges.",
            "Other metalwork. Ornamental ironwork and storefront metal finishing also suit architectural powder coating, and we handle other architectural metalwork on request."
        ],
        "To prepare for drop-off, label each section, remove loose dirt and take clear photos of any damage. Good photos let us quote architectural powder coating accurately and spot issues early. Larger assemblies can exceed oven limits, so check our capabilities page for size and weight limits before you order. Long runs can often be split into sections that fit, then joined on site.",
        "## What Finishes Does Architectural Powder Coating Offer?",
        "Architectural powder coating offers gloss, satin, matte, textured and metallic finishes, with colours matched to a RAL code or a physical sample. We help you pick a finish that suits the building design and its exposure to sun and weather.",
        [
            "Popular looks. A matte architectural finish suits modern buildings, while textured powder coating hides minor surface marks on busy railings and gates.",
            "Metallic and custom. A metallic architectural finish adds depth to feature elements. Custom architectural powder coating lets you match brand or building palettes, and our custom powder coating colours page shows the wider range.",
            "Matching. RAL colour matching helps you align new parts with existing metalwork. Send a sample or colour code, and we will recommend the closest powder, including custom architectural colours.",
            "Exterior grade. Exterior-grade powder coating is chosen for weather exposure, so tell us where the part will be installed."
        ],
        "Not sure which finish fits? Send photos and tell us where the metalwork will be installed. A short chat before coating prevents surprises and keeps your architectural powder coating project on schedule. For weathered railings, our restoration and recoating service handles stripping and railing recoating.",
        "## How Do We Check Architectural Powder Coating Quality?",
        "We inspect every part before and after coating for even coverage, a smooth film, clean masked areas and a complete cure. Koojo is certified through the Absolute Bureau of Certification, and test reports are available on request.",
        "Preparation drives results. Coating over clean, bare metal gives a corrosion-resistant architectural finish, because the cured film seals the surface against moisture. A reliable weather-resistant finish depends on that same bond, so we never rush stripping or washing.",
        "Outdoor metal also faces sun. A UV-resistant finish and fade-resistant powder coating depend on choosing the right powder for the exposure. If your project calls for AAMA 2604 powder coating or an AAMA 2605 finish, tell us the specification at quote stage so we can confirm which powder and process suit it. Together, these steps create a durable outdoor metal finish.",
        "Consistent architectural powder coating also means the next batch matches the last, because we keep records that support repeat orders. To keep finished metalwork looking sharp, wash it with mild soap and a soft brush, and avoid harsh abrasive cleaners. Our shop team reviews each batch against your order before packing. See our certification page to learn how we document our work.",
        "## See Architectural Powder Coating in a Real Project",
        "Our church gates case study shows how we document a real architectural project, from preparation and powder to colour code and turnaround. It shows the prep-first approach behind every architectural powder coating job we take on.",
        "Read the church gates project to see the standard we hold ourselves to. Before and after photos show the work from bare metal through to the finished coating, and the same documented approach applies to your railings, fences and frames. For repeat orders, we can record the part type, metal and colour code in the same way.",
        "## Who Uses Our Architectural Powder Coating?",
        "Contractors, railing installers, builders, property managers, municipalities and fabrication shops send us building metalwork most often. They want architectural powder coating that is dependable, fast and consistent from the first part to the last.",
        "Crews from contractors and construction often need steel and aluminum parts finished on a schedule, while municipal and institutional clients bring park, school and church metalwork. Commercial building metalwork and larger repeat jobs fit the full range of powder coating services at our Milton shop. Reliable architectural powder coating also keeps maintenance simple for property managers. Whatever you build or maintain, we treat each part as a finished product and plan the coating around how it will be used.",
        "## Architectural Powder Coating FAQs",
        "Short answer: yes, most steel and aluminum building metalwork can be coated, and typical shop orders return in 48 hours. These answers cover outdoor use, specifications, timing, recoating and preparation before you book.",
        "## Get Your Architectural Powder Coating Quote",
        "Ready for stronger, cleaner building metalwork? Send photos, dimensions and your preferred finish through our quote form for architectural powder coating advice, or visit 10874 Steeles Ave E, Milton, Monday to Friday, 7 AM to 5 PM. Call (905) 876-7060 or email sales@koojopowdercoating.com."
    ]

    arch_faqs = [
        ["Can architectural powder coating be used outdoors?", "Yes. We select an exterior-grade powder for parts that face sun, rain and road salt. Tell us where the metalwork will be installed, and we will recommend a suitable powder."],
        ["Do you work to AAMA specifications?", "If your drawings call for AAMA 2604 or 2605, send the specification with your quote request. We confirm which powder and process suit it before any work starts."],
        ["How long does architectural powder coating take?", "Typical shop orders follow our 48-hour turnaround. Long railing runs, heavy rust, several colours or large batches are scheduled when we quote."],
        ["Can you recoat weathered railings?", "Yes. We strip the old coating, treat rust and prepare the bare metal before recoating. Heavily corroded sections may need repair by a fabricator first."],
        ["Can you match my building colour?", "Yes. Send a RAL code or a physical sample, and we will recommend the closest powder. Slight variation can occur between powder batches and original finishes."],
        ["What should I remove before architectural powder coating?", "Remove glass, gaskets, plastic parts and hardware that heat could damage. Label each section so we can return parts in the order you need for installation."]
    ]

    data.setdefault("services", {})["architectural-coatings"] = {
        "meta_title": "Architectural Powder Coating for Railings & Frames | Koojo",
        "meta_desc": "Architectural powder coating for railings, fences and window frames: weather-resistant finishes, RAL colour matching and a 48-hour turnaround. Request a quote.",
        "primary_kw": "architectural powder coating",
        "summary": "Architectural powder coating gives railings, fences, window frames and other building metalwork a tough, colour-stable finish that handles sun, rain and winter salt. Finished in Milton with a 48-hour turnaround.",
        "body": arch_body,
        "faqs": arch_faqs
    }

    # 2. AUTOMOTIVE POWDER COATING (/services/automotive-powder-coating)
    auto_table = make_table_block(
        ["Option", "What it gives you", "Best for"],
        [
            ["Gloss", "Gloss black powder coating and other high-gloss finishes give a deep, smooth look.", "Frames, brackets, show builds"],
            ["Matte or satin", "Matte black powder coating cuts glare and hides light scuffs.", "Trucks, off-road builds"],
            ["Textured", "Textured powder coating hides small surface marks and adds grip.", "Skid plates, running boards"],
            ["Film thickness", "Typical film is 2 to 4 mils. We confirm mil thickness on fit-critical parts.", "Threaded or tight-tolerance parts"],
            ["Toughness", "Chip-resistant powder coating forms a durable automotive finish for daily use.", "Daily-use and off-road parts"]
        ]
    )

    auto_body = [
        "Automotive powder coating gives car frames, chassis parts and motorcycle components a tough, even finish that stands up to chips, rust and winter road salt. At Koojo Custom Powder Coating, our Milton team coats automotive parts in batches, from a single bracket to a full set of suspension components. Since 2012, we have finished more than 10,000 items for customers across the GTA, with a 48-hour turnaround on typical orders. Whether you need vehicle powder coating for a truck frame or car powder coating for a custom build, we match the prep and powder to your metal. Call (905) 876-7060, Monday to Friday, 7 AM to 5 PM, or request an automotive powder coating quote below.",
        "## SPEC STRIP",
        "Since 2012 | 10,000+ Items | 48 Hr Turnaround | 5.0 ★ Google Rating",
        "## What Is Automotive Powder Coating?",
        "Automotive powder coating is a dry finishing process in which electrostatically charged powder is sprayed onto metal vehicle parts, then heated in an oven until it melts and cures into a hard, even coating. It protects bare metal from rust, chips and everyday wear.",
        "The finish is made from thermoset powder, which cures with heat instead of drying like liquid paint. At a cure temperature of 180 to 200 °C, the powder flows, bonds to the metal and hardens into one continuous layer without runs or drips. That makes it a dependable corrosion-resistant automotive coating for parts that face grit, moisture and impact, such as frames, brackets, suspension arms and underbody components. That is why vehicle powder coating is common on trucks and trailers that see winter road salt.",
        "Typical customers include builders of custom motorcycles, owners of trucks and trailers, and shops that send out metal parts for finishing. If your project needs custom car parts powder coating, our powder coating services cover it from intake to handoff. Good auto parts powder coating also depends on the work done before the powder goes on, so we plan every job from the bare metal up.",
        "## Our Automotive Powder Coating Process",
        "Our automotive powder coating process has six stages: intake and inspection, cleaning and pretreatment, masking, powder application, oven curing and final inspection. Each stage is documented so repeat orders match the first batch. The same controls support our industrial powder coating work.",
        [
            "Step 1 – Intake and Inspection: We check each part for heavy rust, old coatings, weld quality and damage, then confirm the finish you want for your automotive powder coating order. We also decide how to hang the part so every surface can be reached.",
            "Step 2 – Cleaning and Pretreatment: Parts are washed and pretreated so the powder bonds to clean metal. Skipping this stage is a common reason rust protection for car parts fails early.",
            "Step 3 – Masking and Plugging: Threads, bearing surfaces and mounting holes are protected before coating. Masking and plugging keep bolts turning and parts fitting, which matters on any valve cover powder coating or engine bracket powder coating order.",
            "Step 4 – Electrostatic Powder Application: Charged powder is sprayed onto the grounded part, so it wraps around tubes, corners and recesses. Electrostatic powder application gives an even film across a complex frame.",
            "Step 5 – Oven Curing: The part moves into the curing oven, where automotive powder coating reaches temperature and hardens. Cure time depends on the powder and the mass of the part, so a heavy chassis is planned differently from a small bracket.",
            "Step 6 – Final Inspection and Handoff: We inspect the cured finish for coverage, adhesion and appearance. Typical orders are ready within 48 hours, and larger batch powder coating jobs are scheduled when we quote. We receive parts Monday to Friday, 7 AM to 5 PM."
        ],
        "Our automotive powder coating services schedule each stage so parts never wait between steps, and for car powder coating on a deadline, tell us your date at quote.",
        "## Parts and Metals We Coat",
        "We apply automotive powder coating to steel, aluminum and cast parts, including frames, chassis components, brackets, valve covers and suspension parts. Our capabilities page lists 6,000 lb capacity, so heavy truck frames, trailer parts and other large vehicle components are worth a quote.",
        [
            "Frames: car frame powder coating and truck frame powder coating, full or partial.",
            "Chassis and suspension: chassis powder coating, suspension parts powder coating and control arm powder coating.",
            "Motorcycles: motorcycle frame powder coating and motorcycle parts powder coating for custom builds.",
            "Body hardware: bumper powder coating, skid plate powder coating, running board powder coating and roll cage powder coating.",
            "Heavy use: trailer hitch powder coating and off-road parts powder coating."
        ],
        "Wheels have their own dedicated process, so see our wheel and rim powder coating page for rims. Not sure what can be coated? Read which car parts can be powder coated, or send photos with your quote request.",
        "Metals we handle: steel for frames and brackets, aluminum for lighter components, and cast parts such as covers and housings. Our powder coating for automotive parts starts with a material check at intake, because the right prep and cure plan depends on the metal and the thickness of the part.",
        "## Finish and Option Choices",
        "Choose from gloss, satin, matte and textured finishes in a wide range of colours. We confirm the powder type, colour code and film thickness at quote, so the finish suits the part, the metal and how it will be used.",
        auto_table,
        "Whatever you pick, vehicle powder coating should look consistent from part to part, so a matching frame and brackets leave the shop in one colour.",
        "Film thickness affects fit, so tell us about tight tolerances before we coat. For a gloss, matte or textured automotive powder coating finish, send your colour code or a sample with your quote request.",
        "## Quality Standards for Automotive Powder Coating",
        "Our automotive powder coating follows recognized standards: ASTM D3359 for adhesion, ASTM D7091 for dry film thickness and ASTM B117 for salt spray resistance. Koojo is certified through the Absolute Bureau of Certification, and test reports are available on request.",
        "Quality starts at intake and ends at handoff. After curing, a good finish looks even in colour and gloss, with no thin spots, runs or bare edges. We flag any concern with you before parts leave the shop.",
        "An ASTM D3359 adhesion test checks that the coating bonds to the metal. Dry film thickness readings confirm the coating is neither too thin to protect nor too thick to fit. The ASTM B117 salt spray test measures corrosion resistance in a controlled chamber. It is a comparison tool rather than a promise of real-world life, so we explain what results mean for your parts.",
        "Batch inspection means each load is checked before parts leave the shop, which keeps repeat orders consistent and adds road salt protection you can rely on. Careful vehicle powder coating also depends on clean prep and correct curing, so every order follows the same documented steps. See our certification page for details.",
        "## Recent Project: Conveyor Frame for an Automotive Plant",
        "Our conveyor frame for an automotive plant shows how we handle heavy, welded steel that must keep its finish in a busy production setting. Frames like this face grease, impact and constant handling, the same demands your vehicle parts meet on the road.",
        "The case study records the part, metal, size, powder, colour code and turnaround, with before and after photos. Read the conveyor frame project to see the standard behind our work, and expect the same documented approach on your car powder coating order, from frame to bracket.",
        "## Industries That Use Automotive Powder Coating",
        "Machine shops, farm and heavy equipment owners, fabricators, trailer builders and vehicle builders use our automotive powder coating most. These customers want dependable auto parts powder coating, fast turnaround and repeatable quality across batches, whether they send one part or a full production run.",
        "See how we support machine shops, which often send precision parts with threads and bores that need masking, and agricultural and heavy equipment owners, who need tough finishes on trucks, trailers and attachments.",
        "## Automotive Powder Coating FAQs",
        "Short answer: we coat steel, aluminum and cast car parts in batches, with fast turnaround on typical orders. These answers cover size, timing, rust, fit and logistics so you know what to expect before you book your order. Ask us anything else before you send parts.",
        "## Get an Automotive Powder Coating Quote",
        "Ready to protect your frame, chassis or parts? Send photos, dimensions and your finish choice through our quote form, or call (905) 876-7060, Monday to Friday, 7 AM to 5 PM. Visit 10874 Steeles Ave E, Milton, or contact us with questions."
    ]

    auto_faqs = [
        ["What size of car parts can you coat?", "Our automotive powder coating handles everything from small brackets to full frames. Our capabilities page lists 6,000 lb capacity, so send dimensions and weight with your quote and we will confirm the fit."],
        ["How long does automotive powder coating take?", "Typical orders follow our 48-hour turnaround. Large, heavy or high-volume jobs are scheduled at quote, and we receive parts Monday to Friday, 7 AM to 5 PM."],
        ["Can you coat parts with rust or old paint?", "Yes, but heavy rust and old coatings must come off before powder goes on. Tell us the condition when you quote, and see our powder coat stripping and recoating service for parts that need full removal."],
        ["Will bolts and threads still fit after coating?", "Yes, when we mask them. We plug threaded holes and protect mounting faces, and we confirm film thickness on tight-tolerance parts. Flag fit-critical areas on your quote."],
        ["What finish suits winter driving and road salt?", "Protection depends on correct prep, the right powder and a full cure more than on colour or gloss. Tell us how the part is used, and we will recommend a powder for vehicle powder coating on trucks and cars driven through winter."],
        ["Do you offer pickup and delivery?", "For auto parts powder coating, pickup and delivery details are confirmed at quote based on your location and parts. You can also drop parts off at 10874 Steeles Ave E, Milton, during opening hours."]
    ]

    data["services"]["automotive-powder-coating"] = {
        "meta_title": "Automotive Powder Coating | Koojo Custom Powder Coating",
        "meta_desc": "Automotive powder coating for car frames, chassis, brackets and motorcycle parts. Chip-resistant finishes, 48-hour turnaround. Get a quote today.",
        "primary_kw": "automotive powder coating",
        "summary": "Automotive powder coating gives car frames, chassis parts and motorcycle components a tough, even finish that stands up to chips, rust and winter road salt. Finished in Milton with a 48-hour turnaround.",
        "body": auto_body,
        "faqs": auto_faqs
    }

    # 3. COMMERCIAL & BULK ORDERS (/services/bulk-commercial-orders)
    comm_table = make_table_block(
        ["Option", "What it gives you", "Best for"],
        [
            ["Gloss", "A smooth, high-shine look", "Visible parts, display items"],
            ["Matte or satin", "Lower glare and hides light scuffs", "Equipment, enclosures"],
            ["Textured", "Hides small surface marks and adds grip", "Handled parts, guards"],
            ["Film thickness", "Typical film is 2 to 4 mils, confirmed on fit-critical parts", "Threaded or tight-tolerance parts"],
            ["Repeat colour", "A RAL colour or sample matched on every reorder", "Reorders and recurring work"]
        ]
    )

    comm_body = [
        "Commercial powder coating gives fabricated metal parts a tough, even finish that holds up across large runs and repeat deliveries. At Koojo Custom Powder Coating, our Milton team handles bulk powder coating for businesses that need hundreds of matching parts, not just one. Since 2012, we have finished more than 10,000 items for customers across the GTA, with a 48-hour turnaround on typical orders. Whether you place a single purchase order or arrange a standing schedule, we plan each stage so every load looks the same. Call (905) 876-7060, Monday to Friday, 7 AM to 5 PM, or request a commercial powder coating quote below.",
        "## SPEC STRIP",
        "Since 2012 | 10,000+ Items | 48 Hr Turnaround | 5.0 ★ Google Rating",
        "## What Is Commercial Powder Coating?",
        "Commercial powder coating is a dry finishing process in which electrostatically charged powder is sprayed onto metal parts, then heated in an oven until it cures into a hard, even layer. It suits business orders where many parts must match, resist wear and ship on schedule.",
        "The finish is made from thermoset powder, which cures with heat instead of drying like liquid paint. At a cure temperature of 180 to 200 °C, the powder flows, bonds to the metal and hardens into one continuous coating without runs or drips. As a form of commercial metal finishing, it replaces liquid paint where durability and repeatability matter. That makes it a dependable corrosion-resistant and chip-resistant choice for parts that face handling, weather and wear.",
        "Typical customers send fabricated metal parts and commercial equipment components that must look alike from the first piece to the last. A commercial-grade finish should look the same on part one and part five hundred. Strong production powder coating depends on repeatable steps, so our commercial powder coating is planned around the whole order, starting from the bare metal. Our wider powder coating services cover the full range of work we do.",
        "## Our Commercial Powder Coating Process",
        "Our commercial powder coating process has six stages: intake and inspection, cleaning and pretreatment, masking, powder application, oven curing and final inspection. Each stage is documented so reorders match the first batch. The same controls support our industrial powder coating work.",
        [
            "Step 1 – Intake and Inspection: We check each part for heavy rust, old coatings, weld quality and damage, then confirm the finish, quantity and delivery date for your order. We also plan racking so every surface can be reached and each load holds as many parts as it safely can.",
            "Step 2 – Cleaning and Pretreatment: Parts are washed and chemically treated so the powder bonds to clean metal. Skipping this stage is a common reason finishes fail early. For more on this stage, see our powder coating surface preparation page.",
            "Step 3 – Masking and Plugging: Threads, bearing surfaces and mounting holes are protected before coating. Masking and plugging keep bolts turning and parts fitting, which matters when hundreds of identical parts must assemble without rework.",
            "Step 4 – Electrostatic Powder Application: Charged powder is applied by electrostatic spray onto the grounded part, so it wraps around tubes, corners and recesses. This gives an even film across every piece in the run.",
            "Step 5 – Oven Curing: Parts move into the curing oven, where commercial powder coating reaches temperature and hardens. Cure time depends on the powder and the mass of the part, so a heavy frame is planned differently from a small bracket.",
            "Step 6 – Final Inspection and Handoff: We inspect the cured finish for coverage, adhesion and appearance. Typical orders are ready within 48 hours, and larger production runs are scheduled when we quote. We receive parts Monday to Friday, 7 AM to 5 PM. We also record the colour and powder used, so a later order can repeat the finish exactly."
        ],
        "Our batch powder coating schedule keeps parts from waiting between steps, and for a tight lead time, tell us your date at quote.",
        "## Parts and Metals We Coat",
        "We apply commercial powder coating to steel and aluminum parts, including brackets, enclosures, frames, guards, panels and welded assemblies. Our capabilities page lists 6,000 lb capacity, so heavy assemblies, long frames and large batches are all worth a quote, and we confirm fit at intake.",
        [
            "Structural parts: frames, supports, brackets and base plates.",
            "Enclosures and guards: machine guards, panels, covers and housings.",
            "Site metalwork: posts, shelving, display racks and gates.",
            "Equipment parts: chutes, trays, carts and storage racks.",
            "Repeat items: identical parts shipped in large orders on a regular schedule."
        ],
        "Metals we handle include steel for frames and brackets, aluminum for lighter components, and cast parts such as covers and housings. Good commercial powder coating on mixed metals also depends on how parts are hung, so we confirm that at intake. Our bulk powder coating starts with a material check at intake, because the right prep and cure plan depends on the metal and the thickness of the part. Send photos and dimensions with your request, and we will tell you how your parts will be hung and coated.",
        "## Finish and Option Choices",
        "Choose from gloss, satin, matte and textured finishes in a wide range of colours. We confirm the powder type, colour code and film thickness at quote, so the finish suits the part, the metal and how it will be used. For wider palettes, see our custom powder coating colours page.",
        comm_table,
        "Whatever you pick, a consistent finish matters when parts from different loads ship together, so we record your colour code and powder for every job. For commercial powder coating that must match over time, give us your code once and we log it. This also helps when a reorder arrives months after the first batch. Film thickness affects fit, so flag tight tolerances before we coat.",
        "## Quality Standards for Commercial Powder Coating",
        "Our commercial powder coating follows recognized standards: ASTM D3359 for adhesion, ASTM D7091 for dry film thickness and ASTM B117 for salt spray resistance on every order. Koojo is certified through the Absolute Bureau of Certification, and test reports are available on request.",
        "Quality starts at intake and ends at handoff. After curing, a good finish looks even in colour and gloss, with no thin spots, runs or bare edges. Edges, welds and recesses get particular attention because thin spots usually appear there. We flag any concern with you before parts leave the shop.",
        "An adhesion test checks that the coating bonds to the metal. Dry film thickness readings confirm the coating is neither too thin to protect nor too thick to fit. The salt spray test measures corrosion resistance in a controlled chamber. It is a comparison tool rather than a promise of real-world life, so we explain what results mean for your commercial powder coating order.",
        "Batch inspection means each load is checked before parts leave the shop, which keeps later deliveries consistent with the first. Careful production powder coating also depends on clean prep and correct curing, so every order follows the same documented steps. See our certification page for details.",
        "## Recent Project: Automation Line Frame",
        "Our automation line frame shows how we handle large framed assemblies that must keep their finish in a busy production setting. Frames like this face grease, impact and constant handling, the same demands that bulk parts meet in daily use, so it is a useful reference for your own order.",
        "The case study records the part, metal, size, powder, colour and turnaround, with before and after photos. Read the automation line frame case study to see the standard behind our work, and expect the same documented approach on your commercial powder coating order.",
        "## Businesses That Use Commercial Powder Coating",
        "Manufacturers, contractors, fabricators, equipment builders and facility managers use our commercial powder coating most. These customers want dependable commercial metal finishing, fast turnaround and repeatable quality across batches, whether they send one part or a full run of matching items, and they want clear scheduling.",
        "See how we support powder coating for manufacturers, who often send matching frames and guards on a regular schedule, and powder coating for contractors, who need tough finishes on steel parts ready for site delivery.",
        "## Commercial Powder Coating FAQs",
        "Short answer: we run commercial powder coating on metal parts in batches, with fast turnaround on typical orders. These answers cover order size, timing, repeat work, colour and logistics so you know what to expect before you book. Ask us anything else before you send parts.",
        "## Get a Commercial Powder Coating Quote",
        "Ready to coat your next batch? Send photos, quantity, dimensions and your finish choice through our quote form, or call (905) 876-7060, Monday to Friday, 7 AM to 5 PM. Visit 10874 Steeles Ave E, Milton, or contact us with questions."
    ]

    comm_faqs = [
        ["How many parts can you coat in one order?", "We coat orders from a few parts to large orders of matching pieces. Our capabilities page lists 6,000 lb capacity, so send quantity, dimensions and weight with your request and we will confirm how the order is batched."],
        ["How long does a bulk order take?", "Typical commercial powder coating orders follow our 48-hour turnaround. Large or high-volume powder coating jobs are scheduled at quote based on quantity and part size. We receive parts Monday to Friday, 7 AM to 5 PM."],
        ["Can you match the same colour on every reorder?", "Yes. We record your colour and powder for each job so later batches match the first. Send a RAL code or a sample with your first order."],
        ["Can you set up recurring orders?", "Yes. Tell us the part, quantity and timing at quote, and we plan racking and booking so each load is handled the same way."],
        ["Can one order include different part sizes?", "Yes. We rack mixed parts so they cure well together, and heavier items are planned apart from small ones. List each part type with its quantity when you request a volume quote."],
        ["How do I get a quote for a large batch?", "Send photos, dimensions, quantity and finish through our quote form. Pickup and delivery details are confirmed at quote based on your location, or you can drop parts off at 10874 Steeles Ave E, Milton, during opening hours."]
    ]

    data["services"]["bulk-commercial-orders"] = {
        "meta_title": "Commercial Powder Coating | Koojo Custom Powder Coating",
        "meta_desc": "Commercial powder coating for bulk and recurring orders. Durable finishes, consistent batches and 48-hour turnaround. Request your quote today.",
        "primary_kw": "commercial powder coating",
        "summary": "Commercial powder coating gives fabricated metal parts a tough, even finish that holds up across large runs and repeat deliveries. Finished in Milton with a 48-hour turnaround.",
        "body": comm_body,
        "faqs": comm_faqs
    }

    # 4. CUSTOM POWDER COATING COLOURS & FINISHES (/services/custom-colors-finishes)
    custom_body = [
        "Custom powder coating colours give your metal parts an exact shade, sheen and texture instead of whatever a stock range happens to offer. At Koojo Custom Powder Coating in Milton, we have finished more than 10,000 items since 2012, and colour matching is part of that daily work. Whether you need a RAL shade, a brand colour or a match to a sample, our custom colour powder coating service turns the specification into a hard, even finish. Browse our custom powder coating colour options below.",
        "Our standard turnaround is 48 hours. We are open Monday to Friday, 7 AM to 5 PM, so you can send a sample, ask a question or drop off parts during the working week. Every order of custom powder coating colours starts with a short conversation about the part, the shade and where it will be used.",
        "## SPEC STRIP",
        "Since 2012 | 10,000+ Items | 48 Hr Turnaround | 5.0 ★ Google Rating",
        "## What Are Custom Powder Coating Colours?",
        "Custom powder coating colours are shades matched to your specification rather than picked from a stock range. The powder is sprayed on electrostatically and cured in an oven, so the colour becomes part of a hard, even finish instead of a thin layer of paint.",
        "Most requests fall into three groups. The first is a standard shade from our powder colour range. The second is RAL colour matching, where you give us a RAL number. The third is a colour match to a sample, where you send us a chip, swatch or small part. Each group changes how we source the powder and how we confirm the result with you. A custom powder coat colour is only as good as its reference, so a clear specification saves time.",
        "Custom powder coat colour is only half of the decision. Sheen levels decide how that colour looks once it is on the part. Gloss powder coating is smooth and bright, matte powder coating cuts glare, and satin powder coating sits in between. The same shade can read very differently in each, so we talk through sheen before we order the powder.",
        "## How We Match and Apply Custom Powder Coating Colours",
        "We confirm your colour reference, prepare the metal, apply the powder electrostatically, cure it at 180–200 °C and inspect the result against your sample. Each step protects the colour match and the finish quality from the first brief to the final check.",
        [
            "1. Colour brief. Send a RAL number, a RAL colour chart reference, a brand specification or physical colour samples. Samples are best, because screens and printed charts rarely show the true shade. This is where custom colour matching starts.",
            "2. Powder selection. We check the powder coating colour chart and our supplier range for your shade and finish. If a colour must be ordered in, we confirm the timing with you before work starts.",
            "3. Surface preparation. Clean metal holds colour evenly. We degrease, remove rust and scale, and pretreat the part where needed, as described on our surface preparation page.",
            "4. Masking. We plug threads and bores and cover contact points so your custom powder coat colour stays only where you want it.",
            "5. Spray and cure. The powder is applied electrostatically, then cured in the oven at 180–200 °C. The heat melts the powder and bonds the pigment into one continuous film.",
            "6. Inspection. We compare the finished custom powder coating colours with your reference, check coverage and thickness, and look for defects before packing."
        ],
        "Some finishes need an extra step. Candy colours and certain effect powders are often built as a two-coat finish, with a coloured base followed by a second layer. This adds time, so we explain it when we quote. For repeat orders, we record the powder and colour code to support batch colour consistency on later runs of your custom powder coating colours. Whether your custom powder coating colours are in stock changes the timing, so we check availability early.",
        "## Which Parts and Metals Can We Colour?",
        "We apply custom powder coating colours to steel and aluminum parts, from small brackets to large fabricated frames. The part must withstand oven curing, so we review each item before quoting. See our capabilities page for size and weight limits.",
        "Typical work includes railings, gates, bollards, machine guards, equipment housings and frames. Powder coating for fabricated parts is a large share of what we do, and one consistent colour across welded assemblies is often the main requirement. Galvanized and cast metals can need extra checks because trapped gases may affect the surface, so tell us the material when you ask for a quote. Send photos with your request so we can check size, weight and masking needs early. Every custom powder coat colour we apply is matched to the metal as well as the specification.",
        "Parts that live outdoors also need the right powder. UV-resistant powder coating holds its colour better in sunlight, which matters for fences, outdoor furniture and building metalwork. For an outdoor-durable finish on exterior products, see our architectural powder coating service, or read our guide to outdoor furniture finishes.",
        "## Finish Options for Your Colour Choice",
        "You can pair any custom powder coat colour with a finish type: gloss, satin, matte, textured, metallic, candy or clear coat. The finish changes how the colour looks, feels and wears, so it is worth choosing both together. These powder coating finishes give you plenty of room to match a design.",
        [
            "Gloss and high-gloss finish. A smooth, reflective surface that is easy to wipe clean.",
            "Satin and low-gloss finish. A softer sheen that shows fewer fingerprints and marks.",
            "Matte. A flat, modern look with the least glare.",
            "Textured powder coating. A wrinkle finish or hammertone finish adds pattern, and an anti-slip textured finish improves grip. Texture also hides surface imperfections such as light weld marks.",
            "Metallic powder coat. Our custom colour powder coating can include silver, bronze and copper metallics that add depth and sparkle.",
            "Candy powder coating. A translucent custom powder coat colour over a base that gives rich colour depth.",
            "Clear coat powder coating. A transparent top layer that protects metallic and candy effects."
        ],
        "Choosing between metallic shades? Our metallic finishes guide explains the differences, and our RAL colour guide shows how RAL numbers translate to powder.",
        "## How We Check Colour and Finish Quality",
        "We check your custom powder coat colour against your reference, measure film thickness and test adhesion before parts leave the shop. Our quality steps are outlined on our certification page, and test reports are available on request. Ask us about them when your project specification requires proof.",
        "Where a job calls for it, test methods include ASTM D3359 for adhesion, ASTM D7091 for dry film thickness and ASTM B117 for salt spray resistance. Our certification is held through the Absolute Bureau of Certification. A custom powder coating colour is only useful if it stays attached and even, so we test the finish as well as the shade.",
        "Fade resistance depends on the powder chemistry and the pigment. Bright reds and oranges fade faster outdoors than neutral tones, so we ask where the part will be used before recommending a powder.",
        "## Colour Work in Practice",
        "Our safety bollards project shows how a durable colour is chosen for exposed steel. The case study lists the part, metal, powder, colour code and turnaround, so you can see how the finish was specified.",
        "You can also browse more finished parts on our Our Work page, filtered by industrial, automotive, architectural and specialty projects. A good colour brief includes the part, the metal, the colour reference and the finish. With those four details, we can quote custom powder coating colours accurately and confirm the match before curing.",
        "## Who Uses Custom Colour Finishes",
        "Fabricators, welding shops, contractors and manufacturers order custom powder coating colours most often, because their parts must match a client's brand or a building's design. Consistent custom powder coating colours matter as much as the shade itself.",
        "Metal fabricators and welding shops send us weldments that must match a customer's colour. Contractors and construction teams order railings, gates and site metalwork in colours chosen by designers. Branded colour matching and corporate colour finishes are common for equipment makers. For larger production runs, see our industrial powder coating service, or browse all of our powder coating services. Whatever your sector, we handle custom powder coating colours the same way: confirm the reference, match the powder and check the result.",
        "## Custom Colour and Finish FAQs",
        "These answers cover colour matching, sheen, fading, clear coats and repeat orders for custom powder coating colours. Each answer is specific to this service, so you can decide quickly what to send us.",
        "## Request Your Custom Finish Quote",
        "Tell us about your custom powder coating colours, finish and quantity, and we will confirm the details before work begins. Request a quote online, call (905) 876-7060 or email sales@koojopowdercoating.com. We are at 10874 Steeles Ave E, Milton, and open Monday to Friday, 7 AM to 5 PM."
    ]

    custom_faqs = [
        ["Can you match a colour from a physical sample?", "Yes. Send a chip, swatch or small part and we will work to match it to the closest available powder. We tell you before work starts if the match is not close enough."],
        ["What is the difference between gloss, satin and matte?", "Sheen. Gloss is shiny and smooth, satin is softer and matte is flat. Sheen changes the look, while protection comes from the powder type and the preparation."],
        ["Will custom powder coating colours fade outdoors?", "Any colour can fade over time, but UV-resistant powders slow it. Bright reds and oranges fade faster than neutrals, so tell us the exposure and we will suggest a suitable powder."],
        ["Do metallic and candy finishes need a clear coat?", "Often, yes. A clear coat protects the effect and improves durability. We confirm whether your colour needs one when we prepare the quote."],
        ["Can you keep the same colour across repeat orders?", "Yes. We record the powder and colour code for each job, which supports batch colour consistency for your custom powder coating colours. Tell us if a tight match matters, because powder batches can vary slightly."],
        ["What do I need to send for a custom colour quote?", "Send the part size, quantity, finish and a colour reference such as a RAL number or sample. A photo of the part helps us confirm masking and preparation. This lets us price your custom powder coating colours accurately."]
    ]

    data["services"]["custom-colors-finishes"] = {
        "meta_title": "Custom Powder Coating Colours | Koojo Custom Powder Coating",
        "meta_desc": "Custom powder coating colours matched to RAL, brand or sample. Gloss, matte, textured and metallic finishes from Koojo in Milton. Request a quote.",
        "primary_kw": "custom powder coating colours",
        "summary": "Custom powder coating colours give your metal parts an exact shade, sheen and texture instead of whatever a stock range happens to offer. Finished in Milton with a 48-hour turnaround.",
        "body": custom_body,
        "faqs": custom_faqs
    }

    # 5. INDUSTRIAL POWDER COATING (/services/industrial-powder-coating)
    ind_table1 = make_table_block(
        ["Capacity", "Detail"],
        [
            ["Maximum part weight", "6,000 lb per piece"],
            ["Oven size", "23 ft L x 9 ft W x 9 ft H"],
            ["Metals", "Carbon steel, structural steel, aluminum, galvanized steel, cast iron"],
            ["Order size", "One-off parts to recurring production runs"],
            ["Batch volume", "1 to 1,000+ parts (prototypes to full production runs)"],
            ["On-site preparation", "Mobile sandblasting for fixed structures"]
        ]
    )

    ind_table2 = make_table_block(
        ["Powder", "Best for", "Limitation"],
        [
            ["Epoxy", "Indoor machinery, chemical and abrasion resistance", "Chalks and fades in sunlight"],
            ["Polyester", "Outdoor equipment and structures needing UV stability", "Lower chemical resistance than epoxy"],
            ["Hybrid (epoxy-polyester)", "Indoor enclosures, racks and guards", "Not suited to long outdoor exposure"],
            ["Super-durable polyester", "Outdoor parts needing long colour and gloss retention", "Higher material cost"],
            ["Zinc-rich primer + topcoat", "Road salt, outdoor steel and high-corrosion sites", "Two coats add time and cost"]
        ]
    )

    ind_table3 = make_table_block(
        ["Test", "Standard", "What it shows"],
        [
            ["Dry film thickness (DFT)", "ASTM D7091", "Coating is within the specified mil range"],
            ["Adhesion (cross-hatch)", "ASTM D3359", "Coating is properly bonded to the metal"],
            ["Salt spray", "ASTM B117", "Comparative corrosion resistance in hours"],
            ["Corrosivity category", "ISO 12944", "Which system suits the exposure, from C1 to CX"]
        ]
    )

    ind_table4 = make_table_block(
        ["Factor", "Powder coating", "Wet paint", "Hot-dip galvanizing"],
        [
            ["Application", "Electrostatic spray and oven cure", "Brush, roll or spray", "Dip in molten zinc"],
            ["Chip resistance", "High", "Low to medium", "High"],
            ["VOCs", "Near zero", "Released by solvent-borne paints", "None"],
            ["Colour options", "Full RAL range", "Full range", "Grey only"],
            ["Best for", "Durable colour on shop parts", "On-site touch-up", "Sacrificial corrosion protection"]
        ]
    )

    ind_body = [
        "Koojo Custom Powder Coating delivers industrial powder coating for structural steel, machinery, frames, guards and fabricated assemblies that must survive abrasion, chemicals, road salt and years outdoors. Every part is inspected, blasted, pretreated, coated, oven-cured and tested for film thickness and adhesion in one shop before each powder-coated part ships. We handle single pieces up to 6,000 lb and recurring production runs for OEMs and fabricators, with in-house and mobile sandblasting for structures that cannot travel to our shop. When your drawing names a powder, colour or film build, we meet that specification exactly and document the results for your records.",
        "## SPEC STRIP",
        "23 ft Oven • Up to 6,000 lb • 48 Hr Turnaround • In-House & Mobile Sandblasting • Since 2012 • 10,000+ Items • 5.0 ★ Google Rating",
        "## What Is Industrial Powder Coating?",
        "Industrial powder coating is a dry, electrostatically applied thermoset finish, cured at roughly 180 to 200 °C and engineered for parts in heavy service rather than for appearance alone. Compared with decorative work, it demands tighter control of surface profile, film thickness and cure, backed by documented testing.",
        "An industrial coating system is chosen for the exposure the part will face: indoor plant floors, washdown areas, outdoor yards or salted roads. That choice sets the blast grade, pretreatment, powder chemistry and whether a primer is needed. Typical parts include machine bases, conveyor frames, structural beams, storage racks, electrical enclosures, safety guards, hoppers, chutes and trailer components. New to the finish itself? Start with our guide on what is powder coating, then come back here for the industrial detail that matters on spec work.",
        "## What We Can Coat: Size, Weight & Volume",
        "We coat parts from small brackets to structural assemblies weighing up to 6,000 lb, as single pieces or recurring production batches. Our cure oven fits parts up to 23 ft long, 9 ft wide and 9 ft high, so most frames, bases and long beams are coated whole rather than cut into sections.",
        ind_table1,
        "Coating large weldments whole avoids extra joints and touch-up lines in the finished industrial powder coating. Every heavy-duty powder coating job is scheduled so cure time is never rushed. Full equipment limits are listed on our large part powder coating page.",
        "## Our Industrial Powder Coating Process",
        "Every order moves through the same eight controlled steps, from spec review to packed shipment, so results repeat from the first part to the last. Each step is recorded against your drawing, which is how we meet an industrial coating spec rather than simply a colour.",
        "### Inspection & Spec Review",
        "We check the drawing or spec sheet, metal type, weld quality, part weight and exposure environment, then confirm the powder, colour, film build and any test requirements in writing before work starts.",
        "### Abrasive & Mobile Sandblasting",
        "Rust, mill scale and old coatings are removed by abrasive blasting, leaving a clean, angular profile that meets your specified SSPC or ISO blast grade. Fixed or oversized structures can be blasted on site with our sandblasting services.",
        "### Cleaning & Phosphate Pretreatment",
        "Parts are degreased, rinsed and treated with iron or zinc phosphate to improve adhesion and slow under-film corrosion. Our powder coating surface preparation page explains each chemical stage in more detail.",
        "### Masking & Plugging",
        "Threads, bores, bearing seats, grounding points and mating faces are plugged or taped with high-temperature masking, so they stay bare and fit correctly at assembly.",
        "### Electrostatic Powder Application",
        "Charged powder is sprayed onto the grounded part, wrapping edges and recesses evenly. Primer and topcoat are applied in sequence when a two-coat industrial powder coating system is specified for harsher exposure.",
        "### Oven Curing",
        "Parts are cured to the powder maker's schedule, typically 180 to 200 °C for 10 to 20 minutes at metal temperature, so the film fully cross-links. Thick, heavy sections are given longer soak time to reach temperature.",
        "### Quality Inspection & DFT Check",
        "We measure dry film thickness, run adhesion checks and inspect colour, gloss and coverage on each batch. Readings are recorded for every batch and can be supplied with your order.",
        "### Packaging & Shipping",
        "Finished parts are wrapped, blocked and strapped to protect the powder-coated surface in transit, then shipped or held for pickup at our shop.",
        "## Which Powder Is Best for Industrial Parts?",
        "The right powder depends on exposure. Epoxy suits indoor and chemical exposure, polyester suits outdoor UV, and a zinc-rich primer under a topcoat suits road salt and high corrosion. Matching chemistry to exposure is the core of heavy-duty powder coating.",
        ind_table2,
        "On industrial powder coating jobs with a written spec, we follow the specified powder and its supplier data sheet exactly. Unsure? Tell us where the part will live and we will recommend one. For deeper chemistry, read epoxy vs polyester powder coating.",
        "## Performance Testing & Quality Control",
        "We verify each order against measurable, repeatable tests, not appearance alone. Film thickness and adhesion are checked in our shop on every batch, while salt spray and corrosivity ratings are matched to the powder supplier's certified data for your environment.",
        ind_table3,
        "Results can be supplied with each shipment, so your inspector, auditor or end customer has written proof that the finish meets the agreed spec. This documentation is what separates industrial powder coating from cosmetic work, and it is available on every powder-coated order. Our ASTM standards for powder coating guide explains each method, and our powder coating quality assurance page covers certification.",
        "## Industries & Parts We Coat",
        "Our industrial coating customers range from fabricators and OEMs to contractors and municipalities. Most send steel parts that work hard: frames, bases, guards, chutes, bollards and implements, each given industrial powder coating suited to its sector.",
        [
            "Metal Fabricators & Welding Shops: weldments and frames coated to spec. See powder coating for metal fabricators.",
            "Manufacturing & Automation: conveyor frames, robotic bases and machine guards. See powder coating for manufacturers.",
            "Machine Shops: precision-masked parts with clean threads. See powder coating for machine shops.",
            "Contractors & Construction: structural steel, stairs and railings. See powder coating for contractors.",
            "Food Processing Equipment: washdown-resistant line frames. See powder coating for food processing equipment.",
            "Agricultural & Heavy Equipment: implements and trailers. See agricultural equipment powder coating.",
            "Municipal & Institutional: bollards and public metalwork. See powder coating for municipalities."
        ],
        "## Industrial Powder Coating vs Wet Paint vs Galvanizing",
        "Powder coating gives the toughest chip-resistant colour finish, galvanizing gives sacrificial zinc protection, and wet paint is easiest to apply on site. For outdoor steel, galvanizing under a powder-coated topcoat often performs best.",
        ind_table4,
        "For full comparisons, see powder coating vs wet paint and powder coating vs galvanizing.",
        "## Recent Industrial Projects",
        "These jobs show how we handle large, spec-driven parts from first blast to final shipment. Each case study lists the metal, size, prep, powder, colour code and turnaround for the powder-coated part, with before-and-after photos.",
        [
            "Conveyor Frame for an Automotive Plant: a long steel frame coated in one piece to the plant's colour standard.",
            "Automation Line Frame: a multi-section frame finished in one batch for matched colour along the line.",
            "Robotic Base: a heavy base masked at its machined mounting faces before coating."
        ],
        "Browse more powder coating projects.",
        "## What Affects Cost and Lead Time",
        "Price and lead time depend on part size and weight, surface condition, masking, powder type, number of coats and order volume. Clean, bare steel in a standard colour moves fastest.",
        [
            "Size and weight: larger parts use more oven space and handling.",
            "Surface condition: rust, mill scale or old paint add blasting.",
            "Masking: every plugged hole adds labour.",
            "Coats: primers and two-coat systems add cure cycles.",
            "Volume: repeat runs in one colour cost less per part."
        ],
        "We quote every industrial powder coating job to its drawings; our powder coating cost Ontario guide explains typical ranges.",
        "## How to Get an Industrial Powder Coating Quote",
        "Send drawings or photos, dimensions, weight, quantity, metal type, colour or RAL code and any coating spec through our powder coating quote form, or call (905) 876-7060. We reply with a written price, lead time and process plan within 1 business day.",
        "Tell us the exposure, such as indoor, outdoor or washdown, to help us recommend the right powder. Drop parts at our Milton shop, a short drive from Highway 401, or book a pickup.",
        "## Industrial Powder Coating FAQs",
        "These answers cover what engineers, buyers and fabricators ask us most often before sending parts, from welded assemblies and film thickness to galvanized steel, test reports and outdoor service life.",
        "## Ready to Quote Your Industrial Job?",
        "Send your drawings, quantities and finish requirements, and we will reply with a written price, lead time and process plan for your industrial powder coating. Need other finishes? See all our powder coating services."
    ]

    ind_faqs = [
        ["Can you powder coat parts that are already welded or assembled?", "Yes, if the assembly can handle cure temperatures of about 200 °C. Rubber, plastic, bearings and electronics must come out first or the oven will damage them."],
        ["How thick should an industrial powder coat be?", "Most single-coat parts are specified at 2 to 4 mils, and two-coat systems with a primer often run 4 to 6 mils. Our powder coating thickness guide explains the ranges."],
        ["Can galvanized steel be powder coated?", "Yes, with the right preparation. Galvanized steel is sweep-blasted and often preheated to release trapped gas, which prevents pinholes. Our powder coating galvanized steel guide explains outgassing."],
        ["Do you supply film thickness readings or test reports?", "Yes. DFT and adhesion results can be recorded and supplied with your shipment, and supplier data sheets cover salt spray and chemical resistance. Ask for reports when you request a quote."],
        ["How long does industrial powder coating last outdoors?", "A well-prepared polyester or super-durable system commonly lasts 10 to 20 years outdoors, depending on UV, salt and abrasion. A zinc-rich primer extends service life on steel in corrosive sites."]
    ]

    data["services"]["industrial-powder-coating"] = {
        "meta_title": "Industrial Powder Coating | Heavy-Duty Metal Parts | Koojo",
        "meta_desc": "Industrial powder coating for steel and aluminum parts up to 6,000 lb. In-house blasting, phosphate pretreatment and tested finishes. Get a quote.",
        "primary_kw": "industrial powder coating",
        "summary": "Heavy-duty, rust-resistant finishes for machinery, equipment, structural steel and conveyor frames, cured in our 23 ft oven. Finished in Milton with a 48-hour turnaround.",
        "body": ind_body,
        "faqs": ind_faqs
    }

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("Successfully restored all 5 service pillars with native tables and exact blueprint copy!")

if __name__ == "__main__":
    restore_services()
