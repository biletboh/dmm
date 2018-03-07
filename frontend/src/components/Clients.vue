<template>
<!-- Clients -->
  <div class="bg-color-sky-light">
    <div class="content-lg container">
      <!-- Swiper Clients -->
      <div class="swiper-slider swiper-clients">
        <!-- Swiper Wrapper -->
        <div class="swiper-wrapper">
          <div class="swiper-slide" v-for="item in clientlogos" :key="item.id">
              <img class="swiper-clients-img" :src="item.logo" alt="Clients Logo">
          </div>
        </div>
        <!-- End Swiper Wrapper -->
      </div>
      <!-- End Swiper Clients -->
    </div>
  </div>
  <!-- End Clients -->
</template>

<script>
import Swiper from 'swiper'

export default {
  name: 'Clients',
  data () {
    return {
      clientlogos: [
        { logo: require('../assets/img/clients/01.png') },
        { logo: require('../assets/img/clients/02.png') },
        { logo: require('../assets/img/clients/03.png') },
        { logo: require('../assets/img/clients/04.png') },
        { logo: require('../assets/img/clients/05.png') },
        { logo: require('../assets/img/clients/06.png') }
      ]
    }
  },
  mounted: function () {
    this.initSwiper()
  },
  methods: {
    initSwiper: function () {
      /* eslint-disable no-new */
      new Swiper('.swiper-clients', {
        slidesPerView: 5,
        spaceBetween: 50,
        loop: !0,
        breakpoints: {
          1024: {
            slidesPerView: 4,
            spaceBetween: 50
          },
          992: {
            slidesPerView: 3,
            spaceBetween: 40
          },
          768: {
            slidesPerView: 3,
            spaceBetween: 30
          },
          600: {
            slidesPerView: 2,
            spaceBetween: 30
          },
          480: {
            slidesPerView: 1,
            spaceBetween: 0
          }
        }
      })
    }
  }
}
</script>
<style scoped>
@import'swiper/dist/css/swiper.min.css'
</style>
