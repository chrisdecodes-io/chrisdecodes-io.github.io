const category = new URLSearchParams(location.search).get('category');
const target = category === 'prompting' || location.hash === '#start' ? '/?type=prompts'
  : category === 'workflows' ? '/?type=workflows' : '/';
location.replace(target);
