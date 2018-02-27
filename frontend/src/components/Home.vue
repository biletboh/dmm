<template>
  <div>
    <dmm-slider></dmm-slider>
    <dmm-latest-products></dmm-latest-products>
    <dmm-clients></dmm-clients>
    <dmm-achievements></dmm-achievements>
  </div>
</template>

<script>
/* eslint-disable */
import Slider from '@/components/Slider'
import LatestProducts from '@/components/LatestProducts'
import Clients from '@/components/Clients'
import Achievements from '@/components/Achievements'

export default {
  name: 'Home',
  components: {
    'dmm-slider': Slider,
    'dmm-latest-products': LatestProducts,
    'dmm-clients': Clients,
    'dmm-achievements': Achievements
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
