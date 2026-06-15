# LIVE — Deep Clean Summer Offer (Meta)

**Went live:** 2026-06-15 ~15:07 UTC
**Account:** 761087688736713 (Bluehorizondetailing – Ad account)
**Status:** ⏸️ PAUSED (delivery stopped ~16:43 UTC) — wrong video was used; awaiting correct ad-account video before relaunch. NOT spending.

> **2026-06-15 ~17:00 UTC update:** The 4 ads went live ~15:07 then were found to use the wrong video (an older "DETAILING OFFER AD.mp4", `989139670316049`). All 4 ads were paused to stop spend. Josh supplied a replacement video ID `1019304307482803`, but Meta rejects it as "not a valid video_id" and it never appears in the ad-account media list — almost certainly a Page video ID, not an ad-account video. Campaign + ad set remain ACTIVE but have **zero active ads, so nothing is delivering or spending**. Relaunch is blocked until a valid **ad-account** video is available. To fix: upload the deep-clean video directly in Ads Manager → Media (ad account), then use that video's ID. The 4 paused ads (V1–V4) are listed below and will be replaced with correct-video versions on relaunch.

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
