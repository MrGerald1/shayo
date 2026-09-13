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
| Check a price before ordering | Prices → search the drink | 2 |
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
is open by default. A decrement writes a void and a replacement round, so the
receipt still shows what changed and when.

**The bill icon meant nothing.** It is a labelled segment inside Tonight now.

**The radar only offered ten drinks.** It searches all 73.

**The radar and the shelf had no entry point.** They are tabs.

---

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

| Frame | Needs | Says |
|---|---|---|
| This bar, before | 1 of your own figures | "₦1,400 is what you paid here before" |
| You, anywhere | 1 of your own figures | "₦1,400 is what you usually pay" |
| The area | 5 people | "₦1,400 is what people pay around here" |

**This answers from your first report.** A crowd median needs five strangers,
which is the cold start that kills Numbeo and that `DESIGN.md` already names as
the thing to avoid. Your own history needs one person.

Four verdicts, and the screen always says which frame it used and how thin it is:

- **Cheaper than usual** (15% or more under)
- **Normal** (within 15%)
- **They added something** (15 to 40% over)
- **They saw you coming** (40%+ over)

Crate Red is reserved for the top band, which is the bar overcharging you. It is
never used for how much you drank. That rule was already in `BRAND.md`.

The first time you price a drink there is no frame, and the screen says so rather
than inventing confidence: "First time you are pricing Star. From the next one we
can tell you if a bar is taking you."
