"""Website loop assembled from approved entry, continuation and opaque dip. No art changes."""
from pathlib import Path
import subprocess,sys,shutil
root=Path(__file__).resolve().parent.parent
library=Path.home()/'Library/Mobile Documents/com~apple~CloudDocs/Chris-Decodes-Media/characters'
ffmpeg=sys.argv[1]
out=root/'assets/characters/peek.webm'
encoder=subprocess.Popen([ffmpeg,'-v','error','-y','-f','rawvideo','-pixel_format','rgba','-video_size','512x512','-framerate','30','-i','pipe:0','-c:v','libvpx-vp9','-pix_fmt','yuva420p','-b:v','0','-crf','32','-auto-alt-ref','0','-an',str(out)],stdin=subprocess.PIPE)
for name,count in [('Decoder Cat Peek Rise and Blink 2026-11-16/transparent.mov',49),('Decoder Cat On-Screen Loops 2026-11-16/peek/loop.mov',147),('Decoder Cat On-Screen Loops 2026-11-16/peek/loop.mov',147),('Decoder Cat Peek Dip Exit 2026-11-19/transparent.mov',28)]:
 decoder=subprocess.Popen([ffmpeg,'-v','error','-i',str(library/name),'-frames:v',str(count),'-f','rawvideo','-pix_fmt','rgba','pipe:1'],stdout=subprocess.PIPE)
 shutil.copyfileobj(decoder.stdout,encoder.stdin)
 assert decoder.wait()==0
encoder.stdin.write(bytes(512*512*4)*19)
encoder.stdin.close();assert encoder.wait()==0
shutil.copyfile(library/'Decoder Cat Peek Rise and Blink 2026-11-16/settled-hold.png',root/'assets/characters/peek.png')
print('Prepared 390-frame, 13-second peek: rise, two approved continuations, opaque dip, brief hidden interval.')
