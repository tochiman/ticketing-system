<script>
    import { Card, Button, Label, Input } from 'flowbite-svelte';
    import { goto } from '$app/navigation';
  
    export let items = [
      {
        name: 'パン',
        setumei: 'ユーザAの注文',
        arelgy: '小麦粉',
        size: 'S',
        cost: '500'
      },
      {
          name: 'ご飯',
          setumei: 'ユーザAの注文',
          arelgy: '米',
          size: 'M',
          cost: '300'
      }
    ];
  </script>
  
  <div class="flex justify-center items-center min-h-screen p-4">
    {#each items as item, index}
    <Card class="w-full max-w-2xl">
      <div class="space-y-6">
          <div class="flex items-start space-x-4">
            <div class="w-24 h-24 bg-gray-200"></div>
            <div>
              <h2 class="text-lg font-medium">{item.name}</h2>
              <Label for="itemName-{index}">商品名</Label>
              <h2 class="text-lg font-medium">{item.setumei}</h2>
              <Label for="setumei-{index}">説明</Label>
            </div>
          </div>
  
          <div class="grid grid-cols-3 gap-4">
            <div>
              <Label for="arelgy-{index}">アレルギー</Label>
              <h2 class="text-lg font-medium">{item.arelgy}</h2>
            </div>
            <div>
              <Label for="size-{index}">サイズ</Label>
              <h2 class="text-lg font-medium">{item.size}</h2>
            </div>
            <div>
              <Label for="cost-{index}">値段</Label>
              <h2 class="text-lg font-medium">{item.cost}</h2>
            </div>
          </div>
  
          <div class="flex justify-center mt-6">
            <Button color="blue" class="px-8" on:click={()=>goto(`./detail/edit`)}>編集</Button>
          </div>
      </div>
    </Card>
    {/each}
  </div>