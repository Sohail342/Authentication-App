<template>
    <button class="mt-2 flex h-[unset] w-full items-center justify-center rounded-lg bg-blue-600 px-4 py-4 text-sm font-medium text-white hover:bg-blue-700 focus:ring-2 focus:ring-blue-400 focus:outline-none transition-all" @click="handleLogout">logout</button>
  </template>
  
  <script setup>
  import useAuth from '@/composables/useAuth';
  import { useRouter } from 'vue-router';
  
  // Use destructuring to get error and logout from useAuth
  const { logout, error } = useAuth();
  const router = useRouter();
  
  const handleLogout = async () => {
    await logout();
    if (!error.value) {
      router.push("/login");
    }
  };
  </script>
  