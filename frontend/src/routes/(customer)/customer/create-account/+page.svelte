<script>
    import { Button, Label, Input } from 'flowbite-svelte';
    let email = '';
    let password = '';
</script>

<div class="flex flex-col items-center justify-center min-h-screen bg-gray-100">
    <div class="w-full max-w-md bg-white p-8 shadow-md rounded-lg">
        <h2 class="text-2xl font-bold text-center mb-6">Create an Account</h2>
        <form class="space-y-4">
            <div>
                <Label for="email" class="mb-2">Email</Label>
                <Input
                    id="email"
                    type="email"
                    bind:value={email}
                    placeholder="Enter your email"
                    required
                    class="mt-1"
                />
            </div>
            <div>
                <Label for="password" class="mb-2">Password</Label>
                <Input
                    id="password"
                    type="password"
                    bind:value={password}
                    placeholder="Enter your password"
                    required
                    class="mt-1"
                />
            </div>
            <Button type="submit" class="w-full" color="green">
                Sign up
            </Button>
        </form>
        <p class="text-sm text-center text-gray-500 mt-4">
            Already have an account? <a href="/customer/login" class="text-blue-500 hover:underline">Here to login</a>
        </p>
    </div>
</div>
