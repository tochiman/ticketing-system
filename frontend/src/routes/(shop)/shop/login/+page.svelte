<script>
  import { Button, Label, Input } from 'flowbite-svelte';
  import { goto } from '$app/navigation'; 
  let email=``
  let password=``
  async function handleSubmit() {
    console.log(`a`)
    try {
      const response = await fetch('/api/org/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password }),
      });

      if (response.status === 401) {
        console.log('ログインに失敗しました')
        return;
      }
      goto("/shop/control");
    } catch (error) {
      console.log('ログインに失敗しました');
    }
  }
  
</script>

<section class="bg-white dark:bg-gray-900 h-screen">
  <div class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-full lg:py-0">
    <h2 class="mb-6 text-3xl font-bold text-gray-900 dark:text-white">バキバキ開発部</h2>
    
    <form class="w-full max-w-md space-y-6" on:submit|preventDefault={handleSubmit}>
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
    </form>
  </div>
</section>