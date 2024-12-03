<script>
  import { goto } from '$app/navigation'; 

  let name = '';
  let email = '';
  let phone = '';
  let password = '';
  let confirmPassword = '';

  async function handleSubmit() {
    try {
      const response = await fetch('/api/org/add_org', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        //phoneを足す
        body: JSON.stringify({ email, password, name}),
      });

      if (response.status === 401) {
        console.log('ログインに失敗しました')
        return;
      }
      goto("/shop/login");
    } catch (error) {
      console.log('ログインに失敗しました');
    }
  }
</script>

<form class="max-w-md mx-auto" on:submit|preventDefault={handleSubmit}>
  <div class="mb-6">
    <label for="organization" class="block mb-2 text-sm font-medium text-gray-900">組織名</label>
    <input
      type="text"
      id="organization"
      bind:value={name}
      class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
      required
    />
  </div>
  
  <div class="mb-6">
    <label for="email" class="block mb-2 text-sm font-medium text-gray-900">メールアドレス</label>
    <input
      type="email"
      id="email"
      bind:value={email}
      class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
      required
    />
  </div>
  
  <div class="mb-6">
    <label for="phone" class="block mb-2 text-sm font-medium text-gray-900">電話番号</label>
    <input
      type="tel"
      id="phone"
      bind:value={phone}
      class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
      required
    />
  </div>
  
  <div class="mb-6">
    <label for="password" class="block mb-2 text-sm font-medium text-gray-900">パスワード</label>
    <input
      type="password"
      id="password"
      bind:value={password}
      class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
      required
    />
  </div>
  
  <div class="mb-6">
    <label for="confirm-password" class="block mb-2 text-sm font-medium text-gray-900">パスワード（もう一度入力してください）</label>
    <input
      type="password"
      id="confirm-password"
      bind:value={confirmPassword}
      class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
      required
    />
  </div>
  
  <div class="flex gap-4">
    <button type="button" class="text-gray-900 bg-white border border-gray-300 hover:bg-gray-100 font-medium rounded-lg text-sm px-5 py-2.5 w-full">
      戻る
    </button>
    <button type="submit" class="text-white bg-blue-700 hover:bg-blue-800 font-medium rounded-lg text-sm px-5 py-2.5 w-full">
      登録
    </button>
  </div>
</form>