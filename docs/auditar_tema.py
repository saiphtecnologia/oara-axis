"""Inventário estático do tema; não lê credenciais nem altera arquivos sincronizados."""
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / 'docs'
FOLDERS = ('blocks', 'config', 'layouts', 'sections', 'snippets', 'static', 'templates', 'translations')
files = sorted(p for folder in FOLDERS for p in (ROOT / folder).rglob('*') if p.is_file())
texts = {p.relative_to(ROOT).as_posix(): p.read_text(encoding='utf-8-sig') for p in files if p.suffix in ('.tpl', '.json', '.js', '.css', '.txt')}
schemas = {}
errors = []
warnings = []
json_count = 0
try:
    json.loads((ROOT / 'manifest.json').read_text(encoding='utf-8-sig'))
except (OSError, ValueError) as exc:
    errors.append(f'manifest.json: leitura/JSON inválido: {exc}')
    # O relatório soma um manifesto válido à contagem dos diretórios.
    json_count = -1
for path, text in texts.items():
    if path.endswith('.json'):
        try:
            json.loads(text)
            json_count += 1
        except ValueError as exc:
            errors.append(f'{path}: JSON inválido: {exc}')
    if path.startswith(('sections/', 'blocks/')):
        found = re.search(r'{%\s*schema\s*%}(.*?){%\s*endschema\s*%}', text, re.S)
        if not found:
            errors.append(f'{path}: schema ausente')
            continue
        try:
            schemas[path] = json.loads(found[1])
        except ValueError as exc:
            errors.append(f'{path}: schema inválido: {exc}')

global_schema = json.loads(texts['config/settings_schema.json'])
global_data = json.loads(texts['config/settings_data.json']).get('settings', {})
setting_rows = []
def settings_of(schema, scope, path):
    seen = set()
    for item in schema.get('settings', []):
        if 'id' not in item:
            continue
        key = item['id']
        if key in seen:
            errors.append(f'{path} / {scope}: setting duplicado {key}')
        seen.add(key)
        setting_rows.append({'path': path, 'scope': scope, **item})
    for block in schema.get('blocks', []):
        if isinstance(block, dict) and 'settings' in block:
            settings_of(block, scope + '/inline:' + str(block.get('type', '?')), path)
for panel in global_schema:
    settings_of(panel, 'global:' + panel.get('name', '?'), 'config/settings_schema.json')
for path, schema in schemas.items():
    settings_of(schema, path.removesuffix('.tpl'), path)

templates = []
instances = []
def walk_blocks(blocks, order, location, parent_schema):
    if not isinstance(blocks, dict):
        return
    check_order(blocks, order, location)
    for key, node in blocks.items():
        typ = node.get('type', '?')
        path = f'blocks/{typ}.tpl'
        inline = next((x for x in parent_schema.get('blocks', []) if isinstance(x, dict) and x.get('type') == typ and 'settings' in x), None)
        schema = inline or schemas.get(path, {})
        if path not in schemas and inline is None:
            warnings.append(f'{location}/{key}: tipo de bloco sem arquivo ou schema inline identificado: {typ}')
        instances.append({'location': location + '/' + key, 'type': typ, 'kind': 'block', 'settings': list(node.get('settings', {}))})
        walk_blocks(node.get('blocks', {}), node.get('block_order', []), location + '/' + key, schema)
def check_order(nodes, order, location):
    if len(order) != len(set(order)):
        errors.append(f'{location}: ordem duplicada')
    for key in order:
        if key not in nodes:
            errors.append(f'{location}: ordem aponta para ID ausente: {key}')
    missing = sorted(set(nodes) - set(order))
    if missing:
        warnings.append(f'{location}: IDs fora da ordem: {", ".join(missing)}')
