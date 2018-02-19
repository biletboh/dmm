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
// import Brief from '@/components/Brief'
import Dashboard from '@/components/Dashboard'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
  { path: '/', component: Home },
  { path: '/product_1', component: Product_1 },
  { path: '/product_2', component: Product_2 },
  { path: '/product_3', component: Product_3 },
  { path: '/terms', component: Terms },
  { path: '/policy', component: Policy },
    // { path: '/brief', component: Brief },
  { path: '/dashboard', component: Dashboard }

    ],
    scrollBehavior (to, from, savedPosition) {
      return { x: 0, y: 0 }
    }
  })