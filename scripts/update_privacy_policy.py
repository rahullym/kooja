import json

def block(text, style="normal", list_item=None):
    b = {
        "_type": "block",
        "style": style,
        "markDefs": [],
        "children": [
            {
                "_type": "span",
                "text": text,
                "marks": []
            }
        ]
    }
    if list_item:
        b["listItem"] = list_item
        b["level"] = 1
    return b

privacy_blocks = [
    block("Koojo Custom Powder Coating respects your privacy. This policy explains what personal information we collect when you use koojopowdercoating.com, request a quote or contact our shop, how we use it, and the choices you have. It covers our website and enquiries made by phone or email."),
    block("Who We Are", "h2"),
    block("Koojo Custom Powder Coating is a powder coating shop at 10874 Steeles Ave E, Milton, ON L9T 2X8, serving customers across the Greater Toronto Area since 2012. We are responsible for the personal information we collect, and we handle it in line with Canada’s Personal Information Protection and Electronic Documents Act (PIPEDA)."),
    block("Information We Collect", "h2"),
    block("We collect only what we need to answer you and quote your project. When you use our Get a Quote form, call us or send an email, that can include:"),
    block("Contact details: your name, email address and phone number.", list_item="bullet"),
    block("Project details: the message you send, including part descriptions, sizes, quantities and any photos or drawings you choose to share.", list_item="bullet"),
    block("Technical data: basic information such as browser type, device and pages visited, collected through our website platform as described under Cookies.", list_item="bullet"),
    block("Please do not send us sensitive personal information, such as financial account or government ID numbers. We do not need it to quote or coat your parts."),
    block("How We Use Your Information", "h2"),
    block("We use your information to respond to enquiries and provide quotes, and for the purposes below:"),
    block("Communicate with you about your project, timing, pickup and delivery.", list_item="bullet"),
    block("Keep business and job records and meet our legal and tax obligations.", list_item="bullet"),
    block("Improve our customer service and the way our website works.", list_item="bullet"),
    block("We do not send marketing emails without your consent, and we will never use your information for a purpose you would not reasonably expect."),
    block("Who We Share It With", "h2"),
    block("We do not sell or rent your personal information, and we do not share it with third parties except where this is needed to fulfil your request or is required by law."),
    block("Service providers that help us run the business, such as our website platform and email provider, may handle information on our behalf. They may store or process it outside Canada, including in the United States, where it can be accessed by courts and authorities under local law. We require these providers to protect it appropriately."),
    block("Cookies and Website Analytics", "h2"),
    block("Our website uses cookies and similar technologies to load pages securely and keep the site working properly. We may also use basic analytics to see how many people visit and which pages they read. You can block or delete cookies in your browser settings, although some parts of the site may not function as expected if you do."),
    block("How Long We Keep It and How We Protect It", "h2"),
    block("We keep quote requests and job records only as long as needed to respond, complete your order and meet our business, tax and legal obligations, and then delete or anonymise them."),
    block("We use reasonable physical, technical and organisational safeguards, and we limit access to staff who need it. No method of transmission or storage over the internet is completely secure, so we cannot guarantee absolute security."),
    block("Your Choices and Rights", "h2"),
    block("You can ask to see the personal information we hold about you, ask us to correct it, or withdraw your consent to our using it, subject to legal and contractual limits. Email sales@koojopowdercoating.com or call (905) 876-7060, and we will reply promptly."),
    block("If you are not satisfied with our response, you can contact the Office of the Privacy Commissioner of Canada at priv.gc.ca."),
    block("Other Websites, Children and Changes to This Policy", "h2"),
    block("Our site may link to other websites, such as Google Maps or our Google Business Profile. We do not control their privacy practices, so please read their policies."),
    block("Our website and services are intended for businesses and adults, and we do not knowingly collect personal information from children."),
    block("We may update this policy from time to time. The date at the top of this page shows when it was last revised, and continued use of the site after an update means you accept the revised policy."),
    block("Contact Us About Privacy", "h2"),
    block("Questions about this policy or your information? Contact Koojo Custom Powder Coating at 10874 Steeles Ave E, Milton, ON L9T 2X8. Phone (905) 876-7060, Monday to Friday, 7 AM to 5 PM. Email sales@koojopowdercoating.com. You can also use our Contact Us page or request a quote.")
]

# Assign unique keys
for i, b in enumerate(privacy_blocks):
    b["_key"] = f"priv_b_{i+1}"
    for j, c in enumerate(b["children"]):
        c["_key"] = f"priv_s_{i+1}_{j+1}"

with open("scripts/seed/wix-privacy-policy.json", "w", encoding="utf-8") as f:
    json.dump(privacy_blocks, f, indent=2, ensure_ascii=False)

print("Updated wix-privacy-policy.json with 2026 blueprint content!")
