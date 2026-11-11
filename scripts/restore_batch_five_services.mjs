import fs from "fs";

function make_pt_table(headers, rows) {
  const all_rows = [];
  // Header row
  const hdr_cells = headers.map(h => ({
    _type: "tableCell",
    isHeader: true,
    content: [{ _type: "span", _key: "sp_" + Math.random().toString(36).substring(2, 9), text: String(h), marks: [] }]
  }));
  all_rows.push({
    _type: "tableRow",
    _key: "tr_h_" + Math.random().toString(36).substring(2, 9),
    cells: hdr_cells
  });

  // Data rows
  rows.forEach((r, r_idx) => {
    const row_cells = r.map(c => ({
      _type: "tableCell",
      isHeader: false,
      content: [{ _type: "span", _key: "sp_" + Math.random().toString(36).substring(2, 9), text: String(c), marks: [] }]
    }));
    all_rows.push({
      _type: "tableRow",
      _key: "tr_" + r_idx + "_" + Math.random().toString(36).substring(2, 9),
      cells: row_cells
    });
  });

  return {
    _type: "table",
    _key: "tbl_" + Math.random().toString(36).substring(2, 9),
    hasHeaderRow: true,
    rows: all_rows
  };
}

const content = JSON.parse(fs.readFileSync("scripts/seed/uploaded_content.json", "utf-8"));

// 1. /services/restoration-recoating
content.services["restoration-recoating"] = {
  title: "Powder Coat Stripping and Recoating | Koojo",
  seo_title: "Powder Coat Stripping and Recoating | Koojo",
  seo_description: "Powder coat stripping and recoating for worn, rusted or faded parts. Old coating removal, rust repair and a fresh cured finish in Milton. Get a quote.",
  primary_keyword: "powder coat stripping and recoating",
  h1: "Powder Coat Stripping and Recoating for Metal Parts",
  body: [
    "Powder coat stripping and recoating removes a failed, damaged or unwanted finish and replaces it with a fresh powder coat finish that bonds to clean metal. At Koojo Custom Powder Coating in Milton, we have finished more than 10,000 items since 2012, and many of them were older parts brought back into service. Whether your railings are peeling, your frames are chipped or your equipment has rusted, our powder coat removal and recoating service restores the metal and its protection. Tell us what the part is and what is wrong with it, and we will recommend the right approach.",
    "Our standard turnaround is 48 hours for typical shop orders, and we are open Monday to Friday, 7 AM to 5 PM. Heavily rusted or multi-part jobs are scheduled when we quote, once we know the size, the condition and how much old coating removal the parts need. Every powder coat stripping and recoating job starts with a short conversation about the part and what went wrong.",
    "Since 2012 | 10,000+ Items | 48 Hr Turnaround | 5.0 ★ Google Rating",
    "## What Is Powder Coat Stripping and Recoating?",
    "Powder coat stripping and recoating is a two-part restoration process. The old finish comes off completely, then new powder is applied electrostatically and cured in an oven. The goal is a clean, even finish that bonds to bare metal instead of a new layer sitting on a failing one.",
    "Powder coat recoating over a damaged finish rarely lasts. A peeling powder coat or a chipped powder coating usually means the bond has already failed, and a new coat on top can lift in the same places. Rust under the surface makes this worse, because it keeps spreading beneath any new film. That is why we remove the old finish first and complete surface rust treatment before the new powder goes on.",
    "Not every part needs full powder coating restoration. A faded powder coat on a sound surface may only need cleaning and a refresh, while rust, damage or a colour change calls for complete old coating removal. We assess each part before we quote, so powder coat stripping and recoating covers only the work the part actually needs.",
    "## How Our Powder Coat Stripping and Recoating Process Works",
    "Our powder coat stripping and recoating process has six stages: assessment, removal, rust repair, pretreatment, recoating and inspection. Each stage protects the next one, so the new finish bonds properly and lasts.",
    "1. Assessment. We look at the metal, the existing coating, the extent of rust and any damage. Photos sent with your quote request help us plan the stripping and recoating, including the removal method, the repairs and the finish, before the part arrives.",
    "2. Removal. We take the old finish down to bare metal. Paint stripping and powder coat stripping take different effort, so we confirm the method for your part when we quote. Heavy coatings, scale and rust often call for blasting, described on our sandblasting services page.",
    "3. Rust repair. Surface rust is cleaned from the metal so it cannot spread under the new coat. Deep pitting or structural damage is flagged to you early, because recoating cannot restore a weakened part.",
    "4. Pretreatment. Clean metal can develop flash rust quickly, so pretreatment before recoating follows removal closely. Our surface preparation page explains the washing and masking steps, and surface preparation for recoating is part of every restoration job.",
    "5. Recoating. We plug threads and bores, then apply the powder electrostatically. Oven curing at 180–200 °C melts the powder into one continuous film.",
    "6. Inspection. We check coverage, colour and finish, measure film thickness and look for defects before packing the part.",
    "Timing matters as much as technique. Typical shop work follows our standard 48-hour turnaround, and we receive parts Monday to Friday, 7 AM to 5 PM. Planning powder coat stripping and recoating as one job keeps bare metal from sitting uncoated, which is the main cause of early flash rust. Recoating turnaround for larger or heavily rusted parts is confirmed when we quote. Parts with several layers of old paint can take longer to strip, so we ask for photos early.",
    "## Which Parts and Metals Can We Restore?",
    "Our stripping and recoating service covers steel and aluminum parts that can withstand curing, from small brackets to large fabricated frames. See our capabilities page for size and weight limits. Typical jobs include:",
    [
      "Railings and gates. Railing restoration and gate restoration are common, because outdoor metalwork loses its finish first.",
      "Equipment and machinery. Equipment refurbishment and machinery refurbishment bring worn housings, guards and frames back to a protected finish.",
      "Structural steel and frames. Structural steel recoating suits fabricated frames and supports where rust has started under the old coat.",
      "Older metalwork. Aging metalwork from churches, parks and buildings often carries several layers of old paint, which we remove before recoating."
    ],
    "Galvanized, cast and heavily welded parts can need extra checks because trapped gases may affect the surface, so tell us the material when you request a quote. Some parts are not worth restoring, and we will say so if the metal is too weak or too damaged. For parts that live outdoors, powder coat stripping and recoating helps restore weathered metal and extend coating life.",
    "## Restoration and Recoating Options",
    "You can return a part to its original look or change it completely. The stripping and recoating options below cover the most common requests, and each can be paired with a new finish.",
    [
      "Like-for-like recoating. We aim for an original colour match so the restored part blends with the rest of the installation. Send a colour code, a RAL number or a small sample.",
      "Colour change recoating. A new shade, sheen or texture gives older parts a new look. Our custom powder coating colours page explains the choices.",
      "Removal with repair. Some parts need old coating removal and rust repair before they return to service. Tell us what is wrong and we will confirm the steps.",
      "Repair or recoat. A small chip may be repairable, but widespread peeling, rust or fading means a full recoat is the better choice. We tell you which applies when we assess the part."
    ],
    "Not sure whether your part needs stripping at all? Send photos with your quote request. A restoration quote for powder coat stripping and recoating starts with a clear description of the damage and the finish you want, and it lets us refinish metal parts without guesswork. Whatever you choose, we confirm the plan with you before work starts.",
    "## How We Check Restoration Quality",
    "For every powder coat stripping and recoating job, we check the bare metal after removal, then the finished coat, before parts leave the shop. Our quality steps are outlined on our certification page, and test reports are available on request.",
    "Where a job calls for it, test methods include the ASTM D3359 adhesion test, ASTM D7091 for dry film thickness and ASTM B117 for salt spray resistance. Our certification is held through the Absolute Bureau of Certification. A new finish is only worth applying if it stays bonded, so we test adhesion as well as appearance on powder coat recoating work, which helps prevent a repeat adhesion failure or coating failure. We also confirm the cured finish is even, with no thin spots, runs or bare patches.",
    "## Restoration in Practice",
    "Our church gates project shows how Koojo documents architectural metalwork from first inspection to the finished coat. The case study lists the part, metal, size, powder, colour code and turnaround, with before and after photos, so you can see how stripping and recoating work is recorded.",
    "You can also browse more finished parts on our Our Work page. A good restoration brief includes the part, the metal, what is wrong and the finish you want. With those four details, we can quote powder coat stripping and recoating accurately and confirm the plan before work begins.",
    "## Who Uses Our Recoating Service",
    "Municipal and institutional owners, contractors, farm and heavy equipment owners and manufacturers use our powder coat stripping and recoating service most. These customers have metal that has aged, and they need a durable finish back quickly, with a clear scope and a documented result.",
    "See how we support municipal and institutional customers with bollards, park equipment and church metalwork, and agricultural and heavy equipment owners, where rust is the main concern. Our powder coat stripping and recoating also supports our wider industrial powder coating work and the full range of powder coating services at our Milton shop.",
    "## Get Your Metal Restored",
    "Ready to bring worn metal back to a lasting finish? Send part photos and details through our quote form for powder coat stripping and recoating advice, or visit 10874 Steeles Ave E, Milton, Monday to Friday, 7 AM to 5 PM. Call (905) 876-7060 or email sales@koojopowdercoating.com."
  ],
  faqs: [
    {
      question: "Can you remove old powder coating from my part?",
      answer: "Yes. Our powder coat stripping takes the finish down to bare metal, then we check the surface and recoat it. Send photos and part details with your quote request so we can confirm the removal method and any repairs."
    },
    {
      question: "Is it better to repair a chip or recoat the whole part?",
      answer: "A small chip may be repairable, but widespread chipping, peeling or rust means a full recoat is the better choice. A new coat on top of a failing one tends to lift again, so we advise stripping and recoating with a bare metal finish first."
    },
    {
      question: "Do you treat rust before recoating?",
      answer: "Yes. We clean surface rust from the metal so it cannot spread under the new coat. Deep pitting or structural damage is flagged early, because recoating cannot restore a weakened part."
    },
    {
      question: "Can I change the colour when I recoat?",
      answer: "Yes. A recoat is a good time to choose a new colour, sheen or texture. Send a RAL number or sample and we will confirm what is available when we quote."
    },
    {
      question: "How long does powder coat stripping and recoating take?",
      answer: "Typical shop orders follow our standard 48-hour turnaround. Large, heavily rusted or multi-part jobs are scheduled when we quote, once we know the size, condition and amount of removal."
    },
    {
      question: "What should I send for a restoration quote?",
      answer: "Send photos of the part, its size and quantity, a description of the problem and the colour you want. This lets us price powder coat stripping and recoating accurately."
    }
  ]
};

