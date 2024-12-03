<script>
    import { onMount } from 'svelte';
    import { Button, Label, Input } from 'flowbite-svelte';
    import L from 'leaflet';

    let search = '';
    let map; // 地図のインスタンスを保持

    onMount(() => {
        // このコードはクライアントサイドでのみ実行される
        if (typeof window !== 'undefined') {
            map = L.map('map').setView([35.6895, 139.6917], 13); // 東京を初期表示

            // タイルレイヤーを追加
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '© OpenStreetMap contributors',
            }).addTo(map);
        }
    });
</script>

<div class="flex flex-col items-center justify-center min-h-screen bg-gray-100 space-y-4 p-4">
    <!-- 検索バー -->
    <Input
        id="search"
        type="text"
        bind:value={search}
        placeholder="Search location"
        required
        class="mt-1"
    />
    <Button on:click={() => alert(`Searching for: ${search}`)}>Search</Button>

    <!-- 地図を表示する要素 -->
    <div id="map" class="w-full h-[500px] bg-gray-200 rounded-lg shadow-lg"></div>
</div>
