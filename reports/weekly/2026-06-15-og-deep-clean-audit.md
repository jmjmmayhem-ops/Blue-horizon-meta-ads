# OG Deep Clean — Full Campaign Audit & Optimisation Plan

**Date:** 2026-06-15
**Prepared by:** Claude (Meta Ads operator)
**Account:** 761087688736713 (Bluehorizondetailing – Ad account)
**Status:** Read-only analysis. No live changes made. All actions presented as APPROVE / REJECT / EDIT.

---

## 0. Campaign identification (resolved)

The campaign you call "OG Deep Clean" is stored in Meta as:

- **Campaign:** `{BHD} - Valeting Campaign` — ID `120244204180640294`
- **Ad set:** `ADV+ - 621K Aud` — ID `120244204180660294`
- **Ad:** `OG deep clean creative` — ID `120244204180650294`
- **Creative:** ID `1634762737574376` — "FREE 3-Month Ceramic Sealant 🔥✨" (VIDEO, `video_id` 994466939917175)

So the "Valeting Campaign" container holds the Deep Clean creative. There is also a separate **archived** `Deep clean advert` campaign (`120244741843280294`, ad "blue horizon deep clean creative") with no recoverable metrics, and a `Detailing campaign` (`120245747039030294`, "20% OFF Detailing services") used below only for comparison.

---

## 1. Full setup inspection

| Setting | Value | Source |
|---|---|---|
| Objective | OUTCOME_LEADS | API |
| Status | PAUSED (campaign off) | API |
| Daily budget | £10.00/day (campaign-level) | API |
| Optimisation goal | LEAD_GENERATION (Meta **instant form**) | API |
| Attribution | 1-day view / 7-day click | API |
| Bid strategy | Not readable via MCP (no value returned — likely Highest Volume / lowest-cost auto) | gap |
| Ad set | `ADV+ - 621K Aud` → Advantage+ Audience, ~621K size | inferred from name |
| Audience/age/gender/location **settings** | **Not readable** via MCP | gap |
| Placements | Advantage+ / automatic (delivered across FB feed, FB Reels, IG Reels, Stories, in-stream, etc.) | inferred from delivery breakdown |
| Creative type | Single **video** + Meta instant form | API |
| CTA | GET_OFFER | API |
| Destination | Meta **instant lead form** (results = `leadgen.other`); no website link on the creative | API |
| Primary text | See below | API |
| Headline (title) | "FREE 3-Month Ceramic Sealant 🔥✨" | API |
| Description | none stored | API |
| Pixel/dataset | "Bluehorizondetailing – Meta pixel" `1404609760266229`, active, last fired 2026-06-12 | API |
| Dataset quality (EMQ) | `web: []` — no web event-match-quality data returned | API/gap |
| Delivery errors | None (`{}`) | API |
| Opportunity score | 100/100, no recommendations | API |

**Primary text currently live:**
> 🔥 ATTENTION RUGBY DRIVERS + SURROUNDING AREAS 🔥
> ⚠️ FOR ONE LAST WEEK: FREE 3 month ceramic sealant + engine-bay detail disappearing forever!
> ✅ Mobile service - we come to you
> ✅ Professional paint armour for 6 months
> ✅ Showroom shine that lasts all year
> Most shops charge £100+ extra for this level of protection 💰💰
> We're doing it for £150 to prove we're the best!
> ⏰ Spots filling FAST - don't miss out!

### Setup weaknesses flagged
1. **Off-brand copy.** "FOR ONE LAST WEEK", "disappearing forever", "Spots filling FAST", "don't miss out", "we're the best", heavy 🔥💰 emojis — this is exactly the urgency/hype tone the brand voice rules say to avoid, and "we're the best" is an unsupported claim.
2. **Pricing conflict.** Deep Clean is "From £180" in the knowledge file; the ad sells at **£150** framed as a deal. That undercuts premium positioning and likely pulls in price-shoppers (the customer the knowledge says to avoid).
3. **Internal inconsistency.** "FREE 3 month ceramic sealant" (headline/offer) vs "Professional paint armour for **6 months**" (body) — durability claim is inconsistent and unsupported by a named product/warranty.
4. **Templated, non-differentiated offer.** Competitor research (below) shows a rival ("Crow valeting and detailing") running the **identical** "FREE Ceramic Sealant + Engine-Bay Detail" offer — this is a copy-paste template circulating among UK detailers, so it does not make Blue Horizon look distinct or premium.
5. **No review/proof** (4.8★ / 50+ reviews) in the copy.
6. **Offer requires approval.** A free-add-on + discounted price is an offer; treat as Josh-owned (he set it up), but it is not in the approved-offer list.

