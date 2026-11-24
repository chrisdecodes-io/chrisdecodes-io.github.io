// Approved silent loops. User-directed playback ignores OS reduced-motion preferences.
// Static posters remain visible until playback succeeds or when the format is unsupported.
const assetURLs = JSON.parse(document.querySelector('#character-assets')?.textContent || '{}');
const assetURL = path => assetURLs[path] || path;
const characters = [...document.querySelectorAll('.decoder-cat')];
const peekSlots = [...document.querySelectorAll('.peek-edge')];
let activePeek = -1;
function inViewport(element) {
  const box = element.getBoundingClientRect();
  return box.bottom > 0 && box.top < innerHeight && box.right > 0 && box.left < innerWidth;
}
function activatePeek(index) {
  activePeek = index;
  peekSlots.forEach((slot, i) => {
    slot.toggleAttribute('data-peek-active', i === index);
    const video = slot.querySelector('video');
    video.pause();
    if (video.readyState) video.currentTime = 0;
  });
  if (index >= 0) refreshCharacter(peekSlots[index].querySelector('.decoder-cat'));
}
function followVisibleSection() {
  if (activePeek >= 0 && inViewport(peekSlots[activePeek])) return;
  for (let step = 1; step <= peekSlots.length; step++) {
    const index = (activePeek + step) % peekSlots.length;
    if (inViewport(peekSlots[index])) { activatePeek(index); break; }
  }
}
function refreshCharacter(container) {
  const video = container.querySelector('video');
  const image = container.querySelector('img');
  const action = container.dataset.action;
  if (action === 'peek' && !container.closest('[data-peek-active]')) { video.pause(); return; }
  if (!video.canPlayType('video/webm; codecs="vp9"')) return;
  if (video.dataset.action !== action) {
    video.pause();
    video.removeAttribute('src');
    container.classList.remove('has-video');
    video.dataset.action = action;
    image.src = assetURL(`/assets/characters/${action}.png`);
    video.poster = image.src;
  }
  const bounds = container.getBoundingClientRect();
  const visible = !container.hidden && container.getClientRects().length > 0 && !document.hidden && bounds.bottom > 0 && bounds.top < innerHeight && bounds.right > 0 && bounds.left < innerWidth;
  if (!visible) { video.pause(); return; }
  if (!video.getAttribute('src')) {
    video.src = assetURL(`/assets/characters/${action}.webm`);
    video.muted = true;
  }
  video.play().catch(() => container.classList.remove('has-video'));
}
for (const container of characters) {
  const video = container.querySelector('video');
  video.addEventListener('playing', () => container.classList.add('has-video'));
  video.addEventListener('error', () => container.classList.remove('has-video'));
}
function refreshCharacters() { followVisibleSection(); characters.forEach(refreshCharacter); }
document.addEventListener('library:motion-update', refreshCharacters);
document.addEventListener('visibilitychange', refreshCharacters);
refreshCharacters();

// Load/play a character only when its reserved area enters the viewport.
if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver(() => refreshCharacters());
  characters.forEach(container => observer.observe(container));
}


// Each appearance completes its opaque dip before another section receives it.
for (const [index, slot] of peekSlots.entries()) {
  const video = slot.querySelector('video');
  video.addEventListener('timeupdate', () => {
    if (index === activePeek && Number.isFinite(video.duration) && video.currentTime >= video.duration - 19 / 30) {
      activatePeek((index + 1) % peekSlots.length);
    }
  });
}
