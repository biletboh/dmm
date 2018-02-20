<template>
  <!--========== HEADER ==========-->
  <header v-bind:class="{ page_on_scroll: scrollPosition > 60 }" class="header navbar-fixed-top">
    <!-- Navbar -->
    <nav class="navbar" role="navigation">
      <div class="container">
        <!-- Brand and toggle get grouped for better mobile display -->
        <div class="menu-container">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".nav-collapse">
                        <span class="sr-only">Toggle navigation</span>
                        <span class="toggle-icon"></span>
                    </button>

          <!-- Logo -->
          <div class="logo">
            <router-link to="/" class="logo-wrap">
              <img class="logo-img logo-img-main" src="../assets/img/logo.svg" alt="Asentus Logo">
              <img class="logo-img logo-img-active" src="../assets/img/logo-dark.svg" alt="Asentus Logo">
            </router-link>
          </div>
          <!-- End Logo -->
        </div>

        <!-- Collect the nav links, forms, and other content for toggling -->
        <div class="collapse navbar-collapse nav-collapse">
          <div class="menu-container">
            <ul class="navbar-nav navbar-nav-right">
              <li class="nav-item"><router-link to="/brief"  class="nav-item-child nav-item-hover">SAY HELLO</router-link></li>
            </ul>
          </div>
        </div>
        <!-- End Navbar Collapse -->
      </div>
    </nav>
    <!-- Navbar -->
  </header>
  <!--========== END HEADER ==========-->
</template>

<script>
export default {
  name: 'Header',
  data: function () {
    return {scrollPosition: null}
  },
  methods: {
    updateScroll () {
      this.scrollPosition = window.scrollY
    }
  },
  mounted () {
    window.addEventListener('scroll', this.updateScroll)
  },
  destroy () {
    window.removeEventListener('scroll', this.updateScroll)
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
