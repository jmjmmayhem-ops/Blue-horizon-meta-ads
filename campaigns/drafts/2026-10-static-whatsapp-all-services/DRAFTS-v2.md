# v2 designed creatives (3 Oct 2026, evening) — REPLACES the v1 ads above

Josh: "I'm gonna start expecting all of the ads that you made to look like this" (his Refined Correction sample: dark navy, logo, big white/blue headline, photo panel, warranty badge, kicker line, price block with strike-through, GET MY QUOTE button, fine print). All ads were rebuilt in that style from his own Drive library (1,559 photos reviewed; shortlist and layout in the meta-ads repo `designed-spec.json`).

**Owner rules applied (3 Oct):** no SMART repair ads at all; "best cars, best pictures" (Rolls-Royce Wraith and Spectre, Bentley Continental GT and Mulsanne, Porsche 911 GT3 and Turbo, Audi TT RS, Defender, G63, Cullinan collection shot); **every number plate pixelated exactly on the plate quadrilateral only** (OpenCV plate detection inside a hand-set region, checked by eye for all 22 plates; two ads re-cropped so the plate is out of frame).

**State in Ads Manager (draft, nothing published, campaigns still PAUSED):**
- 32 new `v2` ads created in the same 13 ad sets, all VALIDATED. 31 of the 32 old v1 ads set to DELETED in the draft; the old **RC1 v1 (ad 120251919588800294) could not be deleted (permission denied), Josh to delete it when publishing.**
- MV3 v2 (Range Rover "Valeted on your driveway") was not built: the image upload was refused by the permission layer. Maintenance Valet runs with 2 ads (Rolls Wraith, Bentley GT).
- SMART Repairs: a draft campaign + ad set was created before Josh said no; Meta refuses to delete an unpublished draft, so it is PAUSED and renamed `ZZ DISCARD | SMART Repairs ...` (campaign 120251923770910294). Discard it in the draft.
- Creatives, renderer (`render.py`, Pillow) and plate tool (`plates.py`, OpenCV) are in the meta-ads repo branch `claude/designed-creatives-2026-10`, folder `campaigns/drafts/2026-10-static-whatsapp-all-services/` (commit 4c6ec2a). Meta fetched the images from that branch's raw URLs. The 35 earlier (unblurred) uploads from commit 35936b4 sit unused in the image library; delete them there if wanted.
- Copy, prefills, targeting and budgets unchanged from v1 (see above). PC1 body no longer mentions SMART repairs.

