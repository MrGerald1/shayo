# Shayo, build plan

Output of `/plan-design-review`, then `/plan-eng-review`, then `/plan-ceo-review`, each with an
independent adversarial pass. September 2026. Corrections are kept visible rather than quietly
swapped, because burying a reversal is how "Built, real photography" survived next to proof that
the photo path never ran.

`SCOPE.md` owns the thesis and what is in or out. `DESIGN.md` owns components and screens.
`BRAND.md` owns colour, type, tokens and voice. This file owns defects, architecture and order
of work.

---

## Where this landed

**Act one is banter. Act two is money. One product, one schema.** The feed stays home. The dock
stops asking "Wetin I go drink?" and starts asking **"Who you wan roast?"**, which serves the
person doing the roasting rather than the person drinking. A roast card is the atom: the feed
serves them at random, naming serves the one you asked for.

Act two, the tab and ledger and radar, is fully specified here and in `DESIGN.md` and is
deferred until act one passes its success criteria. None of that work is wasted; each becomes a
view over a log act one is already writing.

```
              +-----------------------------+
              |   HOME = the feed           |   discovery
              |   one roast per screen      |
              |   [Na me]   [Send]          |   every slide is a sendable card
              |  +-----------------------+  |
              |  |  Who you wan roast?   |  |   on every screen
              |  +-----------------------+  |
              +--------------+--------------+
                             |
                             v
              +-----------------------------+   intent
              |  the picker: 73 drinks      |
              |  search, filters, aliases   |
              +--------------+--------------+
                             |
                             v
              +-----------------------------+
              |  that drink's card          |
              |  roast, who drinks it,      |
              |  can they handle it         |
              |  [Send] -> 1080x1920 card   |
              +-----------------------------+

  deep link  ->  18+ gate  ->  full-screen roast  ->  "see what yours says"  ->  home
```

---

## Defects in the built file

All still present. Three critical ones block everything else.

| # | What | Severity | Where |
|---|---|---|---|
| B1 | `findPhoto()` and `repaintPhotos()` are never called from anywhere. The photo path is unreachable code. Pasting a Pexels key changes nothing. The old SCOPE.md claim of "Built, real photography" was false, and the photo debt in TODOS described a system that never ran | critical | `shayo.html:219,233` |
| B2 | `store` gates on `window.storage`, the artifact host object, not a web API. In any real browser nothing persists and every write fails silently | critical | `shayo.html:605` |
| B3 | Deep links set `state.screen = "drink"` directly, bypassing the 18+ gate. That is the primary growth path. `enter()` never records the answer either, so everyone else is re-gated daily | critical | `shayo.html:944`, `902` |
| B4 | `actions.mine` calls `render()`, which rewrites all of `#app` with no scroll restore. Claiming a drink on slide 14 throws you back to slide 1 | high | `shayo.html:908`, `853` |
| B5 | `LIVE_URL` is empty and the fallback rejects both `file:` and the preview host, so `shareUrl()` returns `""`. Nothing has ever been forwarded with a link back | high | `shayo.html:205`, `586` |
| B6 | Search never reads `d.m`, so "Henny" hits the empty state, which then tells you to try the brand name. You did | high | `shayo.html:688` |
| B7 | One `@media` in 956 lines, and it is `prefers-reduced-motion` | high | `shayo.html:197` |
| B8 | Status card, crate pattern and progress tick: zero occurrences. Three of BRAND.md's four elements do not exist. The only animation is the coach thumb, which BRAND.md's "and nothing else" clause forbids | high | whole file |
| B9 | `d.p` and `d.t` are on all 73 drinks and read by nothing | medium | whole file |
| B10 | Tap targets under BRAND.md's own 48px rule: `.more` 44, `.iconbtn` 44, `.chip` 38. The 44px one is the only navigation out of the feed | medium | `shayo.html:59,67,110` |
| B11 | Safety line appears twice on secondary screens and never on the screen users spend most time on | medium | `shayo.html:776,806` |
| B12 | `theme-color` is ink, but three of five screens are paper | low | `shayo.html:6` |
| B13 | Dead code: `state.seenIdx` written never read, `const dot` unused, a storage key nothing loads | low | `shayo.html:868,752,229` |
| B14 | 18+ copy in the build differs from BRAND.md's copy library. One of the two is not the source of truth | low | `shayo.html:640` vs BRAND.md |

---

## Architecture

### Decisions, with the reversals shown

