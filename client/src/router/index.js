import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue')
  },
  {
    path: '/clue/:clue_id',
    name: 'Clue',
    component: () => import('../views/Clue.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