| Ad | Headline on image | Sub-line | Price block | Drive photo(s) | Draft ad ID | Image hash |
|---|---|---|---|---|---|---|
| DC1 | DEEP CLEAN INSIDE & OUT | Seats, carpets, every nook and crevice. | Was from £180 / Now from £150 | 20241027_170623.jpg + inset 20241027_110036.jpg | 120251923809750294 | 7c7f0763a087444ddcd141a89558129c |
| DC2 | IT'S NOT JUST A SMELL | We go to the source. Shampoo and extraction. | Was from £180 / Now from £150 | 20241027_170713.jpg + inset 20260917_081614.jpg | 120251923809780294 | 0bed8727e5dfb2d2330d9db3502af2d4 |
| DC3 | FAMILY CAR? WE'VE SEEN WORSE. | Crumbs, mud, spills and stains. Gone. | Was from £180 / Now from £150 | 20260928_151709.jpg + inset 20241027_110026.jpg | 120251923809810294 | 9ef5e245f752c08d3c1a159a38307b87 |
| MV1 | MAINTENANCE VALET | Inside and out, on your driveway. | From £80 | 20260225_125711.jpg | 120251923809840294 | 4ebccc9ca14cb73de514467896ceddf3 |
| MV2 | KEEP IT LOOKING NEW | Regular valets at your home or work. | From £80 | 20260225_171600.jpg | 120251923809870294 | f5cc098680fbbafef1fa9603727605bb |
| MP1 | MAINTENANCE PLUS | Leather, wheel and glass properly done. | From £110 | 20241025_131647.jpg | 120251923809900294 | 6fe58716921d5d39111bcb8de4cbee34 |
| MP2 | THE BITS YOU TOUCH EVERY DAY | Steering wheel, leather, inside glass. | From £110 | 20241031_153833.jpg | 120251923809950294 | 4a4b59ea1a3ee4a3d3d81b881b93d61c |
| ED1 | ENHANCEMENT DETAIL | Decon, clay, machine polish, 1-year ceramic. | Was from £495 / Now from £395 | 20260815_110848.jpg | 120251923810030294 | 7becf431719b60650e296fc3ea606e89 |
| ED2 | GLOSS A WAX CAN'T GIVE YOU | Gloss-enhancing polish plus Gyeon ceramic. | Was from £495 / Now from £395 | 20241104_155033.jpg | 120251923810060294 | e22a00a250b11e6a7bd17fa987a694cc |
| ED3 | LOOKING LIKE COLLECTION DAY | Bring the gloss back. Protect it for a year. | Was from £495 / Now from £395 | 20250628_142052.jpg | 120251923810090294 | 1b6b6b8e5ae5bda4a5ec738ce6d1647f |
| RC1 | PAINT CORRECTION + CERAMIC COATING | Deeper gloss. Easier cleaning. | Was from £595 / Now from £495 | 20260914_123022.jpg + inset 20241021_134909.jpg | 120251923810170294 | 072a56a9a79ff5559471fb1329c4bd45 |
| RC2 | YOUR PAINT ISN'T TIRED. IT'S SCRATCHED. | Swirls removed, then sealed for 5 years. | Was from £595 / Now from £495 | 20260815_111047.jpg + inset 20240821_105113.jpg | 120251923810210294 | fb316ddb9414b50821de0c7bef9a5ea7 |
| RC3 | CORRECT IT ONCE. PROTECT IT 5 YEARS. | Gtechniq Crystal Serum Light included. | Was from £595 / Now from £495 | 20241021_221149.jpg + inset 20241021_134909.jpg | 120251923810240294 | 18f96e6578a26069382ecf42d551e24c |
| FF1 | FLAWLESS FINISH | Multi-stage correction. Show-car gloss. | From £745 | file_000000003d60720ab1c8b2aec4252c95.png | 120251923810450294 | 48ef1eb0679eeff1e1567999192b0c31 |
| FF2 | "BEST MONEY I'VE SPENT ON THE CAR" | Real Google review. Flawless Finish Package. | From £745 | 20260815_110353.jpg | 120251923810660294 | c83be49211c171d1175baef76e90d6d3 |
| NCP1 | NEW CAR? PROTECT IT PROPERLY | Paint, glass and wheels coated for 5 years. | From £675 | 20260824_165304_001.jpg | 120251923811040294 | 972e30250462294f369eaef007ff3543 |
| NCP2 | NOT A DEALER ADD-ON | A full day's work on your driveway. | From £675 | 20240913_150314.jpg | 120251923811560294 | d9372946a40436230e47d3f3590ea62d |
| NCP3 | FACTORY-FRESH. KEPT THAT WAY. | Protect it in the first weeks, not after the first winter. | From £675 | 20241011_121254.jpg | 120251923811670294 | 507b8f5a6b26463655943e9a55cc49b5 |
| CC1 | CERAMIC COATING | 1, 3 or 5-year protection. No polishing needed. | From £200 | 20241004_180535.jpg | 120251923811850294 | bfd50a24678a420b2a9ccadd2ee57844 |
| CC2 | WINTER-PROOF YOUR PAINT | Salt, grime and rain slide straight off. | From £200 | 20260824_121925.jpg | 120251923811890294 | 11bda7870c214b5f59b1ddd68afb3afe |
| CC3 | EASIER WASHES FOR YEARS | Half the time. Half the damage. | From £200 | 20241020_230919.jpg | 120251923812020294 | bcb229aaeb1d9a3a6a15a87481cf9054 |
| HL1 | HEADLIGHT RESTORATION | Hazed, yellow lenses restored and re-cleared. | £90 per pair | 20260910_160124.jpg + inset 20240816_140035.jpg | 120251923812060294 | 62ce8f02f22e14b9bea44b9ba1560f57 |
| HL2 | THE £90 FIX THAT SHOWS | Not just polished. Re-cleared to last. | £90 per pair | 20260815_111109.jpg + inset 20240816_140035.jpg | 120251923812140294 | d148a6ec4b40657f94fb4ab3fb13f0c7 |
| ST1 | SOFT TOP CLEAN & PROTECT | Algae and mould out. Waterproofed for a year. | From £100 | 20241007_114534.jpg | 120251923812440294 | 47f1433618fac6314fa00098684a4fe5 |
| ST2 | TREAT FABRIC LIKE FABRIC | Deep clean, dry, re-proof. No pressure washer. | From £100 | 20260225_171618.jpg | 120251923812590294 | 6ccb5edf8f4b02d8e64501cc72103735 |
| CV1 | CARAVAN, CAMPER & MOTORHOME CARE | Washed, decontaminated, protected. | Quoted by size and condition | 20240927_143425.jpg | 120251923812940294 | e7eaf339ddad3bec4669e9143c5b2650 |
| CV2 | CARAVAN CERAMIC COATING | Chalky sides and black streaks, sorted for seasons. | Quoted by size and condition | 20240927_143353.jpg | 120251923813040294 | a5aba16a443185077e2b37d60b43efc0 |
| CMV1 | YOUR VAN IS YOUR ADVERT | Vans and fleets valeted at your premises. | Quoted per vehicle | 20250614_124539.jpg | 120251923813330294 | 993f5e912414c2a8e70ded290a5db14d |
| CMV2 | WORKS HARD. STILL LOOKS SHARP. | Pickups, vans and work trucks. | Quoted per vehicle | 20250713_140638.jpg | 120251923813740294 | ab4196e33413c9b8c8384d2e086ae661 |
| PC1 | PRIVATE COLLECTION CARE | Every car clean, protected and ready to drive. | Bespoke. Quoted per collection. | 20260827_135331.jpg | 120251923814040294 | 5699ca01b5402027f63db7d3be2f8cec |
| PC2 | READY TO DRIVE. EVERY TIME. | Scheduled visits at your property. | Bespoke. Quoted per collection. | 20260824_165159.jpg | 120251923814070294 | ffffb9723a29ed74509a9d8f45b24fa5 |
| PC3 | DISCREET. AT YOUR HOME. | Valet to full correction, one trusted pair of hands. | Bespoke. Quoted per collection. | 20260224_163647.jpg | 120251923814230294 | 858be0392b71ab906754f52a741bf067 |

