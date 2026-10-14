# Memória técnica permanente

- Alvo confirmado: loja `8346216`, tema `14601136`, Ipanema `Clothing-2` `1.2.4`, fork ativo e produtivo. Não reutilizar a conexão anterior da demo.
- Separar snapshot local, referência oficial e testes pendentes; não transferir estrutura de outros temas por suposição.
- A instalação usa `translations/`, com arquivos de storefront e `*.schema.json` do editor.
- Preservar IDs, tipos, chaves, ordens e valores persistidos; schema e renderer devem evoluir juntos. `product-info` também declara schemas inline: conferir o pai.
- Conteúdo personalizável deve ser administrável no editor nativo; reutilizar componentes e preservar fluxos de compra.
- Preservar contratos LS, `data-store`, `data-component`, `block_attributes`, slots Nube SDK e injeções da plataforma.
- Tema ativo: watch envia mudanças ao salvar. A revisão documental não autoriza futuras alterações funcionais/publicação.
- Comparar templates e valores do lojista com snapshot remoto recente antes de enviar; não sincronizar árvore incompleta.
- CLI 2.4.0 restringe sincronização por prefixos: documentos na raiz e docs/ ficam fora do escopo. Revalidar após atualização.
- Nesta versão, authorize abre Chromium separado. Link brasileiro usa `region=br`; pode-se colar no CLI o token gerado no Chrome habitual.
- Não há pipeline de build local identificado. Não editar bibliotecas minificadas sem fonte e geração confirmadas.
- Git existe sem commits; `.git` sozinho não fornece rollback versionado.
- Nunca incluir tokens, conteúdo de `.nuvem`, senhas ou cookies em documentação, logs compartilhados ou commits.
- Regenerar [inventário](INVENTARIO_TEMA.md) com `python docs/auditar_tema.py` após mudanças de composição/schema; análise estática não equivale a teste visual.
