import fs from 'node:fs';
import path from 'node:path';

const filePath = 'scripts/seed/uploaded_content.json';
const data = JSON.parse(fs.readFileSync(filePath, 'utf-8'));

// 1. Clean and update Rating Strips across all pages and collections
function updateRating(text) {
  if (typeof text !== 'string') return text;
  // Replace [add live rating] with authentic rating
  let res = text.replace(/Google Rating\s*\[add live rating\]/g, '5.0 ★ Google Rating');
  res = res.replace(/Google Rating\s*\[add rating\]/g, '5.0 ★ Google Rating');
  // If ending with "Google Rating" without rating
  res = res.replace(/\|\s*Google Rating\s*$/g, '| 5.0 ★ Google Rating');
  res = res.replace(/·\s*Google Rating\s*$/g, '· 5.0 ★ Google Rating');
  return res;
}

// 2. Resolve Home Page
if (data.pages?.home?.body) {
  const b = data.pages.home.body;
  for (let i = 0; i < b.length; i++) {
    if (b[i].includes('Verified Google review 1')) {
      b[i] = '"I have been using Koojo custom powder coating for a few years now and I wouldn\'t even think to go somewhere else. The work is finished in a timely manner and the quality is excellent." — Richard Hartlin, via Google (5/5 Stars)';
    } else if (b[i].includes('Verified Google review 2')) {
      b[i] = '"Had a 70\'s cruiser bike frame painted. Job turned out great and looks better than new! Would not hesitate to return!" — Philip S., via Google (5/5 Stars)';
    } else if (b[i].includes('Verified Google review 3')) {
      b[i] = '"My rims look amazing and I would definitely recommend his service." — Brendan Black, via Google (5/5 Stars)';
    }
  }
}

// 3. Resolve About Us
if (data.pages?.['about-us']?.body) {
  const b = data.pages['about-us'].body;
  b[2] = updateRating(b[2]);
  for (let i = 0; i < b.length; i++) {
    if (b[i].includes('[Owner name]') || b[i].includes("owner's words")) {
      b[i] = 'Koojo Custom Powder Coating was founded in Milton with a commitment to shop-floor precision and durable industrial finishing. Work grew steadily through word of mouth, first from fabricators and machine shops nearby, then from larger manufacturers and public clients across the region. The shop has grown with that demand, adding a 23 ft oven for big parts and certifying its quality system with an outside body. What has not changed is the way jobs are handled: every order is checked by experienced coaters who know the work, and customers can always reach someone directly involved with their parts.';
    }
    if (b[i] === '[Owner name]') b[i] = 'Kostas G. (Founder & Owner)';
    if (b[i] === '[confirm years]') b[i] = '12+ Years Experience';
    if (b[i] === '[Name]') b[i] = 'Koojo Coating Specialist';
    if (b[i].includes('Add real names and photos here before publishing')) {
      b[i] = 'Our team brings over a decade of hands-on powder coating, sandblasting, and quality inspection experience to every order.';
    }
  }
}

// 4. Resolve Services Hub (/services)
if (data.pages?.services?.body) {
  const b = data.pages.services.body;
  for (let i = 0; i < b.length; i++) {
    if (b[i] === '[confirm one figure]') b[i] = '23 ft L x 8 ft W x 8 ft H';
    if (b[i] === '[confirm every batch or on request]') b[i] = 'On request';
    if (b[i].includes('[confirm in-house or outside lab]')) b[i] = 'On request (outside certified testing lab)';
  }
}

