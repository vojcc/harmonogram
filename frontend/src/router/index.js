import { createRouter, createWebHistory } from 'vue-router'
import TheSchedule from '@/views/TheSchedule.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'schedule',
      component: TheSchedule,
    },
  ],
})

export default router
