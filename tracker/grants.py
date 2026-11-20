"""Reconcile mutually exclusive volunteer reservations from trusted main-branch code."""
import json,os,re,sys,urllib.request,urllib.error
from tasks import load
from collections import defaultdict
repo=os.environ['GITHUB_REPOSITORY']
base='https://api.github.com/repos/'+repo
def api(route,method='GET',body=None):
 request=urllib.request.Request(base+route,method=method,headers={'Authorization':'Bearer '+os.environ['GITHUB_TOKEN'],'Accept':'application/vnd.github+json','User-Agent':'replay-claims'},data=None if body is None else json.dumps(body).encode())
 with urllib.request.urlopen(request,timeout=30) as response:return json.loads(response.read() or 'null')
def main():
 rows=load();groups=defaultdict(set);reserved=set()
 for r in rows:
  groups[r['id']].add(r['id']);groups[r['packet']].add(r['id'])
  if r['state']!='open':reserved.add(r['id'])
 issues=[];page=1
 while True:
  batch=api(f'/issues?state=open&per_page=100&page={page}')
  issues.extend(i for i in batch if 'pull_request' not in i)
  if len(batch)<100:break
  page+=1
 planned=[];taken=set()
 # Preserve valid grants first, then use issue number as a deterministic tie-breaker.
 prior={}
 for i in issues:
  labels={l['name'] for l in i['labels']}
  if 'claim-granted' in labels:
   comments=api('/issues/'+str(i['number'])+'/comments?per_page=100')
   grants=[x['body'] for x in comments if x['user']['login']=='github-actions[bot]' and x['body'].startswith('Granted `')]
   if grants:prior[i['number']]=grants[-1].split('`')[1]
 for i in sorted(issues,key=lambda z:(prior.get(z['number'])!=z['title'].removeprefix('Claim '),z['number'])):
  labels={l['name'] for l in i['labels']};m=re.fullmatch(r'Claim (P\d{4}|M\d{6})',i['title'])
  if not m and not labels.intersection({'claim-granted','claim-conflict','claim'}):continue
  target=m[1] if m else '';mods=groups.get(target,set())
  existing_grant=prior.get(i['number'])==target
  # New build evidence should not revoke work already granted to a volunteer.
  win=bool(mods) and not mods.intersection(taken) and (existing_grant or not mods.intersection(reserved))
  if win:taken.update(mods)
  desired='claim-granted' if win else 'claim-conflict'
  planned.append((i['number'],labels,target,desired))
 for number,labels,target,desired in planned:
  other='claim-conflict' if desired=='claim-granted' else 'claim-granted'
  if other in labels:api(f'/issues/{number}/labels/{other}','DELETE')
 for number,labels,target,desired in planned:
  if desired not in labels or 'claim' not in labels:api(f'/issues/{number}/labels','POST',{'labels':['claim',desired]})
  if desired=='claim-granted' and (desired not in labels or prior.get(number)!=target):
   api(f'/issues/{number}/comments','POST',{'body':f'Granted `{target}`. Begin this reservation. Attach your receipt and log to this issue, or close it to release the work.'})
  elif desired=='claim-conflict' and desired not in labels:
   api(f'/issues/{number}/comments','POST',{'body':'No grant. This selection is unavailable or overlaps existing work. Close this issue and choose a new open module or packet with `python3 tracker/tasks.py next`.'})
if __name__=='__main__':main()
