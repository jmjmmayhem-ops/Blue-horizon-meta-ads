# Premium Deep Clean £150 — Meta Campaign Strategy

**Prepared:** 29 July 2026
**Objective in one line:** Maximise **booked Deep Clean jobs** in Warwickshire — not clicks, not leads, not engagement.
**Offer:** Premium Deep Clean, usually **£180**, currently **£150**.
**Destination:** https://www.bluehorizondetailing.com/offers/deep-clean-150
**Status:** Built PAUSED (draft). Nothing spends until Josh approves.

---

## 1. The strategic problem (read this first)

Three facts decide this entire campaign:

**1. The pixel cannot currently see a lead.** The landing page form is a GoHighLevel **iframe** on a different domain. Browser-side Lead events don't cross that boundary. We confirmed this directly — Meta's dataset showed **0 Lead events in 7 days** while the live Deep Clean campaign was producing clicks. GHL's Conversions API "Lead Event" is also a dead end: it demands a Facebook Lead ID that only exists for Meta native lead forms, not website forms.

**Consequence:** if we optimise this campaign for "website leads", we are asking Meta to optimise toward a signal it never receives. That is exactly what produced the **£0 cost-per-result** reading Josh saw earlier. It doesn't just report wrong — it actively degrades delivery, because Meta has no feedback to learn from.

**2. The current live Deep Clean campaign gets clicks but few form fills.** CTR ~4–5% and cost per link click ~£0.11–0.13 — genuinely good numbers. The drop-off is *after* the click. That points at the landing page and the tracking, not the ads.

**3. Creative is the only real targeting lever available.** No `targeting_search` tool is connected, so I cannot attach verified interest IDs via MCP (inventing IDs is not an option — Meta rejects them). See §4 for why this is a strength, not a compromise.

**So the strategy is:** win on creative, send to a page we've flagged for fixing, optimise on a signal that actually exists, and instrument attribution through UTMs into GHL so we can see which ad books jobs even while the pixel is blind.

---

## 2. Campaign structure

```
CAMPAIGN  BH | Meta Leads | Deep Clean £150 | Warwickshire | 2026-07
│         Objective: OUTCOME_LEADS · ABO (ad-set budgets) · £25/day total
│
├── AD SET 1  Broad Warwickshire            £12/day   ← primary engine
├── AD SET 2  High-Value Areas              £7/day    ← job-value test
└── AD SET 3  Retargeting — Warm            £6/day    ← cheapest bookings
```

### Why OUTCOME_LEADS optimised for LANDING PAGE VIEWS (not conversions, not clicks)

| Option | Verdict |
|---|---|
| Optimise for **Leads / Offsite Conversions** | ❌ Not yet — the Lead event doesn't fire. Meta would be flying blind. This is the trap we already fell into. |
| Optimise for **Link Clicks** | ❌ Too shallow. We already know clicks are cheap and don't convert. Optimising for clicks buys more of the problem. |
| Optimise for **Landing Page Views** | ✅ **Chosen.** It's a real signal Meta reliably receives, and it filters for people who actually *wait for the page to load* — a materially higher-intent group than click-happy scrollers. It is the deepest honest signal available today. |

**The upgrade path is the point.** Once the Lead event fires (see `03-LANDING-PAGE-AUDIT.md` §1), we build a **new ad set** optimised for Offsite Conversions — a new one, because Meta blocks changing optimisation on an existing ad set ("Attribution Window Update Is No Longer Supported"). That switch is when this campaign steps up a level, and it should happen within 2–3 weeks.

### Why ABO, not CBO

Meta's default advice is CBO, and for a mature account I'd agree. Not here, for two concrete reasons:

1. **CBO would starve the retargeting ad set.** Warm audiences are small but convert best. Under CBO, Meta reliably dumps budget into the biggest audience and leaves the small one on scraps. I want a guaranteed £6/day on the warmest traffic Blue Horizon has.
2. **CBO forces one shared optimisation goal across all ad sets.** That's the exact error we hit before. When we add the conversion-optimised ad set in a few weeks, ABO lets it live in this same campaign. CBO would not.

Once tracking is fixed and a winner is obvious, consolidating to CBO is the right move for scaling.

---

## 3. Budget

**Recommendation: £25/day for this campaign.**

| Ad set | Daily | Share | Rationale |
|---|---|---|---|
| Broad Warwickshire | £12 | 48% | The engine. Broad + strong creative is where modern Meta performs. |
| High-Value Areas | £7 | 28% | Tests whether premium postcodes deliver higher job value. |
| Retargeting — Warm | £6 | 24% | Small audience, cheapest bookings. Deliberately protected. |