// 2. /services/sandblasting
content.services["sandblasting"] = {
  title: "Sandblasting Services & Mobile Sandblasting | Koojo",
  seo_title: "Sandblasting Services & Mobile Sandblasting | Koojo",
  seo_description: "Sandblasting services in our shop or on site: rust and mill-scale removal, abrasive blasting and mobile sandblasting. Request a quote.",
  primary_keyword: "sandblasting services",
  h1: "Sandblasting Services & Mobile Sandblasting",
  body: [
    "Sandblasting services remove rust, scale and old surface contamination so bare metal is ready for a lasting powder coat. At Koojo Custom Powder Coating, our Milton team uses abrasive blasting in the shop and offers mobile sandblasting for parts and structures that cannot travel. Since 2012, we have finished more than 10,000 items for fabricators, manufacturers and contractors across the GTA, with a 48-hour turnaround on shop work. Whether you have welded frames, aging railings or heavy equipment, we match the blasting method to the metal and the finish you want. Request a sandblasting quote below, or call (905) 876-7060, Monday to Friday, 7 AM to 5 PM, to talk through your project. Careful sandblasting before powder coating keeps the finish bonded for years.",
    "Since 2012 | 10,000+ Items | 48 Hr Turnaround | 5.0 ★ Google Rating",
    "## What Are Sandblasting Services?",
    "Sandblasting services use compressed air to drive abrasive media against metal, removing rust, scale and old surface debris. The result is clean, bare metal with an even texture that lets powder coating grip firmly and last for years, even in tough outdoor conditions.",
    "The word sandblasting is common, but most modern work uses other abrasives, so the broader names are media blasting and abrasive blasting. Each media cuts differently. Aluminum oxide blasting and steel grit blasting cut fast and leave a rougher surface, while glass bead blasting leaves a smoother, cleaner finish. The texture left behind is called the surface profile, or anchor profile, and it gives powder something to hold. Good blast cleaning removes everything that would stop a coating from bonding and leaves a bare metal finish ready to coat.",
    "That is why we treat industrial sandblasting as part of the coating process, not a separate chore. Sandblasting and powder coating work best when one team plans both, because clean steel starts to show flash rust soon after blasting. Skipping this link in the chain is the most common reason a coating fails early.",
    "## How Does Our Sandblasting Process Work?",
    "Our sandblasting services follow five stages: inspection, blast media selection, blasting, cleanup, and handoff to coating. Each stage protects the metal and the finish, and blasted parts move to coating quickly so rust never gets a chance to return to the metal before the coating goes on.",
    "1. Inspection and planning (on arrival). We check each part for heavy rust, pitted and scaled steel, weld spatter and thin sections. We then decide whether the job suits our shop or on-site sandblasting. Early inspection lets us flag problem areas before they cost you time.",
    "2. Blast media selection. The right media depends on the metal and the finish you need. Tough rust and scale call for harder media, while softer metals and cosmetic parts need gentler options. We confirm the choice with you when the finish or tolerance is critical.",
    "3. Blasting. Our operators work across every surface, including welds, corners and recesses. They adjust pressure and distance so rust and mill-scale removal is complete without damaging thin sections. Industrial sandblasting at this stage is methodical, never rushed.",
    "4. Cleanup. Compressed air and brushing clear spent media and dust from holes, seams and enclosed sections. Trapped grit would cause defects under the powder, so we never skip this step.",
    "5. Inspection and handoff. We confirm a uniform, blast-cleaned surface, then move the part toward coating as soon as possible, since flash rust can form quickly on clean steel.",
    "Timing matters as much as technique. Shop blasting sits inside our standard 48-hour turnaround, and we receive parts Monday to Friday, 7 AM to 5 PM. For mobile sandblasting, tell us the site, access and schedule when you request a quote and we will plan the visit around your deadline. Industrial sandblasting is scheduled alongside coating, so a blasted part never waits long between steps. That planning prevents the gaps that let bare metal rust, and it keeps your project moving.",
    "## Which Metals and Parts Need Sandblasting?",
    "Steel and iron benefit most, because rust and scale form naturally on them. Cast parts, structural steel, fabricated frames and heavy equipment also respond well. Thin or soft metals need gentler media, so our sandblasting services plan the method for each metal before blasting starts.",
    [
      "Steel and iron. Sandblasting steel removes rust and mill scale, the hard grey layer left by hot rolling that blocks coating adhesion. It is the most common job we handle, and it suits everything from small brackets to large frames.",
      "Welded and cast parts. Sandblasting weldments cleans weld discoloration and spatter, and gives rust removal from metal even in tight corners.",
      "Aluminum and softer metals. Gentler media protects the surface, so we choose finer abrasives and lower pressure for these parts, which keeps edges and details sharp."
    ],
    "Typical work includes sandblasting structural steel, sandblasting gates and railings, sandblasting trailers and frames, machine bases and equipment housings. Sandblasting heavy equipment and sandblasting large fabrications can be done in our shop or on site, so confirm the part size when you request a quote. Whether you need sandblasting metal parts one at a time or industrial sandblasting for a full production run, we plan the abrasive blasting to protect the metal.",
    "## What Sandblasting Options Does Koojo Offer?",
    "Koojo offers shop blasting for parts we can move, a mobile service for work on site, and a choice of blast media to suit the metal. Blasting is most often paired with powder coating, so ask us how your job should be planned from start to finish.",
    [
      "Shop sandblasting. Parts come to our Milton shop, where blasting happens in a controlled setting with dust containment and a fast route into coating.",
      "Mobile sandblasting. Our mobile blasting crew brings on-site blasting equipment to structures, large frames and fixed equipment that are hard to move. Portable sandblasting equipment suits these jobs. Share site access and layout when you quote.",
      "Media choices. Blast media selection covers aluminum oxide, steel grit and glass bead, matched to the metal and the finish you want. Larger industrial sandblasting jobs often use a mix of media.",
      "What comes next. After blasting, many parts still need washing and masking, which our powder coating surface preparation service covers. Parts with aged coatings may suit our restoration and recoating service."
    ],
    "Not sure which option fits? Send photos and the part material. We will recommend an approach, and our sandblasting services advice comes with your quote. Choosing the right method up front avoids a damaged part, and protects the rust protection your coating is meant to provide.",
    "## How Do We Check Blasting Quality?",
    "We verify blasting through visual inspection and a surface check before coating. Koojo is certified through the Absolute Bureau of Certification, our inspection steps are documented, and test reports are available on request, so you can trust the work behind every finish.",
    "Quality starts at intake, when we look for heavy rust, thick scale and old coatings. After blasting, a blast-cleaned surface should look even in colour, with no shiny rust patches, leftover scale or traces of old paint. Surface profile matters too. If the surface is too smooth, powder grips poorly, and if it is too rough, peaks can show through the finish and shorten its life. We check this before parts move on, and we flag any concern with you early.",
    "Our sandblasting services are never signed off until the part passes these checks. Consistent industrial sandblasting also means the next batch matches the last, because we keep records that support repeat orders. Cleanup is part of quality. Loose grit left in seams spoils the coating, so we clear it before parts move on. Because clean bare steel can show flash rust quickly, we plan coating soon after blasting, and we hold shop and mobile work to the same documented checks every time. See our certification page for details on how we work. Careful abrasive blasting also leaves the clean bare steel that strong coatings need.",
    "## See Sandblasting in a Real Project",
    "Outdoor metalwork such as bollards and gates collects rust, scale and old coatings, which makes sandblasting services a smart first step. Our safety bollards case study documents the part, metal, size, powder, colour code and turnaround for a real customer, so you can see what a documented job looks like.",
    "Read the safety bollards project to see the finished result. Before and after photos show the standard we hold ourselves to, from the bare metal stage through to the finished coating, and the same documented approach applies to your parts.",
    "## Which Industries Use Our Sandblasting Services?",
    "Fabricators, contractors, farm and heavy equipment owners and manufacturers use us most. These customers need dependable industrial sandblasting, quick turnaround and a clean surface that supports coating. Our approach scales from single parts to production runs, with the same care every time.",
    "See how we support contractors and construction teams, who often need work done on site, and agricultural and heavy equipment owners, where heavy rust is the main concern, so you can find the page that matches your work. Our sandblasting services also support our wider industrial powder coating work and the full range of powder coating services at our Milton shop.",
    "## Get Your Metal Blasted Right",
    "Ready for clean, bare metal and a lasting finish? Send part photos and details through our quote form for sandblasting services advice, or visit 10874 Steeles Ave E, Milton, Monday to Friday, 7 AM to 5 PM. Call (905) 876-7060 or email sales@koojopowdercoating.com."
  ],
  faqs: [
    {
      question: "Do you offer mobile sandblasting?",
      answer: "Yes. We offer mobile sandblasting for work that cannot travel to our shop. Send site details, photos and your preferred schedule when you request a quote so we can plan access, cleanup and timing before anyone arrives."
    },
    {
      question: "What is the difference between sandblasting and abrasive blasting?",
      answer: "Sandblasting is the common name, while abrasive blasting is the broader term for any media driven by air. Most modern work uses media other than sand, chosen to suit the metal, the finish and the coating that follows."
    },
    {
      question: "How soon should blasted parts be coated?",
      answer: "As soon as possible. Clean steel develops flash rust quickly, so we plan blasting and coating together to keep the surface protected. Tell us your deadline and we will sequence the work to match."
    },
    {
      question: "How long does a sandblasting job take?",
      answer: "Shop work follows our standard 48-hour turnaround for typical orders. Large, heavily rusted or mobile jobs are scheduled when we quote, once we know the size, condition and access."
    }
  ]
};

