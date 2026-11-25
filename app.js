const params = new URLSearchParams(location.search);
const siteConfig = JSON.parse(document.querySelector('#site-config')?.textContent || '{}');
if (location.pathname === '/' && (params.has('type') || params.has('q'))) {
  const type = params.get('type');
  location.replace(['prompts','instructions','skills'].includes(type) ? siteConfig.types[type].url : '/');
}
const sidebarToggle = document.querySelector('.sidebar-toggle');
sidebarToggle?.addEventListener('click', () => {
  const expanded = sidebarToggle.getAttribute('aria-expanded') !== 'true';
  sidebarToggle.setAttribute('aria-expanded',String(expanded));
  document.querySelector('#sidebar-links').classList.toggle('is-open', expanded);
  sidebarToggle.querySelector('span').textContent = expanded ? '−' : '+';
});
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && sidebarToggle?.getAttribute('aria-expanded') === 'true') {
    sidebarToggle.setAttribute('aria-expanded','false');
    document.querySelector('#sidebar-links').classList.remove('is-open');
    sidebarToggle.querySelector('span').textContent = '+';
    sidebarToggle.focus();
  }
});
document.querySelectorAll('[data-copy-target]').forEach(button => button.addEventListener('click', async () => {
  const prompt = document.querySelector(button.dataset.copyTarget);
  const status = document.querySelector('#copy-status');
  let copyTimeout;
  try {
    await Promise.race([navigator.clipboard.writeText(prompt.textContent), new Promise((_, reject) => { copyTimeout = setTimeout(() => reject(new Error('Clipboard unavailable')), 1500); })]);
    status.textContent = button.dataset.copyMessage || 'Copied.';
  } catch {
    const selection = window.getSelection();
    const range = document.createRange();
    range.selectNodeContents(prompt);
    selection.removeAllRanges();
    selection.addRange(range);
    status.textContent = 'Text selected. Use your device’s Copy command.';
  } finally {
    clearTimeout(copyTimeout);
  }
}));
