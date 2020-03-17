import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store'

Vue.use(VueRouter)

const notAuthenticated = (to, from, next) => {
  if(!store.getters.isAuthenticated) {
    next()
    return
  }
  next('/')
}

const isAuthenticated = (to, from, next) => {
  if(store.getters.isAuthenticated) {
    next()
    return
  }
  next('/')
}

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue'),
    beforeEnter: notAuthenticated,
  },
  {
    path: '/clue/:clue_id',
    name: 'Clue',
    component: () => import('../views/Clue.vue'),
    beforeEnter: isAuthenticated,
  },
  {
    path: '/input/:input_id',
    name: 'Input',
    component: () => import('../views/InputPage.vue'),
    beforeEnter: isAuthenticated,
  },
  {
    path: '/input',
    name: 'Input',
    component: () => import('../views/InputPage.vue'),
    beforeEnter: isAuthenticated,
  },
  {
    path: '/newuser/:user',
    name: 'NewUser',
    component: () => import('../views/NewUser.vue'),
    beforeEnter: isAuthenticated,
  },
]

const router = new VueRouter({
  routes
})

export default router
