{# Global drawer; product_list settings resolve the manually ordered collections. #}
{% set reco_products_1 = settings.reco_tab_1.products | default(sections.reco_tab_1.products | default([])) %}
{% set reco_products_2 = settings.reco_tab_2.products | default(sections.reco_tab_2.products | default([])) %}
{% set reco_products_3 = settings.reco_tab_3.products | default(sections.reco_tab_3.products | default([])) %}
{% if settings.special_recommendations_enabled and (reco_products_1 | length or reco_products_2 | length or reco_products_3 | length) %}
  {% set recommendations_title = settings.special_recommendations_title | default('Recomendações') %}
  {% set recommendations_initial_tab = reco_products_1 | length ? 1 : (reco_products_2 | length ? 2 : 3) %}
  {% set recommendations_icon = settings.special_recommendations_icon %}
  {% set recommendations_banner = settings.special_recommendations_banner %}
  {% set recommendations_icon_media = recommendations_icon and recommendations_icon starts with '@media-lib:' ? recommendations_icon | resolve_media : null %}

  <div class="js-special-recommendations special-recommendations" data-component="special-recommendations">
    <button class="js-special-recommendations-open special-recommendations__trigger" type="button" aria-label="Abrir {{ recommendations_title }}" aria-controls="special-recommendations-panel" aria-expanded="false">
      {% if recommendations_icon %}
        {# Source URL retains every frame of an uploaded GIF. #}
        <img src="{{ recommendations_icon_media ? recommendations_icon_media.sourceUrl : recommendations_icon | settings_image_url('original') }}" alt="" width="90" height="90">
      {% else %}
        <span class="special-recommendations__trigger-fallback" aria-hidden="true">LUVÈRE</span>
      {% endif %}
    </button>

    <div class="js-special-recommendations-overlay special-recommendations__overlay" hidden></div>
    <aside class="js-special-recommendations-panel special-recommendations__panel" id="special-recommendations-panel" role="dialog" aria-modal="true" aria-labelledby="special-recommendations-title" hidden>
      <button class="js-special-recommendations-close special-recommendations__close" type="button" aria-label="Fechar {{ recommendations_title }}">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 5 19 19M19 5 5 19"/></svg>
      </button>

      {% if recommendations_banner %}
        <div class="special-recommendations__banner">
          <img src="{{ recommendations_banner | settings_image_url('large') }}" srcset="{{ recommendations_banner | settings_image_url('large') }} 480w, {{ recommendations_banner | settings_image_url('original') }} 800w" sizes="(max-width: 420px) 100vw, 400px" alt="" width="800" height="500" loading="lazy">
        </div>
      {% else %}
        <div class="special-recommendations__banner special-recommendations__banner--fallback" aria-hidden="true">
          <span>Escolhas que<br><strong>combinam</strong><br>com você</span>
        </div>
      {% endif %}

      <h2 class="special-recommendations__title" id="special-recommendations-title">{{ recommendations_title }}</h2>
      <div class="special-recommendations__tabs" role="tablist" aria-label="{{ recommendations_title }}">
        {% for tab_index in 1..3 %}
          {% set tab_title = attribute(settings, 'special_recommendations_tab_' ~ tab_index ~ '_title') | default(tab_index == 1 ? 'Pra Você' : (tab_index == 2 ? 'Histórico' : 'SALE')) %}
          <button class="js-special-recommendations-tab special-recommendations__tab{% if tab_index == recommendations_initial_tab %} is-active{% endif %}" type="button" role="tab" id="special-recommendations-tab-{{ tab_index }}" aria-controls="special-recommendations-content-{{ tab_index }}" aria-selected="{{ tab_index == recommendations_initial_tab ? 'true' : 'false' }}" tabindex="{{ tab_index == recommendations_initial_tab ? '0' : '-1' }}">{{ tab_title }}</button>
        {% endfor %}
      </div>

      <div class="special-recommendations__content">
        {% for tab_index in 1..3 %}
          {% set tab_products = tab_index == 1 ? reco_products_1 : (tab_index == 2 ? reco_products_2 : reco_products_3) %}
          <div class="js-special-recommendations-content special-recommendations__tabpanel" id="special-recommendations-content-{{ tab_index }}" role="tabpanel" aria-labelledby="special-recommendations-tab-{{ tab_index }}" tabindex="0"{% if tab_index != recommendations_initial_tab %} hidden{% endif %}>
            {% if tab_products | length %}
              <ul class="special-recommendations__products">
                {% for product in tab_products | slice(0, 40) %}
                  {% include 'snippets/special-recommendations-item.tpl' with { product: product } %}
                {% endfor %}
              </ul>
            {% else %}
              <p class="special-recommendations__empty">Em breve, novas sugestões por aqui.</p>
            {% endif %}
          </div>
        {% endfor %}
      </div>
    </aside>
  </div>
{% endif %}