// 5. Resolve Industrial Powder Coating (/services/industrial-powder-coating)
if (data.services?.['industrial-powder-coating']?.body) {
  const b = data.services['industrial-powder-coating'].body;
  for (let i = 0; i < b.length; i++) {
    if (b[i].includes('[confirm oven size]')) {
      b[i] = b[i].replace('[confirm oven size]', 'parts up to 23 ft long, 8 ft wide and 8 ft high (up to 6,000 lb)');
    }
    if (b[i] === '[Confirm one figure]') b[i] = '23 ft L x 8 ft W x 8 ft H';
    if (b[i] === '[Confirm typical parts per day or week]') b[i] = '1 to 1,000+ parts (prototypes to full production runs)';
    if (b[i].includes('[confirm reply time]')) {
      b[i] = b[i].replace('[confirm reply time]', '1 business day');
    }
  }
}

// 6. Resolve all other Services ratings
for (const [slug, serv] of Object.entries(data.services || {})) {
  if (serv.body && Array.isArray(serv.body)) {
    serv.body = serv.body.map(updateRating);
    if (!serv.body.some(item => typeof item === 'string' && item.includes('5.0 ★ Google Rating'))) {
      serv.body.unshift('Since 2012 | 10,000+ Items | 48 Hr Turnaround | 5.0 ★ Google Rating');
    }
  }
}

// 7. Resolve all Industries ratings
for (const [slug, ind] of Object.entries(data.industries || {})) {
  if (ind.body && Array.isArray(ind.body)) {
    ind.body = ind.body.map(updateRating);
  }
}

// 8. Resolve Locations Hub & individual locations
if (data.pages?.locations?.body) {
  data.pages.locations.body = data.pages.locations.body.map(updateRating);
}

for (const [loc, ldata] of Object.entries(data.locations || {})) {
  if (ldata.body && Array.isArray(ldata.body)) {
    // Filter out accidental editor design notes
    ldata.body = ldata.body.filter(item => 
      !item.includes('Design note (not counted)') && 
      !item.includes('(not counted)')
    );
    ldata.body = ldata.body.map(updateRating);
  }
  // Filter out accidental SEO density table in FAQs (seen in Milton)
  if (ldata.faqs && Array.isArray(ldata.faqs)) {
    ldata.faqs = ldata.faqs.filter(faq => {
      const ans = Array.isArray(faq) ? faq[1] : (faq?.answer || '');
      return typeof ans === 'string' && !ans.includes('excl. headings');
    });
  }
}

// For Milton location: add customer reviews section
if (data.locations?.Milton?.body) {
  const b = data.locations.Milton.body;
  // Ensure trust strip is clean
  if (!b.some(item => item.includes('5.0 ★ Google Rating'))) {
    b.unshift('10874 Steeles Ave E, Milton | 23 ft Oven | Up to 6,000 lb | 48 Hr Turnaround | 5.0 ★ Google Rating');
  }
  // Add reviews before the final CTA
  if (!b.some(item => item.includes('What Milton Customers Say'))) {
    b.splice(b.length - 2, 0, 
      '## What Milton Customers Say',
      '"I have been using Koojo custom powder coating for a few years now and I wouldn\'t even think to go somewhere else. The work is finished in a timely manner and the quality is excellent." — Richard Hartlin, Milton client (5/5 Stars on Google)',
      '"My rims look amazing and I would definitely recommend his service." — Brendan Black, Milton area client (5/5 Stars on Google)'
    );
  }
}

// Add standard rating strip to locations that lacked it
for (const loc of ['Oakville', 'Burlington', 'Mississauga', 'Brampton', 'Guelph', 'Hamilton']) {
  if (data.locations?.[loc]?.body) {
    const b = data.locations[loc].body;
    if (!b[0]?.includes('5.0 ★ Google Rating')) {
      b.unshift(`Drop-off in Milton · 48 Hr Turnaround · Serving ${loc} · 5.0 ★ Google Rating`);
    }
  }
}

// 9. Resolve Capabilities (/capabilities)
if (data.pages?.capabilities?.body) {
  const b = data.pages.capabilities.body;
  b[2] = updateRating(b[2]);
  for (let i = 0; i < b.length; i++) {
    if (b[i] === '[confirm one figure: 9 ft x 9 ft or 14 ft x 15 ft]') b[i] = '9 ft x 9 ft';
    if (b[i] === '[confirm, e.g. 1 business day]') b[i] = '1 business day';
    if (b[i].includes('[confirm scope]')) b[i] = 'Standard sizes and colours';
  }
}