---

## 2. Performance analysis (lifetime, 1 Apr – 15 Jun 2026)

**Headline numbers (OG Deep Clean):**

| Metric | Value |
|---|---|
| Spend | £293.64 |
| Impressions | 45,326 |
| Reach | 18,598 |
| Frequency | 2.44 |
| CPM | £6.48 |
| Clicks (all) | 1,415 |
| Link clicks | 581 |
| CTR (all) | 3.12% |
| CPC (all) | £0.21 |
| Cost / link click | £0.51 |
| Page engagement | 11,033 |
| **Leads** | **101** |
| **Cost per lead** | **£2.91** |

For comparison, the Detailing campaign ("20% OFF") produced 35 leads at **£1.50 CPL** but on far less spend (£52) and a discount-led offer.

### Age breakdown
| Age | Leads | CPL | Spend |
|---|---|---|---|
| 18–24 | 7 | £2.93 | £20.52 |
| 25–34 | 11 | £3.82 | £42.07 |
| 35–44 | 17 | £3.22 | £54.77 |
| **45–54** | **23** | **£2.44** | £56.06 |
| **55–64** | **24** | £2.93 | £70.22 |
| **65+** | 19 | £2.63 | £50.00 |

**45+ = 66 of 101 leads (65%)** and the lowest CPLs. 25–34 is the most expensive (£3.82).

### Gender breakdown
| Gender | Leads | CPL | Spend |
|---|---|---|---|
| Male | 93 | £2.85 | £265.25 |
| Female | 8 | £3.09 | £24.73 |

Delivery is ~92% male. Female volume is tiny but CPL is only marginally higher — under-tested, not proven weak.

### Placement breakdown (lead-driving placements)
| Placement | Leads | CPL | CTR | Spend |
|---|---|---|---|---|
| **Facebook Feed** | 43 | £2.73 | 4.19% | £117.43 |
| **Facebook Reels** | 35 | £2.76 | 2.45% | £96.65 |
| Instagram Reels | 14 | £3.80 | 1.97% | £53.24 |
| Instagram Stories | 6 | £2.79 | 2.75% | £16.73 |
| In-stream video | 3 | £2.06 | 3.15% | £6.18 |
| IG Stories/Explore/other | ~0 | – | – | negligible |

**Facebook Feed + Facebook Reels = 78 of 101 leads** at the best CPLs. **Instagram Reels is the weakest paid placement (£3.80 CPL)**.

### Region
Only `England` returned (£293.64 / 45,326 imp). **City/town-level breakdown not available via MCP** — cannot confirm Rugby+20 vs spill outside service area from Meta here.

### What this means
1. **Working well:** Strong CTR (3.12%) and a genuinely low £2.91 CPL for a lead-form video; healthy 101 leads on ~£294; frequency 2.44 (no fatigue); Facebook Feed/Reels are efficient; 45+ affluent demo is engaging.
2. **Not working well:** Off-brand creative; Instagram Reels CPL ~40% higher than FB; copy likely skews toward bargain-seekers.
3. **Wasting money:** Instagram Reels relative to Facebook; tiny spend scattered across non-converting placements (marketplace, search, profile feed).
4. **Promising:** 45–64 segment + Facebook Feed/Reels + video format is a clear winner to lean into; female audience cheap to test wider.
5. **Unclear (missing data):** **Lead quality / booked jobs / revenue** (in GHL, not Meta) — so we don't know if £2.91 leads are *good* leads. Form open→completion split, exact targeting, city-level geo, and bid strategy are all not readable here.
6. **Do not change yet:** Don't kill Instagram entirely on this sample; don't touch budget; don't restructure the winning FB Feed/Reels + 45+ core.
7. **Test next:** On-brand creative variants (Section 5), audience age-floor at 35+, Feed/Reels-priority placements, and a lead-quality qualifier in the form.

---

## 3. Funnel audit (Ad → form → GHL)

