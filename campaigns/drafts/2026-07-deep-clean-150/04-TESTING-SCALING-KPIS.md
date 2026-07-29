# Testing, Scaling & KPIs — Deep Clean £150

# 1. KPI hierarchy

Read top-down. Everything below line 1 is diagnostic — useful for *explaining* performance, never a goal in itself.

| # | Metric | Target | What it tells you |
|---|---|---|---|
| **1** | **Cost per booked job** | **< £40** (viable to £60 while optimising) | The only number that matters. £150 job — at £40 the campaign is strongly profitable. |
| 2 | Booked jobs / week | 3–5 at £25/day | Real business outcome. |
| 3 | Enquiry → booking rate | > 40% | If enquiries are high but bookings low, the problem is response speed or lead quality, not the ads. |
| 4 | Cost per enquiry (GHL form) | £8–20 | Tracked via UTMs in GHL, not Meta, until the pixel is fixed. |
| 5 | Landing page view → enquiry rate | > 8% | **The landing page's report card.** Currently the weakest link. |
| 6 | Cost per landing page view | £0.30–0.80 | Meta's optimisation target. |
| 7 | CTR (link) | > 2%; expect 4%+ | Creative strength. Current campaign runs 4–5%. |
| 8 | CPM | Trend, not absolute | Rising CPM + flat results = fatigue. |
| 9 | Frequency (7-day) | < 2.5 | Above 3 = audience exhaustion. |

**The critical diagnostic:** if metrics 6–9 are healthy but 4–5 are poor, the ads are working and the **page** is failing. That is exactly the current situation — see `03-LANDING-PAGE-AUDIT.md`.

---

# 2. Testing strategy

## The golden rule
**Do not touch anything for the first 5–7 days.** Every edit — budget, audience, creative, pause/unpause — restarts Meta's learning phase and wastes the spend that came before it. The urge to fiddle on day 2 is the most expensive instinct in paid social.

## Learning phase expectations
Meta wants ~50 optimisation events in 7 days to exit Learning. At £25/day optimising for landing page views, that's achievable. If the ad sets sit in "Learning Limited", judge on cost per enquiry and booked jobs, not the label.

**Days 1–2 will look erratic.** Delivery is uneven while Meta explores. This is normal and not a signal.

## The review cadence

**Day 7 — first real review**
- Pause any ad with **>£15 spent and 0 enquiries** *and* a clearly below-average CTR.
- Note the top 2 performers by cost per landing page view.
- Do not touch budgets yet.

**Day 14 — the decision point**
- Pause the weakest ad set on cost per enquiry.
- Rotate in **Wave 2 creative** (`02-CREATIVE-STRATEGY-AND-COPY.md` §5).
- Review the **placement breakdown** — cut Audience Network if it's spending with nothing to show.
- Review the **geographic breakdown** — which towns actually book?
- **If the Lead event is now firing:** build the conversion-optimised ad set (see §4).

**Weekly thereafter**
- Cost per booked job, tracked in GHL against `utm_content`.
- Frequency check — above 3, refresh creative rather than widening the audience.
- One new creative concept in, one loser out. Continuous rotation beats periodic overhaul.

## What to test, in order

1. **Creative concept** (biggest lever by a wide margin — 10× the impact of audience tweaks)
2. **Hook / first line** of primary text
3. **Image** — which transformation stops the scroll hardest
4. **CTA** — Book Now vs Learn More
5. **Audience** — only once creative winners are established

**Never test more than one variable at a time within an ad set**, and never change the control while a test is running.

## Kill and scale rules

| Situation | Action |
|---|---|
| Ad: >£15 spent, 0 enquiries, below-average CTR | Pause |
| Ad: Meta gave it almost no spend | **Leave it.** That's Meta's verdict, not a fair test. Don't force it. |
| Ad: clear winner on cost per enquiry | Duplicate it, test a new hook against it |
| Ad set: 14 days, worst cost per enquiry | Pause, reallocate to the winner |
| Frequency > 3 with rising CPM | Creative fatigue → rotate, don't add budget |

---

# 3. Scaling strategy

**The enemy is resetting learning.** Large sudden budget jumps destabilise delivery and spike cost per result.

## Method A — Gradual (default)
- Raise by **no more than 20–30% at a time**
- Hold **3–4 days** between increases
- Only increase when cost per booked job has been acceptable and *steady* for those 3–4 days

**Example ramp:** £25 → £32 → £40 → £50 → £65 → £80/day, roughly 3 weeks to double.

**If a jump spikes cost per booking, step back one level and hold.** Don't push through it.

## Method B — Duplicate to jump
For bigger leaps (£40 → £80), duplicate the winning ad set at the higher budget and run alongside rather than shocking the original. It learns fresh but from proven creative, so it ramps fast. Pause the smaller one once the duplicate settles.

## ⚠️ The capacity check — do this before every increase

**Josh does the work personally.** A Deep Clean is a half-day-plus job. More budget means more enquiries means more diary pressure — and the fastest way to damage a premium brand is to take bookings you can't service well or reply slowly.

**Scale spend only as fast as the diary can absorb it.** If the calendar is full, hold budget and clear the backlog. This constraint is more binding than any performance metric — and it's why "just increase the budget" is often the wrong answer even when the numbers look great.

## Bid strategy as you scale
- Start: **Highest volume (lowest cost)** — no cap
- Once cost per booked job is known and stable, a **cost cap** can protect efficiency at higher budgets
- **Don't cap early** — it throttles delivery before Meta has learned anything

---

# 4. The tracking upgrade (the most important scheduled action)

Once the Lead event fires reliably (target: within 2 weeks):

1. **Confirm** real Lead events in Events Manager for 3–5 consecutive days
2. **Build a NEW ad set** — optimisation goal `OFFSITE_CONVERSIONS`, promoted object = pixel `1404609760266229`, custom event `Lead`
   - **It must be a new ad set.** Meta blocks changing optimisation on an existing one ("Attribution Window Update Is No Longer Supported"). We hit this before — don't waste time retrying it.
3. **Run alongside** the Landing Page Views ad set at equal budget for 7 days
4. **Compare on cost per booked job**, not cost per result — the two goals report different events and aren't directly comparable
5. Shift budget to the winner

**Expected outcome:** conversion optimisation typically improves cost per lead 20–40% over traffic-style goals, because Meta can finally target people who *complete forms* rather than people who *click*. This single change is likely worth more than any creative test in this document.

**Prerequisite:** ~15–30 Lead events per week for Meta to optimise properly. Below that, stay on Landing Page Views.

---

# 5. What would make me change the whole approach

Honest failure conditions, defined in advance so we don't rationalise later:

- **Enquiries are cheap but nobody books** → the offer or the lead quality is wrong, not the ads. Revisit who we're attracting.
- **Landing page views are cheap but enquiries never come** (and the page has been fixed) → the offer itself isn't compelling enough at £150, or the page can't sell it. Consider testing Meta native lead forms instead.
- **Cost per booked job stays above £60 after 3 weeks with fixed tracking** → Meta may not be the right primary channel for this service. The knowledge file's own guidance is that Google Search intent is higher for "car deep clean Rugby" — that would be the pivot.

Naming these now prevents the classic trap of spending three months optimising a channel that was never going to work.
