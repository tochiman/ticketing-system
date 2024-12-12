<script>
  import { goto } from '$app/navigation';
  import { Button, Input, Label } from 'flowbite-svelte';
  
  let email = '';
  let password = '';
  let errorMessage = '';
  
  async function handleSubmit() {
    try {
      errorMessage = ''; // エラーメッセージをリセット
      const response = await fetch('/api/org/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password }),
      });
  
      if (response.status === 401) {
        const response2 = await fetch('/api/store/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ email, password }),
        });
  
        if (response2.status === 401) {
          errorMessage = 'ログインに失敗しました。メールアドレスとパスワードを確認してください。';
          return;
        } else if (!response2.ok) {
          throw new Error('Store login failed');
        }
      } else if (!response.ok) {
        throw new Error('Org login failed');
      }
      goto("/shop/control");
    } catch (error) {
      if (error instanceof Error) {
        errorMessage = `ログインに失敗しました。メールアドレスとパスワードを確認してください。: ${error.message}`;
      } else {
        errorMessage = `ログインに失敗しました。メールアドレスとパスワードを確認してください。: ${String(error)}`;
      }
    }
  }
  </script>
  
  <section class="bg-white dark:bg-gray-900 h-screen">
    <div class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-full lg:py-0">
      <h2 class="mb-6 text-3xl font-bold text-gray-900 dark:text-white">バキバキ開発部</h2>
      
      <form class="w-full max-w-md space-y-6" on:submit|preventDefault={handleSubmit}>
        {#if errorMessage}
          <div class="p-4 mb-4 text-sm text-red-800 rounded-lg bg-red-50 dark:bg-gray-800 dark:text-red-400" role="alert">
            {errorMessage}
          </div>
        {/if}
  
        <div>
          <Label class="block mb-2">メールアドレス</Label>
          <Input type="text" placeholder="Value" required bind:value={email}/>
        </div>
        
        <div>
          <Label class="block mb-2">パスワード</Label>
          <Input type="password" placeholder="Value" required bind:value={password}/>
        </div>
  
        <Button type="submit" class="w-full">ログイン</Button>
        
        <div class="text-center">
          <a href="/shop/login/forget-pw" class="text-sm text-blue-600 hover:underline dark:text-blue-500">
            パスワードをお忘れの方
          </a>
        </div>
        <div class="text-center">
          <a href="/shop/org-regist" class="text-sm text-blue-600 hover:underline dark:text-blue-500">
            組織の新規作成
          </a>
        </div>
      </form>
    </div>
  </section>
  