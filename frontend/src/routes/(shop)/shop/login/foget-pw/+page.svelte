<script lang="ts">
  import { Input, Label } from 'flowbite-svelte';
  
  let username = '';
  let email = '';
  </script>
  
  <div class="max-w-md mx-auto p-6">
    <form class="flex flex-col space-y-4">
      <div>
        <Label for="username" class="mb-2">ユーザー(組織・店舗)名を入力してください。</Label>
        <Input 
          id="username"
          type="text" 
          bind:value={username}
          placeholder="Value"
          required
        />
      </div>
  
      <div>
        <Label for="email" class="mb-2">メールアドレスを入力してください。</Label>
        <Input
          id="email"
          type="email"
          bind:value={email}
          placeholder="Value" 
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