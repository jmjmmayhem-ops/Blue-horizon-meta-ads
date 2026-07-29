# Build Record & Launch Checklist — Deep Clean £150

**Built:** 29 July 2026 · **Status:** 🟡 **DRAFT — everything PAUSED, £0 committed**

---

# 1. What was built

## Campaign
| | |
|---|---|
| Name | `BH \| Meta Leads \| Deep Clean £150 \| Warwickshire \| 2026-07` |
| ID | `120250775729340294` |
| Objective | OUTCOME_LEADS |
| Budget model | **ABO** (budgets at ad-set level) |
| Buying type | Auction |
| Special ad categories | None |
| Status | **PAUSED** |

## Ad sets

**1 · `BH | AS | Broad Warwickshire | LPV | 2026-07`** — `120250775747220294`
- £12.00/day · Landing Page Views · Website destination
- Rugby (52.3705, −1.2646) **+20 miles**
- Age 28–65, all genders · No interest targeting
- Advantage+ Audience **on** (age passed as suggestion)
- Autobid (highest volume)

**2 · `BH | AS | High-Value Areas | LPV | 2026-07`** — `120250775753220294`
- £7.00/day · Landing Page Views · Website destination
- 8 town radii: Leamington Spa (6mi), Warwick (6mi), Kenilworth (5mi), Solihull (6mi), Balsall Common (5mi), Southam (5mi), Dunchurch (4mi), Stratford-upon-Avon (6mi)
- Age **30–65 (hard limit)** · Advantage+ Audience **off** — deliberate, so the geo test stays valid

**3 · `BH | AS | Retargeting Warm | LPV | 2026-07`** — `120250775770610294`
- £6.00/day · Landing Page Views · Website destination
- Rugby +25 miles · Age 25–65
- Custom audiences: Facebook page visitors 180d (`120245714247980294`), Instagram page visitors 180d (`120245714271030294`), Website visitors 180d (`120245714225190294`)
- Advantage+ Audience **off**

**Total: £25.00/day**

## Ads — 12, all PAUSED, all clean (PENDING_REVIEW / IN_PROCESS, zero WITH_ISSUES)

### Broad Warwickshire (7)
| Ad | ID | Image | CTA |
|---|---|---|---|
| Filthy V1 — Your Car Reset | `120250775868470294` | filthy befaft | Book Now |
| Filthy V1 — No More Apologising | `120250775871200294` | filthy befaft | Book Now |
| Filthy V2 — We've Seen Worse | `120250775874700294` | filthy befaft 2 | Book Now |
| Dog Hair — Keep The Dog Lose The Hair | `120250775877050294` | dog hair befaft | Book Now |
| Dog Hair — Remove It Don't Mask It | `120250775882110294` | dog hair befaft | Book Now |
| Mouldy Carpet — Not Just A Smell | `120250775898490294` | mouldy carpet befaft | Book Now |
| Defender — Earns Its Dirt | `120250775900400294` | defender exterior befaft | Book Now |

### High-Value Areas (3)
| Ad | ID | Image | CTA |
|---|---|---|---|
| White Seats — White Leather Restored | `120250775903070294` | white seats befaft | Book Now |
| Taycan — Trusted With Prestige Cars | `120250775908090294` | taycan clean | Book Now |
| Urus — The Method Matters | `120250775910100294` | urus clean | Learn More |

### Retargeting (2)
| Ad | ID | Image | CTA |
|---|---|---|---|
| RT — Still Thinking About It | `120250775912650294` | filthy befaft 2 | Book Now |
| RT — We Come To You | `120250775915990294` | taycan footwell | Book Now |

## Destination URL (all 12 ads)
```
https://www.bluehorizondetailing.com/offers/deep-clean-150
  ?utm_source=meta
  &utm_medium=paid_social
  &utm_campaign=deep-clean-150
  &utm_content={{ad.name}}
  &utm_term={{adset.name}}
  &utm_placement={{placement}}
```

---

# 2. Notes on what changed during the build

**Two images from the original brief were never uploaded** — *Wheel Mid Clean* and *Dirty Footwell*. Their concepts (12A, 12B, 13A, 13B) remain written in the copy bank and can be built in minutes if those images appear.

Concept **13A "You Stopped Noticing"** had a Wave 1 slot in the Broad ad set. With no Dirty Footwell image, I substituted **6A "Earns Its Dirt"** (Defender) — a strong broad-appeal Warwickshire concept.

