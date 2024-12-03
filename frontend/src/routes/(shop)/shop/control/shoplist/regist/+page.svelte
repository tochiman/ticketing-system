<script>
  import { Card, Button, Label, Input } from 'flowbite-svelte';
  import { goto } from '$app/navigation';
</script>

<div class="flex justify-center items-center min-h-screen p-4">
  <Card class="w-full max-w-2xl">
    <form class="space-y-6">
      <!-- 店舗情報セクション -->
      <div class="flex items-start space-x-4">
        <div class="w-24 h-24 bg-gray-200"></div>
        <div>
          <Label for="storeName">店舗名</Label>
          <Input id="storeName" type="text" />
          <div class="mt-2 text-sm text-gray-500">説明</div>
        </div>
      </div>

      <!-- 情報入力セクション -->
      <div class="grid grid-cols-3 gap-4">
        <div>
          <Label for="password">パスワード</Label>
          <Input id="password" type="password" />
        </div>
        <div>
          <Label for="address">住所</Label>
          <Input id="address" type="text" />
        </div>
        <div>
          <Label for="contact">email/TEL</Label>
          <Input id="contact" type="text" />
        </div>
      </div>

      <!-- 登録ボタン -->
      <div class="flex justify-center mt-6">
        <Button color="blue" class="px-8" on:click={()=>goto(`/shop/control/shoplist`)}>登録</Button>
      </div>
    </form>
  </Card>
</div>