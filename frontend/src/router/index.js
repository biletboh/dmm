/* eslint-disable */
import Vue from 'vue'
import App from '../App'
import Router from 'vue-router'
import Home from '@/components/Home'
import Product_1 from '@/components/Product_1'
import Product_2 from '@/components/Product_2'
import Product_3 from '@/components/Product_3'
import Terms from '@/components/Terms'
import Policy from '@/components/Policy'
import Dashboard from '@/components/Dashboard'
import Landing from '@/components/Landing'
import Not_Found from '@/components/Not_Found'
import Brief from '@/components/Brief'
import Thanks from '@/components/Thanks'
import ErrorPage from '@/components/ErrorPage'
import Login from '@/components/Login'

Vue.use(Router)

export default new Router({
  // mode: 'history',
  routes: [
  {
    path: '/',
    components: { landing: Landing },
    children: [
    { path: '',          components: {sublanding: Home} },
    { path: 'product_1', components: {sublanding: Product_1} },
    { path: 'product_2', components: {sublanding: Product_2} },
    { path: 'product_3', components: {sublanding: Product_3} },
    { path: 'terms',     components: {sublanding: Terms} },
    { path: 'policy',    components: {sublanding: Policy} },
    { path: 'brief',     components: {sublanding: Brief} },
    { path: 'not-found', components: {sublanding: Not_Found} },
    { path: 'thanks',    components: {sublanding: Thanks} },
    { path: 'error',     components: {sublanding: ErrorPage} },
    { path: 'login',     components: {sublanding: Login} },
    ]
  },
  { path: '/dashboard', components: {dashboard: Dashboard} },
  { path: '*', redirect: '/not-found' }
  ],
  scrollBehavior (to, from, savedPosition) {
    return { x: 0, y: 0 }
  }
})
