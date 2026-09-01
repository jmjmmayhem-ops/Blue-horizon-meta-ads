# Deep Clean VIDEO Campaign + Lead Form Spec

**Built:** 2 August 2026 · **Status:** 🟡 PAUSED (draft) — £0 spent

---

# The video campaign — BUILT

**Campaign:** `BH | Meta Messages | Deep Clean VIDEO | Affluent Rugby+20 | 2026-08` — `120250990582200294`
Messages → WhatsApp → **Conversations** · native `app_destination` attribution

**Ad set:** `120250990589010294` — **£12/day** · age **30–65 hard cap** · Advantage+ Audience **OFF** (so the affluent geo actually holds)

**Video:** `deep clean offer ad.mp4` (`972834505558281`) — the original Summer Offer video.

## Targeting — affluent areas *inside* Rugby +20 miles
Rather than a blanket 20-mile radius (which sweeps in everything), eight tight radii on the affluent towns that fall within it:

| Town | Radius |
|---|---|
| Leamington Spa | 5 mi |
| Warwick | 5 mi |
| Kenilworth | 4 mi |
| Balsall Common | 4 mi |
| Southam | 4 mi |
| Dunchurch | 3 mi |
| Rugby | 4 mi |
| Lutterworth | 4 mi |

*Solihull and Stratford were excluded — both sit ~22 miles out, outside the brief.*

## The 8 variations — same video, eight different arguments

| Ad | ID | Angle |
|---|---|---|
| DCV1 Value Anchor | `120250990638380294` | Price-led: "Usually £180. Currently £150." |
| DCV2 Not A Car Wash | `120250990652580294` | Category reframe — defends the premium |
| DCV3 No More Apologising | `120250990663580294` | Embarrassment (top performer historically) |
| DCV4 We Come To You | `120250990680350294` | Convenience — "we bring the water, you need a socket" |
| DCV5 Trusted With Prestige | `120250990708420294` | Rolls-Royce/Lambo/Porsche trust transfer |
| DCV6 Real Review Claire T | `120250990744480294` | Real named customer review as the hook |
| DCV7 Selling Your Car | `120250990789500294` | Pre-sale / part-ex / handback deadline |
| DCV8 Dog Owners | `120250990845420294` | Best-performing angle in the account |

All 8 clean, no delivery errors. Thumbnails vary by angle (filthy interior, dog hair, Taycan, Urus, white seats).

## Two corrections made to the original copy

**1. The £200 anchor was dropped.** The old Summer Offer ads said *"normally just over £200."* The live site says Deep Clean is **from £180**. Advertising a £200+ anchor against a £180 list price isn't defensible, so every variant now uses **"Usually £180. Currently £150."**

**2. Emoji-heavy formatting removed.** The originals opened with 🔥 ATTENTION WARWICKSHIRE DRIVERS 🔥 and ✅ bullet lists. That conflicts with the brand rules (premium, calm, no excessive emoji, no shouting). Rewritten in the current voice.

*If Josh wants the old emoji style tested as a control, say so — it's a legitimate test and one variant could carry it.*

---

# The lead form — BLOCKED, twice

## Blocker 1: Lead Gen Terms of Service not accepted
Verified just now:
```
page_id: 110694795276891  ·  leadgen_tos_accepted: FALSE
```
**No lead form ad can be created until this is accepted.** Josh must accept at **https://www.facebook.com/legal/leadgen/tos** — two minutes, one-off.

## Blocker 2: no MCP tool creates Instant Forms
This connection exposes campaign, ad set, ad, creative and audience tools — **but nothing that creates a lead form**. The form must be built by Josh in **Ads Manager** or **Page → Publishing Tools → Forms Library**. Once it exists I can reference its `form_id` and build everything around it.

---

# Lead form spec — ready to build

Recommended settings once ToS is accepted:

**Form type:** **More volume** (fewer steps) — *not* Higher intent. Josh replies personally anyway, so the qualifying happens in conversation.

**Intro screen**
- Headline: **Premium Deep Clean — Usually £180, Currently £150**
- Image: the filthy before/after
- Body: *A complete reset, inside and out. Seats and carpets shampooed and extracted, A/C sanitised with steam, full decontamination and ceramic paint protection lasting 6–8 months. We come to you across Warwickshire — we bring our own water, you just need a socket.*

**Questions — keep it to four**
1. Full name *(prefilled)*
2. Phone number *(prefilled)*
3. Postcode — *custom, short answer*
4. Car make and model — *custom, short answer*

*Deliberately no email.* Every extra field costs completions, and Josh quotes by phone/WhatsApp.

**Privacy policy:** https://bluehorizondetailing.com/privacy

**Completion screen — this is the important bit**
- Headline: **Thanks — Josh will be in touch shortly**
- Body: *Usually within a few hours, same day almost always. Want a price faster? Message Josh directly.*
- Button: **Message on WhatsApp** → `https://api.whatsapp.com/send?phone=447818514079&text=Hi Josh, I'd like a quote for the Premium Deep Clean offer. Here's my car and postcode:`

