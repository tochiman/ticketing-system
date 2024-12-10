<script lang="ts">
	import '../../../app.css';
	import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from 'flowbite-svelte';
	let { children } = $props();
</script>


	<Navbar let:hidden let:toggle>
	  <NavBrand href="/shop">
		<img src="/images/logo.svg" class="mr-3 h-6 sm:h-9" alt="Logo" />
		<span class="self-center whitespace-nowrap text-xl font-semibold dark:text-white">
		  サイト名
		</span>
	  </NavBrand>
	
	  <NavHamburger on:click={toggle} />
	
	  <NavUl {hidden}>
		<NavLi href="/shop" >ホーム</NavLi>
		<NavLi href="/shop/logout">ログアウト</NavLi>
	  </NavUl>
	</Navbar>

{@render children()}
