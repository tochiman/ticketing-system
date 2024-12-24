<script>
  import { onMount } from 'svelte';
  import { Button } from 'flowbite-svelte';

  let name = '';
  let email = '';
  let phone = '';
  let password = '';

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
</script>

<form class="max-w-md mx-auto">
  <div class="mb-6">
    <label for="organization" class="block mb-2 text-sm font-medium text-gray-900">組織名</label>
    <input
      type="text"
      id="organization"
      value={name}
      class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg block w-full p-2.5"
      readonly
    />
  </div>
  
  <div class="mb-6">
    <label for="email" class="block mb-2 text-sm font-medium text-gray-900">メールアドレス</label>
    <input
      type="email"
      id="email"
      value={email}
      class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg block w-full p-2.5"
      readonly
    />
  </div>
  
  <div class="mb-6">
    <label for="phone" class="block mb-2 text-sm font-medium text-gray-900">電話番号</label>
    <input
      type="tel"
      id="phone"
      value={phone}
      class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg block w-full p-2.5"
      readonly
    />
  </div>
  
  <div class="mb-6">
    <label for="password" class="block mb-2 text-sm font-medium text-gray-900">パスワード</label>
    <input
      type="password"
      id="password"
      value={password}
      class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg block w-full p-2.5"
      readonly
    />
  </div>
  
  <div class="flex justify-center">
    <Button type="button" class="text-white bg-blue-700 hover:bg-blue-800 font-medium rounded-lg text-sm px-5 py-2.5">
      更新
    </Button>
  </div>
</form>
