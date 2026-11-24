"""Website-only paw-baseline registration of the approved walk. No redrawing or retiming."""
from pathlib import Path
import hashlib,json,subprocess,sys
root=Path(__file__).resolve().parent.parent
ffmpeg=sys.argv[1]
source=Path(sys.argv[2]) if len(sys.argv)>2 else Path.home()/'Library/Mobile Documents/com~apple~CloudDocs/Chris-Decodes-Media/characters/Decoder Cat Flow Neon Walk 2026-10-20/Loop asset v1/loop-transparent.webm'
source_hash=hashlib.sha256(source.read_bytes()).hexdigest()
assert source_hash=='0e60369b88139db064f3afd565a59db9bd37712421360edda578d8802e4ac217','Unexpected source; preserve the approved walk'
w=h=720;stride=w*4;frame_bytes=stride*h;target=620
raw=subprocess.check_output([ffmpeg,'-v','error','-c:v','libvpx-vp9','-i',str(source),'-f','rawvideo','-pix_fmt','rgba','pipe:1'])
assert len(raw)==frame_bytes*30
frames=[];offsets=[];before=[]
def floor(frame):
 alpha=frame[3::4]
 return max(y for y in range(h) if any(a>=128 for a in alpha[y*w:(y+1)*w]))
for i in range(30):
 frame=raw[i*frame_bytes:(i+1)*frame_bytes];base=floor(frame);dy=target-base;before.append(base);offsets.append(dy)
 if dy>0:
  assert not any(frame[-dy*stride+3::4]);fixed=bytes(dy*stride)+frame[:-dy*stride]
 elif dy<0:
  assert not any(frame[:(-dy)*stride][3::4]);fixed=frame[-dy*stride:]+bytes(-dy*stride)
 else:fixed=frame
 assert floor(fixed)==target
 frames.append(fixed)
normalized=b''.join(frames)
out=root/'assets/characters/walk.webm'
subprocess.run([ffmpeg,'-v','error','-y','-f','rawvideo','-pixel_format','rgba','-video_size','720x720','-framerate','30','-i','pipe:0','-frames:v','30','-c:v','libvpx-vp9','-lossless','1','-pix_fmt','yuva420p','-auto-alt-ref','0','-an',str(out)],input=normalized,check=True)
subprocess.run([ffmpeg,'-v','error','-y','-f','rawvideo','-pixel_format','rgba','-video_size','720x720','-i','pipe:0','-frames:v','1',str(root/'assets/characters/walk.png')],input=frames[0],check=True)
# Verify the actual encoded alpha, not only the frames supplied to the encoder.
decoded=subprocess.check_output([ffmpeg,'-v','error','-c:v','libvpx-vp9','-i',str(out),'-f','rawvideo','-pix_fmt','rgba','pipe:1'])
assert len(decoded)==frame_bytes*30
after=[floor(decoded[i*frame_bytes:(i+1)*frame_bytes]) for i in range(30)]
assert after==[target]*30
qa={'scope':'Website-only derivative; shared approved source unchanged','source_sha256':source_hash,'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'size':[w,h],'frames':30,'fps':30,'seconds':1,'registration':'Integer vertical translation only; no scaling, warping, redrawing, interpolation or timing changes','alpha_threshold':128,'baseline':target,'source_paw_baselines':before,'vertical_offsets':offsets,'encoded_paw_baselines':after,'visible_pixels_cropped':False,'loop_join_baseline_delta':after[-1]-after[0]}
(root/'assets/characters/walk-registration.json').write_text(json.dumps(qa,indent=2)+'\n')
print('30 decoded frames verified: fixed paw baseline, preserved duration and zero baseline jump at restart.')
