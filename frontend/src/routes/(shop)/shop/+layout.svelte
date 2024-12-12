<script lang="ts">
	import '../../../app.css';
	import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from 'flowbite-svelte';
	import { page } from '$app/stores';
  
	let { children } = $props();
  </script>
  
  {#if !$page.url.pathname.startsWith('/shop/control')}
	<Navbar let:hidden let:toggle>
	  <NavBrand href="/shop">
		<img src="/images/logo.svg" class="mr-3 h-6 sm:h-9" alt="Logo" />
		<span class="self-center whitespace-nowrap text-xl font-semibold dark:text-white">
		  バキバキ開発部
		</span>
	  </NavBrand>
	</Navbar>
  {/if}
  
  {@render children()}
  