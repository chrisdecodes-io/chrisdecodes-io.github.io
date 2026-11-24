"""Derive a horizontal web lockup from the approved unmodified wordmark paths."""
from pathlib import Path
import hashlib,json,re,statistics,xml.etree.ElementTree as ET
root=Path(__file__).resolve().parent.parent
source=root/'assets/wordmark-ink.svg'
expected='3f2a193b097bed6b7a78fc71e0562bd47ea8a8b2310c01cfe9a9edfd4e89a391'
assert hashlib.sha256(source.read_bytes()).hexdigest()==expected,'Review changed source artwork before rebuilding'
paths=[p.attrib['d'] for p in ET.parse(source).getroot().iter() if p.tag.endswith('path')]
assert len(paths)==12
# The approved artwork consists only of absolute M/Q commands and closed contours.
# Include quadratic controls in bounds, giving a conservative, uncropped frame.
def bounds(d):
 assert set(re.findall('[A-Za-z]',d))<=set('MQZ')
 values=[float(n) for n in re.findall(r'-?\d+(?:\.\d+)?',d)]
 return min(values[::2]),min(values[1::2]),max(values[::2]),max(values[1::2])
def word_bounds(group):
 b=[bounds(d) for d in group]
 return min(v[0] for v in b),min(v[1] for v in b),max(v[2] for v in b),max(v[3] for v in b)
first,second=paths[:5],paths[5:]
a,b=word_bounds(first),word_bounds(second)
baseline_a=statistics.median(bounds(d)[3] for d in first)
baseline_b=statistics.median(bounds(d)[3] for d in second)
pad=(a[3]-a[1])*.025
gap=(a[3]-a[1])*.35
first_x=pad-a[0];first_y=pad-a[1]
second_x=pad+(a[2]-a[0])+gap-b[0]
second_y=first_y+baseline_a-baseline_b
width=second_x+b[2]+pad
height=max(first_y+a[3],second_y+b[3])+pad
def group(ds,x,y):return f'<g transform="translate({x:.4f} {y:.4f})">'+''.join(f'<path d="{d}"/>' for d in ds)+'</g>'
svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width:.4f} {height:.4f}" width="{width:.4f}" height="{height:.4f}"><g fill="#171717" fill-rule="evenodd">'+group(first,first_x,first_y)+group(second,second_x,second_y)+'</g></svg>\n'
out=root/'assets/wordmark-horizontal-ink.svg';out.write_text(svg)
receipt={'state':'Website-specific horizontal derivative requested by Christopher','source':'assets/wordmark-ink.svg; approved wordmark-smooth-v1 outlines','source_sha256':expected,'output_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'role':'Unboxed centered header and centered footer signature','method':'First five and final seven original paths translated into one row; align median letter baselines; no path edits, retyping, scaling or stretching','word_gap':round(gap,4),'viewBox':[0,0,round(width,4),round(height,4)],'path_count':len(paths),'rebuild':'python3 scripts/prepare-wordmark.py'}
(root/'assets/wordmark-horizontal-usage.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(f'Created horizontal lockup: {width:.2f} × {height:.2f}; 12 original paths preserved.')
