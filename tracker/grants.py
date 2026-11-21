"""Reconcile mutually exclusive volunteer reservations from trusted main-branch code."""
import json,os,re,sys,urllib.request
from claim_comments import COMMENT_FEED, comments_by_issue
from tasks import load
from github_rate_limit import rate_limit_delay, retry_rate_limited
from collections import defaultdict
from pathlib import Path
PAUSED=Path(__file__).with_name('paused-claimants.txt')
def load_paused(path=None):
 """GitHub logins whose new claims receive no grant; '#' starts a comment."""
 path=path or PAUSED
 if not path.is_file():return set()
 return {line.split('#',1)[0].strip().lower() for line in path.read_text().splitlines()}-{''}
def api(route,method='GET',body=None):
 base='https://api.github.com/repos/'+os.environ['GITHUB_REPOSITORY']
 request=urllib.request.Request(base+route,method=method,headers={'Authorization':'Bearer '+os.environ['GITHUB_TOKEN'],'Accept':'application/vnd.github+json','User-Agent':'replay-claims'},data=None if body is None else json.dumps(body).encode())
 with urllib.request.urlopen(request,timeout=30) as response:return json.loads(response.read() or 'null')
def pages(route):
    page = 1
    while True:
        batch = api(f'{route}&page={page}')
        yield from batch
        if len(batch) < 100:
            return
        page += 1


def prior_decisions(issues, get_pages=None):
    get_pages = get_pages or pages
    labels = {i['number']: {label['name'] for label in i['labels']} for i in issues}
    decided = [i for i in issues if labels[i['number']] & {'claim-granted', 'claim-conflict'}]
    histories = comments_by_issue(decided, get_pages('/' + COMMENT_FEED))
    prior = {}
    conflicts = set()
    for number, comments in histories.items():
        for comment in sorted(comments, key=lambda c: c['id']):
            if comment['user']['login'] != 'github-actions[bot]':
                continue
            grant = re.match(r'Granted `(P\d{4}|M\d{6})`\.', comment['body'])
            if grant:
                if 'claim-granted' in labels[number]:
                    prior[number] = grant[1]
                conflicts.discard(number)
            elif comment['body'].startswith('No grant.'):
                conflicts.add(number)
    return prior, conflicts


def reconcile(get_pages=None, mutate=None):
 get_pages = get_pages or pages
 mutate = mutate or api
 rows=load();groups=defaultdict(set);reserved=set();completed=set()
 for r in rows:
  groups[r['id']].add(r['id']);groups[r['packet']].add(r['id'])
  if r['state']!='open':reserved.add(r['id'])
  if r['state'] not in ('open','assigned'):completed.add(r['id'])
 issues=[i for i in get_pages('/issues?state=open&per_page=100') if 'pull_request' not in i]
 paused=load_paused();planned=[];taken=set()
 # Preserve valid grants first, then use issue number as a deterministic tie-breaker.
 prior,conflicts=prior_decisions(issues,get_pages)
 for i in sorted(issues,key=lambda z:(prior.get(z['number'])!=z['title'].removeprefix('Claim '),z['number'])):
  labels={l['name'] for l in i['labels']};m=re.fullmatch(r'Claim (P\d{4}|M\d{6})',i['title'])
  if not m and not labels.intersection({'claim-granted','claim-conflict','claim'}):continue
  target=m[1] if m else '';mods=groups.get(target,set())
  existing_grant=prior.get(i['number'])==target
  # A paused claimant keeps existing grants so earlier submissions can be fixed,
  # but receives no new grants.
  held=not existing_grant and ((i.get('user') or {}).get('login') or '').lower() in paused
  # Completed work can never be granted later, unlike an overlap that may free up.
  finished=bool(mods) and not existing_grant and mods<=completed
  # New build evidence should not revoke work already granted to a volunteer.
  win=bool(mods) and not held and not mods.intersection(taken) and (existing_grant or not mods.intersection(reserved))
  if win:taken.update(mods)
  desired='claim-granted' if win else 'claim-conflict'
  planned.append((i['number'],labels,target,desired,held or finished))
 for number,labels,target,desired,held in planned:
  other='claim-conflict' if desired=='claim-granted' else 'claim-granted'
  if other in labels:mutate(f'/issues/{number}/labels/{other}','DELETE')
 for number,labels,target,desired,held in planned:
  if desired not in labels or 'claim' not in labels:mutate(f'/issues/{number}/labels','POST',{'labels':['claim',desired]})
  if desired=='claim-granted' and (desired not in labels or prior.get(number)!=target):
   mutate(f'/issues/{number}/comments','POST',{'body':f'Granted `{target}`. Begin this reservation. Attach your receipt and log to this issue, or close it to release the work.'})
  elif desired=='claim-conflict' and (desired not in labels or number not in conflicts):
   paused_owner=((next(z for z in issues if z['number']==number).get('user') or {}).get('login') or '').lower() in paused
   body=('No grant. New claims from this account are paused until the pending submissions on your granted claims are fixed. '
         'See the review comments there and the submission self-check in CONTRIBUTING.md. This issue is closed.') if held and paused_owner else \
        ('No grant. This work is already completed. This issue is closed. Run `git pull` before `python3 tracker/tasks.py next` '
         'so your queue skips completed modules.') if held else \
        'No grant. This selection is unavailable or overlaps existing work. Close this issue and choose a new open module or packet with `python3 tracker/tasks.py next`.'
   mutate(f'/issues/{number}/comments','POST',{'body':body})
  # Close refused claims from paused accounts so they don't grow the open set every run reads.
  if held and desired=='claim-conflict':
   mutate(f'/issues/{number}','PATCH',{'state':'closed','state_reason':'not_planned'})


def main():
    if '--graphql' in sys.argv:
        import claims_graphql
        return claims_graphql.reconcile(reconcile)
    return retry_rate_limited(reconcile, 'Rechecking all claims')


if __name__=='__main__':main()
