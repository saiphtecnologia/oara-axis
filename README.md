# Oara Axis — Tema Nuvemshop Ipanema

Instalação real baixada e auditada estaticamente em 13/10/2026. A documentação inicial foi escrita quando a pasta estava vazia; o estado abaixo substitui aquelas pendências.

## Estado confirmado

| Item | Evidência atual |
| --- | --- |
| Loja | Oara Axis; domínio informado `oaraaxis.lojavirtualnuvem.com.br`; Store ID `8346216` validado pela API |
| Instalação | `14601136`, Ipanema, variante `Clothing-2`, sectionable |
| Versão / fork | `1.2.4`; fork ativo, confirmado pela API e manifesto |
| Tema produtivo | Sim: alterações sincronizadas afetam a vitrine atual |
| Arquivos | 323 incluindo manifesto; 49 sections, 54 blocks, 115 snippets |
| Acesso | `.nuvem` presente e ignorado pelo Git; credenciais não documentadas |
| CLI / Node | CLI `2.4.0`; Node `v24.21.0` |
| Git | Repositório local existente, sem commits e sem arquivos rastreados |
| Sincronização | `theme diff`: zero diferenças; 322 arquivos inalterados |
| Watch | Iniciado nesta sessão com `--no-browser`; verificar se continua ativo antes de editar |

## Documentação

| Arquivo | Conteúdo |
| --- | --- |
| [CLAUDE.md](CLAUDE.md) | Regras permanentes e contexto |
| [Memória técnica](docs/AI_RULES.md) | Convenções e limites |
| [Arquitetura](docs/ARQUITETURA_PROJETO.md) | Auditoria, estrutura e pendências |
| [Componentes](docs/COMPONENTES.md) | Mapa dos fluxos e arquivos |
| [Sections e blocks](docs/SECTIONS_E_BLOCKS.md) | Contratos e reutilização |
| [Configurações](docs/CONFIGURACOES_TEMA.md) | Escopos, consumidores e preservação |
| [Integrações](docs/INTEGRACOES.md) | Contratos e serviços identificados |
| [CLI e deploy](docs/CLI_E_DEPLOY.md) | Acesso, sincronização e rollback |
| [Inventário completo](docs/INVENTARIO_TEMA.md) | Schemas, campos, templates, ordens e includes |
| [Histórico](docs/HISTORICO_ALTERACOES.md) | Etapas e evidências |

## Desenvolvimento

Ler CLAUDE.md antes de editar. O tema está ativo e forkado; melhorias futuras da Nuvemshop precisam ser aplicadas manualmente. Preferir cópia não produtiva para mudanças funcionais, mediante definição e autorização do alvo.

Auditoria reproduzível: `python docs/auditar_tema.py`. O script gera somente o inventário em docs/ e não lê credenciais. JSONs, schemas, includes literais, ordens e sintaxe de JavaScript puro foram conferidos. Editor, frontend, responsividade e compra permanecem pendentes.

Documentação na raiz e em docs/ fica fora da sincronização da CLI instalada. Nenhum renderer, schema, configuração salva ou asset foi editado nesta revisão documental.
