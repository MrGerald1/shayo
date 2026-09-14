import io
p='shayo.html'; s=io.open(p,encoding='utf-8').read()
def rep(old,new,label):
    global s
    assert old in s, "MISS: "+label
    s=s.replace(old,new,1); print("ok",label)

# ── fold adjustment chains into one line ────────────────────────────────────
# The log stays append-only, because that is what lets the receipt say a round
# was cancelled at 11:42pm. But +1 and -1 are not new items, they are the same
# item at a new count, so the VIEW folds the chain and shows the live count.
rep("""function itemList(){
  const v = voidedIds();
  const rows = state.log.filter(e => e.type === "round" && e.night === state.night);
  if (!rows.length) return "";
  return `<div class="items">${rows.map(e => {
    const dead = v.has(e.id), d = BY[e.drink];
    return `<div class="item${dead ? " dead" : ""}">
      <span class="t">${clock(e.ts)}</span>
      <span class="nm">${esc(d ? d.name : e.drink)}</span>
      ${dead ? `<span class="gone">removed</span>` : `<span class="qty">
        <button data-a="dec" data-v="${e.id}" aria-label="One less ${esc(d ? d.name : e.drink)}">&minus;</button>
        <b>${e.qty}</b>
        <button data-a="inc" data-v="${e.id}" aria-label="One more ${esc(d ? d.name : e.drink)}">+</button>
      </span>`}
      <span class="pr">${e.price ? naira(e.qty * e.price) : "—"}</span>
    </div>`;
  }).join("")}</div>`;
}
function decRound(id){
  const e = state.log.find(x => x.id === id);
  if (!e || e.type !== "round") return;
  voidEvent(e.id, "reduced");
  if (e.qty > 1) log("round", {drink:e.drink, qty:e.qty - 1, price:e.price,
    night:e.night, seq:nextSeq(e.night), replaces:e.id});
}
function incRound(id){
  const e = state.log.find(x => x.id === id);
  if (!e || e.type !== "round") return;
  voidEvent(e.id, "increased");
  log("round", {drink:e.drink, qty:e.qty + 1, price:e.price,
    night:e.night, seq:nextSeq(e.night), replaces:e.id});
}""",
"""/* Rounds fold into lines. Changing a count writes a new event that points at the
   one it replaces, so the log stays append-only and a cancelled round is still
   provable. The bill does not show that plumbing: +1 and -1 are the same item at
   a new count, not two more items, so the chain collapses to one line. */
function chainsOn(night){
  const v = voidedIds();
  const byId = new Map(state.log.map(e => [e.id, e]));
  const groups = new Map();
  for (const e of state.log){
    if (e.type !== "round" || e.night !== night) continue;
    let root = e, guard = 0;
    while (root.replaces && byId.has(root.replaces) && guard++ < 500) root = byId.get(root.replaces);
    if (!groups.has(root.id)) groups.set(root.id, {root, events:[]});
    groups.get(root.id).events.push(e);
  }
  return [...groups.values()].map(g => {
    const alive = g.events.filter(e => !v.has(e.id));
    return {root:g.root, live:alive[alive.length - 1] || null};
  });
}
function itemList(){
  const rows = chainsOn(state.night);
  if (!rows.length) return "";
  return `<div class="items">${rows.map(c => {
    const e = c.live || c.root, d = BY[e.drink], dead = !c.live;
    return `<div class="item${dead ? " dead" : ""}">
      <span class="t">${clock(c.root.ts)}</span>
      <span class="nm">${esc(d ? d.name : e.drink)}</span>
      ${dead ? `<span class="gone">Removed</span>` : `<span class="qty">
        <button data-a="dec" data-v="${e.id}" aria-label="One less ${esc(d ? d.name : e.drink)}">&minus;</button>
        <b>${e.qty}</b>
        <button data-a="inc" data-v="${e.id}" aria-label="One more ${esc(d ? d.name : e.drink)}">+</button>
      </span>`}
      <span class="pr">${e.price ? naira(e.qty * e.price) : "—"}</span>
    </div>`;
  }).join("")}</div>`;
}
function adjustRound(id, delta){
  const e = state.log.find(x => x.id === id);
  if (!e || e.type !== "round") return;
  const next = e.qty + delta;
  voidEvent(e.id, delta > 0 ? "increased" : "reduced");
  if (next > 0) log("round", {drink:e.drink, qty:next, price:e.price,
    night:e.night, seq:nextSeq(e.night), replaces:e.replaces || e.id});
}
function decRound(id){ adjustRound(id, -1); }
function incRound(id){ adjustRound(id, 1); }""", "fold chains")

# the receipt folds too, and only shows a strike for a line actually removed
rep("""      ${rows.map(e => {
        const dead = v.has(e.id), d = BY[e.drink];
        const amt = e.qty * (e.price || 0);
        return `<div class="rrow${dead ? " dead" : ""}">
          <span class="t">${clock(e.ts)}</span>
          <span class="nm">${esc(d ? shortName(d) : e.drink)}${e.qty > 1 ? ` ×${e.qty}` : ""}</span>
          <span class="pr">${dead ? "-" : ""}${e.price ? Math.round(amt).toLocaleString("en-NG") : "—"}</span>
          ${dead ? `<span class="rm">removed</span>` : ""}
        </div>`;
      }).join("")}""",
"""      ${rows.map(c => {
        const e = c.live || c.root, dead = !c.live, d = BY[e.drink];
        const amt = e.qty * (e.price || 0);
        return `<div class="rrow${dead ? " dead" : ""}">
          <span class="t">${clock(c.root.ts)}</span>
          <span class="nm">${esc(d ? shortName(d) : e.drink)}${e.qty > 1 ? ` x${e.qty}` : ""}</span>
          <span class="pr">${e.price ? Math.round(amt).toLocaleString("en-NG") : "—"}</span>
          ${dead ? `<span class="rm">removed ${clock((state.log.find(x => x.type === "void" && x.target === c.root.id) || c.root).ts)}</span>` : ""}
        </div>`;
      }).join("")}""", "receipt fold")

rep("""  const night = state.night, v = voidedIds();
  const rows = state.log.filter(e => e.type === "round" && e.night === night);
  const live = rows.filter(e => !v.has(e.id));
  const total = nightTotal(night), n = nightCount(night);""",
"""  const night = state.night;
  const rows = chainsOn(night);
  const total = nightTotal(night), n = nightCount(night);""", "settle head")

rep("""  const first = rows[0], last = rows[rows.length - 1];""",
"""  const first = rows.length ? rows[0].root : null;
  const last = rows.length ? rows[rows.length - 1].root : null;""", "settle times")

io.open(p,'w',encoding='utf-8',newline='\n').write(s)
print("bill done")
