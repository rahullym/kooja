"""Authored seed content for the Koojo site, following the 2026 website blueprint.

Body shorthand used throughout (converted to Portable Text by build.py):
  "## Heading"   -> h2          "### Heading" -> h3
  ["a", "b"]     -> bullet list  anything else -> paragraph
  [label](url)   -> inline link

Facts come from the live koojopowdercoating.com pages and the blueprint. Anything
the business still has to confirm (oven width/height, drive times, case-study
specs, team names) is deliberately left out rather than guessed.
"""

WIX = "https://static.wixstatic.com/media/"


def img(media_id, alt, filename, width=1600):
	"""Seed media reference, resized by Wix so we do not import 3 MB originals."""
	return {"$media": {"url": f"{WIX}{media_id}/v1/fit/w_{width},h_{width},q_85/{filename}", "alt": alt, "filename": filename}}


SETTINGS = {"title": "Koojo Custom Powder Coating", "tagline": "Industrial-grade powder coating in Milton, serving the Greater Toronto Area since 2012."}

# ---------------------------------------------------------------------------
# Services (/services/<slug>) -- process intent. Cities never in title or H1.
# ---------------------------------------------------------------------------

SERVICES = [
	{
		"slug": "industrial-powder-coating",
		"title": "Industrial Powder Coating",
		"nav_label": "Industrial Powder Coating",
		"keyword": "industrial powder coating",
		"seo_title": "Industrial Powder Coating | Koojo Custom Powder Coating",
		"summary": "Heavy-duty, rust-resistant finishes for machinery, equipment, structural steel and conveyor frames, cured in a 23 ft oven with a 6,000 lb capacity.",
		"image": img("b95a8d_c448034e96aa4e7c94f96969ea940423~mv2.jpeg", "A heavy fabricated frame base coated blue", "koojo-industrial-frame-base.jpg"),
		"body": [
			"Industrial powder coating is a dry finishing process that bonds a thermoset powder to metal with an electrostatic charge and cures it in an oven into a hard, continuous film. At Koojo we use it to protect machinery, equipment, structural steel and conveyor frames that have to keep working in plants, yards and on the road.",
			"## What industrial powder coating protects against",
			"A cured powder finish resists chipping, scratching, fading, rust and corrosion far better than a conventional wet paint film. That matters on parts that get bumped by forklifts, washed down, or left outdoors through an Ontario winter of road salt and freeze-thaw cycles.",
			"## What we coat",
			"We coat heavy fabrications and production parts alike. Typical work includes:",
			["Machine frames, bases and guards", "Conveyor and automation line frames", "Structural steel and weldments", "Chutes, bollards and equipment housings", "Tools, racks and material-handling equipment"],
			"For the size and weight limits of our line, see [large part powder coating](/capabilities).",
			"## How the process works",
			"Every part is degreased, chemically cleaned and phosphated, then rinsed, dried, masked and inspected before any powder is applied. Powder is sprayed electrostatically and cured in the oven. Good preparation is what makes the finish last, which is why [powder coating surface preparation](/services/surface-preparation) is part of every industrial job.",
		],
		"faqs": [
			("How big a part can you powder coat?", "Our oven is 23 ft long and our line handles parts up to 6,000 lb. Send us the dimensions and weight of your largest piece and we will confirm it fits before you ship."),
			("Is industrial powder coating suitable for outdoor equipment?", "Yes. With the right pretreatment and a polyester or hybrid powder chosen for UV and weather exposure, powder-coated equipment holds its colour and resists rust outdoors."),
			("Can you match our existing equipment colour?", "In most cases, yes. Give us a RAL number, a manufacturer colour code or a sample part and we will match it as closely as the available powders allow."),
			("Do you take one-off industrial parts or only production runs?", "Both. We coat single frames and prototypes as well as recurring production batches."),
		],
		"services": ["surface-preparation", "sandblasting"],
		"industries": ["manufacturing-automation", "metal-fabricators-welding-shops"],
		"project": "conveyor-frame-automotive-plant",
	},
	{
		"slug": "surface-preparation",
		"title": "Powder Coating Surface Preparation & Pretreatment",
		"nav_label": "Surface Preparation",
		"keyword": "powder coating surface preparation",
		"seo_title": "Powder Coating Surface Preparation & Pretreatment | Koojo",
		"summary": "Degreasing, chemical cleaning, phosphate pretreatment, rinsing, drying and masking, so the powder bonds properly and the finish lasts.",
		"image": img("b95a8d_06cd3354e8c54fb68fbff5e140c38165~mv2.jpg", "A coated plate with masking still in place", "koojo-masked-plate.jpg"),
		"body": [
			"Powder coating surface preparation is the cleaning and pretreatment a metal part goes through before powder is applied. It removes oil, dirt and residue and leaves a conversion coating the powder can bond to. Skipping it is the most common reason a coating peels or rusts early.",
			"## What surface preparation includes",
			"Our preparation line follows the same sequence on every job:",
			["Degreasing: removing oils, grease and dirt with cleaning solutions", "Chemical cleaning: treatments that eliminate remaining residues", "Phosphating: a conversion coating that improves corrosion resistance and powder bonding", "Rinsing: clearing chemicals from the surface, with a deionized final rinse where mineral spotting is a concern", "Drying: in an oven or with hot air, because trapped moisture causes adhesion defects"],
			"## How masking and plugging work",
			"Masking keeps powder off the areas that must stay bare, such as threads, bores, mating faces and grounding points. We cover them with high-temperature tape, plugs or caps before coating and remove them after cure. Mark these areas on your drawing or tag them on the part at drop-off.",
			"## Inspection before coating",
			"After preparation each part is inspected for contaminants and surface defects. Only parts that pass move on to the booth. Parts with heavy rust, mill scale or old coatings are routed to [sandblasting services](/services/sandblasting) first.",
		],
		"faqs": [
			("Why does powder coating need pretreatment?", "Powder bonds to clean, chemically prepared metal. Pretreatment removes contaminants and adds a phosphate layer that improves adhesion and slows corrosion if the finish is ever damaged."),
			("What is the difference between iron and zinc phosphate?", "Both are conversion coatings. Iron phosphate is a common general-purpose pretreatment, while zinc phosphate builds a heavier layer for harsher environments. Tell us where the part will live and we will recommend one."),
			("Do I need to clean parts before dropping them off?", "No special cleaning is required. Remove any non-metal hardware, rubber and plastic, and let us know about heavy grease or old paint so we can plan the prep."),
			("Can you mask threaded holes and machined faces?", "Yes. Threads, bores and machined faces are masked or plugged before coating so they stay to size."),
		],
		"services": ["sandblasting", "industrial-powder-coating"],
		"industries": ["machine-shops", "metal-fabricators-welding-shops"],
		"project": "automation-line-frame",
	},
	{
		"slug": "sandblasting",
		"title": "Sandblasting Services & Mobile Sandblasting",
		"nav_label": "Sandblasting",
		"keyword": "sandblasting services",
		"seo_title": "Sandblasting Services & Mobile Sandblasting | Koojo",
		"summary": "Abrasive blasting that strips rust, mill scale and old coatings back to clean metal, in our shop or on site with mobile sandblasting.",
		"image": img("06611b_d35aff27f666448e834edc418e4a88cd~mv2.jpg", "Fabricated frames and bare steel plate on the shop floor", "koojo-frames-and-bare-steel.jpg"),
		"body": [
			"Sandblasting, also called abrasive or media blasting, propels abrasive media at a surface to strip rust, mill scale, paint and old powder coat back to clean metal. It also leaves a surface profile that helps a new coating grip. We offer it in the shop and as a mobile service.",
			"## When a part needs sandblasting",
			"Blasting is the right first step when chemical cleaning alone will not leave sound metal. That includes hot-rolled steel with mill scale, rusted or pitted parts, and anything carrying an old coating that has to come off before recoating.",
			"## Mobile sandblasting",
			"Mobile sandblasting brings the equipment to you for work that cannot travel, such as installed structures or equipment that is too large or too awkward to move. Contact us with the location, the surface area and what is on the surface now, and we will tell you whether it is a fit.",
			"## Blasting before powder coating",
			"Blasted steel starts to flash-rust quickly, so parts we blast go straight into pretreatment and coating. Combining blasting with [industrial powder coating](/services/industrial-powder-coating) in one shop avoids the handling and delay of moving parts between vendors.",
		],
		"faqs": [
			("What is the difference between sandblasting and media blasting?", "They describe the same process. \"Media\" is the abrasive used, which is chosen to suit the metal and the coating being removed."),
			("Will sandblasting damage thin sheet metal?", "It can warp thin panels if done with the wrong media or pressure. Tell us the material and thickness and we will choose a gentler approach or recommend chemical stripping."),
			("Can you sandblast without powder coating afterwards?", "Yes, blasting is available on its own. Bare blasted steel should be primed or coated promptly to prevent flash rust."),
			("Do you remove mill scale from new steel?", "Yes. Mill scale on hot-rolled steel is removed by blasting so the coating bonds to the steel itself."),
		],
		"services": ["surface-preparation", "restoration-recoating"],
		"industries": ["contractors-construction", "agricultural-heavy-equipment"],
		"project": "safety-bollards",
	},
	{
		"slug": "custom-colors-finishes",
		"title": "Custom Powder Coating Colours & Finishes",
		"nav_label": "Custom Colours & Finishes",
		"keyword": "custom powder coating colours",
		"seo_title": "Custom Powder Coating Colours & Finishes | Koojo",
		"summary": "RAL colour matching and a full range of finishes: matte, gloss, textured, metallic, candy and clear coat.",
		"image": img("b95a8d_6e2f8bcec2df4b3c9ece3837a9603283~mv2.jpg", "Orange powder being sprayed onto a part in the booth", "koojo-orange-powder-in-booth.jpg"),
		"body": [
			"Custom powder coating colours let you specify the exact colour, gloss level and texture of a finish rather than choosing from a short stock list. We match RAL numbers and samples and apply matte, gloss, textured, metallic, candy and clear-coat finishes.",
			"## How colour matching works",
			"The fastest route is a RAL number, which identifies a standard colour every powder supplier can produce. If you have a brand colour or a physical sample instead, we compare it against available powders and confirm the closest match with you before coating.",
			"## Which finishes are available",
			["Matte and satin: low-glare finishes that hide handling marks", "Gloss: a smooth, reflective finish that is easy to wipe clean", "Textured and wrinkle: hides weld and surface imperfections and adds grip", "Metallic and candy: decorative effects, usually finished with a clear topcoat", "Clear coat: protection over bare or polished metal and over metallics"],
			"## Choosing a finish for outdoor use",
			"Outdoor parts need a powder chemistry that tolerates sunlight as well as a colour you like. Polyester powders hold colour and gloss outdoors, which is why they are the usual choice for railings, gates and furniture. See [architectural powder coating](/services/architectural-coatings) for exterior specifications.",
		],
		"faqs": [
			("Can you match a colour without a RAL number?", "Yes. Bring a sample part, a paint chip or a manufacturer colour code and we will find the closest available powder."),
			("Do metallic finishes need a clear coat?", "Most do. A clear topcoat protects the metallic flake from oxidizing and makes the finish easier to clean."),
			("Is there a minimum order for a custom colour?", "Standard colours can be coated in any quantity. Special-order powders are bought per job, so tell us the quantity and we will advise."),
			("Will the colour look the same on every batch?", "Using the same powder, cure schedule and film thickness keeps batches consistent. For repeat work we record the powder and settings used."),
		],
		"services": ["architectural-coatings", "specialty-custom-projects"],
		"industries": ["municipal-institutional", "contractors-construction"],
		"project": "church-gates",
	},
	{
		"slug": "restoration-recoating",
		"title": "Powder Coat Stripping and Recoating",
		"nav_label": "Restoration & Recoating",
		"keyword": "powder coat stripping and recoating",
		"seo_title": "Powder Coat Stripping and Recoating | Koojo",
		"summary": "We strip worn powder coat and paint, repair rust and recoat old parts so they look and perform like new.",
		"image": img("b95a8d_71770284e59844a18dc5c4e73bfafb78~mv2.jpg", "Spraying a steel frame in the booth", "koojo-spraying-frame.jpg"),
		"body": [
			"Powder coat stripping and recoating removes a failed or dated finish, repairs the metal underneath and applies a fresh powder coating. It costs less than replacing a sound part and, done properly, the new finish performs like an original one.",
			"## What can be restored",
			"Most steel and aluminum items that are structurally sound can be stripped and recoated. Common jobs include outdoor furniture, railings and gates, equipment panels, trailers and automotive parts.",
			"## How old coatings are removed",
			"Old powder coat and paint are taken off by abrasive blasting or chemical stripping, depending on the metal and its thickness. Rust is removed back to clean metal at the same stage, because coating over rust only hides it for a short time.",
			"## Recoating",
			"Once the part is bare it goes through the same pretreatment as new work and is coated in the colour and finish you choose. This is a good moment to change colour: see [custom powder coating colours](/services/custom-colors-finishes).",
		],
		"faqs": [
			("Is it cheaper to recoat or replace?", "For a sound part, recoating is usually cheaper than replacement. If rust has eaten through the metal, replacement or repair by a fabricator comes first."),
			("Can you remove powder coating from aluminum?", "Yes. Aluminum is softer than steel, so we choose a stripping method that removes the coating without damaging the surface."),
			("Can you powder coat directly over the old finish?", "We do not recommend it. A new coating is only as good as what is underneath, so failing finishes are removed first."),
			("How should I prepare an item for restoration?", "Remove plastic, rubber, glass and upholstery, since they cannot go through the cure oven. We handle the stripping."),
		],
		"services": ["sandblasting", "automotive-powder-coating"],
		"industries": ["agricultural-heavy-equipment", "municipal-institutional"],
		"project": "church-gates",
	},
	{
		"slug": "automotive-powder-coating",
		"title": "Automotive Powder Coating",
		"nav_label": "Automotive Powder Coating",
		"keyword": "automotive powder coating",
		"seo_title": "Automotive Powder Coating | Koojo Custom Powder Coating",
		"summary": "Scratch-resistant finishes for car and motorcycle frames, chassis parts, brackets and valve covers.",
		"image": img("b95a8d_54a73a631b7f46e1867812a2f1959555~mv2.jpg", "Parts racked in the spray booth", "koojo-parts-racked-in-booth.jpg"),
		"body": [
			"Automotive powder coating applies a durable, scratch-resistant finish to vehicle frames and components. We coat car and motorcycle frames, chassis and suspension parts, brackets and valve covers for restorers, builders and shops.",
			"## Which parts we coat",
			["Car, truck and motorcycle frames", "Chassis, subframes and suspension components", "Brackets, mounts and cross-members", "Valve covers, intake parts and engine-bay dress-up pieces"],
			"Wheels are handled as their own service: see [rim powder coating](/services/wheel-rim-powder-coating).",
			"## Why powder suits vehicle parts",
			"Underbody and engine-bay parts see road salt, stone chips, heat and fluids. A cured powder film is thicker and tougher than most paint systems and covers welds and edges evenly, which is where rust on a frame usually starts.",
			"## Preparing parts for coating",
			"Parts must be fully disassembled, with bearings, bushings, seals, rubber and plastic removed, because everything goes through a cure oven. Tell us which threads, bores and mating faces to mask.",
		],
		"faqs": [
			("Can you powder coat a full car frame?", "Yes. Frames are blasted to bare metal, pretreated and coated. Our oven is 23 ft long, so full-length frames fit."),
			("Do parts need to be disassembled first?", "Yes. Anything that is not bare metal, including bearings, bushings and seals, has to come off before coating."),
			("Can valve covers and engine parts be powder coated?", "Yes, provided they are fully degreased. Cast parts are pre-baked first to drive out trapped oil that would otherwise mark the finish."),
			("Will powder coating hold up to brake fluid and fuel?", "Cured powder resists occasional splashes, but spills should be wiped off promptly."),
		],
		"services": ["wheel-rim-powder-coating", "restoration-recoating"],
		"industries": ["machine-shops", "metal-fabricators-welding-shops"],
		"project": "conveyor-frame-automotive-plant",
	},
	{
		"slug": "wheel-rim-powder-coating",
		"title": "Rim Powder Coating",
		"nav_label": "Wheels & Rims",
		"keyword": "rim powder coating",
		"seo_title": "Rim Powder Coating & Wheel Refinishing | Koojo",
		"summary": "Alloy wheel powder coating and refinishing: old finish stripped, rims coated in the colour of your choice.",
		"image": img("b95a8d_1e3d4c90a80745c1a005285464b3ace2~mv2.jpg", "A steel wheel finished in a purple metallic powder coat", "koojo-purple-metallic-wheel.jpg"),
		"body": [
			"Rim powder coating strips a wheel to bare metal and applies a new baked-on finish. It is the most durable way to refinish alloy wheels or change their colour, and it stands up to brake dust, road salt and cleaning far better than spray paint.",
			"## How rims are refinished",
			"Tires, valve stems and weights come off first. Each rim is stripped, cleaned and pretreated, then coated and cured. Mounting faces and lug seats are masked so the wheel still seats correctly on the hub.",
			"## Colour and finish options",
			"Gloss black, satin black, gunmetal, silver and bronze are the most requested wheel colours, and any RAL colour is possible. Metallic finishes are sealed under a clear topcoat.",
			"## What rim coating does not fix",
			"Powder coating follows the surface it is applied to. Curb rash, bends and cracks need repair by a wheel specialist before coating, and structurally damaged wheels should be replaced.",
		],
		"faqs": [
			("Do tires have to be removed before rim powder coating?", "Yes. Tires, valve stems, sensors and weights must be removed because the wheel is stripped and oven-cured."),
			("How long does powder coating last on rims?", "With normal washing a powder-coated rim keeps its finish for years. Avoid harsh acidic wheel cleaners."),
			("Can you powder coat chrome rims?", "Chrome has to be removed completely first, which adds work. Send us photos and we will tell you whether it is practical."),
			("Can I get all four rims done at once?", "Yes. Coating a full set together keeps the colour and gloss identical across all four."),
		],
		"services": ["automotive-powder-coating", "custom-colors-finishes"],
		"industries": [],
		"project": None,
	},
	{
		"slug": "architectural-coatings",
		"title": "Architectural Powder Coating",
		"nav_label": "Architectural Powder Coating",
		"keyword": "architectural powder coating",
		"seo_title": "Architectural Powder Coating | Koojo Custom Powder Coating",
		"summary": "Weather-resistant finishes for railings, window frames, fences and gates on commercial and residential projects.",
		"image": img("06611b_7b5a811cfa624e9bb4c1abefb0828dd5~mv2.jpg", "Coated bollards hanging on the line", "koojo-bollards-on-the-line.jpg"),
		"body": [
			"Architectural powder coating protects and colours the exterior metalwork of a building or site. We coat railings, window frames, fences, gates and bollards with finishes selected to hold their colour and resist corrosion outdoors.",
			"## What we coat for buildings and sites",
			["Railings, guards and handrails", "Fences, gates and posts", "Window and door frames", "Bollards, canopies and site furniture"],
			"## Which specification to ask for",
			"Exterior aluminum is commonly specified to an AAMA performance level. AAMA 2604 and 2605 are the higher-performance levels, written around long-term colour and gloss retention. If your drawings call out a level, send us the spec section so we can select a powder that meets it.",
			"## Working with contractors and installers",
			"We coat to your schedule and package finished work for transport to site. Long sections are welcome: check [large part powder coating](/capabilities) for our length and weight limits.",
		],
		"faqs": [
			("Is powder coating suitable for exterior railings?", "Yes. With proper pretreatment and an exterior-grade polyester powder, railings resist rust and fading for years."),
			("Can you coat galvanized steel railings?", "Yes. Galvanized parts need specific preparation and a pre-bake to prevent bubbling, so tell us in advance."),
			("Do you coat aluminum window frames?", "Yes. Aluminum extrusions and fabricated frames are pretreated and coated to the specified colour."),
			("Can site-welded sections be touched up after installation?", "Field welds cannot be powder coated in place. Plan joints so coated sections bolt together, or allow for a compatible touch-up paint."),
		],
		"services": ["custom-colors-finishes", "sandblasting"],
		"industries": ["contractors-construction", "municipal-institutional"],
		"project": "safety-bollards",
	},
	{
		"slug": "bulk-commercial-orders",
		"title": "Commercial Powder Coating & Bulk Orders",
		"nav_label": "Commercial & Bulk Orders",
		"keyword": "commercial powder coating",
		"seo_title": "Commercial Powder Coating & Bulk Orders | Koojo",
		"summary": "Production powder coating for high-volume and recurring orders, with consistent finish from batch to batch.",
		"image": img("b95a8d_fc7d68641acb4774bb920e0d82b5bafb~mv2.jpg", "A white powder-coated equipment enclosure", "koojo-white-enclosure.jpg"),
		"body": [
			"Commercial powder coating is production finishing for businesses: high-volume runs, recurring orders and scheduled work for manufacturers and fabricators. We set up each part once, record the powder and settings, and repeat them on every batch.",
			"## How recurring orders work",
			"For repeat parts we keep the colour, powder, masking and racking details on file so each release is coated the same way. If you work with blanket purchase orders, send us your forecast and we will plan capacity around your releases.",
			"## Keeping batches consistent",
			"Consistency comes from controlling the same variables every time: preparation, film thickness and cure. Parts are inspected before coating and after cure.",
			"## Packaging and shipping",
			"Finished parts are wrapped and packed to suit the part, from protective wrap and boxes to custom packing for large or irregular items. We work with shipping providers to deliver across Milton and the GTA, or you can arrange your own pickup.",
		],
		"faqs": [
			("Is there a minimum quantity for commercial orders?", "No. We coat everything from a handful of parts to full production runs. Pricing reflects quantity and setup."),
			("Can you hold a colour standard across multiple orders?", "Yes. We record the powder and process settings for repeat parts and use them on every batch."),
			("Do you offer scheduled pickups and deliveries?", "We can arrange delivery through our shipping partners or coordinate with your carrier. Ask when you request a quote."),
			("How should production parts be delivered to you?", "Clean, dry and racked or palletized so they can be unloaded safely. Let us know about any handling restrictions."),
		],
		"services": ["industrial-powder-coating", "surface-preparation"],
		"industries": ["manufacturing-automation", "metal-fabricators-welding-shops"],
		"project": "automation-line-frame",
	},
	{
		"slug": "specialty-custom-projects",
		"title": "Specialty Powder Coating & Custom Projects",
		"nav_label": "Specialty & Custom Projects",
		"keyword": "specialty powder coating",
		"seo_title": "Specialty Powder Coating & Custom Projects | Koojo",
		"summary": "One-off parts, art pieces, prototypes and unusual shapes, coated with the same care as production work.",
		"image": img("b95a8d_4b694450f09e4f26b0a8dbca001bced2~mv2.jpg", "Red and blue custom plaques laid out after coating", "koojo-custom-plaques.jpg"),
		"body": [
			"Specialty powder coating covers the jobs that do not fit a production line: one-off parts, art pieces, prototypes and unusual shapes. We give them the same preparation and inspection as industrial work.",
			"## What counts as a specialty project",
			["Sculpture and custom art pieces", "Prototypes and pre-production samples", "Custom furniture and fixtures", "Vintage and hobby restorations, such as bicycle frames"],
			"## How we approach a one-off",
			"Unusual shapes take planning: where to hang the part, what to mask and how the powder will reach recesses. We review photos or drawings with you first and agree on the finish before anything is coated.",
			"## Materials that can be coated",
			"Any metal that holds an electrostatic charge and tolerates cure temperatures of roughly 180 to 200 °C can be powder coated. That covers steel, stainless steel and aluminum. Wood, plastic and rubber cannot go through the oven.",
		],
		"faqs": [
			("Will you coat a single small part?", "Yes. Single items are welcome."),
			("Can you powder coat an art piece with fine detail?", "Usually. Powder builds a thicker film than paint, so very fine detail can soften. Send photos and we will advise."),
			("Can I supply my own powder?", "Ask us first. We need to confirm the powder suits our equipment and cure schedule."),
			("Can I see a sample before the full piece is coated?", "For custom colours and effects we can coat a test panel so you can approve the finish."),
		],
		"services": ["custom-colors-finishes", "restoration-recoating"],
		"industries": ["machine-shops", "municipal-institutional"],
		"project": "church-gates",
	},
]

