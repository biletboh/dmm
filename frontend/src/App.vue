<template>
  <div id="app">
    <dmm-header></dmm-header>
    <dmm-slider></dmm-slider>
    <!--========== PAGE LAYOUT ==========-->
    <dmm-latest-products></dmm-latest-products>
    <dmm-clients></dmm-clients>
    <!--========== END PAGE LAYOUT ==========-->
    <dmm-footer></dmm-footer>
  </div>
</template>

<script>
import DmmBase from './components/DmmBase'
import Preloader from './components/Preloader'
import Header from './components/Header'
import Footer from './components/Footer'
import Slider from './components/Slider'
import LatestProducts from './components/LatestProducts'
import Clients from './components/Clients'

export default {
  name: 'App',
  components: {
    'dmm-base': DmmBase,
    'dmm-preloader': Preloader,
    'dmm-header': Header,
    'dmm-footer': Footer,
    'dmm-slider': Slider,
    'dmm-latest-products': LatestProducts,
    'dmm-clients': Clients
  }
}
</script>

<style>
@import'bootstrap/dist/css/bootstrap.css'
</style>
