<template>
    <div class="flex flex-col justify-start items-center bg-gray-100 dark:bg-gray-900 h-[100vh]">
        <div
            class="mx-auto flex w-full flex-col justify-start px-5 pt-0 md:h-[unset] md:max-w-[50%] lg:h-[100vh] min-h-[100vh] lg:max-w-[50%] lg:px-6">
            
            <div class="my-auto mt-16 flex flex-col md:mt-20 w-[350px] max-w-[450px] mx-auto md:max-w-[450px] lg:mt-24 lg:max-w-[450px]">
            <p class="text-[32px] font-bold text-zinc-950 dark:text-white text-center">
                Sign In
            </p>
            <div class="relative my-4">
                <div class="relative flex items-center py-1">
                <div class="grow border-t border-zinc-300 dark:border-zinc-700"></div>
                <div class="grow border-t border-zinc-300 dark:border-zinc-700"></div>
                </div>
            </div>
            <div class="border border-zinc-300 dark:border-zinc-700 rounded-lg shadow-lg p-6 bg-white dark:bg-gray-800">
                <form @submit.prevent="handleLogin" class="mb-4">
                <div class="grid gap-4">
                    <!-- Email Field -->
                    <div class="grid gap-1">
                    <label class="text-zinc-950 dark:text-white" for="email">
                        Email
                    </label>
                    <input
                        class="h-full min-h-[44px] w-full rounded-lg border border-zinc-300 bg-white px-4 py-3 text-sm text-zinc-950 placeholder:text-zinc-400 focus:ring-2 focus:ring-blue-500 focus:outline-none dark:border-zinc-600 dark:bg-gray-700 dark:text-white dark:placeholder:text-zinc-500"
                        id="email"
                        placeholder="name@example.com"
                        type="email"
                        v-model="email"
                        autocomplete="email"
                        name="email"
                    />
                    </div>
                    <!-- Password Field -->
                    <div class="grid gap-1">
                    <label class="text-zinc-950 dark:text-white" for="password">
                        Password
                    </label>
                    <input
                        id="password"
                        placeholder="Password"
                        type="password"
                        v-model="password"
                        autocomplete="current-password"
                        class="h-full min-h-[44px] w-full rounded-lg border border-zinc-300 bg-white px-4 py-3 text-sm text-zinc-950 placeholder:text-zinc-400 focus:ring-2 focus:ring-blue-500 focus:outline-none dark:border-zinc-600 dark:bg-gray-700 dark:text-white dark:placeholder:text-zinc-500"
                        name="password"
                    />
                    </div>
                    <!-- Submit Button -->
                    <button
                    class="mt-2 flex h-[unset] w-full items-center justify-center rounded-lg bg-blue-600 px-4 py-4 text-sm font-medium text-white hover:bg-blue-700 focus:ring-2 focus:ring-blue-400 focus:outline-none transition-all"
                    type="submit"
                    :disabled="loading"
                    >
                    {{ loading ? "Logging in ": "Login" }}
                    </button>
                    <!-- Forgot Password -->
                    <div class="text-center mt-2">
                    <a href="#" class="text-sm text-blue-600 hover:underline dark:text-blue-400">
                        Forgot your password?
                    </a>
                    </div>
                </div>
                </form>
            </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import useAuth from '@/composables/useAuth';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const {login, error, loading} = useAuth();

const email = ref("");
const password = ref("");
const router = useRouter();

const handleLogin = async () => {
      const message = await login(email.value, password.value);
      if (!error.value) {
        router.push("/home")
        
      }
    };

</script>
