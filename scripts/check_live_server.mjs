const pages = [
  "/",
  "/capabilities",
  "/certification",
  "/contact-us",
  "/get-a-quote",
  "/about-us",
  "/services",
  "/services/industrial-powder-coating",
  "/services/surface-preparation",
  "/services/sandblasting",
  "/services/custom-colors-finishes",
  "/services/restoration-recoating",
  "/services/automotive-powder-coating",
  "/services/wheel-rim-powder-coating",
  "/services/specialty-custom-projects",
  "/services/architectural-coatings",
  "/services/bulk-commercial-orders",
  "/industries/food-processing-equipment",
  "/industries/agricultural-heavy-equipment",
  "/industries/contractors-construction",
  "/industries/manufacturing-automation",
  "/industries/machine-shops",
  "/industries/metal-fabricators-welding-shops",
  "/industries/municipal-institutional",
  "/locations",
  "/locations/powder-coating-milton",
  "/locations/powder-coating-oakville",
  "/locations/powder-coating-burlington",
  "/locations/powder-coating-mississauga",
  "/locations/powder-coating-halton-hills",
  "/locations/powder-coating-brampton",
  "/locations/powder-coating-guelph",
  "/locations/powder-coating-cambridge",
  "/locations/powder-coating-hamilton",
  "/projects",
  "/projects/food-processing-line-frame",
  "/projects/automation-line-frame",
  "/projects/church-gates",
  "/projects/conveyor-frame-automotive-plant",
  "/projects/robotic-base",
  "/projects/safety-bollards",
  "/blog"
];

async function check() {
  for (const page of pages) {
    try {
      const res = await fetch(`http://localhost:4321${page}`);
      const text = await res.text();
      const hasConfirm = text.includes("[confirm");
      const hasRatingPlaceholder = text.includes("add live rating");
      const hasBracket = /\[confirm[^\]]*\]/i.test(text);
      if (hasConfirm || hasRatingPlaceholder || hasBracket) {
        console.log(`❌ Page ${page} HAS PLACEHOLDERS:`);
        if (hasConfirm) console.log("  has [confirm");
        if (hasRatingPlaceholder) console.log("  has add live rating");
        const match = text.match(/\[[^\]]{3,40}\]/g);
        if (match) console.log("  Matches:", match.slice(0, 5));
      } else {
        // check table count
        const tableCount = (text.match(/<table/g) || []).length;
        console.log(`✅ ${page}: HTTP ${res.status}, tables: ${tableCount}`);
      }
    } catch (e) {
      console.log(`⚠️ ${page}: fetch failed (${e.message})`);
      break;
    }
  }
}

check();
