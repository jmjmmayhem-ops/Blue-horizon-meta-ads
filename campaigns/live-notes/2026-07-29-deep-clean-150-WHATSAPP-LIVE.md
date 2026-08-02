# Deep Clean £150 — WhatsApp Version — LIVE

**Switched:** 29 July 2026, on Josh's instruction — *"change all of the objectives to every creative to WhatsApp now with prefilled message instead… copy every campaign, audience, and creative and every variant perfectly."*

## Why we switched
The landing page campaign delivered excellent ad metrics (2.44% link CTR, £0.19 per landing page view, 49 landing page views) but **zero enquiries**. That matches weeks of the same pattern on the previous Deep Clean campaign: cheap clicks, strong CTR, almost no form fills. The bottleneck is the page and the broken Lead event, not the ads.

WhatsApp also **fixes the tracking problem rather than working around it** — Meta receives "conversations started" natively, so the algorithm optimises on a real outcome instead of the landing-page-view proxy.

## Actions taken
1. **PAUSED** landing page campaign `120250775729340294` — final spend **£9.24**, 2,414 impressions, 59 link clicks, 49 landing page views, 0 enquiries. Kept, not deleted, so it can be revived if the page is fixed.
2. **Built and launched** a complete WhatsApp duplicate.

## New campaign
| | |
|---|---|
| Name | `BH \| Meta Messages \| Deep Clean £150 \| Warwickshire \| 2026-07` |
| ID | `120250777694170294` |
| Objective | OUTCOME_ENGAGEMENT → Messages |
| Optimisation | **CONVERSATIONS** |
| Destination | **WhatsApp** — 07818 514079 |
| Budget | £25/day (ABO, unchanged) |

**Pre-filled message — general, not ad-specific (per Josh):**
```
Hi Josh, I'd like a quote for the Premium Deep Clean offer. Here's my car and postcode:
```
Deliberately generic — someone who clicked the dog-hair ad doesn't open WhatsApp talking about dog hair. The trailing prompt gets vehicle + postcode in the first message so Josh can quote immediately. Plain text, no pre-encoding (avoids the `%2520` double-encoding bug hit on the SMART campaign).

## Ad sets — mirrored exactly from the landing page version
- `120250777701660294` **Broad Warwickshire** — £12/day · Rugby+20mi · 28–65 · A+ Audience on · **7 ads**
- `120250777705080294` **High-Value Areas** — £7/day · same 8 town radii · 30–65 hard cap · A+ Audience off · **3 ads**
- `120250777707080294` **Retargeting Warm** — £6/day · same 3 custom audiences · Rugby+25mi · 25–65 · **2 ads**

## Ads — all 12 copied, all ACTIVE
| Ad set | Ad | ID |
|---|---|---|
| Broad | Filthy V1 — Your Car Reset | `120250777741820294` |
| Broad | Filthy V1 — No More Apologising | `120250777744880294` |
| Broad | Filthy V2 — We've Seen Worse | `120250777746810294` |
| Broad | Dog Hair — Keep The Dog Lose The Hair | `120250777750190294` |
| Broad | Dog Hair — Remove It Don't Mask It | `120250777752190294` |
| Broad | Mouldy Carpet — Not Just A Smell | `120250777754690294` |
| Broad | Defender — Earns Its Dirt | `120250777756320294` |
| High-Value | White Seats — White Leather Restored | `120250777757620294` |
| High-Value | Taycan — Trusted With Prestige Cars | `120250777759670294` |
| High-Value | Urus — The Method Matters | `120250777761970294` |
| Retargeting | RT — Still Thinking About It | `120250777763770294` |
| Retargeting | RT — We Come To You | `120250777765890294` |

**Body copy, headlines, descriptions and images are byte-identical to the landing page version.** No delivery issues on any ad.

## Two forced changes
1. **All CTAs are now "Send Message."** A WhatsApp Messages campaign accepts no other CTA — Meta creates ads with other buttons then blocks them at delivery with *"Invalid Creative For Objective"* (this cost a rebuild on the SMART campaign). The Urus ad was "Learn More" and is now "Send Message" like the rest.
2. **UTM parameters dropped** — meaningless for a WhatsApp destination. Attribution is now Meta's native conversation reporting, which is more reliable than the UTM workaround ever was.

---

## What changes about measurement — this is the upgrade

