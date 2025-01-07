<script>
  import { Button, Hr, P, Heading } from 'flowbite-svelte'
</script>


<Heading tag="h1" customSize="text-5xl font-bold" class="my-12 mt-20 text-center">Thank you!!</Heading>
<div class="flex flex-col items-center mx-8 my-12">
  <Button type="submit" class="w-full m-8" size="lg" color="blue" href="">Press here to pick up</Button>
</div>
<P size=lg align="left" class="ml-8 mb-2">ご注文内容</P>
<div class="mx-8 p-4 bg-gray-300">
  <Heading tag="h2" customSize="md">購入日時</Heading>
  <P size="xl" align="left" weight="bold" class="mb-8">2024/12/18(月) 11:22</P>
  <Heading tag="h2" customSize="md">受け取り店舗</Heading>
  <P size="xl" align="left" weight="bold" class="mb-8">東京都立産業技術高等専門学校店</P>
  <Heading tag="h2" customSize="md">注文内容</Heading>
  <div class="grid md:grid-cols-4">
    <P size="xl" align="left" weight="bold" class="mb-1">唐揚げ丼: 1個</P>
    <P size="xl" align="left" weight="bold" class="mb-1">¥500</P>
  </div>
  <Hr classHr="my-1 mx-auto h-1 md:my-8 bg-black " />
  <div class="grid md:grid-cols-4">
    <P size="2xl" align="left" weight="bold" class="mb-1">合計</P>
    <P size="2xl" align="left" weight="bold" class="mb-1">¥500(税込)</P>
  </div>
</div>
