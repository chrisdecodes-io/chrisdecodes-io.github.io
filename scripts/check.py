"""Check generated pages, local destinations, downloads and release scope."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,hashlib,xml.etree.ElementTree as ET
root=Path(__file__).resolve().parent.parent
class Page(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.refs=[];self.h1=0;self.videos=[];self.images=[];self.heading=False;self.heading_text=[];self.text=[];self.ignore_text=False;self.tile_count=0;self.home_tiles=[];self.nav_items=[];self.in_sidebar=False;self.in_h1=False;self.h1_text=[]
 def handle_starttag(self,t,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if t in ['script','style']:self.ignore_text=True
  if 'home-tile' in a.get('class','').split():self.tile_count+=1;self.home_tiles.append(a)
  if t=='nav' and a.get('id')=='sidebar-links':self.in_sidebar=True
  if t=='a' and self.in_sidebar and 'data-nav' in a:self.nav_items.append(a.get('data-nav'))
  if t=='h1':self.h1+=1;self.in_h1=True
  if t in ['h1','h2','h3']:self.heading=True
  if t=='video':self.videos.append(a)
  if t=='img':self.images.append(a)
  for k in ['src','href','poster']:
   if k in a:self.refs.append(a[k])
 def handle_endtag(self,t):
  if t in ['script','style']:self.ignore_text=False
  if t=='nav':self.in_sidebar=False
  if t=='h1':self.in_h1=False
  if t in ['h1','h2','h3']:self.heading=False
 def handle_data(self,s):
  if not self.ignore_text:self.text.append(s)
  if self.heading:self.heading_text.append(s)
  if self.in_h1:self.h1_text.append(s)
pages={}
for p in root.rglob('*.html'):
 if '.git' in p.parts:continue
 q=Page();q.feed(p.read_text());pages[p]=q
 assert q.h1==1,(p,'one h1 required')
 if p not in [root/f'{name}/index.html' for name in ['guides','resources','projects','prompts','instructions']]:
  assert p.read_text().count('class="peek-edge"')==3,(p,'three distinct peek slots required')
  assert q.nav_items==[item['id'] for item in json.loads((root/'data/site.json').read_text())['navigation']],(p,'unexpected sidebar entries')
  text=' '.join(' '.join(q.text).split())
  assert text.count("Understand what's possible. Decide what matters to you.")==1,(p,'tagline must appear once')
 assert len(q.ids)==len(set(q.ids)),(p,'duplicate IDs')
 for text in q.heading_text:
  assert not(text.strip().isupper() and len(text.strip())>2),(p,'all-caps heading')
 for im in q.images:assert 'alt' in im,(p,'missing image alternative')
 for v in q.videos:assert 'loop' in v and 'muted' in v and 'playsinline' in v and 'controls' not in v,(p,'unexpected character playback controls')
for p,q in pages.items():
 for x in q.refs:
  u=urlsplit(x)
  if u.scheme:continue
  dest=(root/unquote(u.path.lstrip('/'))) if u.path.startswith('/') else p.parent/unquote(u.path) if u.path else p
  if dest.is_dir():dest=dest/'index.html'
  assert dest.is_file(),(p.relative_to(root),x)
  if u.fragment:assert u.fragment in pages[dest].ids,(p,x,'missing fragment')
home=pages[root/'index.html']
assert ' '.join(' '.join(home.h1_text).split())==json.loads((root/'data/site.json').read_text())['tagline'],'Home must lead with the approved tagline'
original=[p.attrib['d'] for p in ET.parse(root/'assets/wordmark-ink.svg').getroot().iter() if p.tag.endswith('path')]
cta=[p.attrib['d'] for p in ET.parse(root/'assets/wordmark-cta-ink.svg').getroot().iter() if p.tag.endswith('path')]
assert original==cta,'CTA wordmark must preserve the original approved outlines and stacked arrangement'
assert (root/'index.html').read_text().count('class="platform-token"')==4,'Home should show four named platform marks flanking the tagline'
assert home.tile_count==5,'Home must highlight Skills, the three channels and About Chris'
assert [item['id'] for item in json.loads((root/'data/site.json').read_text())['navigation']]==['home','skills','about'],'Navigation should prioritize Skills without a resource taxonomy'
assert all('href' in tile for tile in home.home_tiles),'All confirmed Home destinations should be linked'
assert 'featured-title' in home.ids,'Featured must have its own labeled panel'
assert (root/'resources/index.html') in pages
items=json.loads((root/'data/resources.json').read_text())
assert len(items)==1 and items[0]['id']=='task-context-starter-prompt','Initial release must contain only the existing approved prompt'
for item in items:
 assert (root/item['download'].lstrip('/')).read_text()==item['content']+'\n','Download differs from displayed prompt'
 assert (root/f"resources/{item['id']}/index.html").exists()
usage=json.loads((root/'assets/characters/usage.json').read_text())
for name,asset in usage['assets'].items():
 assert hashlib.sha256((root/f'assets/characters/{name}.webm').read_bytes()).hexdigest()==asset['sha256']
print(f'{len(pages)} pages checked: headings, links, assets, fragments, video attributes and prompt download match.')
assert all(asset['frames']==390 and asset['seconds']==13 if name=='peek' else asset['frames']==30 and asset['seconds']==1 if name=='walk' else asset['frames']==360 and asset['seconds']==12 for name,asset in usage['assets'].items()),'Use original full gestures or the recorded complete 13-second peek composition'
print('Release scope: one public prompt, approved character animations; no private resource imports.')

font_usage=json.loads((root/'assets/wordmark-editorial-usage.json').read_text())
assert hashlib.sha256((root/'assets/WordmarkEditorial.ttf').read_bytes()).hexdigest()==font_usage['sha256'],'Tagline font differs from selected wordmark-led source'
assert (root/'assets'/font_usage['license']).is_file(),'Tagline font license must ship with the website'

assert (root/'index.html').read_text().count('class="walk-track"')==1,'Home has one reserved walking lane'
assert all('class="walk-track"' not in p.read_text() for p in pages if p!=root/'index.html'),'Walking interlude is Home-only'

skill_page=(root/'skills/index.html').read_text()
assert 'data-nav="skills" aria-current="page"' in skill_page
assert 'No skills available yet' in skill_page and 'download=' not in skill_page
assert 'Try the starter prompt' in skill_page
assert '<a href="/prompts/">Prompts</a>' not in (root/'resources/task-context-starter-prompt/index.html').read_text()
for key,target in {'prompts':'/resources/task-context-starter-prompt/','instructions':'/skills/','resources':'/skills/','projects':'/','guides':'/skills/'}.items():
 page=(root/f'{key}/index.html').read_text()
 assert f'data-redirect="{target}"' in page,(key,'legacy destination')
for route in ['index.html','skills/index.html','about/index.html','resources/task-context-starter-prompt/index.html']:
 page=(root/route).read_text()
 assert 'href="/prompts/"' not in page and 'href="/instructions/"' not in page,(route,'retired collection still linked')

for item in items:
 page=(root/f"resources/{item['id']}/index.html").read_text()
 assert 'Purpose</h2>' in page and 'Expected outcomes</h2>' in page and 'What you need</h2>' in page and 'How to use it</h2>' in page
 assert item['expectedOutcomes'] and item['requirements'] and item['instructions']

channels=json.loads((root/'data/site.json').read_text())['channels']
for channel in channels:
 for route in ['index.html','about/index.html','skills/index.html','resources/task-context-starter-prompt/index.html']:
  assert f'href="{channel["url"]}"' in (root/route).read_text(),(route,channel['id'],'missing confirmed channel link')
assert 'Coming soon' not in (root/'index.html').read_text(),'Confirmed profiles replace the channel placeholders'

assert skill_page.index('class="skills-collection') < skill_page.index('class="collection-how"'),'Availability must precede optional usage guidance'
assert 'href="#prompt-title"' in (root/'resources/task-context-starter-prompt/index.html').read_text(),'Prompt text needs direct access from its introduction'

walk_qa=json.loads((root/'assets/characters/walk-registration.json').read_text())
assert walk_qa['sha256']==hashlib.sha256((root/'assets/characters/walk.webm').read_bytes()).hexdigest(),'Walk registration receipt must match deployed media'
assert len(walk_qa['encoded_paw_baselines'])==30 and set(walk_qa['encoded_paw_baselines'])=={walk_qa['baseline']},'All decoded gait frames must share one ground line'
assert walk_qa['loop_join_baseline_delta']==0 and walk_qa['visible_pixels_cropped'] is False,'Walk restart must preserve ground contact without cropping artwork'

# Every maintained animation must have the verified Safari delivery derivative.
usage=json.loads((root/'assets/characters/usage.json').read_text())
for action,meta in usage['assets'].items():
 file=root/'assets/characters'/f'{action}.mov'
 assert file.is_file() and hashlib.sha256(file.read_bytes()).hexdigest()==meta['safari_sha256'],(action,'Safari derivative missing or changed without review')
print('Safari derivatives match the maintained asset hashes.')