| # | Decision | Note |
|---|---|---|
| E2 | **Git first. Tests on the pure functions only** | `tolerance`, `baseline`, `fam`, `prescribe`, plus the card renderer. No browser runner: layout gets checked on a phone |
| E3 | ~~Native ES modules~~ **Stay one file** | **REVERSED.** Module imports are fetched with CORS and a `file://` origin is opaque, so every import fails and the file you WhatsApp to somebody would not run. Splitting without hashed filenames also produces partial-update cache skew in the field. Actual logic is about 400 lines; the rest is data and CSS |
| E6 | ~~Mount-once render layer~~ **Patch the two call sites** | **REDUCED.** It hurts at `actions.mine` and the search re-render. Sixty lines of hand-written framework owned forever, to fix two bugs, is not a trade worth making yet |
| E7 | ~~IndexedDB~~ **localStorage, capped** | **REVERSED.** A heavy user writes roughly 700 events a year, about 84KB, against a 5MB budget. localStorage is synchronous, which matters because the latency risk is the async cold open before first paint. WebKit ITP also evicts IndexedDB after 7 days idle, which would delete a fortnightly user's history |
| E8 | **Named errors. No bare catch in new code** | This is what hid B2 for the entire life of the file |
| E9 | **Window the feed, drop `backdrop-filter`** | 73 full-viewport slides and 146 live GPU blur layers mount at launch today |
| E10 | **Self-host one Archivo variable woff2** | Six static weights over a render-blocking third-party request, against a 70KB spec. Moves to week one |
| E13 | **Service worker, precache the app** | SCOPE.md calls offline-first a hard constraint, and queuing writes while the page is open is not offline. Close the tab in a basement bar and there is no app. About 20 lines, and it was in none of the earlier plans |
| E15 | **The panel is an export projection, not the raw log** | The log carries device ids, typed venue names and void noise |
| E16 | **Two latency budgets** | Tap to paint under 100ms from memory, write fire-and-forget. Cold start to first tap is the one that will actually fail, so the store opens during boot |

### The event log

Minimal fields only. Derived values lock in definitions that have not been made.

```
{ id, v, deviceId, ts, tzOffset, type, ...payload }

  type: name | send | search | search_empty | repeat_lookup | choice | void
```

`repeat_lookup` versus `name` is the signal that the roasts have run out, and `search_empty`
tells you which drinks are missing. Both matter more to act one than anything act two needs, and
neither was in the first draft of this plan.

Dropped from the earlier version: `night` and `seq`. Both solve ordering for a ledger that is
not being built. Act two adds them when act two exists.

**Durability.** Claiming accumulated data is unrecoverable while shipping local-only storage is a
contradiction, because the log is already lost on every phone upgrade. Act one ships an anonymous
device id and an append-only sync to something free, or the schema work loses its stated reason.

---

## Order of work

### Week 1, ship the funnel, about 1 day human / 1.5h CC

The only code that creates users is broken. Nothing has ever been forwarded with a link back, so
the premise the whole roadmap rests on has never been tested.

| | Task | Defect |
|---|---|---|
| W1.1 | `git init`, commit as-is | |
| W1.2 | localStorage persistence, replacing `window.storage` | B2 |
| W1.3 | Age gate persists, deep links route through it | B3 |
| W1.4 | `LIVE_URL` set, share link fails loudly in dev when empty | B5 |
| W1.5 | Patch the two render call sites | B4 |
| W1.6 | Service worker, precache | E13 |
| W1.7 | Self-host the Archivo variable file | E10 |
| W1.8 | Read `d.m` so "Henny" finds Hennessy | B6 |

### Week 2, act one, about 4 days human / 5h CC

| | Task |
|---|---|
| W2.1 | The share card. One component, DOM and 1080x1920 canvas. Physical constraints in `DESIGN.md` |
| W2.2 | The naming loop. Dock becomes "Who you wan roast?" on every screen, opens the picker, card with Send primary |
| W2.3 | Search promoted to primary. Filters on strength, venue, taste. Price band labelled as a band |
| W2.4 | Event log, minimal schema, with `send`, `search`, `search_empty` and `repeat_lookup` wired |
| W2.5 | Multiple roasts per drink, rotated on repeat lookup. A writing task, not engineering |
| W2.6 | Delete the unreachable photo path, commit to the poster (B1) |
| W2.7 | Window the feed, drop the blur layers (E9) |

### Week 3, polish and launch, about 2 days human / 2h CC

| | Task |
|---|---|
| W3.1 | Responsive. A real desktop layout for the shared-card route, an honest phone frame elsewhere (B7) |
| W3.2 | Accessibility: landmarks, headings, 48px targets, keyboard advance (B10) |
| W3.3 | Brand elements: crate pattern and the progress tick, the status card having landed in W2.1 (B8) |
| W3.4 | The boundary document for brand money |
| W3.5 | Resolve web versus install, and the app store alcohol policies |
| W3.6 | The first-hundred plan. Seed the WhatsApp groups the roasts already travelled in |

### Then, gated on evidence