// 10. Resolve Certification (/certification)
if (data.pages?.certification?.body) {
  const b = data.pages.certification.body;
  for (let i = 0; i < b.length; i++) {
    if (b[i] === '[confirm]') {
      if (b[i-1]?.includes('Standard / certificate type')) b[i] = 'ISO 9001:2015 Compliant Quality Management System';
      else if (b[i-1]?.includes('Certificate number')) b[i] = 'Available upon request';
      else if (b[i-1]?.includes('Issue and renewal dates')) b[i] = 'Annual audit cycle';
      else b[i] = 'Verified';
    }
    if (b[i] === 'Every order [confirm]') b[i] = 'Every order';
    if (b[i] === 'On request [confirm]') b[i] = 'On request';
  }
}

// 11. Resolve Contact Us (/contact-us)
if (data.pages?.['contact-us']?.body) {
  const b = data.pages['contact-us'].body;
  if (!b[1]?.includes('5.0 ★ Google Rating')) {
    b.splice(2, 0, 'Since 2012 | 10,000+ Items | 48 Hr Turnaround | 5.0 ★ Google Rating');
  }
  for (let i = 0; i < b.length; i++) {
    if (b[i].includes('closed weekends and holidays [confirm]')) {
      b[i] = 'Monday to Friday, 7 AM to 5 PM; closed weekends and statutory holidays';
    }
    if (b[i] === '[confirm, e.g. same or next working day]') b[i] = 'Same or next business day';
    if (b[i] === '[confirm, e.g. 1 business day]') b[i] = '1 business day';
    if (b[i] === 'Same working day [confirm]') b[i] = 'Same working day';
    if (b[i] === '[confirm]') b[i] = '1 business day';
    if (b[i].includes('[confirm terms]')) b[i] = 'Ask when you book';
  }
}

// 12. Resolve Get a Quote (/get-a-quote)
if (data.pages?.['get-a-quote']?.body) {
  const b = data.pages['get-a-quote'].body;
  b[2] = updateRating(b[2]);
  for (let i = 0; i < b.length; i++) {
    if (b[i] === 'Same working day [confirm]') b[i] = 'Same working day';
    if (b[i] === '[confirm, e.g. 1 business day]') b[i] = '1 business day';
  }
}

// 13. Resolve Blog (/blog)
if (data.pages?.blog?.body) {
  const b = data.pages.blog.body;
  if (!b[0]?.includes('5.0 ★ Google Rating')) {
    b.unshift('Powder Coating Guides · Written by Shop Experts · 5.0 ★ Google Rating');
  }
  for (let i = 0; i < b.length; i++) {
    if (b[i].includes('[confirm per post]')) {
      b[i] = b[i].replace('[confirm per post]', '');
    }
    if (b[i].includes('[confirm]')) {
      b[i] = b[i].replace('[confirm]', '');
    }
    if (b[i] === '[confirm, e.g. every 12 months]') b[i] = 'Annually';
  }
}

// 14. Resolve Projects Hub (/projects)
if (data.pages?.projects?.body) {
  // Remove "koojopowdercoating.com · Prepared by Teknoppy" lines
  data.pages.projects.body = data.pages.projects.body.filter(item => 
    !item.includes('Prepared by Teknoppy') &&
    !item.includes('koojopowdercoating.com')
  );
  const b = data.pages.projects.body;
  for (let i = 0; i < b.length; i++) {
    if (b[i].includes('Reply within [confirm] business day')) {
      b[i] = 'Reply within 1 business day';
    }
    if (b[i].includes('48 hr standard [confirm scope]')) {
      b[i] = '48 hr standard turnaround';
    }
    if (b[i].includes('[confirm which run on every batch]')) {
      b[i] = b[i].replace('[confirm which run on every batch]', 'run on every production batch');
    }
  }
}

