"""Crop only transparent margins around the approved stacked CTA wordmark."""
from pathlib import Path
import hashlib,json,re,xml.etree.ElementTree as ET
root=Path(__file__).resolve().parent.parent
source=root/'assets/wordmark-ink.svg'
assert hashlib.sha256(source.read_bytes()).hexdigest()=='3f2a193b097bed6b7a78fc71e0562bd47ea8a8b2310c01cfe9a9edfd4e89a391'
ET.register_namespace('','http://www.w3.org/2000/svg')
tree=ET.parse(source);svg=tree.getroot();boxes=[]
for node in svg.iter():
 if node.tag.endswith('path'):
  d=node.attrib['d'];assert set(re.findall('[A-Za-z]',d))<=set('MQZ')
  v=[float(n) for n in re.findall(r'-?\d+(?:\.\d+)?',d)]
  boxes.append((min(v[::2]),min(v[1::2]),max(v[::2]),max(v[1::2])))
x,y=min(v[0] for v in boxes),min(v[1] for v in boxes)
w,h=max(v[2] for v in boxes)-x,max(v[3] for v in boxes)-y
svg.set('viewBox',f'{x:.4f} {y:.4f} {w:.4f} {h:.4f}')
svg.set('width',f'{w:.4f}');svg.set('height',f'{h:.4f}')
out=root/'assets/wordmark-cta-ink.svg';tree.write(out,encoding='unicode')
receipt={'state':'Restored approved stacked CTA wordmark; supersedes horizontal website derivative','source':'assets/wordmark-ink.svg; approved smooth-v1 artwork','method':'Crop transparent viewBox margins only; all original paths and word arrangement unchanged','viewBox':[x,y,w,h],'lockup_proportions':{'square':176,'gap':49.3,'wordmark':516,'total':741.3},'proportion_source':'Adopted refined logo lockup v2, October 16, 2026','output_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'role':'Header and footer CTA-style lockup','rebuild':'python3 scripts/prepare-cta-wordmark.py'}
(root/'assets/wordmark-cta-usage.json').write_text(json.dumps(receipt,indent=2)+'\n')
print('CTA wordmark restored without altering any letter outlines or their arrangement.')