# ---------------------------------------------------------------------------
# Industries (/industries/<slug>) -- buyer intent.
# ---------------------------------------------------------------------------

INDUSTRIES = [
	{
		"slug": "metal-fabricators-welding-shops",
		"title": "Powder Coating for Metal Fabricators & Welding Shops",
		"nav_label": "Metal Fabricators & Welding Shops",
		"keyword": "powder coating for metal fabricators",
		"seo_title": "Powder Coating for Metal Fabricators & Welding Shops | Koojo",
		"summary": "A finishing partner for fabricators: weldments and fabricated steel blasted, coated and ready to ship.",
		"body": [
			"Powder coating for metal fabricators means a finishing partner that can take a weldment straight off your floor and return it coated, on the date you promised your customer. Koojo has coated fabricated steel for shops across the GTA since 2012.",
			"## What fabricators send us",
			"Frames, guards, brackets, racks, railings and structural weldments, from single pieces to full production releases. Hot-rolled material with mill scale is blasted before coating.",
			"## Turnaround",
			"Finishing is the last step before your part ships, so delays land on you. Tell us your ship date when you request a quote and we will confirm whether we can meet it before you commit.",
			"## Getting weldments ready",
			"Coating shows what is underneath. Grind spatter, seal or vent closed sections and drill drain holes so pretreatment can escape. We will flag anything we spot at receiving.",
		],
		"faqs": [
			("Can you coat our parts and ship directly to our customer?", "Yes. We can package finished parts and arrange delivery, or hold them for your carrier."),
			("Do you blast hot-rolled steel before coating?", "Yes. Mill scale is removed by blasting so the coating bonds to the steel."),
			("Will weld spatter show through powder coating?", "Yes. Powder follows the surface, so spatter and rough welds remain visible. Clean them up before sending parts."),
		],
		"services": ["industrial-powder-coating", "sandblasting", "bulk-commercial-orders"],
		"project": "conveyor-frame-automotive-plant",
	},
	{
		"slug": "manufacturing-automation",
		"title": "Powder Coating for Manufacturers & Automation Builders",
		"nav_label": "Manufacturing & Automation",
		"keyword": "powder coating for manufacturers",
		"seo_title": "Powder Coating for Manufacturers & Automation | Koojo",
		"summary": "OEM coating for conveyor frames, robotic bases and machine guards, with consistent colour across every build.",
		"body": [
			"Powder coating for manufacturers gives OEMs and automation builders a repeatable finish on the frames and guards that make up their machines. We coat conveyor frames, robotic bases and machine guards to your colour standard, build after build.",
			"## What we coat for equipment builders",
			["Conveyor and automation line frames", "Robot bases and pedestals", "Machine guards, doors and panels", "Brackets, mounts and operator stations"],
			"## Matching your machine colours",
			"Most builders have a standard frame colour and a safety colour for guards. Give us the RAL numbers once and we keep them on file for every order.",
			"## Large frames",
			"Automation frames are often long and heavy. Our line takes parts up to 6,000 lb in a 23 ft oven: details are on our [capabilities](/capabilities) page.",
		],
		"faqs": [
			("Can you coat machine frames after machining?", "Yes. Machined pads, tapped holes and datum faces are masked so they stay bare and to size."),
			("Can you keep safety yellow guards consistent between orders?", "Yes. We record the powder used and reuse it on repeat orders."),
			("Can you work to our build schedule?", "Share your build dates and we will schedule coating around them."),
		],
		"services": ["industrial-powder-coating", "bulk-commercial-orders", "surface-preparation"],
		"project": "robotic-base",
	},
	{
		"slug": "machine-shops",
		"title": "Powder Coating for Machine Shops",
		"nav_label": "Machine Shops",
		"keyword": "powder coating for machine shops",
		"seo_title": "Powder Coating for Machine Shops | Koojo",
		"summary": "Precision masking of threads, bores and machined faces, and careful handling of small-part batches.",
		"body": [
			"Powder coating for machine shops is mostly about what does not get coated. Threads, bores and precision faces have to stay bare and to size, so the work depends on accurate masking and careful handling of small-part batches.",
			"## Masking to your drawing",
			"Send a drawing or marked-up photo showing which features stay bare. We mask threaded holes with plugs and faces with high-temperature tape, and remove everything after cure.",
			"## Small-part batches",
			"Small parts are racked so each piece is fully covered and hang marks land where you want them. Tell us where a contact point is acceptable.",
			"## Film thickness and fit",
			"Powder adds measurable thickness. If coated surfaces need to mate or slide, flag it so we can mask them or you can allow for the film in your tolerances.",
		],
		"faqs": [
			("Can you keep powder out of tapped holes?", "Yes. Tapped holes are plugged before coating."),
			("How much thickness does powder coating add?", "It depends on the powder and application. Tell us about any fit-critical surfaces so we can mask them."),
			("Do you take small batch quantities?", "Yes. Small batches and prototype quantities are welcome."),
		],
		"services": ["surface-preparation", "bulk-commercial-orders", "specialty-custom-projects"],
		"project": "robotic-base",
	},
	{
		"slug": "contractors-construction",
		"title": "Powder Coating for Contractors & Construction",
		"nav_label": "Contractors & Construction",
		"keyword": "powder coating for contractors",
		"seo_title": "Powder Coating for Contractors & Construction | Koojo",
		"summary": "Coated railings, structural pieces and site metalwork for steel erectors and railing installers, packaged for site delivery.",
		"body": [
			"Powder coating for contractors covers the railings, stairs, posts and miscellaneous metals that go into a building. We coat for steel erectors and railing installers and package the work so it reaches site without damage.",
			"## What we coat for construction projects",
			["Railings, guards and stair components", "Posts, bollards and gates", "Lintels, brackets and miscellaneous metals", "Canopy and screen framing"],
			"## Delivery to site",
			"Finished sections are wrapped and packed for transport. Tell us how the load will be handled on site and we will pack to suit.",
			"## Meeting the spec",
			"If the project specification names a colour, gloss or performance level, send it with your quote request. See [architectural powder coating](/services/architectural-coatings) for exterior finish levels.",
		],
		"faqs": [
			("Can you coat long railing sections?", "Yes. Our oven is 23 ft long. Send section lengths with your quote request."),
			("What colour information do you need from the spec?", "A RAL number or manufacturer colour reference, the gloss level, and any performance standard called out."),
			("How are finished railings protected for transport?", "They are wrapped and packed to prevent rubbing. Tell us your handling method so we can pack accordingly."),
		],
		"services": ["architectural-coatings", "sandblasting", "industrial-powder-coating"],
		"project": "safety-bollards",
	},
	{
		"slug": "food-processing-equipment",
		"title": "Powder Coating for Food Processing Equipment",
		"nav_label": "Food Processing Equipment",
		"keyword": "powder coating for food processing equipment",
		"seo_title": "Powder Coating for Food Processing Equipment | Koojo",
		"summary": "Washdown-resistant finishes for line frames and supports in food and beverage plants.",
		"body": [
			"Powder coating for food processing equipment protects the frames and supports around a production line from frequent washdowns and cleaning chemicals. We coat line frames, stands, guards and platforms for food and beverage plants.",
			"## Where powder coating is used in a food plant",
			"Powder is used on structural and non-contact parts: frames, legs, guards, platforms and enclosures. Surfaces that touch food are normally stainless steel.",
			"## Standing up to washdown",
			"A continuous, well-cured film over properly pretreated steel resists moisture and cleaning chemicals. Good design helps too: sealed welds and drain holes prevent water sitting inside tube.",
			"## Compliance requirements",
			"If your customer or auditor requires a powder formulated to a specific food-contact standard, tell us at the quote stage so the right product is specified and documented.",
		],
		"faqs": [
			("Can powder-coated frames be pressure washed?", "Yes. Cured powder tolerates routine washdown. Avoid holding a high-pressure jet on edges and damaged areas."),
			("Do you provide documentation for the powder used?", "Yes. Product data sheets for the powder can be supplied on request."),
			("Should food-contact surfaces be powder coated?", "Food-contact surfaces are usually stainless steel. Powder is best for frames and non-contact structure."),
		],
		"services": ["industrial-powder-coating", "surface-preparation", "bulk-commercial-orders"],
		"project": "food-processing-line-frame",
	},
	{
		"slug": "agricultural-heavy-equipment",
		"title": "Agricultural Equipment Powder Coating",
		"nav_label": "Agricultural & Heavy Equipment",
		"keyword": "agricultural equipment powder coating",
		"seo_title": "Agricultural Equipment Powder Coating | Koojo",
		"summary": "Rust protection for implements, trailers and attachments that live outdoors and work in dirt.",
		"body": [
			"Agricultural equipment powder coating protects implements, trailers and attachments from the rust that comes with outdoor storage, fertilizer and soil. We blast worn equipment back to clean steel and apply a heavy-duty finish.",
			"## What we coat",
			["Implements and attachments", "Trailers and trailer frames", "Loader buckets, forks and hitches", "Gates, panels and handling equipment"],
			"## Refinishing used equipment",
			"Most farm equipment arrives with old paint and surface rust. Blasting removes both so the new coating bonds to sound metal.",
			"## Size and weight",
			"Heavy pieces are routine. Our line handles parts up to 6,000 lb: see [capabilities](/capabilities).",
		],
		"faqs": [
			("Can you powder coat a trailer frame?", "Yes, provided it fits our 23 ft oven and 6,000 lb limit. Wiring, lights, tires and wood decking must be removed."),
			("Do you coat used equipment with existing rust?", "Yes. Rust and old paint are blasted off first."),
			("Can you match manufacturer equipment colours?", "We match to the closest available powder. Bring a colour code or sample."),
		],
		"services": ["industrial-powder-coating", "sandblasting", "restoration-recoating"],
		"project": "conveyor-frame-automotive-plant",
	},
	{
		"slug": "municipal-institutional",
		"title": "Powder Coating for Municipalities & Institutions",
		"nav_label": "Municipal & Institutional",
		"keyword": "powder coating for municipalities",
		"seo_title": "Powder Coating for Municipalities & Institutions | Koojo",
		"summary": "Durable finishes for bollards, park equipment and school and church metalwork.",
		"body": [
			"Powder coating for municipalities and institutions keeps public metalwork presentable for longer between maintenance cycles. We coat bollards, park equipment and the gates, railings and fixtures of schools and churches.",
			"## What we coat",
			["Safety and traffic bollards", "Park benches, bike racks and site furniture", "Gates, fences and railings", "School, church and community-building metalwork"],
			"## New work and refurbishment",
			"We coat new fabrications for your contractor and refurbish existing assets by stripping and recoating them.",
			"## Colours and visibility",
			"Safety yellow is standard for bollards, and heritage or brand colours can be matched for gates and architectural pieces.",
		],
		"faqs": [
			("Can existing bollards be refinished?", "Yes. Removable bollards can be stripped and recoated."),
			("Do you provide certification documents for tenders?", "Yes. Certification and compliance documents are available on request."),
			("Can you match a heritage colour on church gates?", "Yes. Bring a sample or colour reference and we will match it as closely as available powders allow."),
		],
		"services": ["architectural-coatings", "custom-colors-finishes", "restoration-recoating"],
		"project": "safety-bollards",
	},
]

