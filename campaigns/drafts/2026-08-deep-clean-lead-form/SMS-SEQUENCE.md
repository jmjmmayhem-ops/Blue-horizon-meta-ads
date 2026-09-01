# GHL SMS Sequence — Deep Clean Lead Form

**Purpose:** acknowledge the enquiry instantly and ask for availability up front,
so the booking conversation starts already halfway done.

## CRITICAL — plain characters only

GHL bills per 160-character segment, but only for the **GSM-7** character set.
One curly apostrophe, em dash or ellipsis flips the message to UCS-2, where a
segment is **70 characters**. Same message, roughly double the cost, every send.

Safe: `£` `'` (straight) `-` (hyphen)
Unsafe: `'` `"` `—` `…`

**Do not retype these in Word or on a phone — autocorrect will break them.**

---

## Message 1 — immediate

Hi {{contact.first_name}}, it's Josh from Blue Horizon Detailing. Thanks for your Deep Clean enquiry - I'll give you a call shortly. Want it sorted faster? Just reply with the days that generally suit you and I'll check the diary and get you booked straight in.

## Message 2 — +2 hours, only if no reply

Hi {{contact.first_name}}, Josh from Blue Horizon again. Just checking that reached you. If you let me know roughly when you're free - weekdays, weekends, mornings - I'll find you a slot. If the inside is in a bad way, send a photo and I'll confirm the exact price too. Reply STOP to opt out.

## Message 3 — day 3, only if still no reply

Hi {{contact.first_name}}, Josh from Blue Horizon Detailing. Happy to hold the £150 first visit price for you if you still want it. Just reply with a day that suits and I'll sort the rest. If now isn't the right time, no problem at all - just ignore this. Reply STOP to opt out.

---

# Build in GHL

Automation → Workflows → Create Workflow → Start from Scratch

1. **Trigger:** Facebook Lead Form Submitted → filter Form = Deep Clean form
2. **Wait:** time window **08:00-21:00** (stops midnight texts)
3. **Send SMS** → Message 1
4. **Wait** 2 hours (same window)
5. **Send SMS** → Message 2
6. **Wait** 2 days
7. **Send SMS** → Message 3
8. **Settings tab → "Stop on Response" ON** — otherwise repliers get chased twice more

## Checks before switching on

- Custom fields `Postcode` and `Vehicle Make and Model` must exist in
  Settings → Custom Fields, then be mapped, or the answers are dropped.
- Test `{{contact.first_name}}` renders — blank gives "Hi , it's Josh".
- Confirm which number it sends from; if it differs from the WhatsApp number
  (07818 514079) people won't connect the two.

## Saved manual reply — when they give availability

Great - I've got space on [DAY]. It takes about 5 hours and I'll come to you, so I just need somewhere to park and access to a plug socket. I'll text you 20 minutes before I arrive. Shall I put you down?

---

# STATUS

**Not live.** The Meta -> GHL lead connection was never working: leads register
on Meta but do not reach GHL. Josh is handling leads manually in Meta for now.
This sequence starts working the moment that connection is fixed - see the
review report for the Lead Access / LeadConnector diagnosis.
