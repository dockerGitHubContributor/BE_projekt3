{include file='_partials/form-errors.tpl' errors=$errors['']}

<form action="{$action}" id="customer-form" method="post" class="form-horizontal">

  <section class="form-fields">
    {block "form_fields"}
      {foreach from=$formFields item="field"}
        {block "form_field"}
          {form_field field=$field}
        {/block}
      {/foreach}
    {/block}
  </section>

  <footer class="form-footer">
    <input type="hidden" name="submitCreate" value="1">
    {block "form_buttons"}
      <button data-link-action="save-customer" type="submit" class="btn btn-primary">
        {l s='Save' d='Shop.Theme.Actions'}
      </button>
    {/block}
  </footer>

</form>
