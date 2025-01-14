<script>
  import { onMount } from 'svelte';
  import { Button } from 'flowbite-svelte';
  import { goto } from '$app/navigation';

  let name = '';
  let email = '';
  let phone = '';
  let password = '';
  let new_password = '';
  let confirm_password = '';
  let error = '';

  onMount(async () => {
    try {
      const response = await fetch('/api/org/me');
      if (response.ok) {
        const orgData = await response.json();
        name = orgData.name || '';
        email = orgData.email || '';
        phone = orgData.phone || '';
        password = orgData.password || '';
      }
    } catch (error) {
      console.error('組織情報の取得に失敗しました:', error);
    }
  });

  async function handleUpdate() {
    if (new_password !== confirm_password) {
      error = '新しいパスワードが一致しません。';
      alert('パスワードが一致していません。');
      return;
    }

    try {
      const response = await fetch('/api/org/edit_org_profile', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          name,
          email,
          phone,
          password,
          new_password
        }),
      });

      if (response.ok) {
        alert('プロフィールが更新されました。');
        error = '';
        goto(`/shop/control`);
      } else {
        error = '更新に失敗しました。';
      }
    } catch (err) {
      console.error('更新中にエラーが発生しました:', err);
      error = '更新中にエラーが発生しました。';
    }
  }
</script>

<form class="max-w-md mx-auto">
  <div class="mb-6">
    <label for="organization" class="block mb-2 text-sm font-medium text-gray-900">組織名</label>
    <input
      type="text"
      id="organization"
      bind:value={name}
      class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg block w-full p-2.5"
    />
  </div>
  
  <div class="mb-6">
    <label for="email" class="block mb-2 text-sm font-medium text-gray-900">メールアドレス</label>
    <input
      type="email"
      id="email"
      bind:value={email}
      class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg block w-full p-2.5"
    />
  </div>
  
  <div class="mb-6">
    <label for="phone" class="block mb-2 text-sm font-medium text-gray-900">電話番号</label>
    <input
      type="tel"
      id="phone"
      bind:value={phone}
      class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg block w-full p-2.5"
    />
  </div>
  
  <div class="mb-6">
    <label for="password" class="block mb-2 text-sm font-medium text-gray-900">現在のパスワード</label>
    <input
      type="password"
      id="password"
      bind:value={password}
      class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg block w-full p-2.5"
    />
  </div>

  <div class="mb-6">
    <label for="new_password" class="block mb-2 text-sm font-medium text-gray-900">新しいパスワード</label>
    <input
      type="password"
      id="new_password"
      bind:value={new_password}
      class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg block w-full p-2.5"
    />
  </div>

  <div class="mb-6">
    <label for="confirm_password" class="block mb-2 text-sm font-medium text-gray-900">新しいパスワード（確認）</label>
    <input
      type="password"
      id="confirm_password"
      bind:value={confirm_password}
      class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg block w-full p-2.5"
    />
  </div>
  
  <div class="flex justify-center">
    <Button type="button" on:click={handleUpdate} class="text-white bg-blue-700 hover:bg-blue-800 font-medium rounded-lg text-sm px-5 py-2.5">
      更新
    </Button>
  </div>
</form>
