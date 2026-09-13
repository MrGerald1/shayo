# Distribution

Two questions that PLAN.md listed as launch blockers and nobody had answered: whether Shayo is
a web page or an installed app, and how the first hundred people find it. Written 13 September
2026, after reading the actual store policies rather than assuming them.

---

## 1. Web or installed app

**Recommendation: web, and it is not close. The decision is yours.**

The code as it stands supports either. It is a web page with a service worker and a manifest,
so it installs to a home screen from the browser without ever touching a store. Nothing below
has to be undone if you later decide to ship a wrapper.

### What the stores actually say

**Apple, App Review Guideline 1.4.3.** "Apps that encourage consumption of tobacco and vape
products, illegal drugs, or excessive amounts of alcohol are not permitted. Apps that encourage
minors to consume any of these substances will be rejected."

**Apple 4.7.5 and 1.2.1(a).** An app must "use an age restriction mechanism based on verified or
declared age to limit access by underage users." Declared age is explicitly allowed, so the gate
Shayo already has satisfies this.

**Apple age ratings.** The 12+ and 17+ bands are gone; 13+, 16+ and 18+ were added. Shayo is 18+.
Responses to the new rating questions were due 31 January 2026, so this is live, not upcoming.

**Google Play, restricted content.** "Portraying excessive drinking favorably, including the
favorable portrayal of excessive, binge or competition drinking is not allowed." And: "Depicting
or encouraging the use or sale of alcohol or tobacco to minors is not allowed."

### What that means for the 73 lines

I read every roast against the Google clause. Ten mention quantity, repetition or a late hour:
`gulder`, `smirnoff_ice`, `shots`, `x1`, `pito`, `palmwine`, `champagne`, `odogwu`, `chamdor`,
`water`.

Nine of the ten are safe on the wording that matters. The clause bans portraying excess
**favourably**, and the register throughout is consequence and mockery: Gulder ends with you
giving the barman marriage advice, Smirnoff Ice ends with you texting your ex, X1 ends with you
finishing the bottle before the rice is served. `water` is openly the anti-drinking line. The
closest to the line is `shots`, where "Nobody in history has taken only one shot" normalises the
second one before the payoff turns it into a video you beg your friends to delete.

So a human reviewer should pass this. **The risk is not the human.** Both stores now run
automated content scanning against the declared rating, and a mismatch can trigger removal
rather than a review request. An automated classifier reads "Two bottles in" and does not read
irony. And the corpus is about to grow five-fold when you write the other four roasts per drink:
365 lines, each one a fresh surface, on a store listing that can be pulled without warning.

### The argument that settles it

The store risk is real but secondary. The premise of the whole product is that a card travels
through WhatsApp and the person who receives it looks up their own drink. Putting an install
between "I got a funny card about Alomo" and "let me see what mine says" breaks the one loop act
one exists to measure. Nobody in three reviews defended that step, including me.

Web also means the roasts are yours. No review queue between writing a line and shipping it.

**What web costs you.** No push notifications on iOS unless the user adds to home screen. No
store search as a discovery channel, which matters not at all at zero users and might matter at
fifty thousand. And a home-screen install on iOS is a three-tap flow most Nigerians have never
performed, so treat the manifest as a bonus, not a plan.

**Revisit when:** the forward-through rate is proven and you want retention, or a brewer
conversation needs a store listing as a credibility prop.

---

## 2. The first hundred

Every plan written so far assumed users we do not have. This is the smallest honest plan.

**The only proven-reach asset is the WhatsApp groups the original roasts already travelled in.**
Those lines moved between real Nigerians without an app, a link or a brand. That already happened
and it is the single piece of evidence this product rests on.

### The sequence

1. **Set `LIVE_URL` and deploy.** One string in `shayo.html`. Until it is set the app shows a
   red banner and every card leaves without a way back, which is the exact failure that has made
   the premise untestable for the life of the file.
2. **Seed the original groups.** Not a launch announcement. Post the card for the drink that
   person actually drinks, the way the lines travelled the first time. One card, one group, no
   explanation.
3. **Count one number: forward-through rate.** Cards sent, against `#d=` deep-link opens. The
   event log records `send`; the server logs record the opens. That ratio is the entire thesis
   and it has never been measured, because `shareUrl()` has never returned a link.
4. **Read `search_empty`.** Every miss is a drink somebody wanted roasted that does not exist
   yet. That is your content roadmap, written by users, for free.
5. **Read `repeat_lookup`.** Every repeat is somebody who came back to a drink and got the same
   joke. That is the countdown on the one-roast-per-drink problem.

### The kill rule, written before the data

If a hundred sent cards produce fewer than ten deep-link opens, forwarding is not the
distribution mechanism and no amount of product work fixes it. Decide that now, not after
looking at the number.

### What this plan is not

It is not growth. A hundred people is a measurement, not a business. Nothing about brand money,
the Index or act two should start moving until the ratio above exists.

---

## Sources

Apple App Review Guidelines, 1.4.3 / 2.3.6 / 4.7.5 / 1.2.1(a): developer.apple.com/app-store/review/guidelines.
Apple age rating change: developer.apple.com/news (updated age ratings in App Store Connect).
Google Play restricted content and alcohol wording: support.google.com/googleplay/android-developer.
Roast audit: read against the 73 lines in `shayo.html`, 13 September 2026.