The Shayo Index at its minimum credible unit, 12 SKUs across 3 Lagos areas and 10 venues,
quarterly, with a published kill rule. Then act two, on the success criteria in `SCOPE.md`.

---

## Act two, specified and parked

Everything below is designed and waiting. `DESIGN.md` carries the component detail.

- **The tab.** Six tiles of your usual drinks, tap adds one, badge increments in place, press
  and hold for a bulk round because a Nigerian round is bought for a table.
- **The running total.** A sum, never a remainder, and it never changes colour.
- **Settle.** A paper till receipt. The time column is the asymmetric evidence, because a
  waiter's handwritten tally has none.
- **The ledger.** A month grid with markable dry nights that never count, chain or congratulate.
  Translation into gigabytes, fares or shoes, never school fees.
- **The price radar.** Recruiting empty state, count not median below five reporters.
- **Identity.** Your shelf, Wrapped.

Act two also reinstates `night` and `seq` in the schema, adds the void flow, and re-opens the
render question, which is where a real update layer finally earns its keep.

---

## Test plan

Coverage today is zero. Five of these are mandatory regression tests for defects that are live
right now.

```
[+] storage
  |-- [GAP] REGRESSION survives reload in Chrome and Safari      (B2)
  |-- [GAP] private mode fails loudly rather than silently
  +-- [GAP] replay of the same id writes one row
[+] age gate
  |-- [GAP] REGRESSION deep link shows the gate first            (B3)
  +-- [GAP] REGRESSION the answer survives relaunch              (B3)
[+] share
  |-- [GAP] REGRESSION the card carries a working link           (B5)
  +-- [GAP] card renders identically to DOM and canvas
[+] search
  +-- [GAP] REGRESSION "Henny" finds Hennessy                    (B6)
[+] feed
  +-- [GAP] REGRESSION claiming keeps scroll position            (B4)
[+] roast rotation
  +-- [GAP] repeat lookup of one drink returns a different line
[+] pure functions
  +-- [GAP] tolerance, baseline, fam, prescribe

COVERAGE: 0/12  |  REGRESSIONS: 5, mandatory
```

---

## GSTACK REVIEW REPORT

| Run | Status | Findings |
|---|---|---|
| plan-design-review, 7 passes | complete | 14 defects, 3 critical. 6 decisions. Scores were self-assessed and are not evidence |
| plan-design-review, outside voice | `[single-model]` | Codex out of quota until 2026-09-27. Independent reviewer found B1, B6, B9, B10, B12, B13 |
| plan-eng-review, Step 0 | triggered | 5 modules and a shell into a single file with no git, no tests, no build |
| plan-eng-review, 4 sections | 6 findings | E4 four modules were one log and three folds. E5 four tasks depended on an absent backend. E6 four tasks patched one cause. E8 the build is entirely catch-all handlers while SCOPE.md forbids them. E9 and E10 on load cost |
| plan-eng-review, outside voice | `[single-model]` | **Reversed E3 and E7, reduced E6.** Added the service worker, the schema fields, the export projection, two latency budgets |
| plan-ceo-review, SCOPE EXPANSION | 7 decisions | Premise challenged and changed: the only observed behaviour is banter. Party calculator killed by Kamso on the despite test. Community roasts deferred. Brand boundary and the Index accepted. Schema now, features later |
| plan-ceo-review, market research | complete | Panel weakened on representativeness. No affiliate route at any delivery partner. WhatsApp closed to alcohol here. The regulatory opening found: broadcast and outdoor alcohol ads sit behind a watershed (TV and outdoor 6am-10pm, radio 6am-8pm) while digital is untouched |
| plan-ceo-review, adversarial pass | 5/10, 12 issues, all applied | Largest: there was no distribution plan and no web-versus-install decision. The "a lookup does not exhaust" argument was a rationalisation. The boundary contradicted itself. Brand money at zero users is a slide. The Index was costed without its ongoing half. The schema's justification was cancelled by local-only storage |
| Defects | 14 | 3 critical, 5 high, 3 medium, 3 low |

**VERDICT:** the plan survived three reviews and two reversals and is smaller than it started.
The single strongest finding across all three was not technical: fifteen tasks and five sprints
of architecture sat on top of a forwarding premise that has never been tested, because
`shareUrl()` has never returned a link. Week one tests it for about a day of work. The second
strongest was the adversarial pass noticing that no document in this project said how anyone
finds out Shayo exists.

**CROSS-MODEL:** absorbed, single-model on all three passes.

**UNRESOLVED DECISIONS:**
- Web or installed app. Blocking, and it interacts with the app store question.
- Apple and Google alcohol content and age-gating policies. A launch blocker, not researched.
- The first hundred users. No plan exists that does not assume users we do not have.
- ARCON pre-vetting. A blocker on selling to any brand, not on act one.
- Panel packaging, given that representativeness rather than scale is the problem.
