<script>
    import { onMount } from 'svelte';
    import { P, Button, Label, Input, Radio } from 'flowbite-svelte';

    let selectPoint4 = "4"
    let card_register = "1"
    let card = true
</script>
<!-- <div class="flex flex-col items-center justify-center min-h-screen">
  <input id="bordered-input0" type="radio" value="" name="500yen" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600" />
  <label for="bordered-radio-1" class="w-full py-4 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">Default radio</label>
</div> -->
<h1 class="m-6 font-bold text-3xl text-center">Point Purchasement</h1>
<p class="m-6 text-lg text-center">Select a kind of points what you'd like to purchase.</p>
<div class="flex flex-col gap-6">
  <div class="border bg-white border-gray-200 rounded dark:border-gray-700">
    <Radio value="1" color="blue" class="w-full p-4" bind:group={selectPoint4}><P class="text-center w-full">500P - 500JPY</P></Radio>
  </div>
  <div class="border bg-white border-gray-200 rounded dark:border-gray-700">
    <Radio value="2" color="blue" class="w-full p-4" bind:group={selectPoint4}><P class="text-center w-full">1000P - 1000JPY</P></Radio>
  </div>
  <div class="border bg-white border-gray-200 rounded dark:border-gray-700">
    <Radio value="3" color="blue" class="w-full p-4" bind:group={selectPoint4}><P class="text-center w-full">2500P - 2500JPY</P></Radio>
  </div>
  <div class="border bg-white border-gray-200 rounded dark:border-gray-700">
    <Radio value="4" color="blue" class="w-full p-4" bind:group={selectPoint4}><P class="text-center w-full">5000P - 5000JPY</P></Radio>
  </div>
</div>

<div class="items-center flex flex-col gap-4">
  <h1 class="mt-8 mb-2 text-lg text-center">Select a payment method.</h1>
  {#if card}
  <div class="flex flex-gap-8 items-center ps-4 border bg-white border-gray-200 rounded dark:border-gray-700">
    <Radio value="card" color="blue" bind:group={card_register} class="text-center w-200 px-4"          >
    <P class="text-center w-full mr-7 py-4 ms-2 mx-8 text-lg font-large text-gray-900 dark:text-gray-300">Card1(VISA **** 0000)</P>
    </Radio>
  </div>
  {/if}
  <Button class="py-5 px-8 me-2 mb-2 text-md font-2xl text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700">
    <a href="/customer/card-register">Add a new payment method</a>
  </Button>
</div>

<Button type="submit" class="w-full py-4 my-3" size="lg" color="blue" href="">
  Purchase
</Button>
