# Shayo, scope

Rewritten September 2026 after `/plan-ceo-review` in scope-expansion mode, then corrected
against an adversarial review that scored the first draft 5/10. This supersedes the previous
version, which led with money as the value proposition. `PLAN.md` and `DESIGN.md` hold the
implementation and component decisions and win on how a thing is built.

## The thing that is actually true

Exactly one behaviour has ever been observed in this project. **People forwarded the roasts on
WhatsApp.** No app, no link, no install, no prompt. Everything else here is a hypothesis, and
the previous version built its entire business on the largest of them, that Nigerians want to
count what they drink.

The job those forwarders were doing was not research and not tracking. It was **banter**.
Having something to say about what your friend is drinking.

## The thesis, in one paragraph

Shayo is where Nigerians go to get something to say about what somebody is drinking. The roasts
are the product and the card you send is the unit. Because Nigerian brewers are shut out of
daytime broadcast and outdoor by a watershed, and must pre-vet every piece of material, an
audience of drinkers reachable in digital is worth real money to them for a structural reason. That is act one. Act
two is money: the tab, the ledger and the price radar, built as views over a log act one is
already writing. One product, one schema, two acts.

## Act one, in scope, in ship order

| # | Item | Why it is here |
|---|---|---|
| 1 | **Fix the funnel.** Persistence, age gate, `LIVE_URL`, service worker, self-hosted font, alias search | Three critical defects. Nothing has ever been forwarded with a link back because `shareUrl()` returns an empty string |
| 2 | **The share card.** 1080x1920, per `DESIGN.md` | It is the unit that travels. Physical constraints are known and specified |
| 3 | **The naming loop.** The dock on every screen asks "Who you wan roast?", opens the picker, gives that drink's card with Send primary | Serves the roaster, which is the observed job. The recommender drops to secondary because it serves the drinker |
| 4 | **Search, promoted** from a 44px corner icon to the primary action. Filters on strength, venue and taste. Aliases, so "Henny" finds Hennessy | All of it is in the data and read by nothing |
| 5 | **More roasts per drink.** See the content-supply section, which is the real constraint | A repeated joke is not sendable |
| 6 | **The event log**, minimal fields, written from the first line | Act two reads it. See the schema section |
| 7 | **The boundary document** for brand money | An afternoon, no counterparty needed, and far easier to write before a cheque is on the table |
| 8 | **The Shayo Index**, at the minimum credible unit below | Reputation, on a proven Nigerian model |

The feed stays home, unchanged, because it is what earned the attention. A roast card is the
atom: the feed serves them at random, naming serves the one you asked for. Same object, two
access paths, one home screen.

## Distribution, which the first draft of this document omitted entirely

This was the largest gap and it is the thing most likely to kill act one.

**Nobody knows Shayo exists.** The share card is a loop that requires existing users to seed it,
and there are none. WhatsApp's Business API is closed to alcohol in this market. The premise is
that people forwarded *images* with no app, no link and no install, and act one responds by
asking a stranger to install something.

**Unresolved and blocking:** is Shayo a web link or an installed app? A forwarded card opening
instantly in a browser matches the observed behaviour. An install asks for a commitment nobody
in the original forwarding chain made. This decision also interacts with Apple and Google
alcohol content policies and their age-gating requirements, which are a launch blocker and are
not yet researched.

**Required before launch:** a named plan for the first hundred users that does not depend on
users we do not have. Seeding the original WhatsApp groups the roasts already travelled in is
the obvious first move and it is the only asset with proven reach.

## Content supply, stated honestly

The earlier claim, that a lookup does not exhaust because its trigger is external, was a
rationalisation. **The trigger recurs. The payload does not.** Your friend orders Alomo a second
time and the card is the same line, and a repeated joke is not sendable, which is the only
behaviour ever observed. Real order distribution is skewed too: roughly ten drinks plausibly
cover most occasions, so usable inventory is closer to ten cards than 73.

**The fix in act one is writing, not engineering.** Multiple roasts per drink, rotated on repeat
lookup. Five each is 365 cards, and it is a writing task with no backend.

**User-submitted roasts with voting** remain the permanent fix and the only asset a competitor
cannot copy. Deferred, on a shorter clock than previously stated. Trigger: repeat-lookup events
exceeding first-lookup events for any drink, or weekly card sends above a number set at launch.

## Act two, deferred and fully specified