// 3. /services/surface-preparation
content.services["surface-preparation"] = {
  title: "Powder Coating Surface Preparation | Koojo Powder Coating",
  seo_title: "Powder Coating Surface Preparation | Koojo Powder Coating",
  seo_description: "Powder coating surface preparation: degreasing, phosphate pretreatment, masking and dry-off for lasting adhesion. 48-hour turnaround. Request a quote.",
  primary_keyword: "powder coating surface preparation",
  h1: "Powder Coating Surface Preparation & Pretreatment",
  body: [
    "Powder coating surface preparation is the cleaning, pretreatment and masking work that decides whether a powder finish bonds for years or fails within months. At Koojo Custom Powder Coating, every part is degreased, chemically treated, rinsed and dried before any powder goes on. Since 2012, our Milton team has prepared more than 10,000 items for fabricators, manufacturers and contractors across the GTA, with a 48-hour turnaround. Whether you send raw steel weldments, machined components or aluminum brackets, our surface preparation for powder coating removes oil, residue and contamination so the coating can grip the metal. Request a quote below, or call (905) 876-7060, Monday to Friday, 7 AM to 5 PM, and our team will advise on the right pretreatment for your parts.",
    "Since 2012 | 10,000+ Items | 48 Hr Turnaround | 5.0 ★ Google Rating",
    "## What Is Powder Coating Surface Preparation?",
    "Powder coating surface preparation is the sequence of cleaning, chemical treatment, masking and drying steps that readies bare metal for powder. It removes oils, oxides and soils, then leaves a clean, slightly reactive surface so the powder bonds firmly while it cures.",
    "Powder cannot hide a dirty surface. Thermoset powder melts and flows in the oven at a cure temperature of 180–200 °C, so any film of cutting oil, forming lubricant or fingerprint residue trapped underneath causes craters, fisheyes and weak powder coating adhesion. Proper powder coating pretreatment solves two problems at once: it cleans the part, and it adds a thin conversion coating that improves grip and slows rust under the finish.",
    "Without it, even premium powder can lift at edges and welds. That is why we treat surface preparation for powder coating as a core production step, never a cosmetic extra, and why every job at our shop begins here rather than in the spray booth. The powder is the visible finish, but the bond underneath decides how long it stays attached.",
    "## How Does Our Powder Coating Pretreatment Process Work?",
    "Our powder coating surface preparation has five stages: inspection and masking, alkaline cleaning, rinse, phosphate conversion treatment, and a final rinse and dry-off. Each stage removes one specific barrier to adhesion, and parts move to coating only when they are clean, dry and free of flash rust.",
    "1. Inspection and masking (on arrival). We check each part for heavy rust, old coatings, weld spatter and trapped oil. We then mask threads, bores and contact faces with high-temperature plugs and tape. Masking for powder coating protects precision features, so bolts still thread in after curing.",
    "2. Alkaline cleaning. A cleaning bath performs oil and grease removal from cutting fluid, shop dirt and handling marks. Degreasing before powder coating is the strongest defence against craters, so we never skip it, even on parts that look clean.",
    "3. Rinse. Clean water flushes cleaner residue, which would otherwise interfere with the chemical treatment that follows.",
    "4. Phosphate pretreatment. This step forms a thin crystalline layer on the metal. The layer improves grip and gives the finish a protected base. Metal pretreatment for powder coating always depends on the substrate and on where the finished part will live.",
    "5. Final rinse and dry-off. A last rinse removes chemical salts. The rinse and dry-off step then drives off moisture, which is the key to flash rust prevention. Parts go straight to coating once dry.",
    "Timing matters as much as chemistry. Every stage sits inside our standard 48-hour turnaround, and we receive parts Monday to Friday, 7 AM to 5 PM. Because multi-stage pretreatment happens first, coating and curing always start from a controlled surface. Our powder coating pretreatment is built into the schedule, not added afterwards, so a well-prepared part never waits on a separate booking. If your project has a deadline, tell us when you request a quote and we will plan around it. Clear communication at the start keeps powder coating surface preparation on schedule and avoids surprises at pickup.",
    "## Which Metals and Parts Need Surface Preparation for Powder Coating?",
    "Every metal needs preparation, but the method changes with the substrate. Steel needs oil and residue removed, aluminum needs its oxide layer controlled, and galvanized steel needs careful treatment and outgassing management. Fabricated and machined parts also need masking before coating.",
    [
      "Steel. Steel pretreatment targets mill oil, weld residue removal and early rust. It is the most common job we handle, and the metal pretreatment for powder coating we apply is matched to the part.",
      "Aluminum. Aluminum pretreatment uses a chemical treatment that cleans the surface and builds a bonding layer, because raw aluminum oxidizes quickly. Here, the chemical treatment protects adhesion more than any other step.",
      "Galvanized steel. Zinc surfaces respond differently from bare steel and can release trapped gases while curing, so galvanized parts get their own preparation plan."
    ],
    "Typical parts include welded frames, brackets, guards, railings, bollards, machine components and equipment housings. Each one needs powder coating surface preparation sized to its shape, because deep corners and enclosed sections trap oil and moisture more easily than flat plate. Our fabricated parts pretreatment and custom part preparation cover one-off pieces and repeat production runs, with the same standard applied to both. Good preparation means each load leaves with a production-ready surface, whatever the shape or size.",
    "## What Pretreatment Options Does Koojo Offer?",
    "Koojo matches the pretreatment to the part. Most steel receives a standard wash and phosphate sequence, aluminum and galvanized metal get a suitable chemical pretreatment, and parts with threads or sealing faces receive detailed masking. Heavy rust or old coatings are handled before pretreatment.",
    [
      "Standard pretreatment wash stages. Cleaning, rinsing, conversion treatment and drying for everyday steel parts, delivered as consistent powder coating pretreatment.",
      "Iron or zinc phosphate. Iron phosphate pretreatment suits many indoor and general-duty parts. Zinc phosphate pretreatment is considered when a part needs extra rust prevention before coating, such as outdoor equipment.",
      "Plugging and masking. Threaded hole masking, bore plugs and tape protect dimensions. Tell us about special requirements when you quote.",
      "Heavy cleaning first. Thick rust, scale or an old finish needs more than a wash. Our sandblasting service removes it mechanically, and our restoration and recoating service handles aged coatings, before pretreatment begins."
    ],
    "Not sure which option fits? Send photos and the part material. We will recommend an approach, and our surface preparation for powder coating advice comes with your quote. Choosing the right powder coating surface preparation up front is far cheaper than fixing a failed finish later, and for aluminum and galvanized work we select the metal pretreatment for powder coating that suits that substrate.",
    "## How Do We Check Pretreatment Quality?",
    "We verify preparation through visual inspection, surface checks and adhesion testing on the finished coating. Koojo is certified through the Absolute Bureau of Certification, our inspection steps are documented, and test reports are available on request, so you can trust the work behind every finish.",
    "Pretreatment quality control starts before the bath: we look for oil, rust and weld residue on arrival. After rinsing, a clean surface should hold a continuous film of water, which is the idea behind the water break test. On the finished part, a cross-hatch adhesion test to ASTM D3359 shows whether the powder is gripping the metal.",
    "Surface contamination is the most common cause of coating adhesion failure, and it shows up later as peeling and blistering. Catching it early costs far less than recoating. Strong powder coating pretreatment also keeps results consistent from batch to batch, and the same surface preparation for powder coating standard applies to every load. We hold our metal pretreatment for powder coating to the same documented checks, and powder coating surface preparation is never signed off until the part passes them. For the blasting cleanliness grades behind these checks, read our guide to surface preparation standards, and see our certification page for details on how we work. Our metal cleaning before powder coating is part of that documented process.",
    "## See Surface Preparation in a Real Project",
    "Welded frames arrive with weld residue, forming oil and tight tolerances, which makes powder coating surface preparation critical. Our conveyor frame case study shows what a documented job looks like for a real production customer, from the incoming part to the finished coating.",
    "Read the conveyor frame for an automotive plant project to see the part, metal, size, powder, colour code and turnaround recorded for a real production job. Before and after photos show the standard we hold ourselves to, and the same documented approach applies to your parts.",
    "## Which Industries Rely on Our Surface Preparation?",
    "Fabricators, machine shops, manufacturers and contractors rely on us most. These customers need dependable industrial metal cleaning, tight masking and repeatable results that match the next batch. Our approach scales from single parts to production runs, and every customer receives the same careful treatment.",
    "See how we support metal fabricators and welding shops, where weld residue is the main concern, and machine shops, where masking protects precision features. Our powder coating surface preparation also supports our wider industrial powder coating work, our metal pretreatment for powder coating on large fabrications, and the full range of powder coating services at our Milton shop.",
    "## Get Your Parts Prepared Right",
    "Ready for a stronger finish? Send part photos and details through our quote form for powder coating surface preparation advice, or visit 10874 Steeles Ave E, Milton, Monday to Friday, 7 AM to 5 PM. Call (905) 876-7060 or email sales@koojopowdercoating.com."
  ],
  faqs: [
    {
      question: "What happens if powder coating surface preparation is skipped?",
      answer: "Oil and residue stay under the powder, so the finish can crater, peel or blister, and rust can creep in from edges. Skipping surface preparation for powder coating usually means early failure and a costly strip and redo."
    },
    {
      question: "What is the difference between iron and zinc phosphate?",
      answer: "Iron phosphate forms a light conversion layer and suits general-duty indoor parts, while the right metal pretreatment for powder coating on outdoor equipment is often zinc. Zinc phosphate forms a heavier crystalline layer that offers stronger rust resistance for demanding or outdoor service."
    },
    {
      question: "Can you mask threads and holes?",
      answer: "Yes. We plug and tape threads, bores and contact faces before coating so they stay clean and in tolerance. Mark critical features on your drawing or photos when you request a quote."
    },
    {
      question: "Is pretreatment part of the 48-hour turnaround?",
      answer: "Yes. Powder coating pretreatment, drying and coating all fit inside our standard 48-hour turnaround for typical orders. Large or complex jobs are scheduled when we quote."
    }
  ]
};

