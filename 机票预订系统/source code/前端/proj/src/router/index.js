import Vue from 'vue'
import VueRouter from 'vue-router'
import Flight from '../views/Flight.vue'
import Login from '../views/Login.vue'
import Person from '../views/Person.vue'
import Inform from '../views/Inform.vue'
import Register from '../views/Register.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login
  },
  {
    path: '/Register',
    name: 'Register',
    component: Register
  },
  {
    path: '/Flight',
    name: 'Flight',
    component: Flight
  },
  {
    path: '/Book',
    name: 'Book',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "Book" */ '../views/Book.vue')
  },
  {
    path: '/Inform',
    name: 'Inform',
    component: Inform
  },
  {
    path: '/Person',
    name: 'Person',
    component: Person
  },
]

const router = new VueRouter({
  routes
})

export default router
