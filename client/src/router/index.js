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
  },
  {
    path: '/input/:input_id',
    name: 'Input',
    component: () => import('../views/InputPage.vue')
  },
  {
    path: '/input',
    name: 'Input',
    component: () => import('../views/InputPage.vue')
  },
  {
    path: '/newuser/:user',
    name: 'NewUser',
    component: () => import('../views/NewUser.vue')
  },
]

const router = new VueRouter({
  routes
})

export default router