// 4. /services/specialty-custom-projects
content.services["specialty-custom-projects"] = {
  title: "Specialty Powder Coating | Koojo Custom Powder Coating",
  seo_title: "Specialty Powder Coating | Koojo Custom Powder Coating",
  seo_description: "Specialty powder coating for one-off parts, prototypes and custom metal projects. Durable finishes, 48-hour turnaround. Get a quote today.",
  primary_keyword: "specialty powder coating",
  h1: "Specialty Powder Coating for One-Off and Custom Projects",
  body: [
    "Specialty powder coating gives unusual parts, test pieces and art pieces a tough, even finish that suits the job instead of forcing it into a standard run. At Koojo Custom Powder Coating, our Milton team coats single pieces and small sets with the same care as large orders. Since 2012, we have finished more than 10,000 items for customers across the GTA, with a 48-hour turnaround on typical orders. Whether you need one-off powder coating for a sculpture or a repair, we plan every step around your part. Call (905) 876-7060, Monday to Friday, 7 AM to 5 PM, or request a specialty powder coating quote below.",
    "Since 2012 | 10,000+ Items | 48 Hr Turnaround | 5.0 ★ Google Rating",
    "## What Is Specialty Powder Coating?",
    "Specialty powder coating is a dry finishing process for unusual, one-off or custom metal parts, in which electrostatically charged powder is sprayed onto the part and heated in an oven until it cures into a hard, even layer. It suits work that does not fit a standard production run.",
    "The finish is made from thermoset powder, which cures with heat instead of drying like liquid paint. At a cure temperature of 180 to 200 °C, the powder flows, bonds to the metal and hardens into one continuous coating without runs or drips. That makes it a dependable corrosion-resistant and chip-resistant choice for parts that face weather, handling and wear. As a form of specialty metal finishing, it is often chosen where a part is hard to replace.",
    "Typical projects include one-off parts, test builds, custom fabrications and decorative metalwork, along with metal sculptures from artists and makers. Good one-off powder coating depends on planning each job from the bare metal up, so our specialty powder coating is planned around the part in front of us, not a standard recipe. Our wider powder coating services cover the full range of work we do.",
    "## Our Specialty Powder Coating Process",
    "Our specialty powder coating process has six stages: intake and inspection, cleaning and pretreatment, masking, powder application, oven curing and final inspection. Each stage is documented, so a repeat of your project matches the first piece. The same controls support our industrial powder coating work.",
    "Step 1 – Intake and Inspection: We check each part for rust, old coatings, weld seams and damage, then confirm the finish and your timing. Unusual shapes are studied first, because hanging a part so every surface can be reached is often the hardest step on a single job.",
    "Step 2 – Cleaning and Pretreatment: Parts are washed and chemically treated so the powder bonds to clean metal. Skipping this stage is a common reason finishes fail early. Parts that need old coatings removed first may suit our powder coat stripping and recoating service.",
    "Step 3 – Masking and Plugging: Threaded holes, bearing surfaces and mounting points are protected before coating. Masking and plugging keep bolts turning and parts fitting, which matters when there is only one part and no spare.",
    "Step 4 – Electrostatic Powder Application: Charged powder is applied by electrostatic spray onto the grounded part, so it wraps around tubes, corners and recesses. This helps even coverage on irregular shapes that a flat panel recipe would miss.",
    "Step 5 – Oven Curing: The part moves into the curing oven, where specialty powder coating reaches temperature and hardens. Cure time depends on the powder and the mass of the part, so a heavy casting is planned differently from a thin decorative piece.",
    "Step 6 – Final Inspection and Handoff: We inspect the cured finish for coverage, adhesion and appearance. Typical orders are ready within 48 hours, and unusual jobs are scheduled when we quote. We receive parts Monday to Friday, 7 AM to 5 PM. We also record the colour code and powder used, so a later piece can match.",
    "Our small-batch powder coating schedule keeps parts from waiting between steps, and for a tight lead time, tell us your date at quote.",
    "## Parts and Metals We Coat",
    "We apply specialty powder coating to steel, aluminum and cast parts, including test parts, brackets, decorative panels, sculptures and welded assemblies. Our capabilities page lists 6,000 lb capacity, so heavy pieces, long frames and odd shapes are all worth a quote, and we confirm fit at intake.",
    [
      "One-off parts: replacement pieces, repairs and single custom items.",
      "Prototypes: test parts and early builds that need a durable finish.",
      "Art and decor: signs, stands and powder coating for art pieces.",
      "Custom fabrications: frames, fixtures and welded builds.",
      "Small sets: a handful of matching pieces coated together."
    ],
    "Metals we handle include steel for frames and supports, aluminum for lighter pieces, and cast parts such as housings and ornaments. Good specialty powder coating on mixed metals also depends on how parts are hung, so we confirm that at intake. Our prototype powder coating starts with a material check, because the right prep and cure plan depends on the metal and the thickness of the part. Send photos and dimensions with your request, and we will tell you how your part will be coated.",
    "## Finish and Option Choices",
    "Specialty powder coating comes in gloss, satin, matte and textured finishes in many colours. We confirm the powder type, colour code and film thickness at quote, so the finish suits the part, the metal and its use. For wider palettes, see our custom powder coating colours page.",
    make_pt_table(
      ["Option", "What it gives you", "Best for"],
      [
        ["Gloss", "A smooth, high-shine look", "Display pieces, decor"],
        ["Matte or satin", "Lower glare and hides light scuffs", "Fixtures, enclosures"],
        ["Textured", "Hides small surface marks and adds grip", "Handled parts, stands"],
        ["Film thickness", "Typical film is 2 to 4 mils, confirmed on fit-critical parts", "Tight tolerances, threaded parts"],
        ["Colour match", "A RAL colour or sample matched to your piece", "Repairs and matching sets"]
      ]
    ),
    "Whatever you pick, we match the finish to how the part will live, whether that is an outdoor gate or an indoor display. For specialty powder coating that must match an existing piece, send the piece or a sample. Film thickness affects fit, so flag tight tolerances before we coat.",
    "## Quality Standards for Specialty Powder Coating",
    "Our specialty powder coating follows recognized standards: ASTM D3359 for adhesion, ASTM D7091 for dry film thickness and ASTM B117 for salt spray resistance on every order. Koojo is certified through the Absolute Bureau of Certification, and test reports are available on request.",
    "Quality starts at intake and ends at handoff. After curing, a good finish looks even in colour and gloss, with no thin spots, runs or bare edges. Edges, welds and recesses get particular attention because thin spots usually appear there. We flag any concern with you before parts leave the shop.",
    "An adhesion test checks that the coating bonds to the metal. Dry film thickness readings confirm the coating is neither too thin to protect nor too thick to fit. The salt spray test measures corrosion resistance in a controlled chamber. It is a comparison tool rather than a promise of real-world life, so we explain what results mean for your specialty powder coating order.",
    "Because a unique piece has no second chance, each part is checked before it leaves the shop. Careful finishing of a one-off piece also depends on clean prep and correct curing, so every order follows the same documented steps. Good rust protection comes from that prep and cure, not from colour alone. See our certification page for details.",
    "## Recent Project: Church Gates",
    "Our church gates show how we handle decorative metalwork that people see up close and that stays outdoors in every season. Work like this has to look right and resist weather, the same demands that a custom piece of your own will face.",
    "The case study records the part, metal, size, powder, colour and turnaround, with before and after photos. Read the church gates case study to see the standard behind our work, and expect the same documented approach on your specialty powder coating order.",
    "## Businesses and Makers That Use Specialty Powder Coating",
    "Machine shops, fabricators, artists, builders and facility managers use our specialty powder coating most. These customers want a dependable finish on parts that are unusual, hard to replace or built to order, whether they send one piece or a small matched set.",
    "See how we support powder coating for machine shops, who often send precision pieces with threads and bores that need masking, and powder coating for municipalities, who need tough finishes on custom public metalwork.",
    "## Get a Specialty Powder Coating Quote",
    "Ready to coat your next unusual piece? Send photos, dimensions and your finish choice through our quote form, or call (905) 876-7060, Monday to Friday, 7 AM to 5 PM. Visit 10874 Steeles Ave E, Milton, or contact us with questions."
  ],
  faqs: [
    {
      question: "Can you coat a single piece?",
      answer: "Yes. Our small-batch powder coating covers single pieces and small sets, from a repaired bracket to a finished sculpture. Send photos and dimensions with your request, and a project consultation at quote confirms how your part will be coated."
    },
    {
      question: "Can you coat a prototype before the design is final?",
      answer: "Yes. Prototypes often change, so tell us the metal, size and finish you expect. Coating a test part shows how the finish behaves before you commit to more."
    },
    {
      question: "When will my custom piece be ready?",
      answer: "Typical specialty powder coating orders follow our 48-hour turnaround. Large, heavy or complex jobs are scheduled at quote based on size and prep. We receive parts Monday to Friday, 7 AM to 5 PM."
    },
    {
      question: "Can you match the finish of an existing piece?",
      answer: "Yes. Send the piece or a RAL code, and we confirm the powder and colour at quote. Because colour depends on the powder and the metal, we explain any difference before coating."
    },
    {
      question: "What if my part has deep recesses or tight areas?",
      answer: "Electrostatic powder wraps around many shapes, but deep recesses can limit coverage. Tell us about hard-to-reach areas, and we plan masking and coating before we start."
    },
    {
      question: "How should I prepare a fragile or unique part for drop-off?",
      answer: "Contact us first so we can plan handling. Pack the part so coating surfaces stay clear, and tell us which areas are fit-critical. Pickup and delivery details are confirmed at quote, and drop-off at 10874 Steeles Ave E, Milton, is open Monday to Friday, 7 AM to 5 PM."
    }
  ]
};