**Defender copy was rewritten for the actual image.** The original 6A leaned on an interior reset; Josh's description confirms the shot is *exterior, very muddy, safe wash*. The live copy now leads on snow foam, two-bucket safe wash, non-acidic wheel products and decontamination — matching what the picture actually shows. An ad whose copy contradicts its image is the fastest way to lose trust.

**Retargeting image swapped** — 9B "We Come To You" was written for the Urus; since the Urus is used in the High-Value ad set, the retargeting version uses **taycan footwell** instead, and the copy gained a closing line about footwells, seat rails and seat belts so image and words align.

**Promoted object rejected.** Attaching `{"pixel_id": ...}` to a LANDING_PAGE_VIEWS ad set returned *"Promoted Object Invalid"*. Removed — it's optional for this goal, and Meta reads landing page views from the pixel on the destination page regardless. No impact.

---

# 3. 🔴 New finding — the website custom audience has ~20 people

The audience list shows **"website visitors 180 days" at roughly 20 people**, despite weeks of traffic from a campaign running 4–5% CTR at £0.11–0.13 per click. By contrast, the Facebook and Instagram page audiences both sit at 1,000+.

That gap is hard to explain by anything other than **the pixel barely firing on the website at all** — not just the missing Lead event, but potentially base PageView too. If PageView isn't firing reliably, then Landing Page Views optimisation is also degraded, and this becomes the highest-priority item in the whole project.

**Check before launch:** open the offer page with Meta Pixel Helper and confirm PageView fires. Five minutes, and it changes what we do next.

Because of this the retargeting ad set leans on the FB/IG engagement audiences, which are healthy, rather than the website audience alone.

---

# 4. Pre-launch checklist

### 🔴 Must be done before spending anything
- [ ] **Verify the pixel fires PageView** on the offer page (Meta Pixel Helper). See §3 — this is the big one.
- [ ] **Verify GHL captures UTM fields** on the contact record. Without this there is no attribution at all while the pixel is compromised. Submit a test form via an ad-style URL and confirm the values land.
- [ ] **Decide on the auction conflict** — pause the existing £20/day Deep Clean campaign, or accept bidding against ourselves. *(Recommendation: pause it. Josh's call — I have not touched it.)*
- [ ] **Confirm the £150 offer is live on the page** and matches the ads exactly.

### 🟠 Strongly recommended before launch
- [ ] Landing page: form above the fold on mobile, or a sticky Book button
- [ ] Landing page: reduce to 4 fields (name, phone, postcode, vehicle)
- [ ] Landing page: 4.8★ / 50+ reviews visible beside the form
- [ ] Add a WhatsApp option alongside the form
- [ ] Check for `0+` / `0.0★` placeholder counters on mobile
- [ ] Set up the thank-you page + Lead event (unlocks the whole optimisation upgrade)

### 🟢 Operational
- [ ] Diary capacity to absorb 3–5 extra Deep Cleans per week
- [ ] Reply process for enquiries — speed is the biggest booking driver
- [ ] Lead tagging agreed: booked / quoted not booked / out of area / price shopper / no response

### Final settings verification — ✅ all confirmed
- [x] Campaign objective OUTCOME_LEADS, ABO, no special ad category
- [x] 3 ad sets, correct budgets (£12 / £7 / £6 = £25/day)
- [x] All optimising for Landing Page Views, website destination
- [x] Geo correct — Rugby+20, 8 high-value towns, Rugby+25 for retargeting
- [x] Age gates correct; Advantage+ Audience off where the test requires it
- [x] 12 ads, correct ad-set distribution (7 / 3 / 2)
- [x] Every ad carries full UTM string
- [x] No WITH_ISSUES on any ad
- [x] Preview renders correctly — before/after stacked vertically, no graphic clutter
- [x] Copy complies: no invented claims, no banned words, review claim accurate (4.8★, 50+), price presented as "Usually £180. Currently £150."
- [x] **Everything PAUSED — £0 spent**

---

# 5. To launch

Say the word and I'll activate campaign → ad sets → all 12 ads, top-down. Nothing spends until then.

**Recommended launch sequence:**
1. Fix pixel PageView (§3) — or knowingly accept degraded optimisation
2. Confirm GHL UTM capture
3. Pause the old Deep Clean campaign
4. Activate this campaign
5. **Hands off for 5–7 days**
6. Day 7 review per `04-TESTING-SCALING-KPIS.md`
