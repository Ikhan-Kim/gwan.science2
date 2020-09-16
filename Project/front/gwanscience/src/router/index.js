import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

import FaceReading from '../views/FaceReading.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/face-reading',
    name: 'FaceReading',
    component: FaceReading
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
