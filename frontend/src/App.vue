<template>
  <div id="app">
    <dmm-preloader></dmm-preloader>
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
import Preloader from './components/Preloader'


Vue.use(VueResource)
Vue.use(VueSession)
Vue.use(VueParallaxJs)

export default {
  name: 'App',
  components: {
    'dmm-preloader': Preloader
  }
}
</script>

<style></style>
