# Deep Clean £150 — Meta Campaign — LIVE

**Went live:** 29 July 2026, on Josh's explicit APPROVE.
**Campaign:** `BH | Meta Leads | Deep Clean £150 | Warwickshire | 2026-07` — `120250775729340294`
**Full strategy + copy bank:** `campaigns/drafts/2026-07-deep-clean-150/`

## Live configuration

| | |
|---|---|
| Objective | OUTCOME_LEADS |
| Optimisation | Landing Page Views (all ad sets) |
| Budget model | ABO — £25/day total |
| Destination | bluehorizondetailing.com/offers/deep-clean-150 (URLs verified by Josh) |
| Offer | Usually £180. Currently £150. |

**Ad sets — all ACTIVE**
- `120250775747220294` Broad Warwickshire — £12/day · Rugby+20mi · 28–65 · A+ Audience on · **7 ads**
- `120250775753220294` High-Value Areas — £7/day · 8 town radii · 30–65 hard cap · A+ Audience off · **3 ads**
- `120250775770610294` Retargeting Warm — £6/day · FB/IG engagers + site visitors · **2 ads**

**All 12 ads verified ACTIVE / ACTIVE at launch. No delivery issues.**

## Account state at launch
Only two campaigns are live:
- Deep Clean £150 — £25/day (this one)
- SMART Repairs WhatsApp — £10/day
- **Total Meta spend: £35/day**

**Auction conflict resolved:** the older Deep Clean campaign was flagged pre-launch as a self-competition risk. On checking at launch it is **not active**, so no conflict exists and no action was needed. Net new spend is the full £25/day.

---

## ⚠️ Outstanding risks — launched knowingly

Josh approved launch with these open. They do not stop the campaign working, but they limit how precisely we can measure it.

**1. Pixel may not be firing PageView.** The website custom audience holds ~20 people after weeks of traffic, while FB/IG audiences hold 1,000+. If PageView is unreliable, Landing Page Views optimisation is degraded — Meta is optimising on partial data. **Check with Meta Pixel Helper.** Highest-value open item.

**2. Lead event does not fire at all.** Confirmed: 0 Lead events in 7 days. The GHL form is a cross-domain iframe. Fix = thank-you page + URL-rule Lead event (`03-LANDING-PAGE-AUDIT.md` §1). Until then no conversion optimisation is possible.

**3. UTM capture in GHL unverified.** UTMs are currently the *only* reliable attribution path. If GHL isn't storing `utm_content`, we cannot tell which ad books jobs. Test with one form submission.

**4. Landing page not audited.** Environment blocked all outbound web access (confirmed — `example.com` also 403). Evidence-based findings stand; the visual/UX review is outstanding.

---

## First week

**Days 1–5: hands off.** Every edit restarts learning. Delivery will look uneven on days 1–2 — normal.

**Watch:** enquiries arriving in GHL, and whether `utm_content` is populated on each.

**Day 7 review:**
- Pause any ad with >£15 spent, 0 enquiries and below-average CTR
- Note top 2 performers by cost per landing page view
- Do not touch budgets

**Day 14:** rotate in Wave 2 creative, review placement + geo breakdown, and — if the Lead event is live by then — build the conversion-optimised ad set (must be a NEW ad set; Meta blocks changing optimisation on an existing one).

**The only number that matters:** cost per booked job. Target under £40 on a £150 job.

**Capacity check:** Josh does the work personally. Scale only as fast as the diary absorbs it.