# ---------------------------------------------------------------------------
# Locations (/locations/powder-coating-<city>) -- local intent.
# Wave 2 pages stay in draft until there is real local work to show.
# drive_time and pickup_details are left for Koojo to fill in.
# ---------------------------------------------------------------------------

LOCATION_SERVICES = ["industrial-powder-coating", "sandblasting", "custom-colors-finishes"]

LOCATIONS = [
	{
		"city": "Milton",
		"wave": 1,
		"region": "Halton Region",
		"summary": "Our shop and head office at 10874 Steeles Ave E. Drop parts off and pick them up Monday to Friday, 7 AM to 5 PM.",
		"body": [
			"Powder coating in Milton is done at our own shop at 10874 Steeles Ave E, where Koojo has operated since 2012. Milton customers can drop parts off, speak to the people coating them and pick up finished work without arranging shipping.",
			"## Visiting the shop",
			"We are open Monday to Friday, 7 AM to 5 PM. Call (905) 876-7060 before bringing large or heavy pieces so we can have the right equipment ready to unload.",
			"## What Milton customers bring us",
			"Local fabricators and manufacturers send frames, guards and production parts, and residents bring wheels, railings and furniture.",
		],
		"faqs": [
			("Where is Koojo located in Milton?", "10874 Steeles Ave E, Milton, ON L9T 2X8."),
			("Can I drop parts off without an appointment?", "Yes during business hours, but call ahead for large or heavy items."),
		],
	},
	{
		"city": "Oakville",
		"wave": 1,
		"region": "Halton Region",
		"summary": "Powder coating for Oakville manufacturers, fabricators and homeowners from our Milton shop next door.",
		"body": [
			"Powder coating for Oakville is handled at our Milton shop, the next municipality north in Halton Region. Oakville businesses and residents can drop parts off or ask us about pickup and delivery.",
			"## Getting parts to us from Oakville",
			"Bring parts to 10874 Steeles Ave E in Milton during business hours, or ask about pickup when you request a quote.",
		],
		"faqs": [
			("Do you pick up parts from Oakville?", "Ask when you request a quote. Pickup and delivery depend on the size of the load and our schedule."),
			("Do you have a shop in Oakville?", "No. All coating is done at our Milton facility."),
		],
	},
	{
		"city": "Burlington",
		"wave": 1,
		"region": "Halton Region",
		"summary": "Powder coating for Burlington fabricators and manufacturers, coated at our Milton facility.",
		"body": [
			"Powder coating for Burlington customers is done at our Milton facility in Halton Region. We coat for Burlington fabricators and equipment builders as well as individual customers.",
			"## Getting parts to us from Burlington",
			"Drop parts at 10874 Steeles Ave E in Milton, Monday to Friday, 7 AM to 5 PM, or ask about pickup and delivery with your quote.",
		],
		"faqs": [
			("Do you serve Burlington businesses?", "Yes. Burlington is within our regular service area."),
			("Can finished parts be delivered to Burlington?", "Delivery can be arranged. Ask when you request a quote."),
		],
	},
	{
		"city": "Mississauga",
		"wave": 1,
		"region": "Peel Region",
		"summary": "Industrial powder coating for Mississauga and Peel Region manufacturers from our Milton shop.",
		"body": [
			"Powder coating for Mississauga is done at our Milton shop, just west of Peel Region. We work with Mississauga manufacturers and fabricators that need large or heavy parts coated.",
			"## Getting parts to us from Mississauga",
			"Our shop is at 10874 Steeles Ave E in Milton. Drop off during business hours or ask about pickup and delivery for production loads.",
		],
		"faqs": [
			("Do you coat production parts for Mississauga manufacturers?", "Yes. We handle recurring production work as well as one-off parts."),
			("How do I get a large frame from Mississauga to your shop?", "Send dimensions and weight with your quote request and we will help plan transport."),
		],
	},
	{
		"city": "Halton Hills",
		"wave": 1,
		"region": "Halton Region",
		"summary": "Powder coating for Georgetown and Acton, from our shop on Steeles Ave E in Milton.",
		"body": [
			"Powder coating for Halton Hills, including Georgetown and Acton, is done at our Milton shop on Steeles Ave E. We coat for local shops, farms and residents.",
			"## Getting parts to us from Georgetown and Acton",
			"Drop parts at 10874 Steeles Ave E in Milton, Monday to Friday, 7 AM to 5 PM, or ask about pickup with your quote.",
		],
		"faqs": [
			("Do you serve Georgetown and Acton?", "Yes. Both are part of our Halton Hills service area."),
			("Do you coat farm equipment from Halton Hills?", "Yes. Implements, trailers and attachments are regular work for us."),
		],
	},
	{
		"city": "Brampton",
		"wave": 2,
		"region": "Peel Region",
		"summary": "Powder coating for Brampton industrial parts, from our Milton shop.",
		"body": [],
		"faqs": [],
	},
	{
		"city": "Guelph",
		"wave": 2,
		"region": "Wellington County",
		"summary": "Powder coating for Guelph manufacturers, with delivery to Guelph.",
		"body": [],
		"faqs": [],
	},
	{
		"city": "Cambridge",
		"wave": 2,
		"region": "Waterloo Region",
		"summary": "Powder coating for Cambridge fabricators and Waterloo Region manufacturers.",
		"body": [],
		"faqs": [],
	},
	{
		"city": "Hamilton",
		"wave": 2,
		"region": "Hamilton",
		"summary": "Powder coating for Hamilton and Stoney Creek steel fabricators.",
		"body": [],
		"faqs": [],
	},
]

