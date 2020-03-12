import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue'),
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
    meta: {
      title: 'Scavenger Hunt - Clue'
    }
  },
  {
    path: '/input/:input_id',
    name: 'Input',
    component: () => import('../views/InputPage.vue'),
    meta: {
      title: 'Scavenger Hunt - Enter Answer'
    }
  },
  {
    path: '/input',
    name: 'Input',
    component: () => import('../views/InputPage.vue'),
    meta: {
      title: 'Scavenger Hunt - Enter Answer'
    }
  },
  {
    path: '/newuser/:user',
    name: 'NewUser',
    component: () => import('../views/NewUser.vue'),
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
