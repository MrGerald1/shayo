# Shayo , Brand (engineering reference)

> Companion to the 26-page brand guide (`Shayo-Status-Brand-Guide.pdf`).
> Where this conflicts with anything in the previous `shayo-status.html` build, **this file wins**.
> Every contrast number below was computed with `brandkit.py`, not estimated.

## The one-liners

> **Updated September 2026** after `/plan-ceo-review` split the product into two acts. The
> essence survives, because the Nigerian sense of *receipts* is exactly what a roast is:
> evidence of what somebody did. Positioning, enemy and the shipping question were written for
> the money thesis and are corrected below. Colour, type, tokens and the elements are unchanged.

- **Essence:** Receipts. Nigerian for evidence. A roast is receipts on somebody, the tolerance
  answer is receipts on you, and in act two the tab prints them literally. Review filter:
  *what does this screen have receipts for?*
- **Positioning, act one:** For Nigerians in their twenties and thirties who drink socially,
  Shayo is where you get something to say about what your friend is drinking. The roast is the
  product and the card you send is the unit.
- **Positioning, act two:** the same receipts turned on your own money. What the night cost, and
  whether this bar is charging you double.
- **Enemy, act one:** having nothing to say. The silence when your guy orders something
  ridiculous and the best you manage is a laugh.
- **Enemy, act two:** the shrug, and the waiter. The shrug is not counting. The waiter is
  instant, free and trusted, so the tab has to beat a human standing right there.
- **Personality:** roadside honest · local first · deadpan · generous · sober about consequences.
- **The shipping question:** does it survive the second month? The old answer, that a roast does
  not and a running total does, was half right. A roast *feed* does not survive, because 73 is
  one evening. A roast *lookup* survives as long as there are lines left, which is why act one
  ships several roasts per drink and why user submission is the permanent fix.

## Colour

The pairing rule: **every brand colour carries exactly one text colour, and it is one of the
two neutrals. Look it up, never choose it. White is banned as a text colour.**

| Name | Hex | Token | Text on it | Ratio | Grade |
|---|---|---|---|---|---|
| Signboard (paper) | `#F6F1E2` | `--sy-paper` | Ink | 16.50:1 | AAA |
| Tarmac (ink) | `#16120F` | `--sy-ink` | Paper | 16.50:1 | AAA |
| Danfo Yellow | `#F5B301` | `--sy-yellow` | Ink | 10.05:1 | AAA |
| Crate Red | `#C62026` | `--sy-red` | Paper | 5.12:1 | AA |
| Star Blue | `#1B4A8B` | `--sy-blue` | Paper | 7.75:1 | AAA |
| Harvest Green | `#1E7A45` | `--sy-green` | Paper | 4.74:1 | AA |
| Muted ink | `#57504A` | `--sy-muted` | on Paper | 7.01:1 | AAA |

```ts
export const TEXT_ON: Record<string, string> = {
  "#F5B301": INK,    // 10.05:1
  "#C62026": PAPER,     // 5.12:1
  "#1B4A8B": PAPER,     // 7.75:1
  "#1E7A45": PAPER, // 4.74:1
};
```

White on Danfo Yellow is 1.85:1. That is why the map exists.

### Ramps (generated, never hand-picked)

| Colour | Deep (type only) | Core | Soft (fill) | Mist (card fill) |
|---|---|---|---|---|
| Danfo Yellow | `#976F07` | `#F5B301` | `#F6D57D` | `#F6E8C2` |
| Crate Red | `#7C1A1C` | `#C62026` | `#E0938D` | `#EFD4C8` |
| Star Blue | `#193257` | `#1B4A8B` | `#93A6BB` | `#D7DAD6` |
| Harvest Green | `#1B4E2E` | `#1E7A45` | `#95BB9B` | `#D8E0CC` |

- `#F6E8C2` (yellow mist) carries Ink at 15.29:1
- `#EFD4C8` (red mist) carries Ink at 13.23:1
- `#D7DAD6` (blue mist) carries Ink at 13.20:1
- `#D8E0CC` (green mist) carries Ink at 13.71:1

### The yellow rule

Danfo Yellow passes on paper (10.05:1 with Ink) but
`brandkit.is_glary` returns **true**: luminance 0.52 with high
chroma vibrates at scale. The constraint is area, not hue.

- Allowed: primary buttons, the cork, active tab, one block or one headline word per screen, app icon.
- Not allowed: page background behind body text, status-card fill for a long roast, two large blocks on one screen.
- Need a big warm field? Use `#F6E8C2`.
- Dominance per screen: paper 60 · ink 25 · yellow 10 · one accent 5.

### Functional colours

Harvest Green = every yes, success, "Oya go". Crate Red = every no, warning, destructive,
"avoid tonight", and the WhatsApp share button. Deliberately the same values as the verdicts so
the app has one language for good and bad.

