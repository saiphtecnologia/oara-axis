<li class="special-recommendations__item">
  <article class="special-recommendations__product">
    <a class="special-recommendations__product-image" href="{{ product.url }}" aria-label="Ver {{ product.name }}">
      {% if product.featured_image %}
        <img src="{{ product.featured_image | product_image_url('medium') }}" alt="{{ product.featured_image.alt | default(product.name) }}" width="80" height="80" loading="lazy">
      {% else %}
        <span class="special-recommendations__image-placeholder" aria-hidden="true"></span>
      {% endif %}
    </a>
    <div class="special-recommendations__product-details">
      <a class="special-recommendations__product-name" href="{{ product.url }}" title="{{ product.name }}">{{ product.name }}</a>
      {% if product.display_price %}
        <div class="special-recommendations__product-prices">
          {% if product.compare_at_price > product.price %}
            <span class="special-recommendations__compare-price">{{ product.compare_at_price | money }}</span>
          {% endif %}
          <strong class="special-recommendations__price">{{ product.price | money }}</strong>
        </div>
        {% if settings.product_installments %}
          {% include 'snippets/payments/installments.tpl' with {
            location: 'product_item',
            container_classes: { installment: 'special-recommendations__installments' }
          } %}
        {% endif %}
      {% endif %}
    </div>
    <a class="special-recommendations__buy" href="{{ product.url }}" aria-label="{% if product.available and product.display_price %}Comprar{% else %}Ver{% endif %} {{ product.name }}">
      {% if product.available and product.display_price %}Comprar{% else %}Ver produto{% endif %}
    </a>
  </article>
</li>
