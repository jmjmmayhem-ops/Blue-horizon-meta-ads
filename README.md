# Blue Horizon Detailing — Meta Ads Control Workspace

Private control workspace for running **Blue Horizon Detailing** Meta Ads (Facebook + Instagram) with Claude Code.

This repo is where Meta campaigns, ad sets, ads, lead forms, creative briefs and optimisation reports are drafted, reviewed and stored. Nothing here is published automatically — Josh approves every action.

> **Scope:** Meta Ads only. Blue Horizon Detailing only. No Google Ads files belong here.

---

## How to use

1. Open this repo in Claude Code.
2. Claude reads `CLAUDE.md` (operating brief) and the knowledge files automatically.
3. Use a prompt from `prompts/` for the task (analyse, draft, optimise, brief, lead form).
4. Claude produces drafts/reports and saves them to the correct folder.
5. Josh reviews each recommendation as **APPROVE / REJECT / EDIT**.
6. Josh implements approved changes in Meta Ads Manager. Claude never publishes.

---

## Repo structure

```text
CLAUDE.md                         Operating brief Claude follows every session
knowledge/
  blue-horizon-detailing-master-business-knowledge.md   Source of truth (business)
  meta-ads-operating-rules.md     Meta-specific rules, approval format, guardrails
assets/
  photos/                         Vehicle / service photos
  videos/                         Campaign videos Josh supplies
  before-after/                   Before/after proof images
  logos/                          Brand logos
campaigns/
  drafts/                         New campaign drafts awaiting decision
  approved/                       Drafts Josh approved
  rejected/                       Drafts Josh rejected
  live-notes/                     Notes on what is currently live
reports/
  weekly/                         Weekly optimisation reports
  monthly/                        Monthly reports
prompts/
  01-analyse-old-meta-ads.md
  02-draft-new-meta-campaign.md
  03-weekly-meta-optimisation.md
  04-meta-creative-brief.md
  05-meta-lead-form-builder.md
```

---

## Core rules (full detail in `CLAUDE.md` and `knowledge/meta-ads-operating-rules.md`)

- Always read `knowledge/blue-horizon-detailing-master-business-knowledge.md` first — it is the source of truth for services, pricing, areas, voice, proof and offers.
- Do not publish, pause, delete, change budgets, billing or tracking, or change live forms/landing pages without Josh's explicit approval.
- Keep Blue Horizon premium and local. No "cheap"/"budget" positioning.
- Prioritise Warwickshire, Rugby + 20 miles, and high-revenue areas.
- Static/image ads use higher-end vehicle proof. Video ads use the specific video Josh provides.
- **SMART repairs** and **alloy refurbishment** are live from 1 July 2026 but are on ad-hold — do not advertise them until Josh explicitly asks.
- Review proof only as **4.8-star Google rating / 50+ Google reviews**.
- Present every recommendation as **APPROVE / REJECT / EDIT**.

---

## Security

- Never commit API keys, access tokens, OAuth secrets, Meta tokens, pixel secrets or any credentials.
- MCP/connector credentials stay in Claude/connector settings, never in this repo.

---

## Key contacts and links

- Website: https://www.bluehorizondetailing.com/
- Phone / WhatsApp: 07818 514079
- Owner/operator: Josh May
- Base: Rugby, Warwickshire
