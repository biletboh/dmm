<template>
  <div class="component-wrapper">
    <!--========== PARALLAX ==========-->
    <div class="parallax-window" >
      <img src="../assets/img/1920x1080/01.jpg" v-parallax="0.4" class="parallax-img" alt="">
      <div class="parallax-content container">
        <h1 class="carousel-title">Sorry, page not found</h1>
      </div>
    </div>
    <!--========== PARALLAX ==========-->
    <div class="content-lg container">
      <div class="row">
        <div class="col-sm-12">
          <h2>
            Sorry, this page doesn't exist
          </h2>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  name: 'Not_Found'

}
</script>

<style scoped>
.parallax-img{
  top: -90%;
}
</style>
