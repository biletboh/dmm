// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import 'bootstrap'
import 'swiper'

require('jquery-ui')
require('./assets/vendor/simple-line-icons/simple-line-icons.min.css')
require('./assets/css/animate.css')
require('./assets/css/layout.css')
require('./assets/css/custom.css')
require('./assets/img/1920x1080/03.jpg')

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  components: { App },
  template: '<App/>'
})