# ---------------------------------------------------------------------------
# Projects (/projects/<slug>) -- case studies. Photos are from the live gallery.
# Spec fields (metal, size, powder, colour code, turnaround) need Koojo's input.
# ---------------------------------------------------------------------------

PROJECTS = [
	{
		"slug": "conveyor-frame-automotive-plant",
		"title": "Conveyor Frame for an Automotive Plant",
		"keyword": "automotive plant conveyor frame case study",
		"category": "industrial",
		"client_industry": "Automotive manufacturing",
		"part": "Conveyor system frame",
		"summary": "A large conveyor frame coated for use on an automotive plant floor.",
		"image": img("06611b_078421f0799e4d188bfbc7f808731b30~mv2.jpg", "Powder-coated conveyor frame for an automotive plant", "conveyor-frame-automotive-plant.jpg"),
		"service": "industrial-powder-coating",
		"industry": "manufacturing-automation",
	},
	{
		"slug": "automation-line-frame",
		"title": "Automation Line Frame",
		"keyword": "automation line frame case study",
		"category": "industrial",
		"client_industry": "Automation equipment",
		"part": "Machine frame for an automation line",
		"summary": "A machine frame coated for an automation line builder.",
		"image": img("06611b_a22f33221688494e868af4307acfcf83~mv2.jpg", "Powder-coated frame for an automation line", "automation-line-frame.jpg"),
		"service": "industrial-powder-coating",
		"industry": "manufacturing-automation",
	},
	{
		"slug": "food-processing-line-frame",
		"title": "Food Processing Line Frame",
		"keyword": "food processing line frame case study",
		"category": "industrial",
		"client_industry": "Food processing",
		"part": "Frame for a food processing line",
		"summary": "A line frame coated for a food plant, where equipment is washed down regularly.",
		"image": img("b95a8d_e55f8b4a316a47979eb84f3a5ffdec05~mv2.jpeg", "Powder-coated frame for a food processing line", "food-processing-line-frame.jpg"),
		"service": "industrial-powder-coating",
		"industry": "food-processing-equipment",
	},
	{
		"slug": "robotic-base",
		"title": "Robotic Base",
		"keyword": "robotic base case study",
		"category": "industrial",
		"client_industry": "Manufacturing",
		"part": "Robot base / pedestal",
		"summary": "A heavy fabricated robot base coated for a manufacturing cell.",
		"image": img("b95a8d_be36a24ff84142a8a0574bc947f5d72a~mv2.jpeg", "Powder-coated robotic base", "robotic-base.jpg"),
		"service": "industrial-powder-coating",
		"industry": "manufacturing-automation",
	},
	{
		"slug": "safety-bollards",
		"title": "Safety Bollards",
		"keyword": "bollard powder coating case study",
		"category": "architectural",
		"client_industry": "Site protection",
		"part": "Steel safety bollards",
		"summary": "Steel bollards coated for site protection.",
		"image": img("06611b_31c9316daba54b529caa75c12a16270a~mv2.jpg", "Powder-coated safety bollards", "safety-bollards.jpg"),
		"service": "architectural-coatings",
		"industry": "municipal-institutional",
	},
	{
		"slug": "church-gates",
		"title": "Church Gates",
		"keyword": "church gates case study",
		"category": "architectural",
		"client_industry": "Religious institution",
		"part": "Decorative steel gates",
		"summary": "Decorative gates for a church, coated and wrapped for delivery.",
		"image": img("06611b_41f710f03836413b99799c330ce5c057~mv2.jpg", "Powder-coated gates for a church, wrapped for delivery", "church-gates.jpg"),
		"service": "architectural-coatings",
		"industry": "municipal-institutional",
	},
]