# v4 creatives (3 Oct 2026, late evening) — owner feedback round 1

Josh's feedback on the v2 preview sheets: headlight ads were not headlight pictures; soft top needed much better pictures; Deep Clean needed more variants and nicer cars with nice interior shots (not the Fords); Maintenance Valet and Maintenance Plus need at least four variants with clean shots of nice and average cars; Enhancement Detail perfect, left alone; Refined Correction good, add more high-end cars; the Audi TT inset was mid-polish not swirls; Flawless Finish needed real clean paintwork shots.

**What changed (23 ads rebuilt or added; ED, NCP, CC, CV, CMV, PC untouched):**
- DC: 5 ads (was 3). All interiors from the nicer cars in the library; the Ford shots are gone. DC1–DC3 v2 replaced, DC4 and DC5 new.
- MV: now 5 ads (MV1, MV2 kept; MV3 Range Rover built this time, MV4 and MV5 added: a mix of premium and everyday cars).
- MP: 4 ads (MP3 and MP4 added, interior and exterior).
- RC: 6 ads (RC2 rebuilt with the TT inset captioned "MID-POLISH"; RC4, RC5 Volvo, RC6 Spectre added).
- FF: 5 ads (FF3–FF5 added, clean reflective paintwork only, no insets).
- HL: both rebuilt on real headlight photos from the website (Range Rover Westminster, Porsche Taycan GTS) with a genuine hazed-lens "BEFORE" inset.
- ST: 4 ads (was 2). ST1 is the website soft-top process shot split into before/after; ST2–ST4 are fabric-hood cars from the Drive library.
- Plates: every visible plate pixelated on its exact quadrilateral (hand-set pixel quads for MV3, MV4, RC5, RC6; see `plate_polys.json`). Checked at 4x zoom.

**Ads Manager state:** 23 new `v4` ads created in the existing ad sets (all DRAFT, no validation errors). The eight v2 ads they replace (DC1–DC3, RC2, HL1, HL2, ST1, ST2) are set to DELETED in the draft. Still outstanding for Josh at publish time: delete old RC1 v1 (120251919588800294) and discard the `ZZ DISCARD | SMART Repairs` draft campaign. Images were fetched by Meta from this branch at commit 98992b9.

