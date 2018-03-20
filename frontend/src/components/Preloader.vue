<template>
  <!--========== PRELOADER ==========-->
  <div id="preloader" >
    <div id="status">&nbsp;</div>
  </div>
  <!--========== END PRELOADER ==========-->
</template>

<script>
/* eslint-disable */
export default {
  name: 'Preloader',
  methods:{
    initPreloader: function(){
      jQuery('#preloader').show().delay(1200).fadeOut('slow');
    }
  },
  watch: {
    '$route': function(){
      this.initPreloader();
    }
  },
    mounted(){
      window.onload = function(){
      $('#preloader').fadeOut('slow');
    }
  }
}
</script>

<style scoped>

</style>
