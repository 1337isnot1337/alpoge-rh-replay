#!/usr/bin/env python3
"""Look up module-sized replay tasks, reserve work and produce receipts."""
from collections import Counter
from pathlib import Path
import argparse,datetime,gzip,hashlib,json,os,re,subprocess,sys,tarfile,urllib.request
base=Path(__file__).resolve().parent
repo='rohanarun/alpoge-rh-replay'
def digest(path):
 h=hashlib.sha256()
 with path.open('rb') as f:
  for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
 return h.hexdigest()
def load():
 with gzip.open(base/'modules.jsonl.gz','rt') as f:rows=[json.loads(s) for s in f]
 completed=base/'completed.tsv'
 if completed.exists():
  import csv
  with completed.open() as f:done={r['id']:r['evidence'] for r in csv.DictReader(f,delimiter='\t')}
  for r in rows:
   if r['id'] in done:r['state']=done[r['id']]
 return rows
def select(rows,target):
 out=[r for r in rows if target in (r['id'],r['packet'],r['module'])]
 if not out:raise SystemExit('Unknown task or packet: '+target)
 return out
def cold_modules(rows, busy):
    """Rank available tasks with no project imports by their available direct consumers."""
    available = [r for r in rows if r['state'] == 'open'
                 and r['id'] not in busy and r['packet'] not in busy]
    leaves = {r['id']: r for r in available if not r['imports']}
    sole = Counter()
    direct = Counter()
    for row in available:
        imports = set(row['imports'])
        for dep in imports:
            if dep in leaves:
                direct[dep] += 1
                if len(imports) == 1:
                    sole[dep] += 1
    ranked = sorted(leaves, key=lambda task: (-sole[task], -direct[task], task))
    return [(leaves[task], sole[task], direct[task]) for task in ranked]

def claims():
 url=f'https://api.github.com/repos/{repo}/issues?state=open&per_page=100'
 refs=set()
 while url:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'rh-replay-tracker'}),timeout=25) as response:
   for issue in json.load(response):
    if 'pull_request' not in issue:
     m=re.fullmatch(r'Claim (M\d{6}|P\d{4})',issue['title'])
     if m:refs.add(m[1])
   match=re.search(r'<([^>]+)>; rel="next"',response.headers.get('Link',''))
   url=match[1] if match else None
 return refs
def run(targets,checkout,out,bundle):
 project=checkout.resolve();output=out.resolve();output.mkdir(parents=True,exist_ok=False)
 dirs=project.parent
 env={**os.environ,'ELAN_HOME':str(dirs/'elan'),'XDG_CACHE_HOME':str(dirs/'cache')}
 toolchain = (project / 'lean-toolchain').read_text().strip()
 if toolchain != 'leanprover/lean4:v4.33.1':raise SystemExit('Wrong Lean toolchain')
 launcher = ['elan', 'run', toolchain]
 version=subprocess.check_output([*launcher, 'lean','--version'],env=env,cwd=project,text=True).strip()
 mathlib=subprocess.check_output(['git','-C',str(project/'.lake/packages/mathlib'),'rev-parse','HEAD'],text=True).strip()
 if '4.33.1' not in version or mathlib!=json.loads((base/'summary.json').read_text())['mathlib_commit']:raise SystemExit('Unexpected toolchain or mathlib')
 for r in targets:
  if digest(project/'src'/(r['module'].replace('.','/')+'.lean'))!=r['source_sha256']:raise SystemExit('Source hash mismatch: '+r['module'])
 cmd=['lake','build',*['+'+r['module']+':olean' for r in targets]]
 log=output/'build.log'
 with log.open('wb') as f:result=subprocess.run([*launcher, *cmd],cwd=project,env=env,stdout=f,stderr=subprocess.STDOUT)
 receipt={'tasks':[r['id'] for r in targets],'ended_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'toolchain':version,'mathlib':mathlib,'inputs_manifest_sha256':digest(base.parent/'parts.sha256'),'command':cmd,'exit_code':result.returncode,'log_sha256':digest(log),'objects':{}}
 build=project/'.lake/build'
 if result.returncode==0:
  for r in targets:receipt['objects'][r['id']]=digest(build/'lib/lean'/(r['module'].replace('.','/')+'.olean'))
  if bundle:
   artifact=output/'targets.tar.gz'
   with tarfile.open(artifact,'w:gz') as tar:
    for r in targets:
     stem=r['module'].replace('.','/')
     for prefix in ['lib/lean','ir']:
      path=build/prefix/stem
      for f in path.parent.glob(path.name+'.*'):
       if f.is_file() and not f.is_symlink():tar.add(f,arcname=str(f.relative_to(build)),recursive=False)
   receipt['bundle_sha256']=digest(artifact)
 (output/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
 print('Saved',output,'with exit status',result.returncode)
 return result.returncode
def main():
 p=argparse.ArgumentParser(description=__doc__);s=p.add_subparsers(dest='action',required=True)
 nx=s.add_parser('next');nx.add_argument('--limit',type=int,default=8)
 nx.add_argument('--cold',action='store_true',help='show available individual modules with no project imports')
 for n in ['show','claim','build']:
  sub=s.add_parser(n);sub.add_argument('target')
  if n=='build':
   sub.add_argument('checkout',type=Path);sub.add_argument('output',type=Path);sub.add_argument('--bundle',action='store_true')
 a=p.parse_args();rows=load()
 if a.action=='next':
  busy=claims()
  if a.cold:
   for row,sole,direct in cold_modules(rows,busy)[:max(0,a.limit)]:
    print(row['id'],row['packet'],row['module'],'sole-project-import consumers',sole,'direct consumers',direct)
   return 0
  used={r['packet'] for r in rows if r['id'] in busy or r['state']!='open'};shown=set()
  for r in rows:
   if r['packet'] in busy|used|shown:continue
   print(r['packet'],'depth',r['depth'],'begins with',r['module']);shown.add(r['packet'])
   if len(shown)>=a.limit:break
  return 0
 sel=select(rows,a.target)
 if a.action=='show':
  for r in sel:print(json.dumps(r,ensure_ascii=False))
 elif a.action=='claim':
  busy=claims()
  if any(r['id'] in busy or r['packet'] in busy or r['state']!='open' for r in sel):raise SystemExit('One or more modules are already claimed, observed, or assigned.')
  subprocess.run(['gh','issue','create','--repo',repo,'--title','Claim '+a.target,'--body','I am working on '+a.target+'. I will attach the input hashes, build transcript and receipt, or close this claim if I stop.'],check=True)
 else:return run(sel,a.checkout,a.output,a.bundle)
 return 0
if __name__=='__main__':sys.exit(main())
