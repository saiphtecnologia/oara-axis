# Arquitetura e auditoria da instalação

Auditoria em 13/10/2026. A etapa inicial descrevia pasta vazia; esta revisão inspeciona o tema baixado após autorização, fork e segundo pull.

## Identidade e evidência

API: loja `8346216`, instalação `14601136`, Ipanema `Clothing-2`, versão `1.2.4`, `prod=yes`, `fork=yes`, `archived=no`. Manifesto local confirma ID, versão e fork. Seu campo `theme` é nulo: nome/base foram confirmados pela API. Revisão local está em manifest.json.

`theme diff` retornou zero diferenças e 322 arquivos inalterados. O manifesto é metadado local; são 323 arquivos incluindo ele. Essa comparação descreve o momento da consulta; não impede edição posterior pelo lojista. Não há snapshot anterior ao fork para rollback completo.

## Diretórios reais

| Diretório | Arquivos | Papel |
| --- | ---: | --- |
| blocks/ | 54 | Componentes editáveis, schemas e filhos |
| config/ | 3 | Schema global, valores salvos e grupos de produtos |
| layouts/ | 3 | Shell HTML, tokens e sprite de ícones |
| sections/ | 49 | Renderização de seções/páginas |
| snippets/ | 115 | Compra, navegação, conta e utilitários |
| static/ | 61 | CSS, JavaScript e placeholders |
| templates/ | 23 | 21 páginas e duas regiões de layout |
| translations/ | 14 | Sete JSONs de storefront e sete de schema |

Não encontrados package.json, lockfiles, SCSS/Sass, sourcemaps ou configuração de build. custom/ não existe. O [inventário](INVENTARIO_TEMA.md) detalha arquivos, contratos e consumidores.

## Renderização

`layouts/layout.tpl` injeta tokens de `layouts/resources/style-tokens.tpl`, CSS e conteúdo da plataforma; renderiza header/footer por `layout_template` e página por `page_template_content`. Header é omitido na página de senha; footer adapta seu conteúdo. Carrinho, compra rápida, WhatsApp e popup dependem de contexto/configurações.

Templates preservam IDs, type, settings, blocks, order, block_order e disabled. A composição persistida difere dos presets para novas instâncias. [Modelo oficial](https://nuvemshop.dev/themes/sectionable-themes/overview).

## CSS e JavaScript

CSS crítico/utilitário é inserido inline. style-async.css usa media=print e troca para all após carregar. settings.css_code possui ponto de injeção próprio e está nulo no snapshot. Tokens globais produzem fontes, cores, medidas e botões. Media queries incluem 576, 768, 992, 1024, 1200 e 1400 px, hover e movimento reduzido; não assumir um breakpoint único.

libraries-standalone.js carrega primeiro. Após LS.ready, o layout inclui libraries.js.tpl e carrega store.js. Bibliotecas identificadas: Swiper, Lazysizes e Fancybox; esta última é condicionada à página de produto. Há código minificado nos bundles e no CSS assíncrono; o processo de geração não está presente.

store.js usa LS, jQueryNuvem e `DOMContentLoaded.addEventOrExecute(init)` para navegação, modais, carrosséis, variantes, compra, frete e recomendações. Há listeners delegados e MutationObservers. Preview recebe `brand-editor:select-element` com filtro pela janela pai. Um ciclo completo de teardown/reinicialização de todos os componentes após qualquer mudança no editor não foi comprovado; testar antes de alterar handlers.

## Verificações executadas

| Critério | Resultado |
| --- | --- |
| JSONs | 40 válidos incluindo manifesto |
| Schemas Twig | 103 parseados: 49 sections, 54 blocks |
| Settings declarados | 699 incluindo inline; 93 globais; 83 chaves globais salvas |
| Instâncias nos templates | 49 seções e 39 blocos; referências de ordem conferidas |
| Includes | 298 literais com destinos existentes; 29 expressões dinâmicas catalogadas |
| IDs de settings | Nenhuma duplicidade dentro de cada lista analisada |
| JavaScript puro | node --check aprovado em store.js e libraries-standalone.js |
| Git/credenciais | Repositório sem commits/arquivos rastreados; .nuvem ignorado |
| Comparação remota | Zero diferenças nos arquivos sincronizáveis |

O auditor não compila Twig nem valida integralmente schemas Nuvemshop. Tags, intervalos/opções, traduções, heranças e runtime exigem análise contextual. libraries.js.tpl contém Twig e não foi validado como JavaScript puro.

## Arquivos críticos e pendências

| Área | Verificação ainda necessária |
| --- | --- |
| Produto/variações | main-product, product-form, variantes/galeria: testar SKU, imagem, preço, quantidade e estoque |
| Carrinho/checkout | Snippets de carrinho e LS: testar adição, remoção, frete e passagem à URL nativa |
| SEO | head-tags e structured-data: validar saída HTML/JSON-LD com dados reais |
| Editor | Adição, seleção, reordenação, nesting, campos condicionais/mobile, persistência e atualização dinâmica |
| Integrações | Confirmar apps/pixels efetivamente injetados no Admin/HTML real |
| Responsividade | Header, menus, grid, galeria e modais nas larguras relevantes |
| Git/rollback | Criar base revisada e versionada; não há commits anteriores |
| Desenvolvimento | Definir cópia não produtiva para futuras mudanças; alvo atual está ativo |

Nenhuma falha funcional foi demonstrada nesta análise estática. Código do checkout hospedado, apps administrativos e funcionamento no navegador não estão auditados pelos arquivos locais.
