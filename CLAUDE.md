# Instruções permanentes — Oara Axis

## Contexto e evidências

Plataforma: Nuvemshop. Loja Oara Axis, Store ID `8346216`; tema `14601136`, Ipanema `Clothing-2` `1.2.4`, sectionable, fork ativo e produtivo confirmados pela API em 13/10/2026. Ambiente Windows/PowerShell, VS Code, Claude Code/Codex e CLI oficial `2.4.0`.

A pasta estava vazia antes da documentação inicial. Depois houve autorização correta, pull, fork e novo pull. Existem 323 arquivos do tema incluindo manifesto, `.nuvem` ignorado pelo Git e repositório sem commits. Auditoria estática concluída nos critérios registrados; editor/frontend não testados. Watch iniciado com --no-browser nesta sessão sobre o tema ativo; conferir o processo antes de editar. Consulte [arquitetura](docs/ARQUITETURA_PROJETO.md), [inventário](docs/INVENTARIO_TEMA.md) e [CLI](docs/CLI_E_DEPLOY.md).

## Antes de alterar

1. Ler este arquivo e somente os documentos adicionais relevantes.
2. Consultar a [documentação oficial da Nuvemshop](https://nuvemshop.dev/themes/sectionable-themes/overview), especialmente a referência aplicável à mudança.
3. Identificar arquivos, sections, blocks, schemas, configurações persistidas e dependências.
4. Explicar comportamento atual, plano, impactos e riscos.
5. Aguardar aprovação do usuário para mudanças estruturais.

## Sections, blocks e editor

- Preservar funcionalidades nativas e compatibilidade com o editor visual.
- Reutilizar seções e blocos existentes; evitar duplicações desnecessárias.
- Priorizar configurações editáveis pelo lojista e seguir os schemas oficiais.
- Não modificar schemas sem analisar dependências. Preservar IDs, chaves, tipos de settings, configurações existentes e referências nos templates.
- Não sobrescrever valores do lojista com defaults ou presets.
- Considerar blocos aninhados quando suportados; validar valores padrão, estados vazios, limites, visibilidade e ordenação.
- Toda nova seção visual personalizável deve incluir campos no schema: títulos, textos, imagens, banners, botões, links, cores e espaçamentos quando aplicáveis, visibilidade, ordenação e conteúdo responsivo quando suportado.
- Não deixar hardcoded conteúdo que deva ser editável. Não criar painel externo para recursos atendidos pelo editor nativo.

## CSS, JavaScript e e-commerce

- Reutilizar padrões existentes, isolar CSS e preservar responsividade; evitar CSS global desnecessário.
- Não editar minificados quando houver fonte equivalente. Confirmar geração/build antes de alterar assets.
- Preservar JavaScript nativo; evitar listeners duplicados; considerar re-renderizações do editor; reutilizar bibliotecas adequadas e evitar dependências desnecessárias.
- Preservar produto, preço, variações, estoque, carrinho, checkout, SEO, analytics, integrações e experiência mobile.
- Manter atributos e pontos de integração identificados no código. Não presumir acesso ao código do checkout.

## CLI e Git

- Nunca executar automaticamente comandos que alterem o estado remoto. Autorização da CLI também depende de solicitação explícita.
- Antes de pull com risco de sobrescrita, fork, push, watch, publish, update, delete, clone ou create: apresentar alvo, plano, alterações/exclusões possíveis e aguardar autorização.
- Usar o fluxo oficial após autorização e confirmação da loja e do tema correto. Não publicar automaticamente.
- Distinguir desenvolvimento, sincronização e publicação. Alterar arquivos de um tema já ativo pode afetar visitantes mesmo sem publish.
- Verificar Git status antes de mudanças relevantes e diff após implementação.
- Não executar comandos Git destrutivos sem autorização; não executar reset destrutivo, clean, force push ou push sem autorização.
- Nunca registrar credenciais. Antes de versionar, excluir `.nuvem` do Git e revisar arquivos sensíveis.

## Documentação e entrega

Atualizar somente quando necessário: histórico para alteração funcional relevante; AI_RULES para convenção permanente; arquitetura para mudança arquitetural; componentes para mudança relevante; sections/blocks para criação ou alteração significativa; configurações para nova chave ou mudança relevante; integrações para criação/remoção/modificação; CLI para alteração de fluxo. Não reescrever documentação sem necessidade.

Ao entregar uma funcionalidade informar: implementação, arquivos, sections/blocks, configurações adicionadas, testes no editor, testes no frontend, impactos e o que precisa ser sincronizado/publicado. Não publicar sem autorização.
