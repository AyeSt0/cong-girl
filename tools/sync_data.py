from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
data=root/'site/data'
assets=json.loads((data/'assets.json').read_text(encoding='utf-8'))
prompts={p.stem:p.read_text(encoding='utf-8').strip() for p in (root/'characters/cong/prompts').glob('*.txt')}
for key,obj in [('assets',assets),('prompts',prompts)]:
    (data/f'{key}.js').write_text(f'window.CONG_{key.upper()} = '+json.dumps(obj,ensure_ascii=False,indent=2)+';\n',encoding='utf-8')
