import { createRouter, createWebHistory } from 'vue-router';
import WishesPage from './pages/WishesPage.vue';

const routes = [
  { path: '/', name: 'Wishes', component: WishesPage }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;