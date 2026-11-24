const search = document.querySelector('#resource-search');
const category = document.querySelector('#resource-category');
function filterResources() {
  if (!search || !category) return;
  const query = search.value.trim().toLocaleLowerCase();
  let count = 0;
  for (const card of document.querySelectorAll('.resource')) {
    const matchesQuery = (card.textContent + ' ' + card.dataset.search).toLocaleLowerCase().includes(query);
    card.hidden = !matchesQuery || (category.value !== 'all' && category.value !== card.dataset.category);
    if (!card.hidden) count++;
  }
  document.querySelector('#resource-count').textContent = `${count} guide${count === 1 ? '' : 's'}`;
  document.querySelector('#no-results').hidden = count !== 0;
  for (const link of document.querySelectorAll('[data-topic]')) {
    if (link.dataset.topic === category.value) link.setAttribute('aria-current', 'true');
    else link.removeAttribute('aria-current');
  }
}
search?.addEventListener('input', filterResources);
category?.addEventListener('change', filterResources);
const sidebarToggle = document.querySelector('.sidebar-toggle');
sidebarToggle.addEventListener('click', () => {
  sidebarToggle.setAttribute('aria-expanded', String(sidebarToggle.getAttribute('aria-expanded') !== 'true'));
});
for (const link of document.querySelectorAll('#sidebar-links a')) {
  link.addEventListener('click', () => {
    if (link.dataset.categoryLink) {
      category.value = link.dataset.categoryLink;
      search.value = '';
      filterResources();
    }
    sidebarToggle.setAttribute('aria-expanded', 'false');
  });
}
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

if (category) {
  const requestedCategory = new URLSearchParams(location.search).get('category');
  if ([...category.options].some(option => option.value === requestedCategory)) category.value = requestedCategory;
  filterResources();
}
