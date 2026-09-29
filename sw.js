const VERSION='sng-os-v1.0.0';
const SHELL=['./','./index.html','./assets/app.css','./assets/app.js','./assets/icon.svg','./manifest.webmanifest','./data/safeguarding_seed.json','./docs/CHAT_COMPENDIUM.md','./docs/ARCHITECTURE.md','./README.md'];
self.addEventListener('install',event=>event.waitUntil(caches.open(VERSION).then(c=>c.addAll(SHELL)).then(()=>self.skipWaiting())));
self.addEventListener('activate',event=>event.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(k=>k!==VERSION).map(k=>caches.delete(k)))).then(()=>self.clients.claim())));
self.addEventListener('fetch',event=>{
  if(event.request.method!=='GET') return;
  const url=new URL(event.request.url);
  if(url.origin!==location.origin) return;
  event.respondWith(caches.match(event.request).then(cached=>cached||fetch(event.request).then(response=>{
    const copy=response.clone(); caches.open(VERSION).then(c=>c.put(event.request,copy)); return response;
  }).catch(()=>caches.match('./index.html'))));
});
