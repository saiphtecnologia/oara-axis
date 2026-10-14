# Sections e blocks

## Inventário confirmado

49 sections e 54 blocks, todos com schema JSON parseável. O [inventário completo](INVENTARIO_TEMA.md) registra cada arquivo, settings, filhos aceitos, tags, limites, restrições de página/layout, presets e includes. Também lista 49 instâncias de seção e 39 de bloco nos 23 templates.

## Contratos concretos

- sections/custom.tpl aceita tag general; controla direção desktop/mobile, alinhamento, largura, gap, padding e cores. Preset usa group, heading, text e button.
- group, slide, banner e outros pais incluem filhos dinamicamente pelo tipo. Conferir block_order, contexto herdado e schema aplicável.
- slideshow aceita slide e tem max_blocks=10. Os slides têm composição própria de filhos.
- header/navigation-bar ficam no layout header; footer possui template próprio. enabled_on real está catalogado.
- main-product usa product-media/product-info, limit=1, deletable=false, hideable=false e locked_blocks=true.
- product-info declara schemas inline de filhos além dos arquivos reutilizáveis. Conferir o pai ao alterar description/purchase-info.
- main-products-grid é habilitada para categoria/busca e lê colunas/paginação locais.
- header-logo aplica block_attributes; snippets renderizam imagem/texto e altura desktop/mobile do bloco.
- config/sections.txt define primary, new, sale, timer_offers e featured: grupos de produtos distintos das instâncias de seção visual.

## Cadeias confirmadas

| Composição | Settings | Renderização |
| --- | --- | --- |
| home → slideshow → slide → heading | autoplay, alinhamento/gap, título/tamanhos | slideshow.tpl → slide.tpl → heading.tpl; Swiper/CSS |
| product → main-product → product-media | largura, formato, colunas/gap/miniaturas | main-product.tpl → product-media.tpl → product-image.tpl; Swiper/Fancybox |
| product → product-info → purchase-info → icon-text-item | gap/padding e texto/ícone dos filhos | Schema inline do pai e renderers por arquivo |
| header → header-logo | height, height_mobile, use_different_mobile_height | header.tpl → header-logo.tpl → snippets de logo |

Campos usam type:setting, setting_type, id, labels t:, defaults e default_setting. visible_if/disabled_if não equivalem automaticamente a condição de renderização. Há aliases como block_settings em snippets. [Sections oficiais](https://nuvemshop.dev/themes/sectionable-themes/sections), [blocks](https://nuvemshop.dev/themes/sectionable-themes/blocks).

Preservar IDs, tipos, valores, order/block_order, disabled, tags, limites e atributos do editor. Presets inicializam novas instâncias; não substituir dados atuais por presets/defaults.

O auditor confirma sintaxe, tipos/arquivos e referências das ordens. Tags aceitas, restrições completas e efeito visual exigem análise contextual e teste no editor: adição, remoção permitida, reordenação, nesting, seleção, persistência, atualização dinâmica e mobile.
