# Histórico de alterações

## 2026-10-13 — Documentação inicial e regras permanentes

- Funcionalidade: preparação documental; nenhuma alteração funcional.
- Arquivos: CLAUDE.md, README.md, docs/AI_RULES.md, docs/ARQUITETURA_PROJETO.md, docs/COMPONENTES.md, docs/SECTIONS_E_BLOCKS.md, docs/CONFIGURACOES_TEMA.md, docs/INTEGRACOES.md, docs/CLI_E_DEPLOY.md e este histórico.
- Motivo: estabelecer base técnica e fluxo de desenvolvimento solicitado.
- Resumo técnico: leitura da pasta vazia, documentação oficial, versão/help e filtros locais da CLI; registro das regras permanentes e das pendências de auditoria da instalação.
- Impacto: somente documentação local; sem alterações na loja, autorização, download, fork, watch, sincronização ou publicação.
- Testes/verificações: inventário inicial com arquivos ocultos; CLI 2.4.0 e Node v24.21.0; Git status/diff/log indicam ausência de repositório; revisão dos arquivos Markdown e links relativos. Editor/frontend não testáveis sem código/loja confirmados.

## 2026-10-13 — Conexão real, download/fork e auditoria estática

- A conexão inicial da demo/Amazonas foi substituída após corrigir a região de autorização para br.
- API confirmou loja 8346216, Ipanema 14601136 Clothing-2, versão final 1.2.4, ativo/forkado.
- Executados com autorização: authorize, list, pull, fork, segundo pull e watch --no-browser. Nenhum clone, edição funcional ou publish.
- Fork interrompe atualizações automáticas. Watch pode enviar alterações futuras ao salvar no tema produtivo.
- Documentos revisados: README, contexto de CLAUDE, memória técnica, arquitetura, componentes, sections/blocks, configurações, integrações, CLI e histórico.
- Adicionados docs/auditar_tema.py e docs/INVENTARIO_TEMA.md: mapa completo dos schemas/campos, templates, ordens, includes e media queries.
- Inventário: 323 arquivos com manifesto, 49 sections, 54 blocks, 115 snippets, 23 templates; 699 declarações de settings, 93 globais.
- Validação: 40 JSONs/103 schemas parseados; 298 includes literais existentes; tipos e ordens conferidos; nenhum erro nesses critérios. node --check aprovado nos dois arquivos JS puros. Diff remoto sem diferenças.
- Git presente, sem commits/arquivos rastreados; .nuvem ignorado.
- Editor/frontend/compra: não testados. Auditoria estática não valida runtime ou apps administrativos.
- Impacto desta revisão: somente docs/auditor; nenhum renderer, schema, valor salvo ou asset alterado. Documentação fora da sincronização da CLI 2.4.0.

## Modelo para próximos registros

```markdown
## AAAA-MM-DD — Funcionalidade

- Funcionalidade:
- Arquivos alterados:
- Motivo:
- Resumo técnico:
- Sections/blocks e configurações:
- Impacto:
- Testes no editor:
- Testes no frontend:
- Sincronização/publicação: alvo, autorização e resultado, se realizados.
```

Registrar alterações relevantes; não incluir credenciais. Não declarar testes executados quando forem apenas recomendações.
