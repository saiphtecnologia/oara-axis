# Integrações

Auditadas por presença/uso no código. Não houve consulta à lista administrativa de apps nem ao HTML renderizado; pixels, Analytics/GTM e apps ativos não estão confirmados.

| Contrato/serviço | Evidência | Preservação/teste |
| --- | --- | --- |
| Plataforma | platform_head_content, platform_body_content e component head-tags no layout | Preservar injeções; apps/tracking podem existir só no HTML real |
| Nube SDK | nubesdk-slot em layout, footer, produto, cards e cadastro | Preservar slots antes/depois das áreas críticas |
| Âncoras de apps | data-store/data-component em produto, filtros, frete, carrinho, formulários e assinaturas | Não renomear contratos e IDs dinâmicos |
| LS frontend | LS.ready, variantes, addToCartEnhanced, quantidades, frete, newsletter e assinaturas | Dependem da plataforma; testar retorno/erro |
| Google Fonts | Preconnect no layout, URL de fontes/tokens | Validar carregamento/fallback |
| Vídeo | Vimeo/oEmbed, YouTube e SDK Cloudflare Stream em store.js/snippets | Chamadas condicionadas à mídia; presença não comprova uso em toda página |
| WhatsApp/social | snippets/social/*.tpl | WhatsApp depende de store.whatsapp; destinos vêm do Admin |
| Newsletter/CAPTCHA | newsletter.tpl, recaptcha-script.tpl e LS.newsletter | Ativação e sucesso/erro dependem de runtime/contexto |
| Pagamento/frete | Dados nativos, parcelas, calculadora e logos | Não são credenciais de gateway; preservar integração de compra |
| SEO | head-tags e snippets/structured-data/*.tpl | Validar HTML/JSON-LD renderizados |
| Preview | initPreviewMessageListener, brand-editor:select-element | Filtra janela pai/tipo; testar seleção e scroll no editor |

Slots dinâmicos podem ser injetados pela plataforma: não inferir ausência pelo snapshot. [Integração oficial com apps](https://nuvemshop.dev/themes/sectionable-themes/app-integration).

Não registrar tokens, senhas, cookies ou conteúdo de .nuvem. Confirmar serviços/eventos efetivamente ativos no Admin/preview sem submissões reais ou instalação de apps nesta revisão documental.
