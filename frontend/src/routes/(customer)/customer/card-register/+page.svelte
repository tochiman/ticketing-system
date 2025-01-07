<script>
  import {Button, Label, Input, P} from 'flowbite-svelte'
</script>

<h1 class="m-6 font-bold text-3xl text-center">Adding new payment method</h1>

<div class="mb-4 mx-8">
  <Label for="card_number" class="mb-1 ml-2">Credit card number</Label>
  <Input type="text" inputmode="numeric" id="card_number" pattern={"[0-9]{4} [0-9]{4} [0-9]{4} 0-9{4}"} placeholder="1234 5678 9876 5432" required />
</div>
<div class="grid grid-6 mb-1 md:grid-cols-2">
  <div class="mb-5 mx-8">
    <Label for="expiration" class="mb-1 ml-2">Expiration</Label>
    <Input type="text" inputmode="numeric" id="expiration" pattern={"[0-9]{2}/[0-9]{2}"} placeholder="MM/YY" required />
  </div>
  <div class="mb-5 mx-8">
    <Label for="security code" class="mb-1 ml-2">CVC</Label>
    <Input type="text" inputmode="numeric" id="security code" pattern={"[0-9]{3}"} placeholder="123" required />
  </div>
</div>
<div class="mb-8 mx-8">
  <Label for="name" class="mb-4 ml-2">User's name</Label>
  <Input type="text" inputmode="text" id="name" placeholder="SANGI BAKIO" required />
</div>
<div class="flex flex-col items-center mx-8">
  <Button type="submit" class="w-full mx-8" size="lg" color="blue" href="">
    Add
  </Button>
</div>
