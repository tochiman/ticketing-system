<script>
  import { Button, ButtonGroup } from 'flowbite-svelte';
  import { goto } from '$app/navigation';
  import { org } from '../store';

</script>


<div class="flex flex-col space-y-4 w-full max-w-md mx-auto mt-8">
  {#if $org}
    <!-- 赤いボタングループ -->
    <ButtonGroup class="w-full">
      <Button color="red" class="w-full" on:click={()=>goto(`/shop/control/org-edit`)}>組織編集</Button>
    </ButtonGroup>
    
    <ButtonGroup class="w-full">
      <Button color="red" class="w-full" on:click={()=>goto(`/shop/control/shoplist`)}>店舗一覧</Button>
    </ButtonGroup>
  {/if}

  <!-- 青いボタングループ -->
  <ButtonGroup class="w-full">
    <Button color="blue" class="w-full" on:click={()=>goto(`/shop/control/orderlist`)}>オーダー一覧</Button>
  </ButtonGroup>
  
  <ButtonGroup class="w-full">
    <Button color="blue" class="w-full" on:click={()=>goto(`/shop/control/itemlist`)}>商品一覧</Button>
  </ButtonGroup>
</div>