## Typography

One family: **Archivo** (variable 400-900, one 70 KB woff2). Mono: **IBM Plex Mono 600**, used
only for hex, tokens, ratios and the daily-game grid. Stack: `Archivo, system-ui, sans-serif`.

| Role | Size / line | Weight | Tracking |
|---|---|---|---|
| Roast display | 40 / 40 | 900 | -0.04em |
| Screen H1 | 32 / 34 | 800 | -0.03em |
| Section H2 | 21 / 26 | 800 | -0.02em |
| Roast body | 17 / 23 | 500 | 0 |
| Body | 15.5 / 23 | 400 | 0 |
| Label | 13 / 16 | 600 | 0 |
| Eyebrow | 11 / 12 | 700 | 0.18em |
| Tab | 11 / 12 | 600 | 0.01em |

Rules: body copy caps at 34 characters on a phone. No size between two rows of this table ,
if a screen seems to need one, the layout is wrong. Wordmark is lowercase always, Archivo 900
at -0.045em.

## Elements

- **Core shape:** the status card. Flat drink colour, 24px radius, three progress ticks top,
  centred text, SS badge top-left. Identical on screen, as a 1080×1920 PNG, and on a poster.
- **Pattern:** the crate. 6×4 grid of bottle tops, line art, tile at 320px. 8% behind body
  copy, 20% on flat colour, 55% on a Tarmac divider. Never above a status card or behind roast text.
- **Mark:** crown cork. Crimped ring r43.5 (dash 4.1/4.05), rings r36 and r20 on a 100 grid.
- **Motion constant:** the status progress tick, 5-13s per roast scaled to length, and nothing else.

## Layout

| Token | Value |
|---|---|
| Page margin | 20px |
| Grid | 2 columns, 14px gutter |
| Vertical step | 8px, sections 24px apart |
| Radius | card 20, status card 24, pill 999 |
| Minimum tap target | 48px |

## Voice

Measured from the 73 shipped roasts: 2,710 words, **7.7 words per sentence**, 37 words per
roast, second person, pidgin as seasoning not base.

The four-beat roast: **name it** (caps, own line) · **say the true thing** (one flat sentence)
· **twist it** (goes further than expected) · **land it** (short, no moral, no wink).

Copy library:

| Situation | Line |
|---|---|
| Verdicts | Oya go · Small small · You never reach · Even you, calm down · You don pass am |
| Empty state | We never roast that one yet. Try the brand name. |
| Error | That did not save. Try again. |
| Share prompt | Post it and see who replies. |
| 18+ gate | If you are not 18 yet, abeg go and drink Chapman. |
| Safety line | 18+. Drink responsibly. Nobody is driving tonight. Water between rounds is not weakness. |
| Running total | 4 Star. ₦6,000. Tonight. |
| Month in review | ₦48,200 last month. That is a return ticket to Accra. |
| Over budget | This round puts you past your ₦40,000. Your call. |
| Price warning | ₦2,500? Star is ₦1,400 around here. Ask them why. |
| Bill dispute | 11 bottles between 8:42pm and 1:15am. Here is the list. |

**Four places with no jokes at all:** money, the bill, age, safety. A total that tries to be
funny is a total nobody trusts, and the tab exists to be trusted at 1am. Never scold about
spend: show the number and stop. Money type is display weight, tabular figures, naira sign
always, never abbreviated on the ledger. Crate Red means the bar overcharged, never that you
drank too much.

Never write: "Oops!", "We're sorry", "Cheers!", "Remember to hydrate", "curated",
"experience", "journey", any emoji in a heading, any word that needs a dictionary.

## Migration from the current build

`/mnt/user-data/outputs/shayo-status.html` today:

| Was | Now | Order |
|---|---|---|
| 87 unique hex literals, 15 CSS vars | 6 colours + 16 ramp steps, all tokens | 1 |
| `Bricolage Grotesque` + `Schibsted Grotesk` | Archivo, one file | 2 |
| 15 hand-drawn drink doodles tiled at 380px | one crate pattern | 3 |
| guessed margins and sizes | 20px margin, 8px step, this scale | 4 |
| white text on mid-tone fills | `TEXT_ON` lookup | with 1 |

Colour first. The 87 literals happened because colour was done last.

## Review checklist

- [ ] No hex literal in a component. Tokens only.
- [ ] Every coloured fill takes its text colour from `TEXT_ON`.
- [ ] No `#FFF` as a text colour anywhere.
- [ ] Yellow area under ~10% of the screen.
- [ ] One crate pattern per screen, at most.
- [ ] Safety line present once, at the foot.
- [ ] No word in the never-write list.
- [ ] Tap targets ≥ 48px.
