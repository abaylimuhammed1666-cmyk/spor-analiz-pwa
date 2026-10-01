const CACHE_NAME = 'gol-analiz-v1';

self.addEventListener('install', (e) => {
  console.log('[Service Worker] Yüklendi');
});

self.addEventListener('fetch', (e) => {
  e.respondWith(
    fetch(e.request).catch(() => caches.match(e.request))
  );
});