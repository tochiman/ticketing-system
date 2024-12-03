<script>
  import { Button, Label, Input } from 'flowbite-svelte';
  import { goto } from '$app/navigation'; 

  let orgName = "";
  let password = "";
  let address = "";
  let contact = "";
</script>

<div class="p-6 space-y-6 bg-white">
  <!-- フォーム -->
  <form class="space-y-6">
    <div class="grid grid-cols-3 gap-6">
      <div>
        <Label for="password" class="block text-sm font-medium text-gray-700">パスワード</Label>
        <Input
          type="password"
          id="password"
          bind:value={password}
          class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
        />
      </div>
      <div>
        <Label for="address" class="block text-sm font-medium text-gray-700">住所</Label>
        <Input
          type="text"
          id="address"
          bind:value={address}
          class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
        />
      </div>
      <div>
        <Label for="contact" class="block text-sm font-medium text-gray-700">email/TEL</Label>
        <Input
          type="text"
          id="contact"
          bind:value={contact}
          class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
        />
      </div>
    </div>

    <!-- 保存ボタン -->
    <div class="flex justify-center">
      <Button
        type="submit"
        class="inline-flex justify-center py-2 px-16 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
        on:click={()=>goto(`/shop/control`)}>
        保存
      </Button>
    </div>
  </form>
</div>