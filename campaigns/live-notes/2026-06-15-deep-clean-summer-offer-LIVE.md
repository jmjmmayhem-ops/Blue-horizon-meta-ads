# LIVE — Deep Clean Summer Offer (Meta)

**Went live:** 2026-06-15 ~15:07 UTC
**Account:** 761087688736713 (Bluehorizondetailing – Ad account)
**Status:** ✅ LIVE again (relaunched ~20:25 UTC) with the CORRECT video — spending at £15/day (CBO).

> **2026-06-16 ~08:40 UTC — budget reduced to £5/day.** Overnight result (~12-15h, ~£14 spend): Josh reports **19 leads / £2,850 revenue** (~£0.73 cost-per-lead, ~200x ROAS) — though Meta recorded **0** pixel-Lead conversions (tracking gap: GHL form-submit isn't firing the pixel Lead event; Josh chose not to fix yet). Budget dropped £15→£5/day at Josh's request to let him catch up on bookings (capacity-limited). NOTE: editing the campaign budget via the API force-pauses the campaign — had to re-activate after. Campaign currently ACTIVE at £5/day. Best early creative: V2 - Value Anchor (8.88% CTR, £0.14 CPC).

**Correct video:** `972834505558281` ("deep clean offer ad.mp4", 58s).
**Active ads (correct video):**
- V1 - Summer Fresh — `120248908176840294`
- V2 - Value Anchor — `120248908177930294`
- V3 - Pre-Sale / Pride — `120248908178670294`
- V4 - Inside & Out — `120248908179390294`

> **2026-06-15 saga (resolved):** Original 4 ads went live ~15:07 on the WRONG video (older "DETAILING OFFER AD.mp4" `989139670316049`) and were paused ~16:43 to stop spend. A replacement ID `1019304307482803` was a Page-media video (rejected as invalid). Josh re-uploaded the correct file to the **ad-account** media library → valid video `972834505558281`. Built 4 new ads on it and activated ~20:25. The 4 wrong-video ads were ARCHIVED ~20:36 UTC (per Josh — "anything with the old video can be deleted"): `120248896682740294`, `120248896685590294`, `120248896691560294`, `120248896694110294`. Old video file `989139670316049` left in media (no delete-video API tool); can be removed manually in Ads Manager Media if desired.

## Structure
- **Campaign:** `BH | Meta Leads | Deep Clean Summer Offer | Rugby+20 | 2026-06` — `120248895027620294` — OUTCOME_LEADS, CBO £15/day, ACTIVE
- **Ad set:** `Deep Clean Offer | Age 30+ | Warwickshire | Web Conversions` — `120248895160070294` — ACTIVE
  - Optimisation: OFFSITE_CONVERSIONS → pixel `1404609760266229`, custom_event_type LEAD ("get fast quote")
  - Destination: WEBSITE → https://www.bluehorizondetailing.com/offers/deep-clean-150
  - Targeting: Rugby + 25 miles (custom location), age 30+, Advantage+ audience, automatic placements
- **Ads (all ACTIVE), video `989139670316049`, cover image `976a583605ebf622055cfa2b86b907cd`, CTA GET_OFFER:**
  - V1 - Summer Fresh — `120248896682740294`
  - V2 - Value Anchor — `120248896685590294`
  - V3 - Pre-Sale / Pride — `120248896691560294`
  - V4 - Inside & Out — `120248896694110294`

## Offer (Josh-approved promo)
£150 bundle (Deep Clean + premium paintwork sealant + engine-bay detail), anchored against "normally just over £200". Protection worded as "a few months" (no fixed term). Proof: 4.8★ / 50+ Google reviews.

## Fully owned (agency cord cut)
New campaign, Josh's own uploaded video + cover image, Josh's landing page + GHL form. No Meta instant form / lead-ads ToS dependency. The old agency-origin campaigns remain PAUSED:
- `{BHD} - Valeting Campaign` (OG Deep Clean) — `120244204180640294` — PAUSED
- `Deep clean advert` — `120244741843280294` — PAUSED/archived
- `Detailing campaign` (20% OFF) — `120245747039030294` — PAUSED

## Known caveats / follow-ups
- Optimises toward a **click-based** "get fast quote" Lead event — looser than a true form-submit. TODO: add a Lead event on the GHL form-submit / thank-you page for cleaner optimisation.
- Replace SMS-rescue (lost with instant form) by building a **retargeting audience of landing-page visitors who didn't submit** once traffic builds.
- Conversion learning needs volume; review in 3–4 days, don't judge in the first 24–48h.

## Lead-ads ToS note
Page `110694795276891` ToS confirmed accepted by Josh (page-specific URL), but the MCP connector still reports `leadgen_tos_accepted:false` / page "(unknown)" — a connector permission limit. This is why we went website-destination instead of Meta instant form. If instant-form ads are wanted later via MCP, the connector needs Page + leads permissions re-granted.
