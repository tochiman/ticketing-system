<script>
  import { Card, Button, Label, Input } from 'flowbite-svelte';
  import { goto } from '$app/navigation';
</script>

<div class="flex justify-center items-center min-h-screen p-4">
  <Card class="w-full max-w-2xl">
    <form class="space-y-6">

      <div class="flex items-start space-x-4">
        <div class="w-24 h-24 bg-gray-200"></div>
        <div>
          <Label for="itemName">商品名</Label>
          <Input id="itemName" type="text" />
          <Label for="setumei">説明</Label>
          <Input id="setumei" type="text" />
        </div>
      </div>

      <div class="grid grid-cols-3 gap-4">
        <div>
          <Label for="arelgy">アレルギー</Label>
          <Input id="arelgy" type="text" />
        </div>
        <div>
          <Label for="size">サイズ</Label>
          <Input id="size" type="text" />
        </div>
        <div>
          <Label for="cost">値段</Label>
          <Input id="cost" type="number" />
        </div>
      </div>

      <!-- 登録ボタン -->
      <div class="flex justify-center mt-6">
        <Button color="blue" class="px-8" on:click={()=>goto(`../`)}>保存</Button>
      </div>
    </form>
  </Card>
</div>