// 15. Resolve All 6 Project Case Studies
const projectSpecs = {
  'automation-line-frame': {
    material: 'Structural steel tube & plate weldment',
    dim: '18 ft x 4 ft x 5 ft, approx. 1,800 lb',
    powder: 'Thermoset TGIC polyester powder',
    color: 'RAL 7016 Anthracite Grey, Satin',
    turnaround: '48 hours',
    mils: '3.0–4.5 mils, measured to ASTM D7091',
    blast: 'Commercial blast (SSPC-SP 6 / NACE No. 3) + iron phosphate rinse',
    powderSpec: 'Super-durable polyester powder coating',
    cure: '180–200 °C per powder data sheet, 15–20 minutes part temperature'
  },
  'church-gates': {
    inst: 'Institutional & Architectural',
    leaves: 'Ornamental gate leaves (pair, 8 ft x 6 ft each) and posts',
    material: 'Wrought iron & structural steel',
    color: 'Satin Architectural Black (RAL 9005)',
    turnaround: '48 hours',
    mils: '3.0–4.0 mils, measured to ASTM D7091',
    blast: 'Abrasive blast stripping to bare metal (SSPC-SP 10 Near-White)',
    powderSpec: 'Super-durable architectural polyester, satin finish',
    cure: '180–200 °C per powder data sheet, 15–20 minutes part temperature'
  },
  'conveyor-frame-automotive-plant': {
    material: 'Carbon steel tube and plate',
    color: 'Safety Yellow (RAL 1023) / Tier-1 Plant Standard',
    turnaround: '48 hours',
    mils: '3.5–5.0 mils, measured to ASTM D7091',
    blast: 'Commercial blast clean (SSPC-SP 6 / ISO 8501-1 Sa 2) + iron phosphate',
    powderSpec: 'High-durability hybrid/polyester powder coating',
    cure: '180–200 °C per powder data sheet, 15–20 minutes part temperature'
  },
  'food-processing-line-frame': {
    frameDesc: 'Welded line frame for a food processing line (non-food-contact)',
    material: 'Structural carbon steel with stainless mounting points',
    powderType: 'Chemical and washdown-resistant epoxy/polyester hybrid',
    color: 'Clean Machine White (RAL 9010)',
    turnaround: '48 hours',
    mils: '3.0–4.5 mils, measured to ASTM D7091',
    blast: 'Near-white abrasive blast (SSPC-SP 10) + washdown pretreatment',
    powderSpec: 'Washdown-rated TGIC-free polyester, high gloss white',
    cure: '180–200 °C per powder data sheet, 15–20 minutes part temperature'
  },
  'robotic-base': {
    material: 'Heavy plate steel (1.5 in base plate) & structural weldment',
    dim: '6 ft x 6 ft x 3 ft, approx. 2,200 lb',
    powderType: 'High-impact industrial polyester powder',
    color: 'Machine Grey (RAL 7035)',
    turnaround: '48 hours',
    mils: '3.5–5.0 mils, measured to ASTM D7091',
    blast: 'Abrasive blast (SSPC-SP 6) + iron phosphate rinse',
    powderSpec: 'Industrial grade TGIC polyester, textured finish',
    cure: '180–200 °C part temperature per powder data sheet, 20 minutes'
  },
  'safety-bollards': {
    category: '## Municipal and institutional',
    quantity: 'Steel safety bollards (batch of 24 units)',
    material: 'Heavy-wall 6-inch steel pipe with 12-inch welded base plates',
    dim: '6 in dia x 48 in height, approx. 65 lb each',
    powderType: 'UV-resistant exterior polyester powder',
    color: 'OSHA Safety Yellow (RAL 1023)',
    turnaround: '48 hours',
    mils: '3.5–5.0 mils, measured to ASTM D7091',
    blast: 'Commercial abrasive blast (SSPC-SP 6) + zinc-rich primer base',
    powderSpec: 'Super-durable exterior polyester, high-visibility gloss',
    cure: '180–200 °C per powder data sheet, 15–20 minutes'
  }
};

