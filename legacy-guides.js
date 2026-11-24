const category = new URLSearchParams(location.search).get('category');
const target = category === 'prompting' || location.hash === '#start' ? '/resources/?type=prompts'
  : category === 'workflows' ? '/resources/?type=workflows' : '/resources/';
location.replace(target);
