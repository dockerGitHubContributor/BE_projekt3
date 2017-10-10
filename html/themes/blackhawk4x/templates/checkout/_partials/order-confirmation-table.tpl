<div id='order-items'>

  <h3>{l s='Order items' d='Shop.Theme.Checkout'}</h3>

  <table class="table">
    {foreach from=$products item=product}
      <tr>
        <td>
          <span class="product-image media-middle">
            <img class="" src="{$product.cover.small.url}">
          </span>
        </td>
        <td>
          {$product.name}
          {foreach from=$product.attributes key="attribute" item="value"}
            - <span class="value">{$value}</span>
          {/foreach}
          {if $product.customizations|count}
            <div class="customizations">
              <ul>
                {foreach from=$product.customizations item="customization"}
                  <li>
                    {if $customization.down_quantity_url}
                      <a href="{$customization.down_quantity_url}" data-link-action="update-quantity">-</a>
                    {/if}
                    <span class="product-quantity">{$customization.quantity}</span>
                    {if $customization.up_quantity_url}
                      <a href="{$customization.up_quantity_url}" data-link-action="update-quantity">+</a>
                    {/if}
                    <a href="{$customization.remove_from_cart_url}" class="remove-from-cart" rel="nofollow">
                      {l s='Remove' d='Shop.Theme.Actions'}
                    </a>
                    <ul>
                      {foreach from=$customization.fields item="field"}
                        <li>
                          <label>{$field.label}</label>
                          {if $field.type == 'text'}
                            {if (int)$field.id_module}
                              <span>{$field.text nofilter}</span>
                            {else}
                              <span>{$field.text}</span>
                            {/if}
                          {elseif $field.type == 'image'}
                            <img src="{$field.image.small.url}">
                          {/if}
                        </li>
                      {/foreach}
                    </ul>
                  </li>
                {/foreach}
              </ul>
            </div>
          {/if}
          {hook h='displayProductPriceBlock' product=$product type="unit_price"}
        </td>
        <td>{$product.quantity}</td>
        <td>{$product.price}</td>
      </tr>
    {/foreach}
  </table>

  <hr>

  <table class="table ">
    {foreach $subtotals as $subtotal}
      {if $subtotal.type !== 'tax'}
        <tr>
          <td >{$subtotal.label}</td>
          <td class="align-right">{$subtotal.value}</td>
        </tr>
      {/if}
    {/foreach}

    <tr>
      <td>{$totals.total.label} {$labels.tax_short}</td>
      <td class="align-right">{$totals.total.value}</td>
    </tr>
    <tr>
      <td>{$subtotals.tax.label}</td>
      <td class="align-right">{$subtotals.tax.value}</td>
    </tr>
  </table>

</div>
