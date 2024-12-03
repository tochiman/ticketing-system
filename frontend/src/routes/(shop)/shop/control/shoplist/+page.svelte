<script>
    import { Button, Card} from 'flowbite-svelte';
    import { goto } from '$app/navigation';
    
    const stores = ['店舗A', '店舗B', '店舗C', '店舗D', '店舗E', '店舗F'];
  </script>
  
  <div class="flex">
  
    <!-- メインコンテンツ -->
    <main class="flex-1 p-8">
      <h1 class="text-2xl font-bold mb-6">店舗一覧</h1>
      
      <!-- 検索バー -->
      <div class="mb-6">
        <input type="search" class="w-full p-2 border rounded-lg" placeholder="検索...">
      </div>
      
      <!-- 店舗グリッド -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {#each stores as store}
          <Card>
            <h5 class="mb-2 text-xl font-bold">{store}</h5>
            <Button color="light" class="w-full" on:click={()=>goto(`/shop/control/shoplist/edit`)}>店舗情報編集</Button>
          </Card>
        {/each}
      </div>
  
      <!-- 新規作成ボタン -->
      <div class="mt-6 flex justify-end">
        <Button color="light" on:click={()=>goto(`/shop/control/shoplist/regist`)}>新規作成</Button>
      </div>
    </main>
  </div>