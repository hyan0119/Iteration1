import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../views/HomePage.vue';
import UhiMap from "../views/UhiMap.vue"
import PlantPlanner from '@/views/PlantPlanner.vue';
import MyPlants from '@/views/MyPlants.vue'
import InfoPage from '@/views/InfoPage.vue'
import AboutUs from '@/views/AboutUs.vue'

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
  },
  { path: '/my-plants',
    name: 'MyPlants', 
    component: MyPlants 
  },
  { path: '/info-page',
    name: 'InfoPage',
    component: InfoPage
  },
  { path: '/about-us',
    name:  'AboutUs' ,
    component: AboutUs 
  },
  // Add more routes for other pages
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
