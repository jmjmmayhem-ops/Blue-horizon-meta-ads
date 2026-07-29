# Landing Page Audit — /offers/deep-clean-150

## Access note — read this first

**I could not load the page.** This environment's network policy denied the request (`403` at the proxy on `www.bluehorizondetailing.com`, confirmed in the proxy's own failure log). Both WebFetch and a direct request were blocked. This is an environment restriction, not a problem with the site.

**So this audit separates two things honestly:**

- **Part A — evidence-based findings.** Drawn from live Meta campaign data and Meta's own dataset diagnostics. These are verified facts about how this page behaves, not assumptions.
- **Part B — the checklist I could not verify.** The visual/UX review the brief asked for. I've written it as a specific checklist Josh can answer in five minutes, or I can complete it if the domain is allow-listed or Josh pastes the page content.

I'd rather flag the gap than invent a review of a page I haven't seen.

---

# PART A — Evidence-based findings

## 🔴 PRIORITY 1 — The page cannot report a lead to Meta

**Severity: critical. This is the single highest-value fix available.**

**The evidence:**
- The form is a **GoHighLevel iframe** (`api.leadconnectorhq.com/widget/form/Co6tPqHw2oRS0V2wiVaT`) — a different domain from the page hosting it.
- Browser-side pixel events cannot cross that iframe boundary. The submit happens inside GHL's domain; the pixel on the parent page never sees it.
- **Meta's dataset diagnostics confirmed 0 Lead events in 7 days** while the Deep Clean campaign was actively driving traffic. Not "few". Zero.
- GHL's Conversions API "Lead Event" is a dead end — it requires a Facebook Lead ID that only exists for Meta's native lead forms, not website forms. We attempted this and hit the wall.

**What it costs:**
1. **Meta cannot optimise.** Every conversion-optimised campaign is guessing. This produced the £0 cost-per-result reading Josh saw.
2. **No retargeting precision** — can't exclude converters or build lookalikes from real leads.
3. **No honest ROAS** — impossible to say which ad books jobs from Meta's data alone.

**The fix, in order of preference:**

**Option A — Thank-you page + URL rule (recommended).** Configure GHL to redirect to a dedicated thank-you URL after submit (e.g. `/offers/deep-clean-150/thank-you`). Create a Meta pixel Custom Conversion that fires **Lead** on any page view matching that URL. This works *because* it happens on Blue Horizon's own domain where the pixel already lives — it sidesteps the iframe problem entirely rather than fighting it. Most reliable, ~20 minutes of setup.

**Option B — Conversions API with a Custom Event.** GHL workflow → CAPI → custom event name (not "Lead"), then build a Custom Conversion from it. Works, but more moving parts and a previous attempt already failed on the Lead-ID requirement.

**Option C — Switch to Meta native lead forms.** Sidesteps the website entirely and gives perfect tracking, but loses the landing page's selling power and requires the Page to accept Lead Gen ToS first (currently `leadgen_tos_accepted: false`).

**Until this is fixed**, the campaign optimises for Landing Page Views and attributes bookings through UTMs into GHL. That's a competent workaround — not a substitute.

---

## 🔴 PRIORITY 2 — Clicks are strong, form completion is weak

**The evidence:** the live Deep Clean campaign runs **CTR ~4–5%** and **cost per link click ~£0.11–0.13**. Those are genuinely strong numbers — meaningfully above typical local service benchmarks. Josh's own words: *"clicks are good but not many people are filling the form out."*

**What this tells us:** the ads are working. The creative earns the click. The loss is happening **on the page**, after arrival. When traffic quality is that good and conversion is that poor, the page is the bottleneck — not the targeting and not the copy.

**The most probable causes, in likelihood order:**

1. **The iframe form is slow, or renders below a large hero.** Embedded GHL forms load after the parent page and often land below the fold on mobile. If a visitor has to scroll and then wait, a large share leave before the form even appears. **On mobile, the form should be visible without scrolling, or reachable via a sticky button.**
2. **Too many form fields.** Every field costs completions. For a £150 offer, four fields is plenty: name, phone, postcode, vehicle. Email is optional if you have a phone number. Anything beyond that should earn its place.
3. **No visible price anchor on the page.** If the ad says "usually £180, currently £150" and the page doesn't immediately confirm it, that dissonance kills trust in the first three seconds.
4. **Weak proof above the fold.** 4.8★ and 50+ Google reviews are strong, real assets. If they're not visible next to the form, they're not doing their job.
5. **No WhatsApp alternative.** Some people will never fill a form but will happily send a message. Given WhatsApp is already Blue Horizon's strongest channel, its absence here is a real gap.

