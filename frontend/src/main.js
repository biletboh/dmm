// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.

/* eslint-disable */
import Vue from 'vue'
import App from './App'
import store from './store'
import router from './router'
import 'swiper'

require('jquery-ui')
require('./assets/vendor/simple-line-icons/simple-line-icons.min.css')
require('./assets/vendor/bootstrap/css/bootstrap.min.css')
require('./assets/css/animate.css')
require('./assets/css/layout.css')
require('./assets/css/custom.css')
// require('./assets/img/1920x1080/03.jpg')

Vue.config.productionTip = false

new Vue({
  el: '#app',
  store,
  router,
  components: { App },
  template: '<App/>'
})
