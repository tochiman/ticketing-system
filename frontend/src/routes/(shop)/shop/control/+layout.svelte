<script lang="ts">
	import '../../../../app.css';
	import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from 'flowbite-svelte';
    import { onMount } from 'svelte';
    import { checkSession} from '../../../../lib/index';
    //import { updateControlState } from '../../../../lib/index';
    import { goto } from '$app/navigation';
    import { Button } from 'flowbite-svelte';


    let { children } = $props();

// loginしているかのアクセス制限
    // onMount(async () => {
    //     const isValid = await checkSession();
    //     if (!isValid) {
    //     goto('/shop/login');
    //     }
    // });

//　戻るボタン作ろうと思ったけど難しい
    // onMount( () => {
    //     const controlState =  updateControlState();
    //     return () => {
    //     // コンポーネントがアンマウントされたときの処理
    //     };
    // });

    function goBack() {
        history.back();
    }
</script>

<div class="relative">
    <!-- {#if updateControlState()}
        <Button class="absolute top-2 left-2 z-10" color="light" on:click={goBack}>
            <span class="text-lg font-semibold">{"<<"}</span>
        </Button>
    {/if} -->

    <Navbar let:hidden let:toggle>
        <NavBrand href="/">
            <span class="self-center whitespace-nowrap text-xl font-semibold dark:text-white">
            バキバキ開発部
            </span>
        </NavBrand>
                
        <NavUl {hidden}>
            <NavLi href="/shop/control">ホーム</NavLi>
            <NavLi href="/shop/logout">ログアウト</NavLi>
        </NavUl>
    </Navbar>
</div>

{@render children()}
