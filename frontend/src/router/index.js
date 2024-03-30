import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../views/HomePage.vue';
import UhiMap from "../views/UhiMap.vue"
import PlantPlanner from '@/views/PlantPlanner.vue';
const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: HomePage
  },
  
  {
    path: '/uhi-map',
    name: 'UhiMap',
    component: UhiMap
  },
  {
    path: '/plant-planner',
    name: 'PlantPlanner',
    component: PlantPlanner
  }
  // Add more routes for other pages
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
