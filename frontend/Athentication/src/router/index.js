import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '@/views/LoginView.vue'
import HomeView from '@/views/HomeView.vue';
import UserRegistration from '@/views/UserRegistration.vue';

const isAuthenticated = localStorage.getItem("authToken");

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      name: 'login',
      component: LoginView,
    },
    {
      path: '/register',
      name: 'register',
      component: UserRegistration,
    },
    {
      path: "/home",
      name: 'home',
      component: HomeView,
      beforeEnter: (to, from, next) => {
        if (!isAuthenticated) {
          next("/login");
        } else {
          next();
        }
      },
    },
  ],
})

export default router
