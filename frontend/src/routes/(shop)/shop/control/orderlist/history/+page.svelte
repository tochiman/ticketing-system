<script>
    const items = [
      { id: 1, name: '商品A', user: 'ユーザーA' },
      { id: 2, name: '商品B', user: 'ユーザーB' },
    ];
  </script>
  
  <div class="container mx-auto">
    <table class="min-w-full">
      <thead>
        <tr>
          <th class="px-6 py-3 bg-gray-50 text-left text-xs leading-4 font-medium text-gray-500 uppercase tracking-wider">ID</th>
          <th class="px-6 py-3 bg-gray-50 text-left text-xs leading-4 font-medium text-gray-500 uppercase tracking-wider">商品名</th>
          <th class="px-6 py-3 bg-gray-50 text-left text-xs leading-4 font-medium text-gray-500 uppercase tracking-wider">ユーザー名</th>
        </tr>
      </thead>
      <tbody class="bg-white divide-y divide-gray-200">
        {#each items as item}
          <tr>
            <td class="px-6 py-4 whitespace-nowrap">{item.id}</td>
            <td class="px-6 py-4 whitespace-nowrap">{item.name}</td>
            <td class="px-6 py-4 whitespace-nowrap">{item.user}</td>
          </tr>
        {/each}
      </tbody>
    </table>
  </div>