#!/usr/bin/env python3
"""Build a deterministic schema-1 public profile archive; no credentials required."""
import argparse,gzip,hashlib,io,tarfile
from pathlib import Path

def build(root,destination):
 stream=io.BytesIO()
 with tarfile.open(fileobj=stream,mode='w') as tar:
  for p in sorted(root.rglob('*')):
   rel=p.relative_to(root)
   if any(s in ['.git','dist','.local','__pycache__'] for s in rel.parts):continue
   if p.is_symlink():raise ValueError('Profile bundles cannot contain symlinks')
   if not p.is_file():continue
   data=p.read_bytes();info=tarfile.TarInfo(rel.as_posix());info.size=len(data);info.mode=0o600;info.mtime=0;tar.addfile(info,io.BytesIO(data))
 with destination.open('wb') as target:
  with gzip.GzipFile(fileobj=target,mode='wb',mtime=0,filename='') as compressed:compressed.write(stream.getvalue())
 return hashlib.sha256(destination.read_bytes()).hexdigest()
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--version',required=True);p.add_argument('--output',type=Path,default=Path('dist'));a=p.parse_args();a.output.mkdir(parents=True,exist_ok=True);name=f'outfit-profiles_{a.version}.tar.gz';sha=build(Path(__file__).resolve().parents[1],a.output/name);(a.output/'SHA256SUMS').write_text(sha+'  '+name+'\n');print(sha,name)
