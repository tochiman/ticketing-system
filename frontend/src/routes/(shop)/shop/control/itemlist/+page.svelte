<script>
  let items = [
    { name: "パン", description: "ふんわり" },
    { name: "めん", description: "もちもち" },
    { name: "ごはん", description: "説明" },
  ];

  import { Card, Button, Label, Input } from 'flowbite-svelte';
  import { goto } from '$app/navigation';
</script>

<div class="container mx-auto p-4">
  <h1 class="text-2xl font-bold mb-4">商品一覧</h1>

  <div class="mb-4">
    <input type="text" placeholder="検索" class="border border-gray-300 rounded px-3 py-2 w-full" />
  </div>

  <div class="flex flex-col gap-4">
    {#each items as item}
      <div class="bg-white rounded shadow p-4">
        <div class="flex items-center">
          <div class="w-24 h-24 bg-gray-200 rounded mr-4">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-full h-full text-gray-400">
              <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
            </svg>
          </div>
          <div>
            <h2 class="text-lg font-medium">{item.name}</h2>
            <p class="text-gray-600 text-sm">{item.description}</p>
          </div>
        </div>
        <div class="mt-4 flex justify-between">
          <Button color="blue" class="bg-gray-200 hover:bg-gray-300 text-gray-700 font-medium py-1 px-2 rounded text-sm" on:click={()=>goto(`./itemlist/detail`)}>詳細</Button>
          <label class="inline-flex items-center cursor-pointer">
            <input type="checkbox" value="" class="sr-only peer">
            <div class="float:left relative w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 dark:peer-focus:ring-blue-800 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-blue-600"></div>
            <span class="ms-3 text-sm font-medium text-gray-900 dark:text-gray-300 float:left">取り扱い</span>
          </label>


        </div>
      </div>
    {/each}
  </div>

  <div class="mt-8 text-center">
    <button class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded" on:click={()=>goto(`./itemlist/additem`)}>
      新規商品
    </button>
  </div>
</div>