<template>
  <!--========== FOOTER ==========-->
  <footer class="footer">
    <!-- Links -->
    <div class="footer-seperator">
      <div class="content-lg container">
        <div class="row">
          <div class="col-sm-7 sm-margin-b-50">
            <!-- List -->
<!--             <ul class="list-unstyled footer-list">
              <li class="footer-list-item"><a class="footer-list-link" href="#">Phone </a></li>
              <li class="footer-list-item"><a class="footer-list-link" href="#">Email info@dmm.solutions</a></li>
              <li class="footer-list-item"><a class="footer-list-link" href="#">Skype</a></li>
            </ul> -->
            <!-- End List -->

            <div class="row">
              <div class="col-sm-2 col-xs-2">
                <p class="footer-list-item">Phones</p>
              </div>
              <div class="col-sm-10 col-xs-10">
                <p>5934773945738457934</p>
                <p>s74387885495734957</p>
                <p>57839458734957934875</p>
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
            <br> <router-link to="/policy" class="color-base fweight-700" >Privacy Policy</router-link></p>
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

  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style>
  </style>
