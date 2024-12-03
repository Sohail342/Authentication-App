<template>
    <div class="registration-form">
      <h1>Register</h1>
      <form @submit.prevent="handleSubmit">
        <div class="form-group">
          <label for="email">Email</label>
          <input type="email" id="email" v-model="email" required />
        </div>
  
        <div class="form-group">
          <label for="name">Name</label>
          <input type="text" id="name" v-model="name" required />
        </div>
  
        <div class="form-group">
          <label for="password">Password</label>
          <input type="password" id="password" v-model="password" required />
        </div>
  
        <div class="form-group">
          <label for="password2">Confirm Password</label>
          <input type="password" id="password2" v-model="password2" required />
        </div>
  
        <div class="form-group">
          <label>
            <input type="checkbox" v-model="terms_conditions" /> I agree to the terms and conditions
          </label>
        </div>
  
        <div v-if="error" class="error-message">{{ error }}</div>
  
        <button type="submit" :disabled="loading">
          {{ loading ? "Registering..." : "Register" }}
        </button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref } from "vue";
  import user_register from '@/composables/registration';
  import { useRouter } from 'vue-router';

  const router = useRouter();
  
      const email = ref("");
      const name = ref("");
      const password = ref("");
      const password2 = ref("");
      const terms_conditions = ref(false);
  
      const { register, error, loading } = user_register();
  
      const handleSubmit = async () => {
        if (!terms_conditions.value) {
          error.value = "You must accept the terms and conditions.";
          return;
        }
  
        const message = await register(email.value, password.value, name.value, password2.value, terms_conditions.value);
  
        if (!error.value) {
          router.push("/home");
        }
      };

  </script>
  
  <style scoped>
  .registration-form {
    max-width: 400px;
    margin: auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #f9f9f9;
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  label {
    display: block;
    font-weight: bold;
    margin-bottom: 5px;
  }
  
  input[type="text"],
  input[type="email"],
  input[type="password"] {
    width: 100%;
    padding: 8px;
    margin-bottom: 5px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  button {
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    background-color: #007bff;
    color: white;
    cursor: pointer;
  }
  
  button:disabled {
    background-color: #ccc;
    cursor: not-allowed;
  }
  
  .error-message {
    color: red;
    margin-bottom: 10px;
  }
  </style>
  