# Blue Horizon Detailing — Meta Ads Operating Rules

This file is the Meta-specific operating layer. It sits on top of the master business knowledge file:

`knowledge/blue-horizon-detailing-master-business-knowledge.md`

Always read the master knowledge file first. If anything here conflicts with the master file, the master file wins for business facts (services, pricing, areas, proof, brand voice). This file governs *how Meta Ads work is run and approved*.

---

## 1. Scope and guardrails

- This repo and these rules cover **Meta Ads only** (Facebook + Instagram). Do not create Google Ads files or plans here.
- This repo is for **Blue Horizon Detailing only**.
- Never store API keys, access tokens, OAuth secrets, Meta tokens, pixel secrets or any credentials in this repo. Credentials stay in Claude/connector settings.

### Never do without Josh's explicit approval
- Publish, launch or activate a campaign, ad set or ad.
- Pause or delete a campaign, ad set or ad.
- Increase, decrease or reallocate budget.
- Change billing or payment settings.
- Change the pixel, dataset, conversions API or any tracking.
- Change live lead forms or landing pages.
- Advertise a discount or offer Josh has not approved.
- Draft or launch **SMART repair** or **alloy refurbishment** ads (live from 1 July 2026, ad-hold until Josh explicitly asks).
- Target outside the agreed service area.

### Always
- Present every meaningful action as **APPROVE / REJECT / EDIT**.
- Use exact service names and prices from the master file.
- Keep the brand premium, local and high-quality.
- Justify the lead destination (WhatsApp / Meta lead form / website / landing page).
- Ask Josh for the specific video before building any video ad.

---

## 2. Approval format

Every recommendation uses this structure:

```text
RECOMMENDATION:
[What should be done]

WHY:
[Reasoning]

RISK:
[Risk or uncertainty]

EXACT CHANGE:
[Specific copy, budget, targeting, creative, audience or destination change]

STATUS:
APPROVE / REJECT / EDIT
```

---

## 3. Campaign draft output format

When drafting a Meta campaign, always output these 14 sections in order:

1. Campaign objective
2. Campaign name (see naming convention)
3. Budget
4. Ad set structure
5. Audience/location targeting
6. Placement recommendation
7. Creative assets needed
8. Primary text options
9. Headline options
10. Description options
11. CTA
12. Destination recommendation: WhatsApp / Meta lead form / website landing page
13. Risks and assumptions
14. APPROVE / REJECT / EDIT

---

## 4. Objectives and campaign types

Available Meta campaign types for Blue Horizon:
- Local lead generation (instant lead form).
- WhatsApp message campaign.
- Website traffic / conversions (only if tracking is solid).
- Retargeting website visitors / form abandoners.
- Video views for proof/awareness.
- Before/after carousel.
- Service-specific lead campaign.
- Seasonal campaign (e.g. convertible soft top spring/summer).

### Short-term priority order
1. Valeting / Deep Cleans.
2. Detailing / Paint Correction / Ceramic packages.
3. Business-wide local awareness/proof.
4. Meta proof-based local lead campaign.
5. SMART/alloy — only when Josh explicitly asks after launch readiness.

---

## 5. Budget rules

- Suggested Meta start: **£5/day** for the local proof/lead campaign.
- Do not split too many campaigns at £5/day too early — data will be too thin.
- If a campaign cannot collect enough data, recommend consolidation.
- Move budget based on **qualified leads and booked jobs**, not clicks alone.
- Never increase budget without Josh's explicit approval.

---

## 6. Targeting rules

- Target **Rugby + 20 miles**, **Warwickshire**, and selected high-value surrounding areas.
- Do not target nationally or the whole UK.
- Meta can use slightly wider local coverage than Google, with creative focused on Warwickshire premium vehicle care.
- For high-ticket services (paint correction, ceramic, new car protection, and later SMART/alloy), prioritise high-revenue areas: Leamington Spa, Warwick, Kenilworth, Solihull, Balsall Common, Dunchurch, Southam, Stratford-upon-Avon, Rugby prestige areas.

---

## 7. Creative rules

### Static / image ads
- Prioritise higher-end vehicle proof assets (Lamborghini, Rolls-Royce, Bentley, Range Rover, Defender, Porsche, BMW, Mercedes, Audi RS/AMG, Tesla).
- Clean, premium visuals. Avoid cluttered graphics.
- Direct, quality-led copy.

