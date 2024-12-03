<script lang="ts">
	import '../../../app.css';
	let { children } = $props();
</script>

	<div class="flex flex-col min-h-screen bg-gray-100">
    <!-- Header -->
    <header class="flex justify-between items-center bg-white shadow px-4 py-3">
        <!-- Points Button -->
        <button class="bg-blue-500 text-white px-4 py-2 rounded-lg text-sm">
            9,999 P
        </button>
        <!-- Notification Icon -->
        <div class="relative">
            <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-6 w-6 text-black"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
            >
                <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"
                />
            </svg>
            <span class="absolute top-0 right-0 block h-2 w-2 rounded-full bg-red-500"></span>
        </div>
    </header>

    <!-- Main Content -->
    <main class="flex-1 p-4">
        <slot />
    </main>

    <!-- Footer -->
    <footer class="bg-white shadow-t flex justify-around items-center py-2">
        <!-- Home Icon -->
        <a href="/customer" class="text-black hover:text-blue-500">
            <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-6 w-6"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
            >
                <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M3 10l9-7 9 7v11a1 1 0 01-1 1h-6a1 1 0 01-1-1v-5a1 1 0 00-1-1h-2a1 1 0 00-1 1v5a1 1 0 01-1 1H4a1 1 0 01-1-1V10z"
                />
            </svg>
        </a>
        <!-- Tasks Icon -->
        <a href="/customer/search-store" class="text-black hover:text-blue-500">
            <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-6 w-6"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
            >
                <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M9 12h6m-6 4h6m2 4h-8m-2-8h10m-5-8h2m-3 0H5a2 2 0 00-2 2v14a2 2 0 002 2h14a2 2 0 002-2V7a2 2 0 00-2-2h-6"
                />
            </svg>
        </a>
        <!-- Profile Icon -->
        <a href="/profile" class="text-black hover:text-blue-500">
            <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-6 w-6"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
            >
                <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M5.121 18.292A9 9 0 0112 4a9 9 0 016.879 14.292M9 13h6m-6 4h6"
                />
            </svg>
        </a>
    </footer>
</div>
