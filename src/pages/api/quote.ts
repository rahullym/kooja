import type { APIRoute } from "astro";

export const prerender = false;

export const POST: APIRoute = async ({ request }) => {
	try {
		const data = await request.json();
		const { name, email, phone, message } = data;

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

		const reference = `KQ-${Date.now().toString(36).toUpperCase()}`;

		return new Response(
			JSON.stringify({
				success: true,
				message: "Thank you! Your quote request has been received. Our team will review your specifications and respond within 1 business day.",
				reference,
			}),
			{ status: 200, headers: { "Content-Type": "application/json" } },
		);
	} catch (err: any) {
		return new Response(
			JSON.stringify({ success: false, error: "Failed to process quote request. Please try again or email us directly." }),
			{ status: 500, headers: { "Content-Type": "application/json" } },
		);
	}
};
