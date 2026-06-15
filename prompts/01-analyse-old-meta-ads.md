# Prompt 01 — Analyse Old Meta Ads

Use this prompt to review past Blue Horizon Meta campaigns, ad sets and ads and decide what to keep, kill or change.

---

## Before you start
Read `knowledge/blue-horizon-detailing-master-business-knowledge.md` and `knowledge/meta-ads-operating-rules.md`.

## Prompt

```text
Analyse the Blue Horizon Meta Ads performance I am about to give you (pasted data or connected account).

For the period [DATE RANGE], break down at campaign, ad set and ad level:

1. Spend.
2. Reach and impressions.
3. Frequency (flag creative fatigue if frequency is climbing and CTR is dropping).
4. CTR and CPC.
5. Leads / messages / link clicks.
6. Cost per lead (and cost per booked job if Josh provides it).
7. Lead quality if known (good / poor / no response / booked / out of area / price shopper / wrong service / spam).
8. Best-performing creative and hook.
9. Worst-performing creative and hook.
10. Best-performing service angle (deep clean vs paint correction vs ceramic vs proof, etc.).
11. Best-performing audience and placement.
12. Best-performing destination (Meta lead form vs WhatsApp vs website vs landing page).
13. Wasted spend and where it went.

Then summarise:
- What worked and why.
- What failed and why.
- What to scale, keep, refresh or kill.

Constraints:
- Use only real Blue Horizon services, pricing, areas and proof from the knowledge files.
- Keep the brand premium and local. No "cheap"/"budget" angles.
- Do not include SMART repair or alloy refurbishment analysis unless Josh has explicitly asked for those campaigns.
- Do not make any change to the live account. Recommend only.

Present every recommendation in this format:

RECOMMENDATION:
WHY:
RISK:
EXACT CHANGE:
STATUS: APPROVE / REJECT / EDIT
```

## After analysis
- If Josh wants a written record, save the analysis to `reports/weekly/` (or `reports/monthly/` for longer periods).
- Carry the winning angles/destinations forward into Prompt 02 (new campaign draft).
