// Approved silent loops. User-directed playback ignores OS reduced-motion preferences.
// Static posters remain visible until playback succeeds or when the format is unsupported.
const assetURLs = JSON.parse(document.querySelector('#character-assets')?.textContent || '{}');
const assetURL = path => assetURLs[path] || path;
const characters = [...document.querySelectorAll('.decoder-cat')];
function refreshCharacter(container) {
  const video = container.querySelector('video');
  const image = container.querySelector('img');
  const action = container.dataset.action;
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
function refreshCharacters() { characters.forEach(refreshCharacter); }
document.addEventListener('library:motion-update', refreshCharacters);
document.addEventListener('visibilitychange', refreshCharacters);
refreshCharacters();

// Load/play a character only when its reserved area enters the viewport.
if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver(entries => entries.forEach(entry => refreshCharacter(entry.target)));
  characters.forEach(container => observer.observe(container));
}
