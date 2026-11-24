const params = new URLSearchParams(location.search);
if (location.pathname === '/' && (params.has('type') || params.has('q'))) location.replace('/skills/');
const sidebarToggle = document.querySelector('.sidebar-toggle');
sidebarToggle?.addEventListener('click', () => {
  const expanded = sidebarToggle.getAttribute('aria-expanded') !== 'true';
  sidebarToggle.setAttribute('aria-expanded',String(expanded));
  sidebarToggle.querySelector('span').textContent = expanded ? '−' : '+';
});
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && sidebarToggle?.getAttribute('aria-expanded') === 'true') {
    sidebarToggle.setAttribute('aria-expanded','false');
    sidebarToggle.querySelector('span').textContent = '+';
    sidebarToggle.focus();
  }
});
document.querySelector('#copy-prompt')?.addEventListener('click', async () => {
  const prompt = document.querySelector('#starter-prompt');
  const status = document.querySelector('#copy-status');
  try {
    await navigator.clipboard.writeText(prompt.textContent);
    status.textContent = 'Copied. Replace the brackets with your task.';
  } catch {
    const selection = window.getSelection();
    const range = document.createRange();
    range.selectNodeContents(prompt);
    selection.removeAllRanges();
    selection.addRange(range);
    status.textContent = 'Prompt selected. Use your device’s Copy command.';
  }
});