- **Offer clarity:** Clear but discount-led and off-brand; competes on price/freebie, not premium quality.
- **Scroll-stopper:** Video + 3.12% CTR says the creative does stop the scroll — the hook works; the *positioning* is the problem.
- **Copy local?** Yes ("Rugby + surrounding areas") — good.
- **Qualifies the right customer?** **No** — £150 + "free" + urgency attracts price-shoppers, not premium owners. This is the biggest quality risk.
- **CTA strength:** GET_OFFER is strong for volume, weak for qualification.
- **Landing page match:** Current ad uses the **Meta instant form**, not the website. You mentioned a website/GHL route exists — it is **not** what this ad is using. Could not verify the GHL handoff or instant-form questions from MCP (data gap).
- **Friction:** Instant form = low friction = high volume but lower intent. Website/GHL form = higher friction = fewer, better-qualified leads.
- **Right destination?** For *volume* yes; for *quality* a qualifying question or a website-form split test is the lever.
- **Recommendation:** Keep instant form as control, **split-test** (a) instant form + qualifying question vs (b) website GHL form, and measure by **booked jobs in GHL**, not CPL.

---

## 4. Competitor / Ad Library research (GB, active)

Searched Meta Ad Library "mobile car valeting deep clean", GB, active — ~29 ads. Patterns:

- **Identical offer in market:** *Crow valeting and detailing* runs "**FREE Ceramic Sealant + Engine-Bay Detail**" — the **same template** as the OG ad. Confirms the offer is non-differentiated.
- **Hooks:** "Transform Your Car This Summer" (Body Armour), "Get That Mirror Gloss Shine! / 5 Years of Protection" (Fine Finish), "Stop Paying For Car Washes That Damage Your Paint" (Decadent Detailing — strong pain-point hook), "25% OFF Ceramic Coating" (J.R Mobile).
- **Common patterns:** discount/free-add-on offers, "free quote online" CTAs, before/after transformation, summer seasonality, ceramic/gloss protection angles.
- **Competitor mistakes / openings for Blue Horizon:** most look generic, discount-led and cluttered; few lead clearly on **premium proof (4.8★/50+ reviews), prestige vehicles, fully-mobile convenience, and Josh's personal honest quote**. That is Blue Horizon's white space — look more premium, not cheaper.

---

## 5. Improvement variants (drafts — not published)

All variants: Objective OUTCOME_LEADS; core ad set leaning to the proven winners — **age 35–64+ priority, Facebook Feed + Reels priority, Advantage+ audience, Rugby+20/Warwickshire + high-value areas**. All copy on-brand (no "cheap/hurry/best"), review proof where used (4.8★, 50+ reviews), Deep Clean **from £180**. Any discount/free-add-on offer is flagged **(needs Josh approval)**.

### Variant A — Premium Deep Clean Transformation
- **Name:** `BH | Meta Leads | Deep Clean Premium Reset | Rugby+20 | 2026-06`
- **Objective:** Leads (instant form, control format)
- **Audience:** Advantage+ 35–64+, Rugby+20 & Warwickshire + high-value areas (Leamington, Warwick, Kenilworth, Solihull, Dunchurch, Southam, Stratford)
- **Creative:** Best deep-clean transformation video; if static, a high-end vehicle interior reset (Range Rover / Bentley / Rolls-Royce from proof list)
- **Primary text:** "A proper deep clean isn't a quick wash — it's a full reset. We come to your home or workplace across Warwickshire and bring the interior and paintwork back to life with professional-grade products and a safe, careful process. Rated 4.8★ with 50+ Google reviews. Deep Clean from £180. Send us your vehicle details for a tailored quote from Josh."
- **Short primary:** "Premium mobile Deep Clean across Warwickshire. A full interior + paint reset, done properly. 4.8★, 50+ reviews. From £180 — get a tailored quote."
- **Headline:** "Premium Mobile Deep Clean — From £180"
- **Description:** "We come to you across Warwickshire. 4.8★ Google rated."
- **CTA:** Get Quote
- **Destination:** Meta instant form (control) — *or* website valeting page split
- **Lead form:** General BHD questions + "What's the main thing you want sorted?" qualifier
- **Testing:** On-brand premium framing vs OG discount framing, same format
- **Why it may win:** Removes price-shopper signal; keeps the proven video+form mechanics; attracts owners who value quality → better booked-job rate even if CPL rises slightly.

