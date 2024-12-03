<script>
   import { Button} from 'flowbite-svelte';
   import { goto } from '$app/navigation';
</script>

<style>
  .layout {
    padding: 20px;
  }
</style>

<div class="layout">
  <div class="flex justify-between items-center border-b pb-4 mb-4">
    <div>
      <img src="placeholder.png" alt="Logo" class="w-16 h-16 bg-gray-200">
      <p class="text-lg font-bold mt-2">店舗名</p>
      <span>説明</span>
    </div>
  </div>

  <div class="border rounded-md p-4">
    <table class="w-full">
      <thead>
        <tr>
          <th class="text-left">パスワード</th>
          <th class="text-left">住所</th>
          <th class="text-left">email/TEL</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td colspan="3" class="text-center py-8 text-gray-500">
            <!-- フォームエントリーのプレースホルダー -->
          </td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="flex justify-center mt-4">
    <Button class="btn bg-blue-500 text-white" on:click={()=>goto(`/shop/control/shoplist`)}>保存</Button>
  </div>
</div>