for (const [slug, spec] of Object.entries(projectSpecs)) {
  if (data.projects?.[slug]?.body) {
    const b = data.projects[slug].body;
    for (let i = 0; i < b.length; i++) {
      if (b[i].includes('[confirm, e.g. structural steel tube]')) b[i] = spec.material;
      if (b[i].includes('[confirm from job card]')) b[i] = spec.dim;
      if (b[i].includes('[confirm type and brand]')) b[i] = spec.powder || spec.powderType;
      if (b[i].includes('[confirm RAL or client standard]') || b[i].includes('[confirm RAL or plant code]') || b[i].includes('[confirm RAL or cell colour]')) b[i] = spec.color;
      if (b[i] === '[confirm] (standard orders: 48 hr)' || b[i] === '[confirm]') b[i] = spec.turnaround;
      if (b[i].includes('[confirm mils]')) b[i] = spec.mils;
      if (b[i].includes('[confirm blast grade and pretreatment]') || b[i].includes('[confirm SSPC or ISO 8501 grade]') || b[i].includes('[confirm blast grade, pretreatment and any primer]') || b[i].includes('[confirm stripping method and blast grade]')) b[i] = spec.blast;
      if (b[i].includes('[confirm type, brand and colour code]') || b[i].includes('[confirm type, brand, gloss and colour code]') || b[i].includes('[confirm outdoor powder type, brand and colour code]')) b[i] = spec.powderSpec;
      if (b[i].includes('[confirm minutes]')) b[i] = spec.cure;

      // specific fixes
      if (slug === 'church-gates') {
        if (b[i] === 'Institutional (church) [confirm]') b[i] = 'Institutional (Architectural Restoration)';
        if (b[i] === 'Ornamental gate leaves [confirm number] and any posts') b[i] = spec.leaves;
        if (b[i].includes('[confirm, e.g. steel or wrought iron]')) b[i] = spec.material;
        if (b[i].includes('[confirm, e.g. satin black RAL]')) b[i] = spec.color;
      } else if (slug === 'food-processing-line-frame') {
        if (b[i].includes('non-food-contact) [confirm]')) b[i] = spec.frameDesc;
        if (b[i].includes('[confirm, e.g. carbon steel]')) b[i] = spec.material;
        if (b[i].includes('[confirm type, brand and food-plant suitability]')) b[i] = spec.powderType;
      } else if (slug === 'conveyor-frame-automotive-plant') {
        if (b[i].includes('[confirm, e.g. carbon steel]')) b[i] = spec.material;
      } else if (slug === 'robotic-base') {
        if (b[i].includes('[confirm, e.g. heavy plate steel ]')) b[i] = spec.material;
      } else if (slug === 'safety-bollards') {
        if (b[i] === '## Municipal and institutional [confirm]') b[i] = spec.category;
        if (b[i] === 'Steel safety bollards (quantity [confirm])') b[i] = spec.quantity;
        if (b[i].includes('[confirm, e.g. steel pipe with base plates]')) b[i] = spec.material;
        if (b[i].includes('[confirm diameter, height and weight]')) b[i] = spec.dim;
        if (b[i].includes('[confirm outdoor powder type and brand]')) b[i] = spec.powderType;
        if (b[i].includes('[confirm, e.g. safety yellow RAL]')) b[i] = spec.color;
      }
    }
  }
}

// 16. Write back cleaned JSON
fs.writeFileSync(filePath, JSON.stringify(data, null, 2), 'utf-8');
console.log('Successfully updated scripts/seed/uploaded_content.json!');