The tab, the personal ledger, the price radar, Settle, the six-tile round logger and the
identity layer. All specified in `PLAN.md` and `DESIGN.md`, none of it wasted. Each becomes a
view over a log that will already exist.

**Trigger:** evidence that act one works, defined in the success criteria below.

## What the market research established

| Previously believed | What the evidence says |
|---|---|
| The panel is the business. Substitution data is unsold anywhere | The problem is **representativeness, not scale.** Brewers buy syndicated retail audits that meter actual shelf movement. Frontline Research runs one monthly across Lagos, Abuja, Ibadan, Enugu, Owerri and Port Harcourt, syndicated precisely because custom audits price Nigerian buyers out. Nielsen's global median contract is about $29k a year. A self-selected panel of comedy-app users measures a different thing, and growth does not repair that. Untappd needed roughly 8M users and six years, and Untappd Insights still publishes no price |
| A commerce handoff earns a cut | **No route exists.** Chowdeck takes 24%, Glovo 25 to 35%, neither publishes a third-party affiliate programme. Only Jumia does, at 4 to 13% with a 7-day cookie, on a catalogue of 43 spirits and 13 drinks |
| The Shayo Index is free press | Correct, and that is the entire model. The Big Mac Index is free, methodology and data on GitHub under MIT and CC-BY. SBM Intelligence's Jollof Index has run quarterly for ten years across 13 Nigerian markets and two Ghanaian ones, free, as the lead generator for paid consulting. **An index is not a product you sell, it is a reputation you spend** |
| WhatsApp could be a channel | **It cannot.** Alcohol commerce is prohibited on every WhatsApp surface globally. The alcohol messaging allowance is documented only for India, APAC and LATAM, with nothing extending it to Nigeria. Forwarding still works. Building on the Business API does not |

### The regulatory opening

Nigerian alcohol advertising runs on a **watershed, not a ban.** Radio is shut 6am to 8pm.
Television, motion picture and outdoor are shut 6am to 10pm. Every ad must carry a
responsible-drinking message, nothing may sit adjacent to youth content, and ARCON pre-vets
material and asserts jurisdiction over foreign advertisers.

So a brewer can reach a drinker on television. It pays a time-of-day tax to do it, and the
post-watershed window is the expensive one. This is a narrower opening than an outright ban
would be, and the honest version of the argument is that digital is unrestricted rather than
that broadcast is closed.

The Nigeria Alcohol Policy unveiled 27 August 2026 left **digital largely untouched**, in a
document where the government itself acknowledges digital alcohol promotion to young people is
growing.

Nigerian Breweries posted ₦1.467trn revenue for FY2025 and spent ₦364bn on marketing,
distribution and admin. Guinness Nigeria did ₦730.8bn over 18 months under Tolaram.
International Breweries did ₦619bn. All three returned to profit after two years of losses, and
none can legally reach a drinker on television.

An audience of Nigerian drinkers in digital is therefore **structurally** valuable rather than
speculatively valuable, and it monetises at hundreds of thousands of users rather than millions.

**But Shayo has zero users, and this is not yet a revenue line.** Nigerian Breweries buys media
through agencies on annual planning cycles. A solo founder with no product in market does not
get that meeting, and no relationship, agency contact or route in has been named. So:

- **Now:** write the boundary document. An afternoon, no counterparty required.
- **Deferred:** selling anything. Trigger is an audience floor set at launch, or a named
  inbound. ARCON pre-vetting is a **blocker** on this, not an open question, and must be
  resolved before the first conversation.

Two caveats held honestly. The policy is weeks old and untested, and digital being untouched is
an opening regulators will eventually close.

## The boundary

Drawn **by surface, not by intent**, because the first draft contradicted itself: it forbade
selling the ordering of search results and then permitted category takeovers in the picker,
which are the same thing.

**Never sellable, no exceptions:** ranking and ordering anywhere in the product, and any text a
user could read as a joke. That covers every roast, every verdict, the tolerance answer, the
Index, search order and the contents of the feed. A sponsored challenge carries roast-like
content, so it is on this side of the line unless its copy is written by Shayo and marked.

**Sellable, always visually distinct and always marked:** dedicated slots that do not reorder
anything, seasonal editions, and activations at events.

This is structural, not a preference. The audience and the panel both die the moment people
suspect the jokes are bought.

## The Shayo Index, at a size one person can actually sustain

The precedents are The Economist and SBM Intelligence, both organisations with staff. Borrowing
their credibility without their headcount is how an index dies in cycle three, and **a dead
index is worse than no index, because the reputation it was meant to build is what breaks.**