### Variant B — Busy Owner Convenience
- **Name:** `BH | Meta Leads | Deep Clean Convenience | Rugby+20 | 2026-06`
- **Audience:** Advantage+ 30–55, working professionals/families, Warwickshire
- **Creative:** Josh arriving at a home/driveway, working on the car (mobile/convenience angle)
- **Primary text:** "No time to sort the car? We bring the full Deep Clean to your driveway or workplace anywhere across Warwickshire. You carry on with your day — we hand it back fresh inside and out. 4.8★, 50+ reviews. Deep Clean from £180. Tell us about your vehicle for a tailored quote."
- **Short primary:** "We bring the Deep Clean to your home or work across Warwickshire. You carry on — we handle the car. From £180."
- **Headline:** "We Come To You — Mobile Deep Clean"
- **Description:** "Home or workplace, Warwickshire-wide."
- **CTA:** Get Quote
- **Destination:** Instant form (volume) or WhatsApp (faster qualify)
- **Lead form:** General + preferred day/time
- **Testing:** Convenience hook vs transformation hook
- **Why it may win:** Convenience is Blue Horizon's strongest non-price differentiator for busy 30–55 professionals; broadens beyond the 45+ core.

### Variant C — Interior Reset / Family Car Rescue
- **Name:** `BH | Meta Leads | Interior Rescue | Rugby+20 | 2026-06`
- **Audience:** Advantage+ 30–55, families; Warwickshire
- **Creative:** Before/after interior — dog hair, stains, crumbs → reset (use Range Rover interior deep clean proof)
- **Primary text:** "Kids, dogs, daily life — interiors take a beating. Our Deep Clean shampoos and extracts seats and mats, deep-cleans leather, sanitises the A/C and resets the whole cabin. Mobile across Warwickshire, 4.8★ with 50+ reviews. From £180 — send your details for a quote."
- **Short primary:** "Dog hair, stains, crumbs? We reset family-car interiors properly. Mobile, Warwickshire. From £180."
- **Headline:** "Family Car Interior — Fully Reset"
- **Description:** "Seats, mats, leather, A/C sanitised."
- **CTA:** Get Quote
- **Destination:** Instant form
- **Lead form:** General + "Interior, exterior, or both?"
- **Testing:** Specific pain-point (messy interior) vs general premium
- **Why it may win:** Concrete relatable problem + before/after proof typically lifts CTR and qualifies intent; strong for the family segment.

### Variant D — Before/After Proof Ad
- **Name:** `BH | Meta Leads | Deep Clean Before After | Rugby+20 | 2026-06`
- **Audience:** Advantage+ 35–64+, Warwickshire + high-value areas
- **Creative:** Before/after carousel or split video from proof list (Range Rover interior, Rolls-Royce Ghost deep clean, Bentley Bentayga)
- **Primary text:** "Same car. Same day. We come to you across Warwickshire and reset it properly — inside and out. Swipe to see the difference. 4.8★, 50+ Google reviews. Deep Clean from £180. Send your vehicle details for a tailored quote from Josh."
- **Short primary:** "Before → after, same day, at your home. See the Deep Clean difference. From £180. 4.8★."
- **Headline:** "See The Deep Clean Difference"
- **Description:** "Real Warwickshire results. 4.8★."
- **CTA:** Get Quote
- **Destination:** Instant form
- **Lead form:** General
- **Testing:** Proof-led (let results sell) vs claim-led
- **Why it may win:** Before/after is the highest-trust format in this category; differentiates on real premium results vs competitors' generic discount creatives.

### Variant E — Maintenance Plan Entry Point
- **Name:** `BH | Meta Leads | Deep Clean to Maintenance | Rugby+20 | 2026-06`
- **Audience:** Advantage+ 35–64+, Warwickshire
- **Creative:** Clean prestige car + "start here, stay here" framing
- **Primary text:** "The best way to keep your car looking its best: start with a full Deep Clean reset (from £180), then keep it maintained every few weeks with our mobile Maintenance Valet (from £80). One reset, then easy upkeep — all at your door across Warwickshire. 4.8★, 50+ reviews. Get your tailored plan from Josh."
- **Short primary:** "Start with a Deep Clean reset, then easy mobile upkeep from £80. Warwickshire-wide. 4.8★."
- **Headline:** "Deep Clean Now, Effortless Upkeep After"
- **Description:** "Reset from £180, maintain from £80."
- **CTA:** Get Quote
- **Destination:** Instant form or website valeting page
- **Lead form:** General + "Interested in ongoing maintenance?"
- **Testing:** LTV/relationship framing vs one-off job framing
- **Why it may win:** Frames a higher-value, repeat relationship → attracts customers worth more than a single cheap lead; supports the "quality over cheap" goal directly.

