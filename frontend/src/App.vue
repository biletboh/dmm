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


Vue.use(VueResource)
Vue.use(VueSession)
Vue.use(VueParallaxJs)

export default {
  name: 'App'
}
</script>

<style></style>