PROJECT_CATEGORIES = [
	("industrial", "Industrial"),
	("automotive", "Automotive"),
	("architectural", "Architectural"),
	("specialty", "Specialty"),
]

# ---------------------------------------------------------------------------
# Blog
# ---------------------------------------------------------------------------

# (slug, label, primary keyword, description shown on the category hub)
BLOG_CATEGORIES = [
	("basics-process", "Basics & Process", "powder coating basics", "Powder coating basics start here. These guides explain what powder coating is, how the process works from pretreatment through cure, and what it can and cannot do. They are written for buyers, engineers and owners who are new to the finish and want plain answers before specifying it. You will find a step-by-step walk through the process, the benefits compared with other finishes, the myths we hear most often, how the process affects the environment, and how small parts are handled differently from large fabrications. Start with the definition if powder coating is new to you, then follow the links into the rest of the guides for materials, finishes, standards and cost."),
	("materials-substrates", "Materials & Substrates", "powder coating materials guide", "This powder coating materials guide covers the two things every job starts with: the metal being coated and the powder going onto it. Different substrates behave differently in pretreatment and in the oven, and each powder chemistry has its own strengths. These articles explain which metals can be powder coated, how steel, aluminum, stainless and cast parts are prepared, and how epoxy, polyester and hybrid powders compare for corrosion protection and UV resistance. Use them when you are deciding whether a part is a good candidate for powder coating or choosing a powder for a particular environment."),
	("finishes-colours", "Finishes & Colours", "powder coating finishes guide", "Our powder coating finishes guide explains how colour, gloss and texture are specified and what to expect from each option. Colour is usually communicated with a RAL number, but gloss level and texture change how a part looks and wears just as much. These articles cover RAL colour matching and custom colour requests, and how matte, gloss, textured and metallic finishes differ in appearance, durability and maintenance. Read them before you choose a finish for a product line, a building or a restoration, so that what you ask for is what comes out of the oven."),
	("standards-quality", "Standards, Testing & Quality", "powder coating standards and testing", "Powder coating standards and testing define how a finish is specified, measured and verified. This section explains the documents and tests you will see on drawings and in supplier requirements: ASTM test methods for adhesion, impact and film thickness, ISO quality systems, surface preparation standards, salt spray testing and corrosion ratings. It also covers how film thickness is specified in mils and how it is measured, and what a quality control inspection looks like on each batch. Use these guides to write a clearer specification or to understand a test report from your coater."),
	("comparisons", "Comparisons", "powder coating comparisons", "These powder coating comparisons set the finish side by side with the alternatives buyers most often consider: wet paint, galvanizing and anodizing. Each process protects metal in a different way, at a different cost, and with a different look. The articles compare durability, corrosion protection, appearance, environmental impact and price, and explain when two processes are combined, such as powder coating over galvanized steel. Read them when you are choosing a finish for a new product or questioning whether the finish on an existing specification is still the right one."),
	("applications", "Applications", "powder coating applications", "Powder coating applications cover the parts and products we see most often and what each one needs from its finish. A farm implement, a conveyor frame, a church gate and a patio chair all get powder coated, but they face different conditions and are prepared and specified differently. These guides go through automotive parts, industrial machinery, agricultural equipment, railings and bollards, fences and gates, conveyor and automation frames, robot bases, food-processing equipment, HVAC ductwork, playground equipment and outdoor furniture. Find the article closest to your part to see the preparation, powder choice and common mistakes for that application."),
	("cost-planning", "Cost & Planning", "powder coating cost and planning", "Powder coating cost and planning guides help you budget a job and get parts ready for it. Price depends on the size and number of parts, the preparation they need, the finish chosen and how they are racked and cured, so understanding those factors makes a quote easier to read. This section explains what drives cost, how to prepare parts before dropping them off so no time is lost at receiving, and which questions to ask a coater before you place an order. Read them before requesting a quote and you will get a faster, more accurate answer."),
]

