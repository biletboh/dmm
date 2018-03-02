<template>
  <div id="app">
    <router-view name="landing"></router-view>
    <router-view name="dashboard"></router-view>
  </div>
</template>

<script>
/* eslint-disable */
import Vue from 'vue'
import VueParallaxJs from 'vue-parallax-js'
import VueSession from 'vue-session'
import VueResource from 'vue-resource'

 // require('../src/assets/vendor/material/jquery-3.1.1.min.js')
 // require('../src/assets/vendor/material/bootstrap.min.js')
 // require('../src/assets/vendor/material/perfect-scrollbar.jquery.min.js')
 // require('../src/assets/vendor/material/jquery.tagsinput.js')
 // require('../src/assets/vendor/material/material.min.js')
 // require('../src/assets/vendor/material/material-dashboard.js')


Vue.use(VueResource)
Vue.use(VueSession)
Vue.use(VueParallaxJs)

export default {
  name: 'App'
}
</script>

<style></style>
