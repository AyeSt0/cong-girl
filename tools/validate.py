from pathlib import Path
import json,re
root=Path(__file__).resolve().parents[1]; site=root/'site'; data=site/'data'
assets=json.loads((data/'assets.json').read_text(encoding='utf-8')); ids=set()
for a in assets:
    assert a['id'] not in ids, a['id'];ids.add(a['id'])
    assert (site/a['file']).is_file(), a['file']
    assert a['width']>0 and a['height']>0 and a['frames']>0
    assert (a['category']=='gif')==(a['frames']>1), a['file']
assert {'chibi','proportional'}<=ids
for k in ['assets','prompts']:
    raw=(data/f'{k}.js').read_text(encoding='utf-8'); obj=json.loads(raw.split('=',1)[1].strip().rstrip(';'))
    if k=='assets': assert obj==assets
    else:
        for p in (root/'characters/cong/prompts').glob('*.txt'): assert obj[p.stem]==p.read_text(encoding='utf-8').strip()
for attr,path in re.findall(r'(src|href)="([^"#]+)"',(site/'index.html').read_text(encoding='utf-8')):
    if not path.startswith(('https://','http://')): assert (site/path).is_file(),path
print(f'OK: {len(assets)} assets, data and local HTML links')
