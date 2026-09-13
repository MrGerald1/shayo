# Shayo, DESIGN.md

The component and screen layer. `BRAND.md` owns colour, type, tokens and voice and stays the
source of truth for all four. This file cites the evidence for each decision rather than
asserting taste.

**The memorable thing:** *it saw straight through me.* Every decision below serves that. The roast
lands because it is true, the tolerance verdict is true, the monthly total is true. Design that
tries to be memorable for everything is memorable for nothing.

## What ships when

The CEO review split this product into two acts. This file was written before that split and
still describes everything, which is deliberate: nothing here is wasted, and act two is
specified so it can be built without re-deciding.

| Act | Surfaces | Status |
|---|---|---|
| **One** | The picker, the drink card, the share card | Building now |
| **Two** | Six tiles, running total, Settle, ledger, radar empty state | Specified, parked |

Act one's home screen is unchanged: the feed, one roast per screen. The dock on every screen
asks **"Who you wan roast?"** and opens the picker. A roast card is the atom; the feed serves
them at random and naming serves the one you asked for.

---

## The one mechanic, validated

Untappd's check-in makes every field except identity optional, so the one-tap path and the full
review exit through the same button. Badges are retroactive: cross a threshold and the badge
arrives attached to your next check-in, never as a separate errand. That product went from a
prototype built in under 24 hours on about $1,000 to roughly 9M users and 925M+ check-ins.

**The reward attaches to the action.** In act two that action is logging a round. In act one it
is naming somebody's drink, which is the same shape and needs no habit.

---

## Act one: the picker and the drink card

**Job:** my guy just ordered Alomo and I want that line right now.

The picker is the existing browse grid, promoted from a 44px corner icon to the primary action.
Two up under 600px, three up above. Search field at the top, filters below it as chips.

**Filters, all four already in the data and read by nothing today.** Strength from `d.s`,
venue from `d.ven`, taste from `d.t`. And `d.p` as a **price band**, labelled as a band, because
it is an invented tier for filtering and not a measured price. The Index measures prices. The
product must never present one as the other.

**Aliases matter more than they look.** Every drink carries `d.m` with the names people actually
use, and search reads none of it, so typing "Henny" hits the empty state which then tells you to
try the brand name. You did.

The drink card carries the roast, who else drinks it, the tolerance answer and how to drink it.
**Send is the primary action**, not a secondary one, because sending is the job.

**Rotation.** A repeated joke is not sendable, so a second lookup of the same drink returns a
different line. Five roasts per drink is 365 cards and it is a writing task, not engineering.

---

## Act two below this line, except Surface 6

Surfaces 1 to 5 are the money product and are parked. **Surface 6, the share card, is act one**
and is the highest-priority component in the build, because it is the unit that travels.

## Surface 1: the six tiles

**Job:** when I order another round at a loud bar with my hands full and several drinks in, I
want to record it in one tap. The competing alternative is a waiter, who is instant, free and
already trusted.

```
  ┌──────────────────────────────────────┐
  │  ₦ 6,000                      ●●●    │  total, display 900, tabular
  │  4 rounds, since 8:42pm              │  muted, 13/16
  ├──────────────────────────────────────┤
  │  ┌──────────┐  ┌──────────┐          │
  │  │ STAR   2 │  │ GULDER 1 │          │  tile 1:1, radius 20
  │  └──────────┘  └──────────┘          │  count badge top-right
  │  ┌──────────┐  ┌──────────┐          │
  │  │ TROPHY   │  │ HENNESSY │          │
  │  └──────────┘  └──────────┘          │
  │  ┌──────────┐  ┌──────────┐          │
  │  │ ALOMO  1 │  │ + other  │          │  7th tile opens search
  │  └──────────┘  └──────────┘          │
  ├──────────────────────────────────────┤
  │           Settle the night           │  quiet until rounds > 0
  └──────────────────────────────────────┘
```

