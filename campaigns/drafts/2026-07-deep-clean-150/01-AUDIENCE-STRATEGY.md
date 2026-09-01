# Audience Strategy — Deep Clean £150

## The governing principle

Blue Horizon's addressable market is roughly **700k–1M people** inside Rugby + 20 miles. That sounds large; at £25/day it is not. Spending that budget across five interest-sliced audiences would give each one a few hundred impressions a day — enough to feel busy, not enough to learn anything.

So: **three ad sets, broad geography, and let the creative select the person.** Meta's delivery system finds the dog owners far more efficiently from who engages with the dog-hair ad than from an interest checkbox — because the interest list only knows who *liked a dog page*, while engagement data knows who *cares right now*.

---

## Ad Set 1 — Broad Warwickshire (primary engine, £12/day)

| Setting | Value |
|---|---|
| Location | Rugby, Warwickshire + **20 miles** |
| Age | **28–65** |
| Gender | All |
| Interests | **None** — broad |
| Advantage+ Audience | **On** |
| Optimisation | Landing Page Views |

**Why 28–65 and not 25+:** a £180 service bought at £150 needs disposable income and, usually, a car worth caring about. Under-28s over-index on cheap valeting and price shopping — precisely the customer the knowledge file says to avoid. The lower bound is a quality filter, not an age preference.

**Why no interests:** this ad set exists to give Meta maximum freedom to find buyers. It carries the widest creative spread (see allocation) so the algorithm has multiple hooks to test against the whole local population.

**This is the ad set most likely to win.** Broad targeting with strong creative consistently outperforms hand-built audiences at local budgets.

---

## Ad Set 2 — High-Value Areas (job-value test, £7/day)

| Setting | Value |
|---|---|
| Location | **Leamington Spa, Warwick, Kenilworth, Solihull, Balsall Common, Southam, Dunchurch, Stratford-upon-Avon** |
| Age | **30–65** |
| Gender | All |
| Interests | None |
| Advantage+ Audience | **Off** (deliberately) |
| Optimisation | Landing Page Views |

**The question this ad set answers:** do affluent postcodes produce *better* jobs — higher-value cars, more upsell to detailing packages, less price resistance — or just more expensive clicks?

That's a genuinely open question and worth £7/day to settle. These are the knowledge file's designated high-revenue areas, and they're where the Enhancement Detail (£495) and Flawless Finish (£745) customers live. If Deep Clean customers from here convert upward into detailing work, this ad set is worth far more than its cost-per-lead suggests.

**Advantage+ Audience is OFF here on purpose.** If Meta is allowed to expand beyond these towns, the geographic boundary dissolves and the test tells us nothing. This is the one place where a hard constraint beats algorithmic freedom.

**Creative skew:** premium and prestige-led concepts (Taycan, Urus, white leather, lease handback).

---

## Ad Set 3 — Retargeting, Warm (£6/day)

| Setting | Value |
|---|---|
| Audience | Website visitors (180 days) + Instagram/Facebook engagers (365 days) |
| Location | Rugby + 25 miles (slightly wider — these people already know the brand) |
| Age | 25–65 |
| Exclusions | Past converters, once identifiable |
| Optimisation | Landing Page Views |

**Why this gets protected budget:** these are the cheapest bookings available. The existing Deep Clean campaign has been generating cheap clicks for weeks — meaning there is a real pool of people who visited the offer page and didn't fill the form. They looked. Something stopped them. They are the single highest-intent group Blue Horizon can advertise to, and right now nobody is following up with them.

**Creative skew:** offer-forward and objection-handling. This audience has already seen the transformation; they need the reason to act now — the £150, the "we come to you", the "no judgement".

**Dependency:** requires a website custom audience built from pixel `1404609760266229`, plus a page/IG engagement audience. If the pixel audience is too small to deliver (<1,000), run engagement-only until it fills, and fold this budget into Broad meanwhile.

---

## Deliberately NOT built (and why)

The brief asked for audience strategies around dog owners, parents, SUV owners, company car drivers, used-car buyers and so on. Those are **excellent creative angles** — and that is exactly where I've put them (see `02-CREATIVE-STRATEGY-AND-COPY.md`). They are not good *ad sets* at this budget:

- **Dog owners** as an interest inside a 20-mile radius ≈ 100–150k people. At £5/day that's a fortnight to reach statistical noise. The dog-hair *creative* inside the broad ad set reaches the same people faster and cheaper, and finds ones the interest list misses entirely.
- **Parents / life-stage** — same maths, worse precision. Meta's parent signals are notoriously stale.
- **Used-car buyers** — genuinely high intent but essentially unaddressable by interest; it's a moment, not a trait. Creative catches the moment.
- **Company car drivers** — too small to run as its own ad set locally.

**The professional judgement:** at £25/day, audience fragmentation is the most common way local campaigns fail. One well-fed broad ad set with eight sharp creatives will beat five starved interest audiences every time. When budget reaches ~£60/day, splitting the winners into their own ad sets becomes correct — that's in the scaling plan.

---

## §5 — Interest layers to add manually (optional)

If Josh wants interest targeting despite the above, these are the ones to add by hand in Ads Manager, in priority order. **I have not added them** — MCP has no verified-ID lookup on this connection, and guessing interest IDs gets ads rejected.

**Tier 1 — highest probability**
- Dog owner / Dog (interest)
- Land Rover, Range Rover, Porsche, BMW, Mercedes-Benz, Audi (vehicle brands)
- Car ownership / Vehicle maintenance
- Luxury vehicles / Sport utility vehicle

**Tier 2 — worth testing**
- Auto detailing / Car wash
- New parents / Parents with young children
- Golf, Equestrian, Country sports (Warwickshire affluence proxies)

**Tier 3 — narrow**
- Car leasing / Vehicle finance
- Autotrader, Motors.co.uk (used-car intent)

**How to test them properly:** duplicate the Broad ad set, add one Tier 1 layer, run at equal budget for 7 days, compare cost per landing page view *and* enquiry quality. Do not add interests to the existing Broad ad set — that destroys the control.

---

## Exclusions

- **Exclude past customers** from cold ad sets once a customer list is uploaded to Meta. Nothing wastes local budget faster than advertising a first-visit offer to people who already booked.
- **No age/gender exclusions beyond the above** — no evidence supports them, and narrowing without evidence just raises CPMs.