---

## 6. Optimisation plan

### Immediate fixes (data clearly supports)
- Replace off-brand OG copy with an on-brand premium version (Variant A as the new control). The hype/discount language conflicts with brand rules and likely degrades lead quality.
- Fix the 3-month vs 6-month ceramic inconsistency and remove "we're the best" (unsupported claim).

### Test next
- Variant A (premium reset) head-to-head vs OG, then layer in B/C/D.
- Placement test: Facebook Feed + Reels priority vs full Advantage+ (IG Reels is the weakest at £3.80 CPL).
- Age floor at 35 (35–64+ drove 65% of leads at the best CPLs).
- Destination split: instant form + qualifier vs website GHL form, judged on **booked jobs**.

### Do not touch yet
- Budget (£10/day) — hold until variants run.
- Don't fully cut Instagram on this sample size.
- Don't dismantle the winning FB Feed/Reels + 45+ core.
- Bid strategy / attribution — leave as-is.

### Tracking checks needed
- Confirm Meta lead form → GHL handoff is firing (test lead end-to-end).
- Start scoring leads in GHL: good / booked / quoted-not-booked / out-of-area / price-shopper / spam.
- Confirm pixel events for the website-form route (dataset EMQ returned empty — verify web events are landing).
- Add a city/postcode question so geo quality can be measured (Meta only shows region=England here).

### Budget recommendation (no change made)
**Hold at £10/day** during the variant test. £2.91 CPL is strong, but until GHL shows booked-job quality, scaling spend could just scale cheap leads. Revisit once Variant A vs OG quality is known.

### Lead quality recommendation
- Drop the discount/urgency framing → attract premium owners not bargain hunters.
- Add a qualifying question (vehicle make/model + "what do you want sorted").
- Lean into 35–64+, Facebook Feed/Reels, prestige proof and 4.8★/50+ reviews.
- Measure success by **booked jobs and qualified enquiries in GHL**, not CPL.

---

## 7. Action table

| Recommendation | Reason | Risk | Expected benefit | Approve / Reject / Edit |
|---|---|---|---|---|
| Replace OG copy with on-brand premium control (Variant A) | OG breaks brand voice + attracts price-shoppers | Slightly higher CPL | Better lead quality / booked jobs | APPROVE / REJECT / EDIT |
| Build Variants A–E as PAUSED drafts for review | Structured creative test | None (paused) | Clear winner identification | APPROVE / REJECT / EDIT |
| Prioritise FB Feed + Reels; cut/limit IG Reels | IG Reels £3.80 vs FB £2.73–2.76 CPL | Less reach | Lower CPL, more leads/£ | APPROVE / REJECT / EDIT |
| Set age floor 35+ | 35–64+ = 65% leads, lowest CPL | Lose minor 18–34 volume | More efficient, better-fit leads | APPROVE / REJECT / EDIT |
| Add qualifying question to lead form | Filters price-shoppers | Slightly fewer leads | Higher booked-job rate | APPROVE / REJECT / EDIT |
| Split-test instant form vs website GHL form | Measure quality not just volume | Setup effort | Identifies best-converting route | APPROVE / REJECT / EDIT |
| Start GHL lead scoring | Quality is invisible in Meta | Manual effort | Optimise to booked jobs | APPROVE / REJECT / EDIT |
| Hold budget at £10/day | Don't scale until quality known | Slower growth | Avoids scaling cheap leads | APPROVE / REJECT / EDIT |

**Single best next move:** Approve building **Variant A (Premium Deep Clean Transformation)** as a PAUSED draft to run head-to-head against the OG ad, with a lead-form qualifying question — so we can prove on-brand premium positioning holds the strong CPL while improving lead quality.

*No live action will be taken until you say: "Approve and apply [specific action]."*