**Reasoning on the number:** below ~£20/day across three ad sets, none of them gathers enough data to make a decision, and we'd spend three weeks learning nothing. £25/day is the minimum that lets this campaign actually answer questions. At an assumed £6–12 cost per landing page view→enquiry and a £150 job, one booked job every two days makes this comfortably profitable.

### ⚠️ Auction conflict — needs a decision

The **existing live Deep Clean campaign (£20/day, clicks-optimised)** advertises the *same offer* to the *same people* in the *same auction*. Running both means Blue Horizon bids against itself — inflating its own CPMs and splitting learning across two campaigns.

**Recommendation:** when this campaign goes live, **pause the old Deep Clean campaign.** That's a £20/day reduction there and £25/day here — a net increase of £5/day, not £25.

I have **not** paused anything — that's Josh's call and outside what I'll do without explicit approval.

---

## 4. Targeting approach — creative as the targeting

I can't attach verified interest IDs through this connection. Rather than work around that, this campaign leans into what is now the stronger approach anyway:

**Let the creative do the targeting.** The dog-hair ad finds dog owners because dog owners stop scrolling at dog hair. The lease-handback ad finds people with a handback date. The mouldy-carpet ad finds people whose car smells damp. Meta's delivery system then learns from who responds and compounds it — which, in a 20-mile radius, works better than pre-slicing an already small audience into fragments too thin to optimise.

Interest targeting inside a radius this size mostly *shrinks* the pool and raises CPMs without improving intent. Broad + excellent creative is the current best practice for local service businesses, and it's what I'd recommend even with full interest tooling available.

**If Josh wants interest layers anyway**, `01-AUDIENCE-STRATEGY.md` §5 lists the exact interests to add by hand in Ads Manager, in priority order.

---

## 5. Placements

**Advantage+ Placements (all placements), with one reservation.**

Rationale: at £25/day, manually restricting placements starves the algorithm of the cheap inventory that often produces the best cost per result. Reels and Stories in particular are where premium before/after content performs strongly right now.

**Watch item:** review the placement breakdown at day 14. If **Audience Network** is taking meaningful spend with no enquiries — a common pattern for local service ads — exclude it then, based on data rather than assumption.

**Creative implication:** every image needs to survive a 9:16 crop. See `02-CREATIVE-STRATEGY-AND-COPY.md` §6.

---

## 6. Tracking, UTMs and attribution

Because the pixel can't see leads yet, **UTMs are the primary attribution system**, not a nice-to-have. GHL captures UTM parameters on form submission — which means Josh can see exactly which ad produced each enquiry even while the pixel is blind.

**URL parameters applied to every ad:**

```
utm_source=meta
utm_medium=paid_social
utm_campaign=deep-clean-150
utm_content={{ad.name}}
utm_term={{adset.name}}
utm_placement={{placement}}
```

Meta fills those `{{...}}` macros automatically at delivery.

**What this gives Josh:** open any GHL enquiry and see the exact ad, ad set and placement that produced it. That is the ground truth for which creative books jobs — and it's more reliable than Meta's own attribution.

**Required for this to work:** GHL must be storing UTM fields against the contact record. Verify before launch (`05-LAUNCH-CHECKLIST.md`).

**Pixel:** `1404609760266229`, attached to all ad sets so audience-building and future conversion optimisation keep warming up in the background.

---

## 7. Naming convention

Following the knowledge file's standard:

```
Campaign  BH | Meta Leads | Deep Clean £150 | Warwickshire | 2026-07
Ad set    BH | AS | Broad Warwickshire | LPV | 2026-07
Ad        BH | <Image Label> | <Concept Name> | v1
```

Ad names flow into `utm_content`, so keeping them clean and descriptive is what makes the GHL reporting readable. This is why ad names read like `Dog Hair Boot | Keep The Dog Lose The Hair | v1` rather than `Ad 3`.

---

## 8. Advantage+ recommendations

| Feature | Setting | Why |
|---|---|---|
| Advantage+ Placements | **On** | More inventory, lower CPMs at small budget. |
| Advantage+ Audience | **On** for Broad; **Off** for High-Value Areas | On lets Meta expand past the seed where that helps. Off on the geo test keeps the postcode boundary a hard constraint — otherwise the test answers nothing. |
| Advantage+ Creative enhancements | **Off** | Auto-brightness, filters and frame overlays actively fight a premium look and can distort before/after honesty. The whole positioning depends on the imagery reading as real and unretouched. |
| Advantage+ Shopping (ASC) | N/A | Not applicable to a local service business. |

---

## 9. What success looks like

The only number that matters is **cost per booked job**. At £150 a job, the campaign works comfortably at up to ~£40 per booked job and is still worth running at £60 while we optimise.

Everything else — CTR, CPC, cost per landing page view — is diagnostic, not a goal. Full KPI tree and thresholds in `04-TESTING-SCALING-KPIS.md`.