# slug -> blog category, in blueprint order.
POST_CATEGORIES = {
	"what-is-powder-coating": "basics-process",
	"why-powder-coating-is-ideal": "basics-process",
	"powder-coating-process-step-by-step": "basics-process",
	"powder-coating-myths-debunked": "basics-process",
	"is-powder-coating-eco-friendly": "basics-process",
	"powder-coating-small-parts-vs-large-fabrications": "basics-process",
	"what-metals-can-be-powder-coated-substrate-guide": "materials-substrates",
	"epoxy-vs-polyester-vs-hybrid-powder-coatings-which-to-choose": "materials-substrates",
	"powder-coating-color-matching-ral": "finishes-colours",
	"metallic-finishes-explained-powder-coating": "finishes-colours",
	"powder-coating-thickness-mil-rating-guide": "standards-quality",
	"how-powder-coating-thickness-is-measured-and-why-it-matters": "standards-quality",
	"salt-spray-testing-explained-how-corrosion-resistance-is-measured": "standards-quality",
	"corrosion-resistance-ratings-coated-metal-parts": "standards-quality",
	"astm-standards-for-powder-coating": "standards-quality",
	"iso-certification-in-powder-coating-what-it-means-for-quality": "standards-quality",
	"surface-preparation-standards-powder-coating": "standards-quality",
	"powder-coating-quality-control-batch-inspection": "standards-quality",
	"powder-coating-vs-wet-paint-toronto": "comparisons",
	"powder-coating-vs-galvanizing-corrosion-protection": "comparisons",
	"powder-coating-vs-anodizing-metal-finish-guide": "comparisons",
	"blog-powder-coating-for-automotive-parts": "applications",
	"blog-industrial-machinery-powder-coating": "applications",
	"powder-coating-agricultural-equipment": "applications",
	"powder-coating-for-architectural-railings-bollards": "applications",
	"blog-powder-coating-for-fences-and-gates": "applications",
	"powder-coating-for-conveyor-systems-automation-frames": "applications",
	"powder-coating-robotics-bases-manufacturing-equipment": "applications",
	"food-safe-powder-coating-standards": "applications",
	"hvac-and-ductwork-powder-coating": "applications",
	"powder-coating-playground-park-equipment": "applications",
	"powder-coating-church-gates-religious-metalwork": "applications",
	"powder-coating-outdoor-furniture-weatherproof-finishes": "applications",
}

# Primary keyword each existing post owns (blueprint 3.8).
POST_KEYWORDS = {
	"what-is-powder-coating": "what is powder coating",
	"why-powder-coating-is-ideal": "benefits of powder coating",
	"powder-coating-process-step-by-step": "powder coating process",
	"powder-coating-myths-debunked": "powder coating myths",
	"is-powder-coating-eco-friendly": "is powder coating eco-friendly",
	"powder-coating-small-parts-vs-large-fabrications": "powder coating small parts vs large fabrications",
	"what-metals-can-be-powder-coated-substrate-guide": "what metals can be powder coated",
	"epoxy-vs-polyester-vs-hybrid-powder-coatings-which-to-choose": "epoxy vs polyester powder coating",
	"powder-coating-color-matching-ral": "powder coating RAL colour matching",
	"metallic-finishes-explained-powder-coating": "metallic powder coating finishes",
	"powder-coating-thickness-mil-rating-guide": "powder coating thickness (mils)",
	"how-powder-coating-thickness-is-measured-and-why-it-matters": "how to measure powder coating thickness",
	"salt-spray-testing-explained-how-corrosion-resistance-is-measured": "salt spray test",
	"corrosion-resistance-ratings-coated-metal-parts": "ISO 12944 corrosivity categories",
	"astm-standards-for-powder-coating": "ASTM standards for powder coating",
	"iso-certification-in-powder-coating-what-it-means-for-quality": "ISO certification in powder coating",
	"surface-preparation-standards-powder-coating": "surface preparation standards (SSPC / ISO 8501)",
	"powder-coating-quality-control-batch-inspection": "powder coating quality control",
	"powder-coating-vs-wet-paint-toronto": "powder coating vs wet paint",
	"powder-coating-vs-galvanizing-corrosion-protection": "powder coating vs galvanizing",
	"powder-coating-vs-anodizing-metal-finish-guide": "powder coating vs anodizing",
	"blog-powder-coating-for-automotive-parts": "which car parts can be powder coated",
	"blog-industrial-machinery-powder-coating": "how to protect industrial machinery from corrosion",
	"powder-coating-agricultural-equipment": "how to stop rust on farm equipment",
	"powder-coating-for-architectural-railings-bollards": "powder coating railings and bollards",
	"blog-powder-coating-for-fences-and-gates": "powder coating fences and gates",
	"powder-coating-for-conveyor-systems-automation-frames": "conveyor frame powder coating",
	"powder-coating-robotics-bases-manufacturing-equipment": "robot base powder coating",
	"food-safe-powder-coating-standards": "food safe powder coating",
	"hvac-and-ductwork-powder-coating": "HVAC ductwork powder coating",
	"powder-coating-playground-park-equipment": "playground equipment powder coating",
	"powder-coating-church-gates-religious-metalwork": "church gate powder coating",
	"powder-coating-outdoor-furniture-weatherproof-finishes": "powder coating outdoor furniture",
}

# These keep their URL and migrated copy; the new title/H1/intro is an editorial task.
RETARGET_POSTS = [
	"why-powder-coating-is-ideal",
	"how-powder-coating-thickness-is-measured-and-why-it-matters",
	"corrosion-resistance-ratings-coated-metal-parts",
	"blog-powder-coating-for-automotive-parts",
	"blog-industrial-machinery-powder-coating",
	"powder-coating-agricultural-equipment",
	"powder-coating-for-architectural-railings-bollards",
]

# New gap-topic posts (blueprint 3.9), seeded as drafts: (slug, title, keyword, category).
NEW_POSTS = [
	("how-much-does-powder-coating-cost-ontario", "How Much Does Powder Coating Cost in Ontario?", "powder coating cost Ontario", "cost-planning"),
	("how-long-does-powder-coating-last", "How Long Does Powder Coating Last?", "how long does powder coating last", "basics-process"),
	("how-to-prepare-parts-for-powder-coating", "How to Prepare Parts Before Drop-Off", "how to prepare parts for powder coating", "cost-planning"),
	("can-you-powder-coat-aluminum", "Can You Powder Coat Aluminum?", "can you powder coat aluminum", "materials-substrates"),
	("powder-coating-galvanized-steel", "Powder Coating Galvanized Steel (Outgassing)", "powder coating galvanized steel", "materials-substrates"),
	("can-you-powder-coat-over-paint", "Can You Powder Coat Over Paint or Rust?", "can you powder coat over paint", "basics-process"),
	("aama-2603-vs-2604-vs-2605", "AAMA 2603 vs 2604 vs 2605", "AAMA 2603 vs 2604 vs 2605", "standards-quality"),
	("questions-to-ask-a-powder-coater", "Questions to Ask a Powder Coater", "questions to ask a powder coating company", "cost-planning"),
]

# ---------------------------------------------------------------------------
# Core pages and hubs (pages collection)
# ---------------------------------------------------------------------------

HOME_BLOCKS = [
	{
		"_type": "marketing_hero",
		"_key": "hero",
		"headline": "Powder Coating Company Serving the GTA",
		"subheadline": "Koojo Custom Powder Coating has delivered industrial-grade, long-lasting finishes for metal products from our Milton shop since 2012.",
		"primary_cta_label": "Get a Quote",
		"primary_cta_url": "/get-a-quote",
		"secondary_cta_label": "Call (905) 876-7060",
		"secondary_cta_url": "tel:+19058767060",
		"image": img("b95a8d_66e92e461ea2474ca9261e5782dd27a2~mv2.jpeg", "Freshly coated posts hanging on the line at our Milton shop", "koojo-coated-posts-on-the-line.jpg", width=2400),
	},
	{
		"_type": "site_stats",
		"_key": "stats",
		"items": [
			{"value": "12+", "label": "Years of experience"},
			{"value": "48 hr", "label": "Project turnaround time"},
			{"value": "10,000+", "label": "Items coated"},
			{"value": "6,000 lb", "label": "Part weight capacity"},
		],
	},
	{
		"_type": "site_cards",
		"_key": "services",
		"source": "services",
		"headline": "Ten services, one shop",
		"subheadline": "From heavy industrial frames to a single set of rims.",
		"link_label": "All services",
		"link_url": "/services",
	},
	{
		"_type": "site_cards",
		"_key": "work",
		"source": "projects",
		"headline": "We create standards that last",
		"subheadline": "Recent work from our shop floor.",
		"link_label": "See our work",
		"link_url": "/projects",
	},
	{
		"_type": "site_steps",
		"_key": "process",
		"headline": "How a job runs through the shop",
		"subheadline": "The same sequence on every part, whether it is one bracket or a production run.",
		"steps": [
			{"title": "Quote", "description": "Send photos, sizes, quantity and the colour you want. We confirm price and timing."},
			{"title": "Drop-off", "description": "Bring parts to Steeles Ave E in Milton, or ask about pickup for larger loads."},
			{
				"title": "Clean and pretreat",
				"description": "Degreasing, chemical cleaning and phosphating, then rinse and dry. Rusted or scaled steel is blasted first.",
			},
			{"title": "Mask and inspect", "description": "Threads, bores and mating faces are plugged or taped, and the surface is checked before coating."},
			{"title": "Coat and cure", "description": "Powder is sprayed electrostatically and cured in our 23 ft oven."},
			{"title": "Pack and ship", "description": "Finished parts are inspected, wrapped and held for pickup or delivery."},
		],
	},
	{
		"_type": "site_swatches",
		"_key": "colour",
		"headline": "Any RAL colour, in the finish you need",
		"text": "Give us a RAL number or a sample part. Matte, gloss, textured and metallic finishes are all available.",
		"link_label": "Colours and finishes",
		"link_url": "/services/custom-colors-finishes",
		"swatches": [
			{"code": "RAL 9005", "name": "Jet black", "hex": "#0a0a0d"},
			{"code": "RAL 7016", "name": "Anthracite grey", "hex": "#383e42"},
			{"code": "RAL 9006", "name": "White aluminium", "hex": "#a5a8a6"},
			{"code": "RAL 9016", "name": "Traffic white", "hex": "#f1f0ea"},
			{"code": "RAL 1023", "name": "Traffic yellow", "hex": "#f7b500"},
			{"code": "RAL 2004", "name": "Pure orange", "hex": "#e25303"},
			{"code": "RAL 3020", "name": "Traffic red", "hex": "#c1121c"},
			{"code": "RAL 5010", "name": "Gentian blue", "hex": "#004f7c"},
		],
	},
	{
		"_type": "marketing_features",
		"_key": "why",
		"headline": "Why choose us?",
		"features": [
			{"icon": "shield", "title": "Durability", "description": "Finishes that resist chipping, scratching, fading, rust and corrosion."},
			{"icon": "star", "title": "Customization", "description": "RAL colour matching in matte, gloss, textured and metallic finishes."},
			{"icon": "clock", "title": "Fast turnaround", "description": "Work is scheduled around the date you need it back."},
			{"icon": "globe", "title": "Local presence", "description": "One shop in Milton, Ontario, serving the Greater Toronto Area."},
			{
				"icon": "check",
				"title": "Certified quality assurance",
				"description": "Certified by the Absolute Bureau of Certification, with test reports on request.",
			},
			{"icon": "chart", "title": "Built for large parts", "description": "A 23 ft oven and a line rated for parts up to 6,000 lb."},
		],
	},
	{
		"_type": "site_cards",
		"_key": "industries",
		"source": "industries",
		"headline": "Who we coat for",
		"link_label": "All industries",
		"link_url": "/industries",
	},
	{
		"_type": "marketing_testimonials",
		"_key": "reviews",
		"headline": "What customers say on Google",
		"testimonials": [
			{
				"quote": "I have been using Koojo custom powder coating for a few years now and i wouldn't even think to go somewhere else. The work is finished in a timely manner and the quality is excellent.",
				"author": "Richard Hartlin",
				"role": "via Google",
			},
			{
				"quote": "Had a 70's cruiser bike frame painted. Job turned out great and looks better than new! Would not hestitate to return!",
				"author": "Philip. S",
				"role": "via Google",
			},
			{"quote": "My rims look amazing and I would definitely recommend his service .", "author": "Brendan Black", "role": "via Google"},
		],
	},
	{
		"_type": "site_cards",
		"_key": "locations",
		"source": "locations",
		"headline": "Where we work",
		"subheadline": "Drop off in Milton, or ask about pickup and delivery.",
		"link_label": "All service areas",
		"link_url": "/locations",
	},
	{
		"_type": "site_cta",
		"_key": "cta",
		"headline": "Ready to get your parts coated?",
		"text": "Tell us what you have and when you need it back.",
		"button_label": "Get a Quote",
		"button_url": "/get-a-quote",
	},
]

