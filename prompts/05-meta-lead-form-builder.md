# Prompt 05 — Meta Lead Form Builder

Use this prompt to build a Blue Horizon Meta instant lead form (or decide whether WhatsApp/website is better).

---

## Before you start
Read `knowledge/blue-horizon-detailing-master-business-knowledge.md` and `knowledge/meta-ads-operating-rules.md`.

## Prompt

```text
Build a Meta instant lead form for Blue Horizon Detailing.

Service / campaign: [e.g. Deep Clean / Paint correction / Ceramic / New car protection / General].
Goal: [lead volume / qualified enquiries / photo estimate].
Target area: [default Rugby + 20 miles / Warwickshire].

First, recommend the destination:
- Meta lead form (simple offer, volume).
- WhatsApp (photos needed or conversation qualifies better).
- Website service page or dedicated landing page (needs proof/education).
- Free estimate tool (SMART/alloy photo estimates — only once Josh asks).
Justify the choice.

If a Meta lead form is right, produce:
1. Form type (more volume vs higher intent) and recommendation.
2. Intro headline and description (premium, local tone).
3. Questions (use the standard set unless the service needs changes):
   - Full name
   - Phone number
   - Email (if needed)
   - Postcode
   - Vehicle make/model
   - Service interested in
   - Vehicle condition / notes
   - Preferred contact method
   - When would you like the work done?
4. Any qualifying / screening questions to filter out price-shoppers and out-of-area leads.
5. Privacy note placeholder (Josh to supply the privacy policy URL — do not invent one).
6. Thank-you screen copy + next step (e.g. "Josh will reply with a tailored quote" / WhatsApp button to 07818 514079).
7. Follow-up / routing note (how the lead reaches Josh).

Constraints:
- Real services, pricing, areas and proof only.
- No invented offers, discounts, warranties, timeframes or privacy URLs.
- No SMART / alloy forms unless Josh has explicitly asked. If building SMART/alloy later, use the SMART/alloy question set and prompt the customer to send photos via WhatsApp.

End with: APPROVE / REJECT / EDIT.
```

## After building
- Save the form spec alongside its campaign draft in `campaigns/drafts/`.
- Do not change any live form — Josh implements after explicit APPROVE.
