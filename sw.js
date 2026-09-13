/* Shayo service worker.
   SCOPE.md calls offline-first a hard constraint, and queuing writes while the page
   is already open is not offline. Close the tab in a basement bar with no signal and
   without this there is no app at all.

   Cache-first for the shell, because the shell is one self-contained file that only
   changes when we deploy. Bump VERSION on every deploy or nobody gets the new build. */
const VERSION = "shayo-v1";
const SHELL = ["./", "./shayo.html", "./manifest.webmanifest", "./icon.svg"];

self.addEventListener("install", e => {
  e.waitUntil(
    caches.open(VERSION)
      .then(c => c.addAll(SHELL))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", e => {
  e.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(k => k !== VERSION).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", e => {
  const req = e.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);
  if (url.origin !== location.origin) return;

  e.respondWith(
    caches.match(req, {ignoreSearch:true}).then(hit => {
      if (hit){
        /* refresh in the background so the next open is current */
        fetch(req).then(res => {
          if (res && res.ok) caches.open(VERSION).then(c => c.put(req, res.clone()));
        }).catch(() => {});
        return hit;
      }
      return fetch(req).then(res => {
        if (res && res.ok && res.type === "basic"){
          const copy = res.clone();
          caches.open(VERSION).then(c => c.put(req, copy));
        }
        return res;
      }).catch(() => caches.match("./shayo.html"));
    })
  );
});
