<template>
  <div class="component-wrapper">
    <!--========== PARALLAX ==========-->
    <div class="parallax-window" >
      <img src="../assets/img/all/poster3.jpg" v-parallax="0.4" class="parallax-img" alt="">
      <div class="parallax-content container">
        <h1 class="carousel-title">Service for effective <br>lead generation</h1>
        <p>DMM.Solutions team develops creative materials for the order to increase the number of attracted clients through various networks.</p>
      </div>
    </div>
    <!--========== PARALLAX ==========-->
    <!--========== PAGE LAYOUT ==========-->
    <!-- Our Exceptional Solutions -->
    <div class="content-lg container">
      <div class="row margin-b-40">
        <div class="col-sm-12">
          <h2>What does the service include?</h2>
          <p class="black-text">DMM offers you the development of creative materials based on your proposal.  We create various materials from start to finish for the most successful completion of the sales funnel. You can order landings, banners, pop-ups, pop-unders, HTML-templates for mailing, design, and maintenance of automatic marketing funnels.</p>
          <p class="black-text">Our team is ready to help you maximize customer interest. We also translate texts into all languages of Europe, Asia, and South America. We also improve the design of creative materials to achieve the best result. Such opportunity will significantly increase your target audience coverage. You can download our price list for translations below.</p><br>
          <div class="text-center"><a href="https://dmm.solutions/static/Translation_Price.pdf" target="_blank" class="btn-theme btn-theme-sm btn-base-bg text-uppercase">Download Price</a></div><br>
          <h2>Cooperation algorithm</h2>
          <p class="black-text">We suggest you familiarize with our scheme of work:</p>
            <img src="../assets/img/all/steps.svg"> <br><br><br>
            <p class="black-text">You come to us with your own idea, which we process, and completely immersed in the research of your scope of work. All you need to do is provide a detailed description of the product. It will be taken as base for the formation of creative materials. After that, you integrate the materials in your work and successfully generate leads, turning them into regular customers.</p>
            <div class="text-center"><router-link to="/brief"  class="btn-theme btn-theme-sm btn-base-bg text-uppercase">SAY HELLO</router-link></div>
          </div>
        </div>
        <!--// end row -->
      </div>
      <!--========== END PAGE LAYOUT ==========-->
    </div>
</template>

<script>
/* eslint-disable */
export default {
  name: 'Product_3'
}
</script>

<style scoped>
.parallax-img{
  top: -100%;
}
</style>
