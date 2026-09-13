# TODOS

Deferred, not forgotten. Rewritten September 2026 after the CEO review moved Shayo to an act-one
banter product. Nothing here is in the current build. Each item says what triggers picking it up,
because "later" is not a plan.

## Blocking, answer before launch

### Web or installed app
The premise is that people forwarded images with no app, no link and no install. Act one
responds by asking a stranger to install something, and nobody has defended that. A card opening
instantly in a browser matches the observed behaviour; an install asks for a commitment nobody
in the original chain made.
**Blocks:** the distribution plan, and therefore launch.
**Interacts with:** the app store question below.

### Apple and Google alcohol policies
Both platforms have alcohol content rules and age-gating requirements. Not researched. If the
answer is restrictive it partly decides the question above.
**Blocks:** launch, if the answer is install.

### The first hundred users
No plan exists that does not assume users we do not have. The share card is a loop that needs
seeding. WhatsApp's Business API is closed to alcohol here. The only proven-reach asset is the
original WhatsApp groups the roasts already travelled in.
**Blocks:** launch.

### ARCON pre-vetting
ARCON pre-vets advertising material and asserts jurisdiction over foreign advertisers. The moment
a brewer pays for anything on Shayo this becomes live.
**Blocks:** selling anything to a brand. Does not block act one.

## Deferred by the CEO review

### User-submitted roasts with voting
The permanent fix for content supply and the only asset a competitor cannot copy by shipping
features. SCOPE.md's own words: "a community, not a feature."
**Why it is deferred:** moderation is the first real operational burden in the plan, and it
lands before there is an audience to moderate for.
**Trigger, now numeric:** `repeat_lookup` events exceeding `name` events for any drink, or
weekly card sends above the floor set at launch. Both are logged from event one.
**Watch out:** bad submissions early make the product look worse than it is, so seeding matters
more than the ranking algorithm.

### Act two in full: the tab, ledger, price radar, Settle, six tiles, identity layer
Specified completely in `PLAN.md` and `DESIGN.md`, including the states, the receipt layout, the
ledger's translation rules and the radar's recruiting empty state. None of that work is wasted.
Each becomes a view over a log that will already exist.
**Trigger:** act one passing its success criteria in SCOPE.md.

### Selling to brands
The regulatory opening is real and structural. The relationship is not: Nigerian Breweries buys
media through agencies on annual planning cycles, and no contact or route in has been named.
**Now:** write the boundary document. An afternoon, no counterparty needed.
**Trigger for selling:** an audience floor set at launch, or a named inbound.
**Blocked by:** ARCON pre-vetting, above.

### Backup and account recovery
Local-only means a lost phone erases everything. SCOPE.md now requires the cheapest possible
durability in act one, an anonymous device id plus append-only sync, because without it the
event-schema work loses its stated reason. Anything richer than that, real accounts, cross-device
history, is deferred.
**Trigger:** a user asking for it, which is also the signal that the record matters to someone.

### Clip engine
Every roast rendered as a vertical video: text animation, Nigerian voice, captions, one tap to
post.
**Why it is good:** Cal AI paid 250 creators on retainer for content. Ours writes itself.
**Trigger:** weekly shares above roughly 500, so there is evidence people want to post before
spending on rendering.
**Watch out:** voice synthesis in Nigerian English is the hard part. Test three vendors on the
Alomo line before committing.

### Venue claiming and bar-side tools
Untappd moved monetisation entirely onto venues at $899 to $1,199 per location per year across
roughly 20,000 venues, and paying is the only route to a verified venue in its consumer app. It
did that six years after launch, at around 8 million users. Nigeria already has a crowded local
field for bar software: Staycore, InkeepX, LoungeOS, OyaSync, Lumi Business, all pitching on
fraud and shrinkage rather than menus.
**Trigger:** act two shipped and the price radar holding real coverage in at least one area.

### Detty December mode
Event calendar plus what to drink at each one.
**Trigger:** seasonal. Build in October or not at all that year.

### Morning-after check-in
"How did last night end?" The honest input to the ledger.
**Watch out:** the feature most likely to feel like judgement. Copy work before engineering.

### Gifting
Send a crate to your uncle. Diaspora sends one home.
**Trigger:** blocked indefinitely. The research found no affiliate or referral route at Chowdeck,
Glovo or Drinks.ng, and the new national policy attaches licensing and age verification to
anyone touching a transaction.

## Killed, with reasons, so they do not come back

- **Party stock calculator.** Nobody opens an app to plan a burial. The purchase is made by
  phone through a supplier somebody's aunt already knows. Fails the despite test, same as the
  scanner.
- **Bottle scanner.** Nigerians recognise their own bottles. Identification is not the job.
- **Venue directory ranked by price.** People choose a bar by who is there.
- **Group pick with a join code.** Skipped.
- **Delivery, marketplace, any owned logistics.** Somebody else's business, and it changes
  Shayo's regulatory category.
- **WhatsApp Business API as a channel.** Alcohol commerce is prohibited on every WhatsApp
  surface globally, and the messaging allowance covers India, APAC and LATAM only. Forwarding
  still works; building on the API does not.
- **Any paid placement inside a roast.** Structural, not a preference.

## Known debt in the current build

Full detail, with line numbers and severity, is in `PLAN.md`. The three that block everything:

- **Nothing persists in a real browser.** `store` gates on `window.storage`, an artifact host
  object, so every write fails silently in Chrome and Safari.
- **Deep links bypass the 18+ gate**, and deep links are the growth path.
- **`LIVE_URL` is empty** and the fallback rejects both `file:` and the preview host, so
  `shareUrl()` returns an empty string. Nothing has ever been forwarded with a way back.

Then: the photo pipeline is unreachable code and should be deleted, search never reads the alias
array so "Henny" fails, one `@media` query exists in 956 lines, three of BRAND.md's four
elements are absent, and three tap-target classes sit under BRAND.md's own 48px rule.

## Open questions without an owner

1. **Panel packaging**, given that representativeness rather than scale is the problem. A narrow
   honest claim beats a broad weak one.
2. **Whether the regulatory opening holds.** Digital is untouched in a policy three weeks old.
   Worth watching, not worth betting permanence on.
3. **How many roasts per drink** act one ships with. Five each is 365 cards and it is a writing
   task, not an engineering one.