| | Landing page version | WhatsApp version |
|---|---|---|
| Optimises on | Landing page views (proxy) | **Conversations started (real)** |
| Meta sees the outcome | ❌ No | ✅ Yes |
| Attribution | UTMs into GHL (unverified) | Native, per-ad |
| Cost per result | Not measurable | **Directly reported** |

For the first time, cost per enquiry will be visible per ad in Meta.

## Watch items
- **Reply speed is now the biggest driver of bookings.** Minutes, not hours.
- **Expect more volume and more tyre-kickers** than a form produces. Every message costs Josh a reply — if it gets noisy, tighten the copy to pre-qualify harder.
- **Verify the pre-fill renders** by tapping a live ad — the text should appear in WhatsApp with normal spaces, no `%20`.
- Tag conversations: booked / quoted not booked / out of area / price shopper / no response.

## Day 7
Pause the worst performer on cost per conversation, note the winner. Judge on **booked jobs**, not message count. Both dog-hair ads led the landing page version on efficiency (£0.08–0.10 per landing page view) — worth watching whether that holds now the goal has changed.

---

# UPDATE — Native WhatsApp attribution fix (29 Jul)

## The problem
After ~£50 across both WhatsApp campaigns (Deep Clean + SMART Repairs) and 183 link clicks, Meta recorded **0 conversations started** — while Josh confirmed he **had actually received messages**. So the ads worked; Meta simply could not see the outcome, leaving the CONVERSATIONS optimisation goal with no signal to learn from.

## Root cause
The creatives used a plain **`wa.me` outbound link**. That hands the user to WhatsApp but gives Meta no way to observe what happens next, so conversations always report zero.

Native click-to-WhatsApp requires the creative's call-to-action to carry **`app_destination: "WHATSAPP"`**, which the `ads_create_creative` tool does not expose. The fix was to build the creative inline through `ads_create_ad` using a raw `object_story_spec`:

```json
"call_to_action": {
  "type": "WHATSAPP_MESSAGE",
  "value": {
    "app_destination": "WHATSAPP",
    "link": "https://api.whatsapp.com/send?phone=447818514079&text=<prefill>"
  }
}
```

**Tested first on a single ad before touching anything live.** Confirmed two things: the structure validates, and the `?text=` prefill survives — so we keep native attribution *and* the car+postcode prompt.

## Action taken
Rebuilt all 12 ads with the native structure (`DCWA-N -` prefix), activated them, and paused the 12 `wa.me` versions. Same images, same copy, same ad sets, same budgets — only the WhatsApp wiring changed.

| Ad set | Native ads |
|---|---|
| Broad Warwickshire | `120250847782370294`, `120250847782940294`, `120250847783650294`, `120250847785320294`, `120250847780760294`, `120250847786510294`, `120250847786980294` |
| High-Value Areas | `120250847788160294`, `120250847789110294`, `120250847789550294` |
| Retargeting | `120250847792330294`, `120250847793660294` |

All 12 ACTIVE, no delivery issues. Old `wa.me` ads paused, not deleted.

## What to verify in 24h
**Do conversations now register in Meta?** If yes, the fix worked and Meta can finally optimise toward people who actually message. If they still read zero, the next suspect is the WhatsApp Business account connection in Business Settings, not the creative.

## Still outstanding
SMART Repairs (`120250773503190294`) still runs the old `wa.me` structure and will keep reporting 0 conversations. Apply the same fix once confirmed working on Deep Clean.

---

# UPDATE — Budget cut to £20/day total (29 Jul)

Josh: *"cut total ad budget to £20 a day"* — account-wide, not per campaign.

| Campaign | Ad set | Was | Now |
|---|---|---|---|
| Deep Clean | Broad Warwickshire | £12 | **£7** |
| Deep Clean | High-Value Areas | £7 | **£4** |
| Deep Clean | Retargeting Warm | £6 | **£3** |
| SMART Repairs | Warwickshire 24–65 | £10 | **£6** |
| | **TOTAL** | **£35** | **£20** |

Deep Clean now £14/day, SMART Repairs £6/day. Proportional cut, structure unchanged.

## Flagged risk — spread is now too thin
Four ad sets sharing £20/day. Meta needs roughly 50 optimisation events per ad set per week to exit learning; at £3–7/day none of these will get near that, so all four will likely sit in "Learning Limited" indefinitely and delivery will stay erratic.

