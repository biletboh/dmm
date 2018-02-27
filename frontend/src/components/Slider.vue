<template>
  <!--========== SLIDER ==========-->
  <div id="carousel-example-generic" class="carousel slide" data-ride="carousel">
    <div class="container">
      <!-- Indicators -->
      <ol class="carousel-indicators">
        <li data-target="#carousel-example-generic" data-slide-to="0" class="active"></li>
        <li data-target="#carousel-example-generic" data-slide-to="1"></li>
        <li data-target="#carousel-example-generic" data-slide-to="2"></li>
      </ol>
    </div>

    <!-- Wrapper for slides -->
    <div class="carousel-inner" role="listbox">
      <div class="item active">
        <video autoplay loop poster="../assets/img/all/poster1.jpeg">
                  <source src="../assets/video/1.mp4" type="video/mp4">
                Your browser does not support the video tag.
                </video>
        <div class="container">
          <div class="carousel-centered">
            <div class="margin-b-40">
              <h1 class="carousel-title">General Marketing <br> Strategies</h1>
              <p>DMM is a qualified support for your company at all stages of business development. <br> We offer you a profitable cooperation in marketing consulting for ICO, <br> Forex, Binary, Cloud Mining, Online Games.</p>
            </div>
            <router-link to="/product_1" class="btn-theme btn-theme-sm btn-white-brd text-uppercase">Learn more</router-link>
          </div>
        </div>
      </div>
      <div class="item">
        <video autoplay loop poster="../assets/img/all/poster2.jpeg">
                  <source src="../assets/video/2.mp4" type="video/mp4">
                Your browser does not support the video tag.
                </video>
        <div class="container">
          <div class="carousel-centered">
            <div class="margin-b-40">
              <h2 class="carousel-title">Turn-key Digital <br> Money Startups</h2>
              <p>DMM is a turn-key project management for fast results and the set objectives achievement. <br> We provide all necessary software, integrate management systems and set up <br> marketing in our service lines: ICO, Forex, Binary, Cloud Mining,
                Online Games.</p>
            </div>
            <router-link to="/product_2"  class="btn-theme btn-theme-sm btn-white-brd text-uppercase">Learn more</router-link>
          </div>
        </div>
      </div>
      <div class="item">
        <video autoplay loop poster="../assets/img/all/poster3.jpg">
                  <source src="../assets/video/3.mp4" type="video/mp4">
                Your browser does not support the video tag.
                </video>
        <div class="container">
          <div class="carousel-centered">
            <div class="margin-b-40">
              <h2 class="carousel-title">Payment Systems <br> Integration</h2>
              <p>DMM is a software solution for payment systems integration into your business in our key directions: <br> ICO, Forex, Binary, Cloud Mining, Online Games. We provide the possibility <br> of receiving payments in 4 main ways: Visa / Mastercard,
                E-wallet, Bank Transfer, Cryptocurrencies.</p>
            </div>
            <router-link to="/product_3"  class="btn-theme btn-theme-sm btn-white-brd text-uppercase">Learn more</router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!--========== SLIDER ==========-->
</template>

<script>
export default {
  name: 'Slider'
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.carousel-inner{
  height: 100vh;
  min-height: 700px;
}
.carousel-centered{
  top: 20%;
  transform: none;
}
video{
  display: block;
  margin: 0 auto 0;
}
@media only screen and (min-width: 1024px) {
  video{
    width: 100% !important;
  }
}
</style>
