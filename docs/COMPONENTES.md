# Componentes do e-commerce

Mapa confirmado do Ipanema 1.2.4 em 13/10/2026. Caminhos relativos à raiz. [Inventário](INVENTARIO_TEMA.md) detalha schemas, settings, includes e composição.

| Componente | Arquivos principais | Dependências/controles |
| --- | --- | --- |
| Header | templates/layout/header.json; sections/header.tpl; blocks/header-logo.tpl, header-navigation.tpl, header-utilities.tpl | Logo, menus, utilitários; settings de bloco/seção e inicializadores do header |
| Menus | blocks/header-navigation.tpl; snippets/header/header-nav-mobile.tpl; snippets/navigation/navigation-panel.tpl, navigation-list-hamburger.tpl | menus/categorias, handlers .js-* e modal mobile |
| Busca | snippets/header/search-form.tpl; blocks/header-utilities.tpl; templates/pages/search.json; sections/main-products-grid.tpl | Formulário nativo, initSearchTrigger e grid |
| Barra superior | sections/navigation-bar.tpl; blocks/nav-*.tpl | Anúncios, social, contato e menus; até três blocos e três barras |
| Footer | templates/layout/footer.json; sections/footer.tpl; blocks/footer-*.tpl; snippets/footer/*.tpl | Menus mobile, newsletter, selos, pagamentos/envios e contexto de senha |
| Home | templates/pages/home.json | Ordem e dados salvos; composição catalogada no inventário |
| Banners/hero | sections/banners.tpl, hero.tpl, hero-divided.tpl, slideshow.tpl; blocks/banner.tpl, slide.tpl | Imagens/mobile, textos/filhos, Swiper e parallax com movimento reduzido |
| Vitrines | sections/product-list.tpl, featured-product.tpl, related-products.tpl; blocks/products.tpl; snippets/product-list/products-section.tpl | Fontes de produto, quantidade e grid; grupos em config/sections.txt |
| Card | snippets/product-list/product-item/item.tpl, item-image.tpl, item-slider.tpl, item-colors.tpl, item-quick-shop.tpl | product, labels, parcelas, compra rápida; slots/atributos de apps |
| Categoria/listagem | sections/category-hero.tpl, main-products-grid.tpl; snippets/product-list/filters/*.tpl; pagination.tpl | Colunas locais, filtros, ordenação e paginação; initInfiniteScroll |
| Produto/galeria | sections/main-product.tpl; blocks/product-media.tpl; snippets/product/product-image.tpl, product-image-thumbs.tpl, product-video*.tpl | product; alias block_settings; Swiper/Fancybox e vídeo |
| Informações/compra | blocks/product-info.tpl; snippets/product/product-form.tpl; blocks/description.tpl, purchase-info.tpl | Formulário nativo e filhos; schemas inline no pai |
| Variações/quantidade | snippets/product/product-variants.tpl, product-quantity.tpl, kit-product-variants.tpl | LS.changeVariant/registerOnChangeVariant; kits, estoque e quantidade |
| Preço/estoque | product-form.tpl; snippets/product/price-without-taxes.tpl; snippets/labels.tpl; snippets/promotions/*.tpl | Dados do produto/variante, descontos e settings globais |
| Carrinho | sections/main-cart.tpl; snippets/cart/cart-modal.tpl, cart-panel.tpl, _cart-item.tpl, cart-totals.tpl, cart-summary.tpl, cart-button.tpl | cart, settings.ajax_cart, LS e notificações |
| Checkout | snippets/cart/cart-button.tpl; snippets/forms/checkout-enabled-validation-messages.tpl | URL/validação da plataforma; fonte do checkout hospedado não está no tema |
| Frete | snippets/shipping/shipping-calculator.tpl, shipping-calculator-item.tpl, branches.tpl | CEP, retirada e LS.calculateShippingAjax |
| Conta/formulários | sections/main-account-*.tpl, main-login.tpl, main-register.tpl, main-reset.tpl, main-newpass.tpl, main-contact.tpl; snippets/forms/*.tpl | Dados de cliente, endpoints nativos e CAPTCHA conforme contexto |
| Newsletter | blocks/newsletter-form.tpl, footer-newsletter.tpl; snippets/forms/newsletter.tpl; sections/newsletter.tpl | LS.newsletter, popup e campos nativos |
| Modais/popups | snippets/modals/modal.tpl, quick-shop-modal.tpl; snippets/promotional-modal.tpl, notification.tpl | quick_shop, promotional_popup_enabled e modal handler |
| WhatsApp/social | snippets/social/whatsapp-chat.tpl, contact-links.tpl, social-share.tpl | store.whatsapp e destinos administrativos |
| Assinaturas | snippets/subscriptions/*.tpl; página account/subscription-address | LS.subscription* e contexto da plataforma |

Para alteração concreta, seguir renderer → snippet → seletor/evento → CSS/JS, conferir valores e testar estados vazios/mobile. Presença e vínculos de código não comprovam funcionamento no frontend.
