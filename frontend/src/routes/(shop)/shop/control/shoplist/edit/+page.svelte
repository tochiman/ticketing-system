<script>
  import { Card, Button, Label, Input } from 'flowbite-svelte';
  import { goto } from '$app/navigation';

  // 仮のお店情報データ
  let shopData = {
    storeName: "サンプル店舗",
    password: "********", // パスワードは安全のため表示しません
    address: "東京都渋谷区○○町1-2-3",
    email: "sample@example.com",
    tel: "03-1234-5678",
    openTime: "09:00",
    closeTime: "21:00"
  };

  function handleSubmit() {
    // ここで編集された情報を送信する処理を行います（APIができた後に実装）
    console.log("編集された情報:", shopData);
    goto(`/shop/control/shoplist`);
  }
</script>

<div class="flex justify-center items-center h-screen p-4 overflow-hidden">
  <Card class="w-full max-w-md shadow-lg overflow-y-auto max-h-[90vh]">
    <h2 class="text-2xl font-bold text-center mb-4 text-gray-800">店舗情報編集</h2>
    <form class="space-y-4" on:submit|preventDefault={handleSubmit}>
      <div class="space-y-2">
        <Label for="storeName" class="text-sm font-medium text-gray-700">店舗名</Label>
        <Input id="storeName" type="text" class="w-full" bind:value={shopData.storeName} />
      </div>

      <div class="space-y-2">
        <Label for="password" class="text-sm font-medium text-gray-700">パスワード</Label>
        <Input id="password" type="password" class="w-full" bind:value={shopData.password} />
      </div>

      <div class="space-y-2">
        <Label for="address" class="text-sm font-medium text-gray-700">住所</Label>
        <Input id="address" type="text" class="w-full" bind:value={shopData.address} />
      </div>

      <div class="space-y-2">
        <Label for="email" class="text-sm font-medium text-gray-700">メールアドレス</Label>
        <Input id="email" type="email" class="w-full" bind:value={shopData.email} />
      </div>

      <div class="space-y-2">
        <Label for="tel" class="text-sm font-medium text-gray-700">電話番号</Label>
        <Input id="tel" type="tel" class="w-full" bind:value={shopData.tel} />
      </div>

      <div class="grid grid-cols-2 gap-4">
        <div class="space-y-2">
          <Label for="openTime" class="text-sm font-medium text-gray-700">開店時間</Label>
          <Input id="openTime" type="time" class="w-full" bind:value={shopData.openTime} />
        </div>
        <div class="space-y-2">
          <Label for="closeTime" class="text-sm font-medium text-gray-700">閉店時間</Label>
          <Input id="closeTime" type="time" class="w-full" bind:value={shopData.closeTime} />
        </div>
      </div>

      <div class="flex justify-center mt-6">
        <Button type="submit" color="blue" class="px-8 py-2 text-lg font-semibold">更新</Button>
      </div>
    </form>
  </Card>
</div>
