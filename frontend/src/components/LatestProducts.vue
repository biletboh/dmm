<template>
  <!-- Latest Products -->
  <div class="content-lg container">
    <div class="row margin-b-40">
      <div class="col-sm-6">
        <h2>Our services</h2>
        <p>We develop and execute the best solutions of the marketing consulting for business projects in our key directions: ICO, Forex, Binary, Cloud Mining, Online Games.</p>
      </div>
    </div>
    <!--// end row -->

    <div class="row">
      <!-- Latest Products -->
      <div class="col-sm-4 sm-margin-b-50 latest-product">
        <div class="margin-b-20">
          <div class="wow zoomIn" data-wow-duration=".3" data-wow-delay=".1s">
            <img class="img-responsive" src="../assets/img/970x647/02.jpg" alt="Latest Products Image">
          </div>
        </div>
        <h4><a href="products1.html">General Marketing Strategies</a></h4>
        <p>Services for managers with the aim of implementing marketing solutions for business development and increasing sales.</p>
        <router-link to="/product_1" class="link">Read More</router-link>
      </div>
      <!-- End Latest Products -->

      <!-- Latest Products -->
      <div class="col-sm-4 sm-margin-b-50 latest-product">
        <div class="margin-b-20">
          <div class="wow zoomIn" data-wow-duration=".3" data-wow-delay=".1s">
            <img class="img-responsive" src="../assets/img/970x647/03.jpg" alt="Latest Products Image">
          </div>
        </div>
        <h4><a href="products2.html">Turn-key Digital Money Startups</a></h4>
        <p>Creation of start-ups for a thoughtful business plan, provision and development of the necessary software, integration and adjustment of marketing and management systems.</p>
        <router-link to="/product_2" class="link">Read More</router-link>
      </div>
      <!-- End Latest Products -->

      <!-- Latest Products -->
      <div class="col-sm-4 sm-margin-b-50 latest-product">
        <div class="margin-b-20">
          <div class="wow zoomIn" data-wow-duration=".3" data-wow-delay=".1s">
            <img class="img-responsive" src="../assets/img/970x647/01.jpg" alt="Latest Products Image">
          </div>
        </div>
        <h4><a href="products3 .html">Payment Systems Integration</a></h4>
        <p>Installation of 4 main payment methods: Visa / Mastercard, E-wallet, Bank transfers, Cryptocurrencies in order to simplify payment for services.</p>
        <router-link to="/product_3" class="link">Read More</router-link>
      </div>
      <!-- End Latest Products -->
    </div>
    <!--// end row -->
  </div>
  <!-- End Latest Products -->
</template>

<script>
export default {
  name: 'LatestProducts',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
