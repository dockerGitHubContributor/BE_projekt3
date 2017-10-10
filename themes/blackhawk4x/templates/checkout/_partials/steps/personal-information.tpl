{extends file='checkout/_partials/steps/checkout-step.tpl'}

{block name='step_content'}
  {if $customer.is_logged && !$customer.is_guest}

    <p class="identity">{l s='Connected as %first_name% %last_name%.' sprintf=['%first_name%' => $customer.firstname, '%last_name%' => $customer.lastname] d='Shop.Theme.CustomerAccount'}</p>
    <p>
      {* [1][/1] is for a HTML tag. *}
      {l
        s='Not you? [1]Log out[/1]'
        d='Shop.Theme.CustomerAccount'
        sprintf=[
          '[1]' => "<a href='{$urls.actions.logout}' class='btn btn-default'>",
          '[/1]' => "</a>"
        ]
      }
    </p>
    {if !isset($empty_cart_on_logout) || $empty_cart_on_logout}
      <p><small>{l s='If you sign out now, your cart will be emptied.' d='Shop.Theme.Checkout'}</small></p>
    {/if}

  {elseif $show_login_form}

   <p> <a href="{$urls.pages.order}" class="btn btn-default">{l s='No account?' d='Shop.Theme.CustomerAccount'}</a></p>
    {render file='checkout/_partials/login-form.tpl' ui=$login_form}

  {else}

    <p><a data-link-action="show-login-form" href="{$urls.pages.order_login}" class="btn btn-default">{l s='Already have an account?' d='Shop.Theme.CustomerAccount'} </a></p>
    {render file='checkout/_partials/customer-form.tpl' ui=$register_form guest_allowed=$guest_allowed}

  {/if}
{/block}
