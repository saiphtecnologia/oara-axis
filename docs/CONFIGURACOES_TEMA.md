# Configurações do tema

## Escopos da instalação

| Escopo | Definição | Valores/consumo |
| --- | --- | --- |
| Global | config/settings_schema.json: 93 campos com ID | config/settings_data.json contém 83 chaves em settings; consumo settings.* |
| Section | Schema de sections/*.tpl | Valores nos templates; section.settings.* |
| Block | Schema em blocks/*.tpl ou inline no pai | Valores por instância; block.settings.*, aliases e contexto herdado |

O [inventário](INVENTARIO_TEMA.md) registra 699 declarações incluindo inline, com ID, tipo, default/herança, opções, intervalos, condições e referências diretas por linha. A contagem não representa IDs únicos entre componentes; eles podem se repetir em escopos diferentes.

## Mapa principal

| Grupo | Chaves concretas | Consumidores |
| --- | --- | --- |
| Cores/fontes | background_color, text_color, accent_color, font_headings, font_rest | layouts/resources/style-tokens.tpl e estilos locais |
| Layout/botões | page_width, border_radius, button_primary_background_color, button_primary_style | Tokens/classes compartilhadas e overrides locais |
| Cards | quick_shop, product_installments, product_color_variants, product_hover, product_item_slider | Snippets de produto, modal e store.js |
| Produto | variant_format, product_detail_installments, product_sku, product_stock, shipping_calculator_product_page | Formulário, variantes, informações e frete |
| Carrinho | ajax_cart, cart_open_type, shipping_calculator_cart_page | Layout, snippets, notificações e LS |
| Popup/CSS | promotional_popup_enabled, css_code | Inclusões condicionais e CSS inline do lojista |
| Section | section_width, vertical_padding, horizontal_padding e cores | Instância e renderer local |
| Mídia | format, columns, gap, show_thumbnails, thumbnail_position | product-media → product-image via alias block_settings |
| Logo | height, height_mobile, use_different_mobile_height | header-logo e snippets de logo |

css_code está nulo no snapshot. Textos, imagens e links atuais são preservados nos JSONs sem replicação integral nos docs. WhatsApp é lido de store.whatsapp, dado administrativo.

83 chaves salvas frente a 93 declarações não demonstra perda: há defaults, ausência e compatibilidade. Não preencher/remover automaticamente. Referência não encontrada por busca direta não prova campo sem consumidor: aliases, includes e heranças precisam de leitura contextual.

product-info tem schemas inline. Colunas/paginação de main-products-grid são locais; não presumir efeito de uma alteração global nessa seção.

Comparar templates/settings_data com snapshot remoto recente antes de enviar. Preservar valores, defaults, presets e traduções como camadas distintas. Labels usam t: e storefront | t, com arquivos em translations/. Validar opções, tipos, intervalos, heranças, persistência e resultado no editor/frontend/mobile. [Configurações oficiais](https://nuvemshop.dev/themes/sectionable-themes/global-settings).
