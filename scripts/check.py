"""Check generated pages, local destinations, downloads and release scope."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,hashlib
root=Path(__file__).resolve().parent.parent
class Page(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.refs=[];self.h1=0;self.videos=[];self.images=[];self.heading=False;self.heading_text=[]
 def handle_starttag(self,t,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if t=='h1':self.h1+=1
  if t in ['h1','h2','h3']:self.heading=True
  if t=='video':self.videos.append(a)
  if t=='img':self.images.append(a)
  for k in ['src','href','poster']:
   if k in a:self.refs.append(a[k])
 def handle_endtag(self,t):
  if t in ['h1','h2','h3']:self.heading=False
 def handle_data(self,s):
  if self.heading:self.heading_text.append(s)
pages={}
for p in root.rglob('*.html'):
 if '.git' in p.parts:continue
 q=Page();q.feed(p.read_text());pages[p]=q
 assert q.h1==1,(p,'one h1 required')
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
items=json.loads((root/'data/resources.json').read_text())
assert len(items)==1 and items[0]['id']=='task-context-starter-prompt','Initial release must contain only the existing approved prompt'
for item in items:
 assert (root/item['download'].lstrip('/')).read_text()==item['content']+'\n','Download differs from displayed prompt'
 assert (root/f"resources/{item['id']}/index.html").exists()
usage=json.loads((root/'assets/characters/usage.json').read_text())
for name,asset in usage['assets'].items():
 assert hashlib.sha256((root/f'assets/characters/{name}.webm').read_bytes()).hexdigest()==asset['sha256']
print(f'{len(pages)} pages checked: headings, links, assets, fragments, video attributes and prompt download match.')
print('Release scope: one public prompt, three character derivatives; no private resource imports.')