for path, text in texts.items():
    if not path.startswith('templates/') or not path.endswith('.json'):
        continue
    data = json.loads(text)
    sections = data.get('sections', {})
    order = data.get('order', [])
    check_order(sections, order, path)
    templates.append({'path': path, 'sections': [(key, sections[key].get('type'), sections[key].get('disabled', False)) for key in order if key in sections]})
    for key, node in sections.items():
        typ = node.get('type', '?')
        schema_path = f'sections/{typ}.tpl'
        if schema_path not in schemas:
            errors.append(f'{path}/{key}: seção sem arquivo: {typ}')
        instances.append({'location': path + '/' + key, 'type': typ, 'kind': 'section', 'settings': list(node.get('settings', {}))})
        walk_blocks(node.get('blocks', {}), node.get('block_order', []), path + '/' + key, schemas.get(schema_path, {}))

includes = []
dynamic = []
for path, text in texts.items():
    if not path.endswith('.tpl'):
        continue
    # Ignora comentários Twig; só identifica includes com destino literal completo.
    body = re.sub(r'{#.*?#}', '', text, flags=re.S)
    for match in re.finditer(r'{%\s*(?:include|extends|import|from)\s+([\s\S]*?)%}', body):
        expr = match[1].strip()
        literal = re.match(r"['\"]([^'\"]+)['\"](?:\s+(?:with|ignore|as)|$)", expr)
        if literal:
            target = literal[1]
            includes.append({'source': path, 'target': target})
            if not (ROOT / target).is_file():
                errors.append(f'{path}: include literal ausente: {target}')
        else:
            dynamic.append({'source': path, 'expression': expr})
breakpoints = sorted(set(re.findall(r'@media\s*([^{}]+)\{', '\n'.join(v for k,v in texts.items() if k.endswith('.css')))))
counts = Counter(p.relative_to(ROOT).parts[0] for p in files)
report = {'counts': dict(counts), 'total_theme_files': len(files) + 1, 'valid_json_files': json_count + 1, 'schemas': len(schemas), 'settings': len(setting_rows), 'global_settings': sum(x['scope'].startswith('global:') for x in setting_rows), 'global_saved_keys': len(global_data), 'section_instances': sum(x['kind']=='section' for x in instances), 'block_instances': sum(x['kind']=='block' for x in instances), 'literal_includes': len(includes), 'dynamic_includes': dynamic, 'errors': errors, 'warnings': warnings, 'breakpoints': breakpoints}

def cell(value):
    if value is None:
        return '—'
    text = json.dumps(value, ensure_ascii=False) if not isinstance(value, str) else value
    return text.replace('|', '&#124;').replace('\n', ' ').replace('\r', ' ')
def link(path):
    return f'[{path}](../{path})'
lines = ['# Inventário estático da instalação', '', 'Gerado por `python docs/auditar_tema.py`. Não lê `.nuvem`, não envia arquivos e não valida comportamento no navegador. Instalação 14601136; snapshot local descrito no manifesto.', '', '## Resultado', '', f'- Arquivos do tema, incluindo manifesto: {report["total_theme_files"]}.', f'- JSONs válidos, incluindo manifesto: {report["valid_json_files"]}; schemas Twig válidos: {len(schemas)}.', f'- Settings declarados, incluindo schemas inline: {len(setting_rows)}; globais: {report["global_settings"]}.', f'- Instâncias nos templates: {report["section_instances"]} seções e {report["block_instances"]} blocos.', f'- Includes literais: {len(includes)}; expressões dinâmicas: {len(dynamic)}.', '', 'Limites: esta análise verifica sintaxe JSON, existência de includes literais, tipos de seção, localização de blocos e referências das ordens. Não interpreta Twig, restrições completas de tags, permissões por página, intervalos/opções de todos os campos, traduções ou comportamento da plataforma.', '', '## Erros estruturais encontrados', '']
lines += [f'- {cell(x)}' for x in errors] or ['Nenhum erro encontrado nos critérios acima.']
lines += ['', '## Pontos para revisão', '']
lines += [f'- {cell(x)}' for x in warnings] or ['Nenhum aviso nos critérios acima.']
lines += ['', '## Arquivos por diretório', '', '| Diretório | Arquivos |', '| --- | ---: |']
lines += [f'| {x}/ | {counts[x]} |' for x in FOLDERS]
lines += ['', '## Sections e blocks: contratos por arquivo', '', '| Arquivo | Nome | Settings diretos | Blocos aceitos | Restrições/estrutura | Presets | Includes literais |', '| --- | --- | ---: | --- | --- | ---: | --- |']
for path, schema in schemas.items():
    restrictions = {k: schema[k] for k in ('enabled_on','limit','max_blocks','static','deletable','hideable','locked_blocks','wrapper','class','tags') if k in schema}
    blocks = [{k:v for k,v in x.items() if k in ('type','tags','limit','deletable')} for x in schema.get('blocks', []) if isinstance(x, dict)]
    refs = ', '.join(sorted(set(x['target'] for x in includes if x['source']==path)))
    lines.append(f'| {link(path)} | {cell(schema.get("name"))} | {sum("id" in x for x in schema.get("settings", []))} | {cell(blocks)} | {cell(restrictions)} | {len(schema.get("presets", []))} | {cell(refs)} |')
