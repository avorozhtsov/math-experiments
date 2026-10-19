"""Validate the checked-in bilingual video archive without external services."""
from pathlib import Path
import json,re,struct
ROOT=Path(__file__).resolve().parents[1]
def jpeg_size(path):
 data=path.read_bytes();assert data[:2]==b'\xff\xd8';i=2
 while i<len(data):
  if data[i]!=255:i+=1;continue
  while data[i]==255:i+=1
  marker=data[i];i+=1
  if marker in (0xd8,0xd9) or 0xd0<=marker<=0xd7:continue
  size=int.from_bytes(data[i:i+2],'big')
  if marker in (0xc0,0xc1,0xc2):h,w=struct.unpack('>HH',data[i+3:i+7]);return w,h
  i+=size
 raise AssertionError('No JPEG size: '+str(path))
catalog=json.loads((ROOT/'catalog.json').read_text());videos=catalog['videos'];assert len(videos)==20
assert len({x['video_id'] for x in videos})==20
for video in videos:
 folder=ROOT/video['directory'];assert json.loads((folder/'video.json').read_text())==video
 assert video['youtube_url']=='https://www.youtube.com/watch?v='+video['video_id']
 tags=json.loads((folder/'tags.json').read_text());assert isinstance(tags['tags'],list)
 for lang in ('ru','en'):
  loc=video['locales'][lang];meta=json.loads((folder/loc['metadata_file']).read_text());old=json.loads((folder/f'metadata.{lang}.source.json').read_text())
  assert meta['title']==old['title']==(folder/loc['title_file']).read_text().strip()==loc['title']
  assert meta['description'].startswith(old['description'].rstrip()) and len(meta['description'])<=5000
  assert meta['description']==(folder/loc['description_file']).read_text().rstrip('\n')
  assert ('https://github.com/avorozhtsov/math-experiments/tree/main/'+video['directory']) in meta['description']
  assert (folder/loc['captions_file']).read_text().startswith('WEBVTT')
  assert loc['thumbnail_file'] and (folder/loc['thumbnail_file']).exists()
  if lang=='en':assert jpeg_size(folder/loc['thumbnail_file'])==(1280,720) and (folder/loc['thumbnail_file']).stat().st_size<2000000
 for nb in video['notebooks']:assert (ROOT/nb['path']).exists() and b'Notebook[' in (ROOT/nb['path']).read_bytes()[:10000]
 assert video['exact_notebook_source_found']==any(n['relationship']=='primary' for n in video['notebooks'])
 for source in video['thumbnail_editable_sources']:assert (ROOT/source['path']).is_file()
for file in ROOT.rglob('*.md'):
 if '.git' in file.parts:continue
 for link in re.findall(r'\]\(([^)]+)\)',file.read_text()):
  if link.startswith(('http://','https://','#')):continue
  assert (file.parent/link.split('#')[0]).exists(),(str(file),link)
print('PASS: 20 unique videos, RU/EN metadata, 40 subtitle tracks, 40 thumbnails, notebook references and all relative Markdown links.')
