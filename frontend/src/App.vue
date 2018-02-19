<template>
  <div id="app">
    <dmm-preloader></dmm-preloader>
    <dmm-header></dmm-header>
    <router-view></router-view>
    <dmm-footer></dmm-footer>
  </div>
</template>

<script>
/* eslint-disable */
import Preloader from './components/Preloader'
import Header from './components/Header'
import Footer from './components/Footer'


export default {
  name: 'App',
  components: {
    'dmm-preloader': Preloader,
    'dmm-header': Header,
    'dmm-footer': Footer,
  }
}
</script>

<style>
@import'bootstrap/dist/css/bootstrap.css'
</style>