| Ad | Headline on image | Sub-line | Price block | Photo(s) | Draft ad ID | Image hash |
|---|---|---|---|---|---|---|
| DC1 | DEEP CLEAN INSIDE & OUT | Seats, carpets, every nook and crevice. | Was from £180 / Now from £150 | 20241004_181226.jpg | 120251924486060294 | 5551331976a9f0c2158d92dedc33e060 |
| DC2 | KEEP THE DOG. LOSE THE HAIR. | Shampoo and extraction, not an air freshener. | Was from £180 / Now from £150 | 20241010_140048.jpg | 120251924486200294 | 094f131c464c0625a95d5fe64201943b |
| DC3 | FAMILY CAR? WE'VE SEEN WORSE. | Crumbs, mud, spills and stains. Gone. | Was from £180 / Now from £150 | 20241031_153915.jpg | 120251924486350294 | 24923ca94ad20053c506cf3988ea3882 |
| DC4 | LIKE NEW INSIDE AGAIN | Leather, carpets, trims, glass, door shuts. | Was from £180 / Now from £150 | 20241030_112741.jpg | 120251924486620294 | 1d2cf86d59badd09b95cc37b59d5be82 |
| DC5 | IT'S NOT JUST A SMELL | We go to the source. Shampoo and extraction. | Was from £180 / Now from £150 | 20260815_104504.jpg | 120251924486850294 | 3ef1096742cbf8727a07511a2c7d4a3e |
| MV3 | VALETED ON YOUR DRIVEWAY | We bring the water. You just need a socket. | From £80 | 20240928_123332.jpg | 120251924487020294 | 58f664d9abeca62415d5ead9ccc1e398 |
| MV4 | REGULAR CARE, DONE PROPERLY | Interior reset, safe wash, wheels, glass, wax. | From £80 | 20260224_124936.jpg | 120251924487310294 | 49048fa244135190c668e89bd6d33e22 |
| MV5 | KEEP IT LOOKING NEW | Regular valets at your home or work. | From £80 | 20250502_134224.jpg | 120251924487530294 | 1b65bc9a91a2215fd59e3eabd228eb20 |
| MP3 | MAINTENANCE PLUS | Leather, wheel and glass properly done. | From £110 | 20260224_163905.jpg | 120251924487690294 | 2e209f95e557771ed00c1bfaee7f469a |
| MP4 | INSIDE AND OUT, BROUGHT BACK UP | Everything in the valet plus the detail work. | From £110 | 20240920_143815.jpg | 120251924488130294 | c3e89dfaa0b25b5066358da124b62aba |
| RC2 | YOUR PAINT ISN'T TIRED. IT'S SCRATCHED. | Swirls removed, then sealed for 5 years. | Was from £595 / Now from £495 | 20260815_111047.jpg + inset 20240821_105113.jpg ("MID-POLISH") | 120251924488920294 | 39bb7da7771ed7d5c208ee0b457b4702 |
| RC4 | REFINED CORRECTION | Swirls removed, then sealed for 5 years. | Was from £595 / Now from £495 | 20250628_142012.jpg | 120251924489300294 | 86b8b8b1643c6ae564d75a01e16c3189 |
| RC5 | YOUR PAINT ISN'T TIRED. IT'S SCRATCHED. | Paint thickness checked, corrected, coated. | Was from £595 / Now from £495 | 20250125_155932.jpg | 120251924489750294 | 515cbd6fa8b4d5328c2afb72626445e2 |
| RC6 | CORRECT IT ONCE. PROTECT IT 5 YEARS. | Gtechniq Crystal Serum Light included. | Was from £595 / Now from £495 | 20260910_160157.jpg | 120251924490430294 | 80e9d235fe719bfe4caf58fb39c80b33 |
| FF3 | FLAWLESS FINISH | Multi-stage correction. Show-car gloss. | From £745 | 20260910_160013.jpg | 120251924491100294 | 7369fb4d76092712508691cb1fa831da |
| FF4 | PAINT YOU CAN SEE YOURSELF IN | Reflections like glass, protected for 5 years. | From £745 | 20241004_145806.jpg | 120251924491720294 | 0359069e36cb47c1758ea0b4c2f5a320 |
| FF5 | DEPTH AND CLARITY A WASH CAN'T GIVE | Heavier swirls and scratches, properly removed. | From £745 | 20241003_140302.jpg | 120251924492260294 | a6a4576d9e2ef2b16ee317946b84e3a4 |
| HL1 | HEADLIGHT RESTORATION | Hazed, yellow lenses restored and re-cleared. | £90 per pair | headlight-restoration-range-rover-westminster-warwickshire.jpg + inset 20240816_140035.jpg ("BEFORE") | 120251924493000294 | f3767c84516649d5162b57933080b234 |
| HL2 | THE £90 FIX THAT SHOWS | Not just polished. Re-cleared to last. | £90 per pair | porsche-taycan-gts-front-headlight-warwickshire.jpg + inset 20240816_140035.jpg ("BEFORE") | 120251924493610294 | 2be99aeb16eca6a2bb7334ae9cf8b391 |
| ST1 | SOFT TOP CLEAN & PROTECT | Algae and mould out. Waterproofed for a year. | From £100 | st_after.jpg + inset st_before.jpg ("BEFORE") | 120251924493950294 | c98b35d4ddc57bbadac7cd745b01bafd |
| ST2 | TREAT FABRIC LIKE FABRIC | Deep clean, dry, re-proof. No pressure washer. | From £100 | 20250114_162441.jpg | 120251924494370294 | d38cda65fe5ece3c9d19c72b17912500 |
| ST3 | GREEN TINGE ON THE ROOF? | That's algae. We lift it out and re-proof the hood. | From £100 | 20241007_114550.jpg | 120251924494450294 | 0c4becfe7abd2a5a76981a4e2bbd0149 |
| ST4 | RAIN BEADS OFF. NOT SOAKS IN. | Cleaned, dried and waterproofed for around a year. | From £100 | 20260225_171715.jpg | 120251924494520294 | 0447199ac78bcce928006dacadf512ea |
