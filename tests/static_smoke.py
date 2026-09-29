from pathlib import Path
from bs4 import BeautifulSoup
import re, json, subprocess, sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]; notes=[]
required=['index.html','assets/app.css','assets/app.js','assets/icon.svg','manifest.webmanifest','sw.js','README.md','LICENSE','docs/ARCHITECTURE.md','docs/CHAT_COMPENDIUM.md','data/safeguarding_seed.json']
for rel in required:
    if not (ROOT/rel).exists(): errors.append(f'missing {rel}')
html=(ROOT/'index.html').read_text(encoding='utf-8')
js=(ROOT/'assets/app.js').read_text(encoding='utf-8')
sw=(ROOT/'sw.js').read_text(encoding='utf-8')
soup=BeautifulSoup(html,'html.parser')
ids=[x.get('id') for x in soup.find_all(attrs={'id':True})]
dups=sorted({x for x in ids if ids.count(x)>1})
if dups: errors.append('duplicate IDs: '+', '.join(dups))
sections={x.get('data-route') for x in soup.select('section.route')}
# route IDs from the explicit ROUTES registry at start of JS
route_block=re.search(r'const ROUTES=\[(.*?)\];\n\nconst SYSTEMS=',js,re.S)
route_ids=set(re.findall(r"\{id:'([^']+)'",route_block.group(1) if route_block else ''))
if route_ids != sections:
    errors.append(f'route/section mismatch routes={sorted(route_ids-sections)} sections={sorted(sections-route_ids)}')
# literal ID selectors used as $('#id') must exist in static HTML
literal_ids=set(re.findall(r"\$\('#([A-Za-z0-9_-]+)'\)",js))
missing=sorted(literal_ids-set(ids))
if missing: errors.append('JS references missing static IDs: '+', '.join(missing))
# manifest paths
manifest=json.loads((ROOT/'manifest.webmanifest').read_text())
for icon in manifest.get('icons',[]):
    rel=icon['src'].replace('./','')
    if not (ROOT/rel).exists(): errors.append(f'manifest icon missing: {rel}')
# service worker shell paths
shell=re.search(r'const SHELL=\[(.*?)\];',sw,re.S)
if shell:
    for rel in re.findall(r"'([^']+)'",shell.group(1)):
        if rel in ('./',): continue
        p=ROOT/rel.replace('./','')
        if not p.exists(): errors.append(f'service worker cached path missing: {rel}')
# content counts / required concepts
if len(soup.select('section.route')) < 20: errors.append('expected at least 20 routes')
if js.count("name:'") < 10: errors.append('system content count appears too low')
for title in ['The Generation That Broke the Chain','The City Where Harm Became Inconvenient','The Children Who Redesigned Civilization']:
    if title not in js: errors.append(f'missing story: {title}')
for title in ['Harm Friction OS','Early Signal Commons','Protective Ecosystem Command Center']:
    if title not in js: errors.append(f'missing system: {title}')
# Node syntax checks
for rel in ['assets/app.js','sw.js']:
    r=subprocess.run(['node','--check',str(ROOT/rel)],capture_output=True,text=True)
    if r.returncode: errors.append(f'node syntax failure {rel}: {r.stderr.strip()}')
notes.append(f'{len(ids)} unique static IDs')
notes.append(f'{len(sections)} route sections')
notes.append(f'{len(route_ids)} route-registry entries')
print('STATIC SMOKE:', 'PASS' if not errors else 'FAIL')
for n in notes: print(' -',n)
for e in errors: print(' ERROR:',e)
sys.exit(1 if errors else 0)
