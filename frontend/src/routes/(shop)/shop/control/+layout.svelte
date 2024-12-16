<script lang="ts">
    import '../../../../app.css';
    import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from 'flowbite-svelte';
    import { onMount } from 'svelte';
    import { checkSession } from '../../../../lib/index';
    import { goto } from '$app/navigation';
    import { Button } from 'flowbite-svelte';
    import { org } from '../store';
    import { control } from '../store';
    import { get } from 'svelte/store';
    import { page } from '$app/stores';



    let { children } = $props();

    // loginしているかのアクセス制限
    // onMount(async () => {
    //     const isValid = await checkSession();
    //     if (!isValid) {
    //     goto('/shop/login');
    //     }
    // });  
    
    // orgかどうかでのアクセス制限
    // const currentPath = get(page).url.pathname;
    // if (currentPath.startsWith('/shop/control/shoplist')) {
    //     if (!org) {
    //         goto('/shop/control');
    //     }
    // }
    // if (currentPath.startsWith('/shop/control/org-edit')) {
    //     if (!org) {
    //         goto('/shop/control');
    //     }
    // }

    // Function to handle logout
    async function handleLogout() {
        try {
            const response = await fetch('/api/org/logout', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
            });

            if (response.ok) {
                // Navigate to the shop page after successful logout
                goto('/shop');
            } else {
                console.error('Logout failed:', response.statusText);
                // Optionally handle errors here (e.g., show a notification)
            }
        } catch (error) {
            console.error('Error during logout:', error);
            // Optionally handle errors here (e.g., show a notification)
        }
    }
</script>

<div class="relative">
    <Navbar let:hidden let:toggle>
        <NavBrand href="/">
            <span class="self-center whitespace-nowrap text-xl font-semibold dark:text-white">
                バキバキ開発部
            </span>
        </NavBrand>
                
        <NavUl {hidden}>
            <NavLi href="/shop/control">ホーム</NavLi>
            <NavLi on:click={handleLogout}>ログアウト</NavLi>
        </NavUl>
    </Navbar>
</div>

{@render children()}
