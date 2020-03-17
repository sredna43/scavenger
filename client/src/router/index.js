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
    meta: {
      title: 'Scavenger Hunt',
      metaTags: [
        {
          name: 'description',
          content: 'Home page of Scavenger Hunt'
        },
        {
          property: 'og:description',
          content: 'Home page of Scavenger Hunt'
        }
      ]
    }
  },
  {
    path: '/clue/:clue_id',
    name: 'Clue',
    component: () => import('../views/Clue.vue'),
    beforeEnter: isAuthenticated,
    meta: {
      title: 'Scavenger Hunt - Clue'
    }
  },
  {
    path: '/input/:input_id',
    name: 'Input',
    component: () => import('../views/InputPage.vue'),
    beforeEnter: isAuthenticated,
    meta: {
      title: 'Scavenger Hunt - Enter Answer'
    }
  },
  {
    path: '/input',
    name: 'Input',
    component: () => import('../views/InputPage.vue'),
    beforeEnter: isAuthenticated,
    meta: {
      title: 'Scavenger Hunt - Enter Answer'
    }
  },
  {
    path: '/newuser/:user',
    name: 'NewUser',
    component: () => import('../views/NewUser.vue'),
    beforeEnter: isAuthenticated,
    meta: {
      title: 'Scavenger Hunt - Welcome!'
    }
  },
]

const router = new VueRouter({
  routes
})

router.beforeEach((to, from, next) => {
  document.title = to.meta.title;
  next();
})

export default router
