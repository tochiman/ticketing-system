<script lang="ts">
  import { onMount } from 'svelte';
  import { Button, Card } from 'flowbite-svelte';
  import { goto } from '$app/navigation';
  
  interface Store {
      name: string;
      store_id: string;
  }

  let stores: Store[] = [];
  let filteredStores: Store[] = [];
  let searchTerm = '';

  onMount(async () => {
      try {
          const response = await fetch('/api/org/store_list');
          if (!response.ok) {
              throw new Error('Failed to fetch store list');
          }
          stores = await response.json();
          filteredStores = stores;
      } catch (error) {
          console.error('Error fetching store list:', error);
      }
  });

  function filterStores() {
      filteredStores = stores.filter(store => 
          store.name.toLowerCase().includes(searchTerm.toLowerCase())
      );
  }
</script>

<div class="flex">
  <main class="flex-1 p-8">
      <h1 class="text-2xl font-bold mb-6">店舗一覧</h1>
      
      <!-- 検索バー -->
      <div class="mb-6">
          <input 
              type="search" 
              class="w-full p-2 border rounded-lg" 
              placeholder="検索..." 
              bind:value={searchTerm}
              on:input={filterStores}
          >
      </div>
      
      <!-- 店舗グリッド -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {#each filteredStores as store}
              <Card>
                  <h5 class="mb-2 text-xl font-bold">{store.name}</h5>
                  <Button 
                      color="light" 
                      class="w-full" 
                      on:click={() => goto(`/shop/control/shoplist/edit/${store.store_id}`)}
                  >
                      店舗情報編集
                  </Button>
              </Card>
          {/each}
      </div>

      <!-- 新規作成ボタン -->
      <div class="mt-6 flex justify-end">
          <Button color="light" on:click={() => goto(`/shop/control/shoplist/regist`)}>新規作成</Button>
      </div>
  </main>
</div>
