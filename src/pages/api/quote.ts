import type { APIRoute } from "astro";
import { Resend } from "resend";

export const prerender = false;

function escapeHtml(str: string): string {
	return str
		.replace(/&/g, "&amp;")
		.replace(/</g, "&lt;")
		.replace(/>/g, "&gt;")
		.replace(/"/g, "&quot;")
		.replace(/'/g, "&#039;");
}

export const POST: APIRoute = async ({ request }) => {
	try {
		const data = await request.json();
		const {
			name,
			email,
			phone,
			company,
			service,
			dimensions,
			quantity,
			finish,
			timeline,
			message,
		} = data;

		// 1. Validation
		if (!name || !name.trim()) {
			return new Response(
				JSON.stringify({ success: false, error: "Full Name is required." }),
				{ status: 400, headers: { "Content-Type": "application/json" } },
			);
		}

		if (!email || !email.trim()) {
			return new Response(
				JSON.stringify({ success: false, error: "Email Address is required." }),
				{ status: 400, headers: { "Content-Type": "application/json" } },
			);
		}

		const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
		if (!emailRegex.test(email.trim())) {
			return new Response(
				JSON.stringify({ success: false, error: "Please provide a valid email address." }),
				{ status: 400, headers: { "Content-Type": "application/json" } },
			);
		}

		if (!phone || !phone.trim()) {
			return new Response(
				JSON.stringify({ success: false, error: "Phone Number is required." }),
				{ status: 400, headers: { "Content-Type": "application/json" } },
			);
		}

		const digits = phone.replace(/\D/g, "");
		if (digits.length < 10) {
			return new Response(
				JSON.stringify({ success: false, error: "Please provide a valid 10-digit phone number." }),
				{ status: 400, headers: { "Content-Type": "application/json" } },
			);
		}

		if (!message || !message.trim()) {
			return new Response(
				JSON.stringify({ success: false, error: "Project details or message is required." }),
				{ status: 400, headers: { "Content-Type": "application/json" } },
			);
		}

		// 2. Reference generation
		const reference = `KQ-${Date.now().toString(36).toUpperCase()}`;

		// 3. Read Resend API Key securely server-side
		const apiKey = process.env.RESEND_API_KEY || import.meta.env.RESEND_API_KEY;

		if (!apiKey) {
			console.error("Resend API key is not configured on the server.");
			return new Response(
				JSON.stringify({
					success: false,
					error: "Email notification service is temporarily unavailable. Please call us at (905) 876-7060 or email sales@koojopowdercoating.com.",
				}),
				{ status: 500, headers: { "Content-Type": "application/json" } },
			);
		}

		// 4. Clean and prepare values
		const cleanName = name.trim();
		const cleanEmail = email.trim();
		const cleanPhone = phone.trim();
		const cleanCompany = company?.trim() || "";
		const cleanService = service?.trim() || "General Powder Coating Inquiry";
		const cleanDimensions = dimensions?.trim() || "Not specified";
		const cleanQuantity = quantity?.trim() || "Not specified";
		const cleanFinish = finish?.trim() || "Not specified";
		const cleanTimeline = timeline?.trim() || "Standard turnaround";
		const cleanMessage = message.trim();

		// 5. Build Plain-Text Email Content
		const textContent = `=====================================================
KOOJO CUSTOM POWDER COATING — NEW QUOTE REQUEST
Reference Code: ${reference}
=====================================================

CUSTOMER INFORMATION:
- Name: ${cleanName}
- Email: ${cleanEmail}
- Phone: ${cleanPhone}
- Company: ${cleanCompany || "Not specified"}

PROJECT SPECIFICATIONS:
- Service Required: ${cleanService}
- Dimensions & Weight: ${cleanDimensions}
- Quantity / Batch Size: ${cleanQuantity}
- Colour / Finish / RAL Code: ${cleanFinish}
- Needed By / Timeline: ${cleanTimeline}

PROJECT DETAILS & SPECIFICATIONS:
${cleanMessage}

-----------------------------------------------------
Reply directly to this email to respond to ${cleanName} (${cleanEmail}).
Submitted securely via koojopowdercoating.com`;

		// 6. Build Professional HTML Email Content
		const safeName = escapeHtml(cleanName);
		const safeEmail = escapeHtml(cleanEmail);
		const safePhone = escapeHtml(cleanPhone);
		const safeCompany = escapeHtml(cleanCompany);
		const safeService = escapeHtml(cleanService);
		const safeDimensions = escapeHtml(cleanDimensions);
		const safeQuantity = escapeHtml(cleanQuantity);
		const safeFinish = escapeHtml(cleanFinish);
		const safeTimeline = escapeHtml(cleanTimeline);
		const safeMessage = escapeHtml(cleanMessage).replace(/\n/g, "<br />");

		const htmlContent = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>New Quote Request — ${reference}</title>
</head>
<body style="margin: 0; padding: 24px; background-color: #f4f2ed; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #161412; line-height: 1.5;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width: 620px; margin: 0 auto; background-color: #ffffff; border: 1px solid #cfcac0; border-radius: 8px; overflow: hidden;">
    <!-- Header -->
    <tr>
      <td style="padding: 24px 32px; background-color: #161412; color: #f4f2ed;">
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0">
          <tr>
            <td>
              <span style="font-size: 20px; font-weight: 800; letter-spacing: -0.02em; text-transform: uppercase; color: #ffffff;">KOOJO</span>
              <span style="font-size: 11px; font-family: monospace; letter-spacing: 0.08em; text-transform: uppercase; color: #ff6a2b; margin-left: 8px;">CUSTOM POWDER COATING</span>
              <h1 style="margin: 8px 0 0 0; font-size: 22px; font-weight: 700; color: #ffffff;">New Quote Request</h1>
            </td>
            <td align="right" valign="top">
              <span style="display: inline-block; padding: 6px 12px; background-color: #2b2622; border: 1px solid #ff6a2b; border-radius: 4px; font-family: monospace; font-size: 12px; font-weight: bold; color: #ff6a2b;">
                ${reference}
              </span>
            </td>
          </tr>
        </table>
      </td>
    </tr>

    <!-- Body -->
    <tr>
      <td style="padding: 32px;">
        <!-- Customer Details Box -->
        <h2 style="margin: 0 0 12px 0; font-size: 13px; font-family: monospace; text-transform: uppercase; letter-spacing: 0.08em; color: #c8400a;">Customer Information</h2>
        <table role="presentation" width="100%" cellpadding="6" cellspacing="0" style="border-collapse: collapse; margin-bottom: 24px; font-size: 14px;">
          <tr style="border-bottom: 1px solid #ebe8e1;">
            <td width="35%" style="color: #5f5a54; font-weight: 600;">Name:</td>
            <td style="color: #161412; font-weight: bold;">${safeName}</td>
          </tr>
          <tr style="border-bottom: 1px solid #ebe8e1;">
            <td style="color: #5f5a54; font-weight: 600;">Email:</td>
            <td><a href="mailto:${safeEmail}" style="color: #c8400a; text-decoration: underline;">${safeEmail}</a></td>
          </tr>
          <tr style="border-bottom: 1px solid #ebe8e1;">
            <td style="color: #5f5a54; font-weight: 600;">Phone:</td>
            <td><a href="tel:${safePhone}" style="color: #161412; text-decoration: none; font-weight: 600;">${safePhone}</a></td>
          </tr>
          ${safeCompany ? `
          <tr style="border-bottom: 1px solid #ebe8e1;">
            <td style="color: #5f5a54; font-weight: 600;">Company:</td>
            <td style="color: #161412;">${safeCompany}</td>
          </tr>` : ""}
        </table>

        <!-- Specifications Box -->
        <h2 style="margin: 0 0 12px 0; font-size: 13px; font-family: monospace; text-transform: uppercase; letter-spacing: 0.08em; color: #c8400a;">Project Specifications</h2>
        <table role="presentation" width="100%" cellpadding="6" cellspacing="0" style="border-collapse: collapse; margin-bottom: 24px; font-size: 14px;">
          <tr style="border-bottom: 1px solid #ebe8e1;">
            <td width="35%" style="color: #5f5a54; font-weight: 600;">Service:</td>
            <td style="color: #161412; font-weight: 600;">${safeService}</td>
          </tr>
          <tr style="border-bottom: 1px solid #ebe8e1;">
            <td style="color: #5f5a54; font-weight: 600;">Dimensions & Weight:</td>
            <td style="color: #161412;">${safeDimensions}</td>
          </tr>
          <tr style="border-bottom: 1px solid #ebe8e1;">
            <td style="color: #5f5a54; font-weight: 600;">Quantity:</td>
            <td style="color: #161412;">${safeQuantity}</td>
          </tr>
          <tr style="border-bottom: 1px solid #ebe8e1;">
            <td style="color: #5f5a54; font-weight: 600;">Finish / RAL Code:</td>
            <td style="color: #161412;">${safeFinish}</td>
          </tr>
          <tr style="border-bottom: 1px solid #ebe8e1;">
            <td style="color: #5f5a54; font-weight: 600;">Needed By:</td>
            <td style="color: #161412;">${safeTimeline}</td>
          </tr>
        </table>

        <!-- Message Details -->
        <h2 style="margin: 0 0 12px 0; font-size: 13px; font-family: monospace; text-transform: uppercase; letter-spacing: 0.08em; color: #c8400a;">Project Details &amp; Notes</h2>
        <div style="background-color: #f8fafc; border: 1px solid #cfcac0; border-left: 4px solid #c8400a; border-radius: 4px; padding: 16px; font-size: 14px; color: #161412; line-height: 1.6; margin-bottom: 24px;">
          ${safeMessage}
        </div>

        <!-- Action Note -->
        <p style="margin: 0; padding: 12px; background-color: #ebe8e1; border-radius: 4px; font-size: 13px; color: #5f5a54; text-align: center;">
          💡 <strong>Tip:</strong> You can hit <strong>Reply</strong> in your email app to write directly to <strong>${safeName}</strong> at <strong>${safeEmail}</strong>.
        </p>
      </td>
    </tr>

    <!-- Footer -->
    <tr>
      <td style="padding: 16px 32px; background-color: #ebe8e1; border-top: 1px solid #cfcac0; text-align: center; font-size: 12px; color: #5f5a54;">
        Koojo Custom Powder Coating · 10874 Steeles Ave E, Milton, ON L9T 2X8 · (905) 876-7060<br>
        Submitted via <a href="https://www.koojopowdercoating.com" style="color: #c8400a; text-decoration: none;">koojopowdercoating.com</a>
      </td>
    </tr>
  </table>
</body>
</html>`;

		// 7. Dispatch Email via Resend
		const resend = new Resend(apiKey);

		const emailSubject = cleanCompany
			? `New Quote Request [${reference}] — ${cleanName} (${cleanCompany})`
			: `New Quote Request [${reference}] — ${cleanName}`;

		const { data: resendData, error: resendError } = await resend.emails.send({
			from: "Koojo Powder Coating <notifications@koojopowdercoating.com>",
			to: "sales@koojopowdercoating.com",
			replyTo: cleanEmail,
			subject: emailSubject,
			text: textContent,
			html: htmlContent,
		});

		if (resendError) {
			console.error("Resend API error:", resendError.message);
			return new Response(
				JSON.stringify({
					success: false,
					error: "We could not deliver your request right now. Please email sales@koojopowdercoating.com or call (905) 876-7060.",
				}),
				{ status: 502, headers: { "Content-Type": "application/json" } },
			);
		}

		// 8. Return success
		return new Response(
			JSON.stringify({
				success: true,
				message: "Thank you! Your quote request has been received. Our team will review your specifications and respond within 1 business day.",
				reference,
				id: resendData?.id,
			}),
			{ status: 200, headers: { "Content-Type": "application/json" } },
		);
	} catch (err: any) {
		console.error("Unexpected error in /api/quote:", err?.message || err);
		return new Response(
			JSON.stringify({
				success: false,
				error: "Failed to process quote request. Please try again or email us directly.",
			}),
			{ status: 500, headers: { "Content-Type": "application/json" } },
		);
	}
};
