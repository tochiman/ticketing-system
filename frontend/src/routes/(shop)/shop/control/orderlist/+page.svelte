<script>
    import { Button } from 'flowbite-svelte';
    import { goto } from '$app/navigation';

    export let orders = [
      {
        id: 1,
        title: '商品A',
        price: 1000,
        status: '処理中',
      },
      {
        id: 2,
        title: '商品B',
        price: 2000,
        status: '発送済み',
      },
    ];
  </script>
  
  <div class="container mx-auto">
    <h1 class="text-3xl font-bold">オーダー一覧</h1>
    <div class="mt-4">
      {#each orders as order}
        <div class="bg-white shadow-md rounded-lg p-4 mb-4">
          <div class="flex items-center">
            <div class="flex-shrink-0">
              <img class="w-16 h-16 rounded-full" src="https://via.placeholder.com/150" alt="商品画像">
            </div>
            <div class="ml-4">
              <h2 class="text-lg font-medium">{order.title}</h2>
              <p class="text-gray-500">価格: {order.price}円</p>
              <p class="text-gray-500">ステータス: {order.status}</p>
              <Button>詳細</Button>
              <Button>削除</Button>
            </div>
          </div>
        </div>
      {/each}
    </div>
  </div>

  <Button on:click= {()=> goto ("./orderlist/qr-scan")} color="green">QRスキャン</Button>
  <Button  on:click= {()=> goto ("./orderlist/history")} color="green">履歴</Button>