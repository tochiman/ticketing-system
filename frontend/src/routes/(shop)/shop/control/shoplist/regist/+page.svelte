<script lang="ts">
  import { Card, Button, Label, Input } from 'flowbite-svelte';
  import { goto } from '$app/navigation';
  import { getCoordinates } from '../../../../../../lib/index';

  let name: string = '';
  let email: string = '';
  let password: string = '';
  let address: string = '';
  let phone: string = '';
  let openTime: string = '';
  let closeTime: string = '';

  interface StoreData {
    name: string;
    email: string;
    password: string;
    address: string;
    phone: string;
    latitude: string;
    longitude: string;
    openTime: string;
    closeTime: string;
  }

  async function handleSubmit(): Promise<void> {
    try {
      // 住所を緯度経度に変換
      const coordinates = await getCoordinates(address);

      if (!coordinates) {
        console.log('住所の変換に失敗しました');
        alert('住所の変換に失敗しました。正しい住所を入力してください。');
        return;
      }

      console.log('変換された座標:', coordinates);

      // 電話番号からハイフンを除去
      const formattedPhone: string = phone.replace(/-/g, '');

      const storeData: StoreData = {
        name: name,
        email: email,
        password: password,
        address: address,
        phone: formattedPhone,
        latitude: coordinates.latitude.toString(),
        longitude: coordinates.longitude.toString() ,
        openTime: openTime,
        closeTime: closeTime,
      };

      // バックエンドAPIにデータを送信
      console.log('送信するデータ:', JSON.stringify(storeData));
      const response: Response = await fetch('/api/org/add_store', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(storeData),
      });
      if (response.status == 422) {
        console.log(response.json())
      }
      if (response.ok) {
        alert('店舗情報が正常に登録されました。');
        goto('/shop/control/shoplist');
      } else {
        throw new Error('店舗情報の登録に失敗しました。');
      }
    } catch (error) {
      console.error('エラー:', error);
      alert('店舗情報の登録中にエラーが発生しました。');
    }
  }
</script>

<div class="flex justify-center items-center h-screen p-4 overflow-hidden">
  <Card class="w-full max-w-md shadow-lg overflow-y-auto max-h-[90vh]">
    <h2 class="text-2xl font-bold text-center mb-4 text-gray-800">店舗情報登録</h2>
    <form class="space-y-4" on:submit|preventDefault={handleSubmit}>
      <div class="space-y-2">
        <Label for="name" class="text-sm font-medium text-gray-700">店舗名</Label>
        <Input id="name" type="text" class="w-full" placeholder="店舗名を入力してください" bind:value={name} required />
      </div>

      <div class="space-y-2">
        <Label for="email" class="text-sm font-medium text-gray-700">メールアドレス</Label>
        <Input id="email" type="email" class="w-full" placeholder="メールアドレスを入力してください" bind:value={email} required />
      </div>

      <div class="space-y-2">
        <Label for="password" class="text-sm font-medium text-gray-700">パスワード</Label>
        <Input id="password" type="password" class="w-full" placeholder="パスワードを入力してください" bind:value={password} required />
      </div>

      <div class="space-y-2">
        <Label for="address" class="text-sm font-medium text-gray-700">住所</Label>
        <Input id="address" type="text" class="w-full" placeholder="住所を入力してください" bind:value={address} required />
      </div>

      <div class="space-y-2">
        <Label for="phone" class="text-sm font-medium text-gray-700">電話番号</Label>
        <Input id="phone" type="tel" class="w-full" placeholder="電話番号を入力してください（ハイフンなし）" bind:value={phone} required />
      </div>

      <div class="grid grid-cols-2 gap-4">
        <div class="space-y-2">
          <Label for="openTime" class="text-sm font-medium text-gray-700">開店時間</Label>
          <Input id="openTime" type="time" class="w-full" bind:value={openTime} required />
        </div>
        <div class="space-y-2">
          <Label for="closeTime" class="text-sm font-medium text-gray-700">閉店時間</Label>
          <Input id="closeTime" type="time" class="w-full" bind:value={closeTime} required />
        </div>
      </div>

      <div class="flex justify-center mt-6">
        <Button type="submit" color="blue" class="px-8 py-2 text-lg font-semibold">登録</Button>
      </div>
    </form>
  </Card>
</div>