**Recommendation (not actioned — needs Josh's approval):** consolidate rather than spread.
- Pause **Retargeting Warm** (£3/day is below the threshold where a small warm audience can deliver; it was also the most expensive per click at £0.63) and fold its budget into Broad.
- That gives Broad £10, High-Value £4, SMART £6 — three ad sets, one of them properly fed.

Better to run two or three ad sets well than four badly.

---

# UPDATE — Scheduled stop at 23:00, 2 Aug 2026

Josh: *"pause all the ads we set up at 11pm tonight and then we will get the new proper ones rebuilt properly with specific services tied to them."*

**Date check:** verified against Meta's own clock via `created_time` on a just-created ad — **2026-08-02T17:05:01+0100**. Note that Meta's auto-generated creative names carry "2026-07-29", which is a naming quirk, not the real date. Worth checking before ever scheduling anything.

## Action
Set `stop_time = 2026-08-02T23:00:00+0100` on both live campaigns:
- Deep Clean WhatsApp `120250777694170294`
- SMART Repairs `120250773503190294`

**Gotcha:** setting `stop_time` via `ads_update_entity` **forces the entity to PAUSED immediately** (`status_forced_to_paused: true`). Both campaigns were reactivated straight after so they keep delivering until 23:00 as intended. Anyone repeating this must re-activate after setting a stop time.

**Verification limitation:** `stop_time` is not readable back through `ads_get_ad_entities` at campaign level, so the setting could not be confirmed programmatically. A one-shot session task was scheduled for 23:02 to check both campaigns and hard-pause anything still delivering. That task is session-only and dies if the session ends — so the Meta-side stop time remains the primary mechanism.

## Next
Rebuild as service-specific campaigns. Two are already built and paused (`campaigns/drafts/2026-07-service-campaigns/`): Maintenance Valet from £80, New Car Protection from £675. Remaining services are blocked on proof imagery — see the shot list in that folder.

---

# UPDATE — ALL ADS PAUSED (2 Aug 2026, ~17:20 BST)

Josh: *"pause all ads"* — brought forward from the planned 23:00 stop.

**Account state: nothing is delivering. All 7 campaigns PAUSED, verified.**

| Campaign | ID | Status |
|---|---|---|
| Deep Clean £150 — WhatsApp | `120250777694170294` | PAUSED |
| SMART Repairs — WhatsApp | `120250773503190294` | PAUSED |
| New Car Protection from £675 (draft) | `120250858244190294` | PAUSED |
| Maintenance Valet from £80 (draft) | `120250858231370294` | PAUSED |
| Deep Clean £150 — landing page | `120250775729340294` | PAUSED |
| Deep Clean Summer Offer — Traffic (Jun) | `120249175039720294` | PAUSED |
| Deep Clean Summer Offer — Leads (Jun) | `120249137713000294` | PAUSED |

The scheduled 23:02 safety-net task was removed — no longer needed.

## Where things stand for the rebuild

**Assets ready to reuse:** 11 labelled images, a 28-concept copy bank (`campaigns/drafts/2026-07-deep-clean-150/02-CREATIVE-STRATEGY-AND-COPY.md`), and two service campaigns already built (Maintenance Valet, New Car Protection).

**The working pattern to repeat per service:**
1. One campaign per service — OUTCOME_ENGAGEMENT → CONVERSATIONS → WhatsApp
2. Creative built inline via `ads_create_ad` with `object_story_spec` so `app_destination: WHATSAPP` can be set (attribution does not work without it)
3. Service-specific prefill in the link's `?text=`, plain text, never pre-encoded
4. CTA must be `WHATSAPP_MESSAGE` — no other CTA survives delivery on this objective
5. "From £X" in the copy to pre-qualify

**Known-good performance signals to carry forward:**
- Dog Hair "Remove It Don't Mask It" — best Deep Clean performer (£0.10 per landing page view, 52% of delivery)
- Door Scratch 4A — best SMART performer (£0.27/click, beat both bumper angles)
- Embarrassment and specific-problem angles consistently outperformed premium/aspirational ones

**Open questions for the rebuild:**
- Does the native WhatsApp fix actually register conversations? Never confirmed — the ads were paused within hours of going live.
- Does the ad-level prefill come through, or does Meta override with its default?
- Images still needed: swirl before/after, headlight one-done-one-not, kerbed alloy, water beading.