### Before/after
- Use real Blue Horizon results from the master file's proof list.
- Strong for deep clean interiors, paint correction, alloy and SMART (SMART/alloy on ad-hold).

### Video ads
- Josh provides the specific video per campaign.
- Build the ad around the video's real content — do not assume contents.
- If context is unclear, ask Josh for: hook, vehicle, service, transformation, desired CTA.
- Match angle to footage: process video → process/proof angle; transformation → before/after hook; water beading → ceramic protection; Josh working → trust/founder/local angle.

### Copy guardrails
- Use review proof accurately: **4.8-star Google rating**, **50+ Google reviews**. Never claim 5.0 or hundreds of reviews. Never invent review quotes or names.
- No "cheap", "cheapest", "budget", "bargain", "discount detailing", "lowest price".
- No "today only", "hurry now", "crazy offer", "miracle result".
- No guaranteed showroom finish for every car, no guaranteed scratch removal before assessment.
- No invented offers, finance, warranties, or timeframes.

---

## 8. Lead destination decision

Choose and justify one of: Meta instant lead form / WhatsApp / website service page / dedicated landing page / free estimate tool.

Decision rules:
- **Meta lead form** — simple offer, goal is volume of local leads.
- **WhatsApp** — photos needed or a conversation qualifies the lead better (strong for SMART/alloy photo estimates once live).
- **Website service page** — existing page is strong enough and the service needs proof/education.
- **Dedicated landing page** — high-value campaigns or time-limited approved offers.
- **Free estimate tool** — SMART/alloy photo-estimate journeys (when those campaigns are live).

Key pages:
- Valeting: https://www.bluehorizondetailing.com/services/valeting-services
- Detailing: https://www.bluehorizondetailing.com/services/detailing-services
- SMART repairs: https://www.bluehorizondetailing.com/smart-repairs
- Alloy refurb: https://www.bluehorizondetailing.com/alloy-wheel-repairs-refurbishment
- Headlight restoration: https://www.bluehorizondetailing.com/services/headlight-restoration
- Convertible soft top: https://www.bluehorizondetailing.com/services/convertible-soft-top
- Free estimate tool: https://www.bluehorizondetailing.com/free-estimate
- Homepage / brand: https://www.bluehorizondetailing.com/

WhatsApp / phone: **07818 514079**

---

## 9. Meta lead form questions

### General Blue Horizon leads
- Full name
- Phone number
- Email (if needed)
- Postcode
- Vehicle make/model
- Service interested in
- Vehicle condition / notes
- Preferred contact method
- When would you like the work done?

### SMART / alloy leads (only once Josh asks)
- Full name
- Phone number
- Postcode
- Vehicle make/model
- Type of damage
- Number of damaged areas/wheels
- Prompt to send photos via WhatsApp for an accurate quote

---

## 10. Naming convention

```text
BH | Meta Leads | Deep Clean Proof | Rugby+20 | 2026-07
BH | Meta Leads | Ceramic Protection | High Value Areas | 2026-07
BH | Meta Messages | Paint Correction Video | Warwickshire | 2026-07
BH | Meta Leads | SMART Photo Estimate | Rugby+20 | 2026-07
BH | Meta Retargeting | Website Visitors | All Services | 2026-07
```

Pattern: `BH | Meta <Type> | <Angle/Service> | <Area> | <YYYY-MM>`

---

## 11. Weekly optimisation checks

Each week review: spend, reach, frequency, CTR, CPC, leads, cost per lead, lead quality, creative fatigue, hook performance, comment/message sentiment, form completion rate, landing-page click-through, which service angle produces qualified enquiries, whether creative needs refreshing.

Recommend (always as APPROVE / REJECT / EDIT): pause weak ads, new creative variations, test different first 3 seconds, test WhatsApp vs lead form, test premium-vehicle image vs before/after, test deep clean vs ceramic vs paint correction angle, budget shifts (approval required).

Save weekly reports → `reports/weekly/`. Monthly reports → `reports/monthly/`.

---

## 12. Lead quality scoring

Ask Josh to score leads if not tracked automatically: good lead, poor lead, no response, booked job, quoted but not booked, out of area, price shopper, wrong service, spam.

Optimise for **booked jobs and qualified enquiries**, not cheap leads.
