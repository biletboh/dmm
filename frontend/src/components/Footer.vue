<template>
  <!--========== FOOTER ==========-->
  <footer class="footer">
    <!-- Links -->
    <div class="footer-seperator">
      <div class="content-lg container">
        <div class="row">
          <div class="col-sm-7 sm-margin-b-50">
            <!-- List -->
            <ul class="list-unstyled footer-list">
              <li class="footer-list-item"><a class="footer-list-link" href="#">Phone</a></li>
              <li class="footer-list-item"><a class="footer-list-link" href="#">Email</a></li>
              <li class="footer-list-item"><a class="footer-list-link" href="#">Skype</a></li>
            </ul>
            <!-- End List -->
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
          <p class="margin-b-0"><a class="color-base fweight-700" href="termsofuse.html">Terms of Use</a>
            <br> <a class="color-base fweight-700" href="privacypolicy.html">Privacy Policy</a></p>
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
<style scoped>

</style>
