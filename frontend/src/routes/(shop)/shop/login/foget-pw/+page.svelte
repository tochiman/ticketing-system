<script lang="ts">
  import { Input, Label } from 'flowbite-svelte';
  import { goto } from '$app/navigation';
  
  let email = '';
  let password = '';
  let confirmPassword = '';

  import { page } from '$app/stores';

  const token = $page.url.searchParams.get('token');

  async function handleSubmit(event: Event) {
    event.preventDefault();
    try {
      const response = await fetch('/api/org/forget_password', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email }),
      });
      if (response.ok) {
        alert('メールが送信されました。');
      } else {
        alert('エラーが発生しました。');
      }
    } catch (error) {
      console.error('エラー:', error);
      alert('エラーが発生しました。');
    }
  }

  async function handleResetPassword(event: Event) {
    event.preventDefault();
    if (password !== confirmPassword) {
      alert('パスワードが一致しません。');
      return;
    }
    try {
      const response = await fetch('/api/org/reset_password', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password, token }),
      });
      if (response.ok) {
        alert('パスワードが変更されました。');
        goto('/shop/login'); // ログインページにリダイレクト
      } else {
        alert('エラーが発生しました。');
      }
    } catch (error) {
      console.error('エラー:', error);
      alert('エラーが発生しました。');
    }
  }
</script>

{#if !token}
<div class="max-w-md mx-auto p-6">
  <form class="flex flex-col space-y-4" on:submit={handleSubmit}>
    <div>
      <Label for="email" class="mb-2">メールアドレスを入力してください。</Label>
      <Input
        id="email"
        type="email"
        bind:value={email}
        placeholder="メールアドレス" 
        required
      />
    </div>

    <button
      type="submit"
      class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
    >
      送信
    </button>
  </form>
</div>
{:else}
<div class="max-w-md mx-auto p-6">
  <form class="flex flex-col space-y-4" on:submit={handleResetPassword}>
    <div>
      <Label for="reset-email" class="mb-2">メールアドレス</Label>
      <Input
        id="reset-email"
        type="email"
        bind:value={email}
        placeholder="メールアドレス" 
        required
      />
    </div>
    <div>
      <Label for="password" class="mb-2">新しいパスワード</Label>
      <Input
        id="password"
        type="password"
        bind:value={password}
        placeholder="新しいパスワード" 
        required
      />
    </div>
    <div>
      <Label for="confirm-password" class="mb-2">パスワード（もう一度入力してください）</Label>
      <Input
        id="confirm-password"
        type="password"
        bind:value={confirmPassword}
        placeholder="パスワードを再入力" 
        required
      />
    </div>
    <button
      type="submit"
      class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
    >
      パスワードを変更
    </button>
  </form>
</div>
{/if}
