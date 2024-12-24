<script lang="ts">
  import { Input, Label } from 'flowbite-svelte';
  
  let email = '';

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
  <h1>{token}</h1>
{/if}