**Anatomy.** Tiles are 1:1, two up under 600px, three up above. Minimum tile edge 140px, which is
far past the 48px tap minimum, because the target is a thumb belonging to someone who has been
drinking. Tile fill is the drink's own colour from `d.color`, text colour from `TEXT_ON`. Name in
Archivo 800, uppercase, sized to the longest word so nothing clips.

**The count badge is the whole interaction.** Tap adds one and the badge increments in place. No
screen change, no confirmation, no re-render. This is the shopping-cart convention, so nobody
learns it.

**Press and hold** opens a small number pad for a bulk round, because in Nigeria a round is
bought for a table, not a person. Four people drinking Star is one gesture, not four taps. The
fast path stays one tap and the plural path stays one gesture. Press-and-hold is undiscoverable,
so it gets exactly one hint on first use and never again.

**Press and hold the badge** subtracts, which writes a void event rather than editing the log.

**Two latency budgets, not one.** Tap to paint under 100ms, from memory, write fire-and-forget.
Cold start to first tap is the number that will actually fail, so the store opens during boot.

**Cold start.** A first-ever night has no history, so the six tiles are the national favourites,
labelled as such, and they are replaced by the user's own as soon as there is data. Never an
empty grid.

**What goes wrong elsewhere:** search-first loggers. MyFitnessPal is a text field, then a list of
near-identical entries, then a serving-size disambiguation. Cal AI's documented weakness is not
its happy path but its correction path, several steps to fix one misidentified item, which is
fatal when you are drunk and it is wrong.

---

## Surface 2: the running total

**Job:** when the night is going, I want to know what I have spent without doing arithmetic.

**It is a sum, not a remainder.** Cal AI leads with calories left, which is genuinely elegant, but
a remainder requires a budget and a budget manufactures a moment where you go past it.
MyFitnessPal turns the number red identically whether you are over by 1 calorie or 1,000, and a
BJPsych Open qualitative study recorded users feeling guilt, embarrassment and shame at exactly
that visualisation. Around 30% of eating disorder patients in one survey reported using the app
and believed it contributed.

So:

- Display weight, tabular figures, naira sign always, never abbreviated.
- **The total never changes colour.** Crate Red means a bar overcharged you, never that you drank
  too much. That rule already existed in `BRAND.md` and the research now backs it.
- A remainder line appears **only** if the user set a monthly drink budget, in muted ink at label
  size. It does not bold, does not redden and does not animate on crossing.
- Tap the total to expand to the line items. The convention is that a headline number is always
  derivable, and Splitwise's most-reported failure is a correct total whose derivation is hidden.

---

## Surface 3: Settle

**Job:** when the bill arrives at 1am and it looks wrong, I want itemised timestamped evidence I
can show the waiter. Read at arm's length, in bad light, by a hostile second party.

**It is a paper till receipt.** That format needs no explanation to anyone, including a waiter,
which is the entire point.

```
        SHAYO
   Mama Cass, Surulere
   Sat 13 Sep  8:42pm - 1:15am
  ─────────────────────────────
   8:42pm  Star            1,400
   8:42pm  Star            1,400
   9:07pm  Gulder          1,500
  10:31pm  Star            1,400
  11:42pm  Star           -1,400   removed
  12:04am  Suya            2,000
  ─────────────────────────────
   5 items                 6,300
  ─────────────────────────────
   shayo.ng
```

- Left-aligned item, right-aligned price, a rule, then the total in bold. IBM Plex Mono 600 for
  every figure so decimals sit in a column.
- **The time column is the asymmetric evidence.** A waiter's handwritten tally has no timestamps.
  Yours is the only version of the night that can be checked against itself.
- **Voids are shown, not hidden.** A removed round appears struck with its time. An append-only
  log means the receipt can honestly say something was cancelled at 11:42pm, and a receipt that
  quietly omits things is not evidence.
- Body type no smaller than 17px here, against the 15.5px default, because this is read at arm's
  length in a dark bar.
