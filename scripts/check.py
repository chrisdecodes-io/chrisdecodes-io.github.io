"""Check generated pages, local destinations, downloads and release scope."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,hashlib
root=Path(__file__).resolve().parent.parent
class Page(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.refs=[];self.h1=0;self.videos=[];self.images=[];self.heading=False;self.heading_text=[];self.text=[];self.ignore_text=False;self.tile_count=0;self.home_tiles=[];self.nav_items=[];self.in_sidebar=False
 def handle_starttag(self,t,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if t in ['script','style']:self.ignore_text=True
  if 'home-tile' in a.get('class','').split():self.tile_count+=1;self.home_tiles.append(a)
  if t=='nav' and a.get('id')=='sidebar-links':self.in_sidebar=True
  if t=='a' and self.in_sidebar and 'data-nav' in a:self.nav_items.append(a.get('data-nav'))
  if t=='h1':self.h1+=1
  if t in ['h1','h2','h3']:self.heading=True
  if t=='video':self.videos.append(a)
  if t=='img':self.images.append(a)
  for k in ['src','href','poster']:
   if k in a:self.refs.append(a[k])
 def handle_endtag(self,t):
  if t in ['script','style']:self.ignore_text=False
  if t=='nav':self.in_sidebar=False
  if t in ['h1','h2','h3']:self.heading=False
 def handle_data(self,s):
  if not self.ignore_text:self.text.append(s)
  if self.heading:self.heading_text.append(s)
pages={}
for p in root.rglob('*.html'):
 if '.git' in p.parts:continue
 q=Page();q.feed(p.read_text());pages[p]=q
 assert q.h1==1,(p,'one h1 required')
 if p not in [root/f'{name}/index.html' for name in ['guides','resources','projects']]:
  assert q.nav_items==['home','skills','about'],(p,'unexpected sidebar entries')
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
assert home.tile_count==5,'Home must highlight Skills, Instagram, Substack, GitHub and About Chris'
assert sum('href' not in tile for tile in home.home_tiles)==2,'Instagram and Substack remain visible placeholders'
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
assert all(asset['frames']==390 and asset['seconds']==13 if name=='peek' else asset['frames']==360 and asset['seconds']==12 for name,asset in usage['assets'].items()),'Use original full gestures or the recorded complete 13-second peek composition'
print('Release scope: one public prompt, approved character animations; no private resource imports.')
