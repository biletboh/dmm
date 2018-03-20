<template>
  <!--========== FOOTER ==========-->
  <footer class="footer">
    <!-- Links -->
    <div class="footer-seperator">
      <div class="content-lg container">
        <div class="row">
          <div class="col-sm-7 sm-margin-b-50">
            <div class="row">
              <div class="col-sm-2 col-xs-2">
                <p class="footer-list-item">Phones</p>
              </div>
              <div class="col-sm-10 col-xs-10">
                <p class="phone"><img src="../assets/img/all/ua.svg" class="flag" alt="ua">+380442907253</p>
                <p class="phone"><img src="../assets/img/all/cy.svg" class="flag" alt="cy">+35724024408 </p>
                <p class="phone"><img src="../assets/img/all/lv.svg" class="flag" alt="lv">+37167881935 </p>
              </div>
            </div>
            <div class="row">
              <div class="col-sm-2 col-xs-2">
                <p class="footer-list-item">Email</p>
              </div>
              <div class="col-sm-10 col-xs-10">
                <p>info@dmm.solutions</p>
              </div>
            </div>
            <div class="row">
              <div class="col-sm-2 col-xs-2">
                <p class="footer-list-item">Skype</p>
              </div>
              <div class="col-sm-10 col-xs-10">
                <p>DMM Solutions</p>
              </div>
            </div>
          </div>
          <div class="col-sm-5 sm-margin-b-30">
            <h2 class="color-white">Send Us A Note</h2>
            <dmm-create-lead></dmm-create-lead>
          </div>
        </div>
        <!--// end row -->
      </div>
    </div>
    <!-- End Links -->
    <!-- Copyright -->
    <div class="content container">
      <div class="row">
        <div class="col-xs-6">
          <img class="footer-logo" src="../assets/img/logo.svg" alt="Asentus Logo">
        </div>
        <div class="col-xs-6 text-right">
          <p class="margin-b-0">
            <router-link to="/terms" class="color-base fweight-700">Terms of Use</router-link>
          </p>
          <p class="margin-b-0">

            <router-link to="/policy" class="color-base fweight-700" >Privacy Policy</router-link></p>
          </div>
        </div>
        <!--// end row -->
      </div>
      <!-- End Copyright -->
    </footer>
    <!--========== END FOOTER ==========-->
</template>

<script>
import CreateLead from './CreateLead'

export default {
  name: 'Footer',
  components: {
    'dmm-create-lead': CreateLead
  }
}
</script>

<style>
.phone{
    vertical-align: middle;
}
.flag{
    width: 20px;
    margin-top: -4px;
    margin-right: 5px;
}
</style>
