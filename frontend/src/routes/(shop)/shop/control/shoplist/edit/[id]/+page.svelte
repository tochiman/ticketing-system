
<script lang="ts">
  import { Card, Button, Label, Input } from 'flowbite-svelte';
  import { goto } from '$app/navigation';
  import type { PageData } from './$types';

  export let data: PageData;

  interface ShopData {
    name: string;
    password: string;
    address: string;
    email: string;
    phone: string;
    openTime: string;
    closeTime: string;
  }

  let shopData: ShopData = data.shopData ||{
    name: "",
    password: "",
    address: "",
    email: "",
    phone: "",
    openTime: "",
    closeTime: ""
  }; 

  let error = data.error;

  function clearField(field: keyof ShopData) {
    shopData[field] = "";
  }
  
</script>

<div class="flex justify-center items-center h-screen p-4 overflow-hidden">
  <Card class="w-full max-w-md shadow-lg overflow-y-auto max-h-[90vh]">
    <h2 class="text-2xl font-bold text-center mb-4 text-gray-800">店舗情報編集</h2>
    {#if error}
      <p class="text-red-500">{error}</p>
    {/if}
    <form class="space-y-4" on:submit>
      <div class="space-y-2">
        <Label for="name" class="text-sm font-medium text-gray-700">店舗名</Label>
        <div class="relative">
          <Input id="name" type="text" class="w-full pr-10" bind:value={shopData.name}/>
          <button type="button" class="absolute inset-y-0 right-0 pr-3 flex items-center text-gray-400 hover:text-gray-600" on:click={() => clearField('name')}>
            ✕
          </button>
        </div>
      </div>

      <div class="space-y-2">
        <Label for="password" class="text-sm font-medium text-gray-700">パスワード</Label>
        <div class="relative">
          <Input id="password" type="password" class="w-full pr-10" />
          <button type="button" class="absolute inset-y-0 right-0 pr-3 flex items-center text-gray-400 hover:text-gray-600" on:click={() => clearField('password')}>
            ✕
          </button>
        </div>
      </div>

      <div class="space-y-2">
        <Label for="address" class="text-sm font-medium text-gray-700">住所</Label>
        <div class="relative">
          <Input id="address" type="text" class="w-full pr-10" bind:value={shopData.address}/>
          <button type="button" class="absolute inset-y-0 right-0 pr-3 flex items-center text-gray-400 hover:text-gray-600" on:click={() => clearField('address')}>
            ✕
          </button>
        </div>
      </div>

      <div class="space-y-2">
        <Label for="email" class="text-sm font-medium text-gray-700">メールアドレス</Label>
        <div class="relative">
          <Input id="email" type="email" class="w-full pr-10" bind:value={shopData.email}/>
          <button type="button" class="absolute inset-y-0 right-0 pr-3 flex items-center text-gray-400 hover:text-gray-600" on:click={() => clearField('email')}>
            ✕
          </button>
        </div>
      </div>

      <div class="space-y-2">
        <Label for="phone" class="text-sm font-medium text-gray-700">電話番号</Label>
        <div class="relative">
          <Input id="phone" type="tel" class="w-full pr-10" bind:value={shopData.phone}/>
          <button type="button" class="absolute inset-y-0 right-0 pr-3 flex items-center text-gray-400 hover:text-gray-600" on:click={() => clearField('phone')}>
            ✕
          </button>
        </div>
      </div>

      <div class="grid grid-cols-2 gap-4">
        <div class="space-y-2">
          <Label for="openTime" class="text-sm font-medium text-gray-700">開店時間</Label>
          <div class="relative">
            <Input id="openTime" type="time" class="w-full pr-10" bind:value={shopData.openTime}/>
            <button type="button" class="absolute inset-y-0 right-0 pr-3 flex items-center text-gray-400 hover:text-gray-600" on:click={() => clearField('openTime')}>
              ✕
            </button>
          </div>
        </div>
        <div class="space-y-2">
          <Label for="closeTime" class="text-sm font-medium text-gray-700">閉店時間</Label>
          <div class="relative">
            <Input id="closeTime" type="time" class="w-full pr-10" bind:value={shopData.closeTime}/>
            <button type="button" class="absolute inset-y-0 right-0 pr-3 flex items-center text-gray-400 hover:text-gray-600" on:click={() => clearField('closeTime')}>
              ✕
            </button>
          </div>
        </div>
      </div>

      <div class="flex justify-center mt-6">
        <Button type="submit" color="blue" class="px-8 py-2 text-lg font-semibold">更新</Button>
      </div>
    </form>
  </Card>
</div>