**Why a WhatsApp button and NOT the website form:** sending someone to the GHL form after they've already completed a lead form asks them to fill in a form twice — and that form measured **49 landing page views → 0 enquiries**. The WhatsApp button captures the data *and* gives keen people a fast route through.

---

# Lead delivery — the operational risk

**WhatsApp lands on Josh's phone. Lead forms sit in a dashboard.** For a solo operator where response speed is the biggest booking driver, that difference is the whole ballgame.

If the lead-form test goes ahead, **connect the form to email or GHL before spending a penny**, so leads don't sit unseen in Ads Manager. An unread lead is a lost job.

---

# Next

1. Josh accepts Lead Gen ToS
2. Josh builds the form to the spec above (or asks me to walk him through it)
3. Josh sends me the `form_id`
4. I build a parallel lead-form ad set in this campaign and run it head-to-head against WhatsApp — same video, same targeting, same budget. Clean test.

---

# UPDATE — 6 more variants added (14 total)

Josh: *"need more variants for different people purposes ect to get forms filled."*

Six additional angles, each aimed at a different person and a different reason to book:

| Ad | ID | Who it targets |
|---|---|---|
| DCV9 Parents Family Car | `120250991639850294` | Parents — crumbs, spills, seat rails |
| DCV10 Van & Business Owners | `120250991759680294` | Tradespeople, mobile businesses — **"your van is your advert"** |
| DCV11 Busy Professionals | `120250991796100294` | Time-poor — "your Saturday back" |
| DCV12 Just Bought Used Car | `120250991822830294` | New owners — hygiene/ownership moment |
| DCV13 Smoke & Odour | `120250991873680294` | Smokers, pet owners, damp — odour at source |
| DCV14 Holiday Road Trip | `120250991888910294` | Seasonal — pre-trip prep |

**DCV10 is the one to watch.** The van/business angle is completely untapped locally, it's backed by a real named review (Sarah M.'s dog-grooming van), and business owners expense vehicle presentation rather than treating it as discretionary spend. Nobody in the Warwickshire ad library is targeting it.

**All 14 clean** — no delivery errors. Still PAUSED, £0 spent.

## ⚠️ 14 ads on £12/day is a problem

Roughly **£0.86 per ad per day**. Meta needs ~£15 of spend per ad to form a verdict, so a full read on all fourteen would take **two-and-a-half weeks**.

What will actually happen: Meta concentrates delivery on 2–3 winners within days and barely serves the rest. That's not useless — it *does* surface a winner — but it isn't the "test everything" outcome the variant count implies.

**Three options:**
1. **Raise to £25–30/day** — gives a genuine read on all 14 in about a week
2. **Launch 6–7 now, hold the rest as a refresh pool** — proper test, staged
3. **Run all 14 at £12** and accept Meta picks the winners fast

Recommendation: **option 2**. Launch DCV1, 3, 6, 8, 10, 13 — value anchor, embarrassment, real review, dog owners, van/business, odour. Widest spread of distinct buyers, each properly fed. Rotate the rest in at day 14 as fatigue defence.

## On "getting forms filled"
These all currently point at **WhatsApp**, because the lead form is still blocked on the Lead Gen ToS (see above). **Every one of these variants is reusable** — once the form exists, the same 14 creatives can be duplicated into a lead-form ad set unchanged. No copy is wasted.

---

# UPDATE — Lead form campaign (2 Aug)

Josh: *"no I dont want whatsapp i want lead forms only."*

**Lead form ID supplied by Josh: `1563796925239788`**

**Campaign built:** `BH | Meta Leads | Deep Clean VIDEO | Affluent Rugby+20 | 2026-08` — `120250992441180294` (OUTCOME_LEADS, PAUSED)

**Ad set: BLOCKED.** Two attempts, same rejection both times:
```
Terms of Service Not Accepted: You can't run lead ads until your
Facebook Page accepts Facebook's Lead Generation Terms of Service.
error_subcode: 1815089
```

## Diagnosis
- `ads_get_ad_account_pages` → **Blue Horizon Detailing** (`110694795276891`), `leadgen_tos_accepted: **false**`
- `ads_get_user_pages` → **only one Page exists**, so there is no Page mismatch and no wrong-account theory

**Why the form saved but the ad set didn't:** creating an Instant Form does **not** require the Lead Gen ToS. *Running* lead ads does. So a form can exist on a Page that hasn't accepted — which is exactly the state here. Josh seeing "approved" on his screen is likely acceptance at user/business level, not on this specific Page.

## The fix
Accept the Lead Gen ToS **as an admin of the Blue Horizon Detailing Page specifically**:
- https://www.facebook.com/legal/leadgen/tos (select the Page when prompted), **or**
- Build one lead ad set manually in Ads Manager — Meta shows an inline "Accept Terms" prompt in context, which is the most reliable way to hit the right Page.

**Workaround if the ToS link keeps misbehaving:** Josh creates the ad set manually in Ads Manager (targeting per spec above), then I add all 14 ads to it via API. Only the ad set needs the UI.

## Ready to go the moment it clears
All 14 creatives exist and transfer unchanged — only the CTA and destination swap from WhatsApp to `LEAD_GENERATION` + form `1563796925239788`.