---

## 🟠 PRIORITY 3 — Known site-wide issue: placeholder counters

The knowledge file records that some sections display `0+` or `0.0★` while animated counters load. **If that appears anywhere on this offer page, it is actively destroying trust** — a visitor seeing "0 reviews" and "0.0 stars" next to a £150 ask will leave immediately. Worth checking specifically on mobile and on a slow connection.

---

# PART B — The checklist I could not verify

Answer these and I'll turn them into a prioritised fix list. Or allow-list the domain and I'll do it directly.

**Above the fold (mobile first — most traffic is mobile)**
- [ ] Is the headline about *the customer's outcome*, or about Blue Horizon?
- [ ] Is the £180 → £150 anchor visible immediately, presented calmly?
- [ ] Is there a CTA visible without scrolling?
- [ ] Is the hero image a genuine before/after, or a stock/generic shot?
- [ ] Are 4.8★ / 50+ reviews visible within the first screen?

**The form**
- [ ] How many fields, and which?
- [ ] How far down the page does it sit on a phone?
- [ ] How long does the iframe take to appear?
- [ ] What does the submit button say? ("Submit" is the weakest possible wording — "Book My Deep Clean" or "Get My £150 Slot" convert better.)
- [ ] What happens after submit — thank-you page, or inline message? *(This determines whether Priority 1 Option A is available.)*

**Trust**
- [ ] Any real review quotes, with names?
- [ ] Is "fully insured" stated?
- [ ] Is Josh visible — a face, a name, a founder line? Owner-operator trust is a genuine advantage over faceless competitors.
- [ ] Is the service area listed, so visitors can self-qualify?

**Offer clarity**
- [ ] Is what's included in the Deep Clean spelled out? (Seats extracted, A/C sanitised, decontamination, ceramic protection — this list *is* the price justification.)
- [ ] Is it clear the £150 is limited-time without fake countdown timers?
- [ ] Any FAQ handling "how long does it take", "do you need water/power", "what if it rains"?

**Technical**
- [ ] Mobile load time (target: under 3 seconds)
- [ ] Any layout shift as the iframe loads?
- [ ] Does the page work on a 4G connection, not just wifi?

---

# Recommended changes, in priority order

Ranked by expected impact on **booked jobs** per hour of effort:

| # | Change | Impact | Effort |
|---|---|---|---|
| 1 | **Thank-you page + Lead event** (Priority 1, Option A) | 🔥 Critical — unlocks conversion optimisation and true attribution | ~20 min |
| 2 | **Move the form above the fold on mobile**, or add a sticky "Book Now" button | 🔥 High — most likely single cause of the click/fill gap | Low |
| 3 | **Cut the form to 4 fields** (name, phone, postcode, vehicle) | High | Low |
| 4 | **Add a WhatsApp button** beside the form as an alternative path | High — plays to the channel that already works | Low |
| 5 | **Put 4.8★ / 50+ reviews adjacent to the form**, not in the footer | Medium-high | Low |
| 6 | **Confirm the £180 → £150 anchor above the fold**, matching the ad exactly | Medium-high | Low |
| 7 | **Add the "what's included" list** — the price justification | Medium | Low |
| 8 | **Verify GHL captures UTM fields** on the contact record | 🔥 High — this is the attribution backbone while the pixel is blind | ~10 min |
| 9 | Fix any `0+` / `0.0★` placeholder counters | Medium | Medium |
| 10 | Rewrite submit button to "Book My Deep Clean" | Low-medium | Trivial |

**Note on scope:** the knowledge file forbids me changing live landing pages or forms without explicit approval, so these are recommendations only. Nothing has been touched.

**The one I'd do today:** #8 and #1. Without them, we're spending money we can't measure.
