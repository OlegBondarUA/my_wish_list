import { createRouter, createWebHistory } from 'vue-router'
import WishesPage from './pages/WishesPage.vue'
import ReservedWishesPage from './pages/ReservedWishesPage.vue'
import AchievedWishesPage from './pages/AchievedWishesPage.vue'
import LoginPage from './pages/LoginPage.vue'

const routes = [
  { path: '/', component: WishesPage },
  { path: '/reserved', component: ReservedWishesPage },
  { path: '/achieved', component: AchievedWishesPage },
  { path: '/login', component: LoginPage },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router