<template>
  <!--========== PRELOADER ==========-->
  <div id="preloader">
    <div id="status">&nbsp;</div>
  </div>
  <!--========== END PRELOADER ==========-->
</template>

<script>
export default {
  name: 'Preloader',
  el: '#preloader',
  mounted: function () {
    this.$children.fadeOut()
    this.delay(350).fadeOut('slow')
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
