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
            <form id="footerForm">
              <input type="text" class="form-control footer-input margin-b-20" placeholder="Name" required>
              <input type="email" class="form-control footer-input margin-b-20" placeholder="Email" required>
              <input type="text" class="form-control footer-input margin-b-20" placeholder="Phone" required>
              <textarea class="form-control footer-input margin-b-30" rows="6" placeholder="Message" required></textarea>
              <button type="submit" class="btn-theme btn-theme-sm btn-base-bg text-uppercase">Submit</button>
            </form>
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
/* eslint-disable */
export default {
  name: 'Footer',
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
