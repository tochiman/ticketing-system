<script>
    import { Button } from 'flowbite-svelte';
    import { goto } from "$app/navigation";
    

    const products = [
      {
        name: '商品A',
        price: 1000,
        handling: ["YES"],
      },
    ];
  </script>
  
  <div class="container mx-auto">
    <h1 class="text-3xl font-bold">商品一覧</h1>
    <div class="mt-4">
      <input type="text" placeholder="商品検索" class="border border-gray-300 p-2 rounded">
      <div class="mt-4">
        {#each products as product}
          <div class="bg-white shadow-md rounded-lg p-4 mb-4">
            <div class="flex items-center">
              <div class="flex-shrink-0">
                <img class="w-16 h-16 rounded-full" src="https://via.placeholder.com/150" alt="商品画像">
              </div>
              <div class="ml-4">
                <h2 class="text-lg font-medium">{product.name}</h2>
                <div class="flex space-x-2 mt-2">
                  {#each product.handling as handle}
                    <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700">{handle}</span>
                  {/each}
                  <Button on:click= {()=> goto ("./itemlist/detail")} >詳細</Button>
                  <Button on:click= {()=> goto ("./itemlist/edit")} >編集</Button>
                </div>
              </div>
            </div>
          </div>
        {/each}
      </div>
      <Button on:click= {()=> goto ("./itemlist/handling")} class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded">
        取扱商品
      </Button>
    </div>
  </div>