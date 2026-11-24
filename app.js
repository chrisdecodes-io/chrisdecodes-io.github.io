const site = JSON.parse(document.querySelector('#site-config').textContent);
const types = site.types;
const params = new URLSearchParams(location.search);
if (location.pathname === '/' && (params.has('type') || params.has('q'))) {
  const target = new URL('/resources/', location.origin);
  if (Object.hasOwn(types, params.get('type'))) target.searchParams.set('type', params.get('type'));
  if (params.get('q')) target.searchParams.set('q',params.get('q'));
  location.replace(target);
}
const collection = document.querySelector('[data-collection]');
const search = document.querySelector('#resource-search');
const typeSelect = document.querySelector('#resource-type');
const cards = [...document.querySelectorAll('.resource-card')];
const clear = document.querySelector('#clear-filters');
let selectedType = collection?.dataset.collection || 'all';
if (collection && selectedType === 'all' && Object.hasOwn(types, params.get('type'))) selectedType = params.get('type');
function updateCatalog() {
  if (!collection) return;
  const query = search.value.trim().toLocaleLowerCase();
  const words = query.split(/\s+/).filter(Boolean);
  let matches = 0;
  let available = 0;
  for (const card of cards) {
    const matchesType = selectedType === 'all' || selectedType === card.dataset.type;
    if (matchesType) available++;
    card.hidden = !(matchesType && words.every(word => card.dataset.search.includes(word)));
    if (!card.hidden) matches++;
  }
  const type = types[selectedType];
  document.querySelector('#collection-title').textContent = type.title;
  document.querySelector('#collection-description').textContent = type.description;
  document.title = `${type.title} · Chris Decodes`;
  typeSelect.value = selectedType;
  for (const link of document.querySelectorAll('[data-nav]')) {
    if (link.dataset.nav === type.nav) link.setAttribute('aria-current','page');
    else link.removeAttribute('aria-current');
  }
  document.querySelector('#resource-count').textContent = `${matches} resource${matches === 1 ? '' : 's'}${query ? ' found' : ''}`;
  const empty = document.querySelector('#empty-state');
  empty.hidden = matches !== 0;
  const action = selectedType === 'skills' ? 'work' : selectedType === 'projects' ? 'presenting' : 'curious';
  for (const id of ['intro-cat','empty-cat']) document.getElementById(id).dataset.action = action;
  document.querySelector('#intro-cat').hidden = matches === 0;
  document.querySelector('#empty-title').textContent = available === 0 ? `No ${selectedType === 'all' ? 'resources' : selectedType} available yet` : 'No matching resources';
  document.querySelector('#empty-description').textContent = available === 0
    ? `Released ${selectedType === 'all' ? 'resources' : selectedType} will appear here with instructions and useful links.`
    : 'Try another name, task or app, or clear your search and filters.';
  clear.hidden = !query && selectedType === 'all';
  document.dispatchEvent(new Event('library:motion-update'));
}
if (collection) {
  search.value = params.get('q') || '';
  updateCatalog();
  search.addEventListener('input', () => {
    updateCatalog();
    const url = new URL(location.href);
    if (search.value.trim()) url.searchParams.set('q', search.value.trim());
    else url.searchParams.delete('q');
    history.replaceState(null,'',url);
  });
  typeSelect.addEventListener('change', () => {
    const type = typeSelect.value;
    const url = new URL(types[type].url, location.origin);
    if (search.value.trim()) url.searchParams.set('q',search.value.trim());
    location.assign(url);
  });
  clear.addEventListener('click', () => location.assign(types.all.url));
}
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
