<script lang="ts">
  import { onMount } from 'svelte';
  import { Card, Button, Label, Input } from 'flowbite-svelte';
  import { goto } from '$app/navigation';
  import { page } from '$app/stores';

  interface ShopData {
    storeName: string;
    password: string;
    address: string;
    email: string;
    tel: string;
    openTime: string;
    closeTime: string;
  }

  let shopData: ShopData = {
    storeName: "",
    password: "",
    address: "",
    email: "",
    tel: "",
    openTime: "",
    closeTime: ""
  };

  let isLoading = true;
  let error: string | null = null;

  // 型ガード関数
  function isErrorWithMessage(err: unknown): err is { message: string } {
    return typeof err === "object" && err !== null && "message" in err && typeof (err as any).message === "string";
  }

  onMount(async () => {
    const storeId = $page.params.store_id;
    try {
      const response = await fetch(`/api/org/store/${storeId}`);
      if (!response.ok) {
        throw new Error('Failed to fetch store data');
      }
      const data = await response.json();
      shopData = {
        storeName: data.storeName,
        password: "********", // パスワードは安全のため表示しません
        address: data.address,
        email: data.email,
        tel: data.tel,
        openTime: data.openTime,
        closeTime: data.closeTime
      };
    } catch (err) {
      if (isErrorWithMessage(err)) {
        error = err.message; // エラーメッセージを取得
      } else {
        error = "An unknown error occurred.";
      }
    } finally {
      isLoading = false;
    }
  });

  async function handleSubmit() {
    console.log("編集された情報:", shopData);
    goto(`/shop/control/shoplist`);
  }
</script>

<div class="flex justify-center items-center h-screen p-4 overflow-hidden">
  <Card class="w-full max-w-md shadow-lg overflow-y-auto max-h-[90vh]">
    <h2 class="text-2xl font-bold text-center mb-4 text-gray-800">店舗情報編集</h2>
    {#if isLoading}
      <p>Loading...</p>
    {:else if error}
      <p class="text-red-500">{error}</p>
    {:else}
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
    {/if}
  </Card>
</div>
