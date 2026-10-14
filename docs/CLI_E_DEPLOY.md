# CLI, sincronização e publicação

## Estado confirmado — 13/10/2026

CLI 2.4.0, Node v24.21.0; loja 8346216, tema 14601136, Ipanema Clothing-2 1.2.4, ativo e forkado. .nuvem está ignorado pelo Git; manifesto contém ID/revisão. Git existe sem commits/arquivos rastreados.

Fluxo autorizado realizado: conexão correta → list → pull → fork → segundo pull → watch --no-browser. Não houve clone, tema alternativo, edição funcional ou publish. Fork desativou atualizações automáticas; não criou cópia isolada.

Diff: zero diferenças e 322 arquivos inalterados. Watch iniciado nesta sessão sobre o tema ativo; conferir processo antes de editar e não assumir persistência após reiniciar o ambiente.

## Autorização brasileira

Na versão instalada, authorize lança Chromium via Puppeteer com sessão separada; usa navegador do sistema como fallback. A documentação atual do repositório pode divergir. region=latam levou ao login em espanhol/demo; link correto para Brasil:

`https://brand-editor.tiendanube.com/api/auth/cli/start?region=br`

Pode-se abrir no Chrome habitual com acesso ao Admin e colar o token completo no prompt do CLI. Não substituir o domínio pelo da vitrine. Conferir theme list antes de baixar: login de parceiro sozinho não identifica a loja selecionada. Conexão da demo foi substituída pela correta; nunca registrar tokens.

## Efeitos das operações

| Operação | Efeito |
| --- | --- |
| Edição local | Com watch ativo, salvar já envia alterações |
| Pull | Apaga/recria entradas sincronizáveis e atualiza vínculo; preservar trabalho antes |
| Fork | Libera código e interrompe atualizações automáticas; não clona |
| Push/watch | Modifica remoto e pode excluir; tema ativo afeta visitantes |
| Publish | Torna instalação produtiva; autorização específica |
| Clone | Outra instalação para desenvolvimento; não executado |

--no-browser evita Chromium/recarga automática; atualizar Chrome manualmente. Parar watch com Ctrl+C no terminal proprietário, evitar processos duplicados e interromper antes de pull/reorganização/exclusões de código.

## Referência de comandos

```powershell
# Leituras
nuvemshop theme list
nuvemshop theme current
nuvemshop theme diff --theme-id 14601136 --detailed
nuvemshop theme preview --theme-id 14601136

# Operações já realizadas; não repetir sem necessidade
nuvemshop theme authorize
nuvemshop theme pull --theme-id 14601136
nuvemshop theme fork --theme-id 14601136
nuvemshop theme watch --theme-id 14601136 --no-browser
```

ID documenta o alvo atual; não é autorização permanente. Após clone/troca de loja, confirmar novo alvo. Não automatizar --yes/--force/--published. O segundo pull exigiu confirmação pela árvore existente e foi concluído interativamente, depois de conferir ausência de diferenças.

## Escopo da CLI instalada

dist/cli.js: SYNC_PREFIXES, shouldSync, themeUploadRelativePath e buildThemeDiffPlan restringem o escopo a blocks, config, custom, layouts, sections, snippets, static, templates, translations e manifest.json. Ocultos são ignorados; manifesto não é enviado; custom tem upload bloqueado. Sem fork, envio efetivo se restringe a templates/settings_data.

README.md, CLAUDE.md e docs/ ficam fora desse escopo, inclusive auditor Python/inventário. Revalidar ao atualizar a CLI. [CLI oficial](https://github.com/TiendaNube/cli).

## Preservação e rollback

1. Conferir loja, ID, ativo/fork e watch antes de editar.
2. Definir cópia não produtiva antes de mudanças relevantes; clone exige autorização do alvo.
3. Preservar base e obter snapshot remoto recente separado antes de comparar alterações locais/lojista.
4. Mesclar especialmente templates e config/settings_data.json; diff não resolve conflitos.
5. Revisar alterações/exclusões, validar e obter autorização de envio/publicação conforme tarefa.
6. Criar base Git revisada com credenciais ignoradas. Nenhum commit hoje fornece rollback.
7. Antes de publicar outra instalação, preservar ID/snapshot do produtivo e validar editor/preview. Republicar não desfaz arquivos alterados nesse tema.

Não foi produzido backup anterior ao fork. Recuperação exige snapshot completo, reconciliação e sincronização autorizada; Git local sozinho não restaura remoto.
