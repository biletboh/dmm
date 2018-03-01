<template>
  <div class="component-wrapper">
    <!--========== PARALLAX ==========-->
    <div class="parallax-window" >
      <img src="../assets/img/1920x1080/01.jpg" v-parallax="0.4" class="parallax-img" alt="">
      <div class="parallax-content container">
        <h1 class="carousel-title">Error!</h1>
      </div>
    </div>
    <!--========== PARALLAX ==========-->

    <div class="content-lg container">
      <div class="row margin-b-40">
        <div class="col-sm-12">
          <p class="privacy-text">
            Something went wrong, please, try later
            <br><br><br>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  name: 'Error'

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.parallax-img{
  top: -90%;
}
</style>