// 5. /services (Services Hub)
content.pages["services"] = {
  title: "Powder Coating Services | Industrial to Custom | Koojo",
  seo_title: "Powder Coating Services | Industrial to Custom | Koojo",
  seo_description: "Powder coating services from one certified shop: blasting, pretreatment, custom colours, restoration and bulk work. 48 hr turnaround. Get a quote.",
  primary_keyword: "powder coating services",
  h1: "Powder Coating Services for Industry, Trade and Home",
  body: [
    "Powder coating services at Koojo Custom Powder Coating cover every step from bare metal to finished part: blasting, pretreatment, masking, spraying, curing and inspection, all under one roof. Since 2012 our full-service powder coating shop has finished more than 10,000 items.",
    "Industrial clients, trade customers and homeowners all use the same in-house prep and coating, whether the job is one bracket or a production run. Pick a service below or read on for how the work is done, what it costs to plan and how long it takes. Most standard orders leave within 48 hours, and the shop is open weekdays from 7 AM to 5 PM. Every job starts with a conversation about the part, its use and the finish you want, so the plan fits before any price is given.",
    "23 ft Oven (9 ft W x 9 ft H) · Up to 6,000 lb · 48 Hr Turnaround · In-House & Mobile Sandblasting · Since 2012 · 10,000+ Items · 5.0 ★ Google Rating",
    "## What Are Our Powder Coating Services?",
    "They are ten connected metal finishing services that take a part from rust, scale or old paint to a cured, tested finish. Some jobs need one step, others need several, and we combine them into a single order.",
    "Powder coating itself is a dry powder sprayed by electrostatic spray and hardened by oven curing, which gives protective coatings that resist chips, fading and corrosion better than many liquid paints. Around that core sit the supporting coating services: surface preparation, blasting, colour work, stripping and recoating, plus specialist work for vehicles, wheels, buildings, volume orders and one-off pieces. That one-stop finishing approach keeps quality consistent and saves you managing several suppliers, each with its own schedule, standards and paperwork.",
    "## What We Can Coat: Size, Weight and Volume",
    "Parts as long as 23 ft and as heavy as 6,000 lb fit our line, in quantities from a single piece to recurring batches. Metals include carbon steel and aluminum, structural steel, cast iron and galvanized steel.",
    make_pt_table(
      ["Capability", "Detail"],
      [
        ["Oven length", "23 ft"],
        ["Oven width x height", "9 ft x 9 ft"],
        ["Maximum part weight", "6,000 lb"],
        ["Order size", "One-off and production work"],
        ["Blasting", "In-house, plus mobile sandblasting on site"],
        ["Cure", "180–200 °C, per powder data sheet"]
      ]
    ),
    "Our service range is planned around size from the first call, so long frames and heavy bases get their own cure cycle. We handle one-off and production work on the same line, and batches of small parts can share an oven load with a larger piece in the same colour. For full limits and a fit check, see large part powder coating, which explains how big work is loaded and racked under our powder coating services.",
    "## How Our Powder Coating Services Work",
    "Every order follows the same eight steps, from checking your drawing to packing the finished parts. The steps are fixed so results stay consistent, whether we handle one service for you or all of them.",
    [
      "Inspection & Spec Review: We check each part against your drawing, confirm the finish and mark every surface that must stay bare. We also agree which of our powder coating services the part needs, so nothing is added later without your approval.",
      "Abrasive & Mobile Sandblasting: Blasting removes rust, mill scale and old coatings, in the shop or on site, leaving a clean profile the powder can grip.",
      "Cleaning & Phosphate Pretreatment: Degreasing and pretreatment prepare the metal so the powder bonds firmly, then parts are rinsed and fully dried. Pretreatment also slows corrosion under the coating if the finish is ever damaged.",
      "Masking & Plugging: Masking and plugging protect threads, mounting faces and contact points. Plugs and high-temperature tape come off after curing, leaving clean edges.",
      "Electrostatic Powder Application: Charged powder wraps around edges and into corners for even coverage, the core of our service range. Film build is kept even so colour and gloss match across every part in a batch.",
      "Oven Curing: Parts cure at 180–200 °C until the metal itself reaches temperature, so thick sections cure fully. Curing time follows the powder maker's data sheet, not guesswork.",
      "Quality Inspection & DFT Check: Quality inspection covers film thickness, adhesion, colour and coverage before release. Results are recorded, so test reports can go out with any of our coating services on request.",
      "Packaging & Shipping: Packaging and shipping protect finished faces, and the job ends with pickup or delivery. Finished faces are wrapped so they arrive exactly as they left inspection, the final step of every service."
    ],
    "## Which Service Do You Need?",
    "Match your part to a service card below. Each card links to a page with that service's full process, options and FAQs; if your job needs several, we combine them into one quote.",
    "Our powder coating services are grouped by what the part needs rather than by department, because most jobs use two or three of them together. Every service page explains when it applies and what it adds.",
    make_pt_table(
      ["Service card", "Best for", "Page"],
      [
        ["industrial powder coating", "Machinery, frames and heavy equipment", "Pillar"],
        ["powder coating surface preparation", "Degreasing, pretreatment, masking", "Service"],
        ["sandblasting services", "Rust, scale and old coatings; on-site work", "Service"],
        ["custom powder coating colours", "RAL shades, textures, metallics", "Service"],
        ["powder coat stripping and recoating", "Worn or failed finishes", "Service"],
        ["automotive powder coating", "Frames, chassis and car parts", "Service"],
        ["rim powder coating", "Wheels and rims", "Service"],
        ["architectural powder coating", "Railings, window frames, fences", "Service"],
        ["commercial powder coating", "Recurring and high-volume orders", "Service"],
        ["specialty powder coating", "Prototypes, art pieces, one-offs", "Service"]
      ]
    ),
    "Five more service cards sit on this page only, because each one is handled within a service above. Use them to find the right page fast.",
    make_pt_table(
      ["Hub-only card", "Handled by"],
      [
        ["Fence & Railing", "Architectural service"],
        ["Machinery & Equipment", "Industrial service"],
        ["Outdoor Furniture", "Custom colours, plus the outdoor furniture article"],
        ["Masking & Plugging", "Surface preparation"],
        ["Packaging & Shipping", "Included with every order"]
      ]
    ),
    "Fence and railing work, machinery and equipment, and outdoor furniture refinishing are common requests, so these service categories help visitors who search by part rather than by process.",
    "## Performance Testing and Quality Control",
    "Every finished order is checked before release, and the results are recorded against the job. The table shows each test, the method used and how often it runs, so you know what stands behind every service.",
    make_pt_table(
      ["Test", "Method", "Frequency"],
      [
        ["Film thickness (DFT)", "ASTM D7091", "Every order"],
        ["Adhesion", "ASTM D3359", "Every batch / on request"],
        ["Salt-fog exposure", "ASTM B117", "On request (outside certified testing lab)"],
        ["Visual, colour, gloss", "Approved colour code", "Every part"]
      ]
    ),
    "An outside body, the Absolute Bureau of Certification, certifies our quality system, and we can send test reports with any order. See powder coating quality assurance for the full checks behind our powder coating services. Readings are taken where coatings fail first, on edges, welds and inside corners, not only on flat faces, and any part that misses a check is corrected before it leaves.",
    "If you need readings for a supplier audit or a warranty file, ask when you order. We match the paperwork to your quality system, from a single summary to readings for each part, and keep the records so repeat orders for the same powder coating services can be checked against the first.",
    "## Industries and Parts We Coat",
    "Seven industries account for most of our work, and each has its own page showing the parts, finishes and schedules that sector needs. Pick yours to see how the work fits your sector. Fabricators and contractors send the most parts, followed by manufacturers with recurring batches and public buyers with tender work.",
    make_pt_table(
      ["Industry card", "Typical parts"],
      [
        ["powder coating for metal fabricators", "Weldments and fabrications"],
        ["powder coating for manufacturers", "Frames, guards, enclosures"],
        ["powder coating for machine shops", "Machined parts with tight tolerances"],
        ["powder coating for contractors", "Railings, steel, site equipment"],
        ["powder coating for food processing equipment", "Line frames for washdown areas"],
        ["agricultural equipment powder coating", "Field and heavy equipment"],
        ["powder coating for municipalities", "Bollards, gates, public metalwork"]
      ]
    ),
    "Each industry page lists the services that sector uses most, a matching project and the questions buyers in that field usually ask, so you can plan with the right detail before you call. If your sector is not listed, call us; coating services are not limited to these seven. Our service range adapts to new part types every month, from prototypes to replacement parts for older equipment.",
    "## Powder Coating Services vs Wet Paint vs Galvanizing",
    "Powder gives durable finishes in almost any colour, wet paint suits quick touch-ups and heat-sensitive parts, and galvanizing gives zinc protection with limited looks. The table compares all three at a glance.",
    make_pt_table(
      ["Property", "Powder coating", "Wet paint", "Galvanizing"],
      [
        ["Durability", "Hard, chip-resistant film", "Softer, more prone to chips", "Very high corrosion resistance"],
        ["Finish options", "Wide colour and texture range", "Wide colour range", "Metallic grey only"],
        ["Waste", "Little; overspray can be reclaimed", "Solvents and overspray", "Zinc bath process"]
      ]
    ),
    "For a deeper look, read powder coating vs wet paint and powder coating vs galvanizing. Galvanized steel can also be powder coated when you want both zinc protection and colour. Many customers combine methods, with zinc underneath for protection and powder on top for colour. Our coating services team can advise which route suits your part, its exposure and its budget before you commit.",
    "## Recent Projects Across Our Service Range",
    "Three recent case studies show different services at work on very different parts, from industrial prep to outdoor and restoration finishes. Each one includes specs, photos and test readings you can check.",
    make_pt_table(
      ["Project card", "Services used"],
      [
        ["Conveyor Frame for an Automotive Plant", "Industrial, sandblasting, surface preparation"],
        ["Safety Bollards", "Architectural, sandblasting, custom colours"],
        ["Church Gates", "Stripping and recoating, architectural, colours"]
      ]
    ),
    "Browse every finished job on our powder coating projects page, where you can filter by industrial, automotive, architectural and specialty work.",
    "## What Affects Cost and Lead Time",
    "Price and timing for powder coating services depend on part size, the prep needed, quantity, colour and masking. Standard orders leave two working days after drop-off, while oversized or complex jobs get their own written schedule with the quote.",
    "Heavy rust or old coatings add blasting or stripping time, while batches of matching parts spread setup costs. Special colours and detailed masking add labour. We do not list prices here, because two similar parts can need different work. For typical ranges, read our guide to powder coating cost, then ask for a written price on your own parts. Every service is priced job by job. If your deadline is fixed, say so with the request, and we will confirm in writing whether the date can be met before you book.",
    "## How to Get a Quote for Our Work",
    "Send photos, sizes, quantity, metal and the finish you want for anything in our service range, and we come back with a written price, prep plan and timeline. You can also bring parts to our Milton shop, just off Hwy 401, Monday to Friday, 7 AM to 5 PM. Use the online powder coating quote form, or phone (905) 876-7060.",
    "## Ready to Start Your Project?",
    "Tell us about your parts and we will recommend the right mix from our service range, with prep, finish options and timing in one written quote. Phone (905) 876-7060, or upload photos and measurements on the quote page. We answer weekdays between 7 AM and 5 PM."
  ],
  faqs: [
    {
      question: "How is pricing worked out?",
      answer: "By part size, prep, quantity, colour and masking. We price each order from photos and sizes, so you pay for the work your parts actually need, with no hidden extras added after the job is done."
    },
    {
      question: "What is your usual turnaround time?",
      answer: "Standard orders are ready in 48 hours from drop-off. Large or complex jobs get a written timeline before work starts."
    },
    {
      question: "Which areas do you serve?",
      answer: "Customers across the region send parts to our shop; see powder coating service areas for each city, with drive times, routes and drop-off details."
    },
    {
      question: "Can I combine several services in one order?",
      answer: "Yes. Combined orders, such as stripping, blasting and colour matching, are quoted together and run as one job."
    },
    {
      question: "Do you take one-off jobs as well as volume work?",
      answer: "Yes. All of our coating services are available for single parts and recurring batches alike, and both go through the same prep, curing and inspection as every other order."
    }
  ]
};

fs.writeFileSync("scripts/seed/uploaded_content.json", JSON.stringify(content, null, 2), "utf-8");
console.log("Updated scripts/seed/uploaded_content.json successfully!");