PAGES = [
	{
		"slug": "home",
		"title": "Home",
		"keyword": "powder coating company GTA",
		"seo_title": "Powder Coating Company GTA | Koojo Custom Powder Coating",
		"seo_description": "Koojo Custom Powder Coating is a powder coating company serving the GTA from Milton, Ontario. Industrial-grade finishes since 2012. 23 ft oven, 6,000 lb capacity.",
		"blocks": HOME_BLOCKS,
	},
	{
		"slug": "about-us",
		"title": "About Koojo Custom Powder Coating",
		"keyword": "about Koojo Custom Powder Coating",
		"seo_title": "About Koojo Custom Powder Coating",
		"intro": "A certified powder coating shop that has been finishing metal products since 2012.",
		"body": [
			"## Our mission",
			"At Koojo Custom Powder Coating, our mission is to combine durability, beauty, and precision in every project we undertake. We aim to provide exceptional powder coating solutions that protect and enhance metal products while delivering outstanding customer experiences.",
			"We believe every project deserves the highest level of care and attention to detail, whether it's a single piece or a large-scale order.",
			"## Our experience",
			"With over 12 years of experience and more than 10,000 items coated, Koojo has established itself as a trusted name in the powder coating industry. From small, personalized projects to large-scale industrial orders, we've seen it all, and we deliver results that last.",
			"As a certified powder coating provider, we adhere to industry standards to ensure top-notch quality and durability. Read about our [powder coating quality assurance](/certification).",
			"## Our commitment",
			["Quality first: we use the best materials and techniques to ensure every finish is flawless and durable.", "Customer focus: we work closely with you to bring your vision to life.", "Sustainability matters: our powder coating process is eco-friendly, minimizing waste and reducing environmental impact.", "Certified powder coaters: certifications and compliance documentation are available upon request."],
		],
		"blocks": [next(b for b in HOME_BLOCKS if b["_type"] == "marketing_testimonials") | {"_key": "about-reviews", "headline": "Google testimonials"}],
	},
	{
		"slug": "contact-us",
		"title": "Contact Koojo Powder Coating",
		"keyword": "contact Koojo powder coating",
		"seo_title": "Contact Koojo Powder Coating | Milton, ON",
		"intro": "Call, email or visit the shop. Drop-off and pickup are available during business hours.",
		"body": [
			"## Drop-off and pickup",
			"Parts can be dropped off and picked up at our Milton shop Monday to Friday, 7 AM to 5 PM. Please call ahead for large or heavy items so we can be ready to unload them.",
		],
	},
	{
		"slug": "get-a-quote",
		"title": "Get a Powder Coating Quote",
		"keyword": "powder coating quote",
		"seo_title": "Powder Coating Quote | Koojo Custom Powder Coating",
		"intro": "Tell us about your parts and we'll get back to you shortly with an estimate.",
		"body": [
			"## What to send us",
			["What the part is and what metal it is made from", "Dimensions and approximate weight of the largest piece", "Quantity", "Colour and finish, with a RAL number if you have one", "Photos of the parts in their current condition", "When you need them back"],
			"Projects are not guaranteed to start and finish by the requested dates. We will confirm timing with your quote.",
		],
	},
	{
		"slug": "capabilities",
		"title": "Large Part Powder Coating Capabilities",
		"keyword": "large part powder coating",
		"seo_title": "Large Part Powder Coating | Capabilities | Koojo",
		"intro": "Our facility is built to handle projects of all sizes, from small custom pieces to oversized, heavy fabrications that many coaters can't take.",
		"body": [
			"## What we can handle",
			["23 ft oven length: accommodates oversized parts and long components.", "6,000 lb weight capacity: heavy machinery, industrial frames and structural pieces."],
			"## Facility highlights",
			["Flexibility: we coat everything from small custom projects to full-size industrial assemblies.", "Consistency: large items receive the same durable, even finish as smaller parts.", "Scalability: one-off custom orders or recurring bulk projects."],
			"## What this means for you",
			"When you choose Koojo, you're choosing a facility designed for precision, durability, and scale. If you are not sure a part will fit, send us its dimensions and weight and we will confirm before you ship. For what we do with those parts, see [industrial powder coating](/services/industrial-powder-coating).",
		],
	},
	{
		"slug": "certification",
		"title": "Powder Coating Quality Assurance & Certification",
		"keyword": "powder coating quality assurance",
		"seo_title": "Powder Coating Quality Assurance & Certification | Koojo",
		"intro": "Koojo is a certified provider by the Absolute Bureau of Certification LLC and upholds strict quality control on every project.",
		"body": [
			"## Our quality assurance guarantee",
			"At Koojo Custom Coating, we are committed to delivering exceptional powder coating solutions and mobile sandblasting services that meet the highest industry standards. As a certified provider by the Absolute Bureau of Certification LLC, we uphold strict quality control measures to ensure every project meets or exceeds customer expectations.",
			"## A commitment to excellence",
			"Quality is at the core of everything we do. Our team follows proven industry standards to guarantee durable, long-lasting finishes that stand up to time, weather, and wear. Whether it's protective coatings for industrial machinery, automotive parts, or custom projects, we take every step to ensure a flawless application and superior performance.",
			"## Test reports",
			"For customers requiring additional validation, third-party testing reports can be provided upon request. [Contact us](/contact-us) to learn more about our certification.",
		],
		"image": img("b95a8d_0117c4bef82d47f58e1239687fe31e78~mv2.png", "Koojo quality assurance certification marks", "koojo-certification.png"),
	},
	{
		"slug": "privacy-policy",
		"title": "Privacy Policy",
		"keyword": "",
		"seo_title": "Privacy Policy | Koojo Custom Powder Coating",
		"body": "WIX:privacy-policy",
	},
	{
		"slug": "services",
		"title": "Powder Coating Services",
		"keyword": "powder coating services",
		"seo_title": "Powder Coating Services | Koojo Custom Powder Coating",
		"intro": "All of our services in one place. Choose a service to see what it covers, what we coat and how to prepare your parts.",
		"body": [
			"## Our process",
			"To ensure proper adhesion, the metal surface must be clean and contaminant-free before any powder is applied.",
			["Cleaning: degreasing, chemical cleaning and phosphating to enhance corrosion resistance and powder bonding.", "Rinsing: removing chemicals and residues, sometimes with a deionized final rinse.", "Drying: in an oven or with hot air, because residual moisture causes coating defects.", "Masking: covering threads, holes and other areas that must not be coated.", "Inspection: only parts free of contaminants and defects move on to coating."],
			"## Packaging and shipping",
			"### Customized packaging solutions",
			"Every project is unique, and so are its packaging needs. We use a range of durable materials to protect your items, including protective wrapping, sturdy boxes, and custom packaging options for larger or irregularly shaped items. Our solutions are designed to minimize the risk of damage during transit.",
			"### Safe and reliable shipping",
			"We work with trusted shipping providers to deliver your items securely and on time. Serving clients across Milton and the Greater Toronto Area (GTA), we ensure your products are handled with care from pickup to delivery.",
			"### Efficient loading and handling",
			"To streamline the transportation process, our team employs careful loading practices that prioritize safety and efficiency. Whether you're shipping small parts or large industrial items, we ensure your products are ready for transit without delays.",
		],
		"faqs": [
			("How is powder coating priced?", "Quotes are based on the size and number of parts, the preparation they need and the finish you choose. Send photos and dimensions for an accurate estimate."),
			("What is your turnaround time?", "Turnaround depends on the size of the job and our schedule. Tell us your deadline when you request a quote and we will confirm what is possible."),
			("What areas do you serve?", "Our shop is in Milton and we serve the Greater Toronto Area, including Halton, Peel, Hamilton and Waterloo Region."),
		],
	},
	{
		"slug": "industries",
		"title": "Powder Coating by Industry",
		"keyword": "powder coating by industry",
		"seo_title": "Powder Coating by Industry | Koojo Custom Powder Coating",
		"intro": "An industrial coating partner for fabricators, OEMs and institutions. Find your industry to see how we work with businesses like yours.",
	},
	{
		"slug": "locations",
		"title": "Powder Coating Service Areas",
		"keyword": "powder coating service areas",
		"seo_title": "Powder Coating Service Areas | Koojo",
		"intro": "One shop in Milton serving Halton, Peel, Hamilton and Waterloo Region, with pickup and delivery available.",
	},
	{
		"slug": "projects",
		"title": "Powder Coating Projects",
		"keyword": "powder coating projects",
		"seo_title": "Powder Coating Projects | Our Work | Koojo",
		"intro": "Every project tells a story of durability and design. Browse recent work from our shop floor and filter by type.",
	},
	{
		"slug": "blog",
		"title": "Powder Coating Guides",
		"keyword": "powder coating guides",
		"seo_title": "Powder Coating Guides | Koojo Blog",
		"intro": "How-to guides and plain explanations of powder coating processes, materials, finishes and standards.",
	},
]

