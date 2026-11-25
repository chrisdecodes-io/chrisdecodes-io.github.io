const config = JSON.parse(document.querySelector('#site-config')?.textContent || '{}');
const params = new URLSearchParams(location.search);
const type = params.get('type') || params.get('category');
location.replace(type ? config.legacyRoutes?.[type] || '/' : document.body.dataset.redirect || '/');