lines += ['', '## Composição salva dos templates', '', '| Template | Ordem: ID → tipo |', '| --- | --- |']
for item in templates:
    composition = '; '.join(f'{key} → {typ}' + (' (disabled)' if disabled else '') for key,typ,disabled in item['sections'])
    lines.append(f'| {link(item["path"])} | {cell(composition)} |')
lines += ['', '## Campos de configuração declarados', '', 'A tabela inclui defaults, heranças, condições e opções do schema. Valores livres salvos pelo lojista não são reproduzidos. Os consumidores dinâmicos e heranças exigem leitura contextual do renderer.', '', '| Arquivo/escopo | ID | Tipo | Default/herança | Opções/limites/condições | Referências diretas no código |', '| --- | --- | --- | --- | --- | --- |']
for row in setting_rows:
    prefix = 'settings' if row['scope'].startswith('global:') else ('block.settings' if row['scope'].startswith('blocks/') or '/inline:' in row['scope'] else 'section.settings')
    pattern = re.compile(r'(?<![\w.])' + re.escape(prefix + '.' + row['id']) + r'\b')
    candidates = texts if prefix=='settings' else {row['path']: texts[row['path']]}
    refs = []
    for path,text in candidates.items():
        # schemas podem conter visible_if; contam como referências no mesmo arquivo.
        nums = [str(i) for i,line in enumerate(text.splitlines(),1) if pattern.search(line)]
        if nums:
            refs.append(path + ':' + ','.join(nums))
    constraints = {k:row[k] for k in ('min','max','step','unit','options','visible_if','disabled_if','vertical_default') if k in row}
    default = {k:row[k] for k in ('default','default_setting') if k in row}
    lines.append(f'| {link(row["path"])} / {cell(row["scope"])} | `{row["id"]}` | {cell(row.get("setting_type",row.get("type")))} | {cell(default)} | {cell(constraints)} | {cell("; ".join(refs)) or "Não encontrada por busca direta; verificar include/contexto"} |')
lines += ['', '## Instâncias e chaves persistidas', '', '| Localização | Tipo | Chaves salvas |', '| --- | --- | --- |']
lines += [f'| {cell(x["location"])} | {x["kind"]}: {x["type"]} | {cell(", ".join(x["settings"]))} |' for x in instances]
lines += ['', '## Includes dinâmicos para inspeção contextual', '', '| Origem | Expressão |', '| --- | --- |']
lines += [f'| {link(x["source"])} | {cell(x["expression"])} |' for x in dynamic]
lines += ['', '## Media queries encontradas', '']
lines += [f'- `{cell(x)}`' for x in breakpoints]
(DOCS / 'INVENTARIO_TEMA.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
print(json.dumps(report, ensure_ascii=False, indent=2))