- Zero jokes. `BRAND.md` names four places with no jokes and this is two of them at once, money
  and the bill.
- Shareable as an image, because the argument often continues in a group chat.

**Splitwise gets the first half right and loses the second.** Its itemised mode assigns each line
to a person and allocates tax and tip proportionally, and proportionality is the fairness rule
that ends arguments because it is stateable in one sentence. Its settle-up screen puts two avatars
either side of an arrow so the direction of money reads without being read. Then debt
simplification aggregates obligations into a total whose derivation is invisible, and users report
simply not believing it. Never do the second thing.

---

## Surface 4: the ledger

**Job:** when I look back at a month, I want to see what drinking actually cost me, translated
into something I recognise, without being made to feel judged.

**The grid.** A month of cells, intensity encoding spend. GitHub contributions, Daylio moods,
Apple activity rings on a calendar. People read a grid for pattern, not for score, **as long as no
cell is coloured as failure.**

**Dry nights are markable.** Gentler Streak won an Apple Design Award partly on one mechanic: a
logged rest day counts instead of breaking the streak, and the copy never says you failed. The
principle generalises. A gap in a chart reads as failure; a labelled state does not. A month with
four blank Saturdays looks like a confession, and a month with four Saturdays marked "no drinks"
looks like a record.

So a night with no rounds can be marked with one tap and renders as a filled quiet cell. It
**never counts, never chains, never congratulates, and never prompts.** Nothing accumulates, which
keeps `SCOPE.md`'s no-abstinence-streaks rule true literally rather than nominally.

**Translation is the whole feature, and the unit chosen decides whether it reads as information or
as an accusation.** A month of drinking expressed in gigabytes is a fact. Expressed in school fees
it is an accusation.

Allowed units: data bundles, transport fares, a flight, a pair of shoes, the note denominations
people actually think in. MTN's cheapest monthly plan moved from ₦1,000 for 1.2GB to ₦1,500 for
2GB in February 2025 and its 15GB plan went from ₦2,000 to ₦6,000, so data is a live, felt price
everybody tracks.

Never: school fees, rent, medical costs, anything a dependant needs. Those are not translations,
they are verdicts wearing a translation's clothes.

**The screen nobody has designed.** A 24 year old finding out they spent ₦94,000 on beer last
month. `BRAND.md` says show the number and stop. "Stop" is a copy rule, not a screen. That screen
shows the number, one translation, and a single quiet action that is not about drinking less: see
the nights it came from. It offers no advice and asks no questions.

---

## Surface 5: the price radar, empty

**Job:** when I want to know if this bar is overcharging me but nobody has reported prices here
yet, I want a reason to be the first.

Three bands, and the count is visible in all of them.

| Reports | What the screen shows |
|---|---|
| 0 | No price surface at all. "Nobody has reported Star in Surulere yet. You would be the first." One action: report what you just paid |
| 1 to 4 | The count, never a median. "3 people have reported Star here. We show a price at 5." |
| 5+ | The median, the comparison, the count. "₦2,500? Star is ₦1,400 around here. Ask them why." |

**State the threshold.** Numbeo is the counter-example: it withholds prices below a contributor
threshold it never publishes, so a user cannot tell whether the gap is three reports away or
hopeless, and therefore never contributes. A visible count against a stated target is the
crowdfunding convention and it reads as an invitation.

**Name the beneficiary and the turnaround.** Vivino's unrecognised-label state is a submission
that a review team typically resolves within a few hours, after which every future scan of that
label works instantly. The contribution has a named outcome and a time, which is why people make
it.

**The incentive is already solved and nobody noticed.** `SCOPE.md` item 11 says photographing the
bar's price list makes the prices into buttons, which makes logging one tap. The user does it for
themselves and the radar is fed as a side effect. Nobody performs unpaid labour. That is why OCR
ships with the radar rather than after it.

