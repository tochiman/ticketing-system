<script>
  import { Button } from 'flowbite-svelte';
  import { goto } from '$app/navigation';
</script>

<div class="flex flex-col items-center justify-center min-h-screen bg-white">
  <h1 class="text-4xl font-bold mb-16">バキバキ食券管理システム</h1>
  
  <div class="flex flex-col gap-4 w-full max-w-xs">
    <Button on:click={()=>goto(`/shop/login`)}
      class="w-full bg-blue-600 hover:bg-blue-700"
      size="lg">
      ログイン
    </Button>

    <Button on:click={()=>goto(`/shop/org-regist`)}
      class="w-full bg-blue-600 hover:bg-blue-700"
      size="lg">
      組織登録
    </Button>
  </div>
</div>