#!/usr/bin/env python3
"""Prepare local-only timestamp windows from a private VTC transcript archive.

Never publishes transcript text. The generated files belong to .local-transcripts,
which is gitignored; the source path is passed explicitly by the reader.
"""
import argparse,json,re
from pathlib import Path

WINDOWS={
 '1g0N37EyyvE':[(34*60+43,42*60+43,'AI bubble: host question and guest answer')],
 'iWi9od6vrj4':[(4*60+1,6*60+20,'China EV/AI: host question and guest answer')],
 'fmhyJWJSQGc':[(4*60+15,6*60+10,'US chip design: host question and guest answer')],
 'h6-2nFJbfgg':[(64*60+31,66*60+20,'Chaebol suppliers: host question and guest answer')],
 'JEuBT14Uv3k':[(33*60+26,35*60+35,'Oil: guest explanation, host follow-up and answer')],
}
def seconds(t):
 a=[int(x) for x in t.strip().split(':')];return sum(n*60**i for i,n in enumerate(reversed(a)))
def lines(data):
 if 'rows' in data:
  for row in data['rows']:
   yield seconds(row['time']),row['time']+' '+row['text'].replace('\n',' ').strip()
 else:
  for line in data['timestamped_text'].splitlines():
   m=re.match(r'^(\d+:\d+(?::\d+)?) ',line)
   if m:yield seconds(m.group(1)),line

def main():
 a=argparse.ArgumentParser();a.add_argument('--source',type=Path,required=True,help='private .raw/vtc-bui-ngoc-son directory');args=a.parse_args()
 plugin=Path(__file__).resolve().parents[1];dest=plugin/'knowledge/.local-transcripts/excerpts';dest.mkdir(parents=True,exist_ok=True)
 files=[]
 for vid,windows in WINDOWS.items():
  found=list(args.source.glob(vid+'*.json'))
  if len(found)!=1:raise SystemExit(f'{vid}: expected one transcript, got {len(found)}')
  data=json.loads(found[0].read_text());assert data.get('video_id')==vid
  rows=list(lines(data))
  for start,end,label in windows:
   selected=[line for t,line in rows if start<=t<=end]
   if not selected:raise SystemExit(f'{vid}: no captions in {start}-{end}')
   out=dest/(vid+'.md')
   out.write_text('# '+label+'\n\nPRIVATE local evidence — automatic captions; host and guest turns coexist. Not an exact quote or independent fact check.\n\n'+'\n'.join(selected)+'\n',encoding='utf-8')
   files.append(out)
 print('prepared',len(files),'private excerpt windows from',len(WINDOWS),'full transcripts; output',dest)
if __name__=='__main__':main()
