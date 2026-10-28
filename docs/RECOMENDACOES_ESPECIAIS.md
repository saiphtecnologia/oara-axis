# Recomendações Especiais

O primeiro painel de configurações globais controla o botão, as imagens, o título e os nomes das três abas. As coleções `reco_tab_1`, `reco_tab_2` e `reco_tab_3` são cadastradas em `config/sections.txt` para seleção e ordenação manual no Organizador de produtos. Os três campos `product_list` do painel apontam para essas coleções por padrão; cada aba exibe os primeiros 40 produtos na ordem configurada. O nome “Histórico” é apenas texto editável.

O componente é incluído uma vez no layout global. Não aparece quando o controle está desligado ou todas as abas estão vazias. Abre os produtos pela URL nativa para manter variantes e carrinho no fluxo da loja. As imagens do editor usam `image_picker`; o GIF do botão usa a URL original da biblioteca de mídia para preservar a animação.

O tema atual não possui formulário fixo de produto. O JavaScript do componente detecta um formulário `#product_form` caso ele passe a usar posição fixa no rodapé mobile e ajusta o botão pela altura visível. O CSS também aceita a classe `product-fixed-form-visible` e a variável `--product-fixed-form-height`.

Validação local: JSON e JavaScript válidos; teste em navegador com painel de 400 px no desktop e 350 px em viewport de 390 px, lista rolável, abas vazias, roving tabindex, foco circular, Escape, overlay, bloqueio de rolagem e reabertura durante o fechamento. A renderização Twig, o Organizador de produtos e os estados reais de catálogo exigem sincronizar este tema com um ambiente de preview da Nuvemshop.