**The Nigerian recruitment unit is the group, not the individual.** 96.5% of Nigerian internet
users aged 16+ used WhatsApp in the past month. A first-reporter ask that produces something
forwardable works with that; an in-app points balance does not.

---

## Surface 6: the share card, 1080x1920 — ACT ONE

**Job, act one version:** my guy is drinking Alomo and I want to send the line that exposes him,
so the group piles on. The original job, wanting to post a roast about yourself, still holds and
uses the same card.

This is the unit that travels and the only distribution mechanism the product has, so it is the
first component built after the funnel fixes.

**Physical constraints, which are not negotiable.**

- 1080x1920. WhatsApp recompresses to roughly 1600px on the long edge at about 60 to 70% JPEG
  quality with 4:2:0 chroma subsampling, and strips EXIF. Keep the file under ~1MB.
- **No thin strokes, no light greys, no low-contrast type anywhere.** Chroma subsampling eats them.
  Archivo 800 and 900 only. Flat saturated grounds, which is what the brand already is.
- **The top and bottom ~250px are covered** by the profile chip and caption UI. The payload lives
  in the middle band.
- **The URL is burned into the image as type.** Links are the exception in Nigerian status, not
  the rule, and business flyers there already burn phone numbers into the artwork for the same
  reason.
- **It must carry its own attribution.** WhatsApp's 2025 Status Reshare lets a viewer repost
  someone else's status, and anything forwarded five or more times gets labelled. Context does not
  travel; the image has to.

**What makes a card get posted.** Spotify Wrapped works on three content types: a rank that
confers status, an identity label you can announce, and a group you belong to. The uncomfortable
half of the same research is that people post the version of themselves they want reflected back,
so **the card that flatters gets posted and the card that merely reports does not.**

For Shayo that means the roast card is a self-deprecating flex. Being roasted accurately is the
flattery, which is the whole Nigerian register and it is already in the 73 lines.

Untappd's own counter-example is instructive: its per-check-in share copies details to the
clipboard for you to paste, so the user has to assemble the post. **Anything requiring assembly
does not travel.** The card is finished, cropped and ready, or it is not a share feature.

**Card anatomy**, identical on screen and in the export, per `BRAND.md`:

```
  ┌─────────────────────┐   ← 250px safe, empty
  │                     │
  │  ▓▓▓ ░░░ ░░░        │   three progress ticks
  │                     │
  │  ALOMO              │   drink name, 900, tight
  │  BITTERS            │
  │                     │
  │  "Alomo is not a    │   the roast, 800
  │   drink, it is a    │
  │   decision."        │
  │                     │
  │  ● shayo.ng         │   cork mark + burned URL
  │                     │
  └─────────────────────┘   ← 250px safe, empty
```

---

## What this file does not change

Colour, type, tokens, the crate pattern, the cork mark and the voice all stay exactly as
`BRAND.md` defines them. Every contrast ratio there was computed rather than estimated and every
one survived the design review. Two corrections only, already in `PLAN.md`: `--card:#FFF` becomes
a declared token, and `--blue` gets added since `--blue-mist` exists without it.

## Sources

Untappd: lounge.untappd.com badges guide, updates.untappd.com, Inc. profile of Greg Avola,
Wikipedia. Vivino: Match for You explainer, label scanner guide, rating system. Cal AI:
screensdesign.com teardown, product screenshots. MyFitnessPal harm: BJPsych Open, "Effects of diet
and fitness apps on eating disorder behaviours". Splitwise: Pratt design critique, Medium settle-up
case study. Gentler Streak: gentler.app, Health App Insider review. Wrapped: LSE Impact blog,
Taylor and Francis. Numbeo methodology page. GasBuddy price-reporting help. WhatsApp compression:
moda.app status sizes. Nigerian platform use: Krestel Digital 2025 social statistics. MTN data
pricing: NaijaTechGuide, AllAfrica Feb 2025.
