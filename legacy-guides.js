const config = JSON.parse(document.querySelector('#site-config')?.textContent || '{}');
const params = new URLSearchParams(location.search);
const type = params.get('type') || (params.get('category') === 'prompting' ? 'prompts' : params.get('category') || 'home');
location.replace(['prompts','instructions','skills'].includes(type) ? config.types[type].url : '/');
