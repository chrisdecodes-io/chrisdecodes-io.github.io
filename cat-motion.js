// Approved silent loops. User-directed playback ignores OS reduced-motion preferences.
// Static posters remain visible until playback succeeds or when the format is unsupported.
const assetURLs = JSON.parse(document.querySelector('#character-assets')?.textContent || '{}');
const assetURL = path => assetURLs[path] || path;
const characters = [...document.querySelectorAll('.decoder-cat')];
const peekSlots = [...document.querySelectorAll('.peek-edge')];
let activePeek = -1;
const walkTrack = document.querySelector('.walk-track');
let walking = false;
let nextPeek = 0;
function fitWalkingTrack() {
  if (!walkTrack) return;
  const host = walkTrack.offsetParent.getBoundingClientRect();
  const banner = document.querySelector('.featured-panel').getBoundingClientRect();
  // Rise and dip behind the Featured edge, keeping the complete frame inside it.
  const left = banner.left;
  walkTrack.style.setProperty('--walk-left', `${left - host.left}px`);
  walkTrack.style.setProperty('--walk-width', `${banner.width}px`);
}
fitWalkingTrack();
window.addEventListener('resize', fitWalkingTrack);
function finishWalk() {
  if (!walking) return;
  walking = false;
  walkTrack.removeAttribute('data-walk-active');
  walkTrack.querySelector('video').pause();
  activatePeek(inViewport(peekSlots[0]) ? 0 : nextPeek);
  refreshCharacters();
}
function startWalk(next) {
  if (!walkTrack || !inViewport(walkTrack) || document.hidden) return false;
  fitWalkingTrack();
  const video = walkTrack.querySelector('video');
  if (!video.canPlayType('video/webm; codecs="vp9"')) return false;
  nextPeek = next;
  walking = true;
  walkTrack.querySelector('.decoder-cat').classList.remove('has-video');
  activatePeek(-1);
  const size = walkTrack.querySelector('.decoder-cat').getBoundingClientRect().width;
  const seconds = Math.min(17, Math.max(7.5, (walkTrack.clientWidth + size) / (size * .72)));
  walkTrack.style.setProperty('--walk-duration', `${seconds}s`);
  if (video.readyState) video.currentTime = 0;
  walkTrack.setAttribute('data-walk-active', '');
  refreshCharacter(walkTrack.querySelector('.decoder-cat'));
  return true;
}
walkTrack?.querySelector('.decoder-cat').addEventListener('animationend', event => { if (event.animationName === 'cat-crossing') finishWalk(); });
walkTrack?.querySelector('video').addEventListener('error', finishWalk);
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
  if (walking) {
    if (inViewport(walkTrack)) return;
    finishWalk();
  }
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
  if (action === 'walk' && !walking) { video.pause(); return; }
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
  const visible = !container.hidden && !document.hidden && (action === 'walk' ? inViewport(walkTrack) : container.getClientRects().length > 0 && bounds.bottom > 0 && bounds.top < innerHeight && bounds.right > 0 && bounds.left < innerWidth);
  if (!visible) { video.pause(); return; }
  if (!video.getAttribute('src')) {
    video.src = assetURL(`/assets/characters/${action}.webm`);
    video.muted = true;
  }
  video.play().catch(() => { container.classList.remove('has-video'); if (action === 'walk') finishWalk(); });
}
for (const container of characters) {
  const video = container.querySelector('video');
  video.addEventListener('playing', () => container.classList.add('has-video'));
  video.addEventListener('error', () => container.classList.remove('has-video'));
}
function refreshCharacters() { walkTrack?.toggleAttribute('data-walk-paused', document.hidden); followVisibleSection(); characters.forEach(refreshCharacter); }
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
    // Home tagline only: a slightly quicker arrival and shorter idle, full-speed dip.
    if (walkTrack && index === 0) {
      video.playbackRate = video.currentTime < 49 / 30 ? 1.12 : video.currentTime < 343 / 30 ? 1.18 : 1;
    }
    if (index === activePeek && Number.isFinite(video.duration) && video.currentTime >= video.duration - 19 / 30) {
      const next = (index + 1) % peekSlots.length;
      if (!startWalk(next)) activatePeek(next);
    }
  });
}