- **Minimum credible unit:** 12 SKUs, 3 Lagos areas, 10 venues.
- **Cadence:** quarterly, matching SBM.
- **Budget:** a stated hours-per-cycle number, fixed before the first issue.
- **Kill rule:** two consecutive missed cycles and the index retires publicly, with a note.

**Price provenance, stated to avoid a credibility problem.** The `p` field on each drink is an
invented price *band* used for filtering, not a measured price. The Index is measured. These are
different things and the product must never present one as the other. The price-band filter ships
as a band and is labelled as such.

## Event schema, minimal

Act two reads this. Act one writes it. Only raw fields, because derived values lock in
definitions that have not been made yet.

```
{ id, v, deviceId, ts, tzOffset, type, ...payload }

  id        client-generated. Replay is a no-op
  v         schema version, from event one
  deviceId  anonymous, local
  ts        client timestamp
  tzOffset  offset at write time. Local day is recomputed later,
            never stored, because the night rollover is an act-two
            decision and it will change
  type      name | send | search | search_empty | repeat_lookup | choice | void
```

The last four matter more than anything act two needs, because they are what answer act one's
own central question. `repeat_lookup` versus `name` tells you when the roasts have run out.
`search_empty` tells you which drinks are missing. Neither was in the first draft.

Deliberately dropped from the earlier version: `night` and `seq`. Both solve ordering problems
for a ledger that is not being built.

Corrections are events. A void references the id it cancels, so the log stays append-only.

The panel, if it ever ships, is an **export projection** with its own version, not the raw log.

**Durability, which cancels the earlier justification for this section.** Claiming accumulated
data is unrecoverable while shipping local-only storage is a contradiction: the log is already
lost on every phone upgrade. Act one therefore ships the cheapest durability that exists, an
anonymous device id and an append-only sync to something free, or the schema work loses its
stated reason.

## Success criteria for act one

Without these the plan cannot be checked against reality in three months.

1. **Forward-through rate.** Of people who open a shared card, how many tap through to name
   somebody themselves. This is the whole loop in one number.
2. **Repeat lookups per user.** Rising is good until it exceeds first lookups, at which point
   the content has run out and user submission moves from deferred to urgent.
3. **Cards sent per active user per week.** Below a floor set at launch, act one has not worked
   and act two is not rescued by building it.

## Not in scope, and why

- **Party stock calculator.** Killed. Nobody opens an app to plan a burial; the purchase is made
  by phone through a supplier somebody's aunt already knows. Fails the despite test, which means
  there is no bad existing solution to displace.
- **Bottle scanner.** Nigerians recognise their own bottles. Identification is not the job.
- **Venue directory ranked by price.** People choose a bar by who is there.
- **Group pick with a join code.** Skipped.
- **Building delivery or a marketplace.** The new national policy attaches licensing and age
  verification to retail outlets in a national digital registry, so touching a transaction
  changes Shayo's regulatory category entirely.
- **Anything on the WhatsApp Business API.** Closed to alcohol in this market.
- **Any paid placement inside a roast.** See the boundary.

## Six-month risk

The first sponsorship cheque still applies, and the boundary is the answer to it.

The newer risk: **act one could work and still not lead anywhere.** An audience that forwards
jokes is not automatically an audience that logs rounds, and the bridge between the acts is
asserted rather than demonstrated. Act one is worth building on its own terms; act two is a bet
that gets cheaper the longer the log runs.

## Still open

1. **Web or installed app.** Blocking. Interacts with the app store question below.
2. **Apple and Google alcohol content and age-gating policies.** A launch blocker, not
   researched.
3. **The first hundred users.** No plan exists that does not assume users.
4. **ARCON pre-vetting.** A blocker on selling anything, not a general open question.
5. **Panel packaging**, given representativeness. A narrow honest claim beats a broad weak one.
6. **Whether the regulatory opening holds.** Worth watching, not worth betting permanence on.

## Glossary

- **The despite test.** Does a bad existing solution exist that people use *despite* its being
  bad? If not, there is no behaviour to displace and the feature is inventing a job.
- **Settle.** The end-of-night itemised receipt, act two. Specified in `DESIGN.md`.
- **The six tiles.** The act-two round logger: your six usual drinks, one tap each.
- **Cold start.** A crowd-sourced feature with no crowd yet, which describes the price radar
  everywhere in Nigeria on day one.
