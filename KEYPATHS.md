# Key paths

One row per job. Every feature has a permanent labelled home and a path you can
follow without guessing. Written 13 September 2026 after Kamso's critique that the
radar and the shelf were undiscoverable and the bill icon meant nothing.

## The navigation

A labelled bottom tab bar. Four tabs, always visible, always the same.

```
   Roasts        Tonight         Prices          You
   the feed      the tab         the radar       shelf + month
```

What it replaced: two unlabelled icons in the feed's top bar, with the tab behind
one of them and the radar and shelf buried two levels deeper behind that. Nobody
was going to find those. An icon is not a label.

Inside a tab, states are **segmented sub-tabs**, not new screens. Tonight is
`The tab | The bill`. Pushing a screen hides it; a segment shows it.

---

## The paths

| Job | Path | Taps |
|---|---|---|
| Roast my guy's drink | Roasts → Who you wan roast? → tap the drink → Send | 4 |
| See a roast at random | Roasts, swipe | 0 |
| Log a round of my usual | Tonight → tap the tile | 1 |
| Log a round for the table | Tonight → hold the tile → number | 3 |
| Log something not on my six | Tonight → Something else → **+ on the row** | 2 |
| Take one off | Tonight → − on the row | 1 |
| Remove a whole round | Tonight → − until it is gone | 1+ |
| Settle the bill | Tonight → The bill | 1 |
| Send the bill to the group | Tonight → The bill → Send the bill | 2 |
| Am I being overcharged | enter the price, the verdict comes back unasked | 0 |
| Check a price before ordering | Prices → Drinks → search | 3 |
| See which bars take me | Prices | 1 |
| See what a bar charges | Prices → tap the place | 2 |
| Log a drink I had at that bar | Prices → tap the place → + on the row | 3 |
| Report a price | Prices → drink → Add yours | 3 |
| See my month | You | 1 |
| Mark a night with no drinks | You → tap the night → Mark no drinks | 2 |
| See my shelf | You | 1 |

**The longest path in the product is four taps.** Anything longer is a defect.

---

## What was wrong, and what fixed it

**You could not log a drink that was not one of the six.** Tapping into a drink
from the picker gave you a roast and no way to add it. Two fixes: an **Add to
tonight** button on every drink page, and a dense list view in the picker when it
is opened for logging, with the **+** on the row. Beli's list rows carry their
actions inline so nothing needs a drill-in, and that is the right pattern here.
Adding from the list does not leave the list.

**There was no way to reduce the bill.** Press and hold on a badge was the only
way, which is invisible. Every row in tonight's list now has − and + and the list
is open by default.

**Changing a count does not add a line.** The log still records the change, which
is what lets the receipt prove a round was cancelled at 11:42pm, but +1 and −1 are
the same item at a new count rather than two more items, so the view folds the
chain into one row. One to four to two to zero is one line throughout.

**The bill icon meant nothing.** It is a labelled segment inside Tonight now.

**The radar only offered ten drinks.** It searches all 73.

**The radar and the shelf had no entry point.** They are tabs.

---

## Places

Prices has two segments: **Places** and **Drinks**. Places is a map of the bars
you have priced: one hotspot per bar, sized by how many prices you have there,
coloured by whether it charges you over your usual. Tap one for the drinks priced
there, each with its price and a verdict, and a **+** to log it.

**It is not a tiled geographic map.** Tiles need network and a geocoder, and
offline-first is a hard constraint in `SCOPE.md`, so there is no basemap to fall
back on in a basement bar with no signal. What the Snapchat map actually gives you
is hotspots you tap into, and that part is here in full. A real basemap is a
decision with a cost: a tile provider, a geocoder, a network dependency on a
screen that currently works offline, and an address for every bar somebody types
in. Worth doing when there are enough bars per user for geography to beat a list.

## Discoverability rules, going forward

1. **Every feature has a labelled home in the tab bar or a labelled segment
   inside one.** If it needs an icon to be found, it is not found.
2. **The row is the interface.** If a list item has an action, the action is on
   the row, not behind a tap into a detail page.
3. **Press and hold is never the only way to do anything.** It is a shortcut for
   something already possible with a visible control.
4. **A number never appears without its comparison and its sample size.** See
   below.
5. **Adding to a list does not navigate away from the list.**

---

## Prices: what transfers from Beli and what does not

Beli asks "which did you like better, X or Y?" instead of "rate this out of 10",
and builds a score out of the ordering.

**Do not copy that here.** Beli uses comparison because taste has no unit: your 7
and my 7 are different numbers about different things, so only an ordering is
reliable. Price has a unit and it is printed on the receipt. Asking somebody four
drinks in whether Quilox was dearer than Iya Basira adds exactly the friction Beli
is actually criticised for, and throws away the figure we could have had.

**What transfers is the layer underneath.** Beli's real insight is that a number
alone means nothing and the product's job is to supply the comparison set, not the
number. 9.1 is useless until it sits in your own ranked list.

So Shayo never shows a price without a frame, and the frames run **personal
first**:

| Frame | Needs | Reads as |
|---|---|---|
| This bar, before | 1 of your own prices | `here` |
| You, anywhere | 1 of your own prices | `your usual` |
| The area | 5 people | `the local price` |

**This answers from your first report.** A crowd median needs five strangers,
which is the cold start that kills Numbeo and that `DESIGN.md` already names as
the thing to avoid. Your own history needs one person.

Four verdicts, each with a bare comparison and never a sentence:

| Verdict | When | Reads as |
|---|---|---|
| **Good price** | 15% or more under | `28% under your usual` |
| **Normal** | within 15% | `your usual ₦1,400` |
| **Steep** | 15 to 40% over | `28% over here` |
| **Way over** | 40%+ over | `79% over your usual` |

Crate Red is reserved for the top band, which is the bar overcharging you. It is
never used for how much you drank. That rule was already in `BRAND.md`.

The first time you price a drink there is no frame, and the screen says **"No
history yet"** rather than inventing confidence. It does not explain why.

## How numbers are written

Beli never explains a number, it labels it: **9.1** with **2k** underneath. Shayo
does the same.

- **Figure, then unit, then nothing.** `₦1,400` over `You · 3 prices`.
- **Counts are bare.** `1 of 5 prices`, not "1 person has reported Hero here."
- **No sentence teaches the feature.** If the copy explains how the product works
  rather than what the number is, cut it.
- **Toasts are labels.** `Star ×3`, `Removed`, `Copied`.
