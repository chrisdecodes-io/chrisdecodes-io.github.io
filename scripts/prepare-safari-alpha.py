"""Encode current website VP9-alpha assets for Safari. macOS + Swift + ffmpeg required."""
import argparse, pathlib, subprocess, tempfile
parser=argparse.ArgumentParser()
parser.add_argument('--ffmpeg',required=True)
args=parser.parse_args()
root=pathlib.Path(__file__).resolve().parent.parent
with tempfile.TemporaryDirectory(prefix='cd-alpha-') as temp:
 encoder=pathlib.Path(temp)/'encode'
 subprocess.run(['swiftc','-O',str(root/'scripts/encode-safari-alpha.swift'),'-o',str(encoder)],check=True)
 for action in ['curious','work','presenting','rest','peek','walk']:
  source=root/'assets/characters'/f'{action}.webm'
  size='720' if action=='walk' else '512'
  decoder=subprocess.Popen([args.ffmpeg,'-hide_banner','-c:v','libvpx-vp9','-i',str(source),'-f','rawvideo','-pix_fmt','bgra','-'],stdout=subprocess.PIPE)
  result=subprocess.run([str(encoder),size,size,str(source.with_suffix('.mov'))],stdin=decoder.stdout)
  decoder.stdout.close()
  assert result.returncode==0 and decoder.wait()==0,action