MENUS = [
	{
		"name": "primary",
		"label": "Primary Navigation",
		"items": [
			("Home", "/"),
			("Services", "/services"),
			("Industries", "/industries"),
			("Our Work", "/projects"),
			("Capabilities", "/capabilities"),
			("About", "/about-us"),
			("Blog", "/blog"),
		],
	},
	{
		"name": "footer_company",
		"label": "Footer: Company",
		"items": [
			("About Us", "/about-us"),
			("Contact Us", "/contact-us"),
			("Certification", "/certification"),
			("Get a Quote", "/get-a-quote"),
			("Privacy Policy", "/privacy-policy"),
		],
	},
]

# Legacy URLs named in the blueprint (section 6).
REDIRECTS = [
	("/industrial-powder-coating-gta", "/services/industrial-powder-coating"),
	("/powder-coating-milton-guelph-cambridge-hamilton", "/locations"),
]

# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Uploaded & Audited Content Merge (All 44 unique uploaded documents)
# -----------------------------------------------------------------------------
import os, json

_HERE = os.path.dirname(os.path.abspath(__file__))
_uploaded_json = os.path.join(_HERE, "uploaded_content.json")

CANONICAL_KEYWORDS = {
    # Pages
    "pages:home": "powder coating company GTA",
    "pages:about-us": "about Koojo Custom Powder Coating",
    "pages:contact-us": "contact Koojo powder coating",
    "pages:get-a-quote": "powder coating quote",
    "pages:capabilities": "large part powder coating",
    "pages:certification": "powder coating quality assurance",
    "pages:privacy-policy": "Koojo Custom Powder Coating",
    "pages:services": "powder coating services",
    "pages:industries": "powder coating by industry",
    "pages:locations": "powder coating service areas",
    "pages:projects": "powder coating projects",
    "pages:blog": "powder coating guides",
    # Services
    "services:industrial-powder-coating": "industrial powder coating",
    "services:surface-preparation": "powder coating surface preparation",
    "services:sandblasting": "sandblasting services",
    "services:custom-colors-finishes": "custom powder coating colours",
    "services:restoration-recoating": "powder coat stripping and recoating",
    "services:automotive-powder-coating": "automotive powder coating",
    "services:wheel-rim-powder-coating": "rim powder coating",
    "services:architectural-coatings": "architectural powder coating",
    "services:bulk-commercial-orders": "commercial powder coating",
    "services:specialty-custom-projects": "specialty powder coating",
    # Industries
    "industries:metal-fabricators-welding-shops": "powder coating for metal fabricators",
    "industries:manufacturing-automation": "powder coating for manufacturers",
    "industries:machine-shops": "powder coating for machine shops",
    "industries:contractors-construction": "powder coating for contractors",
    "industries:food-processing-equipment": "powder coating for food processing equipment",
    "industries:agricultural-heavy-equipment": "agricultural equipment powder coating",
    "industries:municipal-institutional": "powder coating for municipalities",
    # Locations
    "locations:Milton": "powder coating Milton",
    "locations:Oakville": "powder coating Oakville",
    "locations:Burlington": "powder coating Burlington",
    "locations:Mississauga": "powder coating Mississauga",
    "locations:Halton Hills": "powder coating Halton Hills",
    "locations:Brampton": "powder coating Brampton",
    "locations:Guelph": "powder coating Guelph",
    "locations:Cambridge": "powder coating Cambridge",
    "locations:Hamilton": "powder coating Hamilton",
    # Projects
    "projects:conveyor-frame-automotive-plant": "conveyor frame powder coating",
    "projects:automation-line-frame": "automation line frame case study",
    "projects:food-processing-line-frame": "food processing line frame case study",
    "projects:robotic-base": "robotic base case study",
    "projects:safety-bollards": "bollard powder coating case study",
    "projects:church-gates": "church gates case study",
}

if os.path.exists(_uploaded_json):
    with open(_uploaded_json, "r", encoding="utf-8") as _f:
        _UP = json.load(_f)

    # Merge Services
    for _s in SERVICES:
        _slug = _s["slug"]
        _s["keyword"] = CANONICAL_KEYWORDS.get(f"services:{_slug}", _s.get("keyword"))
        if "services" in _UP and _slug in _UP["services"]:
            _up = _UP["services"][_slug]
            if _up.get("body"): _s["body"] = _up["body"]
            if _up.get("faqs"): _s["faqs"] = _up["faqs"]
            if _up.get("summary"): _s["summary"] = _up["summary"]
            if _up.get("meta_title"): _s["seo_title"] = _up["meta_title"]
            if _up.get("meta_desc"): _s["seo_description"] = _up["meta_desc"]

    # Merge Industries
    for _ind in INDUSTRIES:
        _slug = _ind["slug"]
        _ind["keyword"] = CANONICAL_KEYWORDS.get(f"industries:{_slug}", _ind.get("keyword"))
        if "industries" in _UP and _slug in _UP["industries"]:
            _up = _UP["industries"][_slug]
            if _up.get("body"): _ind["body"] = _up["body"]
            if _up.get("faqs"): _ind["faqs"] = _up["faqs"]
            if _up.get("summary"): _ind["summary"] = _up["summary"]
            if _up.get("meta_title"): _ind["seo_title"] = _up["meta_title"]
            if _up.get("meta_desc"): _ind["seo_description"] = _up["meta_desc"]

    # Merge Locations (all 9 locations live and published)
    for _loc in LOCATIONS:
        _city = _loc["city"]
        _loc["wave"] = 1
        _loc["keyword"] = CANONICAL_KEYWORDS.get(f"locations:{_city}", f"powder coating {_city}")
        if "locations" in _UP and _city in _UP["locations"]:
            _up = _UP["locations"][_city]
            if _up.get("body"): _loc["body"] = _up["body"]
            if _up.get("faqs"): _loc["faqs"] = _up["faqs"]
            if _up.get("summary"): _loc["summary"] = _up["summary"]
            if _up.get("meta_title"): _loc["seo_title"] = _up["meta_title"]
            if _up.get("meta_desc"): _loc["seo_description"] = _up["meta_desc"]

    # Merge Projects
    for _pr in PROJECTS:
        _slug = _pr["slug"]
        _pr["keyword"] = CANONICAL_KEYWORDS.get(f"projects:{_slug}", _pr.get("keyword"))
        if "projects" in _UP and _slug in _UP["projects"]:
            _up = _UP["projects"][_slug]
            if _up.get("body"): _pr["body"] = _up["body"]
            if _up.get("summary"): _pr["summary"] = _up["summary"]
            if _up.get("meta_title"): _pr["seo_title"] = _up["meta_title"]
            if _up.get("meta_desc"): _pr["seo_description"] = _up["meta_desc"]

    # Merge Pages
    for _p in PAGES:
        _slug = _p["slug"]
        _p["keyword"] = CANONICAL_KEYWORDS.get(f"pages:{_slug}", _p.get("keyword"))
        if _slug == "home":
            if "pages" in _UP and "home" in _UP["pages"]:
                _home_up = _UP["pages"]["home"]
                if not any(_b.get("_type") == "marketing_faq" for _b in HOME_BLOCKS) and _home_up.get("faqs"):
                    _faq_items = [{"question": _q, "answer": _a} for _q, _a in _home_up["faqs"]]
                    _faq_block = {
                        "_type": "marketing_faq",
                        "_key": "faq",
                        "headline": "Frequently Asked Questions",
                        "items": _faq_items,
                    }
                    HOME_BLOCKS.insert(-1, _faq_block)
        else:
            if "pages" in _UP and _slug in _UP["pages"]:
                _up = _UP["pages"][_slug]
                if _up.get("body"): _p["body"] = _up["body"]
                if _up.get("faqs"): _p["faqs"] = _up["faqs"]
                if _up.get("summary"): _p["intro"] = _up["summary"]
                if _up.get("meta_title"): _p["seo_title"] = _up["meta_title"]
                if _up.get("meta_desc"): _p["seo_description"] = _up["meta_desc"]
